from pathlib import Path


DATASET_SPLITS = ("train", "valid", "test")
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}
DEFAULT_BOX = "0.5 0.5 0.8 0.8"
CLASS_BY_NAME = {
    "milho": 0,
    "tomate": 1,
}


def class_id_for_image(image_name: str) -> int | None:
    normalized_name = image_name.lower()
    for class_name, class_id in CLASS_BY_NAME.items():
        if class_name in normalized_name:
            return class_id
    return None


def label_has_content(label_path: Path) -> bool:
    return label_path.exists() and bool(label_path.read_text(encoding="utf-8").strip())


def process_split(project_root: Path, split: str) -> dict[str, int]:
    images_dir = project_root / "data" / split / "images"
    labels_dir = project_root / "data" / split / "labels"
    labels_dir.mkdir(parents=True, exist_ok=True)

    stats = {
        "images": 0,
        "existing_labels": 0,
        "created_labels": 0,
        "ignored_images": 0,
        "missing_images_dir": 0,
    }

    if not images_dir.exists():
        stats["missing_images_dir"] = 1
        return stats

    image_paths = sorted(
        path
        for path in images_dir.iterdir()
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
    )

    for image_path in image_paths:
        stats["images"] += 1
        label_path = labels_dir / f"{image_path.stem}.txt"

        if label_has_content(label_path):
            stats["existing_labels"] += 1
            continue

        class_id = class_id_for_image(image_path.name)
        if class_id is None:
            stats["ignored_images"] += 1
            continue

        label_path.write_text(f"{class_id} {DEFAULT_BOX}\n", encoding="utf-8")
        stats["created_labels"] += 1

    return stats


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    total = {
        "images": 0,
        "existing_labels": 0,
        "created_labels": 0,
        "ignored_images": 0,
        "missing_images_dir": 0,
    }

    print("Relatorio de labels YOLO")
    print("=" * 25)

    for split in DATASET_SPLITS:
        stats = process_split(project_root, split)
        for key, value in stats.items():
            total[key] += value

        print(f"\n{split}:")
        print(f"  imagens encontradas: {stats['images']}")
        print(f"  labels ja existentes: {stats['existing_labels']}")
        print(f"  labels criadas: {stats['created_labels']}")
        print(f"  imagens ignoradas: {stats['ignored_images']}")
        print(f"  pasta images ausente: {'sim' if stats['missing_images_dir'] else 'nao'}")

    print("\nTotal:")
    print(f"  imagens encontradas: {total['images']}")
    print(f"  labels ja existentes: {total['existing_labels']}")
    print(f"  labels criadas: {total['created_labels']}")
    print(f"  imagens ignoradas: {total['ignored_images']}")
    print(f"  pastas images ausentes: {total['missing_images_dir']}")


if __name__ == "__main__":
    main()

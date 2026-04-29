from pathlib import Path
import shutil


SPLITS = ("train", "valid", "test")
CLASSES = ("milho", "tomate")
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


def image_class(image_name: str) -> str | None:
    normalized_name = image_name.lower()
    for class_name in CLASSES:
        if class_name in normalized_name:
            return class_name
    return None


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    source_root = project_root / "data"
    target_root = project_root / "data_cnn"

    total_copied = 0
    total_ignored = 0

    for split in SPLITS:
        copied = 0
        ignored = 0
        missing_source = False
        source_images = source_root / split / "images"

        for class_name in CLASSES:
            (target_root / split / class_name).mkdir(parents=True, exist_ok=True)

        if not source_images.exists():
            missing_source = True
            print(f"{split}: pasta de origem ausente - {source_images}")
            continue

        image_paths = sorted(
            path
            for path in source_images.iterdir()
            if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
        )

        for image_path in image_paths:
            class_name = image_class(image_path.name)
            if class_name is None:
                ignored += 1
                continue

            target_path = target_root / split / class_name / image_path.name
            shutil.copy2(image_path, target_path)
            copied += 1

        total_copied += copied
        total_ignored += ignored
        print(
            f"{split}: {copied} imagens copiadas, {ignored} ignoradas, "
            f"pasta de origem ausente: {'sim' if missing_source else 'nao'}"
        )

    print(f"Total: {total_copied} imagens copiadas, {total_ignored} ignoradas")


if __name__ == "__main__":
    main()

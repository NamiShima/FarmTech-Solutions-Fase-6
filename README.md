# Fase 6 - Visao Computacional com YOLO e CNN

## Objetivo

Projeto de visao computacional para detectar e classificar duas classes:

- milho
- tomate

A entrega compara tres abordagens:

1. YOLOv5 customizado
2. YOLO padrao/pre-treinado
3. CNN treinada do zero

## Estrutura

```text
data/
  train/images e train/labels
  valid/images e valid/labels
  test/images e test/labels
  data.yaml
  data_yolov5.yaml

data_cnn/
  train/milho e train/tomate
  valid/milho e valid/tomate
  test/milho e test/tomate

notebook/
  JacquelineNanamiMatushima_rm568498_pbl_fase6.ipynb

scripts/
  criar_labels_faltantes.py
  criar_data_cnn.py

results/
  yolo_custom/
  yolo_padrao/
  cnn_do_zero/

assets/
  prints_yolo_custom/
  prints_yolo_padrao/
  prints_cnn/
```

## Dataset

O dataset YOLO possui 80 imagens no total:

| Split | Imagens | Labels |
|---|---:|---:|
| train | 64 | 64 |
| valid | 8 | 8 |
| test | 8 | 8 |

Classes:

- `0 = milho`
- `1 = tomate`

Cada imagem deve ter uma label `.txt` com o mesmo nome em sua pasta correspondente de labels.

## Como Rodar

1. Instale as dependencias:

```bash
pip install -r requirements.txt
```

2. Garanta as labels YOLO:

```bash
python scripts/criar_labels_faltantes.py
```

3. Gere a estrutura para a CNN:

```bash
python scripts/criar_data_cnn.py
```

4. Abra o notebook:

```text
notebook/JacquelineNanamiMatushima_rm568498_pbl_fase6.ipynb
```

5. Rode as celulas em ordem.

## Saidas Esperadas

- YOLO customizado: `results/yolo_custom/`
- YOLO padrao: `results/yolo_padrao/`
- CNN do zero: `results/cnn_do_zero/`
- Prints do YOLO customizado: `assets/prints_yolo_custom/`
- Prints do YOLO padrao: `assets/prints_yolo_padrao/`
- Graficos da CNN: `assets/prints_cnn/`

## Conclusao

O YOLO customizado e a abordagem mais adequada para o projeto, pois foi treinado especificamente para milho e tomate e retorna bounding boxes com localizacao e confianca. O YOLO padrao funciona como baseline, mas nao foi treinado especificamente para essas classes. A CNN do zero funciona como classificadora, mas nao localiza objetos e depende de mais dados para generalizar melhor.

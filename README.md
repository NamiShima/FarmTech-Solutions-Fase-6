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
README.md
requirements.txt
.gitignore

data/
  train/images e train/labels
  valid/images e valid/labels
  test/images e test/labels
  data.yaml
  data_yolov5.yaml

notebook/
  JacquelineNanamiMatushima_rm568498_pbl_fase6.ipynb
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

2. Abra o notebook:

[notebook/JacquelineNanamiMatushima_rm568498_pbl_fase6.ipynb](notebook/JacquelineNanamiMatushima_rm568498_pbl_fase6.ipynb)

3. Rode as celulas em ordem.

## Video

Link do video: pendente de inserir o link do YouTube nao listado.

## Saidas Esperadas

- YOLO customizado: `results/yolo_custom/`
- YOLO padrao: `results/yolo_padrao/`
- CNN do zero: `results/cnn_do_zero/`

Essas saidas sao geradas automaticamente e nao ficam versionadas no repositorio.

## Conclusao

O YOLO customizado e a abordagem mais adequada para o projeto, pois foi treinado especificamente para milho e tomate e retorna bounding boxes com localizacao e confianca. O YOLO padrao funciona como baseline, mas nao foi treinado especificamente para essas classes. A CNN do zero funciona como classificadora, mas nao localiza objetos e depende de mais dados para generalizar melhor.

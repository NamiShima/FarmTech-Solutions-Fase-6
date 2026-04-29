# FarmTech Solutions - Visao Computacional

## Objetivo

Desenvolver um projeto academico de visao computacional para detectar e classificar objetos agricolas das classes milho e tomate, utilizando o dataset fornecido e a execucao centralizada em notebook.

## Estrutura do projeto

```text
data/
notebook/
README.md
requirements.txt
```

## Dataset

O dataset esta organizado no formato YOLO e possui 80 imagens anotadas, divididas em treino, validacao e teste.

| Split | Imagens | Labels |
|---|---:|---:|
| train | 64 | 64 |
| valid | 8 | 8 |
| test | 8 | 8 |

Classes:

- `0 = milho`
- `1 = tomate`

## Como rodar

1. Instale as dependencias:

```bash
pip install -r requirements.txt
```

2. Abra o notebook:

```text
notebook/JacquelineNanamiMatushima_rm568498_pbl_fase6.ipynb
```

3. Execute as celulas em ordem.

## O que o projeto faz

O projeto treina e avalia modelos de visao computacional para identificar milho e tomate nas imagens do dataset. A execucao no notebook contempla a preparacao dos dados, o treinamento, a avaliacao e a comparacao dos resultados obtidos.

## Conclusao

O projeto atende ao objetivo academico de aplicar visao computacional em um problema agricola, utilizando um dataset anotado com duas classes e um fluxo simples de execucao por notebook. A abordagem permite avaliar a deteccao e classificacao de milho e tomate de forma direta e reprodutivel.

## Video demonstrativo

Link do video demonstrativo: inserir link aqui.

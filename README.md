# FarmTech Solutions - Visao Computacional

Projeto academico de visao computacional desenvolvido para detectar e classificar objetos agricolas em imagens, com foco nas classes **milho** e **tomate**.

A execucao do projeto e centralizada em um notebook Jupyter, facilitando a reproducao do ambiente, o treinamento dos modelos e a visualizacao dos resultados.

## Objetivo

Aplicar tecnicas de visao computacional em um cenario agricola para:

- preparar e organizar um dataset anotado;
- treinar modelos de deteccao/classificacao;
- avaliar o desempenho dos modelos;
- realizar predicoes sobre imagens de teste;
- visualizar os resultados obtidos.

## Estrutura do Projeto

```text
FarmTech-Solutions-Fase-6/
├── assets/
│   ├── prints_cnn/
│   │   ├── grafico_acuracia.png
│   │   └── grafico_loss.png
│   └── prints_yolo_padrao/
├── data/
│   ├── train/
│   │   ├── images/
│   │   └── labels/
│   ├── valid/
│   │   ├── images/
│   │   └── labels/
│   ├── test/
│   │   ├── images/
│   │   └── labels/
│   ├── data.yaml
│   └── data_yolov5.yaml
├── notebook/
│   └── JacquelineNanamiMatushima_rm568498_pbl_fase6.ipynb
├── yolov5/
├── README.md
├── requirements.txt
└── yolov8n.pt
```

## Dataset

O dataset esta no formato **YOLO** e contem **80 imagens anotadas**.

| Divisao | Imagens | Labels |
| --- | ---: | ---: |
| Treino | 64 | 64 |
| Validacao | 8 | 8 |
| Teste | 8 | 8 |

### Classes

| ID | Classe |
| ---: | --- |
| 0 | milho |
| 1 | tomate |

Cada imagem possui um arquivo `.txt` correspondente com as anotacoes no formato YOLO.

## Requisitos

- Python 3.10 ou 3.11
- Ambiente virtual Python
- Jupyter Notebook ou VS Code com suporte a notebooks

> Observacao: o uso de Python 3.12 pode causar incompatibilidades com algumas bibliotecas utilizadas no projeto.

## Configuracao do Ambiente

### 1. Acessar a pasta do projeto

```bash
cd /home/pedro-zanon/PycharmProjects/FarmTech-Solutions-Fase-6
```

### 2. Criar e ativar o ambiente virtual

```bash
python3.10 -m venv .venv
source .venv/bin/activate
```

Caso `python3.10` nao esteja disponivel, utilize uma versao compativel instalada na maquina, como `python3.11`.

### 3. Atualizar o pip

```bash
python -m pip install --upgrade pip
```

### 4. Instalar as dependencias

```bash
python -m pip install --no-cache-dir -r requirements.txt
```

O parametro `--no-cache-dir` evita problemas com pacotes antigos armazenados no cache local do `pip`.

### 5. Registrar o kernel do Jupyter

```bash
python -m pip install ipykernel
python -m ipykernel install --user --name=fase6 --display-name "Python (fase6)"
```

## Como Executar

1. Abra o notebook:

   ```text
   notebook/JacquelineNanamiMatushima_rm568498_pbl_fase6.ipynb
   ```

2. Selecione o kernel:

   ```text
   Python (fase6)
   ```

3. Execute as celulas do notebook em ordem.

## Pipeline do Projeto

O notebook executa um fluxo completo de visao computacional:

1. importacao das bibliotecas;
2. verificacao e preparacao do dataset;
3. treinamento dos modelos;
4. avaliacao por metricas;
5. predicao em imagens de teste;
6. visualizacao dos graficos e exemplos de resultado.

## Resultados Esperados

Ao final da execucao, espera-se obter:

- deteccao e classificacao das classes **milho** e **tomate**;
- metricas de avaliacao, como precisao e recall;
- graficos de treinamento da CNN;
- imagens de teste com predicoes do modelo YOLO;
- comparacao visual dos resultados obtidos.

## Arquivos de Configuracao YOLO

O projeto inclui dois arquivos de configuracao do dataset:

- `data/data.yaml`: configuracao principal para treinamento com YOLO;
- `data/data_yolov5.yaml`: configuracao especifica para uso com YOLOv5.

## Observacoes Importantes

- Execute o projeto sempre com o ambiente virtual ativado.
- Confirme se o kernel correto esta selecionado antes de rodar o notebook.
- Evite instalar dependencias usando um ambiente virtual de outro projeto.
- Caso ocorra erro de hash no `pip`, reinstale usando `--no-cache-dir`.

## Conclusao

O projeto atende ao objetivo academico de aplicar tecnicas de visao computacional em um contexto agricola. A abordagem permite treinar modelos supervisionados, avaliar desempenho e reproduzir os resultados de forma organizada.

## Video Demonstrativo

Link do video demonstrativo: inserir link aqui.

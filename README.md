# Classificação de Imagens de Raio-X de Covid-19

## Equipe
- Lucas Martins da Silva Sena


## Descrição do projeto
Este repositório contém o código-fonte e os artefatos necessários para a classificação de imagens de raio-X em duas classes: “covid” e “normal”. O objetivo é identificar automaticamente se uma imagem de raio-X pertence a um paciente com COVID-19 ou a um paciente saudável.
Objetivo: Desenvolver um classificador de imagens de raio-X usando Python.
Dataset: O conjunto de dados “Covid-19 & Normal” disponível no Kaggle


## Descrição do Descritor Implementado
Utilizei a Transformada Discreta de Wavelet (DWT) para extrair características das imagens de raio-X. A DWT permite decompor a imagem em diferentes sub-bandas de frequências, capturando tanto informações espaciais quanto frequenciais. Assim padronizei o tamanho das features para garantir consistência.

## Repositório do Projeto
[Link para o repositório do projeto](https://github.com/lukreitor/-Python---Classifica-o-de-Imagens-de-Raio-X-para-Detec-o-de-COVID-19)

## Classificador e Acurácia
Usei um classificador SVM com kernel linear. A acurácia obtida foi de  0.6785714285714286%.

## Instruções de Uso
1. Clone o repositório.
2. É necessário ir ate o site da Kaggle para baixar o dataset. [Clique aqui para baixar](https://www.kaggle.com/datasets/tarandeep97/covid19-normal-posteroanteriorpa-xrays)
3. Depois de baixar extraia a pasta covid e normal e cole na pasta data do projeto 
4. Instale as dependências com `pip install -r requirements.txt`.
5. Coloque as imagens nas pastas `data/covid` e `data/normal`.
6. Execute o script principal com `python src/main.py`.
7. Os resultados serão salvos na pasta `results`.

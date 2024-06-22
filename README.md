# Classificação de Imagens de Raio-X de Covid-19

## Equipe
- Nome do Integrante 1
- Nome do Integrante 2

## Descrição do Descritor Implementado
Utilizamos a Transformada Discreta de Wavelet (DWT) para extrair características das imagens de raio-X. A DWT permite decompor a imagem em diferentes sub-bandas de frequências, capturando tanto informações espaciais quanto frequenciais. Padronizamos o tamanho das features para garantir consistência.

## Repositório do Projeto
[Link para o repositório do projeto](https://github.com/usuario/repositorio)

## Classificador e Acurácia
Utilizamos um classificador SVM com kernel linear. A acurácia obtida foi de  0.6785714285714286%.

## Instruções de Uso
1. Clone o repositório.
2. É necessário ir ate o site da Kaggle para baixar o dataset. [Clique aqui para baixar](https://www.kaggle.com/datasets/tarandeep97/covid19-normal-posteroanteriorpa-xrays)
3. Depois de baixar extraia a pasta covid e normal e cole na pasta data do projeto 
4. Instale as dependências com `pip install -r requirements.txt`.
5. Coloque as imagens nas pastas `data/covid` e `data/normal`.
6. Execute o script principal com `python src/main.py`.
7. Os resultados serão salvos na pasta `results`.

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
Usei um classificador SVM com kernel linear. A acurácia obtida foi de  0.6785714285714286%

## Instruções de Uso
1. Clone o repositório.
2. É necessário ir ate o site da Kaggle para baixar o dataset. [Clique aqui para baixar](https://www.kaggle.com/datasets/tarandeep97/covid19-normal-posteroanteriorpa-xrays)
3. Depois de baixar extraia a pasta covid e normal, crie uma pasta data na raiz do projeto e cole as pastas covid e normal na pasta data do projeto 
4. Instale as dependências com `pip install -r requirements.txt`.
5. Coloque as imagens nas pastas `data/covid` e `data/normal`.
6. Execute o script principal com `python src/main.py`.
7. Os resultados serão salvos na pasta `results`.


## Contributors ✨

<table>
	<tr>
		<th align="center">
				<a href="https://github.com/lukreitor">
					<sub><b>Lucas Martins da Silva Sena</b></sub>
				</a>
		</th>
  	</tr>
 	<tr>
		<td align="center">
			<a href="https://github.com/lukreitor">
				<img src="https://avatars.githubusercontent.com/lukreitor" width="100px" alt="Lucas Martins da Silva Sena"/>
			</a>
		</td>
	</tr>
</table>


## Questions and Feedback

**Please contact me using one of the following:**

[<img src="https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" />](https://twitter.com/lukreitor) 
[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/lucasmartins-2001-2018/) 
[<img src = "https://img.shields.io/badge/instagram-%23E4405F.svg?&style=for-the-badge&logo=instagram&logoColor=white">](https://www.instagram.com/lucas15_m.s/) 
[<img src = "https://img.shields.io/badge/telegram-%233498DB.svg?&style=for-the-badge&logo=telegram&logoColor=white">](https://t.me/lukreitor/) 
[<img src = "https://img.shields.io/badge/facebook-%231877F2.svg?&style=for-the-badge&logo=facebook&logoColor=white">](https://www.facebook.com/profile.php?id=100008448453915) 
[<img src="https://img.shields.io/badge/DEV.TO-%230A0A0A.svg?&style=for-the-badge&logo=dev-dot-to&logoColor=white" />](https://dev.to/username)  

<p align="center">  
<hr>Developed with ❤️ in Brazil 🇮🇳 
</p>

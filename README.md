# Primeiro Bot - Web Scraping registro.com.br 
## Tecnologias utilizadas

- Python
- Selenium 
- Xlrd

## Passo a passo

1. Importar os frameworks necessários
2. Criar uma instância do browser definindo a url inicial
3. Selecionar e abrir um arquivo excel
4. Extrair os dados de pesquisa da tabela excel
5. Selecionar o campo de pesquisa na página através do ID do elemento HTML
6. Limpar o campo de pesquisa (evitando possíveis bugs)
7. Pesquisar sincronizando com os dados da tabela excel por linhas e colunas
8. Selecionar cada resultado da pesquisa através do XPATH do elemento HTML
9. Registrar os resultados em um arquivo .txt
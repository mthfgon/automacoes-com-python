# *Cotação automática do Euro em BRL via Email*

## Tecnologias utilizadas:

- Python 
- API - [Awesome API](https://docs.awesomeapi.com.br/api-de-moedas)
- Libraries/Modules- Requests, smtplib, email.message

### Passo a Passo

1. Importar biblioteca e módulos necessários
2. Consumir API através do método requests.get
3. Armazenar os dados em uma variável tranformando-os em números de ponto flutuante
4. Definir a função que enviará os resultados por email
5. Definir uma condicional onde o email será enviando apenas quando a condição for atingida
6. Testar o código
7. Fazer o deploy em um ambiente cloud
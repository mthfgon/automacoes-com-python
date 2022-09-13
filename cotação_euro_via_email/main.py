import requests
import smtplib
import email.message

# Requisitando através do módulo requests o valor do Euro-BRL

requisicao = requests.get("https://economia.awesomeapi.com.br/last/EUR-BRL")
cotacao_eur = requisicao.json()
cotacao_atualizada = float(cotacao_eur['EURBRL']['bid'])

# Criando a função que enviará email com os dados coletados via API

def enviar_email(cotacao_atualizada):
    corpo_email = f"""
    <h2>A cotação atualizada do Euro hoje é de: <b>R${cotacao_atualizada}. Aproveite!</h2>
    """

    msg = email.message.Message()
    msg['Subject'] = "O preço do Euro caiu!"
    msg['From'] = 'mthenrique1366@gmail.com'
    msg['To'] = 'mthenrique1366@gmail.com'
    password = 'khoggazdwflheqyt'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

# Definindo a condicional para o envio do email

if cotacao_atualizada < 5.20:
    enviar_email(cotacao_atualizada)

# Próximo passo será o deploy em um ambiente cloud
import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

with open('Scripts/relatorio.json', encoding='utf-8') as file:
    relatorio = json.load(file)
    mensagem_1 = relatorio[0]
    mensagem_2 = relatorio[1]
    mensagem_3 = relatorio[2]
    mensagem_4 = relatorio[3]

corpo = f'''
Titulo: {mensagem_1['titulo']} \n
Autor: {mensagem_1['autor']} \n
Mensagem: {mensagem_1['primeiro_paragrafo']} \n

Titulo: {mensagem_2['titulo']} \n
Autor: {mensagem_2['autor']} \n
Mensagem: {mensagem_3['primeiro_paragrafo']} \n

Titulo: {mensagem_3['titulo']} \n
Autor: {mensagem_3['autor']} \n
Mensagem: {mensagem_3['primeiro_paragrafo']} \n

Titulo: {mensagem_4['titulo']} \n
Autor: {mensagem_4['autor']} \n
Mensagem: {mensagem_4['primeiro_paragrafo']} \n
'''

# Informações da conta de e-mail
email_usuario = "lmsl3@aluno.ifal.edu.br"
senha = "lek@lek000%"

# Informações do destinatário
para = "lucasoares3243@gmail.com"

# Criação do objeto MIMEMultipart para a mensagem de e-mail
mensagem = MIMEMultipart()
mensagem["From"] = email_usuario
mensagem["To"] = para
mensagem["Subject"] = "Email teste"

# Adiciona o corpo da mensagem ao objeto MIMEText
corpo_mensagem = MIMEText(corpo, "plain")
mensagem.attach(corpo_mensagem)

# Autenticando e enviando o e-mail
servidor_smtp = smtplib.SMTP("smtp.gmail.com", 587)
servidor_smtp.starttls()
servidor_smtp.login(email_usuario, senha)
texto_do_email = mensagem.as_string()
servidor_smtp.sendmail(email_usuario, para, texto_do_email)
servidor_smtp.quit()

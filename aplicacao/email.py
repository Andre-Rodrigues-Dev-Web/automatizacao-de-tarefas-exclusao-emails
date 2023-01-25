#pacote email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#defini variaveis
email = 'email@gmail.com'
senha = 'senha'
servidor = 'smtp.gmail.com'
porta = 465
pasta = 'INBOX'
email_excluir = ''
#funcao para excluir emails
def excluir_email(email, senha, servidor, porta, pasta, email_excluir):
    #conectando ao servidor
    server = smtplib.SMTP_SSL(servidor, porta)
    server.login(email, senha)

    #excluindo email
    server.store(email_excluir, '+FLAGS', '\\Deleted')

    #desconectando do servidor
    server.expunge()
    server.close()

#se o email for excluido com sucesso retorna mensagem de email excluido
if excluir_email(email, senha, servidor, porta, pasta, email_excluir):
    print('Email excluido com sucesso!')
else:
    print('Erro ao excluir email!')

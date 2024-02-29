from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from decouple import config
import sys
import os

def captura_imagem(url, output_path):
    options = Options()
    options.add_argument('--headless')

    chrome_driver_path = os.environ.get('CHROMEDRIVER_PATH', 'C:\Program Files\Google\Chrome\chromedriver.exe')
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    driver.get(url)
    driver.save_screenshot(output_path)
    driver.quit()

def enviar_email(subject, body, image_path, to_email, bcc_email, smtp_server, smtp_port, smtp_user, smtp_password):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Bcc'] = bcc_email

    text = MIMEText(body)
    msg.attach(text)

    with open(image_path, 'rb') as image_file:
        image = MIMEImage(image_file.read())
    msg.attach(image)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)

    recipients = [to_email, bcc_email]
    server.sendmail(smtp_user, recipients, msg.as_string())

    server.quit()

def main():
    try:
        url, output_path, subject, body = sys.argv[1:5]

        to_email = config('TO_EMAIL')
        bcc_email = config('BCC_EMAIL')
        smtp_server = config('SMTP_SERVER')
        smtp_port = config('SMTP_PORT')
        smtp_user = config('SMTP_USER')
        smtp_password = config('SMTP_PASSWORD')

        captura_imagem(url, output_path)
        enviar_email(subject, body, output_path, to_email, bcc_email, smtp_server, smtp_port, smtp_user, smtp_password)

        print("Print capturado e e-mail enviado com sucesso!")
        print("Assunto:", subject)
        print("Corpo:", body)
        print("Caminho da imagem:", output_path)

    except (IndexError, FileNotFoundError):
        print("Erro: Forneça os argumentos corretos. Exemplo:")
        print("python nome_do_programa.py <URL> <Caminho_da_imagem> <Assunto> <Corpo>")

if __name__ == "__main__":
    main()

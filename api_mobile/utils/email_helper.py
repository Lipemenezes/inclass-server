import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(body, subject, to, email_login, email_password):
    try:
        msg = MIMEMultipart()
        msg['From'] = email_login
        msg['To'] = to
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_login, email_password)
        text = msg.as_string()
        server.sendmail(email_login, to, text)
        server.quit()
        return True, ''
    except Exception as e:
        return False, str(e)


def send_absence_email(absence, email_login, email_password):
    to = absence.student.user.email
    body = 'Voce recebeu {} falta(s) na disciplina {} na aula do dia {}. Acesse o InClass para mais detalhes.' \
        .format(absence.absence_number, absence.lecture.group.subject.name, absence.lecture.date.strftime('%d/%m/%Y'))
    subject = 'Falta {} - {}'.format(absence.lecture.date.strftime('%d/%m/%Y'), absence.lecture.group.subject.name)

    return send_email(body, subject, to, email_login, email_password)

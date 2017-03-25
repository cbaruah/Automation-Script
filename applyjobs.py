import smtplib
import csv
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

def make_email(company, position='Software Engineer Intern'):
    replacements = dict()
    replacements['[company]'] = company
    replacements['[position]'] = position
    lines = []
    with open('cover_rich.txt') as infile:
        for line in infile:
            for src, target in replacements.iteritems():
                line = line.replace(src, target)
            lines.append(line)
    return lines


def read_email():
    with open('names.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:

            name = row[0]
            email = row[2]
            company = row[4]
            print name + email + company
            send_email(email, name, company)



def send_email(email_id, recruiter_name, company):
    fromaddr = "emailID"
    toaddr = email_id

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Application for the position of Software Engineer"

    body = "Dear "+recruiter_name +",\n\n"+ ''.join(make_email(company))

    msg.attach(MIMEText(body, 'html'))

    filename = "chinmoy-latest.pdf"
    attachment = open("chinmoy-latest.pdf", "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "password")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

read_email()

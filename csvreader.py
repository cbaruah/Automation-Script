import csv

def read_email():
    with open('names.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            email = row[1]
            print name + " " + email
read_email()

## Python CSV
CSV este cel mai utilizat mijloc de exportare si importare a datelor in format spreedsheet si baze de date. Modulul CSV implementeaza clase pt citirea si scrierea datelor in format tabelar. Se pot scrie date in format dictionar cu ajutorul claselor **DictReader** si **DictWrieter**.

Citirea dintr-un fisier csv:

    import csv

    with open('formular.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print ', '.join(row)


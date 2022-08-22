import argparse

from revolut import RevolutCsvReader
from mt940 import Mt940Writer


INPUTNAMEFILE = "monthly-statement_01-Jun-2022_30-Jun-2022"
INPUTEXT = ".csv"
OUTPUTEXT = ".940"

INPUTFILE = './Input/' + INPUTNAMEFILE + INPUTEXT
OUTPUTFILE = './Output/' + INPUTNAMEFILE + OUTPUTEXT

IBAN = 'GB06 REVO 0099 6937 2376 70'


def main():

    with open(INPUTFILE, 'r') as f:
        text = f.read()

        converted_text = text.replace('""', '"')

    with open(INPUTFILE, 'w') as f:
        f.write(converted_text)

    reader = RevolutCsvReader(INPUTFILE)

    with Mt940Writer(OUTPUTFILE, IBAN) as writer:
        transactions = reader.get_all_transactions()
        for transaction in transactions:
            writer.write_transaction(transaction)

        print('Wrote {} transactions to file: {}.'.format(len(transactions), OUTPUTFILE))


if __name__ == "__main__":
    main()

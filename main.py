import argparse

from revolut import RevolutCsvReader
from mt940 import Mt940Writer


INPUTFILE = 'C:/Users/benja/Documents/GitHub/revolut-to-mt940/Input/input.csv'
OUTPUTFILE = 'C:/Users/benja/Documents/GitHub/revolut-to-mt940/Output/output.940'

IBAN = 'GB06 REVO 0099 6937 2376 70'

def main():

    with open('./Input/input.csv', 'r') as f:
        text = f.read()

        converted_text = text.replace('""', '"')

    with open('./Input/input.csv', 'w') as f:
        f.write(converted_text)

    reader = RevolutCsvReader(INPUTFILE)

    with Mt940Writer(OUTPUTFILE, IBAN) as writer:
        transactions = reader.get_all_transactions()
        for transaction in transactions:
            writer.write_transaction(transaction)

        print('Wrote {} transactions to file: {}.'.format(len(transactions), OUTPUTFILE))


if __name__ == "__main__":
    main()

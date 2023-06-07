
import shelve
import sys


class DatabaseApi:

    try:
        database = shelve.open('database')
    except FileExistsError:
        print("database exists")

    def parse(self, barcode):
        container_number = 1
        self.database[barcode] = dict(count=0, name=f'refill_container{container_number}')
        container_number += 1
        self.database['sales'] = 0

    @staticmethod
    def fetch(barcode):
        database = shelve.open('database', writeback=True)
        database[str(barcode)]['count'] += 1
        barcode_data = database.get(str(barcode))
        return barcode_data


if __name__ == '__main__':
    db = DatabaseApi()
    while True:
        inp = input('barcode to save')
        if inp == 'do':
            db.database.close()
            break
        db.parse(str(inp))
    while True:
        inpt = input('enter barcodes')
        if inpt == 'exit':
            break
        try:
            print(db.fetch(inpt))
        except KeyError:
            print('scan again')
            print()
            continue
    sys.exit(25)

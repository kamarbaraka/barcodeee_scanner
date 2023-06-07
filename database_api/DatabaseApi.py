import shelve
import sys


class DatabaseApi:

    try:
        file = shelve.open('database')
        database = {}
    except FileExistsError:
        print("database exists")

    def parse(self, barcode):
        self.database[barcode] = dict(count=0, type_of_material='plastic')
        self.database['sales'] = 0
        self.file.close()

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
            continue
    sys.exit(25)


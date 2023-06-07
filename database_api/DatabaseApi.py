import shelve
import sys


class DatabaseApi:

    try:
        database = shelve.open('database')
        #database = {}
    except FileExistsError:
        print("database exists")

    def parse(self, barcode):
        self.database[barcode] = dict(count=0)
        self.database['sales'] = 0


    @staticmethod
    def fetch(barcode):
        database = shelve.open('database', writeback=True)
        #print(database)
        database[str(barcode)]['count'] += 1
        barcode_data = database.get(str(barcode))
        #print(barcode_data)
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


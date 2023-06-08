
import shelve
import sys
import datetime


class DatabaseApi:
    __container_number = 1
    __total_reuse = 0
    __total_kgs = 0

    try:
        database = shelve.open('database')
    except FileExistsError:
        print("database exists")

    def parse(self, barcode):
        self.database[barcode] = dict(count=0, name=self.__container_number, month=datetime.datetime.now().month,
                                      kg=0)
        self.__container_number += 1
        self.database['monthly_reuse'] = 0
        self.database['total_reuse'] = self.__total_reuse
        self.database['total_kgs_saved'] = self.__total_kgs

    @staticmethod
    def set_kg(barcode, kg):
        database = shelve.open('database', writeback=True)
        database[str(barcode)]['kg'] = int(kg)

    @staticmethod
    def fetch(barcode):
        database = shelve.open('database', writeback=True)
        database[str(barcode)]['count'] += 1
        if database[str(barcode)]['month'] != datetime.datetime.now().month:
            database['monthly_reuse'] = 0
        database['monthly_reuse'] += 1
        database['total_reuse'] += 1
        database['total_kgs_saved'] += (int(database[str(barcode)]['count']) * int(database[str(barcode)]['kg']))
        barcode_data = {str(barcode): database.get(str(barcode)), 'monthly_reuse': database.get('monthly_reuse'),
                        'total_reuse': database.get('total_reuse'), 'total_kgs_saved': database['total_kgs_saved']}
        return barcode_data


if __name__ == '__main__':
    db = DatabaseApi()
    while True:
        inp = input('scan barcode to save, type "do" when done \n')
        if inp == 'do':
            db.database.close()
            break
        db.parse(str(inp))
    while True:
        inpt = input('scan barcodes, type "exit" to exit or "kgs" to input kgs \n')
        if inpt == 'exit':
            break
        if inpt == 'kgs':
            while True:
                input_code = input('scan the item to insert kgs, type "do" when done\n')
                if input_code == 'do':
                    break
                input_kg = input('enter the kg to input, type "do" when done \n')
                if input_kg == 'do':
                    break
                db.set_kg(input_code, input_kg)
        try:
            print(db.fetch(inpt))
        except KeyError:
            print('scan again')
            continue
    sys.exit(25)

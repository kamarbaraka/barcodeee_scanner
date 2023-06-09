
import shelve
import sys
import random
import barcode as bc
import datetime
import pandas


class DatabaseApi:
    __container_number = 1
    __total_reuse = 0
    __total_kgs = 0.0
    __class_count = 0
    count = 0

    try:
        database = shelve.open('database', writeback=True)
    except FileExistsError:
        print("database exists")

    def parse_excel(self, excel_doc):
        sheet = pandas.read_excel(excel_doc, sheet_name='Sheet1')
        record = sheet.to_dict(orient='records')
        key_list = []
        value_list = []

        for each_dict in record:
            key_list.append(str(each_dict['barcodes']))
            value_list.append(each_dict['Weight(kgs)'])

        item_dict = dict(zip(key_list, value_list))

        for k, v in item_dict:
            self.set_kg(int(k), v)

    @staticmethod
    def report(output_file):
        database_shelve = shelve.open('database', writeback=True)
        record = database_shelve['report']
        print(f'report {record}')
        data_frame = pandas.DataFrame.from_dict(record)
        print(f'report {data_frame}')
        data_frame.to_excel(output_file)

    def parse(self, barcode):
        if self.__class_count == 0:
            self.database['report'] = []
            report = {'Name': str(barcode), 'Reuse Count': 0, 'Weight(kg)': 0.0, 'Total Weight Saved': 0.0}
            self.database['report'].append(report)
            self.__class_count += 1
            self.database[str(barcode)] = dict(barcode=barcode, count=0, name=self.__container_number,
                                               month=datetime.datetime.now().month, kg=0.0)
            self.__container_number += 1
            self.database['monthly_reuse'] = 0
            self.database['total_reuse'] = self.__total_reuse
            self.database['total_kgs_saved'] = self.__total_kgs
            print(f'parse1 {self.database["report"]}')
            return 'ok'

        self.database[str(barcode)] = dict(barcode=barcode, count=0, name=self.__container_number,
                                           month=datetime.datetime.now().month, kg=0.0)
        report = {'Name': str(barcode), 'Reuse Count': 0, 'Weight(kg)': 0.0, 'Total Weight Saved': 0.0}
        self.database['report'].append(report)
        self.__container_number += 1
        self.database['monthly_reuse'] = 0
        self.database['total_reuse'] = self.__total_reuse
        self.database['total_kgs_saved'] = self.__total_kgs
        print(f'parse {self.database["report"]}')
        return 'ok'

    @staticmethod
    def set_kg(barcode, kg):
        database = shelve.open('database', writeback=True)
        database[str(barcode)]['kg'] = float(kg)
        database['total_kgs_saved'] += (float(database[str(barcode)]['count']) * float(database[str(barcode)]['kg']))
        for dic in database['report']:
            if dic['Name'] == str(barcode):
                dic['Weight(kg)'] = kg
        print(f'set_kg {database["report"]}')

    @staticmethod
    def fetch(barcode):
        database = shelve.open('database', writeback=True)
        database[str(barcode)]['count'] += 1
        for dic in database['report']:
            if dic['Name'] == str(barcode):
                dic['Reuse Count'] += 1
                dic['Total Weight Saved'] += float(database[str(barcode)]['kg'])
        if database[str(barcode)]['month'] != datetime.datetime.now().month:
            database['monthly_reuse'] = 0
        database['monthly_reuse'] += 1
        database['total_reuse'] += 1
        database['total_kgs_saved'] += float(database[str(barcode)]['kg'])
        barcode_data = {str(barcode): database.get(str(barcode)), 'monthly_reuse': database.get('monthly_reuse'),
                        'total_reuse': database.get('total_reuse'), 'total_kgs_saved': database['total_kgs_saved']}
        print(f'fetch {database["report"]}')
        return barcode_data

    def generate(self, count):
        self.count = count
        lis_of_codes = self.__generator()
        for code in lis_of_codes:
            self.parse(code)

    def __generator(self):
        n = 0
        codes = []
        for counts in range(1, self.count+1):
            random_number = random.randint(100000000000, 999999999999)
            bark = bc.EAN13(str(random_number))
            svg = bark.save(f'./barcodes/qrcode{n}')
            n += 1
            codes.append(random_number)
        return codes


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
    db.report('out_test.xlsx')
    sys.exit(25)

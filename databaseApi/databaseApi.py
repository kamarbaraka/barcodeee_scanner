import shelve
import sys

# import EAN13 from barcode module
from barcode import *
import random
import barcode_save as barcode_save 

  
# import ImageWriter to generate an image file
from barcode.writer import ImageWriter


class DatabaseApi:
    container_number = 1

    

    try:
        database = shelve.open('./database/database')
    except FileExistsError:
        print("database exists")

    def parse(self, barcode):
        self.database[barcode] = dict(count=0, name=self.container_number)
        self.container_number += 1
        # self.database['sales'] = 0

    @staticmethod
    def fetch(barcode):
        database = shelve.open('./database/database', writeback=True)
        database[str(barcode)]['count'] += 1
        barcode_data = database.get(str(barcode))
        return barcode_data
    
    def generate(self, count):
        self.count =  count
        return self.__generator()

    def __generator(self):
        n = 0
        codes = []
        for i in range(1, self.count+1):
            random_number = random.randint(1000000000, 9999999999)
            bark = Code128(str(random_number), writer=ImageWriter())
            bark.save(f"barcode_images/{n}")
            codes.append(str(random_number))
            n += 1
        return codes


if __name__ == '__main__':
    db = DatabaseApi()
    
    while True:
        # bs = barcode_save.main()

        # inp = db.generate(bs)
        inp =input("enter code")
        # for i in inp:
        #     db.parse(str(i))
        if inp == 'done':
            db.database.close()
            break
        db.parse(str(inp))

    sys.exit(0)
    # while True:
    #     inpt = input('enter barcodes')
    #     if inpt == 'exit':
    #         break
    #     try:
    #         print(db.fetch(inpt))
    #     except KeyError:
    #         print('scan again')
    #         print()
    #         continue

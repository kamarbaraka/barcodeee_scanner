
import threading
import Gui
import DatabaseApi


class Interface:
    def __int__(self):
        pass

    @staticmethod
    def save_data(barcode):
        barcode = str(barcode)
        database = DatabaseApi.DatabaseApi()
        database.parse(barcode)
        database.database.close()

    @staticmethod
    def fetch_data(barcode):
        database = DatabaseApi.DatabaseApi()
        barcode_data = database.fetch(barcode)
        return barcode_data

    @staticmethod
    def run():
        while True:
            inpt = input('barcodes to save')
            if inpt == 'do':
                break
            Interface.save_data(inpt)

    @staticmethod
    def run2():
        while True:
            inpt = input('enter barcodes')
            if inpt == 'exit':
                break
            data = Interface.fetch_data(inpt)
            disp = Gui.ShowDataset()
            disp.output(data['count'])
            disp.init()


if __name__ == '__main__':
    t1 = threading.Thread(target=Interface.run())
    #t2 = threading.Thread(target=Interface.run2())
    t1.start()
    Interface.run2()

    #t1.join()

    print('done')


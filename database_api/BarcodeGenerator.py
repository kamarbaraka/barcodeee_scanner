import barcode
import random


class BarcodeGenerator:
    count = 0

    def generate(self, count):
        self.count = count
        return self.__generator()

    def __generator(self):
        n = 0
        codes = []
        for counts in range(1, self.count+1):
            random_number = random.randint(100000000000, 999999999999)
            bark = barcode.EAN13(str(random_number))
            svg = bark.save(f'./barcodes/qrcode{n}')
            n += 1
            codes.append(random_number)
        return codes


if __name__ == '__main__':
    gen = BarcodeGenerator()
    print(gen.generate(20))

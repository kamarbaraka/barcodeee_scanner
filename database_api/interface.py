import shelve


def save(barcode):
    data = shelve.open()
def fetch(barcode):
    database = shelve.open('database')
    database[str(barcode)]['count'] += 1
    #database['sales'] += 1
    barcode_data = database.get(str(barcode))
    database.sync()
    return barcode_data

fetch(123456789)
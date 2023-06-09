import pandas, shelve


def test(excel_doc):
    sheet = pandas.read_excel(excel_doc, sheet_name='Sheet1')
    record = sheet.to_dict(orient='records')
    key_list = []
    value_list = []

    for each_dict in record:
        key_list.append(str(each_dict['barcodes']))
        value_list.append(each_dict['Weight(kgs)'])

    item_dict = dict(zip(key_list, value_list))

    print(f'{key_list}\n{value_list}\n')
    print(item_dict)


test('out.xlsx')

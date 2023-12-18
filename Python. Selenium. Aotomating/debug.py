data1 = ['Downloads', 'Word File.doc', 'Excel File.doc']
data2 = ['downloads', 'wordFile', 'excelFile']

print(str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower())

data1 = str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower()
data2 = str(data2).replace(' ', '').lower()

assert data1 == data2

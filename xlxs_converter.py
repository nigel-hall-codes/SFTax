import xlrd
import csv
import os

def csv_from_excel(xlsx):

    year = xlsx[-14:-5]
    print(year)
    sheet_name = "Roll Data {}".format(year)
    file_name = "roll_data_{}.csv".format(year)
    print(sheet_name)
    print(file_name)
    wb = xlrd.open_workbook(xlsx)
    sh = wb.sheet_by_index(0)
    print(wb.sheets())
    csv_file_dir = "/Users/nigel/SFPropertyTax/data/"
    your_csv_file = open((csv_file_dir + file_name), 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()

# runs the csv_from_excel function:
dir_path = "/Users/nigel/SFPropertyTax/xlsx_files/"
for file in os.listdir(dir_path):
    csv_from_excel(dir_path + file)



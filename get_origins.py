import os
import csv
import xlsxwriter
import sys
import xml.etree.ElementTree as ET

from classes.quota_order_number import QuotaOrderNumber


def process_null(elem):
    if elem is None:
        return None
    else:
        return elem.text


quota_order_numbers = []
IMPORT_FOLDER = "/Users/matt.admin/sites and projects/1. Online Tariff/download CDS files/resources/xml"
path = os.walk(IMPORT_FOLDER)
file_array = []
for root, directories, files in path:
    for file in files:
        file_array.append(file)


done = False
file_array.sort(reverse=False)
for file in file_array:
    if ".xml" in file:
        print("File {}".format(file))
        import_path_and_file = os.path.join(IMPORT_FOLDER, file)
        tree = ET.parse(import_path_and_file)
        root_node = tree.getroot()
        for elem in root_node.findall('.//findQuotaOrderNumberByDatesResponseHistory'):
            items = elem.findall("QuotaOrderNumber")
            for item in items:
                quota_order_number = QuotaOrderNumber(item, file)
                a = 1
                quota_order_numbers.append(quota_order_number)
                # done = True
    if done:
        break

folder = os.getcwd()
dest_folder = os.path.join(folder, "dest")
changes_file = os.path.join(dest_folder, "changes.csv")
changes_xlsx = os.path.join(dest_folder, "changes.xlsx")

workbook = xlsxwriter.Workbook(changes_xlsx)
worksheet = workbook.add_worksheet()

row = 1
with open(changes_file, 'w') as f:
    write = csv.writer(f)
    
    worksheet.write(0, 0, "file")
    worksheet.write(0, 1, "operation")
    worksheet.write(0, 2, "transaction_date")
    worksheet.write(0, 3, "quota_order_number_id")
    worksheet.write(0, 4, "sid")
    worksheet.write(0, 5, "geographical_area_id")
    worksheet.write(0, 6, "operation")

    for quota_order_number in quota_order_numbers:
        for quota_order_number_origin in quota_order_number.quota_order_number_origins:
            
            worksheet.write(row, 0, quota_order_number.file)
            worksheet.write(row, 1, quota_order_number.operation)
            worksheet.write(row, 2, quota_order_number.transaction_date)
            worksheet.write(row, 3, quota_order_number.quota_order_number_id)
            worksheet.write(row, 4, quota_order_number.sid)
            worksheet.write(row, 5, quota_order_number_origin.geographical_area_id)
            worksheet.write(row, 6, quota_order_number_origin.operation)
            
            write.writerow([
                quota_order_number.file,
                quota_order_number.operation,
                quota_order_number.transaction_date,
                quota_order_number.quota_order_number_id,
                quota_order_number.sid,
                quota_order_number_origin.geographical_area_id,
                quota_order_number_origin.operation
            ])
            row += 1

workbook.close()
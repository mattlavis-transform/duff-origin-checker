import os
import sys
import xml.etree.ElementTree as ET

from classes.quota_order_number import QuotaOrderNumber

def process_null(elem):
    if elem is None:
        return None
    else:
        return elem.text
        
IMPORT_FOLDER = "/Users/matt.admin/sites and projects/1. Online Tariff/download CDS files/resources/xml"
path = os.walk(IMPORT_FOLDER)
file_array = []
for root, directories, files in path:
    for file in files:
        file_array.append(file)


file_array.sort(reverse=False)
for file in file_array:
    if ".xml" in file:
        
        import_path_and_file = os.path.join(IMPORT_FOLDER, file)
        tree = ET.parse(import_path_and_file)
        root_node = tree.getroot()
        for elem in root_node.findall('.//findQuotaOrderNumberByDatesResponseHistory'):
            quota_order_numbers = elem.findall("QuotaOrderNumber")
            for item in quota_order_numbers:
                quota_order_number = QuotaOrderNumber(item)
                a = 1

            a = 1
            # FootnoteType(elem, self.import_file)

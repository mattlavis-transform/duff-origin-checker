import os
import sys
import csv
import xml.etree.ElementTree as ET

from classes.database import Database
from classes.search_reference import SearchReference


# Get the valid headings
sql = """
select goods_nomenclature_item_id
from goods_nomenclatures gn where right(goods_nomenclature_item_id, 6) = '000000'
and validity_end_date is null order by goods_nomenclature_item_id ;
"""
d = Database()
current_headings = []
rows = d.run_query(sql)
for item in rows:
    current_headings.append(item[0])

# Get the search references
folder = os.getcwd()
source_folder = os.path.join(folder, "source")
dest_folder = os.path.join(folder, "dest")
refs_file = os.path.join(source_folder, "search_references_202105251318.csv")
sql_file = os.path.join(dest_folder, "sql.txt")
errors_file = os.path.join(dest_folder, "heading_errors.csv")

search_references = []
search_errors = []

with open(refs_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            ref = SearchReference()
            ref.id = row[0]
            ref.term = row[1]
            ref.key = row[2]
            ref.type = row[3]
            line_count += 1

            ref.check(current_headings, 4)
            search_references.append(ref)
        
    for search_reference in search_references:
        if not(search_reference.found):
            search_errors.append(search_reference)
            print (search_reference.key)
            
search_errors = sorted(search_errors, key=lambda x: x.key, reverse=False)

uniques = []
sql = ""
# Disambiguate
for item in search_errors:
    if item.key not in uniques:
        uniques.append(item.key)
        sql += "DELETE from search_references where referenced_id = '{}';\n".format(item.key)
    
f = open(sql_file, "w")
f.write(sql)
f.close()


with open(errors_file, 'w') as f:
    write = csv.writer(f)
    for row in search_errors:
        # write.writerow([row.id, row.term, row.key, row.type])
        write.writerow([row.key, row.term, row.type])
 
import csv

products = {}

with open('products_export_1.csv', newline='') as csvfile:
    shopifyreader = csv.reader(csvfile, delimiter=',')
    for idx, row in enumerate(shopifyreader):
        if idx == 0:
            keys = row
        else:
            if row[0] not in products:
                products[row[0]] = {k:[v] for k,v in zip(keys, row)}
            else:
                for i, key in enumerate(keys):
                    if row[i] != "" and row[i] not in products[row[0]][key]:
                        products[row[0]][key].append(row[i])

print(products)

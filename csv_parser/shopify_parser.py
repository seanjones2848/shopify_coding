import csv

repeat_column_keys = {"Handle"}

def convert_csv_to_obj():
    products = {}
    with open('products_export_1.csv', newline='') as csvfile:
        shopifyreader = csv.reader(csvfile, delimiter=',')
        for idx, row in enumerate(shopifyreader):
            if idx == 0:
                keys = row
            else:
                product = row[0]
                if product not in products:
                    products[product] = {k:[v] for k,v in zip(keys, row)}
                else:
                    for i, key in enumerate(keys):
                        value = row[i]
                        if value != "":
                            if value in products[product][key] and len(products[product][key]) == 1:
                                repeat_column_keys.add(key)
                            else:
                                products[row[0]][key].append(row[i])
    return products

def convert_obj_to_csv(products):
    keys = products[list(products.keys())[0]].keys()
    with open("product_update.csv", "w", newline="") as csvfile:
        shopifywriter = csv.DictWriter(csvfile, delimiter=",", fieldnames=keys)
        shopifywriter.writeheader()
        for data in products.values():
            list_max = max([len([y for y in data[x]]) for x in data.keys()])
            for i in range(list_max):
                values = []
                for k in keys:
                    if len(data[k]) > i:
                        values.append(data[k][i])
                    else:
                        if k in repeat_column_keys:
                            values.append(data[k][0])
                        else:
                            values.append("")
                shopifywriter.writerow({k:v for k,v in zip(keys, values)})



# prod = convert_csv_to_obj()
# prod["shaped-hand-soaps"]["Option1 Value"] = ["flerp", "plerp"]
# print(prod["shaped-hand-soaps"])
# print(repeat_column_keys)

# convert_obj_to_csv(prod)


import json
import pprint

with open('products.json' , 'r' , encoding="utf-8") as file:
    data = json.load(file)

# printer = pprint.PrettyPrinter()

# printer.pprint(data)

page = data.get('page')

for product in data.get('hits'):
    print( product.get('name'), product.get('price'))

print(page)

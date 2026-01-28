code = """# Let's query the products_orders database to find AI processing units
import json

# First, let's look at the Product2 table to see what AI processing units exist
query = "SELECT Id, Name, Description FROM Product2 WHERE Name LIKE '%AI%' OR Name LIKE '%artificial%' OR Name LIKE '%processing%' OR Name LIKE '%unit%' OR Description LIKE '%AI%' OR Description LIKE '%artificial%' OR Description LIKE '%processing%' OR Description LIKE '%unit%'"

print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_functions.list_db:0': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem']}

exec(code, env_args)

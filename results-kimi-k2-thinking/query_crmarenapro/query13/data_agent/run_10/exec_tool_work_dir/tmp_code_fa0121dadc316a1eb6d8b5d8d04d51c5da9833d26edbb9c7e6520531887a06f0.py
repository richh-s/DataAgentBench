code = """import json
from datetime import datetime, timedelta

# Calculate date range
today = datetime(2022, 11, 25)
# Past 5 months means from 5 months ago to today
# 5 months ago from 2022-11-25 would be 2022-06-25
start_date = datetime(2022, 6, 25)

print('__RESULT__:')
print(json.dumps({
    "start_date": start_date.strftime('%Y-%m-%d'),
    "end_date": today.strftime('%Y-%m-%d')
}))"""

env_args = {'var_functions.list_db:0': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem']}

exec(code, env_args)

code = """import json
import pandas as pd

quote_items = json.loads(locals()['var_function-call-16440815126689710381'][0])
df = pd.DataFrame(quote_items)
df['Quantity'] = pd.to_numeric(df['Quantity'])
df['Discount'] = pd.to_numeric(df['Discount'])

invalid_configs = df[(df['Discount'] > 0) & (df['Quantity'] > 10)]

print('__RESULT__:')
print(json.dumps(not invalid_configs.empty))"""

env_args = {'var_function-call-16440815126689710381': [{'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0'}, {'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0'}, {'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0'}, {'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0'}]}

exec(code, env_args)

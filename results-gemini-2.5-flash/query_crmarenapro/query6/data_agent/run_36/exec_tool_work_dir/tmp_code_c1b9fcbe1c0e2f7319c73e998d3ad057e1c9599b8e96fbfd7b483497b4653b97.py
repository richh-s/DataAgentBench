code = """import pandas as pd
import json

quote_line_items = json.loads(locals()['var_function-call-8591743726354909176']['results'][0])
df = pd.DataFrame(quote_line_items)

df['Quantity'] = df['Quantity'].astype(float)
df['UnitPrice'] = df['UnitPrice'].astype(float)
df['Discount'] = df['Discount'].astype(float)
df['TotalPrice'] = df['TotalPrice'].astype(float)

df['CalculatedTotalPrice'] = df['Quantity'] * df['UnitPrice'] * (1 - df['Discount'] / 100)

df['Difference'] = abs(df['TotalPrice'] - df['CalculatedTotalPrice'])

# A small tolerance for floating point comparisons
tolerance = 0.01
invalid_configs = df[df['Difference'] > tolerance]

# If there are invalid configs, we need to find a knowledge article.
# Since we don't have specific rules from the prompt, we'll assume a discrepancy 
# in TotalPrice calculation is the 'invalid config' to look for knowledge article.

if not invalid_configs.empty:
    result = {'invalid_config_found': True, 'invalid_items': invalid_configs.to_dict(orient='records')}
else:
    result = {'invalid_config_found': False}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-8591743726354909176': [{'Id': '0QLWt0000022j3GOAQ', 'Product2Id': '#01tWt000006hV6jIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'Product2Id': '#01tWt000006hPffIAE', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'Product2Id': '01tWt000006hVczIAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}]}

exec(code, env_args)

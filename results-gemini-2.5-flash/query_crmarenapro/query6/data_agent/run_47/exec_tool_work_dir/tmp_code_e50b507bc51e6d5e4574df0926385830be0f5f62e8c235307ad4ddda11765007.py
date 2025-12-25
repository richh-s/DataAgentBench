code = """import json
import pandas as pd

raw_output_string = locals()['var_function-call-16440815126689710381']['query_db_response']['results'][0]

start_index = raw_output_string.find('[')
end_index = raw_output_string.rfind(']')

json_array_string = raw_output_string[start_index : end_index + 1]

quote_items = json.loads(json_array_string)

df = pd.DataFrame(quote_items)
df['Quantity'] = pd.to_numeric(df['Quantity'])
df['Discount'] = pd.to_numeric(df['Discount'])

invalid_configs_exist = not df[(df['Discount'] > 0) & (df['Quantity'] > 10)].empty

print('__RESULT__:')
print(json.dumps(invalid_configs_exist))"""

env_args = {'var_function-call-16440815126689710381': [{'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0'}, {'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0'}, {'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0'}, {'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0'}]}

exec(code, env_args)

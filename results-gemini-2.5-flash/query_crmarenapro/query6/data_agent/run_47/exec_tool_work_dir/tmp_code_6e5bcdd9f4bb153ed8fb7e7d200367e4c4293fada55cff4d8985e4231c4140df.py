code = """import json
import pandas as pd

# The variable var_function-call-16440815126689710381 contains the entire output dictionary as shown in the previous output.
# So we need to access the dictionary first.
# Based on the error messages, it seems that locals()['var_function-call-16440815126689710381'] is a dictionary directly, not a string or list.
# Let's try to access it as a dictionary.

# Direct access to the dictionary, then navigate.
raw_result_dict = locals()['var_function-call-16440815126689710381']
raw_json_string_with_extra = raw_result_dict['query_db_response']['results'][0]

# Extract only the JSON array part from the string
start_index = raw_json_string_with_extra.find('[')
end_index = raw_json_string_with_extra.rfind(']') + 1
json_only_string = raw_json_string_with_extra[start_index:end_index]

# Parse the JSON string into a Python list of dictionaries
quote_items = json.loads(json_only_string)

df = pd.DataFrame(quote_items)
df['Quantity'] = pd.to_numeric(df['Quantity'])
df['Discount'] = pd.to_numeric(df['Discount'])

invalid_configs_exist = not df[(df['Discount'] > 0) & (df['Quantity'] > 10)].empty

print('__RESULT__:')
print(json.dumps(invalid_configs_exist))"""

env_args = {'var_function-call-16440815126689710381': [{'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0'}, {'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0'}, {'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0'}, {'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0'}]}

exec(code, env_args)

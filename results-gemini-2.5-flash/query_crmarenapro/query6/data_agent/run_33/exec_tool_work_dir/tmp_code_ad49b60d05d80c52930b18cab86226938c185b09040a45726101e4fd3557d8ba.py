code = """import json
import pandas as pd

# Get the list of knowledge article IDs from the previous tool call
article_ids = [item['id'] for item in locals()['var_function-call-17048460673220857598']]

# Prepare a list of article IDs for the next query
# Need to handle the '#' character and quote them for SQL IN clause
cleaned_article_ids = [f"'{id.replace('#', '')}'" for id in article_ids]
ids_string = ', '.join(cleaned_article_ids)

print('__RESULT__:')
print(json.dumps(ids_string))"""

env_args = {'var_function-call-4198281158085155910': [{'Id': '0QLWt0000022j3GOAQ', 'Product2Id': '#01tWt000006hV6jIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'Product2Id': '#01tWt000006hPffIAE', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'Product2Id': '01tWt000006hVczIAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-1169451631084900939': 'file_storage/function-call-1169451631084900939.json', 'var_function-call-3824789175363094292': [], 'var_function-call-17048460673220857598': [{'id': '#ka0Wt000000EqRlIAK'}, {'id': 'ka0Wt000000Eq0MIAS'}, {'id': 'ka0Wt000000EqQ9IAK'}, {'id': '#ka0Wt000000EpSUIA0'}, {'id': 'ka0Wt000000EnthIAC'}]}

exec(code, env_args)

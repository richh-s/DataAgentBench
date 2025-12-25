code = """import json
import pandas as pd

# Assuming the result of the previous tool call is in `var_function-call-14289792533565253859`
# and it's a list of dictionaries like `[{"Product2Id": "#01tWt000006hV8LIAU"}, ...]`

product_ids_data = json.loads(locals()['var_function-call-14289792533565253859'])[0]
product_ids = [item['Product2Id'].strip('#') for item in product_ids_data if item.get('Product2Id')]

# Prepare the list of product IDs for the SQL IN clause
product_ids_str = ', '.join(f"'{pid}'" for pid in product_ids)

print("__RESULT__:")
print(json.dumps(product_ids_str))"""

env_args = {'var_function-call-14289792533565253859': [{'Product2Id': '#01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hTUkIAM'}, {'Product2Id': '01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hV9xIAE'}]}

exec(code, env_args)

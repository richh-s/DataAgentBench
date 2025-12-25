code = """import json
import re

# Access the result from the previous tool call, which is a dictionary
query_result_dict = locals()['var_function-call-8465159177126568387']

# Extract the list of result strings
result_strings = query_result_dict['query_db_response']['results']

all_product_ids = []

# Each string in result_strings contains a JSON array of dictionaries
for result_str in result_strings:
    # The JSON array itself is within the string. Use regex to find and extract it.
    match = re.search(r'\[.+\]', result_str, re.DOTALL)
    if match:
        json_array_str = match.group(0)
        data = json.loads(json_array_str)
        for item in data:
            product_id = item.get('Product2Id')
            if product_id:
                all_product_ids.append(product_id.replace('#', ''))

# Filter for unique product IDs and remove potential empty strings if any
unique_cleaned_product_ids = list(set([pid for pid in all_product_ids if pid]))

print('__RESULT__:')
print(json.dumps(unique_cleaned_product_ids))"""

env_args = {'var_function-call-10152468221337320365': [{'Id': '006Wt000007B0g2IAC'}, {'Id': '006Wt000007B7TcIAK'}], 'var_function-call-8465159177126568387': [{'Product2Id': '#01tWt000006hV8LIAU'}, {'Product2Id': '#01tWt000006hV58IAE'}, {'Product2Id': '01tWt000006hTUkIAM'}, {'Product2Id': '01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hV9xIAE'}, {'Product2Id': '01tWt000006hVczIAE'}]}

exec(code, env_args)

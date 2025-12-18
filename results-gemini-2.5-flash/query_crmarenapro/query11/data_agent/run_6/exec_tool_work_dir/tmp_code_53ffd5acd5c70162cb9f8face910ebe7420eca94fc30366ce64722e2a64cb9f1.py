code = """import json
import re
raw_output = locals()['var_function-call-8465159177126568387']['results'][0]
json_string_match = re.search(r'\[.*\]', raw_output, re.DOTALL)
if json_string_match:
    json_string = json_string_match.group(0)
    data = json.loads(json_string)
    product_ids = [item['Product2Id'] for item in data]
    cleaned_product_ids = [pid.replace('#', '') for pid in product_ids]
else:
    cleaned_product_ids = []

print('__RESULT__:')
print(json.dumps(cleaned_product_ids))"""

env_args = {'var_function-call-10152468221337320365': [{'Id': '006Wt000007B0g2IAC'}, {'Id': '006Wt000007B7TcIAK'}], 'var_function-call-8465159177126568387': [{'Product2Id': '#01tWt000006hV8LIAU'}, {'Product2Id': '#01tWt000006hV58IAE'}, {'Product2Id': '01tWt000006hTUkIAM'}, {'Product2Id': '01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hV9xIAE'}, {'Product2Id': '01tWt000006hVczIAE'}]}

exec(code, env_args)

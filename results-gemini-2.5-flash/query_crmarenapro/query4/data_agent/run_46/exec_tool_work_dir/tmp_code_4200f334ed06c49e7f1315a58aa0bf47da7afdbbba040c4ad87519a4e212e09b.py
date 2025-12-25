code = """import json
import re

product_id_result_string = locals()['var_function-call-3721613820015664191']['query_db_response']['results'][0]
product_id_match = re.search(r'\[.*\]', product_id_result_string, re.DOTALL)

product_id = None
if product_id_match:
    product_id_json_string = product_id_match.group(0)
    product_id_raw = json.loads(product_id_json_string)
    if product_id_raw:
        product_id = product_id_raw[0]['Id']

print('__RESULT__:')
print(json.dumps(product_id))"""

env_args = {'var_function-call-3721613820015664191': [{'Id': '#01tWt000006hVJdIAM'}], 'var_function-call-2967129351824236084': [{'Id': '802Wt00000797awIAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B6gIAE'}]}

exec(code, env_args)

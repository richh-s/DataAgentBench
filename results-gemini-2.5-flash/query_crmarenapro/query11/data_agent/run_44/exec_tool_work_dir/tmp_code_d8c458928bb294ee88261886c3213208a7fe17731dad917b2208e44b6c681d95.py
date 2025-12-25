code = """import json
import re

def extract_json_from_string(s):
    # Extracts the first JSON array or object from a string
    match = re.search(r'(\[.*\]|\{.*\})', s, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            return None
    return None

# Safely extract and parse Account ID
account_id_raw_string = locals()['var_function-call-12597888680083809858']['query_db_response']['results'][0]
account_id_data = extract_json_from_string(account_id_raw_string)
account_id = account_id_data[0]['AccountId'].lstrip('#') if account_id_data and account_id_data[0] and 'AccountId' in account_id_data[0] else None

# Safely extract and parse AI product IDs
ai_product_ids_raw_string = locals()['var_function-call-7471893383420240367']['query_db_response']['results'][0]
ai_product_data = extract_json_from_string(ai_product_ids_raw_string)
ai_product_ids = [item["Id"] for item in ai_product_data] if ai_product_data else []

# Create a comma-separated string of product IDs for the SQL IN clause
ai_product_ids_str = ", ".join([f"'{pid}'" for pid in ai_product_ids])

print("__RESULT__:")
print(json.dumps({"account_id": account_id, "ai_product_ids_str": ai_product_ids_str}))"""

env_args = {'var_function-call-1550464384392667606': [], 'var_function-call-1987399488361058051': [{'Id': '01tWt000006hUgwIAE'}, {'Id': '01tWt000006hV8LIAU'}, {'Id': '01tWt000006hVI1IAM'}, {'Id': '01tWt000006hVMrIAM'}, {'Id': '01tWt000006hVebIAE'}, {'Id': '01tWt000006hVjSIAU'}], 'var_function-call-11008515269321474486': [{'AccountId': '#001Wt00000PGXrNIAX'}], 'var_function-call-13790589994052656290': [], 'var_function-call-5935668778037279343': [], 'var_function-call-7606461974371517891': [{'AccountId': '#001Wt00000PGXrNIAX'}], 'var_function-call-12597888680083809858': [{'AccountId': '#001Wt00000PGXrNIAX'}], 'var_function-call-7471893383420240367': [{'Id': '01tWt000006hUgwIAE'}, {'Id': '01tWt000006hV8LIAU'}, {'Id': '01tWt000006hVI1IAM'}, {'Id': '01tWt000006hVMrIAM'}, {'Id': '01tWt000006hVebIAE'}, {'Id': '01tWt000006hVjSIAU'}]}

exec(code, env_args)

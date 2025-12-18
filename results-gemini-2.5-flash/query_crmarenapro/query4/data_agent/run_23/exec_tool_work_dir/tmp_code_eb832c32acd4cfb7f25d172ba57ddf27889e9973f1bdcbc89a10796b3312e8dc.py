code = """import json

raw_results = locals()['var_function-call-9320036195922497951']['results']
all_order_item_ids = []

for res_str in raw_results:
    # Find the JSON array within the string
    start_idx = res_str.find('[')
    end_idx = res_str.rfind(']')
    if start_idx != -1 and end_idx != -1:
        json_data_str = res_str[start_idx : end_idx + 1]
        try:
            data = json.loads(json_data_str)
            for item in data:
                if 'Id' in item:
                    all_order_item_ids.append(item['Id'].replace('#', '').strip())
        except json.JSONDecodeError:
            # Handle cases where the extracted string is not valid JSON
            pass

cleaned_ids_string = ', '.join([f"'{id_}'" for id_ in all_order_item_ids])

print("__RESULT__:")
print(json.dumps(cleaned_ids_string))"""

env_args = {'var_function-call-9320036195922497951': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)

code = """import json

raw_result_dict = locals()['var_function-call-8876751307380815954']
full_output_string = raw_result_dict['query_db_response']['results'][0]

# Locate the start of the actual JSON array after "The result is:\n"
json_start_marker = "The result is:\n"
start_idx = full_output_string.find(json_start_marker)

json_array_str = "[]" # Default to empty if parsing fails

if start_idx != -1:
    # Adjust start_idx to point to the beginning of the JSON array itself
    potential_json_str = full_output_string[start_idx + len(json_start_marker):].strip()
    
    # Ensure it starts with '[' and ends with ']'
    if potential_json_str.startswith('[') and potential_json_str.endswith(']'):
        json_array_str = potential_json_str
    else:
        # Fallback to finding the brackets if the above method fails
        bracket_start = potential_json_str.find('[')
        bracket_end = potential_json_str.rfind(']')
        if bracket_start != -1 and bracket_end != -1:
            json_array_str = potential_json_str[bracket_start : bracket_end + 1]

order_item_ids_list = json.loads(json_array_str)

cleaned_ids = [item['Id'].replace('#', '').strip() for item in order_item_ids_list]
ids_str = ', '.join([f"'{_id}'" for _id in cleaned_ids])

print("__RESULT__:")
print(json.dumps(ids_str))"""

env_args = {'var_function-call-8876751307380815954': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)

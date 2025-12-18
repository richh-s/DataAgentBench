code = """import json

# Access the raw result from the storage variable. 
# Assuming the variable directly holds the list of strings, not the full dictionary.
raw_result_list = locals()['var_function-call-8876751307380815954']

# Get the first (and likely only) string containing the full output
full_output_string = raw_result_list[0]

# Now, extract the JSON array part from this string
start_idx = full_output_string.find('[')
end_idx = full_output_string.rfind(']')
json_array_str = full_output_string[start_idx : end_idx + 1]

# Finally, parse the JSON array string
order_item_ids_list = json.loads(json_array_str)

cleaned_ids = [item['Id'].replace('#', '').strip() for item in order_item_ids_list]
ids_str = ', '.join([f"'{_id}'" for _id in cleaned_ids])

print("__RESULT__:")
print(json.dumps(ids_str))"""

env_args = {'var_function-call-8876751307380815954': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)

code = """import json
import pandas as pd

# Access the string containing the JSON list, which is the first element of 'results'
raw_json_string = locals()['var_function-call-8734665002838025116']['query_db_response']['results'][0]

# The string itself contains additional text from the tool execution log. Extract only the JSON part.
# The JSON part starts with '[' and ends with ']'.
start_index = raw_json_string.find('[')
end_index = raw_json_string.rfind(']')
json_only_string = raw_json_string[start_index : end_index + 1]

# Parse the JSON string into a Python list of dictionaries
parsed_results = json.loads(json_only_string)

business_refs = [record['business_ref'] for record in parsed_results]
business_ids = [ref.replace('businessref_', 'businessid_') for ref in business_refs]

# Prepare the list of business_ids for MongoDB $in operator
result = json.dumps(business_ids)
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-8734665002838025116': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}]}

exec(code, env_args)

code = """import json
import re

# Access the raw string result from the previous query_db call
# The variable 'var_function-call-16734970030880208519' is the entire dictionary output from the tool.
db_response_dict = locals()['var_function-call-16734970030880208519']
raw_db_result_str = db_response_dict['query_db_response']['results'][0]

# The actual JSON array is embedded within a string that also contains metadata about the tool execution.
# Use a regular expression to extract just the JSON array string.
# The regex needs to be careful about escaped quotes within the JSON string itself.
# However, it seems the problem is simpler: the string content itself is a valid JSON string that needs to be loaded.
# The `
` and other descriptive text are part of the overall tool output string, not part of the JSON data structure.

# Let's try to parse the entire string as a series of lines and then find the line that starts with '[' and ends with ']'.
json_lines = []
for line in raw_db_result_str.splitlines():
    stripped_line = line.strip()
    if stripped_line.startswith('[') and stripped_line.endswith(']'):
        json_lines.append(stripped_line)

if json_lines:
    json_array_str = json_lines[0] # Assuming there's only one JSON array line
    review_data = json.loads(json_array_str)

    extracted_data = []
    gmap_ids = []
    for item in review_data:
        gmap_id = item['gmap_id']
        high_rating_review_count = int(item['high_rating_review_count'])
        extracted_data.append({'gmap_id': gmap_id, 'high_rating_review_count': high_rating_review_count})
        gmap_ids.append(gmap_id)

    print('__RESULT__:')
    print(json.dumps({'extracted_data': extracted_data, 'gmap_ids': gmap_ids}))
else:
    print('__RESULT__:')
    print(json.dumps({'extracted_data': [], 'gmap_ids': []}))"""

env_args = {'var_function-call-16734970030880208519': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}]}

exec(code, env_args)

code = """import json
import re

# The tool output is stored under var_function-call-1966758457191584311
# It's a dictionary with a key 'query_db_response'.
# Inside 'query_db_response', there's a 'results' key which holds a list.
# The actual string with the JSON data is the first element of this 'results' list.

full_output_string = locals()['var_function-call-1966758457191584311']['query_db_response']['results'][0]

# Use regex to extract the JSON array from the string.
# The pattern `r'\[.*?\]'` will match the content between the first `[` and the last `]`.
# `re.DOTALL` is crucial here as the JSON string might span multiple lines.
json_match = re.search(r'\[.*?\]', full_output_string, re.DOTALL)

if json_match:
    json_array_str = json_match.group(0)
    # Parse the JSON string into a Python list of dictionaries
    sales_data = json.loads(json_array_str)

    # Calculate the total revenue
    total_revenue = sum(float(record['revenue_usd']) for record in sales_data)

    print('__RESULT__:')
    print(json.dumps(total_revenue))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'Failed to extract JSON data from query_db result.'}))"""

env_args = {'var_function-call-16342884014696280868': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07"}], 'var_function-call-1966758457191584311': [{'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)

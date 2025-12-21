code = """import json
import re

# Access the complete tool output, which is a dictionary
tool_output = locals()['var_function-call-1966758457191584311']

# Extract the string containing the results from the 'results' key within 'query_db_response'
results_string = tool_output['query_db_response']['results'][0]

# Use a regular expression to find the JSON array within the string
# This pattern looks for a string that starts with '[' and ends with ']' and contains JSON-like content
match = re.search(r'\[.*?\]', results_string, re.DOTALL)

if match:
    json_array_str = match.group(0)
    # Parse the JSON string into a Python list of dictionaries
    results_list = json.loads(json_array_str)

    # Calculate the total revenue
    total_revenue = sum(float(record['revenue_usd']) for record in results_list)

    print('__RESULT__:')
    print(json.dumps(total_revenue))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'No JSON array found in the results string'}))"""

env_args = {'var_function-call-16342884014696280868': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07"}], 'var_function-call-1966758457191584311': [{'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)

code = """import json

# Access the string containing the JSON array of results along with other text
output_string = locals()['var_function-call-1966758457191584311']['query_db_response']['results'][0]

# Extract the JSON array string from the full output string
json_start = output_string.find('[')
json_end = output_string.rfind(']')
json_array_str = output_string[json_start : json_end + 1]

# Parse the JSON string into a Python list of dictionaries
results_list = json.loads(json_array_str)

# Calculate the total revenue
total_revenue = sum(float(record['revenue_usd']) for record in results_list)

print('__RESULT__:')
print(json.dumps(total_revenue))"""

env_args = {'var_function-call-16342884014696280868': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07"}], 'var_function-call-1966758457191584311': [{'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)

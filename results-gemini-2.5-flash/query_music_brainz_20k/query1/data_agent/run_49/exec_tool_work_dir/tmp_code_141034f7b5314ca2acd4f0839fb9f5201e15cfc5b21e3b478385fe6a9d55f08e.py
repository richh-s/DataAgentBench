code = """import json

# Access the result directly, assuming it's a JSON string of the list of records
results_json_string = locals()['var_function-call-1966758457191584311']

# Parse the JSON string into a Python list of dictionaries
results_list = json.loads(results_json_string)

# Calculate the total revenue
total_revenue = sum(float(record['revenue_usd']) for record in results_list)

print('__RESULT__:')
print(json.dumps(total_revenue))"""

env_args = {'var_function-call-16342884014696280868': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07"}], 'var_function-call-1966758457191584311': [{'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)

code = """import json

# Get top_track_ids from storage
# Actually I printed them in the last step but they are not automatically available as a variable unless I read them.
# But wait, I can access the result of the previous tool call.
# The previous tool call result is stored in `var_function-call-5674796126939342252`.
# Let's read it.

file_path = locals()['var_function-call-5674796126939342252']
with open(file_path, 'r') as f:
    top_track_ids = json.load(f)

# Construct SQL query
ids_str = ",".join(map(str, top_track_ids))
query = f"SELECT track_id, title, artist, album, year, length FROM tracks WHERE track_id IN ({ids_str})"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-14714155237110464570': 'file_storage/function-call-14714155237110464570.json', 'var_function-call-5674796126939342252': 'file_storage/function-call-5674796126939342252.json'}

exec(code, env_args)

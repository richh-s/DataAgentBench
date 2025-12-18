code = """import json

# Retrieve the list of massage gmap_ids
massage_gmap_ids = locals()['var_function-call-2149115437330784946']

# Construct the IN clause for the SQL query
gmap_id_list_str = ', '.join([f"'{gmap_id}'" for gmap_id in massage_gmap_ids])

# Construct the full SQL query
sql_query = f"SELECT gmap_id, rating FROM review WHERE gmap_id IN ({gmap_id_list_str});"

print('__RESULT__:')
print(json.dumps(sql_query))"""

env_args = {'var_function-call-2705248405242993009': [], 'var_function-call-6260699461556202789': [], 'var_function-call-3994384311218662169': 'file_storage/function-call-3994384311218662169.json', 'var_function-call-2149115437330784946': ['gmap_22', 'gmap_25', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_21', 'gmap_28']}

exec(code, env_args)

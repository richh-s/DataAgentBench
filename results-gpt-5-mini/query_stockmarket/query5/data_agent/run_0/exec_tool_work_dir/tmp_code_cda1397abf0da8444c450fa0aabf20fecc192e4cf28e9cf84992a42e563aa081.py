code = """import json
with open(var_call_8sPApHfmPrpLxFoixe5XxPs2, 'r') as f:
    data = json.load(f)
symbols = data['symbols']

parts = []
for s in symbols:
    tbl = '"' + s.replace('"', '""') + '"'
    part = f"SELECT '{s}' AS symbol, COUNT(*) AS cnt FROM {tbl} WHERE Date LIKE '2019-%' AND (High - Low) > 0.2 * Low"
    parts.append(part)
sql = '\nUNION ALL\n'.join(parts) + '\nORDER BY cnt DESC;'

print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_0yaHAZkfGrcaXHyke6o3ibIL': 'file_storage/call_0yaHAZkfGrcaXHyke6o3ibIL.json', 'var_call_dKSpiYnifg74W8Lb0g48hfat': 'file_storage/call_dKSpiYnifg74W8Lb0g48hfat.json', 'var_call_8sPApHfmPrpLxFoixe5XxPs2': 'file_storage/call_8sPApHfmPrpLxFoixe5XxPs2.json'}

exec(code, env_args)

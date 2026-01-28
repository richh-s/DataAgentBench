code = """import json
with open(var_call_FHdvyaEFB6c41YjYzxoiKKZg, 'r') as f:
    symbols = json.load(f)

# Filter unique and sort
symbols = sorted(set(symbols))

# Build SQL union query
parts = []
for s in symbols:
    # escape single quotes in symbol
    sval = s.replace("'", "''")
    part = f"SELECT '{sval}' AS symbol FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
    parts.append(part)

sql = '\nUNION ALL\n'.join(parts) + ';'
# Output the SQL string as JSON
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_BZ0vbjInUsrjIR40BDpeJO2j': 'file_storage/call_BZ0vbjInUsrjIR40BDpeJO2j.json', 'var_call_ETnWX20FaLVdAYR2akuYOwgE': 'file_storage/call_ETnWX20FaLVdAYR2akuYOwgE.json', 'var_call_FHdvyaEFB6c41YjYzxoiKKZg': 'file_storage/call_FHdvyaEFB6c41YjYzxoiKKZg.json'}

exec(code, env_args)

code = """import json, pandas as pd

path = var_call_1KSmw8wTWVRtAfpKPz4Wtunl
with open(path, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

path2 = var_call_DYfAOBC3wLroJmA6thnVUubL
with open(path2, 'r') as f:
    tables = json.load(f)
tables_set = set(tables)

symbols = sorted(set(info_df['Symbol']).intersection(tables_set))

unions = []
for sym in symbols:
    part = (
        "SELECT '{sym}' AS Symbol, "
        "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
        "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
        "FROM \"{sym}\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
    ).format(sym=sym)
    unions.append(part)

query = "\nUNION ALL\n".join(unions)

out = json.dumps({"query": query, "symbol_count": len(symbols)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_1KSmw8wTWVRtAfpKPz4Wtunl': 'file_storage/call_1KSmw8wTWVRtAfpKPz4Wtunl.json', 'var_call_DYfAOBC3wLroJmA6thnVUubL': 'file_storage/call_DYfAOBC3wLroJmA6thnVUubL.json'}

exec(code, env_args)

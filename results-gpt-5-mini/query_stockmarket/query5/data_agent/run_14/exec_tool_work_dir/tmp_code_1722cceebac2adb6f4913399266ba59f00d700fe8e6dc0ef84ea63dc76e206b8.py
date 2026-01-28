code = """import json
with open(var_call_9KfMvHz2ISZfx4mNM9e1gcJ0, 'r') as f:
    data = json.load(f)
symbols = data['symbols']
parts = []
for s in symbols:
    parts.append("SELECT {0!r} AS symbol, COUNT(*) AS cnt FROM \"{0}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.2 * Low".format(s))
sql = "\nUNION ALL\n".join(parts)
final = "SELECT symbol, cnt FROM (\n" + sql + "\n) ORDER BY cnt DESC, symbol LIMIT 5;"
print("__RESULT__:")
print(json.dumps({"sql": final}))"""

env_args = {'var_call_EEujyNWciR62lhYczKx9JiG1': 'file_storage/call_EEujyNWciR62lhYczKx9JiG1.json', 'var_call_HGyGjC7o6mlyzGcV9YqRot21': 'file_storage/call_HGyGjC7o6mlyzGcV9YqRot21.json', 'var_call_9KfMvHz2ISZfx4mNM9e1gcJ0': 'file_storage/call_9KfMvHz2ISZfx4mNM9e1gcJ0.json', 'var_call_9AJBphqyDri2qwpn96pvOsUB': {'n': 86, 'first': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}}

exec(code, env_args)

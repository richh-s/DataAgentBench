code = """import json
with open(var_call_9KfMvHz2ISZfx4mNM9e1gcJ0, 'r') as f:
    data=json.load(f)
symbols=data['symbols']
parts=[]
for s in symbols:
    sq = "SELECT '{}' AS symbol, COUNT(*) AS cnt FROM \"{}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.2 * Low".format(s, s)
    parts.append(sq)
sql = "\nUNION ALL\n".join(parts)
final_sql = "SELECT symbol, cnt FROM (\n" + sql + "\n) ORDER BY cnt DESC NULLS LAST, symbol LIMIT 5;"
print("__RESULT__:")
print(json.dumps({"sql": final_sql}))"""

env_args = {'var_call_EEujyNWciR62lhYczKx9JiG1': 'file_storage/call_EEujyNWciR62lhYczKx9JiG1.json', 'var_call_HGyGjC7o6mlyzGcV9YqRot21': 'file_storage/call_HGyGjC7o6mlyzGcV9YqRot21.json', 'var_call_9KfMvHz2ISZfx4mNM9e1gcJ0': 'file_storage/call_9KfMvHz2ISZfx4mNM9e1gcJ0.json'}

exec(code, env_args)

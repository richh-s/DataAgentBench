code = """import json
cpc_defs = json.load(open(var_call_YbY7DM7wImXuzhOIchcbO51h,'r',encoding='utf-8'))
# collect sample symbols and lengths
symbols = [rec.get('symbol') for rec in cpc_defs if 'symbol' in rec]
lengths = {}
for s in symbols[:200]:
    lengths.setdefault(len(s),0)
    lengths[len(s)] += 1
sample = symbols[:100]
import json
print("__RESULT__:")
print(json.dumps({'counts_by_length': lengths, 'sample_symbols': sample}))"""

env_args = {'var_call_YbY7DM7wImXuzhOIchcbO51h': 'file_storage/call_YbY7DM7wImXuzhOIchcbO51h.json', 'var_call_N0b91Hn5uZaQS2tLZuS3l9hW': 'file_storage/call_N0b91Hn5uZaQS2tLZuS3l9hW.json', 'var_call_OSp9CHdVJaPAAwHzrsm7Aejv': []}

exec(code, env_args)

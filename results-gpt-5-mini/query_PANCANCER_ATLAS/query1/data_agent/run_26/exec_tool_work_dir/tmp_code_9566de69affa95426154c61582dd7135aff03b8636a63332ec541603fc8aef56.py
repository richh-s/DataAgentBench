code = """import json
fp = var_call_jTVAhWbwM9ZBR1YoADiDpl2t
with open(fp, 'r') as f:
    data = json.load(f)
# get keys from first record
keys = sorted(list(data[0].keys()))
# print
print("__RESULT__:")
print(json.dumps({"num_records_preview": len(data), "keys": keys}))"""

env_args = {'var_call_tjL3pAojpXuMoyOIKj9nRnxk': ['clinical_info'], 'var_call_1eUvhHV2vq0IgYjWAkvhUkVy': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_jTVAhWbwM9ZBR1YoADiDpl2t': 'file_storage/call_jTVAhWbwM9ZBR1YoADiDpl2t.json'}

exec(code, env_args)

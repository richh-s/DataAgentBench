code = """import json, re
# load the query result stored in the provided file path variable
path = var_call_K76lhjqcVHeDejOLVAMm6Otx
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
pubnums = set()
pattern = re.compile(r"[A-Z]{2}-\d+[A-Z0-9\-]*")
for rec in data:
    pi = rec.get('Patents_info','')
    matches = pattern.findall(pi)
    for m in matches:
        pubnums.add(m)
# convert to sorted list
pubnum_list = sorted(pubnums)
import json
print("__RESULT__:")
print(json.dumps(pubnum_list))"""

env_args = {'var_call_xHEU1oMOIvdkYQaTjqaxctyM': ['publicationinfo'], 'var_call_ucVteL4Xu01z0mGWHlKCPgu1': ['cpc_definition'], 'var_call_nSgVCKsp6e4qxto73Du7R7hu': 'file_storage/call_nSgVCKsp6e4qxto73Du7R7hu.json', 'var_call_K76lhjqcVHeDejOLVAMm6Otx': 'file_storage/call_K76lhjqcVHeDejOLVAMm6Otx.json'}

exec(code, env_args)

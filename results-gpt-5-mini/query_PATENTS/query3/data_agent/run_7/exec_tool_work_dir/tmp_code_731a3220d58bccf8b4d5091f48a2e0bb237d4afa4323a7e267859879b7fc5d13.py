code = """import json, re
# var_call_AMrDYDRyAiDk5vRxmCAz6wcC is the storage key for the previous query_db result file path
path = var_call_AMrDYDRyAiDk5vRxmCAz6wcC
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
pubnums = set()
pat = re.compile(r'(?:pub\. number|publication number|pub\. no\.|pub\. number)\s*([A-Z]{2}-[0-9A-Za-z-]+)', re.IGNORECASE)
for rec in data:
    pi = rec.get('Patents_info','')
    for m in pat.finditer(pi):
        pubnums.add(m.group(1))
# Also try to extract patterns like beginning with country and dash, e.g., US-11421276-B2 even if phrase differs
pat2 = re.compile(r'\b([A-Z]{2}-\d{4,}[A-Z0-9-]*)\b')
for rec in data:
    pi = rec.get('Patents_info','')
    for m in pat2.finditer(pi):
        token = m.group(1)
        # filter unrealistic tokens
        if '-' in token and any(c.isdigit() for c in token):
            pubnums.add(token)
pubnums = sorted(pubnums)
print("__RESULT__:")
print(json.dumps(pubnums))"""

env_args = {'var_call_WakKrtRs7x6PBnTcp6hvegg1': ['publicationinfo'], 'var_call_qAMMTH6DzqiVvTFW2mhfJi8Q': ['cpc_definition'], 'var_call_AMrDYDRyAiDk5vRxmCAz6wcC': 'file_storage/call_AMrDYDRyAiDk5vRxmCAz6wcC.json'}

exec(code, env_args)

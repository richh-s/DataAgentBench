code = """import json, re
with open(var_call_5rHtrHNCXLAWFEXzgsUP2BJs, 'r', encoding='utf-8') as f:
    records = json.load(f)

cnt_contains_DE = 0
cnt_from_DE = 0
examples = []
for rec in records:
    info = rec.get('Patents_info') or ''
    if 'DE' in info:
        cnt_contains_DE += 1
    if 'from DE' in info or 'from DE,' in info:
        cnt_from_DE += 1
    if re.search(r'\bDE-', info):
        examples.append(info)

res = {'total': len(records), 'cnt_contains_DE': cnt_contains_DE, 'cnt_from_DE': cnt_from_DE, 'examples_with_DE_dash': examples[:10]}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_aotf5Uc4J2te04vTC8sI8JrG': ['publicationinfo'], 'var_call_IVHWtrdfXTmXDR9hUhfcqliw': ['cpc_definition'], 'var_call_pmiPwWzDql1MApaUfscIR8R0': 'file_storage/call_pmiPwWzDql1MApaUfscIR8R0.json', 'var_call_96ynt5c54hdqWNWAPK3VhPur': 'file_storage/call_96ynt5c54hdqWNWAPK3VhPur.json', 'var_call_NsvNsGurGkwfOEmVn6LEFA53': 'file_storage/call_NsvNsGurGkwfOEmVn6LEFA53.json', 'var_call_5rHtrHNCXLAWFEXzgsUP2BJs': 'file_storage/call_5rHtrHNCXLAWFEXzgsUP2BJs.json', 'var_call_JfappaY2weevdUnaJZefgNUK': [], 'var_call_2XPqZhmiMIE2tG6E4kVTdTym': {'total_records': 211, 'de_candidates': 0, 'de_h2_2019': 0, 'sample': []}}

exec(code, env_args)

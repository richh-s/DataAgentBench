code = """import json, re

with open(var_call_tvobrBCauIeEF7HgXhjZu1Qp,'r') as f:
    docs = json.load(f)

text = docs[0]['text']
# find disaster section snippet
idx = text.lower().find('disaster projects')
snippet = text[idx:idx+3000]
print('__RESULT__:')
print(json.dumps({'snippet': snippet}))"""

env_args = {'var_call_cguj2JY470StqtvTJdpADgC5': ['Funding'], 'var_call_E3A3KNZAloQm34K4K1JvVvyY': 'file_storage/call_E3A3KNZAloQm34K4K1JvVvyY.json', 'var_call_JESPpTsMF7CJnZLezqHiSbmp': 'file_storage/call_JESPpTsMF7CJnZLezqHiSbmp.json', 'var_call_jtmPqoYIzrjKo9fcalJWNbHi': {'total_funding_amount_usd': 0, 'num_disaster_projects_started_2022_with_funding_match': 0, 'matched_projects': [], 'extracted_disaster_projects_started_2022': [], 'num_extracted_disaster_projects_started_2022': 0}, 'var_call_tvobrBCauIeEF7HgXhjZu1Qp': 'file_storage/call_tvobrBCauIeEF7HgXhjZu1Qp.json', 'var_call_tJzkUAZC0U6FljVuIHL5Zb4r': {'total_funding_amount_usd': 0, 'projects_started_2022': [], 'matched_projects': []}}

exec(code, env_args)

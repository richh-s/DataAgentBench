code = """import json, re

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

docs_2022 = load_records(var_call_NZJkfTDqLIsk7PFQBeRVaweQ)

# find lines with completed and 2022 and show surrounding context for first 20 occurrences
occ = []
for d in docs_2022:
    lines = d.get('text','').splitlines()
    for i, ln in enumerate(lines):
        if '2022' in ln and re.search(r'completed', ln, re.I):
            snippet = "\\n".join([l.strip() for l in lines[max(0,i-3):min(len(lines),i+4)]])
            occ.append({'filename': d.get('filename'), 'line': ln.strip(), 'snippet': snippet})

print('__RESULT__:')
print(json.dumps(occ[:30]))"""

env_args = {'var_call_PF945Zw0JElUWZwT5KGXqZEA': 'file_storage/call_PF945Zw0JElUWZwT5KGXqZEA.json', 'var_call_DzrJsyGi8yVyguqqLp4vcoWd': 'file_storage/call_DzrJsyGi8yVyguqqLp4vcoWd.json', 'var_call_T91ysjF9P7VgpzVdTV1ByLnj': {'total_funding': 0, 'matched_projects': []}, 'var_call_CrcRzhL9q7DiYIrKy3uVxOU9': [], 'var_call_NZJkfTDqLIsk7PFQBeRVaweQ': 'file_storage/call_NZJkfTDqLIsk7PFQBeRVaweQ.json', 'var_call_Cax9yluJNVoPSK6RKDEvS3oN': 'file_storage/call_Cax9yluJNVoPSK6RKDEvS3oN.json', 'var_call_zww0BUzO2UrMING15mJ6npN2': 'file_storage/call_zww0BUzO2UrMING15mJ6npN2.json', 'var_call_pl17LDEzJbcq5WLFZNLezpPw': {'completed_park_projects_2022': [], 'matched_funding_rows': [], 'total_funding': 0}}

exec(code, env_args)

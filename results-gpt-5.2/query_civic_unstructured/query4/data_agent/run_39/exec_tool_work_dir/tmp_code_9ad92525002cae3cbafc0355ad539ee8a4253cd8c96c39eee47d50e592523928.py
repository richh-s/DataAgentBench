code = """import json, re
path_docs = var_call_doDJq1s9rwUWUOVU3na3B1gf
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)
text = docs[0]['text']
# find exact lines containing 'Begin Construction: Spring 2022'
lines = [ln.strip() for ln in text.splitlines()]
matches = [(i, lines[i]) for i in range(len(lines)) if re.search(r'Begin\s+Construction\s*:\s*Spring\s*2022', lines[i], re.I)]
print('__RESULT__:')
print(json.dumps(matches[:10]))"""

env_args = {'var_call_XtEzw5AyTsnXaaX8ijHhlrwl': ['Funding'], 'var_call_rb6ikrCfiVg35rh8JoXlANJh': ['civic_docs'], 'var_call_doDJq1s9rwUWUOVU3na3B1gf': 'file_storage/call_doDJq1s9rwUWUOVU3na3B1gf.json', 'var_call_SGs0mH129VnZcNiI76ckFcuz': 'file_storage/call_SGs0mH129VnZcNiI76ckFcuz.json', 'var_call_Cf0GMiMWAxjQKqAOFkIfIzbA': {'spring_2022_started_projects_count': 0, 'total_funding_usd': 0, 'matched_projects': []}}

exec(code, env_args)

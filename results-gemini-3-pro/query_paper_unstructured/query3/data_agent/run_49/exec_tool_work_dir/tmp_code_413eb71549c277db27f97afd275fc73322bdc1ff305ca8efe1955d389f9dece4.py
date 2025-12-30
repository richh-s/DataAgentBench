code = """import json
import re

with open(locals()['var_function-call-3050203900418415447'], 'r') as f:
    papers = json.load(f)

print("__RESULT__:")
info = {}
info['total_papers'] = len(papers)
info['empirical_count'] = sum(1 for p in papers if 'empirical' in p.get('text', '').lower())

samples = []
for p in papers[:5]:
    text_sample = p.get('text', '')[:300]
    years = re.findall(r'\b(20\d\d)\b', text_sample)
    samples.append({'filename': p['filename'], 'text_start': text_sample, 'years_found': years})

info['samples'] = samples
print(json.dumps(info))"""

env_args = {'var_function-call-7133362832000802960': 'file_storage/function-call-7133362832000802960.json', 'var_function-call-7133362832000806077': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-3665432082971907292': 'file_storage/function-call-3665432082971907292.json', 'var_function-call-3050203900418415447': 'file_storage/function-call-3050203900418415447.json', 'var_function-call-4351111685594668903': []}

exec(code, env_args)

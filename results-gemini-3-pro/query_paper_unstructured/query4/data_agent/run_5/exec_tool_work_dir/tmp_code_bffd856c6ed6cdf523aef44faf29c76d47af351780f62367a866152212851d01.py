code = """import json

with open(locals()['var_function-call-7732815880617685738'], 'r') as f:
    papers = json.load(f)

pa_papers = []
for paper in papers:
    if 'physical activity' in paper['text'].lower():
        pa_papers.append(paper)

print("__RESULT__:")
# Print first 300 chars of first 3 matches
debug_info = []
for p in pa_papers[:3]:
    debug_info.append({
        "filename": p['filename'],
        "header_snippet": p['text'][:300]
    })
print(json.dumps(debug_info))"""

env_args = {'var_function-call-12176732640452715958': 'file_storage/function-call-12176732640452715958.json', 'var_function-call-9822203806490735992': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-7732815880617685738': 'file_storage/function-call-7732815880617685738.json', 'var_function-call-8701835322479169308': []}

exec(code, env_args)

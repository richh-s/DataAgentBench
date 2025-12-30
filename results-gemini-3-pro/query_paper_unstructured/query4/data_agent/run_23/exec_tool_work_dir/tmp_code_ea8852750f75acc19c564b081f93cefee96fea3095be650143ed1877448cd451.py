code = """import json

with open(locals()['var_function-call-6532184733094038919'], 'r') as f:
    papers_data = json.load(f)

debug_info = []
for paper in papers_data[:5]:
    debug_info.append({
        "filename": paper['filename'],
        "header": paper['text'][:300]
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-5019104688225349175': 'file_storage/function-call-5019104688225349175.json', 'var_function-call-4539344191155681833': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-6532184733094038919': 'file_storage/function-call-6532184733094038919.json', 'var_function-call-16720471753298143428': 'file_storage/function-call-16720471753298143428.json', 'var_function-call-5284581737905555654': []}

exec(code, env_args)

code = """import json

with open(locals()['var_function-call-18372255859020147212'], 'r') as f:
    papers = json.load(f)

print("__RESULT__:")
print(json.dumps([{'filename': p['filename'], 'header': p['text'][:300]} for p in papers[:5]]))"""

env_args = {'var_function-call-1760363004607511404': 'file_storage/function-call-1760363004607511404.json', 'var_function-call-1760363004607508631': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-12400401275276692089': 'file_storage/function-call-12400401275276692089.json', 'var_function-call-18372255859020147212': 'file_storage/function-call-18372255859020147212.json', 'var_function-call-6662495405269273368': [], 'var_function-call-11090582513645745945': 'file_storage/function-call-11090582513645745945.json', 'var_function-call-2142637407128357390': 'file_storage/function-call-2142637407128357390.json', 'var_function-call-1632076592843413196': []}

exec(code, env_args)

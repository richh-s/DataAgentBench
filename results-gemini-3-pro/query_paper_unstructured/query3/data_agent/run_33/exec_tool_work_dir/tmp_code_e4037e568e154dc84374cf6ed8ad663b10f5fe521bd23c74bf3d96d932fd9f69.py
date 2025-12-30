code = """import json

path = locals()['var_function-call-454889790813745050']
with open(path, 'r') as f:
    data = json.load(f)

doc = data[0]
t = doc['text']
res = {
    'start': t[:500],
    'end': t[-500:]
}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_function-call-454889790813745050': 'file_storage/function-call-454889790813745050.json', 'var_function-call-2725923968047008507': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)

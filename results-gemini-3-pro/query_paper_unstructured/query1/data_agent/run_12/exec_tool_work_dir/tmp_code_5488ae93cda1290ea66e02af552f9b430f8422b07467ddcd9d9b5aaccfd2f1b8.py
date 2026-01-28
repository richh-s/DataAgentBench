code = """import json

file_path = locals()['var_function-call-17858895574398346247']
with open(file_path, 'r') as f:
    papers = json.load(f)

titles = [p.get('filename', '').replace('.txt', '') for p in papers]
print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_function-call-1852344882916152676': 'file_storage/function-call-1852344882916152676.json', 'var_function-call-1852344882916155297': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-17858895574398346247': 'file_storage/function-call-17858895574398346247.json', 'var_function-call-7066089185120334334': []}

exec(code, env_args)

code = """import json

with open(locals()['var_function-call-18231062501554874953'], 'r') as f:
    docs = json.load(f)

# Print first 300 chars of first 5 docs
headers = []
for doc in docs[:5]:
    headers.append(doc['text'][:300])

print("__RESULT__:")
print(json.dumps(headers))"""

env_args = {'var_function-call-15828363465301237669': 'file_storage/function-call-15828363465301237669.json', 'var_function-call-5049852519434866755': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-18231062501554874953': 'file_storage/function-call-18231062501554874953.json', 'var_function-call-4823252345665697145': []}

exec(code, env_args)

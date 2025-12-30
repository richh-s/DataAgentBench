code = """import json

file_path = locals()['var_function-call-5063725347681925527']

try:
    with open(file_path, 'r') as f:
        docs = json.load(f)
except Exception as e:
    docs = []
    print(f"Error: {e}")

candidates = []

for d in docs:
    text = d.get('text', '')
    filename = d.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check domain
    if 'physical activity' in text.lower():
        # Check year in header (first 1000 chars)
        header = text[:1000]
        if '2016' in header:
            candidates.append(title)

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-1380107038733155732': 'file_storage/function-call-1380107038733155732.json', 'var_function-call-1380107038733154663': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-10254966279675134776': 'file_storage/function-call-10254966279675134776.json', 'var_function-call-5480804102424637066': [], 'var_function-call-5063725347681925527': 'file_storage/function-call-5063725347681925527.json'}

exec(code, env_args)

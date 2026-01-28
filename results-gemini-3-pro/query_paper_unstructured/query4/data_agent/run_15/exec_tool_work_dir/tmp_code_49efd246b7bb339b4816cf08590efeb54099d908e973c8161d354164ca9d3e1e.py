code = """import json

# Load the result from the previous tool call
with open(locals()['var_function-call-18231062501554874953'], 'r') as f:
    docs = json.load(f)

titles = []
for doc in docs:
    # Check if 2016 is in the first 2000 characters (header/meta)
    # This avoids counting 2016 in references
    if '2016' in doc['text'][:2000]:
        # Clean title
        title = doc['filename'].replace('.txt', '')
        titles.append(title)

print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_function-call-15828363465301237669': 'file_storage/function-call-15828363465301237669.json', 'var_function-call-5049852519434866755': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-18231062501554874953': 'file_storage/function-call-18231062501554874953.json'}

exec(code, env_args)

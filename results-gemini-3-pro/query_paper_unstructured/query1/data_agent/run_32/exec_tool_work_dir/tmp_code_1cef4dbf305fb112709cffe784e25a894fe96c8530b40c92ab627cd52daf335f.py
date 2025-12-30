code = """import json

with open(locals()['var_function-call-10209984453905821604'], 'r') as f:
    paper_docs = json.load(f)

print("__RESULT__:")
matches = []
for doc in paper_docs:
    text = doc['text']
    title = doc['filename']
    if 'food' in text.lower():
        # Find index
        idx = text.lower().find('food')
        snippet = text[max(0, idx-50):min(len(text), idx+50)]
        matches.append({"title": title, "snippet": snippet})

print(json.dumps(matches[:5]))"""

env_args = {'var_function-call-15020890105501723075': ['paper_docs'], 'var_function-call-15020890105501724646': ['Citations', 'sqlite_sequence'], 'var_function-call-10118985144780459012': 'file_storage/function-call-10118985144780459012.json', 'var_function-call-10118985144780458999': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-10209984453905821604': 'file_storage/function-call-10209984453905821604.json', 'var_function-call-10209984453905818035': 'file_storage/function-call-10209984453905818035.json', 'var_function-call-974932691459579436': {'total_citations': 0, 'food_papers': []}}

exec(code, env_args)

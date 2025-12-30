code = """import json
import re

docs_path = locals()['var_function-call-11712304195294590657']
citations_path = locals()['var_function-call-1716571983847186930']

with open(docs_path, 'r') as f:
    docs = json.load(f)

print(f"Total docs: {len(docs)}")

with open(citations_path, 'r') as f:
    citations_list = json.load(f)
print(f"Total citations loaded: {len(citations_list)}")

year_pattern = re.compile(r'\b(20\d{2})\b')

debug_count = 0
for doc in docs[:10]:
    title = doc['filename'].replace('.txt', '')
    text = doc.get('text', '')
    head = text[:1000]
    matches = year_pattern.findall(head)
    valid_years = [int(y) for y in matches if 2000 <= int(y) <= 2025]
    
    pub_year = valid_years[0] if valid_years else None
    has_empirical = 'empirical' in text.lower()
    
    print(f"Title: {title}")
    print(f"Years found: {valid_years}")
    print(f"Pub Year: {pub_year}")
    print(f"Has empirical: {has_empirical}")
    print("-" * 20)
    
print("__RESULT__:")
print("DEBUG_DONE")"""

env_args = {'var_function-call-2488897031636296364': 'file_storage/function-call-2488897031636296364.json', 'var_function-call-2488897031636298801': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-13084840739219341064': 'file_storage/function-call-13084840739219341064.json', 'var_function-call-11712304195294590657': 'file_storage/function-call-11712304195294590657.json', 'var_function-call-14759133979912557114': [{'count(*)': '1405'}], 'var_function-call-1716571983847186930': 'file_storage/function-call-1716571983847186930.json', 'var_function-call-6824277840340661163': []}

exec(code, env_args)

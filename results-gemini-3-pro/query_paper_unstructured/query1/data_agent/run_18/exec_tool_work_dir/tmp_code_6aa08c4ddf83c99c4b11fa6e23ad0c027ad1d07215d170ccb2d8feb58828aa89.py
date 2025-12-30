code = """import json
import re

papers_path = locals()['var_function-call-12584433843491866597']
with open(papers_path, 'r') as f:
    paper_docs = json.load(f)

results = []
for doc in paper_docs[:10]:
    text = doc.get('text', '')
    title = doc.get('filename', '')
    
    # Simple extraction
    # pattern: Author Keywords [text] \n\n
    match = re.search(r"Author Keywords(.*?)\n\n", text, re.DOTALL | re.IGNORECASE)
    kw = match.group(1).strip() if match else "None"
    
    has_food = "food" in text.lower()
    
    results.append([title, kw[:50], has_food])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3783672913394696319': ['paper_docs'], 'var_function-call-3783672913394696700': ['Citations', 'sqlite_sequence'], 'var_function-call-272073867596597133': 'file_storage/function-call-272073867596597133.json', 'var_function-call-272073867596596742': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-9679994414761045024': 'file_storage/function-call-9679994414761045024.json', 'var_function-call-12584433843491866400': 'file_storage/function-call-12584433843491866400.json', 'var_function-call-12584433843491866597': 'file_storage/function-call-12584433843491866597.json', 'var_function-call-3836062097239578025': {'food_paper_count': 0, 'total_citations': 0, 'sample_titles': []}}

exec(code, env_args)

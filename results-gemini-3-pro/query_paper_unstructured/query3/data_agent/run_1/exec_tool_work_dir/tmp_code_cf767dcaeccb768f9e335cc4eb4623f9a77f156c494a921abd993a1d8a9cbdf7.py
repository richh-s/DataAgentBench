code = """import json
import re

# Load citations
with open(locals()['var_function-call-15796312403929804430'], 'r') as f:
    citations_data = json.load(f)

citation_map = {}
for item in citations_data:
    t = item['title']
    c = int(item['citation_count'])
    citation_map[t] = citation_map.get(t, 0) + c

# Load papers
with open(locals()['var_function-call-12278789652942674597'], 'r') as f:
    papers_data = json.load(f)

print(f"Total papers: {len(papers_data)}")

# Inspect first few papers for metadata patterns
for i in range(5):
    p = papers_data[i]
    text = p['text']
    print(f"--- Paper {i} ---")
    print(f"Filename: {p['filename']}")
    print(f"First 200 chars: {text[:200]}")
    
    # Check for lines starting with "Contribution" or containing "Contribution:"
    lines = text.split('\n')
    found_contribution_line = False
    for line in lines:
        if "contribution" in line.lower() and len(line) < 200:
             print(f"Potential metadata line: {line.strip()}")
             found_contribution_line = True
    
    if not found_contribution_line:
        print("No explicit contribution line found.")

print("__RESULT__:")
print(json.dumps("Inspection Done"))"""

env_args = {'var_function-call-7844967085086575341': 'file_storage/function-call-7844967085086575341.json', 'var_function-call-7844967085086573572': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-12278789652942674597': 'file_storage/function-call-12278789652942674597.json', 'var_function-call-15796312403929804430': 'file_storage/function-call-15796312403929804430.json'}

exec(code, env_args)

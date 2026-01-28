code = """import json
import re

# Load the result from the query that was supposed to count/list docs
# Since I'm not sure if it returned all, I'll check the length.
# If it's small (like 1), I'll issue a new query for all docs.

try:
    with open(locals()['var_function-call-10254966279675134776'], 'r') as f:
        docs = json.load(f)
except Exception as e:
    docs = []
    print(f"Error loading file: {e}")

print(f"Loaded {len(docs)} documents.")

# If we have documents, let's process them to find candidates.
# Heuristic for year: Look for 2016 in the first 1000 chars.
# Heuristic for domain: Look for 'physical activity' in the text.

candidates = []

for d in docs:
    text = d.get('text', '')
    filename = d.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check domain
    if 'physical activity' in text.lower():
        # Check year
        # Simple check: is "2016" in the first 500 chars?
        header = text[:500]
        if '2016' in header:
            candidates.append(title)

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-1380107038733155732': 'file_storage/function-call-1380107038733155732.json', 'var_function-call-1380107038733154663': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-10254966279675134776': 'file_storage/function-call-10254966279675134776.json'}

exec(code, env_args)

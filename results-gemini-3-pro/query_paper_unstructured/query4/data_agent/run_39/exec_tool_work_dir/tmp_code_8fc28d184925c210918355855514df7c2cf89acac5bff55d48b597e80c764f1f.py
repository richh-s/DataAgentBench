code = """import json
import re

# Load the result from MongoDB query
with open('var_function-call-10008279034646517979.json', 'r') as f:
    papers = json.load(f)

matching_titles = []

for paper in papers:
    text = paper.get('text', '')
    # Check first 500 characters for year 2016
    header = text[:500]
    
    # Simple check for 2016. 
    # Also check for '16 if preceded by conference acronyms, but 2016 is safer.
    # Common headers: "CHI '16", "Ubicomp '16", "September 2016", "Copyright 2016"
    if '2016' in header:
        # Extract title
        filename = paper.get('filename', '')
        if filename.endswith('.txt'):
            title = filename[:-4]
            matching_titles.append(title)
    # Check for '16 with conference names just in case "2016" is not explicitly written (less likely)
    elif re.search(r"(CHI|UbiComp|CSCW|DIS|IUI|OzCHI|TEI|AH)\s*'?16", header, re.IGNORECASE):
        filename = paper.get('filename', '')
        if filename.endswith('.txt'):
            title = filename[:-4]
            matching_titles.append(title)

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-14274151391044550289': 'file_storage/function-call-14274151391044550289.json', 'var_function-call-14274151391044549302': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-10008279034646517979': 'file_storage/function-call-10008279034646517979.json'}

exec(code, env_args)

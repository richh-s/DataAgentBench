code = """import json, os, re

# Access the file path variable
file_path = locals()['var_functions.query_db:2']
print("File path value:", type(file_path))

# Load the paper documents
with open(file_path) as f:
    paper_docs = json.load(f)

print(f"Loaded {len(paper_docs)} documents")

# Extract information
papers_2016_pa = []
for doc in paper_docs:
    # Get title from filename
    title = doc.get('filename', '').replace('.txt', '')
    if not title:
        continue
    
    # Get year from text
    year = None
    text = doc.get('text', '')
    matches = re.findall(r'\b20\d{2}\b', text[:1000])
    for m in matches:
        y = int(m)
        if 2010 <= y <= 2020:
            year = y
            break
    
    # Check domain
    is_pa = 'physical activity' in text.lower()
    
    if year == 2016 and is_pa:
        papers_2016_pa.append(title)

print(f"Found {len(papers_2016_pa)} 2016 PA papers")
print('__RESULT__:')
print(json.dumps(papers_2016_pa))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)

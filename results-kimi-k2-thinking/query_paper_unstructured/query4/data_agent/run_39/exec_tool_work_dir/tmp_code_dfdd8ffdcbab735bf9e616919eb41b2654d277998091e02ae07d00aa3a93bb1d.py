code = """import json
import re
import os

# Load the paper documents
paper_docs_file = locals()['var_functions.query_db:14']
print(f"Loading papers from: {paper_docs_file}")

with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

print(f"Total papers loaded: {len(paper_docs)}")

# Extract paper information
papers_2016_pa = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    # Get title
    title = os.path.splitext(filename)[0]
    
    # Check for 2016 year
    year_matches = re.findall(r'\b(20\d{2})\b', text)
    if '2016' not in year_matches:
        continue
    
    # Check for physical activity domain
    text_lower = text.lower()
    pa_keywords = ['physical activity', 'fitness', 'exercise', 'activity tracking', 
                   'steps', 'walking', 'running', 'workout', 'active', 'fitbit']
    
    if any(kw in text_lower for kw in pa_keywords):
        papers_2016_pa.append(title)

print(f"Found {len(papers_2016_pa)} 2016 physical activity papers")
for t in papers_2016_pa:
    print(f"  - {t}")

# Load citation data
citations_file = locals()['var_functions.query_db:16']
print(f"\nLoading citations from: {citations_file}")

with open(citations_file, 'r') as f:
    citations = json.load(f)

citation_dict = {item['title']: int(item['total_citations']) for item in citations}
print(f"Total citation records: {len(citation_dict)}")

# Match papers with citations
results = []
for title in papers_2016_pa:
    if title in citation_dict:
        results.append({
            'title': title,
            'total_citations': citation_dict[title]
        })
        print(f"Found citations: {title} ({citation_dict[title]})")

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)

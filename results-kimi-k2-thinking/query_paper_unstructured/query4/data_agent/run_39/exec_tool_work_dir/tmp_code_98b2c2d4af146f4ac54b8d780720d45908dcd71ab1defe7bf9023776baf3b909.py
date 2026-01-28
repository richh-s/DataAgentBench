code = """import json
import re
import os

# Get the paper documents file path
paper_docs_file = locals()['var_functions.query_db:14']
print(f"Loading paper documents from: {paper_docs_file}")

with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

print(f"Total paper documents: {len(paper_docs)}")

# Process papers
papers_2016_physical_activity = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    # Extract title
    title = os.path.splitext(filename)[0]
    
    # Extract year - look for 2016 specifically
    year = None
    year_matches = re.findall(r'\b(20\d{2})\b', text)
    for match in year_matches:
        yr = int(match)
        if yr == 2016:
            year = yr
            break
    
    # Skip if not 2016
    if year != 2016:
        continue
    
    # Check for physical activity domain
    text_lower = text.lower()
    physical_activity_keywords = [
        'physical activity', 'fitness', 'exercise', 'activity tracking', 
        'steps', 'walking', 'running', 'workout', 'active', 'fitbit'
    ]
    
    is_physical_activity = any(keyword in text_lower for keyword in physical_activity_keywords)
    
    if is_physical_activity:
        papers_2016_physical_activity.append(title)

print(f"Found {len(papers_2016_physical_activity)} papers from 2016 in physical activity domain")
for title in papers_2016_physical_activity:
    print(f"- {title}")

# Get citation data file path
citations_file = locals()['var_functions.query_db:16']
print(f"\nLoading citation data from: {citations_file}")

with open(citations_file, 'r') as f:
    citations_data = json.load(f)

print(f"Total papers in citation database: {len(citations_data)}")

# Create lookup dictionary
citation_dict = {item['title']: int(item['total_citations']) for item in citations_data}

# Match papers with citations
final_results = []
for title in papers_2016_physical_activity:
    if title in citation_dict:
        final_results.append({
            'title': title,
            'total_citation_count': citation_dict[title]
        })
        print(f"MATCHED: {title} - {citation_dict[title]} citations")
    else:
        print(f"NO CITATION DATA: {title}")

print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)

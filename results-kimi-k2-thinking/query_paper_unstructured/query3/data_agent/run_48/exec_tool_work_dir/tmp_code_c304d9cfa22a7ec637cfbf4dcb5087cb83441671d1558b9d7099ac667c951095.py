code = """import json
import re

# Load paper documents
with open('var_functions.query_db:24.json', 'r') as f:
    paper_docs = json.load(f)

# Extract paper information
papers_info = []
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    year = None
    year_match = re.search(r"(20[12][0-9])", text[:1000])
    if year_match:
        year = int(year_match.group(1))
    
    contribution = None
    text_lower = text.lower()
    if 'empirical' in text_lower:
        contribution = 'empirical'
    elif 'theoretical' in text_lower:
        contribution = 'theoretical'
    elif 'survey' in text_lower:
        contribution = 'survey'
    elif 'system' in text_lower or 'prototype' in text_lower:
        contribution = 'artifact'
    
    papers_info.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

# Filter empirical papers after 2016
empirical_papers = [p for p in papers_info if p['contribution'] == 'empirical' and p['year'] and p['year'] > 2016]

# Load citation data
with open('var_functions.query_db:28.json', 'r') as f:
    citations = json.load(f)

# Create a dictionary for easy lookup
citation_dict = {c['title']: int(c['total_citations']) for c in citations}

# Join and calculate total citations
result = []
for paper in empirical_papers:
    title = paper['title']
    total_citations = citation_dict.get(title, 0)
    result.append({
        'title': title,
        'total_citations': total_citations
    })

# Sort by citation countesult_sorted = sorted(result, key=lambda x: x['total_citations'], reverse=True)

print("__RESULT__:")
print(json.dumps({"papers": result_sorted, "count": len(result_sorted)}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:7': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)

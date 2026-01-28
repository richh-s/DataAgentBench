code = """import json, os, re

# Access the stored query results
paper_docs_var = locals()['var_functions.query_db:34']
citations_var = locals()['var_functions.query_db:28']

# Load the paper documents
with open(paper_docs_var, 'r') as f:
    paper_docs = json.load(f)

# Load the citations
with open(citations_var, 'r') as f:
    citations = json.load(f)

# Extract paper information
papers_info = []
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    # Extract year
    year = None
    # Look for 4-digit year patterns
    year_match = re.search(r'20[12][0-9]', text[:2000])
    if year_match:
        year = int(year_match.group())
    
    # Identify contribution type
    contribution = None
    text_lower = text.lower()
    
    if 'empirical' in text_lower or 'empirically' in text_lower:
        contribution = 'empirical'
    elif 'theoretical' in text_lower or 'theory' in text_lower:
        contribution = 'theoretical'
    elif 'survey' in text_lower or 'literature review' in text_lower:
        contribution = 'survey'
    elif any(word in text_lower for word in ['system', 'prototype', 'tool', 'application']):
        contribution = 'artifact'
    
    papers_info.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

# Filter for empirical papers published after 2016
empirical_papers_2017 = [
    p for p in papers_info 
    if p['contribution'] == 'empirical' and p['year'] and p['year'] > 2016
]

# Create citation lookup dictionary
citation_dict = {c['title']: int(c['total_citations']) for c in citations}

# Join papers with their citation counts
result = []
for paper in empirical_papers_2017:
    title = paper['title']
    total_citations = citation_dict.get(title, 0)
    result.append({
        'title': title,
        'total_citations': total_citations
    })

# Sort by citation count descending
result_sorted = sorted(result, key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps({'papers': result_sorted, 'total_count': len(result_sorted)}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:7': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)

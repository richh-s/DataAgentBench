code = """import json
import re

# Get the file paths
paper_docs_path = locals()['var_functions.query_db:2']
citations_path = locals()['var_functions.query_db:5']

# Load the data
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

with open(citations_path, 'r') as f:
    citations = json.load(f)

# Step 1: Extract paper information from MongoDB documents
papers_info = []

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text (look for patterns like 2017, 2018, etc.)
    year_match = re.search(r"\b(20(1[7-9]|2[0-9]|3[0-9]))\b", text)
    year = int(year_match.group(1)) if year_match else None
    
    # Extract contribution type (look for 'empirical', 'artifact', 'theoretical', 'survey', 'methodological')
    contribution = ''
    if text:
        text_lower = text.lower()
        contrib_keywords = ['empirical', 'artifact', 'theoretical', 'survey', 'methodological']
        for keyword in contrib_keywords:
            if keyword in text_lower:
                contribution = keyword
                break
    
    papers_info.append({
        'title': title,
        'year': year,
        'contribution': contribution,
        'filename': filename
    })

# Step 2: Process citations data
# Build a dict to aggregate citation counts by paper title
citation_counts = {}
for citation in citations:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    citation_counts[title] = citation_counts.get(title, 0) + count

# Step 3: Join and filter
results = []

for paper in papers_info:
    if paper['year'] and paper['year'] > 2016 and paper['contribution'] == 'empirical':
        total_citations = citation_counts.get(paper['title'], 0)
        results.append({
            'title': paper['title'],
            'total_citation_count': total_citations,
            'year': paper['year']
        })

# Sort by citation count (descending)
results = sorted(results, key=lambda x: x['total_citation_count'], reverse=True)

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'paper_docs_path': 'file_storage/functions.query_db:2.json', 'citations_path': 'file_storage/functions.query_db:5.json'}}

exec(code, env_args)

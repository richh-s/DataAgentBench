code = """import json
import pandas as pd
import re
from collections import defaultdict

# Load paper documents
paper_docs_var = locals().get('var_functions.query_db:14', [])
print("Paper docs variable type:", type(paper_docs_var))

# Load citations data
citations_var = locals().get('var_functions.query_db:15', [])
print("Citations variable type:", type(citations_var))

# If they are strings (file paths), load them
if isinstance(paper_docs_var, str):
    with open(paper_docs_var, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_var

if isinstance(citations_var, str):
    with open(citations_var, 'r') as f:
        citations = json.load(f)
else:
    citations = citations_var

print("Paper docs count:", len(paper_docs))
print("Citations count:", len(citations))

# Process paper docs to extract title, year, and domain
paper_info = []
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year
    year = None
    # Look for year patterns in the text
    year_match = re.search(r'(20\d{2})', text)
    if year_match:
        year = int(year_match.group(1))
    
    # Extract domain - specifically look for physical activity
    domain = []
    lower_text = text.lower()
    
    # Keywords for physical activity domain
    activity_keywords = ['physical activity', 'fitness', 'exercise', 'steps', 'walking', 
                        'running', 'workout', 'activit', 'fitbit']
    
    # Other domains for completeness
    if any(keyword in lower_text for keyword in activity_keywords):
        domain.append('physical activity')
    
    if title and year:
        paper_info.append({
            'title': title,
            'year': year,
            'domains': domain
        })

# Filter papers from 2016 in physical activity domain
papers_2016_activity = [p for p in paper_info if p['year'] == 2016 and 'physical activity' in p['domains']]
print("\nPapers from 2016 in physical activity domain:", len(papers_2016_activity))

# Convert citations to DataFrame
df_citations = pd.DataFrame(citations)
print("\nCitations columns:", df_citations.columns.tolist())
print("Citations shape:", df_citations.shape)

# Sum all citations per title (all years combined)
total_citations = df_citations.groupby('title')['total_citations'].sum().reset_index()
print("\nTotal citations table shape:", total_citations.shape)

# Find matching citations for our 2016 physical activity papers
result = []
for paper in papers_2016_activity:
    title = paper['title']
    # Check if title exists in citations (might need approximate matching)
    match = total_citations[total_citations['title'].str.contains(title, case=False, na=False)]
    if not match.empty:
        citation_count = int(match.iloc[0]['total_citations'])
        result.append({
            'title': title,
            'total_citation_count': citation_count,
            'year': 2016
        })
    else:
        # Direct match attempt
        direct_match = total_citations[total_citations['title'] == title]
        if not direct_match.empty:
            citation_count = int(direct_match.iloc[0]['total_citations'])
            result.append({
                'title': title,
                'total_citation_count': citation_count,
                'year': 2016
            })

print("\nResults found:", len(result))
for r in result:
    print(f"{r['title']}: {r['total_citation_count']} citations")

# Save for debugging
result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json'}

exec(code, env_args)

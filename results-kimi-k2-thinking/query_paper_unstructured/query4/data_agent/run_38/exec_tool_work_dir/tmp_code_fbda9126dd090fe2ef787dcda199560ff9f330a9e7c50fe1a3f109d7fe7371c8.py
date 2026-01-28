code = """import json
import re
import os

# Read the file path for paper documents
paper_docs_file = var_functions.query_db:8

# Read paper documents
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Read the file path for citations
citations_file = var_functions.query_db:5

# Read citations
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Extract paper information
paper_info = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Extract year from text - look for 4-digit years near the beginning
    year = None
    # Look for patterns like '2016' or conference years
    year_matches = re.findall(r"\b(20\d{2})\b", text[:2000])
    if year_matches:
        # Filter for reasonable publication years (2010-2025)
        valid_years = [int(y) for y in year_matches if 2010 <= int(y) <= 2025]
        if valid_years:
            year = min(valid_years)  # Use the earliest valid year found
    
    # Check if it's a 2016 paper
    if year != 2016:
        continue
    
    # Extract domain - check for physical activity related terms
    text_lower = text.lower()
    
    # Look for physical activity domain indicators
    domain_indicators = [
        'physical activity',
        'fitness',
        'exercise',
        'activity tracking',
        'activity tracker',
        'workout',
        'sedentary'
    ]
    
    is_physical_activity = any(indicator in text_lower for indicator in domain_indicators)
    
    if is_physical_activity:
        paper_info.append({
            '_id': doc['_id'],
            'title': title,
            'year': year,
            'domain': 'physical activity'
        })

print(f"Found {len(paper_info)} papers from 2016 in physical activity domain")

# Process citations data
import pandas as pd

df_citations = pd.DataFrame(citations)
# Convert citation_count to int
df_citations['citation_count'] = df_citations['citation_count'].astype(int)

# Group by title and sum citations
if not df_citations.empty:
    df_citation_sums = df_citations.groupby('title')['citation_count'].sum().reset_index()
    df_citation_sums.columns = ['title', 'total_citations']
else:
    df_citation_sums = pd.DataFrame(columns=['title', 'total_citations'])

# Create DataFrame for physical activity papers
if paper_info:
    df_physical_activity = pd.DataFrame(paper_info)
    
    # Merge with citation data
    result = pd.merge(df_physical_activity, df_citation_sums, on='title', how='left')
    result = result.fillna({'total_citations': 0})
    result['total_citations'] = result['total_citations'].astype(int)
    
    # Select and sort by citations
    final_result = result[['title', 'total_citations']].sort_values('total_citations', ascending=False)
    
    # Convert to list of dicts
    output = final_result.to_dict('records')
else:
    output = []

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

code = """import json
import re
from collections import defaultdict
import os

# Access the variables from storage
citations_var = var_functions.query_db:5
paper_docs_var = var_functions.query_db:6

# Read citations data
if isinstance(citations_var, str) and citations_var.endswith('.json'):
    with open(citations_var, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_var

# Read paper documents data  
if isinstance(paper_docs_var, str) and paper_docs_var.endswith('.json'):
    with open(paper_docs_var, 'r') as f:
        paper_docs_data = json.load(f)
else:
    paper_docs_data = paper_docs_var

# Initialize results storage
papers_2016_with_citations = []

# Create a mapping from title to total citation count
title_to_total_citations = defaultdict(int)
for citation in citations_data:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    if title:
        title_to_total_citations[title] += count

# Process each paper document
for doc in paper_docs_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
        
    # Extract title from filename
    title = filename.replace('.txt', '').strip()
    
    # Extract year from text (look in first 1000 characters)
    text_start = text[:1000]
    year = None
    
    # Look for year patterns
    year_match = re.search(r"\b(20\d{2})\b", text_start)
    if year_match:
        year = int(year_match.group(1))
    else:
        # Look for venue year like '15
        venue_match = re.search(r"[A-Z]+\s*'?(\d{2})\b", text_start)
        if venue_match:
            year_str = venue_match.group(1)
            if int(year_str) >= 10:  # Assuming 2010s
                year = int('20' + year_str)
    
    # Skip if not 2016
    if year != 2016:
        continue
    
    # Check if paper is about physical activity (case insensitive)
    text_lower = text.lower()
    is_physical_activity = (
        'physical activity' in text_lower or
        'physical fitness' in text_lower or
        'exercise' in text_lower
    )
    
    if not is_physical_activity:
        continue
    
    # Get total citations for this paper
    total_citations = title_to_total_citations.get(title, 0)
    
    papers_2016_with_citations.append({
        'title': title,
        'total_citation_count': total_citations
    })

# Sort by citation count (descending)
papers_2016_with_citations.sort(key=lambda x: x['total_citation_count'], reverse=True)

print('__RESULT__:')
print(json.dumps(papers_2016_with_citations))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

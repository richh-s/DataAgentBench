code = """import json
import re

# Load all paper documents
papers_file_path = locals()['var_functions.query_db:16']
if isinstance(papers_file_path, str):
    with open(papers_file_path, 'r') as f:
        papers = json.load(f)
else:
    papers = papers_file_path

# Load all citations
citations_file_path = locals()['var_functions.query_db:10']
if isinstance(citations_file_path, str):
    with open(citations_file_path, 'r') as f:
        citations = json.load(f)
else:
    citations = citations_file_path

# Function to extract paper metadata
paper_metadata = []
for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else 'Unknown'
    
    # Extract year from text (look for patterns like 2017, '18, etc.)
    year = None
    year_patterns = [
        r"(?:\b|')((?:19|20)\d{2})(?:\b|'|\s|-|\))",  # 2015, '15, 2017), etc.
        r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*['\s]((?:19|20)\d{2})"
    ]
    
    for pattern in year_patterns:
        year_match = re.search(pattern, text[:2000])  # Search in first 2000 chars
        if year_match:
            year = int(year_match.group(1))
            if 1900 <= year <= 2100:  # Reasonable year range
                break
    
    # Check if text contains empirical study indicators
    contribution = []
    text_lower = text.lower()
    
    # Check for empirical contribution indicators
    empirical_keywords = ['empirical', 'study', 'experiment', 'survey', 'interview', 'data collection', 'user study', 'field study', 'case study']
    if any(keyword in text_lower for keyword in empirical_keywords):
        contribution.append('empirical')
    
    # Check for other contributions
    if 'theor' in text_lower:
        contribution.append('theoretical')
    if 'artifact' in text_lower or 'prototype' in text_lower or 'system' in text_lower:
        contribution.append('artifact')
    if 'survey' in text_lower and 'literature' in text_lower:
        contribution.append('survey')
    if 'method' in text_lower:
        contribution.append('methodological')
    
    # Defaults
    if not year:
        year = 1900
    if not contribution:
        contribution = ['unknown']
    else:
        contribution = contribution
        
    paper_metadata.append({
        'title': title,
        'year': year,
        'contribution': ','.join(contribution)  # Convert to string for easy joining
    })

# Display some info for debugging
print('__RESULT__:')
print(json.dumps({
    "papers_processed": len(paper_metadata),
    "sample_papers": paper_metadata[:10],
    "citations_count": len(citations)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'total_papers': 5}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)

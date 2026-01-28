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

# Parse papers more carefully
papers_with_year = []
contribution_keywords = ['empirical', 'artifact', 'theoretical', 'survey', 'methodological']

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if not text:
        continue
    
    # Extract year - look for date patterns in paper headers
    year_phrases = re.findall(r"\b(20(1[7-9]|2[0-9]|3[0-9]))\b", text)
    if year_phrases:
        # Take the first year found (usually publication year)
        year = int(year_phrases[0][1])
    else:
        year = None
    
    # Determine contribution type - look for keywords like "EMPIRICAL" or "empirical study"
    text_lower = text.lower()
    contribution = None
    for keyword in contribution_keywords:
        if keyword in text_lower and ('study' in text_lower or keyword == 'empirical'):
            contribution = keyword
            break
    
    papers_with_year.append({
        'title': title,
        'year': year,
        'contribution': contribution,
        'text_snippet': text[:200]  # First 200 chars for debugging
    })

# Build citation aggregate
citation_totals = {}
for citation in citations:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    if title in citation_totals:
        citation_totals[title] += count
    else:
        citation_totals[title] = count

# Debug: List all papers
debug_info = {
    'papers_parsed': papers_with_year,
    'citation_totals_sample': dict(list(citation_totals.items())[:5])
}

print('__RESULT__:')
print(json.dumps(debug_info, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'paper_docs_path': 'file_storage/functions.query_db:2.json', 'citations_path': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:14': [], 'var_functions.execute_python:16': {'first_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'total_papers': 5, 'total_citations': 1405, 'citation_sample': {'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}}}

exec(code, env_args)

code = """import json
import re
from collections import defaultdict

# Get the file path for paper_docs data
paper_docs_file = var_functions.query_db:2

# Read paper_docs data
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Citations data is directly available
# var_functions.query_db:5 contains the citations list
citations = var_functions.query_db:5

# Process papers
papers_info = []

for doc in paper_docs:
    # Extract title from filename
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Get full text
    text = doc.get('text', '')
    
    # Extract year (look for 20xx pattern)
    year_match = re.search(r'(20[0-2][0-9])', text[:2000])
    year = int(year_match.group(1)) if year_match else None
    
    # Extract contribution types
    contributions = []
    text_lower = text.lower()
    
    # Check for empirical contributions
    if re.search(r'\b(empirical|study|survey|interview|experiment|evaluation|user study|field study|case study)\b', text_lower):
        contributions.append('empirical')
    
    if re.search(r'\b(system|prototype|tool|application|app|design|implementation|artifact)\b', text_lower):
        contributions.append('artifact')
    
    if re.search(r'\b(theoretical|theory|model|framework|conceptual|concept)\b', text_lower):
        contributions.append('theoretical')
    
    if re.search(r'\b(literature review|systematic review|meta.analysis)\b', text_lower):
        contributions.append('survey')
    
    if re.search(r'\b(methodological|methodology|method|approach|technique)\b', text_lower):
        contributions.append('methodological')
    
    papers_info.append({
        'title': title,
        'year': year,
        'contributions': contributions
    })

# Process citations - group by title
citations_by_title = defaultdict(int)
for citation in citations:
    cit_title = citation.get('title', '').lower()
    cit_count = int(citation.get('citation_count', 0))
    citations_by_title[cit_title] += cit_count

# Find papers that match criteria
result_papers = []
for paper in papers_info:
    year = paper.get('year')
    contributions = paper.get('contributions', [])
    
    # Check if published after 2016 and has empirical contribution
    if year and year > 2016 and 'empirical' in contributions:
        title = paper['title']
        title_lower = title.lower()
        
        # Get total citations
        total_citations = citations_by_title.get(title_lower, 0)
        
        result_papers.append({
            'title': title,
            'total_citations': total_citations
        })

# Sort by citation count descending
result_papers.sort(key=lambda x: x['total_citations'], reverse=True)

# Return as JSON string
import sys
print('__RESULT__:')
print(json.dumps(result_papers))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence']}

exec(code, env_args)

code = """import json
import os
import re

# Load citations data
citations_key = 'var_functions.query_db:0'
citations_file = locals()[citations_key]
if isinstance(citations_file, str) and os.path.exists(citations_file):
    with open(citations_file, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = citations_file

# Load paper documents data
papers_key = 'var_FUNCTIONS.QUERY_DB:6'
papers_file = locals()['var_functions.query_db:6']
if isinstance(papers_file, str) and os.path.exists(papers_file):
    with open(papers_file, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = papers_file

# Identify CHI papers
chi_papers = {}

for doc in paper_docs:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Look for CHI venue indicators in the text
    # Check first 20 lines where venue info usually appears
    lines = text.split('\n')[:20]
    header_text = ' '.join(lines).upper()
    
    # Check for various CHI patterns
    chi_patterns = [
        r'CHI\s*\'\s*\d{2}',     # CHI '15
        r'CHI\s*\d{4}',         # CHI 2015
        r'CHI\s+CONFERENCE',
        r'PROCEEDINGS\s+OF\s+CHI',
        r'CHI\s+\d{2}\s*,',      # CHI 15,
        r'CHI\s+\d{4}\s*,',      # CHI 2015,
    ]
    
    is_chi = False
    for pattern in chi_patterns:
        if re.search(pattern, header_text, re.IGNORECASE):
            is_chi = True
            break
    
    if is_chi:
        chi_papers[title] = True

# Match citations and sum counts
total_citations = 0
matched_papers = 0

for citation in citations_2020:
    citation_title = citation.get('title', '')
    if citation_title in chi_papers:
        count = int(citation.get('citation_count', 0))
        total_citations += count
        matched_papers += 1

result = {
    'chi_papers_identified': len(chi_papers),
    'chi_papers_cited_in_2020': matched_papers,
    'total_citation_count_2020': total_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 188, 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'Data loaded successfully', 'var_functions.execute_python:14': {'chi_papers_total': 5, 'chi_papers_cited': 4, 'total_citations_2020': 243, 'sample_matched_titles': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'A Lived Informatics Model of Personal Informatics', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_functions.execute_python:18': {'chi_papers_total': 0, 'chi_papers_cited_2020': 0, 'total_citations_2020': 0}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)

code = """import json
import os
import re

# Load citations data
citations_file = locals()['var_functions.query_db:0']
if isinstance(citations_file, str) and os.path.exists(citations_file):
    with open(citations_file, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = citations_file

# Load CHI papers data
chi_papers_file = locals()['var_functions.query_db:26']
if isinstance(chi_papers_file, str) and os.path.exists(chi_papers_file):
    with open(chi_papers_file, 'r') as f:
        chi_papers_docs = json.load(f)
else:
    chi_papers_docs = chi_papers_file

# Extract titles and verify they are CHI papers
chi_titles = set()

for doc in chi_papers_docs:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Verify it's a CHI paper by checking for conference indicators
    text_upper = text.upper()
    
    # Look for conference header patterns
    chi_indicators = [
        'PROCEEDINGS OF CHI',
        'CHI CONFERENCE',
        'CHI \'\d{2}',
        'CHI \d{4}',
        'ACM CHI',
        'CHI \d{2},',
        'CHI \d{4},'
    ]
    
    is_chi_paper = False
    for indicator in chi_indicators:
        if re.search(indicator, text_upper):
            is_chi_paper = True
            break
    
    if is_chi_paper:
        chi_titles.add(title)

# Match with citations and sum counts
total_citations = 0
matched_count = 0

for citation in citations_2020:
    citation_title = citation.get('title', '')
    if citation_title in chi_titles:
        count = int(citation.get('citation_count', 0))
        total_citations += count
        matched_count += 1

result = {
    'chi_papers_found': len(chi_titles),
    'chi_papers_cited_in_2020': matched_count,
    'total_2020_citations': total_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 188, 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'Data loaded successfully', 'var_functions.execute_python:14': {'chi_papers_total': 5, 'chi_papers_cited': 4, 'total_citations_2020': 243, 'sample_matched_titles': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'A Lived Informatics Model of Personal Informatics', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_functions.execute_python:18': {'chi_papers_total': 0, 'chi_papers_cited_2020': 0, 'total_citations_2020': 0}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)

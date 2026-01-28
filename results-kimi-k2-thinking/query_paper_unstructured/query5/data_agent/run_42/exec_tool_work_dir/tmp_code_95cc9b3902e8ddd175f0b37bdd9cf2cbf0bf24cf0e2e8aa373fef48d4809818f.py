code = """import json
import os
import re

# Load all citations for 2020
citations_data = locals()['var_functions.query_db:0']
if isinstance(citations_data, str) and os.path.exists(citations_data):
    with open(citations_data, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = citations_data

# Load a sample of paper docs to understand structure
papers_data = locals()['var_functions.query_db:6']
if isinstance(papers_data, str) and os.path.exists(papers_data):
    with open(papers_data, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = papers_data

# Create a title to venue mapping by searching for clear CHI indicators
chi_titles = set()

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    
    # Look for CHI venue indicators - more specific patterns
    text_upper = text.upper()
    
    # Check if it contains CHI conference info
    if 'CHI' in text_upper:
        # Check for common conference patterns (avoid false positives)
        lines = text.split('\n')
        for i, line in enumerate(lines[:10]):  # Check first 10 lines (header area)
            line_upper = line.upper()
            if 'CHI' in line_upper and any(x in line_upper for x in ['PROCEEDINGS', 'CONFERENCE', 'PAPER']):
                # Additional checks to avoid common words containing CHI
                words = line_upper.split()
                for word in words:
                    if word == 'CHI' or word.startswith('CHI\'') or word.startswith('CHI20'):
                        chi_titles.add(title)
                        break

# Now match with citations
total_citations = 0
matched_papers = 0

for citation in citations_2020:
    citation_title = citation.get('title', '')
    if citation_title in chi_titles:
        count = int(citation.get('citation_count', 0))
        total_citations += count
        matched_papers += 1

result = {
    'chi_papers_identified': len(chi_titles),
    'chi_papers_cited_in_2020': matched_papers,
    'total_citation_count': total_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 188, 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'Data loaded successfully', 'var_functions.execute_python:14': {'chi_papers_total': 5, 'chi_papers_cited': 4, 'total_citations_2020': 243, 'sample_matched_titles': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'A Lived Informatics Model of Personal Informatics', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_functions.execute_python:18': {'chi_papers_total': 0, 'chi_papers_cited_2020': 0, 'total_citations_2020': 0}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)

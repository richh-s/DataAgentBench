code = """import json
import os
import re

# Load data
citations_data = locals()['var_functions.query_db:0']
if isinstance(citations_data, str) and os.path.exists(citations_data):
    with open(citations_data, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = citations_data

papers_data = locals()['var_functions.query_db:6']
if isinstance(papers_data, str) and os.path.exists(papers_data):
    with open(papers_data, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = papers_data

# Find CHI papers
chi_papers = set()

for doc in paper_docs:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Check for CHI in the text using simple string matching
    text_upper = text.upper()
    if 'CHI' in text_upper:
        # Additional checks to avoid false positives
        # Look for conference patterns
        conference_indicators = [
            'PROCEEDINGS', 'CONFERENCE', 'PAPER', 'PUBLISHED',
            'ACM', 'IEEE', 'WORKSHOP', 'SYMPOSIUM'
        ]
        
        has_indicator = any(indicator in text_upper for indicator in conference_indicators)
        
        if has_indicator:
            # Verify it's not just a random CHI word
            # Count occurrences and context
            chi_count = text_upper.count('CHI')
            if chi_count < 10:  # Not too many occurrences (avoid common words)
                chi_papers.add(title)

# Match with citations
total_citations = 0
chi_citation_count = 0

for citation in citations_2020:
    citation_title = citation.get('title', '')
    if citation_title in chi_papers:
        count = int(citation.get('citation_count', 0))
        total_citations += count
        chi_citation_count += 1

result = {
    'chi_papers_total': len(chi_papers),
    'chi_papers_cited_2020': chi_citation_count,
    'total_citations_2020': total_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 188, 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'Data loaded successfully', 'var_functions.execute_python:14': {'chi_papers_total': 5, 'chi_papers_cited': 4, 'total_citations_2020': 243, 'sample_matched_titles': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'A Lived Informatics Model of Personal Informatics', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}}

exec(code, env_args)

code = """import json
import re

# Read citations data
citations_file = locals()['var_functions.query_db:0']
citations_data = []
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Read paper documents
papers_file = locals()['var_functions.query_db:4']
papers_data = []
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

chi_papers = []
for paper in papers_data:
    filename = paper['filename']
    text = paper['text']
    title = filename.replace('.txt', '')
    
    text_upper = text.upper()
    
    # Check for CHI in various formats
    is_chi = False
    if 'CHI' in text_upper:
        # Verify it's a conference paper, not just random occurrence
        header = text[:1000]
        header_upper = header.upper()
        
        # Look for conference-related patterns with CHI
        conference_patterns = [
            'PROCEEDINGS OF THE',
            'CONFERENCE ON HUMAN FACTORS',
            'ACM CHI',
            'CHI CONFERENCE',
            'CHI TO APPEAR'
        ]
        
        for pattern in conference_patterns:
            if pattern in header_upper and 'CHI' in header_upper:
                # Make sure it's not a different venue
                venue_check = header_upper
                if any(venue in venue_check for venue in ['UBICOMP', 'CSCW', 'DIS', 'PERVASIVEHEALTH', 'WWW', 'IUI', 'OZCHI', 'TEI', 'AH']):
                    break
                is_chi = True
                break
    
    if is_chi:
        chi_papers.append(title.lower().strip())

# Match with citations
chi_citation_counts = []
for citation in citations_data:
    cite_title = citation['title'].lower().strip()
    if cite_title in chi_papers:
        chi_citation_counts.append(int(citation['citation_count']))

total_citation_count = sum(chi_citation_counts)
chi_papers_count = len(chi_citation_counts)

result = {
    'total_citation_count': total_citation_count,
    'chi_papers_count': chi_papers_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'total_citation_count': 243, 'chi_papers_identified': 4, 'sample_chi_papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': 16, 'venue': 'CHI'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': 77, 'venue': 'CHI'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': 98, 'venue': 'CHI'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': 52, 'venue': 'CHI'}]}}

exec(code, env_args)

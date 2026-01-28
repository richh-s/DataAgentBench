code = """import json
import re

# Read the citations data
citations_file = locals()['var_functions.query_db:0']
citations_data = []
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Read the paper documents  
papers_file = locals()['var_functions.query_db:4']
papers_data = []
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

# Build dictionary of CHI papers with careful detection
chi_papers = {}

for paper in papers_data:
    filename = paper['filename']
    text = paper['text']
    title = filename.replace('.txt', '')
    
    # Look for CHI conference information
    # Check first 2000 characters where conference header is
    header = text[:2000]
    
    # Multiple patterns to identify CHI papers
    chi_patterns = [
        (r'CHI\s*\'\d{2}', 'CHI'),
        (r'CHI\s*\d{4}', 'CHI'), 
        (r'Proceedings of the .*?CHI', 'CHI'),
        (r'ACM Conference on Human Factors', 'CHI'),
        (r'Conference on Human Factors in Computing Systems', 'CHI')
    ]
    
    is_chi = False
    for pattern, venue in chi_patterns:
        if re.search(pattern, header, re.IGNORECASE):
            # Verify context - look for conference/proceedings
            context_window = header[max(0, re.search(pattern, header, re.IGNORECASE).start()-200):re.search(pattern, header, re.IGNORECASE).end()+200]
            
            if re.search(r'(conference|proceedings|paper|ACM)', context_window, re.IGNORECASE):
                # Extra check: ensure not a different venue
                other_venues = ['UBICOMP', 'CSCW', 'DIS', 'PERVASIVEHEALTH', 'WWW', 'IUI', 'OZCHI', 'TEI', 'AH']
                has_other = any(venue in header.upper() for venue in other_venues)
                
                if not has_other:
                    is_chi = True
                    break
    
    if is_chi:
        chi_papers[title.lower().strip()] = title

# Match with citations data
total_citation_sum = 0
matched_chi_papers = []

for citation in citations_data:
    cite_title = citation['title'].lower().strip()
    citation_count = int(citation['citation_count'])
    
    if cite_title in chi_papers:
        total_citation_sum += citation_count
        matched_chi_papers.append({
            'title': citation['title'],
            'citations_2020': citation_count
        })

result = {
    'total_citations_for_chi_papers_in_2020': total_citation_sum,
    'number_of_chi_papers_cited': len(matched_chi_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'total_citation_count': 243, 'chi_papers_identified': 4, 'sample_chi_papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': 16, 'venue': 'CHI'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': 77, 'venue': 'CHI'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': 98, 'venue': 'CHI'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': 52, 'venue': 'CHI'}]}, 'var_functions.execute_python:12': {'total_citation_count': 0, 'chi_papers_count': 0}, 'var_functions.execute_python:14': {'total_citation_count': 0, 'number_of_chi_papers_cited': 0}, 'var_functions.execute_python:16': {'total_citation_count': 0, 'number_of_chi_papers': 0, 'matched_papers_sample': []}}

exec(code, env_args)

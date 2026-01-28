code = """import json
import re

# Read citations data for 2020
citations_file = locals()['var_functions.query_db:0']
citations_data = []
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Read paper documents
papers_file = locals()['var_functions.query_db:4']
papers_data = []
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

# Build CHI papers dictionary with careful detection
chi_papers_dict = {}
chi_papers_full = []

for paper in papers_data:
    filename = paper['filename']
    text = paper['text']
    title = filename.replace('.txt', '')
    
    # Look for CHI conference information in header
    # Conference info is typically in first 1000-2000 characters
    header = text[:2000]
    
    # Check for CHI conference patterns
    chi_patterns = [
        r'CHI\s+\d{4}',
        r"CHI\s+['’]\d{2}",
        r'Proceedings of the .*CHI',
        r'ACM .*CHI Conference',
        r'Conference on Human Factors in Computing Systems'
    ]
    
    is_chi = False
    for pattern in chi_patterns:
        if re.search(pattern, header, re.IGNORECASE):
            # Verify not a false positive by checking for other venues
            other_venues = ['UBICOMP', 'CSCW', 'DIS', 'PERVASIVEHEALTH', 
                          'WWW', 'IUI', 'OZCHI', 'TEI', 'AH', 'JOURNAL', 
                          'UBI COMP', 'PERVASIVE']
            header_upper = header.upper()
            
            # Only mark as CHI if no other venue is mentioned
            has_other_venue = any(venue in header_upper for venue in other_venues)
            
            # Special check: if CHI appears with conference/proceedings, it's likely CHI
            if 'CHI' in header_upper:
                if 'CONFERENCE' in header_upper or 'PROCEEDINGS' in header_upper:
                    # Check if CHI is part of a longer word (false positive)
                    chi_matches = re.finditer(r'\bCHI\b', header_upper)
                    for match in chi_matches:
                        # If CHI is found as a whole word, it's likely correct
                        is_chi = True
                        break
    
    if is_chi:
        title_lower = title.lower().strip()
        chi_papers_dict[title_lower] = title
        chi_papers_full.append(title)

# Match citations using more flexible approach
total_citations = 0
matched_chi_papers = []

for citation in citations_data:
    cite_title = citation['title'].lower().strip()
    cite_count = int(citation['citation_count'])
    
    # Direct match
    if cite_title in chi_papers_dict:
        total_citations += cite_count
        matched_chi_papers.append({
            'title': citation['title'],
            'citations': cite_count
        })

result = {
    'total_citation_count': total_citations,
    'number_of_chi_papers': len(matched_chi_papers),
    'matched_papers_sample': matched_chi_papers[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'total_citation_count': 243, 'chi_papers_identified': 4, 'sample_chi_papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': 16, 'venue': 'CHI'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': 77, 'venue': 'CHI'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': 98, 'venue': 'CHI'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': 52, 'venue': 'CHI'}]}, 'var_functions.execute_python:12': {'total_citation_count': 0, 'chi_papers_count': 0}, 'var_functions.execute_python:14': {'total_citation_count': 0, 'number_of_chi_papers_cited': 0}}

exec(code, env_args)

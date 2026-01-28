code = """import json

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

# Extract papers from CHI venue by checking the document text
chi_paper_titles = []

for paper in papers_data:
    filename = paper['filename']
    text = paper['text']
    title = filename.replace('.txt', '')
    
    # Check if the paper was presented at CHI
    # Look for CHI conference indicators in the text
    text_upper = text.upper()
    
    # Check first 2000 characters for venue information
    header = text_upper[:2000]
    
    # Look for CHI patterns that indicate a CHI conference paper
    if 'CHI' in header:
        # Ensure it's a conference proceeding, not just a citation
        # Look for common conference-related phrases near CHI
        import re
        chi_pos = header.find('CHI')
        context = header[max(0, chi_pos-100):chi_pos+200]
        
        if any(phrase in context for phrase in ['PROCEEDINGS', 'CONFERENCE', 'PAPER', 'ACM']):
            # Make sure we're not picking up other venues
            other_venues = ['UBICOMP', 'CSCW', 'DIS', 'PERVASIVEHEALTH', 
                          'WWW', 'IUI', 'OZCHI', 'TEI', 'AH', 'JOURNAL', 'SYMPOSIUM']
            
            # Check if another venue is mentioned
            has_other_venue = any(venue in header for venue in other_venues)
            
            # If CHI is found and no other major venue, count it as CHI
            if not has_other_venue:
                chi_paper_titles.append(title.lower().strip())

# Now count citations for these CHI papers
total_citations = 0
chi_papers_in_citations = 0

for citation in citations_data:
    cite_title = citation['title'].lower().strip()
    
    if cite_title in chi_paper_titles:
        total_citations += int(citation['citation_count'])
        chi_papers_in_citations += 1

result = {
    'total_citations_for_chi_papers_in_2020': total_citations,
    'number_of_chi_papers_cited': chi_papers_in_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'total_citation_count': 243, 'chi_papers_identified': 4, 'sample_chi_papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': 16, 'venue': 'CHI'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': 77, 'venue': 'CHI'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': 98, 'venue': 'CHI'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': 52, 'venue': 'CHI'}]}, 'var_functions.execute_python:12': {'total_citation_count': 0, 'chi_papers_count': 0}, 'var_functions.execute_python:14': {'total_citation_count': 0, 'number_of_chi_papers_cited': 0}, 'var_functions.execute_python:16': {'total_citation_count': 0, 'number_of_chi_papers': 0, 'matched_papers_sample': []}, 'var_functions.execute_python:20': {'total_citation_count': 0, 'papers_analyzed': 188, 'chi_papers_identified': 0, 'chi_papers': []}}

exec(code, env_args)

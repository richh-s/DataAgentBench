code = """import json

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

# Build a comprehensive dictionary of papers with title as key
# This will help with matching despite minor title differences
papers_dict = {}
for paper in papers_data:
    filename = paper['filename']
    text = paper['text']
    title = filename.replace('.txt', '')
    
    # Check if this is a CHI paper by looking for CHI in the text
    # Conference info is usually in the first part of the paper
    is_chi = False
    
    # Look in the first 2000 characters for conference header
    header = text[:2000]
    header_upper = header.upper()
    
    # Check for CHI conference indicators
    chi_indicators = [
        ('CHI', ['CONFERENCE', 'PROCEEDINGS', 'ACM', 'HUMAN FACTORS']),
    ]
    
    if 'CHI' in header_upper:
        # Verify it's actually a CHI conference paper
        # by checking for conference-related words nearby
        chi_pos = header_upper.find('CHI')
        context = header_upper[max(0, chi_pos-100):chi_pos+100]
        
        conference_words = ['CONFERENCE', 'PROCEEDINGS', 'PAPER']
        has_conference_context = any(word in context for word in conference_words)
        
        # Make sure it's not another venue
        other_venues = ['UBICOMP', 'CSCW', 'DIS', 'PERVASIVEHEALTH', 
                       'WWW', 'IUI', 'OZCHI', 'TEI', 'AH', 'JOURNAL']
        has_other_venue = any(venue in header_upper for venue in other_venues)
        
        if has_conference_context and not has_other_venue:
            is_chi = True
    
    if is_chi:
        # Store by exact title
        papers_dict[title.lower().strip()] = {
            'title': title,
            'venue': 'CHI',
            'is_chi': True
        }

# Now match citations with CHI papers
chi_citations_found = []
citation_count_total = 0

for citation in citations_data:
    cite_title = citation['title'].lower().strip()
    
    # Check for exact match first
    if cite_title in papers_dict:
        chi_citations_found.append({
            'title': citation['title'],
            'citations': int(citation['citation_count'])
        })
        citation_count_total += int(citation['citation_count'])

result = {
    'total_citation_count': citation_count_total,
    'number_of_chi_papers_cited': len(chi_citations_found)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'total_citation_count': 243, 'chi_papers_identified': 4, 'sample_chi_papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': 16, 'venue': 'CHI'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': 77, 'venue': 'CHI'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': 98, 'venue': 'CHI'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': 52, 'venue': 'CHI'}]}, 'var_functions.execute_python:12': {'total_citation_count': 0, 'chi_papers_count': 0}}

exec(code, env_args)

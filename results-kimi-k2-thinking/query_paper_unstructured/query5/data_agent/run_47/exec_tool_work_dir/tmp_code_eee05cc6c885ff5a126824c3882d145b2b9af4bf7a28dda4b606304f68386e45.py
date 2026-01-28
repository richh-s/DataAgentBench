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

# Create dictionary to store CHI papers by title
chi_papers_lower = set()
chi_papers_full = {}

for paper in papers_data:
    filename = paper['filename']
    text = paper['text']
    title = filename.replace('.txt', '')
    
    # Check first 2000 chars for conference information
    header = text[:2000]
    
    # Look for CHI conference patterns
    # Check if CHI appears with conference/proceedings context
    if re.search(r'\bCHI\b', header, re.IGNORECASE):
        # Verify it's a conference paper by checking context
        # Look for phrases like "Proceedings", "Conference", "ACM"
        context_match = re.search(r'CHI.{0,100}', header, re.IGNORECASE)
        if context_match:
            context = context_match.group(0).upper()
            if any(word in context for word in ['PROCEEDINGS', 'CONFERENCE', 'ACM', 'PAPER']):
                # Check for other venues to avoid false positives
                other_venues = ['UBICOMP', 'CSCW', 'DIS', 'PERVASIVEHEALTH', 
                              'WWW', 'IUI', 'OZCHI', 'TEI', 'AH']
                header_upper = header.upper()
                
                # Only count as CHI if no other venue is mentioned
                has_other_venue = any(venue in header_upper for venue in other_venues)
                
                if not has_other_venue:
                    title_lower = title.lower().strip()
                    chi_papers_lower.add(title_lower)
                    chi_papers_full[title_lower] = title

# Now match with citations data
total_citation_count = 0
chi_papers_cited = []

for citation in citations_data:
    cite_title = citation['title'].lower().strip()
    citations = int(citation['citation_count'])
    
    if cite_title in chi_papers_lower:
        total_citation_count += citations
        chi_papers_cited.append({
            'title': citation['title'],
            'citations_2020': citations
        })

result = {
    'total_citation_count': total_citation_count,
    'papers_analyzed': len(citations_data),
    'chi_papers_identified': len(chi_papers_cited),
    'chi_papers': chi_papers_cited
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'total_citation_count': 243, 'chi_papers_identified': 4, 'sample_chi_papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': 16, 'venue': 'CHI'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': 77, 'venue': 'CHI'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': 98, 'venue': 'CHI'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': 52, 'venue': 'CHI'}]}, 'var_functions.execute_python:12': {'total_citation_count': 0, 'chi_papers_count': 0}, 'var_functions.execute_python:14': {'total_citation_count': 0, 'number_of_chi_papers_cited': 0}, 'var_functions.execute_python:16': {'total_citation_count': 0, 'number_of_chi_papers': 0, 'matched_papers_sample': []}}

exec(code, env_args)

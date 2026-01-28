code = """import json
import re

# Read the citations data for 2020
citations_file = locals()['var_functions.query_db:0']
citations_data = []
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Read the paper documents data
papers_file = locals()['var_functions.query_db:4']
papers_data = []
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

# More accurate CHI detection
chi_papers = []
for paper in papers_data:
    filename = paper['filename']
    text = paper['text']
    
    # Extract title
    title = filename.replace('.txt', '')
    
    # Look for explicit CHI venue information in the text
    # Common patterns for CHI conference papers
    chi_patterns = [
        r'CHI\s*\'\d{2}',  # CHI '20
        r'CHI\s*\d{4}',   # CHI 2020
        r'Proceedings of the .*?CHI.*?(?:Conference|Conference on Human Factors)',
        r'ACM\s+CHI\s+Conference',
        r'Conference on Human Factors in Computing Systems'
    ]
    
    is_chi = False
    for pattern in chi_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_chi = True
            break
    
    # Additional check: look in the first 500 characters where conference info usually appears
    if not is_chi:
        header = text[:500]
        if 'CHI' in header and ('Proceedings' in header or 'Conference' in header):
            # More specific check to avoid false positives
            if re.search(r'\bCHI\b', header):
                # Check if it's not another venue with "CHI" in the name
                if not any(venue in header for venue in ['Ubicomp', 'CSCW', 'DIS', 'TEI']):
                    is_chi = True
    
    if is_chi:
        chi_papers.append({
            'title': title,
            'title_lower': title.lower().strip()
        })

# Create lookup dictionary
chi_papers_dict = {p['title_lower']: p for p in chi_papers}

# Find citations for CHI papers
chi_citations = []
matched_titles = []

for citation in citations_data:
    cite_title = citation['title'].lower().strip()
    if cite_title in chi_papers_dict:
        chi_citations.append(int(citation['citation_count']))
        matched_titles.append(citation['title'])

# Calculate results
total_citation_count = sum(chi_citations)
chi_papers_count = len(chi_citations)

result = {
    'total_citation_count': total_citation_count,
    'chi_papers_cited': chi_papers_count,
    'average_citations_per_paper': round(total_citation_count / chi_papers_count, 2) if chi_papers_count > 0 else 0
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'total_citation_count': 243, 'chi_papers_identified': 4, 'sample_chi_papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': 16, 'venue': 'CHI'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': 77, 'venue': 'CHI'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': 98, 'venue': 'CHI'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': 52, 'venue': 'CHI'}]}}

exec(code, env_args)

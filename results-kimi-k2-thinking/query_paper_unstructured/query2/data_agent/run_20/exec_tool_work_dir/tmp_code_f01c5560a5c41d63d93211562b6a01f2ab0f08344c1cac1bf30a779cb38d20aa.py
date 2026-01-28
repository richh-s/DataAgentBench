code = """import json
import re

# Load datasets
citations_file = locals()['var_functions.query_db:14']
papers_file = locals()['var_functions.query_db:12']

with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

with open(papers_file, 'r') as f:
    all_papers = json.load(f)

# Identify ACM papers using multiple patterns
acm_paper_titles = []
acm_patterns = [
    r'Copyright.*© ACM',
    r'Copyright.*ACM',
    r'http://dx\.doi\.org/10\.1145/',  # ACM DOI prefix
    r'ACM Classification Keywords',
    r'Association for Computing Machinery'
]

for paper in all_papers:
    filename = paper['filename']
    text = paper['text']
    title = filename.replace('.txt', '')
    
    # Check if any ACM pattern appears in the text
    for pattern in acm_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            acm_paper_titles.append(title)
            break

# Also look for common ACM venues (though not perfect)
acm_venues = ['CHI', 'UbiComp', 'CSCW', 'DIS', 'TEI', 'IUI']
for paper in all_papers:
    filename = paper['filename']
    text = paper['text']
    title = filename.replace('.txt', '')
    
    if title not in acm_paper_titles:  # Only check if not already identified
        # Look for ACM venue patterns like "CHI '15" or "UbiComp 2015"
        venue_pattern = r"\b(CHI|UbiComp|CSCW|DIS|TEI|IUI)\s*['\"]?\s*\d{2,4}\b"
        if re.search(venue_pattern, text):
            acm_paper_titles.append(title)

# Match 2018 citations with ACM papers
acm_citations = []
matched_titles = []
for citation in citations_2018:
    citation_title = citation['title']
    if citation_title in acm_paper_titles:
        acm_citations.append(int(citation['citation_count']))
        matched_titles.append(citation_title)

# Calculate average
if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
    result = {
        'average_citation_count': round(avg_citations, 2),
        'total_acm_papers_cited': len(acm_citations),
        'total_citations_2018': len(citations_2018),
        'sample_matched_titles': matched_titles[:5]
    }
else:
    result = {
        'average_citation_count': 0,
        'total_acm_papers_cited': 0,
        'total_citations_2018': len(citations_2018),
        'acm_papers_identified': len(acm_paper_titles),
        'sample_acm_titles': acm_paper_titles[:5],
        'message': 'No ACM papers found in 2018 citations'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'average_citation_count': 68.5, 'total_matched_papers': 2}, 'var_functions.execute_python:8': {'total_citations_2018': 158, 'acm_papers_found': 5, 'sample_citation_titles': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28', 'citation_year': '2018'}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58', 'citation_year': '2018'}], 'sample_acm_filenames': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt']}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_citations_2018': 158, 'total_papers_in_db': 5}, 'var_functions.execute_python:18': {'average_citation_count': 68.5, 'total_acm_papers_cited': 2, 'total_citations_2018': 158}}

exec(code, env_args)

code = """import json
import re

# Load the citations data for 2018
citations_file_path = locals()['var_functions.query_db:5']
with open(citations_file_path, 'r') as f:
    citations_2018 = json.load(f)

# Load the paper documents from MongoDB
paper_docs_file_path = locals()['var_functions.query_db:6']
with open(paper_docs_file_path, 'r') as f:
    paper_docs = json.load(f)

# Extract paper information with source detection
papers_with_source = []
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if ACM is the source/publisher
    is_acm = False
    acm_patterns = [
        r'ACM\s+Classification',
        r'ACM\s+\d{4}',
        r'permissions@acm\.org',
        r'ACM\s+\d{3}-\d',
        r'ACM\s+[Cc]onference',
        r'ACM\s+[Pp]ublication'
    ]
    
    for pattern in acm_patterns:
        if re.search(pattern, text):
            is_acm = True
            break
    
    if is_acm:
        papers_with_source.append({
            'title': title,
            'source': 'ACM',
            'filename': filename
        })

# Create a dictionary for fast lookup of ACM papers by title
acm_papers_dict = {paper['title'].lower().strip(): paper for paper in papers_with_source}

# Match citations with ACM papers
acm_citations = []
for citation in citations_2018:
    cit_title = citation.get('title', '').lower().strip()
    if cit_title in acm_papers_dict:
        acm_citations.append({
            'title': citation['title'],
            'citation_count': int(citation['citation_count']),
            'source': 'ACM'
        })

# Calculate average citation count
if acm_citations:
    total_citations = sum(c['citation_count'] for c in acm_citations)
    avg_citations = total_citations / len(acm_citations)
    result = {
        'average_citation_count': round(avg_citations, 2),
        'acm_papers_count': len(acm_citations),
        'total_citations': total_citations
    }
else:
    result = {
        'average_citation_count': 0,
        'acm_papers_count': 0,
        'total_citations': 0,
        'message': 'No ACM papers found in 2018 citations'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '14', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28', 'citation_year': '2018'}, {'id': '25', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58', 'citation_year': '2018'}, {'id': '34', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '20', 'citation_year': '2018'}, {'id': '40', 'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set', 'citation_count': '13', 'citation_year': '2018'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'citations_2018_count': 158, 'paper_docs_count': 5}}

exec(code, env_args)

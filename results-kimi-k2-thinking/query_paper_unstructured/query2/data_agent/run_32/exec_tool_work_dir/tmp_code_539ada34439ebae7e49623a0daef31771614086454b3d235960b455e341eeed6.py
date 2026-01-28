code = """import json
import re

# Load data
citations_2018_file = locals()['var_functions.query_db:8']
paper_docs_file = locals()['var_functions.query_db:19']

citations_2018 = []
paper_docs = []

# Load citations
if isinstance(citations_2018_file, str) and citations_2018_file.endswith('.json'):
    with open(citations_2018_file, 'r') as f:
        citations_2018 = json.load(f)
else:
    citations_2018 = citations_2018_file

# Load paper docs
if isinstance(paper_docs_file, str) and paper_docs_file.endswith('.json'):
    with open(paper_docs_file, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_file

# Extract paper information from documents
paper_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Initialize source
    source = ''
    
    # Look for ACM indicators in the text
    if 'ACM' in text or 'acm' in text or 'acm.org' in text:
        source = 'ACM'
    elif 'IEEE' in text:
        source = 'IEEE'
    elif 'PubMed' in text or 'Pubmed' in text:
        source = 'PubMed'
    
    paper_info.append({
        'title': title,
        'source': source,
        'text': text
    })

print(f"Found {len(paper_info)} papers with source info")
acm_papers = [p for p in paper_info if p['source'] == 'ACM']
print(f"Found {len(acm_papers)} ACM papers")

# Create a mapping of titles to citation counts for 2018
citation_map = {c['title']: int(c['citation_count']) for c in citations_2018}

# Find ACM papers that have citations in 2018
acm_citations = []
for paper in paper_info:
    if paper['source'] == 'ACM' and paper['title'] in citation_map:
        acm_citations.append({
            'title': paper['title'],
            'citation_count': citation_map[paper['title']],
            'source': paper['source']
        })

print(f"Found {len(acm_citations)} ACM papers cited in 2018")

# Calculate average citation count
if acm_citations:
    total_citations = sum(c['citation_count'] for c in acm_citations)
    avg_citations = total_citations / len(acm_citations)
    result = {
        'average_citation_count': round(avg_citations, 2),
        'total_papers': len(acm_citations),
        'total_citations': total_citations
    }
else:
    result = {
        'average_citation_count': 0,
        'total_papers': 0,
        'total_citations': 0
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:16': "Loaded 158 citations for 2018 and 5 paper documents; First citation: {'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95'}; First paper doc filename: A Lived Informatics Model of Personal Informatics.txt", 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json'}

exec(code, env_args)

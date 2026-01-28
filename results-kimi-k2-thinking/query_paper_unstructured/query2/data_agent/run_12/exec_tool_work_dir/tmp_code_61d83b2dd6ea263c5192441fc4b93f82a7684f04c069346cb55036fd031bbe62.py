code = """import json
import pandas as pd
import re

# Load citation data
citation_path = locals()['var_functions.query_db:2']
if isinstance(citation_path, str):
    with open(citation_path, 'r') as f:
        citations = json.load(f)
else:
    citations = citation_path

# Load paper docs data
paper_path = locals()['var_functions.query_db:8']
if isinstance(paper_path, str):
    with open(paper_path, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_path

# Build mapping from paper title to doc
paper_map = {}
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    paper_map[title] = doc

# Common ACM venues in HCI
acm_venues = {
    'CHI', 'Ubicomp', 'UbiComp', 'CSCW', 'DIS', 'TEI', 'IUI', 
    'PervasiveHealth', 'IUW', 'AH', 'OzCHI', 'MobileHCI',
    'WWW'
}

# Extract venue from doc text
def extract_venue(doc):
    text = doc.get('text', '')
    header = text[:1000]
    patterns = [
        r"([A-Z]+)\s*'\d{2}",
        r"([A-Z]+)\s*20\d{2}",
        r"(Ubicomp|UbiComp)\s+'\d{2}",
        r"(Ubicomp|UbiComp)\s+20\d{2}",
    ]
    for pattern in patterns:
        m = re.search(pattern, header)
        if m:
            return m.group(1)
    return None

# Identify ACM papers
acm_paper_titles = []
for title, doc in paper_map.items():
    venue = extract_venue(doc)
    if venue and venue.upper() in {v.upper() for v in acm_venues}:
        acm_paper_titles.append(title)

# Compute avg citation count for ACM papers in 2018
citation_counts = []
for citation in citations:
    title = citation['title']
    if title in acm_paper_titles:
        citation_counts.append(int(citation['citation_count']))

result = {
    'average_citation_count': sum(citation_counts) / len(citation_counts) if citation_counts else None,
    'matched_citations_count': len(citation_counts)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['paper_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'average_citation_count': None, 'matched_citations_count': 0}}

exec(code, env_args)

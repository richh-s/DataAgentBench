code = """import json
import pandas as pd
import re

# Load citation data (from file path stored in var)
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

print('Number of citations for 2018:', len(citations))
print('Number of paper docs:', len(paper_docs))

# Build mapping from paper title (derived from filename) to doc
paper_map = {}
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    paper_map[title] = doc

# Common ACM venues in HCI (case-insensitive)
acm_venues = {
    'CHI', 'Ubicomp', 'UbiComp', 'CSCW', 'DIS', 'TEI', 'IUI', 
    'PervasiveHealth', 'IUW', 'AH', 'OzCHI', 'MobileHCI',
    'WWW'  # WWW is often ACM
}

def extract_venue(doc):
    """Extract venue from document text (usually near top)"""
    text = doc.get('text', '')
    # Look in first 1000 characters for venue pattern
    header = text[:1000]
    # Common venue patterns: "CHI '18", "UBICOMP '15", "CSCW 2017", etc.
    venue_patterns = [
        r"([A-Z]+)\s*'\d{2}",  # CHI '15, CSCW '17
        r"([A-Z]+)\s*20\d{2}",  # CHI 2015, CSCW 2017
        r"(Ubicomp|UbiComp)\s+'\d{2}",
        r"(Ubicomp|UbiComp)\s+20\d{2}",
    ]
    for pattern in venue_patterns:
        m = re.search(pattern, header)
        if m:
            return m.group(1)
    return None

# Extract venues and identify ACM papers
acm_paper_titles = []
venue_counts = {}
for title, doc in paper_map.items():
    venue = extract_venue(doc)
    if venue:
        venue_key = venue.upper()
        venue_counts[venue_key] = venue_counts.get(venue_key, 0) + 1
        if venue_key in {v.upper() for v in acm_venues}:
            acm_paper_titles.append(title)

print('Venue distribution (top 10):')
for v, c in sorted(venue_counts.items(), key=lambda x: -x[1])[:10]:
    print(v, c)

print('Number of papers identified as ACM (by venue):', len(acm_paper_titles))

# Now compute average citation counts for papers in ACM set for citation_year 2018
matching_citations = []
for citation in citations:
    title = citation['title']
    if title in acm_paper_titles:
        matching_citations.append(int(citation['citation_count']))

print('Number of matching citations with ACM:', len(matching_citations))
if matching_citations:
    avg_citations = sum(matching_citations) / len(matching_citations)
    print('Average citation count:', avg_citations)
else:
    print('No matching ACM papers found in 2018 citations')
    avg_citations = None

# Print result as JSON
print('__RESULT__:')
print(json.dumps({"average_citation_count": avg_citations, "matched_citations_count": len(matching_citations)}))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['paper_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'average_citation_count': None, 'matched_citations_count': 0}}

exec(code, env_args)

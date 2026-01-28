code = """import json
import pandas as pd
import re

# Load citation data (from file path stored in var)
citation_path = locals()['var_functions.query_db:2']  # path or data
if isinstance(citation_path, str):
    # It's a filepath
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
    # Title is filename without .txt
    title = doc['filename'].replace('.txt', '')
    paper_map[title] = doc

# Function to extract source from doc text
source_pattern = re.compile(r'(?i)source:\s*(.+)', re.MULTILINE)
def extract_source(doc):
    text = doc.get('text', '')
    # Try pattern
    m = source_pattern.search(text)
    if m:
        return m.group(1).strip()
    # fallback: try to find ACM classification or ACM copyright
    # If 'ACM' appears near top (first 500 chars) maybe it's from ACM
    # Count occurrences
    top = text[:500]
    if 'ACM' in top:
        # Might be ACM
        return 'ACM'
    return None

# Let's examine some examples manually
sample_titles = list(paper_map.keys())[:5]
print('Sample titles and extracted source:')
for t in sample_titles:
    src = extract_source(paper_map[t])
    print(t, '->', src)

# Identify ACM papers
acm_paper_titles = []
for title, doc in paper_map.items():
    src = extract_source(doc)
    if src and src.upper() == 'ACM':
        acm_paper_titles.append(title)

print('Number of papers identified as ACM source (by pattern):', len(acm_paper_titles))

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
    print('No matching ACM papers found')

# Print result as JSON per requirement
print('__RESULT__:')
print(json.dumps({"average_citation_count": avg_citations if matching_citations else None, "matched_citations_count": len(matching_citations)}))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['paper_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

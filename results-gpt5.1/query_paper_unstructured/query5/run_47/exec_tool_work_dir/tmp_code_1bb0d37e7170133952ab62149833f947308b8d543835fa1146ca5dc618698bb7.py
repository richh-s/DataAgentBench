code = """import json
import pandas as pd

# Load citations (2020)
records_citations = var_call_Ai1pPA3HQVaRladiFKuXUWJZ
# If stored as path, load json
if isinstance(records_citations, str):
    with open(records_citations, 'r') as f:
        records_citations = json.load(f)

cit_df = pd.DataFrame(records_citations)
# normalize types
cit_df['citation_count'] = cit_df['citation_count'].astype(int)

# Load paper docs metadata
paper_docs = var_call_Z4pNBqnhdczG2y35pn5mvYVa
if isinstance(paper_docs, str):
    with open(paper_docs, 'r') as f:
        paper_docs = json.load(f)

papers = []
for doc in paper_docs:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    # crude venue detection: look for 'CHI' in first 1000 chars or typical CHI copyright string
    header = text[:1500].upper()
    is_chi = 'CHI ' in header or "CHI'" in header or 'ACM CHI' in header or 'CHI CONFERENCE' in header
    papers.append({'title': title, 'is_chi': is_chi})

papers_df = pd.DataFrame(papers)

# Join on title
merged = cit_df.merge(papers_df, on='title', how='left')
chi_citations = merged[merged['is_chi'] == True]

total_citations = int(chi_citations['citation_count'].sum())

result = {'total_citations_chi_2020': total_citations}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Ai1pPA3HQVaRladiFKuXUWJZ': 'file_storage/call_Ai1pPA3HQVaRladiFKuXUWJZ.json', 'var_call_Z4pNBqnhdczG2y35pn5mvYVa': 'file_storage/call_Z4pNBqnhdczG2y35pn5mvYVa.json'}

exec(code, env_args)

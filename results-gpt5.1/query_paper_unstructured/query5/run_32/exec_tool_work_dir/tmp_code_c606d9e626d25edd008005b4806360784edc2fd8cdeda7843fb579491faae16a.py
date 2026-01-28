code = """import json
import pandas as pd

# Load citations (2020)
records_citations = var_call_4SV9Rtp9FGExqUdSBQnfjSBY
if isinstance(records_citations, str):
    with open(records_citations, 'r') as f:
        records_citations = json.load(f)

cit_df = pd.DataFrame(records_citations)
cit_df['title'] = cit_df['title'].astype(str)
cit_df['citation_count'] = cit_df['citation_count'].astype(int)

# Load paper docs metadata (filenames & text)
records_docs = var_call_O6lp01zwJEbL6ZPVkkCu63vU
if isinstance(records_docs, str):
    with open(records_docs, 'r') as f:
        records_docs = json.load(f)

docs = []
for d in records_docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    is_chi = ' CHI ' in text.upper() or text.upper().startswith('CHI ') or '\nCHI ' in text.upper()
    # heuristic: look for "CHI '" pattern often in headers
    if "CHI '" in text.upper() or 'IN PROCEEDINGS OF THE SIGCHI' in text.upper() or 'SIGCHI CONFERENCE ON HUMAN FACTORS' in text.upper():
        is_chi = True
    docs.append({'title': title, 'is_chi': is_chi})

docs_df = pd.DataFrame(docs)

# Join on title
merged = pd.merge(cit_df, docs_df[docs_df['is_chi']], on='title', how='inner')

total_citations = int(merged['citation_count'].sum())

result = {'total_citations_for_CHI_papers_cited_in_2020': total_citations}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_4SV9Rtp9FGExqUdSBQnfjSBY': 'file_storage/call_4SV9Rtp9FGExqUdSBQnfjSBY.json', 'var_call_O6lp01zwJEbL6ZPVkkCu63vU': 'file_storage/call_O6lp01zwJEbL6ZPVkkCu63vU.json'}

exec(code, env_args)

code = """import json, pandas as pd

# Load citations (already a list of dicts)
rl_citations = var_call_Vz6WxvkTnLT6E6bymdtOkakx

# Load full paper_docs result if it's a file path
paper_docs_ref = var_call_oi22EfVBylXRufx1sRJu90we
if isinstance(paper_docs_ref, str):
    with open(paper_docs_ref, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_ref

# Build mapping from title (filename without .txt) to venue by scanning text for CHI or other cues
records = []
for doc in paper_docs:
    filename = doc.get('filename','')
    text = doc.get('text','') or ''
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    venue = None
    # Heuristic: if ' CHI ' or "CHI'" appears near beginning, mark as CHI
    head = text[:1000].upper()
    if ' CHI ' in head or "CHI '" in head or '\nCHI ' in head or 'CHI CONFERENCE ON HUMAN FACTORS IN COMPUTING SYSTEMS'.upper() in head:
        venue = 'CHI'
    records.append({'title': title, 'venue': venue})

df_venue = pd.DataFrame(records)

# Filter to CHI papers
chi_titles = set(df_venue[df_venue['venue']=='CHI']['title'])

# Sum citation counts in 2020 for CHI titles
citations_df = pd.DataFrame(rl_citations)
# ensure numeric
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

mask = citations_df['title'].isin(chi_titles)
result_total = int(citations_df.loc[mask, 'citation_count'].sum())

out = json.dumps({'total_citations_2020_for_CHI_papers': result_total})
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Vz6WxvkTnLT6E6bymdtOkakx': 'file_storage/call_Vz6WxvkTnLT6E6bymdtOkakx.json', 'var_call_oi22EfVBylXRufx1sRJu90we': 'file_storage/call_oi22EfVBylXRufx1sRJu90we.json'}

exec(code, env_args)

code = """import json, re
import pandas as pd

# Attempt to load the stored results from previous query_db calls
papers_data = None
citations_data = None

# The storage may provide either the full data list or a filepath string to a .json file.
# Try known variable names from prior calls.
possible_papers_vars = ['var_call_IsFdhu3QJLfLJT28pCFaUXL1']
possible_citations_vars = ['var_call_riE3qFMvZWa3oiqprJ24fNy', 'var_call_riE3qFMvZWa3oiqprJ24fNyS']

for v in possible_papers_vars:
    try:
        val = globals()[v]
        if isinstance(val, str) and val.endswith('.json'):
            with open(val, 'r') as f:
                papers_data = json.load(f)
        else:
            papers_data = val
        break
    except Exception:
        continue

for v in possible_citations_vars:
    try:
        val = globals()[v]
        if isinstance(val, str) and val.endswith('.json'):
            with open(val, 'r') as f:
                citations_data = json.load(f)
        else:
            citations_data = val
        break
    except Exception:
        continue

if papers_data is None or citations_data is None:
    # fallback: return empty result
    result_list = []
else:
    df_papers = pd.DataFrame(papers_data)
    # derive title from filename
    def title_from_filename(fn):
        if not isinstance(fn, str):
            return None
        return re.sub(r"\.txt$", "", fn)
    df_papers['title'] = df_papers.get('filename', pd.Series()).apply(title_from_filename)
    def extract_year(text):
        if not isinstance(text, str):
            return None
        m = re.search(r"\b(20(?:1[7-9]|2[0-9]))\b", text)
        return int(m.group(1)) if m else None
    df_papers['year'] = df_papers.get('text', pd.Series()).apply(extract_year)
    df_papers['has_empirical'] = df_papers.get('text', pd.Series()).str.contains(r'\bempirical\b', case=False, na=False)
    df_filtered = df_papers[df_papers['has_empirical'] & df_papers['year'].notnull() & (df_papers['year'] > 2016)].copy()

    df_cit = pd.DataFrame(citations_data)
    # if aggregated
    if 'total_citations' in df_cit.columns:
        df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)
    else:
        if 'citation_count' in df_cit.columns:
            df_cit = df_cit.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})
        else:
            df_cit['total_citations'] = 0

    df_merged = pd.merge(df_filtered[['title','year']], df_cit[['title','total_citations']], on='title', how='left')
    df_merged['total_citations'] = df_merged['total_citations'].fillna(0).astype(int)

    result_list = []
    for _, row in df_merged.sort_values('total_citations', ascending=False).iterrows():
        result_list.append({'title': row['title'], 'total_citation_count': int(row['total_citations'])})

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_call_W12OMTCleckOZ5MbTKK7Bqgu': ['paper_docs'], 'var_call_24V8Vqwp35Q2wTcW4VUhfbWy': ['Citations', 'sqlite_sequence'], 'var_call_IsFdhu3QJLfLJT28pCFaUXL1': 'file_storage/call_IsFdhu3QJLfLJT28pCFaUXL1.json', 'var_call_riE3qFMvZWa3oiqprJ24fNyS': 'file_storage/call_riE3qFMvZWa3oiqprJ24fNyS.json'}

exec(code, env_args)

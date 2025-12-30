code = """import re, json, pandas as pd

file_path = var_call_fp4gDmpHrLaDbRRClf9HuZbS
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

records = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    year_match = re.search(r'(19|20)\d{2}', text)
    year = int(year_match.group(0)) if year_match else None
    contrib_match = re.search(r'contribution[s]?:\s*(.*?)\n', text, re.IGNORECASE)
    if contrib_match:
        contribution_text = contrib_match.group(1).lower()
    else:
        contribution_text = text[:500].lower()
    is_empirical = 'empirical' in contribution_text
    if year and year > 2016 and is_empirical:
        records.append({'title': title, 'year': year})

file_path_cit = var_call_2Kx134S2EHCVnv3rlzeLfo04
with open(file_path_cit, 'r') as f:
    citations = json.load(f)

papers_df = pd.DataFrame(records).drop_duplicates(subset=['title'])
citations_df = pd.DataFrame(citations)

citations_df['title_clean'] = citations_df['title'].str.replace('^\"|\"$', '', regex=True)

merged = pd.merge(papers_df, citations_df, left_on='title', right_on='title_clean', how='left')
result = merged[['title', 'total_citations']].dropna(subset=['total_citations']).to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_fp4gDmpHrLaDbRRClf9HuZbS': 'file_storage/call_fp4gDmpHrLaDbRRClf9HuZbS.json', 'var_call_2Kx134S2EHCVnv3rlzeLfo04': 'file_storage/call_2Kx134S2EHCVnv3rlzeLfo04.json'}

exec(code, env_args)

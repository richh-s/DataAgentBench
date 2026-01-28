code = """import json, pandas as pd

with open(var_call_HYmwXDqSKPoFsCim184Gq35v, 'r') as f:
    citations_2020 = json.load(f)

cit_df = pd.DataFrame(citations_2020)
cit_df['citation_count'] = cit_df['citation_count'].astype(int)

with open(var_call_ZbbTQjnfrYBN9dVZao2LbIrS, 'r') as f:
    papers = json.load(f)

chi_titles = set()
for doc in papers:
    filename = doc.get('filename', '')
    text = doc.get('text', '') or ''
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    t_low = text.lower()
    is_chi = False
    if 'chi ' in t_low or "chi'" in t_low or '\nchi ' in t_low or 'conference on human factors in computing systems' in t_low:
        is_chi = True
    if 'chi conference' in t_low:
        is_chi = True
    if is_chi:
        chi_titles.add(title)

cit_df['is_chi'] = cit_df['title'].isin(chi_titles)
chi_cit_df = cit_df[cit_df['is_chi']]

total_citations = int(chi_cit_df['citation_count'].sum())

result = {"total_citations_CHI_2020": total_citations}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_HYmwXDqSKPoFsCim184Gq35v': 'file_storage/call_HYmwXDqSKPoFsCim184Gq35v.json', 'var_call_sYRKP4KiDXeCjpgrLX7zHSW3': ['paper_docs'], 'var_call_ZbbTQjnfrYBN9dVZao2LbIrS': 'file_storage/call_ZbbTQjnfrYBN9dVZao2LbIrS.json'}

exec(code, env_args)

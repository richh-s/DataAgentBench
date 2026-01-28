code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

cit = load_records(var_call_hZYmPSg6FwSHjxXrQDaWW8fg)
docs = load_records(var_call_YyQRwUhfT7R5zY8vDikjm4bb)

cit_df = pd.DataFrame(cit)
if not cit_df.empty:
    cit_df['total_citations_2020'] = pd.to_numeric(cit_df['total_citations_2020'], errors='coerce').fillna(0).astype(int)

# Build title set for quick matching
cit_titles = set(cit_df['title'].tolist())

# Heuristic venue extraction: look for patterns like "CHI '15" or "CHI 2015" in first 2000 chars
chi_titles = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if title not in cit_titles:
        continue
    text = (d.get('text') or '')[:3000]
    if re.search(r"\bCHI\b\s*['’]?\s*\d{2}\b", text, flags=re.IGNORECASE) or re.search(r"\bCHI\b\s*\d{4}\b", text, flags=re.IGNORECASE) or re.search(r"\bCHI\s*\d{2}\b", text, flags=re.IGNORECASE):
        chi_titles.append(title)

chi_set = set(chi_titles)
chi_cit_df = cit_df[cit_df['title'].isin(chi_set)].copy()

total = int(chi_cit_df['total_citations_2020'].sum())
per_paper = chi_cit_df.sort_values(['total_citations_2020','title'], ascending=[False, True]).to_dict(orient='records')

out = {
    'total_citations_2020_all_CHI_papers': total,
    'num_CHI_papers_cited_in_2020': int(chi_cit_df.shape[0]),
    'per_paper_total_citations_2020': per_paper
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_hZYmPSg6FwSHjxXrQDaWW8fg': 'file_storage/call_hZYmPSg6FwSHjxXrQDaWW8fg.json', 'var_call_YyQRwUhfT7R5zY8vDikjm4bb': 'file_storage/call_YyQRwUhfT7R5zY8vDikjm4bb.json', 'var_call_mshkscGjMJfwBaJ3XcSZKLz6': ['paper_docs'], 'var_call_uXF4RJ4q1bTB1VcwtVhycOt7': ['Citations', 'sqlite_sequence']}

exec(code, env_args)

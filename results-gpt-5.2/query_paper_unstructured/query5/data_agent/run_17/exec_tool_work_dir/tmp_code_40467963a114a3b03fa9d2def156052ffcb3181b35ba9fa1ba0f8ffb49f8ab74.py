code = """import json, re
import pandas as pd

def load_tool_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

cit = load_tool_result(var_call_9X83BuiCEEyXT0BZpBCna1M4)
docs = load_tool_result(var_call_TDnMk5TxCu8yMFjaBkwMw1Gt)

cit_df = pd.DataFrame(cit)
# normalize types
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# build set of CHI titles from docs
chi_titles = set()
for d in docs:
    fn = d.get('filename','')
    if not fn.endswith('.txt'):
        continue
    title = fn[:-4]
    txt = (d.get('text') or '')
    # venue heuristic: look for CHI token in header/citation lines
    if re.search(r"\bCHI\b", txt, flags=re.IGNORECASE):
        # reduce false positives by requiring ACM CHI style marker common: "CHI '" or "CHI 20"
        if re.search(r"\bCHI\s*['’`]?\d{2}\b|\bCHI\s*\d{4}\b", txt, flags=re.IGNORECASE):
            chi_titles.add(title)

chi_2020 = cit_df[cit_df['title'].isin(chi_titles)]

total = int(chi_2020['citation_count'].sum())

out = {
    "total_citation_count_2020_for_CHI_papers": total,
    "num_chi_papers_with_2020_citations": int(chi_2020['title'].nunique())
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_9X83BuiCEEyXT0BZpBCna1M4': 'file_storage/call_9X83BuiCEEyXT0BZpBCna1M4.json', 'var_call_TDnMk5TxCu8yMFjaBkwMw1Gt': 'file_storage/call_TDnMk5TxCu8yMFjaBkwMw1Gt.json'}

exec(code, env_args)

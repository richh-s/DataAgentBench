code = """import json, re
import pandas as pd

def load_tool_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

cit = load_tool_result(var_call_i6qy537ip93DasbacKuvf0vM)
docs = load_tool_result(var_call_n7bC9VbNSqIftG0ryNXyRqVl)

cit_df = pd.DataFrame(cit)
if not cit_df.empty:
    cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# Build a set of titles that are CHI venue based on paper text containing 'CHI' patterns
chi_titles = set()
venue_re = re.compile(r"\bCHI\b", re.IGNORECASE)

for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''

    # Heuristic: treat as CHI if text contains 'CHI' as venue marker. Prefer patterns like "CHI '" or "Proceedings of the SIGCHI".
    if re.search(r"SIGCHI|\bCHI\s*'\d{2}\b|\bCHI\s*\d{4}\b|\bCHI\b", text, flags=re.IGNORECASE):
        # avoid false positives: if also explicitly mentions another venue at header like UBICOMP/CSCW/DIS etc without CHI? hard.
        # We'll keep if it contains SIGCHI or CHI'YY in header.
        if re.search(r"SIGCHI|\bCHI\s*'\d{2}\b", text, flags=re.IGNORECASE):
            chi_titles.add(title)

# Filter citations to CHI titles
chi_cit = cit_df[cit_df['title'].isin(chi_titles)].copy()

# Aggregate total citation counts for these papers in 2020
result_total = int(chi_cit['citation_count'].sum())

out = {
    'total_citations_2020_for_CHI_papers': result_total,
    'num_CHI_papers_with_2020_citations': int(chi_cit['title'].nunique()),
    'papers': chi_cit.sort_values(['citation_count','title'], ascending=[False, True]).to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_i6qy537ip93DasbacKuvf0vM': 'file_storage/call_i6qy537ip93DasbacKuvf0vM.json', 'var_call_n7bC9VbNSqIftG0ryNXyRqVl': 'file_storage/call_n7bC9VbNSqIftG0ryNXyRqVl.json'}

exec(code, env_args)

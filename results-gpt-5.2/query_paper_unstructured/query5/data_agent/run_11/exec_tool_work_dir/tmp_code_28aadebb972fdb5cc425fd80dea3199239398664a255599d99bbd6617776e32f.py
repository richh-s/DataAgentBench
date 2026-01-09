code = """import json, re, pandas as pd

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

cit = load_records(var_call_HbD9ACh0ygpXBHuAklxT7VOb)
docs = load_records(var_call_OD80xYbOg6BFO1IvBBA8egwj)

cit_df = pd.DataFrame(cit)
# coerce types
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# extract venue from text (simple heuristic)
chi_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    # look for CHI marker near top
    head = text[:2000].upper()
    if 'CHI' in head:
        # require pattern like "CHI '" or "CHI 20" or "CHI,"
        if re.search(r"\bCHI\b\s*['’]?\d{2}|\bCHI\s*20\d{2}|\bCHI\b\s*\(", head):
            chi_titles.add(title)
        else:
            # also accept explicit ACM CHI in header
            if 'CONFERENCE ON HUMAN FACTORS IN COMPUTING SYSTEMS' in head:
                chi_titles.add(title)

chi_cit_df = cit_df[cit_df['title'].isin(chi_titles)].copy()

total = int(chi_cit_df['citation_count'].sum())

out = {
    "total_citations_2020_for_CHI_papers": total,
    "num_CHI_papers_cited_in_2020": int(chi_cit_df['title'].nunique())
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_HbD9ACh0ygpXBHuAklxT7VOb': 'file_storage/call_HbD9ACh0ygpXBHuAklxT7VOb.json', 'var_call_OD80xYbOg6BFO1IvBBA8egwj': 'file_storage/call_OD80xYbOg6BFO1IvBBA8egwj.json'}

exec(code, env_args)

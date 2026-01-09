code = """import json, re
import pandas as pd

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path

cit = load_records(var_call_cgEkWTokcu0VWStYf89rjP1d)
docs = load_records(var_call_uRdTMaSingYf0Z2KaoRUmwo4)

# Build set of CHI paper titles from docs by simple venue substring match in text
chi_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$','', fn)
    text = d.get('text','') or ''
    if re.search(r'\bCHI\b', text, flags=re.IGNORECASE):
        # avoid false positives from e.g., "CHINA"? keep as simple per instructions
        chi_titles.add(title)

# Sum citations in 2020 for titles that are CHI
rows = []
for r in cit:
    t = r.get('title')
    if t in chi_titles:
        cc = r.get('citation_count')
        try:
            cc = int(cc)
        except Exception:
            cc = int(float(cc)) if cc is not None else 0
        rows.append({'title': t, 'citation_count_2020': cc})

# Aggregate in case duplicates
if rows:
    df = pd.DataFrame(rows)
    df = df.groupby('title', as_index=False)['citation_count_2020'].sum()
    total = int(df['citation_count_2020'].sum())
    out = {
        'total_citations_2020_for_CHI_papers': total,
        'paper_count': int(df.shape[0]),
        'per_paper': df.sort_values('citation_count_2020', ascending=False).to_dict(orient='records')
    }
else:
    out = {'total_citations_2020_for_CHI_papers': 0, 'paper_count': 0, 'per_paper': []}

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_cgEkWTokcu0VWStYf89rjP1d': 'file_storage/call_cgEkWTokcu0VWStYf89rjP1d.json', 'var_call_uRdTMaSingYf0Z2KaoRUmwo4': 'file_storage/call_uRdTMaSingYf0Z2KaoRUmwo4.json'}

exec(code, env_args)

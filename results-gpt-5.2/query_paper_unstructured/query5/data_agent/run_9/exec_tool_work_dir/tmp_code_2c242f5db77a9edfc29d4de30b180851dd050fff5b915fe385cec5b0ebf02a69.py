code = """import json, re
import pandas as pd

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path

cit = load_records(var_call_fDbs3ta0LW0cGE3duzIQkKyO)
docs = load_records(var_call_gjNKrzZqxa46WJTcoBqU8TuL)

# Build set of CHI paper titles from docs by detecting venue in text
chi_titles = set()
for d in docs:
    fn = d.get('filename','')
    if not fn.endswith('.txt'):
        continue
    title = fn[:-4]
    text = (d.get('text') or '')
    # Heuristic: venue mention
    if re.search(r"\bCHI\b", text) or re.search(r"\bCHI\s*'\d{2}\b", text) or re.search(r"\bCHI\s*\d{4}\b", text) or re.search(r"\bSIGCHI\b", text):
        # Avoid other venues if explicitly identified and not CHI? keep simple
        chi_titles.add(title)

# Filter citations for titles in CHI set
rows = []
for r in cit:
    title = r.get('title')
    if title in chi_titles:
        try:
            cc = int(r.get('citation_count'))
        except Exception:
            cc = None
        rows.append({'title': title, 'citation_count_2020': cc})

# Aggregate total citation counts across all CHI papers cited in 2020
# Also provide per-paper list
valid = [x for x in rows if isinstance(x['citation_count_2020'], int)]
total = sum(x['citation_count_2020'] for x in valid)
valid_sorted = sorted(valid, key=lambda x: (-x['citation_count_2020'], x['title']))

result = {
    'total_citations_2020_for_CHI_papers': total,
    'num_CHI_papers_with_citations_in_2020': len(valid_sorted),
    'papers': valid_sorted
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_fDbs3ta0LW0cGE3duzIQkKyO': 'file_storage/call_fDbs3ta0LW0cGE3duzIQkKyO.json', 'var_call_gjNKrzZqxa46WJTcoBqU8TuL': 'file_storage/call_gjNKrzZqxa46WJTcoBqU8TuL.json'}

exec(code, env_args)

code = """import json, re
import pandas as pd

mongo_src = var_call_b5IICSZANfiBAFMPMoRVmPik
if isinstance(mongo_src, str) and mongo_src.endswith('.json'):
    with open(mongo_src, 'r', encoding='utf-8') as f:
        papers = json.load(f)
else:
    papers = mongo_src

cits_src = var_call_fdCqgtUKPQaghNBE5syzDaGE
if isinstance(cits_src, str) and cits_src.endswith('.json'):
    with open(cits_src, 'r', encoding='utf-8') as f:
        cits = json.load(f)
else:
    cits = cits_src

cit_df = pd.DataFrame(cits)
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)


def extract_year(text):
    if not text:
        return None
    m = re.search(r'Copyright\s*(?:\(c\)|\u00a9)?\s*(20\d{2})', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    years = [int(y) for y in re.findall(r'\b(19\d{2}|20\d{2})\b', text)]
    years = [y for y in years if 1990 <= y <= 2026]
    if not years:
        return None
    return min(years)


def has_empirical(text):
    if not text:
        return False
    t = text.lower()
    keywords = [
        ' empirical ',
        'user study',
        'field study',
        'we conducted',
        'we ran a study',
        'interview',
        'survey',
        'experiment',
        'participants'
    ]
    return any(k in t for k in keywords)

rows = []
for d in papers:
    fn = d.get('filename', '')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text', '')
    year = extract_year(text)
    empirical = has_empirical(text)
    rows.append({'title': title, 'year': year, 'empirical': empirical})

paper_df = pd.DataFrame(rows)
paper_df = paper_df[(paper_df['empirical']) & (paper_df['year'].notna()) & (paper_df['year'] > 2016)]

out = paper_df.merge(cit_df, on='title', how='inner')
out = out[['title', 'total_citations']].sort_values('total_citations', ascending=False)

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_b5IICSZANfiBAFMPMoRVmPik': 'file_storage/call_b5IICSZANfiBAFMPMoRVmPik.json', 'var_call_fdCqgtUKPQaghNBE5syzDaGE': 'file_storage/call_fdCqgtUKPQaghNBE5syzDaGE.json'}

exec(code, env_args)

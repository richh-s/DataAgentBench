code = """import json, re
import pandas as pd

def load_records(maybe_path_or_obj):
    if isinstance(maybe_path_or_obj, str) and maybe_path_or_obj.endswith('.json'):
        with open(maybe_path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_obj

paper_docs = load_records(var_call_vtDa0xHCUsiYeo8Un7sy2WmJ)
citations = load_records(var_call_99nSOYsPbn22jkur7m4K8Bpn)

# Extract year and contribution using heuristic parsing
# year: first 4-digit year between 1990-2030; prefer the one near venue lines or copyright; fallback to first match
# contribution: look for keyword 'empirical' in a metadata-like section; else scan whole text

year_re = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(text):
    if not text:
        return None
    candidates = []
    for m in year_re.finditer(text[:4000]):
        y = int(m.group(1))
        if 1990 <= y <= 2030:
            candidates.append((m.start(), y))
    # prioritize copyright year if present
    m = re.search(r'Copyright\s*(?:\(c\))?\s*(19\d{2}|20\d{2})', text[:8000], flags=re.IGNORECASE)
    if m:
        y = int(m.group(1))
        if 1990 <= y <= 2030:
            return y
    if candidates:
        # choose earliest occurrence
        return sorted(candidates, key=lambda t: t[0])[0][1]
    # broader search
    for m in year_re.finditer(text):
        y = int(m.group(1))
        if 1990 <= y <= 2030:
            return y
    return None

def has_empirical(text):
    if not text:
        return False
    return 'empirical' in text.lower()

rows = []
for d in paper_docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','')
    y = extract_year(text)
    emp = has_empirical(text)
    rows.append({'title': title, 'year': y, 'empirical': emp})

pdf = pd.DataFrame(rows)
# filter after 2016 and empirical contribution
pdf_f = pdf[(pdf['empirical'] == True) & (pdf['year'].notna()) & (pdf['year'] > 2016)].copy()

cdf = pd.DataFrame(citations)
# total_citations might be str
cdf['total_citations'] = pd.to_numeric(cdf['total_citations'], errors='coerce')

out = pdf_f.merge(cdf, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out[['title','total_citations']].sort_values(['total_citations','title'], ascending=[False, True])

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_vtDa0xHCUsiYeo8Un7sy2WmJ': 'file_storage/call_vtDa0xHCUsiYeo8Un7sy2WmJ.json', 'var_call_99nSOYsPbn22jkur7m4K8Bpn': 'file_storage/call_99nSOYsPbn22jkur7m4K8Bpn.json'}

exec(code, env_args)

code = """import json, re, pandas as pd

# load filenames list
import os

def load_json_maybe(path_or_list):
    if isinstance(path_or_list, str) and os.path.exists(path_or_list):
        with open(path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_list

paper_docs = load_json_maybe(var_call_8aDRM5cI4RsJ2JVHuYRA6qBN)
cites = load_json_maybe(var_call_027K08n9PiGCRWzcVGBYGyka)

# heuristics to detect publication year=2016 and domain physical activity

def is_pub_year_2016(text):
    # common patterns: "CHI 2016", "UbiComp 2016", copyright 2016
    patterns = [
        r'\bCHI\s*2016\b', r'\bUbiComp\s*2016\b', r'\bUbicomp\s*2016\b', r'\bCSCW\s*2016\b',
        r'\bDIS\s*2016\b', r'\bIUI\s*2016\b', r'\bWWW\s*2016\b', r'\bTEI\s*2016\b',
        r'\bOzCHI\s*2016\b', r'\bPervasiveHealth\s*2016\b',
        r'\bCopyright\s*(?:©|\(c\))?\s*2016\b', r'\b©\s*2016\b'
    ]
    for pat in patterns:
        if re.search(pat, text, flags=re.IGNORECASE):
            return True
    # fallback: look for publication year line near first page with 2016 and ACM/IEEE
    head = text[:4000]
    if re.search(r'\b2016\b', head) and re.search(r'ACM|IEEE|Proceedings', head, flags=re.IGNORECASE):
        return True
    return False

pa_terms = [
    r'physical activity', r'activity tracking', r'activity tracker', r'fitness tracker', r'step count', r'pedometer',
    r'exercis', r'workout', r'walking', r'run', r'cycling', r'sedentary'
]

def is_physical_activity_domain(text):
    # require explicit physical activity OR strong tracker/exercise signals
    t = text.lower()
    if 'physical activity' in t:
        return True
    score = 0
    for pat in pa_terms[1:]:
        if re.search(pat, t):
            score += 1
    return score >= 2

rows = []
for d in paper_docs:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$','', fn)
    text = d.get('text','')
    if is_pub_year_2016(text) and is_physical_activity_domain(text):
        rows.append({'title': title})

papers_2016_pa = pd.DataFrame(rows).drop_duplicates()

citedf = pd.DataFrame(cites)
if not citedf.empty:
    citedf['citation_count'] = pd.to_numeric(citedf['citation_count'], errors='coerce').fillna(0).astype(int)

# total citations across all years
if papers_2016_pa.empty:
    out = []
else:
    totals = citedf.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citation_count'})
    merged = papers_2016_pa.merge(totals, on='title', how='left')
    merged['total_citation_count'] = merged['total_citation_count'].fillna(0).astype(int)
    merged = merged.sort_values(['total_citation_count','title'], ascending=[False, True])
    out = merged.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_CWXupshSWmsTyUlUGwo0qtk0': 'file_storage/call_CWXupshSWmsTyUlUGwo0qtk0.json', 'var_call_027K08n9PiGCRWzcVGBYGyka': 'file_storage/call_027K08n9PiGCRWzcVGBYGyka.json', 'var_call_8aDRM5cI4RsJ2JVHuYRA6qBN': 'file_storage/call_8aDRM5cI4RsJ2JVHuYRA6qBN.json'}

exec(code, env_args)

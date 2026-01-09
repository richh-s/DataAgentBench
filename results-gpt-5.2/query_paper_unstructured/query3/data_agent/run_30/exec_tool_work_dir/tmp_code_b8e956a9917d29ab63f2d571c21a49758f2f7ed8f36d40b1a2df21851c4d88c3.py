code = """import json, re
import pandas as pd

# Load paper docs (full) from JSON file path
path_docs = var_call_EN9V0Vlayn5hR1sqO4sfeb18
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def parse_year(text):
    if not text:
        return None
    # look for common patterns: CHI '19, UbiComp '15, CSCW '17, etc.
    m = re.search(r"\b(?:CHI|CSCW|UBICOMP|UbiComp|DIS|IUI|WWW|OzCHI|TEI|AH|PervasiveHealth)\s*['’]\s*(\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy <= 30 else 1900 + yy
    # fallback: copyright year
    m = re.search(r"Copyright\s*(?:\(c\)\s*)?(\d{4})", text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    # fallback: first 4-digit year in a plausible range
    m = re.search(r"\b(20\d{2})\b", text)
    if m:
        return int(m.group(1))
    return None

def has_empirical(text):
    if not text:
        return False
    t = text.lower()
    # heuristic: presence of methods/user study/survey/interviews/participants/experiment
    patterns = [
        r"\bmethod\b", r"\bmethods\b", r"\buser study\b", r"\bstudy\b",
        r"\bparticipants\b", r"\binterview\b", r"\binterviews\b", r"\bsurvey\b",
        r"\bexperiment\b", r"\bfield trial\b", r"\bevaluation\b"
    ]
    return any(re.search(p, t) for p in patterns)

rows = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    year = parse_year(d.get('text',''))
    empirical = has_empirical(d.get('text',''))
    rows.append({'title': title, 'year': year, 'empirical': empirical})

paper_df = pd.DataFrame(rows)
# Select empirical and published after 2016
paper_df = paper_df[(paper_df['empirical']) & (paper_df['year'].notna()) & (paper_df['year'] > 2016)]

# Load total citations per title
path_cit = var_call_zVPZKO01inNfZLG89S7tIzjw
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

cit_df = pd.DataFrame(cit)
# normalize types
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce')

out = paper_df.merge(cit_df, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
# sort by citations desc
out = out.sort_values(['total_citations','title'], ascending=[False, True])

result = out[['title','total_citations']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_BBwwzQjwsq5k0oy6UtD7pfyz': 'file_storage/call_BBwwzQjwsq5k0oy6UtD7pfyz.json', 'var_call_zVPZKO01inNfZLG89S7tIzjw': 'file_storage/call_zVPZKO01inNfZLG89S7tIzjw.json', 'var_call_EN9V0Vlayn5hR1sqO4sfeb18': 'file_storage/call_EN9V0Vlayn5hR1sqO4sfeb18.json'}

exec(code, env_args)

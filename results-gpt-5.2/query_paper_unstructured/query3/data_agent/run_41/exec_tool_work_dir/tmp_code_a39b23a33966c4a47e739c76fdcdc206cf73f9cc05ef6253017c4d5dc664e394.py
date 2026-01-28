code = """import json, re
import pandas as pd

# Load mongo docs (may be stored as json file path)
docs_src = var_call_gdpScBbhv5TooWljmDT7Dc6G
if isinstance(docs_src, str):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

cits_src = var_call_2F1arjDMEJ90CApnyrEodfYU
if isinstance(cits_src, str):
    with open(cits_src, 'r', encoding='utf-8') as f:
        cits = json.load(f)
else:
    cits = cits_src

# helpers
month_map = {
    'JANUARY':1,'FEBRUARY':2,'MARCH':3,'APRIL':4,'MAY':5,'JUNE':6,
    'JULY':7,'AUGUST':8,'SEPTEMBER':9,'OCTOBER':10,'NOVEMBER':11,'DECEMBER':12
}

def extract_year(text):
    if not text:
        return None
    t = text[:5000]
    # Prefer explicit Copyright year
    m = re.search(r'Copyright\s*(?:©|\(C\)|\u00a9)?\s*(19\d{2}|20\d{2})', t, flags=re.IGNORECASE)
    if m:
        y = int(m.group(1))
        if 1980 <= y <= 2030:
            return y
    # common bib: CHI '19 etc
    m = re.search(r"'\s*(\d{2})", t)
    if m:
        yy = int(m.group(1))
        y = 2000 + yy if yy <= 30 else 1900 + yy
        if 1980 <= y <= 2030:
            return y
    # any 4-digit year close to venue line
    years = [int(x) for x in re.findall(r'(19\d{2}|20\d{2})', t)]
    years = [y for y in years if 1980 <= y <= 2030]
    if years:
        # choose mode-like: most frequent then max
        ser = pd.Series(years)
        vc = ser.value_counts()
        y = int(vc.index[0])
        return y
    return None

def extract_contribution(text):
    if not text:
        return None
    tl = text.lower()
    # look for explicit metadata lines if present
    m = re.search(r'contribution\s*[:\-]\s*([^\n\r]+)', tl)
    if m:
        return m.group(1).strip()
    return None

# Build paper info from docs
rows = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','')
    year = extract_year(text)
    contrib = extract_contribution(text)
    # if no contrib metadata, infer empirical by keywords
    inferred_empirical = False
    if text:
        l = text.lower()
        # heuristic: if contains study methods / participants and evaluation terms
        if ('we conducted' in l or 'we interviewed' in l or 'we surveyed' in l or 'field study' in l or 'user study' in l or 'participants' in l) and ('method' in l or 'methods' in l or 'results' in l):
            inferred_empirical = True
    rows.append({'title': title, 'year': year, 'contribution_raw': contrib, 'inferred_empirical': inferred_empirical})

papers = pd.DataFrame(rows)

# Determine empirical contribution via raw field contains 'empirical' OR inferred
papers['is_empirical'] = papers['contribution_raw'].fillna('').str.contains('empirical', case=False) | papers['inferred_empirical']

# Filter after 2016
papers_f = papers[(papers['year'].notna()) & (papers['year'] > 2016) & (papers['is_empirical'])][['title','year']]

cits_df = pd.DataFrame(cits)
# total_citations might be string
cits_df['total_citations'] = pd.to_numeric(cits_df['total_citations'], errors='coerce')

out = papers_f.merge(cits_df[['title','total_citations']], on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)

out = out.sort_values(['total_citations','title'], ascending=[False, True])
result = out[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_gdpScBbhv5TooWljmDT7Dc6G': 'file_storage/call_gdpScBbhv5TooWljmDT7Dc6G.json', 'var_call_2F1arjDMEJ90CApnyrEodfYU': 'file_storage/call_2F1arjDMEJ90CApnyrEodfYU.json'}

exec(code, env_args)

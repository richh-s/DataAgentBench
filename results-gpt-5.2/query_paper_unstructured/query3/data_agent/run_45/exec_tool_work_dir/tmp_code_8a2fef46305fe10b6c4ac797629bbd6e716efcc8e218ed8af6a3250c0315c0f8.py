code = """import json, re
import pandas as pd

def load_result(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

docs = load_result(var_call_G5pt9E8NljytNhMW3F6ZBOAY)
cits = load_result(var_call_8lFpfeAXR6atp3SwD9b2Dr4g)

# Extract publication year from text using common patterns
year_patterns = [
    re.compile(r"\bCopyright\s*(?:\(c\)\s*)?(\d{4})\b", re.IGNORECASE),
    re.compile(r"\bCHI\s*'?\s*(\d{2})\b"),
]

venue_patterns = [
    ('CHI', re.compile(r"\bCHI\b", re.IGNORECASE)),
    ('Ubicomp', re.compile(r"\bUbiComp\b|\bUBICOMP\b", re.IGNORECASE)),
    ('CSCW', re.compile(r"\bCSCW\b", re.IGNORECASE)),
    ('DIS', re.compile(r"\bDIS\b", re.IGNORECASE)),
]

source_patterns = [
    ('ACM', re.compile(r"\bACM\b", re.IGNORECASE)),
    ('IEEE', re.compile(r"\bIEEE\b", re.IGNORECASE)),
    ('PubMed', re.compile(r"\bPubMed\b", re.IGNORECASE)),
]

def extract_year(text):
    m = re.search(r"\bCopyright\s*(?:\(c\)\s*)?(\d{4})\b", text, flags=re.IGNORECASE)
    if m:
        y = int(m.group(1))
        if 1980 <= y <= 2030:
            return y
    # fallback: look for typical year near top
    head = text[:2000]
    years = [int(y) for y in re.findall(r"\b(19\d{2}|20\d{2})\b", head)]
    years = [y for y in years if 1980 <= y <= 2030]
    if years:
        # choose most frequent, else min? publication year often appears multiple times; take mode then min
        from collections import Counter
        c = Counter(years)
        maxfreq = max(c.values())
        cand = [y for y,f in c.items() if f==maxfreq]
        return min(cand)
    return None

def extract_title(filename):
    return re.sub(r"\.txt$", "", filename)

def is_empirical(text):
    # substring match per hint; check for explicit 'empirical' term
    return re.search(r"\bempirical\b", text, flags=re.IGNORECASE) is not None

paper_rows = []
for d in docs:
    fn = d.get('filename','')
    text = d.get('text','') or ''
    title = extract_title(fn)
    yr = extract_year(text)
    emp = is_empirical(text)
    paper_rows.append({'title': title, 'year': yr, 'empirical': emp})

papers = pd.DataFrame(paper_rows)
# filter empirical and after 2016
papers_filt = papers[(papers['empirical']==True) & (papers['year'].notna()) & (papers['year']>2016)].copy()

cits_df = pd.DataFrame(cits)
# ensure numeric
for col in ['citation_count','citation_year']:
    cits_df[col] = pd.to_numeric(cits_df[col], errors='coerce')

# total citations per title
tot = cits_df.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citation_count'})

out = papers_filt.merge(tot, on='title', how='left')
out['total_citation_count'] = out['total_citation_count'].fillna(0).astype(int)
# sort by total citations desc
out = out.sort_values(['total_citation_count','title'], ascending=[False, True])
res = out[['title','total_citation_count']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_G5pt9E8NljytNhMW3F6ZBOAY': 'file_storage/call_G5pt9E8NljytNhMW3F6ZBOAY.json', 'var_call_8lFpfeAXR6atp3SwD9b2Dr4g': 'file_storage/call_8lFpfeAXR6atp3SwD9b2Dr4g.json'}

exec(code, env_args)

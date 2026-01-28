code = """import json, re, pandas as pd

# Load full results
paper_docs_path = var_call_YuVtDXgeVVzbHhHyY1TUBBeH
cit_path = var_call_RKrGvquW9om7II3jQdoYPQeH

with open(paper_docs_path, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)
with open(cit_path, 'r', encoding='utf-8') as f:
    cits = json.load(f)

# helper to get title from filename
def title_from_filename(fn):
    return re.sub(r'\.txt$', '', fn).strip()

# extract year and contribution from text using heuristics
year_pat = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(text):
    # look for copyright year first
    m = re.search(r'Copyright\s*(?:\(c\)\s*)?(19\d{2}|20\d{2})', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    # look for venue line like CHI '17 or UbiComp '15
    m = re.search(r"\b(?:CHI|CSCW|UBICOMP|UbiComp|DIS|IUI|WWW|TEI|OzCHI|AH|PervasiveHealth)\s*'\s*(\d{2})\b", text)
    if m:
        yy=int(m.group(1))
        return 2000+yy if yy<70 else 1900+yy
    # else, take earliest plausible year in first 2000 chars
    head=text[:2000]
    yrs=[int(y) for y in year_pat.findall(head)]
    yrs=[y for y in yrs if 1990<=y<=2026]
    return min(yrs) if yrs else None

def is_empirical(text):
    # crude: contains 'study', 'participants', 'we interviewed', 'we surveyed', 'experiment'
    t=text.lower()
    empirical_markers = [
        'we conducted', 'we present', 'we interviewed', 'we surveyed', 'participants',
        'user study', 'field study', 'experiment', 'ethnograph', 'diary study', 'survey'
    ]
    # also require word empirical appears somewhere (per question)
    if 'empirical' in t:
        return True
    # if not, still might be labeled as empirical in metadata not present; follow question strictly
    return False

rows=[]
for doc in paper_docs:
    title=title_from_filename(doc.get('filename',''))
    text=doc.get('text','') or ''
    year=extract_year(text)
    if year is None or year<=2016:
        continue
    if not is_empirical(text):
        continue
    rows.append({'title': title, 'year': year})

papers_df=pd.DataFrame(rows).drop_duplicates('title')

cits_df=pd.DataFrame(cits)
if not cits_df.empty:
    cits_df['citation_count']=pd.to_numeric(cits_df['citation_count'], errors='coerce').fillna(0).astype(int)

# total citations across years per title
cit_tot = cits_df.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})

out = papers_df.merge(cit_tot, on='title', how='left')
out['total_citations']=out['total_citations'].fillna(0).astype(int)

out = out.sort_values(['total_citations','title'], ascending=[False, True])
result = out[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_YuVtDXgeVVzbHhHyY1TUBBeH': 'file_storage/call_YuVtDXgeVVzbHhHyY1TUBBeH.json', 'var_call_RKrGvquW9om7II3jQdoYPQeH': 'file_storage/call_RKrGvquW9om7II3jQdoYPQeH.json'}

exec(code, env_args)

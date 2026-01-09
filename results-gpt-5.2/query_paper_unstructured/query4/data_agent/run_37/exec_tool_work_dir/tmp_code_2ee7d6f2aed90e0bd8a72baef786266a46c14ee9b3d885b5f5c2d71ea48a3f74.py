code = """import json, re, pandas as pd

def load_tool_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

paper_docs = load_tool_result(var_call_EDJvhCqHJlKIkWQZijPKTMy4)
citations = load_tool_result(var_call_3xBMxPGPszQAvaxYnVwj301F)

# Extract publication year and domains from paper text (heuristics)

def extract_year(text):
    if not text:
        return None
    # Prefer explicit copyright year
    m = re.search(r'Copyright\s*(?:\(c\))?\s*(\d{4})', text, flags=re.IGNORECASE)
    if m:
        y = int(m.group(1))
        if 1980 <= y <= 2030:
            return y
    # Look for venue year patterns e.g., CHI '16 or UbiComp '16
    m = re.search(r"\b(?:CHI|UbiComp|CSCW|DIS|IUI|WWW|TEI|AH|PervasiveHealth|OzCHI)\s*'?\s*(\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy < 80 else 1900 + yy
    # Any year near top
    head = text[:2000]
    years = [int(y) for y in re.findall(r'\b(20\d{2}|19\d{2})\b', head)]
    years = [y for y in years if 1980 <= y <= 2030]
    return years[0] if years else None

def extract_domains(text):
    if not text:
        return ''
    head = text[:5000]
    # Author Keywords section
    m = re.search(r'Author Keywords\s*(.*?)\n\s*\n', head, flags=re.IGNORECASE|re.DOTALL)
    kw = m.group(1) if m else head
    kw = kw.replace('\n',' ')
    return kw.lower()

rows=[]
for d in paper_docs:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$','', fn)
    text = d.get('text','')
    year = extract_year(text)
    dom_blob = extract_domains(text)
    rows.append({'title': title, 'pub_year': year, 'dom_blob': dom_blob})

pdf = pd.DataFrame(rows)
# Filter to physical activity domain and year 2016
mask = (pdf['pub_year']==2016) & (pdf['dom_blob'].str.contains('physical activity', na=False))
phys2016 = pdf.loc[mask, ['title']].drop_duplicates()

cdf = pd.DataFrame(citations)
if len(cdf):
    cdf['citation_count'] = pd.to_numeric(cdf['citation_count'], errors='coerce').fillna(0).astype(int)

# Total citations across all years for each paper
ctot = cdf.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})

out = phys2016.merge(ctot, on='title', how='left').fillna({'total_citations':0})
out['total_citations'] = out['total_citations'].astype(int)
out = out.sort_values(['total_citations','title'], ascending=[False, True])

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_EDJvhCqHJlKIkWQZijPKTMy4': 'file_storage/call_EDJvhCqHJlKIkWQZijPKTMy4.json', 'var_call_3xBMxPGPszQAvaxYnVwj301F': 'file_storage/call_3xBMxPGPszQAvaxYnVwj301F.json'}

exec(code, env_args)

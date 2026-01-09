code = """import json, re
import pandas as pd

# load docs
with open(var_call_fctWhpzPaIUkV7suRLsL7LGk, 'r', encoding='utf-8') as f:
    docs = json.load(f)
# load citations
with open(var_call_pJUoBOD4gzic997sxqFXbYgW, 'r', encoding='utf-8') as f:
    cit = json.load(f)

cit_df = pd.DataFrame(cit)
cit_df['title'] = cit_df['title'].astype(str)
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

contrib_pat = re.compile(r'\bempirical\b', re.IGNORECASE)
year_pat1 = re.compile(r'\b(19\d{2}|20\d{2})\b')
venue_year_pat = re.compile(r"\b(?:CHI|CSCW|UbiComp|UBICOMP|DIS|IUI|OzCHI|TEI|WWW|PervasiveHealth)\s*'?\s*(\d{2})\b")

def extract_year(text):
    m = re.search(r'Copyright\s*(?:\(c\)\s*)?(19\d{2}|20\d{2})', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = venue_year_pat.search(text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy < 50 else 1900 + yy
    years = [int(y) for y in year_pat1.findall(text)]
    years = [y for y in years if 1990 <= y <= 2026]
    return min(years) if years else None

rows=[]
for d in docs:
    title = d.get('filename','')
    if title.lower().endswith('.txt'):
        title = title[:-4]
    text = d.get('text','') or ''
    year = extract_year(text)
    if year is None:
        continue
    if year > 2016 and contrib_pat.search(text):
        rows.append({'title': title, 'year': year})

papers_df = pd.DataFrame(rows).drop_duplicates('title')

out = papers_df.merge(cit_df[['title','total_citations']], on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out[['title','total_citations']].sort_values(['total_citations','title'], ascending=[False, True])

print('__RESULT__:')
print(json.dumps(out.to_dict(orient='records')))"""

env_args = {'var_call_F6F7FPlZguD3C8fO9BEXO9cQ': 'file_storage/call_F6F7FPlZguD3C8fO9BEXO9cQ.json', 'var_call_pJUoBOD4gzic997sxqFXbYgW': 'file_storage/call_pJUoBOD4gzic997sxqFXbYgW.json', 'var_call_fctWhpzPaIUkV7suRLsL7LGk': 'file_storage/call_fctWhpzPaIUkV7suRLsL7LGk.json', 'var_call_8iwBWdX0qMkplau8jqlyAoGI': {'columns': ['title', 'total_citations'], 'head': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'total_citations': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'total_citations': '313'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'total_citations': '368'}, {'title': 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'total_citations': '277'}]}}

exec(code, env_args)

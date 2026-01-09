code = """import json, re
import pandas as pd

# Load mongo result (large) from file
mongo_path = var_call_NIfMNiXvpRy1ASYfP2x2fKJc
with open(mongo_path, 'r', encoding='utf-8') as f:
    mongo_docs = json.load(f)

cit_path = var_call_kv1vFazdUi2sn1Ufr5G8IqeK
# cit result may also be a file path
if isinstance(cit_path, str) and cit_path.endswith('.json'):
    with open(cit_path, 'r', encoding='utf-8') as f:
        cit_rows = json.load(f)
else:
    cit_rows = cit_path

# Helper to extract year near header; look for 2016 occurrences like "CHI '16" etc or copyright year

def extract_year(text):
    # prioritize patterns like "'16" with venue
    m = re.search(r"\b(?:CHI|UbiComp|Ubicomp|CSCW|DIS|IUI|WWW|TEI|AH|OzCHI|PervasiveHealth)\s*['’](\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy
    # copyright year
    m = re.search(r"Copyright\s+(\d{4})", text)
    if m:
        return int(m.group(1))
    # year standalone near top
    head = text[:2000]
    years = re.findall(r"\b(20\d{2})\b", head)
    if years:
        # choose most frequent in head
        from collections import Counter
        c = Counter(map(int, years))
        return c.most_common(1)[0][0]
    return None

# Domain detection: require 'physical activity' substring in keywords or text

def is_physical_activity_domain(text):
    return re.search(r"(?i)physical\s+activity", text) is not None

papers = []
for d in mongo_docs:
    fn = d.get('filename','')
    title = re.sub(r"\.txt$", "", fn)
    text = d.get('text','') or ''
    if not is_physical_activity_domain(text):
        continue
    year = extract_year(text)
    papers.append({'title': title, 'year': year})

pdf = pd.DataFrame(papers).drop_duplicates(subset=['title'])
# filter published in 2016
pdf_2016 = pdf[pdf['year']==2016].copy()

cdf = pd.DataFrame(cit_rows)
# totals may be strings
if not cdf.empty:
    cdf['total_citations'] = pd.to_numeric(cdf['total_citations'], errors='coerce').fillna(0).astype(int)

out = pdf_2016.merge(cdf, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out.sort_values(['total_citations','title'], ascending=[False, True])
result = out[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_NIfMNiXvpRy1ASYfP2x2fKJc': 'file_storage/call_NIfMNiXvpRy1ASYfP2x2fKJc.json', 'var_call_kv1vFazdUi2sn1Ufr5G8IqeK': 'file_storage/call_kv1vFazdUi2sn1Ufr5G8IqeK.json'}

exec(code, env_args)

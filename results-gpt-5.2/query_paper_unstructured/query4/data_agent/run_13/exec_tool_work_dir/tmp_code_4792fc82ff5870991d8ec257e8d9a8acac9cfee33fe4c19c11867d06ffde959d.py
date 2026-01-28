code = """import json, re
import pandas as pd

# load docs
path = var_call_UeanCZ2Ph1Wzzih08kqWsV9x
with open(path,'r',encoding='utf-8') as f:
    docs = json.load(f)

# load citations totals
cpath = var_call_0Mro7YzlxkD4BgEGQLoRp8hz
with open(cpath,'r',encoding='utf-8') as f:
    cit = json.load(f)
cit_df = pd.DataFrame(cit)
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)


def extract_year(text):
    head = text[:3500]
    if re.search(r'\b2016\b', head):
        return 2016
    if re.search(r"'\s*16\b", head) and re.search(r'\b(chi|ubicomp|cscw|dis|www|iui|ozchi|tei|ah|pervasivehealth)\b', head, flags=re.I):
        return 2016
    m2 = re.search(r'\b(19|20)\d{2}\b', head)
    return int(m2.group(0)) if m2 else None

def is_physical_activity_domain(text):
    head = text[:5000]
    if re.search(r'(?i)domain\s*[:\-]\s*.*physical\s+activity', head):
        return True
    if re.search(r'(?i)author\s+keywords[\s\S]{0,800}physical\s+activity', head):
        return True
    if re.search(r'(?i)physical\s+activity', text):
        return True
    return False

rows=[]
for d in docs:
    title = d.get('filename','').rsplit('.txt',1)[0]
    text = d.get('text','') or ''
    if not title:
        continue
    if not is_physical_activity_domain(text):
        continue
    if extract_year(text)==2016:
        rows.append({'title': title})

paper_df = pd.DataFrame(rows).drop_duplicates()

if paper_df.empty:
    result = []
else:
    out = paper_df.merge(cit_df, on='title', how='left')
    out['total_citations'] = out['total_citations'].fillna(0).astype(int)
    out = out.sort_values(['total_citations','title'], ascending=[False, True])
    result = out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps({'count': len(result), 'records': result[:50]}))"""

env_args = {'var_call_0Mro7YzlxkD4BgEGQLoRp8hz': 'file_storage/call_0Mro7YzlxkD4BgEGQLoRp8hz.json', 'var_call_UeanCZ2Ph1Wzzih08kqWsV9x': 'file_storage/call_UeanCZ2Ph1Wzzih08kqWsV9x.json', 'var_call_p026YWcQVP4MkLj8ClpLArW2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_call_voAOLXYrBcdBhITBaLoARJ5I': {'columns': ['title', 'total_citations'], 'head': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'total_citations': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'total_citations': '313'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}]}}

exec(code, env_args)

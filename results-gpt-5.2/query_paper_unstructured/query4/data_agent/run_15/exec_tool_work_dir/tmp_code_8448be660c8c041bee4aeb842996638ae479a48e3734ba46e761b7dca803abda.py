code = """import json, re
import pandas as pd

def load(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

papers = load(var_call_GJqrAc3pEFQFIPbsltgnJi46)
cits = load(var_call_sbVyc8J6367gQ2BeFEB5P5uJ)

df_p = pd.DataFrame(papers)
df_c = pd.DataFrame(cits)

def filename_to_title(fn):
    return re.sub(r'\.txt$', '', fn) if isinstance(fn,str) else None

# extract publication year from venue header lines
venue_year_patterns = [
    r"\bCHI\s*'?(\d{2,4})\b",
    r"\bUbiComp\s*'?(\d{2,4})\b",
    r"\bUbicomp\s*'?(\d{2,4})\b",
    r"\bCSCW\s*'?(\d{2,4})\b",
    r"\bDIS\s*'?(\d{2,4})\b",
    r"\bIUI\s*'?(\d{2,4})\b",
    r"\bWWW\s*'?(\d{2,4})\b",
    r"\bTEI\s*'?(\d{2,4})\b",
    r"\bOzCHI\s*'?(\d{2,4})\b",
    r"\bPervasiveHealth\s*'?(\d{2,4})\b",
]

def norm_year(y):
    y=int(y)
    if y<100:
        return 2000+y
    return y

def extract_pub_year(txt):
    if not isinstance(txt,str):
        return None
    head = txt[:3000]
    for pat in venue_year_patterns:
        m=re.search(pat, head, flags=re.I)
        if m:
            return norm_year(m.group(1))
    # fallback any year in head
    m=re.search(r'\b(19|20)\d{2}\b', head)
    return int(m.group(0)) if m else None

if not df_p.empty:
    df_p['title']=df_p['filename'].apply(filename_to_title)
    df_p['pub_year']=df_p['text'].apply(extract_pub_year)

pa2016 = df_p[df_p['pub_year']==2016][['title']].dropna().drop_duplicates()

if pa2016.empty:
    out=[]
else:
    df_c['total_citations']=pd.to_numeric(df_c['total_citations'])
    merged = pa2016.merge(df_c, on='title', how='left')
    merged['total_citations']=merged['total_citations'].fillna(0).astype(int)
    merged=merged.sort_values(['total_citations','title'], ascending=[False, True])
    out=merged.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_NB3Maq1dVPeh4msKKn1SEtew': 'file_storage/call_NB3Maq1dVPeh4msKKn1SEtew.json', 'var_call_sbVyc8J6367gQ2BeFEB5P5uJ': 'file_storage/call_sbVyc8J6367gQ2BeFEB5P5uJ.json', 'var_call_g8BxL16hB7zMSrlMEaYq2Dup': [], 'var_call_GJqrAc3pEFQFIPbsltgnJi46': 'file_storage/call_GJqrAc3pEFQFIPbsltgnJi46.json'}

exec(code, env_args)

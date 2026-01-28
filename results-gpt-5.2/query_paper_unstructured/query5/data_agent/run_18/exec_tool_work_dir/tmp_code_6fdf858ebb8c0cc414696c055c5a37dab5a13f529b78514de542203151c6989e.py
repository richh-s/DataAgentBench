code = """import json, re
import pandas as pd

# Load citations 2020
path_cit = var_call_xwJY1upmut1pJPLyopTrMQnS
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
# coerce types
if not df_cit.empty:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

# Load paper docs
path_docs = var_call_83MpOqyahzqLwNuseTcsNb0P
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def is_chi(text):
    if not text:
        return False
    t = text.lower()
    # match common chi proceedings lines
    if re.search(r"\bchi\s*'?\s*\d{2}\b", t):
        return True
    if re.search(r"\bproceedings\s+of\s+the\s+chi\b", t):
        return True
    if re.search(r"\bacm\s+chi\b", t):
        return True
    # sometimes just 'CHI ' with year
    if re.search(r"\bchi\b.*\bconference\b", t):
        return True
    return False

chi_titles = []
for d in docs:
    fn = d.get('filename','')
    title = re.sub(r"\.txt$","", fn)
    if is_chi(d.get('text','')):
        chi_titles.append(title)

chi_set = set(chi_titles)

# Join with citations and aggregate
if df_cit.empty:
    res = {"total_citations": 0, "num_papers": 0}
else:
    df_chi = df_cit[df_cit['title'].isin(chi_set)].copy()
    total = int(df_chi['citation_count'].sum())
    num = int(df_chi['title'].nunique())
    res = {"total_citations": total, "num_papers": num}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_xwJY1upmut1pJPLyopTrMQnS': 'file_storage/call_xwJY1upmut1pJPLyopTrMQnS.json', 'var_call_83MpOqyahzqLwNuseTcsNb0P': 'file_storage/call_83MpOqyahzqLwNuseTcsNb0P.json'}

exec(code, env_args)

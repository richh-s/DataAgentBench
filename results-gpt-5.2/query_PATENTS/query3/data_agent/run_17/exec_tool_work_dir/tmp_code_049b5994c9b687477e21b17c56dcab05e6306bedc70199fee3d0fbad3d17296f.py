code = """import json, re
from pathlib import Path
import pandas as pd

p_uc = Path(var_call_N4ojgkXEmX1Jc6eA1Rcu8Ai3)
uc_recs = json.loads(p_uc.read_text())
uc_pubs=set()
for r in uc_recs:
    s=r.get('Patents_info') or ''
    m=re.search(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', s)
    if m: uc_pubs.add(m.group(1))

p_all = Path(var_call_m1vGRvdFIx0Ma5zlVsHTQiS2)
all_recs = json.loads(p_all.read_text())

rows=[]
for r in all_recs:
    patinfo=r.get('Patents_info') or ''
    m=re.match(r'^(.*?)\s+holds\s+the\s+', patinfo)
    if not m:
        m=re.match(r'^(.*?)\s+hold[s]?\s+', patinfo)
    assignee=(m.group(1).strip() if m else None)
    if not assignee or 'UNIV CALIFORNIA' in assignee:
        continue
    cit=r.get('citation')
    if not cit: continue
    try:
        cits=json.loads(cit)
    except Exception:
        continue
    cited=[c.get('publication_number') for c in cits if isinstance(c, dict) and c.get('publication_number')]
    if not any(cp in uc_pubs for cp in cited):
        continue
    try:
        cpc_list=json.loads(r.get('cpc') or '[]')
    except Exception:
        cpc_list=[]
    prim=[c.get('code') for c in cpc_list if isinstance(c, dict) and c.get('first') is True and c.get('code')]
    subclasses=sorted(set([pc[:4] for pc in prim if isinstance(pc,str) and len(pc)>=4]))
    for sc in subclasses:
        rows.append({'citing_assignee': assignee, 'cpc_subclass': sc})

df=pd.DataFrame(rows)
if len(df)==0:
    out={'pairs':[], 'unique_subclasses':[], 'n_pairs':0}
else:
    df=df.drop_duplicates()
    out={'pairs':df.to_dict(orient='records'), 'unique_subclasses':sorted(df['cpc_subclass'].unique().tolist()), 'n_pairs':int(len(df))}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_5AUI9b2HwVlqPgKeuUNmzwnA': ['publicationinfo'], 'var_call_fFL44BPQqFYmpSYenwLj41ss': ['cpc_definition'], 'var_call_aFHQuknr5izMKHWl3Wz6WmNM': [], 'var_call_N4ojgkXEmX1Jc6eA1Rcu8Ai3': 'file_storage/call_N4ojgkXEmX1Jc6eA1Rcu8Ai3.json', 'var_call_psh09EGT6IKk7nKXoNgFFI3O': {'uc_pub_count': 64, 'sample_uc_pubs': ['AU-2003297741-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2009234210-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2019275518-B2', 'AU-6492396-A', 'AU-6535890-A', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CN-100339724-C', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-4284234-A1', 'HK-1250569-A1']}, 'var_call_m1vGRvdFIx0Ma5zlVsHTQiS2': 'file_storage/call_m1vGRvdFIx0Ma5zlVsHTQiS2.json'}

exec(code, env_args)

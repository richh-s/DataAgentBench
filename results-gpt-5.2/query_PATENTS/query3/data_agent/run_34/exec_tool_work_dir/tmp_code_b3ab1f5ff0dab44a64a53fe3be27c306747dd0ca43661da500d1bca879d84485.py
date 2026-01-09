code = """import json, re
import pandas as pd

src = var_call_JQ2qp7XrKTwEmiiZItrkiLYb
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        recs = json.load(f)
else:
    recs = src

pub_re = re.compile(r'pub\. number\s+([A-Z]{2,}-[0-9]+[A-Z0-9-]*?)\b')

rows = []
for r in recs:
    pi = r.get('Patents_info','') or ''
    m = pub_re.search(pi)
    if not m:
        continue
    uc_pub = m.group(1)

    cit = r.get('citation')
    if not cit:
        continue
    try:
        cit_list = json.loads(cit)
    except Exception:
        continue
    if not isinstance(cit_list, list) or not cit_list:
        continue

    # primary CPC subclass codes
    subclasses = []
    cpc_raw = r.get('cpc')
    if cpc_raw:
        try:
            cpc_list = json.loads(cpc_raw)
            for e in cpc_list:
                if isinstance(e, dict) and e.get('first') is True and isinstance(e.get('code'), str):
                    subclasses.append(e['code'][:4])
        except Exception:
            pass
    subclasses = sorted(set(subclasses))

    for c in cit_list:
        if isinstance(c, dict) and c.get('publication_number'):
            rows.append({'uc_pub': uc_pub, 'citing_pub': c['publication_number'], 'uc_primary_subclasses': subclasses})

if rows:
    df = pd.DataFrame(rows).drop_duplicates()
    citing_pubs = sorted(df['citing_pub'].unique().tolist())
    uc_map = df.groupby('uc_pub')['uc_primary_subclasses'].apply(lambda s: sorted(set(sum(s.tolist(), [])))).to_dict()
else:
    df = pd.DataFrame([])
    citing_pubs = []
    uc_map = {}

out = {'n_rows': len(rows), 'n_citing_pubs': len(citing_pubs), 'citing_pubs_sample': citing_pubs[:20], 'citing_pubs': citing_pubs, 'uc_pub_to_primary_subclasses': uc_map}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_50CPxvMzlC1CSjfgaYP3oqUB': ['publicationinfo'], 'var_call_aKUrwwqru8I0JXOtcsuLlGZn': ['cpc_definition'], 'var_call_JQ2qp7XrKTwEmiiZItrkiLYb': 'file_storage/call_JQ2qp7XrKTwEmiiZItrkiLYb.json'}

exec(code, env_args)

code = """import json, re
import pandas as pd

# Load full records
src = var_call_JQ2qp7XrKTwEmiiZItrkiLYb
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        recs = json.load(f)
else:
    recs = src

# helper to extract publication_number from Patents_info
pub_re = re.compile(r'pub\. number\s+([A-Z]{2,}-[0-9]+[A-Z0-9-]*?)\b')
ass_re = re.compile(r'owned by (.+?) and has|is assigned to (.+?) and has|holds the .+? owned by (.+?) and has|holds the .*? filing .*? with pub\. number', re.IGNORECASE)

rows = []
for r in recs:
    pi = r.get('Patents_info','') or ''
    m = pub_re.search(pi)
    if not m:
        continue
    cited_pub = m.group(1)
    # parse citations list
    cit = r.get('citation')
    if not cit:
        continue
    try:
        cit_list = json.loads(cit)
    except Exception:
        continue
    if not isinstance(cit_list, list) or len(cit_list)==0:
        continue

    # primary CPC subclasses from cpc field: entries with first==true; take subclass as first 4 chars (e.g., F25B)
    cpc_raw = r.get('cpc')
    subclasses = []
    if cpc_raw:
        try:
            cpc_list = json.loads(cpc_raw)
            for e in cpc_list:
                if isinstance(e, dict) and e.get('first') is True and isinstance(e.get('code'), str):
                    code = e['code']
                    subclass = code[:4]  # CPC subclass (e.g., F25B)
                    subclasses.append(subclass)
        except Exception:
            pass
    subclasses = sorted(set(subclasses))

    for c in cit_list:
        pubnum = (c or {}).get('publication_number')
        if pubnum:
            rows.append({'uc_pub': cited_pub, 'citing_pub': pubnum, 'uc_primary_subclasses': subclasses})

df = pd.DataFrame(rows).drop_duplicates()

# We need assignee of citing_pub (excluding UNIV CALIFORNIA)
# Query publicationinfo for all citing_pub
citing_pubs = sorted(df['citing_pub'].unique().tolist())

# chunk for SQL IN
chunks = [citing_pubs[i:i+500] for i in range(0, len(citing_pubs), 500)]

queries = []
for ch in chunks:
    inlist = ','.join(["'"+p.replace("'","''")+"'" for p in ch])
    queries.append(f"SELECT Patents_info as pi FROM publicationinfo WHERE Patents_info LIKE '%pub. number {''}%' AND (" + " OR ".join([f"Patents_info LIKE '%pub. number {p}%'" for p in ch]) + ");")

# Can't execute queries here; just output needed pubs and uc_subclasses mapping
out = {
    'citing_pubs': citing_pubs,
    'uc_pub_to_primary_subclasses': df.groupby('uc_pub')['uc_primary_subclasses'].apply(lambda s: sorted(set(sum(s.tolist(), [])))).to_dict()
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_50CPxvMzlC1CSjfgaYP3oqUB': ['publicationinfo'], 'var_call_aKUrwwqru8I0JXOtcsuLlGZn': ['cpc_definition'], 'var_call_JQ2qp7XrKTwEmiiZItrkiLYb': 'file_storage/call_JQ2qp7XrKTwEmiiZItrkiLYb.json'}

exec(code, env_args)

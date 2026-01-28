code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub_all = load_records(var_call_3qJin6Dl7iefkmS74xo1mP8N)
cpcdef = load_records(var_call_F202JETNOsuY4uV6uorGzZRJ)

sym2title = {r['symbol']: r.get('titleFull') for r in cpcdef}

def parse_pubno(pat_info: str):
    if not isinstance(pat_info, str):
        return None
    m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', pat_info)
    return m.group(1) if m else None

def parse_assignee(pat_info: str):
    if not isinstance(pat_info, str):
        return None
    # patterns
    m = re.search(r'^(.*?)\s+holds\b', pat_info)
    if not m:
        m = re.search(r'^(.*?)\s+owns\b', pat_info)
    if not m:
        m = re.search(r'^In\s+[A-Z]{2},\s+the\s+.*?\s+is\s+assigned\s+to\s+(.*?)\s+and\s+has\s+publication\s+number\b', pat_info)
    if not m:
        m = re.search(r'^(.*?)\s+holds\s+the\s+[A-Z]{2}\s+patent\s+filing', pat_info)
    return m.group(1).strip() if m else None

def parse_cpc_primary_subclass(cpc_str: str):
    if not isinstance(cpc_str, str) or not cpc_str.strip():
        return None
    try:
        lst = json.loads(cpc_str)
    except Exception:
        return None
    if not isinstance(lst, list) or len(lst)==0:
        return None
    # choose first==true if present else first item
    primary = None
    for it in lst:
        if isinstance(it, dict) and it.get('first') is True and it.get('code'):
            primary = it['code']
            break
    if primary is None:
        for it in lst:
            if isinstance(it, dict) and it.get('code'):
                primary = it['code']
                break
    if not primary:
        return None
    # subclass is first 4 chars like H01M
    return primary[:4]

def parse_citations(cit_str: str):
    if not isinstance(cit_str, str) or not cit_str.strip():
        return []
    try:
        lst = json.loads(cit_str)
    except Exception:
        return []
    pubs=[]
    if isinstance(lst, list):
        for it in lst:
            if isinstance(it, dict):
                pn = it.get('publication_number')
                if pn:
                    pubs.append(pn)
    return pubs

# Build publication lookup
records=[]
for r in pub_all:
    pat_info = r.get('Patents_info')
    pubno = parse_pubno(pat_info)
    assignee = parse_assignee(pat_info)
    subclass = parse_cpc_primary_subclass(r.get('cpc'))
    citations = parse_citations(r.get('citation'))
    records.append({
        'pubno': pubno,
        'assignee': assignee,
        'primary_subclass': subclass,
        'citations': citations
    })

df = pd.DataFrame(records)

# UC pub numbers
uc_pubnos = set(df.loc[df['assignee'].fillna('').str.contains('UNIV CALIFORNIA', case=False, regex=False), 'pubno'].dropna().tolist())

# Find citing patents that cite any UC pub
mask_citing = df['citations'].apply(lambda lst: any(pn in uc_pubnos for pn in lst))
df_citing = df.loc[mask_citing & df['assignee'].notna()].copy()

# Exclude assignee being UNIV CALIFORNIA itself
uc_mask = df_citing['assignee'].str.contains('UNIV CALIFORNIA', case=False, regex=False)
df_citing = df_citing.loc[~uc_mask]

# Map subclass to titleFull; need exact CPC symbol at subclass level like H01M
# Some definitions may include no slash; use symbol==subclass

def subclass_title(sub):
    if not isinstance(sub, str):
        return None
    return sym2title.get(sub)

df_citing['cpc_subclass_title'] = df_citing['primary_subclass'].apply(subclass_title)

out = (df_citing[['assignee','primary_subclass','cpc_subclass_title']]
       .dropna(subset=['assignee','primary_subclass'])
       .drop_duplicates()
       .sort_values(['assignee','primary_subclass']))

# format as requested: name + full title
final = []
for _, row in out.iterrows():
    final.append({
        'citing_assignee': row['assignee'],
        'cpc_subclass': row['primary_subclass'],
        'cpc_subclass_titleFull': row['cpc_subclass_title']
    })

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_r6BfMH8uFQpVcarQ98anmSg7': 'file_storage/call_r6BfMH8uFQpVcarQ98anmSg7.json', 'var_call_F202JETNOsuY4uV6uorGzZRJ': 'file_storage/call_F202JETNOsuY4uV6uorGzZRJ.json', 'var_call_V6FFn220VGvQuirN9Fmq7mCb': {'error': 'Insufficient data: only UC-assigned publications were queried; need all publications to find patents that cite UC patents.'}, 'var_call_3qJin6Dl7iefkmS74xo1mP8N': 'file_storage/call_3qJin6Dl7iefkmS74xo1mP8N.json'}

exec(code, env_args)

code = """import json, re, pandas as pd
from pathlib import Path

# Load large query result
p = Path(var_call_HqyVKqbR9Zae4NA2lAalCQYi)
recs = json.loads(p.read_text())

def parse_assignee(pi: str):
    # patterns observed: "<ASSIGNEE> holds..." or "... is owned by <ASSIGNEE> ..." or "... is assigned to <ASSIGNEE> ..."
    m = re.search(r'^(.*?) holds the US patent', pi)
    if m:
        return m.group(1).strip()
    m = re.search(r'is owned by ([^,]+)', pi)
    if m:
        return m.group(1).strip()
    m = re.search(r'is assigned to ([^,]+)', pi)
    if m:
        return m.group(1).strip()
    m = re.search(r'owned by ([^,]+)', pi)
    if m:
        return m.group(1).strip()
    return None

def parse_pubnum(pi: str):
    m = re.search(r'pub\.? number ([A-Z]{2}-[0-9A-Z-]+)\.?', pi)
    if m:
        return m.group(1)
    m = re.search(r'publication number ([A-Z]{2}-[0-9A-Z-]+)\.?', pi)
    if m:
        return m.group(1)
    m = re.search(r'publication no\.? ([A-Z]{2}-[0-9A-Z-]+)\.?', pi)
    if m:
        return m.group(1)
    m = re.search(r'with publication no\.? ([A-Z]{2}-[0-9A-Z-]+)\.?', pi)
    if m:
        return m.group(1)
    return None

rows=[]
for r in recs:
    pi=r.get('Patents_info','')
    ass=parse_assignee(pi)
    if not ass: continue
    if 'UNIV CALIFORNIA' not in ass and 'UNIVERSITY OF CALIFORNIA' not in ass:
        continue
    pub=parse_pubnum(pi)
    rows.append({'uc_pub':pub,'uc_assignee':ass,'citation':r.get('citation'), 'cpc':r.get('cpc')})

uc_df=pd.DataFrame(rows).drop_duplicates(subset=['uc_pub'])

# Build a set of UC publication numbers cited by others
uc_pubs=set([x for x in uc_df['uc_pub'].dropna().unique().tolist()])

# Now scan all records for citations to any UC pub, and capture citing assignee + their primary CPC subclass
citing=[]
for r in recs:
    pi=r.get('Patents_info','')
    citing_ass=parse_assignee(pi)
    if not citing_ass: continue
    if 'UNIV CALIFORNIA' in citing_ass or 'UNIVERSITY OF CALIFORNIA' in citing_ass:
        continue
    # parse citations list
    cits=r.get('citation')
    try:
        cit_list=json.loads(cits) if isinstance(cits,str) and cits.strip().startswith('[') else []
    except Exception:
        cit_list=[]
    cited_any=False
    for c in cit_list:
        pn=c.get('publication_number')
        if pn in uc_pubs:
            cited_any=True
            break
    if not cited_any:
        continue
    # primary CPC = entries where first==true; take their subclass (first 4 chars with letter+2digits+letter?) e.g., F25B
    cpc_str=r.get('cpc')
    primary_codes=[]
    try:
        cpc_list=json.loads(cpc_str) if isinstance(cpc_str,str) and cpc_str.strip().startswith('[') else []
    except Exception:
        cpc_list=[]
    for ce in cpc_list:
        if ce.get('first') is True and ce.get('code'):
            code=ce['code']
            # extract subclass like F25B from beginning pattern [A-HY][0-9]{2}[A-Z]
            m=re.match(r'^([A-HY][0-9]{2}[A-Z])', code)
            if m:
                primary_codes.append(m.group(1))
    primary_codes=list(dict.fromkeys(primary_codes))
    if not primary_codes:
        continue
    for sc in primary_codes:
        citing.append({'citing_assignee':citing_ass,'cpc_subclass':sc})

cite_df=pd.DataFrame(citing).drop_duplicates()

out = cite_df.to_json(orient='records')
print('__RESULT__:')
print(out)"""

env_args = {'var_call_22VLHQ3yCXqnKDQyP4sc848B': ['publicationinfo'], 'var_call_Ux4w54GioPBWWY6oLDBbRY3W': ['cpc_definition'], 'var_call_5X7lnv7qvSIP0eKu0EMh8mgT': [], 'var_call_GRxiEeBBkAXR8FIoNbUcu3Lz': [], 'var_call_tnPcflxzrPW3IU08Nlpvh51J': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_call_HqyVKqbR9Zae4NA2lAalCQYi': 'file_storage/call_HqyVKqbR9Zae4NA2lAalCQYi.json'}

exec(code, env_args)

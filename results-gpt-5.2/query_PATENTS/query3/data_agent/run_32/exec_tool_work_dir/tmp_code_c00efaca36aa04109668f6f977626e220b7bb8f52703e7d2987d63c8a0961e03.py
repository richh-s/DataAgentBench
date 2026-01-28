code = """import json, pandas as pd, re
from pathlib import Path

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str) and maybe_path_or_list.endswith('.json'):
        return json.loads(Path(maybe_path_or_list).read_text())
    return maybe_path_or_list

recs = load_records(var_call_v1sFxtXkdlNl4BqSXhS1KsPN)

# build map publication_number -> (assignee, primary_cpc_subclass)
assignee_by_pub = {}
primary_subclass_by_pub = {}

for r in recs:
    pi = r.get('Patents_info','') or ''
    m = re.search(r"owned by (.+?) and has pub\.", pi)
    if not m:
        m = re.search(r"assigned to (.+?) and has pub\.", pi)
    if not m:
        m = re.search(r"holds the US patent (?:application|filing) \(.*?\), with publication number (.+?)\.", pi)
    # publication number
    mpub = re.search(r"publication (?:no\.|number) ([A-Z]{2}-[0-9A-Z-]+)\.", pi)
    if not mpub:
        mpub = re.search(r"publication number ([A-Z]{2}-[0-9A-Z-]+)\.", pi)
    pub = mpub.group(1) if mpub else None

    assignee = None
    if 'owned by ' in pi or 'assigned to ' in pi:
        if m:
            assignee = m.group(1).strip()
    else:
        # pattern like "PANASONIC... holds ... with publication number ..."
        m2 = re.match(r"(.+?) holds the ", pi)
        if m2:
            assignee = m2.group(1).strip()

    if pub and assignee:
        assignee_by_pub[pub] = assignee

    # primary CPC subclass: take first==true entries and reduce to subclass (first 4 chars?)
    cpc_txt = r.get('cpc')
    primary_subclass = None
    if cpc_txt:
        try:
            cpcs = json.loads(cpc_txt)
            first_codes = [x.get('code') for x in cpcs if x.get('first') is True and x.get('code')]
            if first_codes:
                code = first_codes[0]
                # subclass is section+class+subclass letter = first 4 of symbol like A61K
                msc = re.match(r"^([A-HY]\d\d[A-Z])", code)
                primary_subclass = msc.group(1) if msc else None
        except Exception:
            primary_subclass=None
    if pub and primary_subclass:
        primary_subclass_by_pub[pub]=primary_subclass

# Find UC publications
uc_pubs = {pub for pub, a in assignee_by_pub.items() if a.strip().upper()=='UNIV CALIFORNIA'}

# Build citations from all records to UC pubs
pairs=[]
for r in recs:
    pi = r.get('Patents_info','') or ''
    # identify citing pub and assignee
    mpub = re.search(r"publication (?:no\.|number) ([A-Z]{2}-[0-9A-Z-]+)\.", pi)
    if not mpub:
        mpub = re.search(r"publication number ([A-Z]{2}-[0-9A-Z-]+)\.", pi)
    citing_pub = mpub.group(1) if mpub else None
    citing_assignee = None
    m = re.search(r"owned by (.+?) and has pub\.", pi)
    if not m:
        m = re.search(r"assigned to (.+?) and has pub\.", pi)
    if m:
        citing_assignee = m.group(1).strip()
    else:
        m2 = re.match(r"(.+?) holds the ", pi)
        if m2:
            citing_assignee = m2.group(1).strip()
    if not citing_pub or not citing_assignee:
        continue

    if citing_assignee.strip().upper()=='UNIV CALIFORNIA':
        continue

    cit_txt = r.get('citation')
    if not cit_txt:
        continue
    try:
        cits = json.loads(cit_txt)
    except Exception:
        continue
    for c in cits:
        cited_pub = c.get('publication_number')
        if cited_pub in uc_pubs:
            pairs.append({
                'citing_assignee': citing_assignee,
                'citing_pub': citing_pub,
                'cited_uc_pub': cited_pub,
                'primary_subclass': primary_subclass_by_pub.get(citing_pub)
            })

# Deduplicate assignee+subclass
df=pd.DataFrame(pairs)
if df.empty:
    out=[]
else:
    df=df.dropna(subset=['primary_subclass'])
    df=df.drop_duplicates(subset=['citing_assignee','primary_subclass'])
    out=df[['citing_assignee','primary_subclass']].to_dict('records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_JUbT2rer8cM4e6gsgt4yeI7l': ['publicationinfo'], 'var_call_zhwIUwCpxm87MRWlyhnMgw84': ['cpc_definition'], 'var_call_Ui9aZ5MDM6PWOUb3vReYMJ3h': [], 'var_call_iwBYDodjZ7zhKqOlKPaFtdPr': [], 'var_call_N3lOwpE8EqvWLZhvzUP3UdaN': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_call_v1sFxtXkdlNl4BqSXhS1KsPN': 'file_storage/call_v1sFxtXkdlNl4BqSXhS1KsPN.json'}

exec(code, env_args)

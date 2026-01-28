code = """import json, re

# Load UC assignee patents list
uc_path = var_call_tlkzTucRomT39NGxEPtHjU1D
with open(uc_path, 'r', encoding='utf-8') as f:
    uc_rows = json.load(f)

# UC pubs set
pub_re = re.compile(r"(?:pub\. number|publication number)\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)")

def get_pub(patents_info:str):
    if not patents_info:
        return None
    m = pub_re.search(patents_info)
    return m.group(1) if m else None

uc_pubs = {get_pub(r.get('Patents_info','')) for r in uc_rows}
uc_pubs.discard(None)

# Load citing candidates
cite_path = var_call_HB8Aj99xAYEazzcoYseMfwtU
with open(cite_path, 'r', encoding='utf-8') as f:
    cite_rows = json.load(f)

# Extract assignee from Patents_info
assignee_re = re.compile(r"^(.*?)\s+holds the ")
assignee_re2 = re.compile(r"is owned by\s+([^\.]+)\s+and has")
assignee_re3 = re.compile(r"is assigned to\s+([^\.]+)\s+and has")

def get_assignee(patents_info:str):
    if not patents_info:
        return None
    m = assignee_re.search(patents_info)
    if m:
        return m.group(1).strip()
    m = assignee_re2.search(patents_info)
    if m:
        return m.group(1).strip()
    m = assignee_re3.search(patents_info)
    if m:
        return m.group(1).strip()
    return None

# Parse citation list and check if any cited pub in uc_pubs
citing = []
for r in cite_rows:
    cit = r.get('citation')
    if not cit or cit == '[]':
        continue
    try:
        cit_list = json.loads(cit)
    except Exception:
        continue
    cited_pubs = {c.get('publication_number') for c in cit_list if isinstance(c, dict)}
    if cited_pubs & uc_pubs:
        assignee = get_assignee(r.get('Patents_info',''))
        if not assignee:
            continue
        if 'UNIV CALIFORNIA' in assignee:
            continue
        # primary CPC subclasses = cpc entries with first==true; take subclass as first 4 chars? actually CPC subclass is like A61K, etc.
        primary_subclasses = set()
        cpc_txt = r.get('cpc')
        if cpc_txt:
            try:
                cpc_list = json.loads(cpc_txt)
                for e in cpc_list:
                    if isinstance(e, dict) and e.get('first') is True:
                        code = (e.get('code') or '').strip()
                        if code:
                            primary_subclasses.add(code.split('/')[0])
            except Exception:
                pass
        for sub in primary_subclasses:
            citing.append({'citing_assignee': assignee, 'cpc_subclass': sub})

# deduplicate
seen=set()
uniq=[]
for x in citing:
    k=(x['citing_assignee'], x['cpc_subclass'])
    if k not in seen:
        seen.add(k)
        uniq.append(x)

print('__RESULT__:')
print(json.dumps(uniq, ensure_ascii=False))"""

env_args = {'var_call_tlkzTucRomT39NGxEPtHjU1D': 'file_storage/call_tlkzTucRomT39NGxEPtHjU1D.json', 'var_call_PhBDJPa11TP1ROqC42Qfqs5k': 'file_storage/call_PhBDJPa11TP1ROqC42Qfqs5k.json', 'var_call_zf5QnerCfz7Lpp9ZBlIFOYWg': {'uc_pub_count': 112}, 'var_call_HB8Aj99xAYEazzcoYseMfwtU': 'file_storage/call_HB8Aj99xAYEazzcoYseMfwtU.json'}

exec(code, env_args)

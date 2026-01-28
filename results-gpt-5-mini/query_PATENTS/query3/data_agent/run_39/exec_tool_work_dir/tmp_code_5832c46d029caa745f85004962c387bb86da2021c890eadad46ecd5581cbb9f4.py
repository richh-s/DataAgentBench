code = """import json, re
p = var_call_CZD6HGEWIebNGzCkkBQs0BHE
with open(p, 'r', encoding='utf-8') as f:
    citing = json.load(f)

# Function to extract assignee from Patents_info
def extract_assignee(info):
    # look for 'is held by X' or 'is assigned to X' or 'is owned by X' or 'held by X' or 'assigned to X' or 'owned by X' or 'is held by X and has'
    patterns = [r"held by ([A-Z0-9 &.,'-]+)", r"assigned to ([A-Z0-9 &.,'-]+)", r"owned by ([A-Z0-9 &.,'-]+)", r"is held by ([A-Z0-9 &.,'-]+)", r"is assigned to ([A-Z0-9 &.,'-]+)", r"is owned by ([A-Z0-9 &.,'-]+)"]
    for pat in patterns:
        m = re.search(pat, info, re.IGNORECASE)
        if m:
            name = m.group(1).strip()
            # Normalize spacing
            name = re.sub(r"\s+"," ", name)
            return name.upper()
    # fallback: look for 'by ' before ' and has' etc
    m = re.search(r"by ([A-Z0-9 &.,'-]+) and has", info, re.IGNORECASE)
    if m:
        return m.group(1).strip().upper()
    return None

assignee_to_codes = {}
for rec in citing:
    info = rec.get('Patents_info','')
    assignee = extract_assignee(info)
    if not assignee:
        continue
    if 'UNIV CALIFORNIA' in assignee:
        # exclude UC
        continue
    # parse cpc field which is JSON-like
    cpc_text = rec.get('cpc','[]')
    try:
        cpc_list = json.loads(cpc_text)
    except Exception:
        # try to fix single quotes
        try:
            cpc_list = json.loads(cpc_text.replace("'","\""))
        except Exception:
            cpc_list = []
    primary_codes = set()
    for c in cpc_list:
        if isinstance(c, dict) and c.get('first'):
            code = c.get('code')
            if code:
                primary_codes.add(code)
    if not primary_codes:
        # if none marked first, pick first code if exists
        for c in cpc_list:
            if isinstance(c, dict) and c.get('code'):
                primary_codes.add(c.get('code'))
                break
    if assignee not in assignee_to_codes:
        assignee_to_codes[assignee] = set()
    assignee_to_codes[assignee].update(primary_codes)

# Convert sets to sorted lists
result = {k: sorted(list(v)) for k,v in assignee_to_codes.items()}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_uDiYoolU3jAQpH2wMff8iPIt': ['publicationinfo'], 'var_call_GlGC2BtHSHcOnyHn5dstNfTH': ['cpc_definition'], 'var_call_teNtoCHZkRPcqi3NXSIAqDMd': 'file_storage/call_teNtoCHZkRPcqi3NXSIAqDMd.json', 'var_call_SkSJcXss6ufl2IEdIhp2GI8L': ['AU-2003297741-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2019275518-B2', 'AU-6535890-A', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CN-100339724-C', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-4284234-A1', 'HK-1250569-A1', 'ID-23426-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-20200041324-A', 'MX-2013002850-A', 'RO-70061-A', 'TW-201925402-A', 'US-11376346-B2', 'US-11546022-B2', 'US-11667770-B2', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2017145219-A1', 'US-2017281687-A1', 'US-2018243924-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2021000566-A1', 'US-2021101879-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023321419-A1', 'US-5304932-A', 'US-5547866-A', 'US-6750960-B2', 'US-6767662-B2', 'US-9061071-B2', 'WO-2010045542-A3', 'WO-2012162563-A2', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2020055916-A9', 'WO-2021102420-A1', 'WO-2023225482-A3', 'WO-2024044766-A3', 'WO-2024112568-A1'], 'var_call_CZD6HGEWIebNGzCkkBQs0BHE': 'file_storage/call_CZD6HGEWIebNGzCkkBQs0BHE.json'}

exec(code, env_args)

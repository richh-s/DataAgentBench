code = """import json, re
# Access prior tool results
# var_call_svEulIQKVK6K6f3fGoh27X1G may be a list or string
uc_var = var_call_svEulIQKVK6K6f3fGoh27X1G
if isinstance(uc_var, str):
    try:
        uc_pubs = json.loads(uc_var)
    except Exception:
        # try to extract list-like entries
        uc_pubs = re.findall(r'[A-Z]{2}-[0-9A-Z\-\.]+', uc_var)
elif isinstance(uc_var, list):
    uc_pubs = uc_var
else:
    uc_pubs = list(uc_var)
uc_set = set([p.rstrip('.') for p in uc_pubs])

# Load records from previous query_db result file
path = var_call_LeeDY9luM4dtmX5DlGm6Fdap
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

assignee_to_codes = {}
for rec in records:
    cit_field = rec.get('citation')
    citations = []
    if isinstance(cit_field, list):
        citations = cit_field
    elif isinstance(cit_field, str):
        try:
            citations = json.loads(cit_field)
        except Exception:
            # extract publication numbers with regex
            for m in re.findall(r'([A-Z]{2,3}-[0-9A-Z\-\.]+|US-[0-9]+-[A-Z0-9]+|US-[0-9]+)', cit_field):
                citations.append({'publication_number': m})
    else:
        citations = []
    cited_pub_nums = set()
    for c in citations:
        if isinstance(c, dict):
            pn = c.get('publication_number','')
            if pn:
                cited_pub_nums.add(pn.rstrip('.'))
        elif isinstance(c, str):
            cited_pub_nums.add(c.rstrip('.'))
    if uc_set & cited_pub_nums:
        info = rec.get('Patents_info','')
        # extract assignee
        assignee = None
        m = re.match(r'^(.*?)\s+(?:holds the|holds|is assigned to|is owned by|owned by|assigned to|has)\b', info, flags=re.IGNORECASE)
        if m:
            assignee = m.group(1).strip()
        else:
            m = re.match(r'^(.*?)(?:,|\s+-|\s+\()', info)
            if m:
                assignee = m.group(1).strip()
        if not assignee:
            assignee = info.split(',')[0].strip()
        if assignee.upper().find('UNIV CALIFORNIA') != -1:
            continue
        # parse cpc
        cpc_field = rec.get('cpc','[]')
        try:
            cpcs = json.loads(cpc_field) if isinstance(cpc_field, str) else cpc_field
        except Exception:
            cpcs = []
        primary_codes = set()
        if isinstance(cpcs, list):
            for entry in cpcs:
                if isinstance(entry, dict):
                    code = entry.get('code')
                    first = entry.get('first', False)
                    if first and code:
                        primary_codes.add(code)
            if not primary_codes:
                for entry in cpcs:
                    if isinstance(entry, dict):
                        code = entry.get('code')
                        if code:
                            primary_codes.add(code)
                            break
        if not primary_codes:
            continue
        assignee_to_codes.setdefault(assignee, set()).update(primary_codes)

out_map = {k: sorted(list(v)) for k,v in assignee_to_codes.items()}
unique_codes = sorted({code for codes in out_map.values() for code in codes})
result = {'assignee_to_codes': out_map, 'unique_codes': unique_codes}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_7xqyIJkzAWq6WVNwai0HPBQs': 'file_storage/call_7xqyIJkzAWq6WVNwai0HPBQs.json', 'var_call_svEulIQKVK6K6f3fGoh27X1G': ['AU-2003247814-A1.', 'AU-2003297741-A1.', 'AU-2004253879-A1.', 'AU-2005269556-A1.', 'AU-2007297661-A1.', 'AU-2008349842-A1.', 'AU-2010214112-B2.', 'AU-2015364602-B2.', 'AU-2017356943-A1.', 'AU-2019275518-B2.', 'AU-2409401-A.', 'AU-2898989-A.', 'AU-3353000-A.', 'AU-5938296-A.', 'AU-6535890-A.', 'CA-2283629-C.', 'CA-2298540-A1.', 'CA-2550552-A1.', 'CA-2562038-C.', 'CA-2718348-C.', 'CA-3161617-A1.', 'CN-100339724-C.', 'CN-101584047-A.', 'CN-102067370-B.', 'CN-102584712-A.', 'CN-103189548-A.', 'CN-103687626-A.', 'EP-0826155-A4.', 'EP-1212462-A1.', 'EP-2210307-A4.', 'EP-3668487-A4.', 'EP-4284234-A1.', 'HK-1052178-A1.', 'HK-1250569-A1.', 'HR-P20201231-T1.', 'ID-23426-A.', 'IL-244029-A0.', 'IL-274176-A.', 'JP-2005104983-A.', 'JP-2009260386-A.', 'JP-2014224156-A.', 'JP-S6163700-A.', 'KR-20050085437-A.', 'KR-20110004413-A.', 'KR-20160119166-A.', 'KR-20200041324-A.', 'MX-2013002850-A.', 'PE-20130764-A1.', 'PT-2970346-T.', 'RO-70061-A.', 'TW-201925402-A.', 'US-10359432-B2.', 'US-10744347-B2.', 'US-11014955-B2.', 'US-11072681-B2.', 'US-11376346-B2.', 'US-11421276-B2.', 'US-11546022-B2.', 'US-11667770-B2.', 'US-12025581-B2.', 'US-2003112494-A1.', 'US-2004115131-A1.', 'US-2005234013-A1.', 'US-2006051790-A1.', 'US-2006292670-A1.', 'US-2009031436-A1.', 'US-2010025717-A1.', 'US-2017087258-A1.', 'US-2017145219-A1.', 'US-2017281687-A1.', 'US-2018243924-A1.', 'US-2019169580-A1.', 'US-2019209590-A1.', 'US-2019328740-A1.', 'US-2020025859-A1.', 'US-2020283856-A1.', 'US-2021000566-A1.', 'US-2021002329-A1.', 'US-2021039104-A1.', 'US-2021101879-A1.', 'US-2021181673-A1.', 'US-2021282642-A1.', 'US-2022018060-A1.', 'US-2022074631-A1.', 'US-2023155090-A1.', 'US-2023171142-A1.', 'US-2023279470-A1.', 'US-2023321419-A1.', 'US-5304932-A.', 'US-5547866-A.', 'US-6237292-B1.', 'US-6750960-B2.', 'US-6767662-B2.', 'US-6980295-B2.', 'US-7052856-B2.', 'US-7745569-B2.', 'US-9061071-B2.', 'WO-2010045542-A3.', 'WO-2012158833-A3.', 'WO-2012162563-A2.', 'WO-2014152660-A1.', 'WO-2017136335-A1.', 'WO-2017214343-A1.', 'WO-2018026404-A3.', 'WO-2018067976-A1.', 'WO-2019067860-A1.', 'WO-2019173834-A1.', 'WO-2020055916-A9.', 'WO-2021102420-A1.', 'WO-2023212447-A2.', 'WO-2023225482-A3.', 'WO-2023239670-A1.', 'WO-2024044766-A3.', 'WO-2024112568-A1.'], 'var_call_LeeDY9luM4dtmX5DlGm6Fdap': 'file_storage/call_LeeDY9luM4dtmX5DlGm6Fdap.json'}

exec(code, env_args)

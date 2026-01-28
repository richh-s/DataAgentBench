code = """import json, re
# Load the dataset of all publicationinfo records with non-empty citations
path = var_call_UB9bFP5TxaTdIWaj7LPnWjic
with open(path, 'r', encoding='utf-8') as f:
    all_recs = json.load(f)
# Load list of Univ California publication numbers from previous step
univ_pubs = var_call_XSuDjjk7sA0GwVAEhb6Frnaq
univ_set = set(univ_pubs)

def parse_citation_list(citation_field):
    if not citation_field:
        return []
    try:
        cites = json.loads(citation_field)
        if isinstance(cites, list):
            return cites
    except Exception:
        pass
    # fallback: try to find publication_number strings via regex
    pubs = re.findall(r"[A-Z]{2}-[A-Za-z0-9\-]+", citation_field)
    res = []
    for p in pubs:
        res.append({'publication_number': p})
    return res

# regex to extract assignee from Patents_info
assignee_re = re.compile(r"^(?P<assignee>[^,\n]+?)\s+(holds|is owned by|is assigned to|assigned to|owns|has the)\b", re.IGNORECASE)
results = []
for rec in all_recs:
    pat_info = rec.get('Patents_info','')
    citations = parse_citation_list(rec.get('citation',''))
    cited_pub_nums = set()
    for c in citations:
        pn = c.get('publication_number') if isinstance(c, dict) else None
        if pn:
            cited_pub_nums.add(pn)
    # check intersection
    if univ_set & cited_pub_nums:
        # extract assignee
        m = assignee_re.search(pat_info)
        if m:
            assignee = m.group('assignee').strip()
        else:
            # fallback: take leading token before 'the' or before 'holds the'
            assignee = pat_info.split(' the ')[0].split(' holds ')[0].split(',')[0].strip()
        # exclude Univ California
        if 'UNIV CALIFORNIA' in assignee.upper():
            continue
        # parse cpc field
        cpc_field = rec.get('cpc','')
        primary_code = None
        try:
            cpcs = json.loads(cpc_field)
            if isinstance(cpcs, list):
                for item in cpcs:
                    if isinstance(item, dict) and item.get('first'):
                        primary_code = item.get('code')
                        break
                if not primary_code and len(cpcs)>0:
                    # take first code available
                    first_item = cpcs[0]
                    primary_code = first_item.get('code') if isinstance(first_item, dict) else None
        except Exception:
            # try regex
            m2 = re.search(r"\b([A-Z]{1,4}[0-9A-Z\-/]+)\b", cpc_field)
            primary_code = m2.group(1) if m2 else None
        results.append({'assignee': assignee, 'primary_cpc': primary_code})

# Deduplicate assignee-primary pairs and aggregate titles per assignee
agg = {}
for r in results:
    ass = r['assignee']
    code = r['primary_cpc']
    if not ass:
        continue
    if ass not in agg:
        agg[ass] = set()
    if code:
        agg[ass].add(code)

# prepare list of unique CPC codes to query
unique_codes = sorted({c for codes in agg.values() for c in codes if c})
output = {'assignee_to_codes': {k: sorted(list(v)) for k,v in agg.items()}, 'unique_codes': unique_codes}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_FYCiQmyJquHDaA3DiPfaYK5x': ['publicationinfo'], 'var_call_mDH52FTLVbIZBVfcBIDocEGU': ['cpc_definition'], 'var_call_ESyf4rKVi5PNp0DQESeG9x1t': 'file_storage/call_ESyf4rKVi5PNp0DQESeG9x1t.json', 'var_call_XSuDjjk7sA0GwVAEhb6Frnaq': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5938296-A', 'AU-6535890-A', 'CA-2283629-C', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CA-2718348-C', 'CA-3161617-A1', 'CN-100339724-C', 'CN-101584047-A', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'CN-103687626-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-2210307-A4', 'EP-3668487-A4', 'EP-4284234-A1', 'HK-1052178-A1', 'HK-1250569-A1', 'HR-P20201231-T1', 'ID-23426-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2005104983-A', 'JP-2009260386-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-20050085437-A', 'KR-20110004413-A', 'KR-20160119166-A', 'KR-20200041324-A', 'MX-2013002850-A', 'PE-20130764-A1', 'PT-2970346-T', 'RO-70061-A', 'TW-201925402-A', 'US-10359432-B2', 'US-10744347-B2', 'US-11014955-B2', 'US-11072681-B2', 'US-11376346-B2', 'US-11421276-B2', 'US-11546022-B2', 'US-11667770-B2', 'US-12025581-B2', 'US-2003112494-A1', 'US-2004115131-A1', 'US-2005234013-A1', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2009031436-A1', 'US-2010025717-A1', 'US-2017087258-A1', 'US-2017145219-A1', 'US-2017281687-A1', 'US-2018243924-A1', 'US-2019169580-A1', 'US-2019209590-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2020283856-A1', 'US-2021000566-A1', 'US-2021002329-A1', 'US-2021039104-A1', 'US-2021101879-A1', 'US-2021181673-A1', 'US-2021282642-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023321419-A1', 'US-5304932-A', 'US-5547866-A', 'US-6237292-B1', 'US-6750960-B2', 'US-6767662-B2', 'US-6980295-B2', 'US-7052856-B2', 'US-7745569-B2', 'US-9061071-B2', 'WO-2010045542-A3', 'WO-2012158833-A3', 'WO-2012162563-A2', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2018067976-A1', 'WO-2019067860-A1', 'WO-2019173834-A1', 'WO-2020055916-A9', 'WO-2021102420-A1', 'WO-2023212447-A2', 'WO-2023225482-A3', 'WO-2023239670-A1', 'WO-2024044766-A3', 'WO-2024112568-A1'], 'var_call_UB9bFP5TxaTdIWaj7LPnWjic': 'file_storage/call_UB9bFP5TxaTdIWaj7LPnWjic.json'}

exec(code, env_args)

code = """import json, re
# Load UNIV CALIFORNIA records
path_univ = var_call_npUMUKEmpDiHTFu2GVHD1Vg3
with open(path_univ, 'r', encoding='utf-8') as f:
    univ_recs = json.load(f)
# Extract publication numbers from Patents_info
pub_pattern = re.compile(r'(?i)(?:publication number|publication no\.|pub\. number|pub no\.|pub number)\s*([A-Z0-9\-]+)')
alt_pattern = re.compile(r'\b([A-Z]{2}-?\d{1,}[A-Z0-9\-]*)\b')
univ_pubs = set()
for rec in univ_recs:
    txt = rec.get('Patents_info','')
    m = pub_pattern.search(txt)
    if m:
        univ_pubs.add(m.group(1).strip())
    else:
        # fallback: try to find token like US-..., TW-..., etc that looks like pub number
        m2 = re.search(r'([A-Z]{2,3}-\d{4,}[A-Z0-9\-]*)', txt)
        if m2:
            univ_pubs.add(m2.group(1))
# Load records with citations
path_cit = var_call_6Av1Grp4xzYa8eWYFcUt3HSW
with open(path_cit, 'r', encoding='utf-8') as f:
    cit_recs = json.load(f)

# Helper to extract assignee name from Patents_info
assignee_patterns = [re.compile(r'^(.*?)\s+(?:holds|has|owns|is owner|is owned by|is assigned to|assigned to|is the owner of|is owned by)\b', re.IGNORECASE),
                     re.compile(r'^(.*?)\s+owns the', re.IGNORECASE),
                     re.compile(r'^(.*?)\s+is the owner', re.IGNORECASE)]

assignee_to_codes = {}
all_codes = set()

for rec in cit_recs:
    citations_str = rec.get('citation','')
    if not citations_str or citations_str.strip() == '[]':
        continue
    try:
        citations = json.loads(citations_str)
    except Exception:
        # try to fix single quotes
        try:
            citations = json.loads(citations_str.replace("'", '"'))
        except Exception:
            continue
    cited_pubs = set()
    for c in citations:
        pn = c.get('publication_number','')
        if pn:
            cited_pubs.add(pn)
    if not (cited_pubs & univ_pubs):
        continue
    # extract assignee
    info = rec.get('Patents_info','')
    assignee = None
    # Try simple pattern: starts with name then 'holds' e.g., 'PANASONIC IP MAN CO LTD holds the US patent...'
    for patt in assignee_patterns:
        m = patt.search(info)
        if m:
            assignee = m.group(1).strip()
            break
    if not assignee:
        # try pattern 'In US, the application (number ...) is owned by XYZ and has pub. number ...'
        m2 = re.search(r'owned by\s+([^.,;]+)', info, re.IGNORECASE)
        if m2:
            assignee = m2.group(1).strip()
        else:
            m3 = re.search(r'assigned to\s+([^.,;]+)', info, re.IGNORECASE)
            if m3:
                assignee = m3.group(1).strip()
    if not assignee:
        # fallback: take leading token before 'the US patent' or before parentheses
        m4 = re.match(r'([^,\(]+)', info)
        if m4:
            assignee = m4.group(1).strip()
    if not assignee:
        continue
    # Normalize whitespace
    assignee = re.sub(r'\s+', ' ', assignee)
    if 'UNIV CALIFORNIA' in assignee.upper():
        continue
    # parse cpc
    cpc_str = rec.get('cpc','')
    primary_code = None
    if cpc_str and cpc_str.strip()!='[]':
        try:
            cpcs = json.loads(cpc_str)
        except Exception:
            try:
                cpcs = json.loads(cpc_str.replace("'", '"'))
            except Exception:
                cpcs = []
        if isinstance(cpcs, list) and cpcs:
            for entry in cpcs:
                if entry.get('first', False):
                    primary_code = entry.get('code')
                    break
            if not primary_code and cpcs:
                primary_code = cpcs[0].get('code')
    if not primary_code:
        continue
    all_codes.add(primary_code)
    assignee_to_codes.setdefault(assignee, set()).add(primary_code)

# Prepare results
results = []
for assignee, codes in assignee_to_codes.items():
    results.append({'assignee': assignee, 'primary_cpc_codes': sorted(list(codes))})

output = {'results': results, 'codes': sorted(list(all_codes))}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_npUMUKEmpDiHTFu2GVHD1Vg3': 'file_storage/call_npUMUKEmpDiHTFu2GVHD1Vg3.json', 'var_call_pWBhAIeSoXnilhUK0CMQin03': ['AP-3334-A', 'AU-2001257114-A1', 'AU-2001296493-B2', 'AU-2002254753-B2', 'AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008329628-B2', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5366398-A', 'AU-5938296-A', 'AU-6535890-A', 'AU-7724398-A', 'BR-112021021092-A8', 'BR-9610580-A', 'CA-2220674-A1', 'CA-2278751-A1', 'CA-2283629-C', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CA-2718348-C', 'CA-3027364-A1', 'CA-3055214-A1', 'CA-3161617-A1', 'CA-3225295-A1', 'CN-100339724-C', 'CN-101584047-A', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'CN-103237558-A', 'CN-103687626-A', 'CN-1120376-C', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-1224461-B1', 'EP-2029921-A4', 'EP-2210307-A4', 'EP-3668487-A4', 'EP-3866867-A1', 'EP-4284234-A1', 'FR-2194760-A1', 'HK-1052178-A1', 'HK-1250569-A1', 'HR-P20201231-T1', 'ID-23426-A', 'IL-140140-A0', 'IL-236725-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2005104983-A', 'JP-2009260386-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-100228821-B1', 'KR-20050085437-A', 'KR-20080078049-A', 'KR-20110004413-A', 'KR-20160119166-A', 'KR-20180041236-A', 'KR-20200041324-A', 'KR-20200084864-A', 'MX-2013002850-A', 'PE-20130764-A1', 'PT-2970346-T', 'RO-70061-A', 'TW-201925402-A', 'US-10337029-B2', 'US-10359432-B2', 'US-10744347-B2', 'US-10765865-B2', 'US-10900049-B2', 'US-11014955-B2', 'US-11072681-B2', 'US-11248107-B2', 'US-11376346-B2', 'US-11421276-B2', 'US-11445941-B2', 'US-11546022-B2', 'US-11607427-B2', 'US-11667770-B2', 'US-11960018-B2', 'US-12025581-B2', 'US-2003112494-A1', 'US-2004115131-A1', 'US-2005136639-A1', 'US-2005234013-A1', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2008047008-A1', 'US-2009031436-A1', 'US-2010025717-A1', 'US-2017050153-A1', 'US-2017087258-A1', 'US-2017145219-A1', 'US-2017194630-A1', 'US-2017281687-A1', 'US-2017294981-A1', 'US-2017369950-A1', 'US-2018080022-A1', 'US-2018243924-A1', 'US-2018277766-A1', 'US-2018304537-A1', 'US-2018348310-A1', 'US-2019169580-A1', 'US-2019209590-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2020283856-A1', 'US-2021000566-A1', 'US-2021002329-A1', 'US-2021039104-A1', 'US-2021101879-A1', 'US-2021181673-A1', 'US-2021282642-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2022123166-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023314781-A1', 'US-2023321419-A1', 'US-2023340506-A1', 'US-3666017-A', 'US-3842373-A', 'US-5304932-A', 'US-5547866-A', 'US-6030830-A', 'US-6237292-B1', 'US-6750960-B2', 'US-6767662-B2', 'US-6980295-B2', 'US-7052856-B2', 'US-7745569-B2', 'US-8361933-B2', 'US-9061071-B2', 'WO-2010045542-A3', 'WO-2012158833-A3', 'WO-2012162563-A2', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2018067976-A1', 'WO-2018152537-A1', 'WO-2019067860-A1', 'WO-2019173834-A1', 'WO-2020055916-A9', 'WO-2020096950-A1', 'WO-2021102420-A1', 'WO-2022178138-A1', 'WO-2023212447-A2', 'WO-2023225482-A3', 'WO-2023239670-A1', 'WO-2024044766-A3', 'WO-2024050335-A2', 'WO-2024112568-A1', 'ZA-200802422-B'], 'var_call_6Av1Grp4xzYa8eWYFcUt3HSW': 'file_storage/call_6Av1Grp4xzYa8eWYFcUt3HSW.json'}

exec(code, env_args)

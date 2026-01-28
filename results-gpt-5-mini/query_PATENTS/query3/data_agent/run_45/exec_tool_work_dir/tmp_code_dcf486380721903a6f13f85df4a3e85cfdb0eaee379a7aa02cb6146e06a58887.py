code = """import json, re
# var_call_WVUazWTKoO20o6fVaBR6HxPl is a list of UC publication numbers
uc_pubnums = var_call_WVUazWTKoO20o6fVaBR6HxPl
# var_call_FesAuiZx9IunCu8G0xi71ezk is a file path to all publicationinfo records
with open(var_call_FesAuiZx9IunCu8G0xi71ezk, 'r') as f:
    all_recs = json.load(f)

uc_set = set([p.strip() for p in uc_pubnums if p])

# helper to parse citation field
def extract_cited_pubnums(citation_field):
    if not citation_field:
        return []
    try:
        cit = json.loads(citation_field)
        res = []
        for c in cit:
            pn = c.get('publication_number')
            if pn:
                res.append(pn.strip())
        return res
    except Exception:
        return re.findall(r"[A-Z]{2}-[0-9][0-9A-Za-z-]+", citation_field)

# helper to extract assignee from Patents_info
def extract_assignee(pi):
    if not pi:
        return None
    patterns = [
        r"^([A-Z0-9 &\.\-]{3,}?)\s+holds the",
        r"([A-Z0-9 &\.\-]{3,}?)\s+holds the",
        r"is assigned to\s+([A-Z0-9 &\.\-]{3,}?)\b",
        r"is owned by\s+([A-Z0-9 &\.\-]{3,}?)\b",
        r"owned by\s+([A-Z0-9 &\.\-]{3,}?)\b",
        r"assigned to\s+([A-Z0-9 &\.\-]{3,}?)\b",
        r"held by\s+([A-Z0-9 &\.\-]{3,}?)\b",
        r"^([A-Z0-9 &\.\-]{3,}?)\s+holds",
    ]
    for pat in patterns:
        m = re.search(pat, pi, re.IGNORECASE)
        if m:
            ass = m.group(1).strip()
            ass = re.sub(r"[\.,;]$", "", ass)
            return ass.upper()
    m = re.search(r"by\s+([A-Z0-9 &\.\-]{3,}?)\b", pi, re.IGNORECASE)
    if m:
        return m.group(1).strip().upper()
    return None

results = []
for rec in all_recs:
    cited = extract_cited_pubnums(rec.get('citation',''))
    if any(p in uc_set for p in cited):
        ass = extract_assignee(rec.get('Patents_info',''))
        if not ass:
            ass = "UNKNOWN"
        if 'UNIV' in ass and 'CALIFORNIA' in ass:
            continue
        # primary CPC
        primary_code = None
        cpc_field = rec.get('cpc','')
        try:
            cpcs = json.loads(cpc_field)
            for entry in cpcs:
                if entry.get('first'):
                    primary_code = entry.get('code')
                    break
            if not primary_code and len(cpcs)>0:
                primary_code = cpcs[0].get('code')
        except Exception:
            codes = re.findall(r"[A-Z]\w{1,2}[0-9][A-Z0-9/]+", cpc_field)
            primary_code = codes[0] if codes else None
        results.append({'rowid': rec.get('rowid'), 'assignee': ass, 'primary_cpc': primary_code})

# deduplicate by assignee+primary_cpc
seen = set()
unique = []
for r in results:
    key = (r['assignee'], r['primary_cpc'])
    if key in seen:
        continue
    seen.add(key)
    unique.append(r)

cpc_codes = sorted(list({r['primary_cpc'] for r in unique if r['primary_cpc']}))
# prepare output
output = {'num_unique_pairs': len(unique), 'pairs': unique, 'cpc_codes': cpc_codes}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_X55MlaZFDaGy31kjzwvu18Qb': ['publicationinfo'], 'var_call_RrwZKYjAfJZtUGwMqt28W4mJ': ['cpc_definition'], 'var_call_1HEfWTTyAxtdte7bpVXwNGAy': 'file_storage/call_1HEfWTTyAxtdte7bpVXwNGAy.json', 'var_call_ZmqIMvdppX0BFeOSlj81vzwf': 'file_storage/call_ZmqIMvdppX0BFeOSlj81vzwf.json', 'var_call_WVUazWTKoO20o6fVaBR6HxPl': ['AP-3334-A', 'AU-2001257114-A1', 'AU-2001296493-B2', 'AU-2002254753-B2', 'AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008329628-B2', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5366398-A', 'AU-5938296-A', 'AU-6535890-A', 'AU-7724398-A', 'BR-112021021092-A8', 'BR-9610580-A', 'CA-2220674-A1', 'CA-2278751-A1', 'CA-2283629-C', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CA-2718348-C', 'CA-3027364-A1', 'CA-3055214-A1', 'CA-3161617-A1', 'CA-3225295-A1', 'CN-100339724-C', 'CN-101584047-A', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'CN-103237558-A', 'CN-103687626-A', 'CN-1120376-C', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-1224461-B1', 'EP-2029921-A4', 'EP-2210307-A4', 'EP-3668487-A4', 'EP-3866867-A1', 'EP-4284234-A1', 'FR-2194760-A1', 'HK-1052178-A1', 'HK-1250569-A1', 'ID-23426-A', 'IL-140140-A0', 'IL-236725-A', 'IL-244029-A0', 'IL-274176-A', 'JP-13313985-A', 'JP-2005104983-A', 'JP-2009260386-A', 'JP-2014224156-A', 'KR-100228821-B1', 'KR-20050085437-A', 'KR-20080078049-A', 'KR-20110004413-A', 'KR-20160119166-A', 'KR-20180041236-A', 'KR-20200041324-A', 'KR-20200084864-A', 'MX-2013002850-A', 'PE-20130764-A1', 'PT-2970346-T', 'RO-70061-A', 'TW-201925402-A', 'US-10337029-B2', 'US-10359432-B2', 'US-10744347-B2', 'US-10765865-B2', 'US-10900049-B2', 'US-11014955-B2', 'US-11072681-B2', 'US-11248107-B2', 'US-11376346-B2', 'US-11421276-B2', 'US-11445941-B2', 'US-11546022-B2', 'US-11607427-B2', 'US-11667770-B2', 'US-11960018-B2', 'US-12025581-B2', 'US-2003112494-A1', 'US-2004115131-A1', 'US-2005136639-A1', 'US-2005234013-A1', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2008047008-A1', 'US-2009031436-A1', 'US-2010025717-A1', 'US-2017050153-A1', 'US-2017087258-A1', 'US-2017145219-A1', 'US-2017194630-A1', 'US-2017281687-A1', 'US-2017294981-A1', 'US-2017369950-A1', 'US-2018080022-A1', 'US-2018243924-A1', 'US-2018277766-A1', 'US-2018304537-A1', 'US-2018348310-A1', 'US-2019169580-A1', 'US-2019209590-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2020283856-A1', 'US-2021000566-A1', 'US-2021002329-A1', 'US-2021039104-A1', 'US-2021101879-A1', 'US-2021181673-A1', 'US-2021282642-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2022123166-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023314781-A1', 'US-2023321419-A1', 'US-2023340506-A1', 'US-3666017-A', 'US-3842373-A', 'US-5304932-A', 'US-5547866-A', 'US-6030830-A', 'US-6237292-B1', 'US-6750960-B2', 'US-6767662-B2', 'US-6980295-B2', 'US-7052856-B2', 'US-7745569-B2', 'US-8361933-B2', 'US-9061071-B2', 'WO-2010045542-A3', 'WO-2012158833-A3', 'WO-2012162563-A2', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2018067976-A1', 'WO-2018152537-A1', 'WO-2019067860-A1', 'WO-2019173834-A1', 'WO-2020055916-A9', 'WO-2020096950-A1', 'WO-2021102420-A1', 'WO-2022178138-A1', 'WO-2023212447-A2', 'WO-2023225482-A3', 'WO-2023239670-A1', 'WO-2024044766-A3', 'WO-2024050335-A2', 'WO-2024112568-A1', 'ZA-200802422-B'], 'var_call_FesAuiZx9IunCu8G0xi71ezk': 'file_storage/call_FesAuiZx9IunCu8G0xi71ezk.json'}

exec(code, env_args)

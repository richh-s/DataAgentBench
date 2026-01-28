code = """import json
# load the large query result file
path = var_call_fgSdFd0nlzrQTl13vaBBtYLD
with open(path,'r') as f:
    recs = json.load(f)
# Extract distinct Patents_info beginnings (assignees) and whether their citation lists include any UNIV CALIFORNIA pub numbers
# We'll search citation JSON strings for UNIV CA publication numbers that we previously extracted (var_call_9d8lYiSLsGbc6ekXKj5tAhZ5)
pubs_univ = json.loads(open(var_call_9d8lYiSLsGbc6ekXKj5tAhZ5,'r').read()) if isinstance(var_call_9d8lYiSLsGbc6ekXKj5tAhZ5, str) else []
# However, var_call_9d8l... is a storage key containing JSON string result; we have its content in variable var_call_9d8lYiSLsGbc6ekXKj5tAhZ5 in the execution environment; but in this function we can't access it directly. Instead, rederive some known UNIV pub numbers from recs by scanning for 'UNIV CALIFORNIA' in Patents_info and collect their publication numbers.
univ_pubs = set()
for r in recs:
    info = r.get('Patents_info','')
    if 'UNIV CALIFORNIA' in info.upper():
        found = __import__('re').findall(r"\b[A-Z]{2}-[0-9A-Za-z-]+\b", info)
        for p in found:
            univ_pubs.add(p)
# Now scan all recs to find which Patents_info (assignee) cite any of these univ_pubs
assignees_citing = {}
import re
for r in recs:
    cit = r.get('citation','')
    if not cit:
        continue
    try:
        cites = json.loads(cit)
    except Exception:
        try:
            cites = json.loads(cit.replace("'", '"'))
        except Exception:
            cites = []
    cited_pubs = [c.get('publication_number') for c in cites if isinstance(c, dict) and c.get('publication_number')]
    if not cited_pubs:
        continue
    if any(p in univ_pubs for p in cited_pubs):
        info = r.get('Patents_info','')
        # naive assignee: first token before comma
        ass = info.split(',')[0]
        if 'UNIV' in ass.upper() and 'CALIFORNIA' in ass.upper():
            continue
        assignees_citing.setdefault(ass.strip(), set()).update([p for p in cited_pubs if p in univ_pubs])

# return a small sample
out = {'univ_pubs': sorted(list(univ_pubs))[:50], 'assignees_citing_count': len(assignees_citing), 'assignees_sample': list(assignees_citing.items())[:20]}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_GHHlpoJLIGHealc6HCfay9RQ': ['publicationinfo'], 'var_call_3LJBg0Bx7wVqc6J2Bvzo7KKF': ['cpc_definition'], 'var_call_o3PfwbtrF1Uq9E4KQ2atPaw9': 'file_storage/call_o3PfwbtrF1Uq9E4KQ2atPaw9.json', 'var_call_9d8lYiSLsGbc6ekXKj5tAhZ5': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5938296-A', 'AU-6535890-A', 'CA-2283629-C', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CA-2718348-C', 'CA-3161617-A1', 'CN-100339724-C', 'CN-101584047-A', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'CN-103687626-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-2210307-A4', 'EP-3668487-A4', 'EP-4284234-A1', 'HK-1052178-A1', 'HK-1250569-A1', 'HR-P20201231-T1', 'ID-23426-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2005104983-A', 'JP-2009260386-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-20050085437-A', 'KR-20110004413-A', 'KR-20160119166-A', 'KR-20200041324-A', 'MX-2013002850-A', 'PE-20130764-A1', 'PT-2970346-T', 'RO-70061-A', 'TW-201925402-A', 'US-10359432-B2', 'US-10744347-B2', 'US-11014955-B2', 'US-11072681-B2', 'US-11376346-B2', 'US-11421276-B2', 'US-11546022-B2', 'US-11667770-B2', 'US-12025581-B2', 'US-2003112494-A1', 'US-2004115131-A1', 'US-2005234013-A1', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2009031436-A1', 'US-2010025717-A1', 'US-2017087258-A1', 'US-2017145219-A1', 'US-2017281687-A1', 'US-2018243924-A1', 'US-2019169580-A1', 'US-2019209590-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2020283856-A1', 'US-2021000566-A1', 'US-2021002329-A1', 'US-2021039104-A1', 'US-2021101879-A1', 'US-2021181673-A1', 'US-2021282642-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023321419-A1', 'US-5304932-A', 'US-5547866-A', 'US-6237292-B1', 'US-6750960-B2', 'US-6767662-B2', 'US-6980295-B2', 'US-7052856-B2', 'US-7745569-B2', 'US-9061071-B2', 'WO-2010045542-A3', 'WO-2012158833-A3', 'WO-2012162563-A2', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2018067976-A1', 'WO-2019067860-A1', 'WO-2019173834-A1', 'WO-2020055916-A9', 'WO-2021102420-A1', 'WO-2023212447-A2', 'WO-2023225482-A3', 'WO-2023239670-A1', 'WO-2024044766-A3', 'WO-2024112568-A1'], 'var_call_BdNFFy7hXbD4Cv4pMaxIaYEM': 'file_storage/call_BdNFFy7hXbD4Cv4pMaxIaYEM.json', 'var_call_u4G7qeZ2I320L1Idc2fyilVW': {'result_list': [], 'all_codes': []}, 'var_call_fgSdFd0nlzrQTl13vaBBtYLD': 'file_storage/call_fgSdFd0nlzrQTl13vaBBtYLD.json'}

exec(code, env_args)

code = """import json, re
# load citing data file
with open(var_call_zm3xlwZY11sR1OUyUkrUODfm, 'r', encoding='utf-8') as f:
    citing = json.load(f)
# load UC pub list
uc_pubs = var_call_us6CX02wzWbLDhFIO1NmvgWP.get('pubs', [])

def norm(s):
    return re.sub(r'[^A-Z0-9]', '', s.upper())
uc_norm = set(norm(x) for x in uc_pubs)

found = []
for rec in citing:
    citation_field = rec.get('citation','')
    if not citation_field or citation_field.strip()=='[]':
        continue
    try:
        citations = json.loads(citation_field)
    except Exception:
        citations = []
    for c in citations:
        pubnum = (c.get('publication_number') or '').strip()
        if not pubnum:
            continue
        if norm(pubnum) in uc_norm:
            found.append({'rowid': rec.get('rowid'), 'Patents_info': rec.get('Patents_info'), 'matched_pub': pubnum})
            break

print('__RESULT__:')
print(json.dumps({'count': len(found), 'examples': found[:20]}))"""

env_args = {'var_call_3n6jtP4avHeccVh0WRwqg5Eh': ['publicationinfo'], 'var_call_ap8lHf5yOKlzQ5GzbDOFj8je': 'file_storage/call_ap8lHf5yOKlzQ5GzbDOFj8je.json', 'var_call_A6kD9ekRGoR9nIdyNsdhVMZI': {'publication_numbers': []}, 'var_call_ECYWy04AmouP8kCLNMlAVGJE': [{'rowid': '1173', 'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'rowid': '6244', 'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'rowid': '6967', 'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'rowid': '10358', 'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'rowid': '14719', 'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'rowid': '17880', 'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'rowid': '20566', 'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'rowid': '21654', 'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'rowid': '23096', 'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'rowid': '26944', 'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}], 'var_call_us6CX02wzWbLDhFIO1NmvgWP': {'count': 180, 'pubs': ['AP-3334-A', 'AU-2001257114-A1', 'AU-2001296493-B2', 'AU-2002254753-B2', 'AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008329628-B2', 'AU-2008349842-A1', 'AU-2009234210-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5366398-A', 'AU-5938296-A', 'AU-6492396-A', 'AU-6535890-A', 'AU-7724398-A', 'BR-112021021092-A8', 'BR-9610580-A', 'CA-2220674-A1', 'CA-2278751-A1', 'CA-2283629-C', 'CA-2298540-A1', 'CA-2494262-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CA-2718348-C', 'CA-3027364-A1', 'CA-3055214-A1', 'CA-3161617-A1', 'CA-3225295-A1', 'CN-100339724-C', 'CN-101584047-A', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'CN-103237558-A', 'CN-103687626-A', 'CN-1120376-C', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-1224461-B1', 'EP-2029921-A4', 'EP-2210307-A4', 'EP-3668487-A4', 'EP-3866867-A1', 'EP-4114888-A1', 'EP-4284234-A1', 'FR-2194760-A1', 'HK-1052178-A1', 'HK-1250569-A1', 'HR-P20201231-T1', 'ID-23426-A', 'IL-140140-A0', 'IL-236725-A', 'IL-244029-A0', 'IL-255026-A0', 'IL-274176-A', 'JP-2005104983-A', 'JP-2009260386-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-100228821-B1', 'KR-20050085437-A', 'KR-20080078049-A', 'KR-20110004413-A', 'KR-20160119166-A', 'KR-20180041236-A', 'KR-20200041324-A', 'KR-20200084864-A', 'MX-2013002850-A', 'PE-20130764-A1', 'PT-2970346-T', 'RO-70061-A', 'TW-201925402-A', 'US-10337029-B2', 'US-10359432-B2', 'US-10744347-B2', 'US-10765865-B2', 'US-10900049-B2', 'US-11014955-B2', 'US-11072681-B2', 'US-11248107-B2', 'US-11376346-B2', 'US-11421276-B2', 'US-11445941-B2', 'US-11546022-B2', 'US-11607427-B2', 'US-11667770-B2', 'US-11960018-B2', 'US-12025581-B2', 'US-2003112494-A1', 'US-2004115131-A1', 'US-2005136639-A1', 'US-2005234013-A1', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2008047008-A1', 'US-2008139409-A1', 'US-2009031436-A1', 'US-2010025717-A1', 'US-2017050153-A1', 'US-2017087258-A1', 'US-2017145219-A1', 'US-2017194630-A1', 'US-2017281687-A1', 'US-2017294981-A1', 'US-2017369950-A1', 'US-2018080022-A1', 'US-2018177786-A1', 'US-2018243924-A1', 'US-2018277766-A1', 'US-2018304537-A1', 'US-2018348310-A1', 'US-2019169580-A1', 'US-2019209590-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2020222513-A1', 'US-2020283856-A1', 'US-2021000566-A1', 'US-2021002329-A1', 'US-2021039104-A1', 'US-2021101879-A1', 'US-2021181673-A1', 'US-2021282642-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2022123166-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023314781-A1', 'US-2023321419-A1', 'US-2023340506-A1', 'US-3666017-A', 'US-3842373-A', 'US-5304932-A', 'US-5547866-A', 'US-6030830-A', 'US-6237292-B1', 'US-6750960-B2', 'US-6767662-B2', 'US-6980295-B2', 'US-7052856-B2', 'US-7745569-B2', 'US-8361933-B2', 'US-9061071-B2', 'US-9274095-B2', 'WO-2010045542-A3', 'WO-2012158833-A3', 'WO-2012162563-A2', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2018067976-A1', 'WO-2018152537-A1', 'WO-2019067860-A1', 'WO-2019173834-A1', 'WO-2020055916-A9', 'WO-2020068183-A3', 'WO-2020096950-A1', 'WO-2021102420-A1', 'WO-2022178138-A1', 'WO-2022245977-A2', 'WO-2023212447-A2', 'WO-2023225482-A3', 'WO-2023239670-A1', 'WO-2024044766-A3', 'WO-2024050335-A2', 'WO-2024112568-A1', 'ZA-200802422-B']}, 'var_call_zm3xlwZY11sR1OUyUkrUODfm': 'file_storage/call_zm3xlwZY11sR1OUyUkrUODfm.json', 'var_call_2S0TJj3dN5bwc3bDfByDkCae': {'results': [], 'unique_codes': []}, 'var_call_YpZQUcum3wWBwFcNrM6elydt': {'count': 0, 'matches': [], 'unique_codes': []}, 'var_call_QzLOyxeDXXYB2J1jVVmcaKRd': []}

exec(code, env_args)

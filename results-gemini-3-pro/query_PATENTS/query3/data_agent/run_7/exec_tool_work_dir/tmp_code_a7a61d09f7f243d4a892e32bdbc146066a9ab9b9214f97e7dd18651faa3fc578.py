code = """import json
import re

# Load UC pub nums from the previous tool result variable
uc_pub_nums_json = locals()['var_function-call-11090742952057133004']
uc_pub_nums = set(json.loads(uc_pub_nums_json))

# Load large data
large_data_file = locals()['var_function-call-3449729610111973543']
with open(large_data_file, 'r') as f:
    large_data = json.load(f)

def get_assignee(info):
    # Normalize spaces
    info = ' '.join(info.split())
    
    # "ASSIGNEE holds..."
    m1 = re.search(r'^(.*?) holds the', info)
    if m1: return m1.group(1).strip()
    
    # "... is owned by ASSIGNEE and"
    m2 = re.search(r'is owned by (.*?) and', info)
    if m2: return m2.group(1).strip()

    # "... is assigned to ASSIGNEE and"
    m3 = re.search(r'is assigned to (.*?) and', info)
    if m3: return m3.group(1).strip()

    # "... is belonging to ASSIGNEE and"
    m4 = re.search(r'is belonging to (.*?) and', info)
    if m4: return m4.group(1).strip()
    
    # "... is held by ASSIGNEE and"
    m5 = re.search(r'is held by (.*?) and', info)
    if m5: return m5.group(1).strip()

    # "... from COUNTRY, held by ASSIGNEE, with"
    m6 = re.search(r'held by (.*?), with', info)
    if m6: return m6.group(1).strip()

    # "... from COUNTRY, assigned to ASSIGNEE, with"
    m7 = re.search(r'assigned to (.*?), with', info)
    if m7: return m7.group(1).strip()

    # "... from COUNTRY, belonging to ASSIGNEE, with"
    m8 = re.search(r'belonging to (.*?), with', info)
    if m8: return m8.group(1).strip()
    
    # "... from COUNTRY, owned by ASSIGNEE, with"
    m9 = re.search(r'owned by (.*?), with', info)
    if m9: return m9.group(1).strip()

    return None

results = []

for record in large_data:
    citation_str = record.get('citation')
    if not citation_str:
        continue
    
    try:
        citations = json.loads(citation_str)
    except:
        continue
        
    found = False
    # citations is a list of dicts
    for cit in citations:
        if cit.get('publication_number') in uc_pub_nums:
            found = True
            break
    
    if found:
        assignee = get_assignee(record['Patents_info'])
        if assignee and "UNIV CALIFORNIA" in assignee:
            # Should have been filtered by SQL, but double check
            continue

        if assignee:
            # Get CPC subclass
            cpc_subclass = None
            cpc_str = record.get('cpc')
            if cpc_str:
                try:
                    cpc_list = json.loads(cpc_str)
                    if isinstance(cpc_list, list) and len(cpc_list) > 0:
                        first_cpc = cpc_list[0]
                        # Check keys
                        code = first_cpc.get('code') or first_cpc.get('symbol')
                        if code:
                            # Extract subclass: first 4 chars e.g. H04W
                            cpc_subclass = code[:4]
                except:
                    pass
            
            if cpc_subclass:
                results.append({'assignee': assignee, 'cpc_subclass': cpc_subclass})

# Dedup results
unique_results = []
seen = set()
for r in results:
    key = (r['assignee'], r['cpc_subclass'])
    if key not in seen:
        seen.add(key)
        unique_results.append(r)

print("__RESULT__:")
print(json.dumps(unique_results))"""

env_args = {'var_function-call-14168386675017252201': ['publicationinfo'], 'var_function-call-3811180657744915643': 'file_storage/function-call-3811180657744915643.json', 'var_function-call-10487200640104094230': 'file_storage/function-call-10487200640104094230.json', 'var_function-call-16461011087031621131': [{'count(*)': '277644'}], 'var_function-call-13330813147012195867': [{'count(*)': '169'}], 'var_function-call-11090742952057133004': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'US-2017194630-A1', 'JP-S6163700-A', 'US-2017281687-A1', 'EP-1224461-B1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2', 'US-11072681-B2', 'AU-2002254753-B2', 'US-9061071-B2', 'KR-20050085437-A', 'KR-20160119166-A', 'EP-0826155-A4', 'US-2019169580-A1', 'US-2020283856-A1', 'AU-2898989-A', 'RO-70061-A', 'WO-2017136335-A1', 'WO-2020096950-A1', 'WO-2021102420-A1', 'WO-2012162563-A2', 'US-10900049-B2', 'US-11376346-B2', 'US-2017369950-A1', 'KR-20180041236-A', 'CN-100339724-C', 'US-2009031436-A1', 'AU-2005269556-A1', 'US-11248107-B2', 'WO-2019173834-A1', 'US-2017145219-A1', 'US-2018304537-A1', 'US-2021002329-A1', 'KR-20200041324-A', 'CN-103189548-A', 'CA-2298540-A1', 'AU-2001296493-B2', 'AU-2008329628-B2', 'US-10765865-B2', 'JP-2005104983-A', 'IL-140140-A0', 'US-2021000566-A1', 'US-2006051790-A1', 'KR-20200084864-A', 'PT-2970346-T', 'US-3842373-A', 'AU-7724398-A', 'US-2023171142-A1', 'WO-2022178138-A1', 'WO-2018026404-A3', 'US-2006292670-A1', 'US-2017050153-A1', 'US-2021101879-A1', 'US-2023321419-A1', 'AU-2003297741-A1', 'WO-2017214343-A1', 'US-2018348310-A1', 'US-2021282642-A1', 'US-2019209590-A1', 'KR-20080078049-A', 'FR-2194760-A1', 'US-10359432-B2', 'US-11667770-B2', 'CA-3161617-A1', 'CA-3225295-A1', 'JP-2009260386-A', 'CA-2562038-C', 'US-7052856-B2', 'US-6750960-B2', 'EP-2210307-A4', 'BR-112021021092-A8', 'US-2005136639-A1', 'US-2020025859-A1', 'US-2021039104-A1', 'EP-1212462-A1', 'WO-2014152660-A1', 'WO-2024050335-A2', 'US-5547866-A', 'KR-100228821-B1', 'US-2023279470-A1', 'AU-2008349842-A1', 'EP-4284234-A1', 'WO-2018067976-A1', 'WO-2020055916-A9', 'US-6767662-B2', 'US-2021181673-A1', 'US-2023314781-A1', 'WO-2018152537-A1', 'WO-2023212447-A2', 'US-6980295-B2', 'AU-2015364602-B2', 'US-2003112494-A1', 'CN-1120376-C', 'CA-2220674-A1', 'IL-274176-A', 'JP-2014224156-A', 'IL-244029-A0', 'US-2004115131-A1', 'US-2005234013-A1', 'US-2008047008-A1', 'US-6030830-A', 'CN-101584047-A', 'AU-2010214112-B2', 'MX-2013002850-A', 'US-2019328740-A1', 'US-2022018060-A1', 'WO-2023225482-A3', 'WO-2024044766-A3', 'CA-3027364-A1', 'CA-3055214-A1', 'AU-2007297661-A1', 'EP-3866867-A1', 'WO-2019067860-A1', 'EP-2029921-A4', 'US-2018080022-A1', 'US-2022123166-A1', 'WO-2024112568-A1', 'US-2018277766-A1', 'AU-2001257114-A1', 'CA-2550552-A1', 'PE-20130764-A1', 'US-2017294981-A1', 'US-11445941-B2', 'US-11014955-B2', 'US-3666017-A', 'IL-236725-A', 'KR-20110004413-A', 'CN-103237558-A', 'CN-102584712-A', 'CN-103687626-A', 'ZA-200802422-B', 'CN-102067370-B', 'CA-2718348-C', 'CA-2278751-A1', 'US-10337029-B2', 'US-11546022-B2', 'HK-1052178-A1', 'US-11607427-B2', 'US-12025581-B2', 'US-11960018-B2', 'US-2023155090-A1', 'WO-2010045542-A3', 'EP-3668487-A4', 'US-8361933-B2', 'AP-3334-A', 'CA-2283629-C', 'US-2023340506-A1', 'HK-1250569-A1', 'AU-2004253879-A1', 'WO-2023239670-A1', 'WO-2012158833-A3', 'US-10744347-B2', 'HR-P20201231-T1', 'BR-9610580-A', 'AU-2409401-A', 'AU-5366398-A', 'ID-23426-A', 'US-5304932-A', 'AU-3353000-A', 'AU-5938296-A', 'US-2010025717-A1', 'US-2017087258-A1', 'US-2018243924-A1', 'AU-6535890-A'], 'var_function-call-3449729610111973543': 'file_storage/function-call-3449729610111973543.json'}

exec(code, env_args)

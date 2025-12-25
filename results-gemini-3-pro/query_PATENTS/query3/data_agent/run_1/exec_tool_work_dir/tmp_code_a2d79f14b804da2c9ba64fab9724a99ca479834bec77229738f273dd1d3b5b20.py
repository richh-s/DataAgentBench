code = """import json
import re

# Load UC patents info to get UC pub numbers
key_uc = 'var_function-call-1072305036396177702'
path_uc = locals()[key_uc]
with open(path_uc, 'r') as f:
    uc_patents_data = json.load(f)

uc_pub_numbers = set()
for row in uc_patents_data:
    info = row['Patents_info']
    match = re.search(r'(?:publication|pub\.?)\s+(?:number|no\.)\s+([A-Za-z0-9-]+)', info, re.IGNORECASE)
    if match:
        uc_pub_numbers.add(match.group(1))

# Load all patents with citation
key_all = 'var_function-call-14283660558727649773'
path_all = locals()[key_all]
# This file is large. I hope json.load handles it.
with open(path_all, 'r') as f:
    all_patents_data = json.load(f)

results = []
subclasses = set()

for row in all_patents_data:
    # Check citations
    citations = row.get('citation', '[]')
    try:
        citations_list = json.loads(citations)
    except:
        continue
    
    found_citation = False
    for cit in citations_list:
        if cit.get('publication_number') in uc_pub_numbers:
            found_citation = True
            break
    
    if found_citation:
        # Extract assignee
        info = row['Patents_info']
        assignee = None
        # Attempt patterns
        # 1. Start with "X holds"
        m = re.match(r'^(.+?)\s+(?:holds|owns)', info, re.IGNORECASE)
        if m:
            assignee = m.group(1)
        else:
            # 2. "... is owned by X and ..." or "... is owned by X."
            # We need to be careful about "and has pub number..."
            # Pattern: "... (?:owned by|assigned to|belonging to|held by) (.+?)(?: and| with|,|\.)"
            m = re.search(r'(?:owned by|assigned to|belonging to|held by)\s+(.+?)(?:\s+(?:and|with|,)|$|\.)', info, re.IGNORECASE)
            if m:
                assignee = m.group(1)
        
        if assignee:
            # Clean assignee
            assignee = assignee.strip()
            # Check if UC
            if "UNIV CALIFORNIA" in assignee.upper() or "UNIVERSITY OF CALIFORNIA" in assignee.upper():
                continue
            
            # Get Primary CPC
            cpc_str = row.get('cpc', '[]')
            try:
                cpc_list = json.loads(cpc_str)
            except:
                cpc_list = []
            
            primary_subclass = None
            if cpc_list:
                # Find first: true
                first_code = None
                for c in cpc_list:
                    if c.get('first') is True:
                        first_code = c.get('code')
                        break
                if not first_code and len(cpc_list) > 0:
                    first_code = cpc_list[0].get('code')
                
                if first_code:
                    # Extract subclass (first 4 chars)
                    # e.g. C01B33/00 -> C01B
                    if len(first_code) >= 4:
                        primary_subclass = first_code[:4]
            
            if assignee and primary_subclass:
                results.append({"assignee": assignee, "subclass": primary_subclass})
                subclasses.add(primary_subclass)

print("__RESULT__:")
print(json.dumps({"matches": results, "subclasses": list(subclasses)}))"""

env_args = {'var_function-call-2317850229295354016': 'file_storage/function-call-2317850229295354016.json', 'var_function-call-1072305036396177702': 'file_storage/function-call-1072305036396177702.json', 'var_function-call-18317220707519744366': ['US-9061071-B2', 'CA-2298540-A1', 'US-6237292-B1', 'CA-2562038-C', 'US-5547866-A', 'US-2021282642-A1', 'WO-2023239670-A1', 'US-2017145219-A1', 'US-2022018060-A1', 'US-2023340506-A1', 'US-2018304537-A1', 'JP-2005104983-A', 'AU-2010214112-B2', 'US-2023321419-A1', 'HR-P20201231-T1', 'AU-2003297741-A1', 'US-8361933-B2', 'WO-2017136335-A1', 'US-2022074631-A1', 'WO-2012158833-A3', 'CN-101584047-A', 'US-2017369950-A1', 'WO-2018026404-A3', 'KR-20180041236-A', 'US-2008047008-A1', 'US-2019328740-A1', 'WO-2020055916-A9', 'JP-S6163700-A', 'US-11014955-B2', 'US-2023171142-A1', 'CN-103237558-A', 'CN-103687626-A', 'BR-9610580-A', 'US-11248107-B2', 'EP-1212462-A1', 'WO-2018152537-A1', 'US-2021000566-A1', 'TW-201925402-A', 'FR-2194760-A1', 'US-2019209590-A1', 'AU-2007297661-A1', 'ZA-200802422-B', 'US-6750960-B2', 'EP-3668487-A4', 'AU-5938296-A', 'US-11960018-B2', 'WO-2014152660-A1', 'CA-2550552-A1', 'US-2009031436-A1', 'WO-2023212447-A2', 'WO-2018067976-A1', 'AU-2001257114-A1', 'US-11667770-B2', 'IL-244029-A0', 'AU-2015364602-B2', 'US-2018080022-A1', 'CA-3027364-A1', 'CA-2283629-C', 'EP-0826155-A4', 'KR-20050085437-A', 'US-5304932-A', 'US-11421276-B2', 'US-2005136639-A1', 'HK-1250569-A1', 'AU-2004253879-A1', 'IL-140140-A0', 'AU-2008349842-A1', 'US-2003112494-A1', 'AU-2017356943-A1', 'AU-7724398-A', 'US-2006292670-A1', 'AU-2008329628-B2', 'JP-2009260386-A', 'CN-100339724-C', 'WO-2022178138-A1', 'CA-3055214-A1', 'AU-2898989-A', 'BR-112021021092-A8', 'US-12025581-B2', 'KR-20080078049-A', 'EP-2029921-A4', 'US-2023314781-A1', 'US-6767662-B2', 'KR-100228821-B1', 'US-6980295-B2', 'US-10337029-B2', 'US-2021039104-A1', 'US-2017294981-A1', 'RO-70061-A', 'KR-20200084864-A', 'IL-236725-A', 'WO-2024044766-A3', 'ID-23426-A', 'EP-2210307-A4', 'AU-2003247814-A1', 'AU-2002254753-B2', 'CN-103189548-A', 'CN-102584712-A', 'CA-2718348-C', 'JP-2014224156-A', 'US-7745569-B2', 'US-10765865-B2', 'PT-2970346-T', 'US-2010025717-A1', 'US-2022123166-A1', 'AU-5366398-A', 'IL-274176-A', 'US-2023279470-A1', 'AU-2005269556-A1', 'MX-2013002850-A', 'KR-20200041324-A', 'US-10744347-B2', 'CN-102067370-B', 'US-10359432-B2', 'US-2023155090-A1', 'WO-2023225482-A3', 'US-2017050153-A1', 'US-2017194630-A1', 'WO-2020096950-A1', 'US-2006051790-A1', 'AU-3353000-A', 'US-11607427-B2', 'CA-2278751-A1', 'WO-2024050335-A2', 'AU-6535890-A', 'US-2020283856-A1', 'CA-3225295-A1', 'US-2017281687-A1', 'US-11445941-B2', 'AU-2001296493-B2', 'US-7052856-B2', 'PE-20130764-A1', 'CA-3161617-A1', 'KR-20110004413-A', 'WO-2012162563-A2', 'US-10900049-B2', 'US-2021181673-A1', 'AP-3334-A', 'CN-1120376-C', 'US-6030830-A', 'WO-2024112568-A1', 'US-2021002329-A1', 'AU-2019275518-B2', 'EP-4284234-A1', 'HK-1052178-A1', 'US-3666017-A', 'US-2005234013-A1', 'US-11546022-B2', 'WO-2019067860-A1', 'US-2017087258-A1', 'WO-2021102420-A1', 'EP-1224461-B1', 'EP-3866867-A1', 'US-2020025859-A1', 'US-2019169580-A1', 'WO-2010045542-A3', 'WO-2019173834-A1', 'CA-2220674-A1', 'US-11376346-B2', 'US-11072681-B2', 'KR-20160119166-A', 'US-2004115131-A1', 'US-3842373-A', 'US-2018277766-A1', 'US-2021101879-A1', 'US-2018348310-A1', 'AU-2409401-A', 'US-2018243924-A1', 'WO-2017214343-A1'], 'var_function-call-2932008334169908075': [{'COUNT(*)': '277813'}], 'var_function-call-14283660558727649773': 'file_storage/function-call-14283660558727649773.json'}

exec(code, env_args)

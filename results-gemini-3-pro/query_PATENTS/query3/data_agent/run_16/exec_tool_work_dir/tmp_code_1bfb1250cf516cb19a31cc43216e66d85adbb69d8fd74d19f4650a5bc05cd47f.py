code = """import json
import re

# Load UC pub numbers
uc_pub_numbers = set(json.loads(locals()['var_call_9805513219337165050_result'])) # Accessing previous result correctly?
# Actually, I printed it in the previous step. I can just re-use the variable `uc_pub_numbers` if I could pass it, but I must parse the output or re-calculate.
# Better to re-calculate or parse the printed output.
# The previous output was printed as:
# print("__RESULT__:")
# print(json.dumps(list(uc_pub_numbers)))
# I can access it via `var_function-call-9805513219337165050` which is the key for the result string?
# No, the result is in `locals()['var_function-call-9805513219337165050']` (Wait, the tool output says "The result is stored under key: var_...").
# So I can load it.

uc_pub_numbers_list = json.loads(locals()['var_function-call-9805513219337165050'])
uc_pub_numbers = set(uc_pub_numbers_list)

# Load the patents data
with open(locals()['var_function-call-16848582328649646875'], 'r') as f:
    patents_data = json.load(f)

# Regex for assignee extraction
# Patterns:
# 1. "X holds the ..."
# 2. "... is assigned to X and ..."
# 3. "... is owned by X and ..."
# 4. "... held by X, with ..."
# 5. "... belonging to X and ..."
# 6. "... held by X and ..."

assignee_patterns = [
    re.compile(r"^(.*?)\s+holds the", re.IGNORECASE),
    re.compile(r"is assigned to\s+(.*?)\s+and", re.IGNORECASE),
    re.compile(r"is owned by\s+(.*?)\s+and", re.IGNORECASE),
    re.compile(r"held by\s+(.*?)(?:,|\s+and)", re.IGNORECASE),
    re.compile(r"belonging to\s+(.*?)\s+and", re.IGNORECASE)
]

results = []
seen = set()

for row in patents_data:
    citations = row.get('citation')
    if not citations:
        continue
    
    # citations is a JSON string
    try:
        cit_list = json.loads(citations)
    except:
        continue
        
    # Check if cites UC
    cites_uc = False
    for cit in cit_list:
        if cit.get('publication_number') in uc_pub_numbers:
            cites_uc = True
            break
    
    if cites_uc:
        # Extract assignee
        info = row.get('Patents_info', '')
        assignee = None
        for p in assignee_patterns:
            m = p.search(info)
            if m:
                assignee = m.group(1).strip()
                break
        
        if not assignee:
            # Fallback or specific case handling?
            # Maybe the assignee is at the start?
            pass
            
        if assignee and "UNIV CALIFORNIA" not in assignee.upper():
            # Get primary CPC
            cpc_json = row.get('cpc')
            if cpc_json:
                try:
                    cpc_list = json.loads(cpc_json)
                    primary_code = None
                    # First try to find "first": true
                    for c in cpc_list:
                        if c.get('first') is True:
                            primary_code = c.get('code')
                            break
                    # If not found, take the first one
                    if not primary_code and len(cpc_list) > 0:
                        primary_code = cpc_list[0].get('code')
                    
                    if primary_code:
                        # Subclass is first 4 chars (e.g. H04W)
                        subclass = primary_code[:4]
                        if (assignee, subclass) not in seen:
                            results.append({"assignee": assignee, "subclass": subclass})
                            seen.add((assignee, subclass))
                except:
                    pass

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-15597883525086594650': ['publicationinfo'], 'var_function-call-6427787848654403341': 'file_storage/function-call-6427787848654403341.json', 'var_function-call-9357512243923287122': 'file_storage/function-call-9357512243923287122.json', 'var_function-call-16665196751990069996': [{'COUNT(*)': '277813'}], 'var_function-call-9805513219337165050': ['AU-5366398-A', 'US-2006051790-A1', 'AU-5938296-A', 'WO-2018026404-A3', 'US-6030830-A', 'KR-20200041324-A', 'CA-2283629-C', 'CN-100339724-C', 'AU-2008349842-A1', 'EP-3668487-A4', 'US-2023171142-A1', 'US-7052856-B2', 'US-2020025859-A1', 'US-11960018-B2', 'AU-2001296493-B2', 'WO-2023239670-A1', 'WO-2012162563-A2', 'WO-2023225482-A3', 'IL-236725-A', 'WO-2019067860-A1', 'AU-2017356943-A1', 'WO-2023212447-A2', 'CA-3161617-A1', 'AU-2002254753-B2', 'US-11014955-B2', 'IL-140140-A0', 'KR-20160119166-A', 'US-7745569-B2', 'US-10765865-B2', 'EP-1224461-B1', 'US-2021181673-A1', 'WO-2012158833-A3', 'KR-20180041236-A', 'AU-2007297661-A1', 'US-10744347-B2', 'AU-2019275518-B2', 'AU-2015364602-B2', 'HR-P20201231-T1', 'IL-244029-A0', 'EP-2029921-A4', 'US-2017294981-A1', 'US-2023155090-A1', 'US-2021000566-A1', 'RO-70061-A', 'WO-2020055916-A9', 'US-6767662-B2', 'EP-1212462-A1', 'US-10337029-B2', 'US-2023321419-A1', 'AU-2409401-A', 'WO-2017136335-A1', 'US-9061071-B2', 'WO-2010045542-A3', 'US-11421276-B2', 'US-2020283856-A1', 'EP-3866867-A1', 'US-2006292670-A1', 'US-2019328740-A1', 'CA-2718348-C', 'IL-274176-A', 'US-11445941-B2', 'US-12025581-B2', 'KR-20050085437-A', 'US-2018304537-A1', 'US-5304932-A', 'US-11376346-B2', 'CN-103189548-A', 'US-2021039104-A1', 'CN-102067370-B', 'WO-2020096950-A1', 'JP-2005104983-A', 'CN-103687626-A', 'ZA-200802422-B', 'US-10359432-B2', 'US-2018080022-A1', 'CA-2298540-A1', 'US-3666017-A', 'WO-2024050335-A2', 'JP-2009260386-A', 'JP-S6163700-A', 'AU-2008329628-B2', 'WO-2018067976-A1', 'US-6750960-B2', 'US-6980295-B2', 'CA-2220674-A1', 'JP-2014224156-A', 'HK-1052178-A1', 'US-2021101879-A1', 'US-5547866-A', 'KR-100228821-B1', 'AU-3353000-A', 'US-2010025717-A1', 'CA-2562038-C', 'US-2022123166-A1', 'PT-2970346-T', 'US-2023340506-A1', 'WO-2024112568-A1', 'US-2023279470-A1', 'WO-2017214343-A1', 'US-2019169580-A1', 'US-2022074631-A1', 'WO-2021102420-A1', 'WO-2014152660-A1', 'US-11248107-B2', 'US-2017369950-A1', 'AU-7724398-A', 'US-2017145219-A1', 'US-2022018060-A1', 'US-2004115131-A1', 'US-2005136639-A1', 'US-6237292-B1', 'BR-112021021092-A8', 'CA-3055214-A1', 'US-2018277766-A1', 'US-8361933-B2', 'US-2003112494-A1', 'CA-3225295-A1', 'EP-0826155-A4', 'BR-9610580-A', 'US-10900049-B2', 'WO-2019173834-A1', 'CN-103237558-A', 'AU-2001257114-A1', 'MX-2013002850-A', 'KR-20110004413-A', 'AU-2005269556-A1', 'US-2017194630-A1', 'US-2018348310-A1', 'US-2009031436-A1', 'AU-2898989-A', 'CN-1120376-C', 'AU-2003247814-A1', 'AP-3334-A', 'FR-2194760-A1', 'US-2005234013-A1', 'US-2023314781-A1', 'CN-101584047-A', 'HK-1250569-A1', 'CA-2278751-A1', 'AU-2010214112-B2', 'WO-2022178138-A1', 'US-11667770-B2', 'AU-2004253879-A1', 'AU-2003297741-A1', 'WO-2024044766-A3', 'US-2017087258-A1', 'CA-3027364-A1', 'US-2018243924-A1', 'US-2021282642-A1', 'US-2008047008-A1', 'ID-23426-A', 'US-2017281687-A1', 'AU-6535890-A', 'US-2017050153-A1', 'US-3842373-A', 'TW-201925402-A', 'PE-20130764-A1', 'US-11607427-B2', 'US-11546022-B2', 'CA-2550552-A1', 'KR-20080078049-A', 'EP-2210307-A4', 'WO-2018152537-A1', 'US-2021002329-A1', 'EP-4284234-A1', 'US-2019209590-A1', 'US-11072681-B2', 'KR-20200084864-A', 'CN-102584712-A'], 'var_function-call-16848582328649646875': 'file_storage/function-call-16848582328649646875.json'}

exec(code, env_args)

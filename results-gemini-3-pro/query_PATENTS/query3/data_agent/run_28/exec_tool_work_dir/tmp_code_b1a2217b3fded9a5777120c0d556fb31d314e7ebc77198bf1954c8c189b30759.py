code = """import json
import re

# Load citing patents
with open(locals()['var_function-call-238855271097293944'], 'r') as f:
    citing_patents = json.load(f)

# Regex for assignee
# Examples:
# "is assigned to ASSIGNEE and"
# "is owned by ASSIGNEE and"
# "is held by ASSIGNEE and"
# "is belonging to ASSIGNEE and"
# "ASSIGNEE holds the"
# "belonging to ASSIGNEE,"
# "held by ASSIGNEE,"
# "owned by ASSIGNEE,"
# "assigned to ASSIGNEE,"

# We need a robust regex.
# Look for "assigned to", "owned by", "held by", "belonging to" followed by the name, until "and" or "," or "has".
# Also look for "X holds the" at the start.

assignee_pattern = re.compile(r"(?:assigned to|owned by|held by|belonging to)\s+([A-Z0-9\s&]+?)(?:\s+(?:and|with|has|,)|$)")
start_pattern = re.compile(r"^([A-Z0-9\s&]+?)\s+holds the")

results = []
subclasses = set()

for row in citing_patents:
    info = row.get('Patents_info', '')
    assignee = None
    
    # Try start pattern first
    match = start_pattern.match(info)
    if match:
        assignee = match.group(1).strip()
    else:
        # Try finding in the middle
        match = assignee_pattern.search(info)
        if match:
            assignee = match.group(1).strip()
    
    if not assignee:
        continue

    # Exclude UNIV CALIFORNIA
    if "UNIV CALIFORNIA" in assignee:
        continue
        
    # Extract CPC
    cpc_json = row.get('cpc', '[]')
    try:
        cpcs = json.loads(cpc_json)
    except:
        continue
        
    primary_code = None
    for item in cpcs:
        if item.get('first') == True:
            primary_code = item.get('code')
            break
    
    # If no 'first' found, maybe take the first in list? 
    # Usually one is marked first. If not, we skip or take first.
    if not primary_code and cpcs:
        primary_code = cpcs[0].get('code')
        
    if primary_code:
        # Subclass is usually 4 chars (e.g. H01L)
        # Sometimes 3? Usually 4 (Class + Subclass letter).
        # Example G01V1/01 -> G01V
        subclass = primary_code[:4]
        subclasses.add(subclass)
        results.append({"assignee": assignee, "subclass": subclass})

# Prepare result
print("__RESULT__:")
print(json.dumps({"results": results, "subclasses": list(subclasses)}))"""

env_args = {'var_function-call-15790452253727073514': 'file_storage/function-call-15790452253727073514.json', 'var_function-call-11654680954070537156': [{'COUNT(*)': '169'}], 'var_function-call-2893938071127917234': 'file_storage/function-call-2893938071127917234.json', 'var_function-call-12328098168387465111': ['US-2021039104-A1', 'US-2018348310-A1', 'US-2003112494-A1', 'EP-4284234-A1', 'US-2018243924-A1', 'AU-2001296493-B2', 'US-11014955-B2', 'HR-P20201231-T1', 'US-5304932-A', 'AU-5366398-A', 'KR-20200041324-A', 'CN-103189548-A', 'US-10744347-B2', 'WO-2024044766-A3', 'AU-2409401-A', 'WO-2018152537-A1', 'JP-S6163700-A', 'KR-20180041236-A', 'JP-2014224156-A', 'WO-2018067976-A1', 'US-11607427-B2', 'AU-2007297661-A1', 'US-2020283856-A1', 'EP-3866867-A1', 'KR-20050085437-A', 'US-10337029-B2', 'US-2020025859-A1', 'US-2023321419-A1', 'US-2005136639-A1', 'WO-2023225482-A3', 'EP-2029921-A4', 'US-2022018060-A1', 'US-11445941-B2', 'CA-2550552-A1', 'US-2017294981-A1', 'WO-2012158833-A3', 'WO-2010045542-A3', 'US-2010025717-A1', 'IL-274176-A', 'WO-2022178138-A1', 'JP-2009260386-A', 'US-2017050153-A1', 'AU-2004253879-A1', 'CA-3055214-A1', 'CN-100339724-C', 'CN-102584712-A', 'BR-112021021092-A8', 'AU-2001257114-A1', 'AU-6535890-A', 'CA-2220674-A1', 'MX-2013002850-A', 'RO-70061-A', 'CN-1120376-C', 'KR-20080078049-A', 'CA-3225295-A1', 'WO-2024050335-A2', 'PT-2970346-T', 'US-6237292-B1', 'WO-2017214343-A1', 'WO-2021102420-A1', 'AP-3334-A', 'AU-7724398-A', 'JP-2005104983-A', 'US-7052856-B2', 'CA-2278751-A1', 'US-2017369950-A1', 'US-11960018-B2', 'US-2022074631-A1', 'WO-2017136335-A1', 'US-2021282642-A1', 'US-2021181673-A1', 'US-2021101879-A1', 'US-2017087258-A1', 'AU-2003297741-A1', 'US-2004115131-A1', 'CA-2283629-C', 'EP-1224461-B1', 'US-11376346-B2', 'US-3666017-A', 'EP-2210307-A4', 'CN-103687626-A', 'US-2022123166-A1', 'US-2018304537-A1', 'CN-103237558-A', 'CN-101584047-A', 'WO-2020055916-A9', 'IL-140140-A0', 'US-2018080022-A1', 'US-2019209590-A1', 'US-3842373-A', 'CN-102067370-B', 'US-2009031436-A1', 'US-10900049-B2', 'AU-2015364602-B2', 'BR-9610580-A', 'US-2019169580-A1', 'US-2017194630-A1', 'IL-244029-A0', 'AU-2008329628-B2', 'EP-1212462-A1', 'AU-2019275518-B2', 'US-5547866-A', 'FR-2194760-A1', 'US-9061071-B2', 'CA-2298540-A1', 'TW-201925402-A', 'US-8361933-B2', 'KR-20160119166-A', 'AU-2005269556-A1', 'AU-2003247814-A1', 'US-2006292670-A1', 'US-6980295-B2', 'AU-2898989-A', 'US-2023279470-A1', 'CA-3027364-A1', 'US-10765865-B2', 'KR-20110004413-A', 'CA-2562038-C', 'US-2017145219-A1', 'WO-2020096950-A1', 'US-11546022-B2', 'AU-5938296-A', 'PE-20130764-A1', 'US-11072681-B2', 'HK-1052178-A1', 'AU-2002254753-B2', 'HK-1250569-A1', 'US-12025581-B2', 'ID-23426-A', 'AU-2010214112-B2', 'US-11667770-B2', 'WO-2023212447-A2', 'WO-2019173834-A1', 'US-10359432-B2', 'KR-100228821-B1', 'WO-2023239670-A1', 'EP-3668487-A4', 'US-2023340506-A1', 'US-2021002329-A1', 'AU-3353000-A', 'US-2006051790-A1', 'CA-2718348-C', 'US-2023171142-A1', 'AU-2017356943-A1', 'US-2005234013-A1', 'EP-0826155-A4', 'CA-3161617-A1', 'US-7745569-B2', 'US-11248107-B2', 'US-6030830-A', 'US-2023314781-A1', 'WO-2018026404-A3', 'IL-236725-A', 'WO-2024112568-A1', 'US-6767662-B2', 'WO-2012162563-A2', 'US-2019328740-A1', 'US-2023155090-A1', 'ZA-200802422-B', 'AU-2008349842-A1', 'US-2021000566-A1', 'WO-2019067860-A1', 'US-2018277766-A1', 'US-6750960-B2', 'US-2008047008-A1', 'KR-20200084864-A', 'US-11421276-B2', 'US-2017281687-A1', 'WO-2014152660-A1'], 'var_function-call-6933898981858991529': 'citation LIKE \'%"US-2021039104-A1"%\' OR citation LIKE \'%"US-2018348310-A1"%\' OR citation LIKE \'%"US-2003112494-A1"%\' OR citation LIKE \'%"EP-4284234-A1"%\' OR citation LIKE \'%"US-2018243924-A1"%\' OR citation LIKE \'%"AU-2001296493-B2"%\' OR citation LIKE \'%"US-11014955-B2"%\' OR citation LIKE \'%"HR-P20201231-T1"%\' OR citation LIKE \'%"US-5304932-A"%\' OR citation LIKE \'%"AU-5366398-A"%\' OR citation LIKE \'%"KR-20200041324-A"%\' OR citation LIKE \'%"CN-103189548-A"%\' OR citation LIKE \'%"US-10744347-B2"%\' OR citation LIKE \'%"WO-2024044766-A3"%\' OR citation LIKE \'%"AU-2409401-A"%\' OR citation LIKE \'%"WO-2018152537-A1"%\' OR citation LIKE \'%"JP-S6163700-A"%\' OR citation LIKE \'%"KR-20180041236-A"%\' OR citation LIKE \'%"JP-2014224156-A"%\' OR citation LIKE \'%"WO-2018067976-A1"%\' OR citation LIKE \'%"US-11607427-B2"%\' OR citation LIKE \'%"AU-2007297661-A1"%\' OR citation LIKE \'%"US-2020283856-A1"%\' OR citation LIKE \'%"EP-3866867-A1"%\' OR citation LIKE \'%"KR-20050085437-A"%\' OR citation LIKE \'%"US-10337029-B2"%\' OR citation LIKE \'%"US-2020025859-A1"%\' OR citation LIKE \'%"US-2023321419-A1"%\' OR citation LIKE \'%"US-2005136639-A1"%\' OR citation LIKE \'%"WO-2023225482-A3"%\' OR citation LIKE \'%"EP-2029921-A4"%\' OR citation LIKE \'%"US-2022018060-A1"%\' OR citation LIKE \'%"US-11445941-B2"%\' OR citation LIKE \'%"CA-2550552-A1"%\' OR citation LIKE \'%"US-2017294981-A1"%\' OR citation LIKE \'%"WO-2012158833-A3"%\' OR citation LIKE \'%"WO-2010045542-A3"%\' OR citation LIKE \'%"US-2010025717-A1"%\' OR citation LIKE \'%"IL-274176-A"%\' OR citation LIKE \'%"WO-2022178138-A1"%\' OR citation LIKE \'%"JP-2009260386-A"%\' OR citation LIKE \'%"US-2017050153-A1"%\' OR citation LIKE \'%"AU-2004253879-A1"%\' OR citation LIKE \'%"CA-3055214-A1"%\' OR citation LIKE \'%"CN-100339724-C"%\' OR citation LIKE \'%"CN-102584712-A"%\' OR citation LIKE \'%"BR-112021021092-A8"%\' OR citation LIKE \'%"AU-2001257114-A1"%\' OR citation LIKE \'%"AU-6535890-A"%\' OR citation LIKE \'%"CA-2220674-A1"%\' OR citation LIKE \'%"MX-2013002850-A"%\' OR citation LIKE \'%"RO-70061-A"%\' OR citation LIKE \'%"CN-1120376-C"%\' OR citation LIKE \'%"KR-20080078049-A"%\' OR citation LIKE \'%"CA-3225295-A1"%\' OR citation LIKE \'%"WO-2024050335-A2"%\' OR citation LIKE \'%"PT-2970346-T"%\' OR citation LIKE \'%"US-6237292-B1"%\' OR citation LIKE \'%"WO-2017214343-A1"%\' OR citation LIKE \'%"WO-2021102420-A1"%\' OR citation LIKE \'%"AP-3334-A"%\' OR citation LIKE \'%"AU-7724398-A"%\' OR citation LIKE \'%"JP-2005104983-A"%\' OR citation LIKE \'%"US-7052856-B2"%\' OR citation LIKE \'%"CA-2278751-A1"%\' OR citation LIKE \'%"US-2017369950-A1"%\' OR citation LIKE \'%"US-11960018-B2"%\' OR citation LIKE \'%"US-2022074631-A1"%\' OR citation LIKE \'%"WO-2017136335-A1"%\' OR citation LIKE \'%"US-2021282642-A1"%\' OR citation LIKE \'%"US-2021181673-A1"%\' OR citation LIKE \'%"US-2021101879-A1"%\' OR citation LIKE \'%"US-2017087258-A1"%\' OR citation LIKE \'%"AU-2003297741-A1"%\' OR citation LIKE \'%"US-2004115131-A1"%\' OR citation LIKE \'%"CA-2283629-C"%\' OR citation LIKE \'%"EP-1224461-B1"%\' OR citation LIKE \'%"US-11376346-B2"%\' OR citation LIKE \'%"US-3666017-A"%\' OR citation LIKE \'%"EP-2210307-A4"%\' OR citation LIKE \'%"CN-103687626-A"%\' OR citation LIKE \'%"US-2022123166-A1"%\' OR citation LIKE \'%"US-2018304537-A1"%\' OR citation LIKE \'%"CN-103237558-A"%\' OR citation LIKE \'%"CN-101584047-A"%\' OR citation LIKE \'%"WO-2020055916-A9"%\' OR citation LIKE \'%"IL-140140-A0"%\' OR citation LIKE \'%"US-2018080022-A1"%\' OR citation LIKE \'%"US-2019209590-A1"%\' OR citation LIKE \'%"US-3842373-A"%\' OR citation LIKE \'%"CN-102067370-B"%\' OR citation LIKE \'%"US-2009031436-A1"%\' OR citation LIKE \'%"US-10900049-B2"%\' OR citation LIKE \'%"AU-2015364602-B2"%\' OR citation LIKE \'%"BR-9610580-A"%\' OR citation LIKE \'%"US-2019169580-A1"%\' OR citation LIKE \'%"US-2017194630-A1"%\' OR citation LIKE \'%"IL-244029-A0"%\' OR citation LIKE \'%"AU-2008329628-B2"%\' OR citation LIKE \'%"EP-1212462-A1"%\' OR citation LIKE \'%"AU-2019275518-B2"%\' OR citation LIKE \'%"US-5547866-A"%\' OR citation LIKE \'%"FR-2194760-A1"%\' OR citation LIKE \'%"US-9061071-B2"%\' OR citation LIKE \'%"CA-2298540-A1"%\' OR citation LIKE \'%"TW-201925402-A"%\' OR citation LIKE \'%"US-8361933-B2"%\' OR citation LIKE \'%"KR-20160119166-A"%\' OR citation LIKE \'%"AU-2005269556-A1"%\' OR citation LIKE \'%"AU-2003247814-A1"%\' OR citation LIKE \'%"US-2006292670-A1"%\' OR citation LIKE \'%"US-6980295-B2"%\' OR citation LIKE \'%"AU-2898989-A"%\' OR citation LIKE \'%"US-2023279470-A1"%\' OR citation LIKE \'%"CA-3027364-A1"%\' OR citation LIKE \'%"US-10765865-B2"%\' OR citation LIKE \'%"KR-20110004413-A"%\' OR citation LIKE \'%"CA-2562038-C"%\' OR citation LIKE \'%"US-2017145219-A1"%\' OR citation LIKE \'%"WO-2020096950-A1"%\' OR citation LIKE \'%"US-11546022-B2"%\' OR citation LIKE \'%"AU-5938296-A"%\' OR citation LIKE \'%"PE-20130764-A1"%\' OR citation LIKE \'%"US-11072681-B2"%\' OR citation LIKE \'%"HK-1052178-A1"%\' OR citation LIKE \'%"AU-2002254753-B2"%\' OR citation LIKE \'%"HK-1250569-A1"%\' OR citation LIKE \'%"US-12025581-B2"%\' OR citation LIKE \'%"ID-23426-A"%\' OR citation LIKE \'%"AU-2010214112-B2"%\' OR citation LIKE \'%"US-11667770-B2"%\' OR citation LIKE \'%"WO-2023212447-A2"%\' OR citation LIKE \'%"WO-2019173834-A1"%\' OR citation LIKE \'%"US-10359432-B2"%\' OR citation LIKE \'%"KR-100228821-B1"%\' OR citation LIKE \'%"WO-2023239670-A1"%\' OR citation LIKE \'%"EP-3668487-A4"%\' OR citation LIKE \'%"US-2023340506-A1"%\' OR citation LIKE \'%"US-2021002329-A1"%\' OR citation LIKE \'%"AU-3353000-A"%\' OR citation LIKE \'%"US-2006051790-A1"%\' OR citation LIKE \'%"CA-2718348-C"%\' OR citation LIKE \'%"US-2023171142-A1"%\' OR citation LIKE \'%"AU-2017356943-A1"%\' OR citation LIKE \'%"US-2005234013-A1"%\' OR citation LIKE \'%"EP-0826155-A4"%\' OR citation LIKE \'%"CA-3161617-A1"%\' OR citation LIKE \'%"US-7745569-B2"%\' OR citation LIKE \'%"US-11248107-B2"%\' OR citation LIKE \'%"US-6030830-A"%\' OR citation LIKE \'%"US-2023314781-A1"%\' OR citation LIKE \'%"WO-2018026404-A3"%\' OR citation LIKE \'%"IL-236725-A"%\' OR citation LIKE \'%"WO-2024112568-A1"%\' OR citation LIKE \'%"US-6767662-B2"%\' OR citation LIKE \'%"WO-2012162563-A2"%\' OR citation LIKE \'%"US-2019328740-A1"%\' OR citation LIKE \'%"US-2023155090-A1"%\' OR citation LIKE \'%"ZA-200802422-B"%\' OR citation LIKE \'%"AU-2008349842-A1"%\' OR citation LIKE \'%"US-2021000566-A1"%\' OR citation LIKE \'%"WO-2019067860-A1"%\' OR citation LIKE \'%"US-2018277766-A1"%\' OR citation LIKE \'%"US-6750960-B2"%\' OR citation LIKE \'%"US-2008047008-A1"%\' OR citation LIKE \'%"KR-20200084864-A"%\' OR citation LIKE \'%"US-11421276-B2"%\' OR citation LIKE \'%"US-2017281687-A1"%\' OR citation LIKE \'%"WO-2014152660-A1"%\'', 'var_function-call-238855271097293944': 'file_storage/function-call-238855271097293944.json'}

exec(code, env_args)

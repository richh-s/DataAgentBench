code = """import json
import re

# Load citing patents data
with open(locals()['var_function-call-15614453151447692542'], 'r') as f:
    citing_data = json.load(f)

assignee_subclasses = {} # Assignee -> set of subclasses
subclasses = set()

# Regex for assignee extraction
# Patterns:
# 1. "... is assigned to ASSIGNEE and ..."
# 2. "... is held by ASSIGNEE and ..."
# 3. "... is owned by ASSIGNEE and ..."
# 4. "... is belonging to ASSIGNEE and ..."
# 5. "ASSIGNEE holds the ..."
p1 = re.compile(r"is (?:assigned to|held by|owned by|belonging to)\s+([^,]+?)\s+(?:and|,|has)", re.IGNORECASE)
p2 = re.compile(r"^(.+?)\s+holds the", re.IGNORECASE)

for entry in citing_data:
    p_info = entry.get('Patents_info', '')
    cpc_json = entry.get('cpc', '[]')
    
    # Extract Assignee
    assignee = None
    m1 = p1.search(p_info)
    if m1:
        assignee = m1.group(1).strip()
    else:
        m2 = p2.search(p_info)
        if m2:
            assignee = m2.group(1).strip()
            
    if not assignee:
        continue
        
    # Clean assignee name (sometimes it might capture extra words if regex is loose)
    # The examples show mostly uppercase.
    # Exclude if "UNIV CALIFORNIA"
    if "CALIFORNIA" in assignee.upper() and "UNIV" in assignee.upper():
        continue
        
    # Extract Primary CPC
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    primary_code = None
    for item in cpc_list:
        if item.get('first') is True:
            primary_code = item.get('code')
            break
    if not primary_code and cpc_list:
        primary_code = cpc_list[0].get('code')
        
    if primary_code:
        # Subclass is first 4 chars (e.g., H01M)
        subclass = primary_code[:4]
        if assignee not in assignee_subclasses:
            assignee_subclasses[assignee] = set()
        assignee_subclasses[assignee].add(subclass)
        subclasses.add(subclass)

# Convert sets to lists for JSON serialization
output_assignees = {k: list(v) for k, v in assignee_subclasses.items()}
unique_subclasses = list(subclasses)

print("__RESULT__:")
print(json.dumps({"assignees": output_assignees, "subclasses": unique_subclasses}))"""

env_args = {'var_function-call-132688835705272036': 'file_storage/function-call-132688835705272036.json', 'var_function-call-8489921310635000644': 'file_storage/function-call-8489921310635000644.json', 'var_function-call-5807803094301361199': [{'count(*)': '277813'}], 'var_function-call-16125413690790445830': ['US-2023171142-A1', 'CN-103687626-A', 'US-2021181673-A1', 'AU-2003297741-A1', 'AP-3334-A', 'IL-274176-A', 'US-11960018-B2', 'WO-2019173834-A1', 'IL-244029-A0', 'US-10900049-B2', 'CA-2220674-A1', 'BR-112021021092-A8', 'WO-2023225482-A3', 'US-2017145219-A1', 'KR-20200041324-A', 'US-12025581-B2', 'ZA-200802422-B', 'CN-100339724-C', 'WO-2024050335-A2', 'FR-2194760-A1', 'RO-70061-A', 'EP-3668487-A4', 'TW-201925402-A', 'US-11014955-B2', 'JP-S6163700-A', 'AU-6535890-A', 'HK-1052178-A1', 'AU-2019275518-B2', 'WO-2020096950-A1', 'WO-2019067860-A1', 'KR-20160119166-A', 'AU-2005269556-A1', 'CN-102067370-B', 'US-6750960-B2', 'WO-2023239670-A1', 'US-11376346-B2', 'US-10359432-B2', 'US-11072681-B2', 'JP-2014224156-A', 'CN-103237558-A', 'US-11607427-B2', 'AU-7724398-A', 'WO-2014152660-A1', 'US-11445941-B2', 'US-2021039104-A1', 'US-2005136639-A1', 'CN-103189548-A', 'US-2022018060-A1', 'US-2022074631-A1', 'EP-2029921-A4', 'US-2017294981-A1', 'US-2023321419-A1', 'EP-4284234-A1', 'JP-2009260386-A', 'KR-20110004413-A', 'US-6237292-B1', 'WO-2017214343-A1', 'US-2006051790-A1', 'WO-2012158833-A3', 'IL-236725-A', 'MX-2013002850-A', 'US-2021282642-A1', 'US-2019328740-A1', 'WO-2020055916-A9', 'AU-2898989-A', 'US-2019169580-A1', 'AU-2003247814-A1', 'AU-2001296493-B2', 'EP-3866867-A1', 'US-6980295-B2', 'WO-2021102420-A1', 'US-2023314781-A1', 'US-6030830-A', 'US-5304932-A', 'KR-20050085437-A', 'US-8361933-B2', 'US-2018304537-A1', 'US-5547866-A', 'WO-2010045542-A3', 'CA-2550552-A1', 'AU-2001257114-A1', 'CA-3027364-A1', 'WO-2018026404-A3', 'KR-100228821-B1', 'WO-2018152537-A1', 'US-2017281687-A1', 'US-11546022-B2', 'CA-2298540-A1', 'US-2021000566-A1', 'WO-2024044766-A3', 'HR-P20201231-T1', 'US-2005234013-A1', 'US-11421276-B2', 'US-7052856-B2', 'US-2017050153-A1', 'US-2022123166-A1', 'IL-140140-A0', 'AU-2008329628-B2', 'CN-101584047-A', 'US-2018348310-A1', 'US-10744347-B2', 'AU-2004253879-A1', 'US-2004115131-A1', 'US-2018277766-A1', 'US-11667770-B2', 'AU-2008349842-A1', 'CN-1120376-C', 'CA-2283629-C', 'US-2018243924-A1', 'KR-20200084864-A', 'KR-20080078049-A', 'US-2018080022-A1', 'AU-5938296-A', 'US-3842373-A', 'WO-2022178138-A1', 'US-2021101879-A1', 'CA-2562038-C', 'US-2023340506-A1', 'US-2017369950-A1', 'US-2019209590-A1', 'CA-3055214-A1', 'PE-20130764-A1', 'AU-2017356943-A1', 'CN-102584712-A', 'US-9061071-B2', 'HK-1250569-A1', 'US-2020283856-A1', 'AU-2015364602-B2', 'AU-2002254753-B2', 'WO-2024112568-A1', 'KR-20180041236-A', 'US-2017087258-A1', 'EP-1224461-B1', 'US-11248107-B2', 'ID-23426-A', 'AU-2007297661-A1', 'WO-2012162563-A2', 'BR-9610580-A', 'US-3666017-A', 'US-2020025859-A1', 'US-10765865-B2', 'US-2023279470-A1', 'US-2017194630-A1', 'PT-2970346-T', 'AU-3353000-A', 'US-2008047008-A1', 'US-2003112494-A1', 'AU-2010214112-B2', 'US-2010025717-A1', 'US-10337029-B2', 'EP-0826155-A4', 'AU-5366398-A', 'EP-2210307-A4', 'CA-3225295-A1', 'WO-2018067976-A1', 'AU-2409401-A', 'US-7745569-B2', 'EP-1212462-A1', 'US-2021002329-A1', 'CA-2718348-C', 'WO-2023212447-A2', 'WO-2017136335-A1', 'US-6767662-B2', 'CA-2278751-A1', 'JP-2005104983-A', 'US-2009031436-A1', 'CA-3161617-A1', 'US-2023155090-A1', 'US-2006292670-A1'], 'var_function-call-3824604485250573977': "SELECT Patents_info, cpc FROM publicationinfo WHERE (citation LIKE '%US-2023171142-A1%' OR citation LIKE '%CN-103687626-A%' OR citation LIKE '%US-2021181673-A1%' OR citation LIKE '%AU-2003297741-A1%' OR citation LIKE '%AP-3334-A%' OR citation LIKE '%IL-274176-A%' OR citation LIKE '%US-11960018-B2%' OR citation LIKE '%WO-2019173834-A1%' OR citation LIKE '%IL-244029-A0%' OR citation LIKE '%US-10900049-B2%' OR citation LIKE '%CA-2220674-A1%' OR citation LIKE '%BR-112021021092-A8%' OR citation LIKE '%WO-2023225482-A3%' OR citation LIKE '%US-2017145219-A1%' OR citation LIKE '%KR-20200041324-A%' OR citation LIKE '%US-12025581-B2%' OR citation LIKE '%ZA-200802422-B%' OR citation LIKE '%CN-100339724-C%' OR citation LIKE '%WO-2024050335-A2%' OR citation LIKE '%FR-2194760-A1%' OR citation LIKE '%RO-70061-A%' OR citation LIKE '%EP-3668487-A4%' OR citation LIKE '%TW-201925402-A%' OR citation LIKE '%US-11014955-B2%' OR citation LIKE '%JP-S6163700-A%' OR citation LIKE '%AU-6535890-A%' OR citation LIKE '%HK-1052178-A1%' OR citation LIKE '%AU-2019275518-B2%' OR citation LIKE '%WO-2020096950-A1%' OR citation LIKE '%WO-2019067860-A1%' OR citation LIKE '%KR-20160119166-A%' OR citation LIKE '%AU-2005269556-A1%' OR citation LIKE '%CN-102067370-B%' OR citation LIKE '%US-6750960-B2%' OR citation LIKE '%WO-2023239670-A1%' OR citation LIKE '%US-11376346-B2%' OR citation LIKE '%US-10359432-B2%' OR citation LIKE '%US-11072681-B2%' OR citation LIKE '%JP-2014224156-A%' OR citation LIKE '%CN-103237558-A%' OR citation LIKE '%US-11607427-B2%' OR citation LIKE '%AU-7724398-A%' OR citation LIKE '%WO-2014152660-A1%' OR citation LIKE '%US-11445941-B2%' OR citation LIKE '%US-2021039104-A1%' OR citation LIKE '%US-2005136639-A1%' OR citation LIKE '%CN-103189548-A%' OR citation LIKE '%US-2022018060-A1%' OR citation LIKE '%US-2022074631-A1%' OR citation LIKE '%EP-2029921-A4%' OR citation LIKE '%US-2017294981-A1%' OR citation LIKE '%US-2023321419-A1%' OR citation LIKE '%EP-4284234-A1%' OR citation LIKE '%JP-2009260386-A%' OR citation LIKE '%KR-20110004413-A%' OR citation LIKE '%US-6237292-B1%' OR citation LIKE '%WO-2017214343-A1%' OR citation LIKE '%US-2006051790-A1%' OR citation LIKE '%WO-2012158833-A3%' OR citation LIKE '%IL-236725-A%' OR citation LIKE '%MX-2013002850-A%' OR citation LIKE '%US-2021282642-A1%' OR citation LIKE '%US-2019328740-A1%' OR citation LIKE '%WO-2020055916-A9%' OR citation LIKE '%AU-2898989-A%' OR citation LIKE '%US-2019169580-A1%' OR citation LIKE '%AU-2003247814-A1%' OR citation LIKE '%AU-2001296493-B2%' OR citation LIKE '%EP-3866867-A1%' OR citation LIKE '%US-6980295-B2%' OR citation LIKE '%WO-2021102420-A1%' OR citation LIKE '%US-2023314781-A1%' OR citation LIKE '%US-6030830-A%' OR citation LIKE '%US-5304932-A%' OR citation LIKE '%KR-20050085437-A%' OR citation LIKE '%US-8361933-B2%' OR citation LIKE '%US-2018304537-A1%' OR citation LIKE '%US-5547866-A%' OR citation LIKE '%WO-2010045542-A3%' OR citation LIKE '%CA-2550552-A1%' OR citation LIKE '%AU-2001257114-A1%' OR citation LIKE '%CA-3027364-A1%' OR citation LIKE '%WO-2018026404-A3%' OR citation LIKE '%KR-100228821-B1%' OR citation LIKE '%WO-2018152537-A1%' OR citation LIKE '%US-2017281687-A1%' OR citation LIKE '%US-11546022-B2%' OR citation LIKE '%CA-2298540-A1%' OR citation LIKE '%US-2021000566-A1%' OR citation LIKE '%WO-2024044766-A3%' OR citation LIKE '%HR-P20201231-T1%' OR citation LIKE '%US-2005234013-A1%' OR citation LIKE '%US-11421276-B2%' OR citation LIKE '%US-7052856-B2%' OR citation LIKE '%US-2017050153-A1%' OR citation LIKE '%US-2022123166-A1%' OR citation LIKE '%IL-140140-A0%' OR citation LIKE '%AU-2008329628-B2%' OR citation LIKE '%CN-101584047-A%' OR citation LIKE '%US-2018348310-A1%' OR citation LIKE '%US-10744347-B2%' OR citation LIKE '%AU-2004253879-A1%' OR citation LIKE '%US-2004115131-A1%' OR citation LIKE '%US-2018277766-A1%' OR citation LIKE '%US-11667770-B2%' OR citation LIKE '%AU-2008349842-A1%' OR citation LIKE '%CN-1120376-C%' OR citation LIKE '%CA-2283629-C%' OR citation LIKE '%US-2018243924-A1%' OR citation LIKE '%KR-20200084864-A%' OR citation LIKE '%KR-20080078049-A%' OR citation LIKE '%US-2018080022-A1%' OR citation LIKE '%AU-5938296-A%' OR citation LIKE '%US-3842373-A%' OR citation LIKE '%WO-2022178138-A1%' OR citation LIKE '%US-2021101879-A1%' OR citation LIKE '%CA-2562038-C%' OR citation LIKE '%US-2023340506-A1%' OR citation LIKE '%US-2017369950-A1%' OR citation LIKE '%US-2019209590-A1%' OR citation LIKE '%CA-3055214-A1%' OR citation LIKE '%PE-20130764-A1%' OR citation LIKE '%AU-2017356943-A1%' OR citation LIKE '%CN-102584712-A%' OR citation LIKE '%US-9061071-B2%' OR citation LIKE '%HK-1250569-A1%' OR citation LIKE '%US-2020283856-A1%' OR citation LIKE '%AU-2015364602-B2%' OR citation LIKE '%AU-2002254753-B2%' OR citation LIKE '%WO-2024112568-A1%' OR citation LIKE '%KR-20180041236-A%' OR citation LIKE '%US-2017087258-A1%' OR citation LIKE '%EP-1224461-B1%' OR citation LIKE '%US-11248107-B2%' OR citation LIKE '%ID-23426-A%' OR citation LIKE '%AU-2007297661-A1%' OR citation LIKE '%WO-2012162563-A2%' OR citation LIKE '%BR-9610580-A%' OR citation LIKE '%US-3666017-A%' OR citation LIKE '%US-2020025859-A1%' OR citation LIKE '%US-10765865-B2%' OR citation LIKE '%US-2023279470-A1%' OR citation LIKE '%US-2017194630-A1%' OR citation LIKE '%PT-2970346-T%' OR citation LIKE '%AU-3353000-A%' OR citation LIKE '%US-2008047008-A1%' OR citation LIKE '%US-2003112494-A1%' OR citation LIKE '%AU-2010214112-B2%' OR citation LIKE '%US-2010025717-A1%' OR citation LIKE '%US-10337029-B2%' OR citation LIKE '%EP-0826155-A4%' OR citation LIKE '%AU-5366398-A%' OR citation LIKE '%EP-2210307-A4%' OR citation LIKE '%CA-3225295-A1%' OR citation LIKE '%WO-2018067976-A1%' OR citation LIKE '%AU-2409401-A%' OR citation LIKE '%US-7745569-B2%' OR citation LIKE '%EP-1212462-A1%' OR citation LIKE '%US-2021002329-A1%' OR citation LIKE '%CA-2718348-C%' OR citation LIKE '%WO-2023212447-A2%' OR citation LIKE '%WO-2017136335-A1%' OR citation LIKE '%US-6767662-B2%' OR citation LIKE '%CA-2278751-A1%' OR citation LIKE '%JP-2005104983-A%' OR citation LIKE '%US-2009031436-A1%' OR citation LIKE '%CA-3161617-A1%' OR citation LIKE '%US-2023155090-A1%' OR citation LIKE '%US-2006292670-A1%') AND Patents_info NOT LIKE '%UNIV CALIFORNIA%'", 'var_function-call-15614453151447692542': 'file_storage/function-call-15614453151447692542.json'}

exec(code, env_args)

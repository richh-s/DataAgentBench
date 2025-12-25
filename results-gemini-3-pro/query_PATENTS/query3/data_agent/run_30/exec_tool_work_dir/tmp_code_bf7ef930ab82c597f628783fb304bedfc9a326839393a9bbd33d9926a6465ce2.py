code = """import json
import re

file_path = locals()['var_function-call-14120595499668642054']
with open(file_path, 'r') as f:
    records = json.load(f)

# Patterns for assignee extraction
# 1. Start with "X holds the ..."
# 2. "is assigned to X and"
# 3. "is held by X and"
# 4. "is owned by X and"
# 5. "is belonging to X and"

# We can try to capture the assignee name.
# Note: Assignee names are usually uppercase.

patterns = [
    re.compile(r'^(.+?)\s+holds\s+the', re.IGNORECASE),
    re.compile(r'is\s+assigned\s+to\s+(.+?)\s+and', re.IGNORECASE),
    re.compile(r'is\s+held\s+by\s+(.+?)\s+and', re.IGNORECASE),
    re.compile(r'is\s+owned\s+by\s+(.+?)\s+and', re.IGNORECASE),
    re.compile(r'is\s+belonging\s+to\s+(.+?)\s+and', re.IGNORECASE)
]

results = []
subclasses_needed = set()

for rec in records:
    text = rec['Patents_info']
    cpc_json = rec.get('cpc')
    
    # Extract assignee
    assignee = None
    for p in patterns:
        m = p.search(text)
        if m:
            assignee = m.group(1).strip()
            break
            
    if not assignee:
        # Fallback or skip?
        # Maybe check for "In COUNTRY, the application ... is owned by X"
        # The patterns above cover "... is owned by X" which matches "In US... is owned by X" part?
        # No, search scans the string.
        pass
        
    if assignee:
        # Clean up assignee
        # Sometimes it might capture "In US, the application ... is owned by X".
        # If the pattern is "is owned by X and", group 1 is X.
        # But if the sentence is "The US app... is owned by X and has...", X is clear.
        pass

    if assignee and "UNIV CALIFORNIA" not in assignee.upper():
        # Get CPC
        primary_subclass = None
        if cpc_json:
            try:
                cpcs = json.loads(cpc_json)
                # Find first=true or take the first one
                target_code = None
                for c in cpcs:
                    if c.get('first') == True:
                        target_code = c.get('code')
                        break
                if not target_code and cpcs:
                    target_code = cpcs[0].get('code')
                
                if target_code:
                    # Subclass is first 4 chars
                    primary_subclass = target_code[:4]
            except:
                pass
        
        if primary_subclass:
            results.append({"assignee": assignee, "subclass": primary_subclass})
            subclasses_needed.add(primary_subclass)

print("__RESULT__:")
print(json.dumps({"subclasses": list(subclasses_needed), "pairs": results}))"""

env_args = {'var_function-call-10219217939531251001': ['publicationinfo'], 'var_function-call-10219217939531249342': 'file_storage/function-call-10219217939531249342.json', 'var_function-call-17419786939920871322': [{'count(*)': '277813'}], 'var_function-call-17419786939920868423': [{'count(*)': '169'}], 'var_function-call-6583670479369406734': 'file_storage/function-call-6583670479369406734.json', 'var_function-call-8361809641763554423': "SELECT Patents_info, cpc FROM publicationinfo WHERE citation LIKE '%CA-2278751-A1%' OR citation LIKE '%AU-2004253879-A1%' OR citation LIKE '%IL-140140-A0%' OR citation LIKE '%WO-2024112568-A1%' OR citation LIKE '%US-2022018060-A1%' OR citation LIKE '%IL-244029-A0%' OR citation LIKE '%KR-20050085437-A%' OR citation LIKE '%US-3842373-A%' OR citation LIKE '%CN-103189548-A%' OR citation LIKE '%AU-2008329628-B2%' OR citation LIKE '%HR-P20201231-T1%' OR citation LIKE '%WO-2024050335-A2%' OR citation LIKE '%US-2020283856-A1%' OR citation LIKE '%KR-20160119166-A%' OR citation LIKE '%CA-2298540-A1%' OR citation LIKE '%US-11248107-B2%' OR citation LIKE '%CN-1120376-C%' OR citation LIKE '%US-2005136639-A1%' OR citation LIKE '%CA-3161617-A1%' OR citation LIKE '%CA-3225295-A1%' OR citation LIKE '%CA-3055214-A1%' OR citation LIKE '%KR-100228821-B1%' OR citation LIKE '%IL-274176-A%' OR citation LIKE '%AU-2001257114-A1%' OR citation LIKE '%US-2023279470-A1%' OR citation LIKE '%JP-2014224156-A%' OR citation LIKE '%WO-2024044766-A3%' OR citation LIKE '%AP-3334-A%' OR citation LIKE '%TW-201925402-A%' OR citation LIKE '%AU-2898989-A%' OR citation LIKE '%RO-70061-A%' OR citation LIKE '%US-2018080022-A1%' OR citation LIKE '%US-2023314781-A1%' OR citation LIKE '%US-2017050153-A1%' OR citation LIKE '%EP-1224461-B1%' OR citation LIKE '%US-10337029-B2%' OR citation LIKE '%AU-5938296-A%' OR citation LIKE '%US-2008047008-A1%' OR citation LIKE '%WO-2017214343-A1%' OR citation LIKE '%US-10744347-B2%' OR citation LIKE '%IL-236725-A%' OR citation LIKE '%WO-2018152537-A1%' OR citation LIKE '%AU-2005269556-A1%' OR citation LIKE '%US-2003112494-A1%' OR citation LIKE '%AU-2008349842-A1%' OR citation LIKE '%AU-2003247814-A1%' OR citation LIKE '%FR-2194760-A1%' OR citation LIKE '%US-2021101879-A1%' OR citation LIKE '%EP-2210307-A4%' OR citation LIKE '%US-6750960-B2%' OR citation LIKE '%US-2021000566-A1%' OR citation LIKE '%US-2021002329-A1%' OR citation LIKE '%US-2010025717-A1%' OR citation LIKE '%US-5547866-A%' OR citation LIKE '%US-2022123166-A1%' OR citation LIKE '%HK-1052178-A1%' OR citation LIKE '%WO-2023212447-A2%' OR citation LIKE '%MX-2013002850-A%' OR citation LIKE '%US-2009031436-A1%' OR citation LIKE '%KR-20080078049-A%' OR citation LIKE '%US-2006051790-A1%' OR citation LIKE '%CA-2562038-C%' OR citation LIKE '%US-11445941-B2%' OR citation LIKE '%WO-2019067860-A1%' OR citation LIKE '%AU-2010214112-B2%' OR citation LIKE '%AU-2002254753-B2%' OR citation LIKE '%US-11667770-B2%' OR citation LIKE '%US-2018243924-A1%' OR citation LIKE '%WO-2018026404-A3%' OR citation LIKE '%ID-23426-A%' OR citation LIKE '%AU-2019275518-B2%' OR citation LIKE '%CA-3027364-A1%' OR citation LIKE '%US-11421276-B2%' OR citation LIKE '%US-7745569-B2%' OR citation LIKE '%EP-2029921-A4%' OR citation LIKE '%US-2017294981-A1%' OR citation LIKE '%US-2020025859-A1%' OR citation LIKE '%CN-103237558-A%' OR citation LIKE '%US-10900049-B2%' OR citation LIKE '%US-2023340506-A1%' OR citation LIKE '%US-2005234013-A1%' OR citation LIKE '%US-11546022-B2%' OR citation LIKE '%WO-2022178138-A1%' OR citation LIKE '%US-2021282642-A1%' OR citation LIKE '%WO-2020055916-A9%' OR citation LIKE '%PT-2970346-T%' OR citation LIKE '%US-2017281687-A1%' OR citation LIKE '%AU-2015364602-B2%' OR citation LIKE '%US-9061071-B2%' OR citation LIKE '%US-2018304537-A1%' OR citation LIKE '%US-2019328740-A1%' OR citation LIKE '%EP-0826155-A4%' OR citation LIKE '%JP-S6163700-A%' OR citation LIKE '%AU-2001296493-B2%' OR citation LIKE '%WO-2014152660-A1%' OR citation LIKE '%KR-20110004413-A%' OR citation LIKE '%US-2023155090-A1%' OR citation LIKE '%US-11014955-B2%' OR citation LIKE '%AU-6535890-A%' OR citation LIKE '%JP-2009260386-A%' OR citation LIKE '%US-2017194630-A1%' OR citation LIKE '%WO-2023239670-A1%' OR citation LIKE '%US-2023321419-A1%' OR citation LIKE '%WO-2020096950-A1%' OR citation LIKE '%CA-2718348-C%' OR citation LIKE '%US-5304932-A%' OR citation LIKE '%US-2017369950-A1%' OR citation LIKE '%CN-100339724-C%' OR citation LIKE '%WO-2018067976-A1%' OR citation LIKE '%US-2006292670-A1%' OR citation LIKE '%CN-102067370-B%' OR citation LIKE '%BR-9610580-A%' OR citation LIKE '%AU-2003297741-A1%' OR citation LIKE '%CA-2550552-A1%' OR citation LIKE '%US-2022074631-A1%' OR citation LIKE '%US-6237292-B1%' OR citation LIKE '%BR-112021021092-A8%' OR citation LIKE '%US-2019209590-A1%' OR citation LIKE '%US-2018277766-A1%' OR citation LIKE '%US-2017145219-A1%' OR citation LIKE '%US-2019169580-A1%' OR citation LIKE '%US-2021039104-A1%' OR citation LIKE '%EP-1212462-A1%' OR citation LIKE '%CA-2220674-A1%' OR citation LIKE '%CN-103687626-A%' OR citation LIKE '%US-11607427-B2%' OR citation LIKE '%US-6980295-B2%' OR citation LIKE '%WO-2021102420-A1%' OR citation LIKE '%WO-2019173834-A1%' OR citation LIKE '%US-8361933-B2%' OR citation LIKE '%US-6767662-B2%' OR citation LIKE '%WO-2012162563-A2%' OR citation LIKE '%US-2021181673-A1%' OR citation LIKE '%US-12025581-B2%' OR citation LIKE '%AU-5366398-A%' OR citation LIKE '%EP-3866867-A1%' OR citation LIKE '%WO-2010045542-A3%' OR citation LIKE '%US-6030830-A%' OR citation LIKE '%CN-102584712-A%' OR citation LIKE '%AU-2007297661-A1%' OR citation LIKE '%WO-2017136335-A1%' OR citation LIKE '%US-2004115131-A1%' OR citation LIKE '%ZA-200802422-B%' OR citation LIKE '%EP-4284234-A1%' OR citation LIKE '%AU-2409401-A%' OR citation LIKE '%US-2017087258-A1%' OR citation LIKE '%US-10765865-B2%' OR citation LIKE '%CA-2283629-C%' OR citation LIKE '%US-3666017-A%' OR citation LIKE '%US-11072681-B2%' OR citation LIKE '%KR-20200041324-A%' OR citation LIKE '%KR-20180041236-A%' OR citation LIKE '%US-2018348310-A1%' OR citation LIKE '%EP-3668487-A4%' OR citation LIKE '%US-7052856-B2%' OR citation LIKE '%PE-20130764-A1%' OR citation LIKE '%US-11376346-B2%' OR citation LIKE '%US-10359432-B2%' OR citation LIKE '%CN-101584047-A%' OR citation LIKE '%US-11960018-B2%' OR citation LIKE '%WO-2012158833-A3%' OR citation LIKE '%WO-2023225482-A3%' OR citation LIKE '%HK-1250569-A1%' OR citation LIKE '%AU-2017356943-A1%' OR citation LIKE '%US-2023171142-A1%' OR citation LIKE '%JP-2005104983-A%' OR citation LIKE '%AU-3353000-A%' OR citation LIKE '%AU-7724398-A%' OR citation LIKE '%KR-20200084864-A%'", 'var_function-call-14120595499668642054': 'file_storage/function-call-14120595499668642054.json'}

exec(code, env_args)

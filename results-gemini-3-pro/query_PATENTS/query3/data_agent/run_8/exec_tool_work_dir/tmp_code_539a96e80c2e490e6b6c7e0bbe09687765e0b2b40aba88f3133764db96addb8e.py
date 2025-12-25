code = """import json

citing_patents_file = locals()['var_function-call-9403066083909934711']
with open(citing_patents_file, 'r') as f:
    citing_data = json.load(f)

print(f"Total citing records loaded: {len(citing_data)}")

# Re-run extraction to get all assignee-subclass pairs
results = []
subclasses = set()
import re

for record in citing_data:
    info = record['Patents_info']
    cpc_json = record['cpc']
    
    assignee = None
    # Regex patterns
    # 1. "X holds the" (X is at start)
    m = re.match(r"^(.*?) holds the", info)
    if m:
        assignee = m.group(1).strip()
    
    # 2. "is assigned to X and"
    if not assignee:
        m = re.search(r"is assigned to (.*?) and", info)
        if m:
            assignee = m.group(1).strip()
            
    # 3. "is held by X and"
    if not assignee:
        m = re.search(r"is held by (.*?) and", info)
        if m:
            assignee = m.group(1).strip()

    # 4. "is owned by X and"
    if not assignee:
        m = re.search(r"is owned by (.*?) and", info)
        if m:
            assignee = m.group(1).strip()

    # 5. "is belonging to X and"
    if not assignee:
        m = re.search(r"is belonging to (.*?) and", info)
        if m:
            assignee = m.group(1).strip()
            
    # 6. "held by X, with"
    if not assignee:
        m = re.search(r"held by (.*?), with", info)
        if m:
            assignee = m.group(1).strip()
            
    # 7. "owned by X, with"
    if not assignee:
        m = re.search(r"owned by (.*?), with", info)
        if m:
            assignee = m.group(1).strip()
            
    # 8. "belonging to X, with"
    if not assignee:
        m = re.search(r"belonging to (.*?), with", info)
        if m:
            assignee = m.group(1).strip()
    
    # 9. "assigned to X, with"
    if not assignee:
        m = re.search(r"assigned to (.*?), with", info)
        if m:
            assignee = m.group(1).strip()

    # Extract CPC Subclass
    primary_subclass = None
    try:
        cpc_list = json.loads(cpc_json)
        # Find first: true
        for item in cpc_list:
            if item.get('first') is True:
                code = item.get('code', '')
                if len(code) >= 4:
                    primary_subclass = code[:4]
                    break
        if not primary_subclass and cpc_list:
            # Fallback to first item
            code = cpc_list[0].get('code', '')
            if len(code) >= 4:
                primary_subclass = code[:4]
    except:
        pass
        
    if assignee and primary_subclass:
        if "UNIV CALIFORNIA" not in assignee:
             results.append({"assignee": assignee, "subclass": primary_subclass})
             subclasses.add(primary_subclass)

print(f"Extracted {len(results)} valid records.")
print(f"Unique subclasses: {list(subclasses)}")

print("__RESULT__:")
print(json.dumps({"subclasses": list(subclasses), "results": results}))"""

env_args = {'var_function-call-2230089444077976184': 'file_storage/function-call-2230089444077976184.json', 'var_function-call-18167531083137253587': 'file_storage/function-call-18167531083137253587.json', 'var_function-call-6822804333576179424': [{'COUNT(*)': '277813'}], 'var_function-call-5873971824289242254': ['US-2022074631-A1', 'US-7052856-B2', 'CN-102584712-A', 'AU-2004253879-A1', 'WO-2021102420-A1', 'US-3842373-A', 'WO-2020055916-A9', 'AU-2002254753-B2', 'WO-2022178138-A1', 'FR-2194760-A1', 'IL-274176-A', 'CA-2550552-A1', 'WO-2017214343-A1', 'WO-2019173834-A1', 'KR-20080078049-A', 'US-2018277766-A1', 'US-2023321419-A1', 'US-2009031436-A1', 'PT-2970346-T', 'US-6767662-B2', 'AU-5366398-A', 'CN-1120376-C', 'US-2005136639-A1', 'WO-2024112568-A1', 'KR-20050085437-A', 'US-6030830-A', 'US-3666017-A', 'CA-3055214-A1', 'EP-1212462-A1', 'CN-102067370-B', 'EP-0826155-A4', 'US-11546022-B2', 'EP-2029921-A4', 'AU-3353000-A', 'KR-20200084864-A', 'AU-7724398-A', 'AU-2003297741-A1', 'EP-3668487-A4', 'US-11421276-B2', 'US-2017194630-A1', 'US-2023279470-A1', 'CN-103237558-A', 'CA-2278751-A1', 'US-2006051790-A1', 'US-2010025717-A1', 'US-11667770-B2', 'CN-103687626-A', 'US-12025581-B2', 'CA-3161617-A1', 'WO-2018152537-A1', 'JP-2009260386-A', 'US-2018348310-A1', 'US-2004115131-A1', 'US-10337029-B2', 'BR-9610580-A', 'US-2018080022-A1', 'BR-112021021092-A8', 'ID-23426-A', 'JP-2014224156-A', 'AP-3334-A', 'CA-2562038-C', 'US-11248107-B2', 'US-2021000566-A1', 'RO-70061-A', 'US-10359432-B2', 'AU-6535890-A', 'US-2006292670-A1', 'US-10765865-B2', 'MX-2013002850-A', 'AU-2017356943-A1', 'AU-2898989-A', 'JP-S6163700-A', 'AU-2008349842-A1', 'HR-P20201231-T1', 'WO-2023239670-A1', 'US-2017145219-A1', 'CA-2298540-A1', 'KR-20160119166-A', 'US-2005234013-A1', 'US-5547866-A', 'AU-2409401-A', 'CA-2283629-C', 'TW-201925402-A', 'US-2017281687-A1', 'AU-2015364602-B2', 'US-11445941-B2', 'US-6237292-B1', 'AU-5938296-A', 'US-10744347-B2', 'CN-100339724-C', 'JP-2005104983-A', 'CN-103189548-A', 'CA-2220674-A1', 'US-2003112494-A1', 'AU-2010214112-B2', 'IL-236725-A', 'EP-4284234-A1', 'US-2021101879-A1', 'CA-3027364-A1', 'EP-1224461-B1', 'US-11072681-B2', 'US-2022018060-A1', 'WO-2023225482-A3', 'US-2021181673-A1', 'EP-3866867-A1', 'ZA-200802422-B', 'US-2020283856-A1', 'AU-2008329628-B2', 'US-8361933-B2', 'WO-2014152660-A1', 'US-2023314781-A1', 'WO-2018026404-A3', 'US-2017087258-A1', 'KR-20180041236-A', 'AU-2001257114-A1', 'WO-2019067860-A1', 'WO-2024050335-A2', 'IL-244029-A0', 'US-5304932-A', 'KR-20110004413-A', 'US-11960018-B2', 'WO-2012162563-A2', 'KR-100228821-B1', 'US-2023340506-A1', 'WO-2024044766-A3', 'WO-2020096950-A1', 'AU-2007297661-A1', 'CA-2718348-C', 'US-2019209590-A1', 'US-7745569-B2', 'US-2017294981-A1', 'WO-2010045542-A3', 'KR-20200041324-A', 'US-2021002329-A1', 'WO-2018067976-A1', 'US-11607427-B2', 'AU-2005269556-A1', 'US-11376346-B2', 'US-2021282642-A1', 'US-2019169580-A1', 'US-9061071-B2', 'US-10900049-B2', 'WO-2023212447-A2', 'HK-1052178-A1', 'US-6980295-B2', 'CN-101584047-A', 'US-2021039104-A1', 'IL-140140-A0', 'US-11014955-B2', 'AU-2003247814-A1', 'PE-20130764-A1', 'US-2023155090-A1', 'US-2020025859-A1', 'US-2023171142-A1', 'US-2018243924-A1', 'US-2018304537-A1', 'US-2008047008-A1', 'US-2019328740-A1', 'WO-2012158833-A3', 'EP-2210307-A4', 'US-2017369950-A1', 'US-6750960-B2', 'AU-2001296493-B2', 'HK-1250569-A1', 'CA-3225295-A1', 'WO-2017136335-A1', 'US-2017050153-A1', 'AU-2019275518-B2', 'US-2022123166-A1'], 'var_function-call-9456846015663124932': "SELECT Patents_info, cpc FROM publicationinfo WHERE Patents_info NOT LIKE '%UNIV CALIFORNIA%' AND (citation LIKE '%US-2022074631-A1%' OR citation LIKE '%US-7052856-B2%' OR citation LIKE '%CN-102584712-A%' OR citation LIKE '%AU-2004253879-A1%' OR citation LIKE '%WO-2021102420-A1%' OR citation LIKE '%US-3842373-A%' OR citation LIKE '%WO-2020055916-A9%' OR citation LIKE '%AU-2002254753-B2%' OR citation LIKE '%WO-2022178138-A1%' OR citation LIKE '%FR-2194760-A1%' OR citation LIKE '%IL-274176-A%' OR citation LIKE '%CA-2550552-A1%' OR citation LIKE '%WO-2017214343-A1%' OR citation LIKE '%WO-2019173834-A1%' OR citation LIKE '%KR-20080078049-A%' OR citation LIKE '%US-2018277766-A1%' OR citation LIKE '%US-2023321419-A1%' OR citation LIKE '%US-2009031436-A1%' OR citation LIKE '%PT-2970346-T%' OR citation LIKE '%US-6767662-B2%' OR citation LIKE '%AU-5366398-A%' OR citation LIKE '%CN-1120376-C%' OR citation LIKE '%US-2005136639-A1%' OR citation LIKE '%WO-2024112568-A1%' OR citation LIKE '%KR-20050085437-A%' OR citation LIKE '%US-6030830-A%' OR citation LIKE '%US-3666017-A%' OR citation LIKE '%CA-3055214-A1%' OR citation LIKE '%EP-1212462-A1%' OR citation LIKE '%CN-102067370-B%' OR citation LIKE '%EP-0826155-A4%' OR citation LIKE '%US-11546022-B2%' OR citation LIKE '%EP-2029921-A4%' OR citation LIKE '%AU-3353000-A%' OR citation LIKE '%KR-20200084864-A%' OR citation LIKE '%AU-7724398-A%' OR citation LIKE '%AU-2003297741-A1%' OR citation LIKE '%EP-3668487-A4%' OR citation LIKE '%US-11421276-B2%' OR citation LIKE '%US-2017194630-A1%' OR citation LIKE '%US-2023279470-A1%' OR citation LIKE '%CN-103237558-A%' OR citation LIKE '%CA-2278751-A1%' OR citation LIKE '%US-2006051790-A1%' OR citation LIKE '%US-2010025717-A1%' OR citation LIKE '%US-11667770-B2%' OR citation LIKE '%CN-103687626-A%' OR citation LIKE '%US-12025581-B2%' OR citation LIKE '%CA-3161617-A1%' OR citation LIKE '%WO-2018152537-A1%' OR citation LIKE '%JP-2009260386-A%' OR citation LIKE '%US-2018348310-A1%' OR citation LIKE '%US-2004115131-A1%' OR citation LIKE '%US-10337029-B2%' OR citation LIKE '%BR-9610580-A%' OR citation LIKE '%US-2018080022-A1%' OR citation LIKE '%BR-112021021092-A8%' OR citation LIKE '%ID-23426-A%' OR citation LIKE '%JP-2014224156-A%' OR citation LIKE '%AP-3334-A%' OR citation LIKE '%CA-2562038-C%' OR citation LIKE '%US-11248107-B2%' OR citation LIKE '%US-2021000566-A1%' OR citation LIKE '%RO-70061-A%' OR citation LIKE '%US-10359432-B2%' OR citation LIKE '%AU-6535890-A%' OR citation LIKE '%US-2006292670-A1%' OR citation LIKE '%US-10765865-B2%' OR citation LIKE '%MX-2013002850-A%' OR citation LIKE '%AU-2017356943-A1%' OR citation LIKE '%AU-2898989-A%' OR citation LIKE '%JP-S6163700-A%' OR citation LIKE '%AU-2008349842-A1%' OR citation LIKE '%HR-P20201231-T1%' OR citation LIKE '%WO-2023239670-A1%' OR citation LIKE '%US-2017145219-A1%' OR citation LIKE '%CA-2298540-A1%' OR citation LIKE '%KR-20160119166-A%' OR citation LIKE '%US-2005234013-A1%' OR citation LIKE '%US-5547866-A%' OR citation LIKE '%AU-2409401-A%' OR citation LIKE '%CA-2283629-C%' OR citation LIKE '%TW-201925402-A%' OR citation LIKE '%US-2017281687-A1%' OR citation LIKE '%AU-2015364602-B2%' OR citation LIKE '%US-11445941-B2%' OR citation LIKE '%US-6237292-B1%' OR citation LIKE '%AU-5938296-A%' OR citation LIKE '%US-10744347-B2%' OR citation LIKE '%CN-100339724-C%' OR citation LIKE '%JP-2005104983-A%' OR citation LIKE '%CN-103189548-A%' OR citation LIKE '%CA-2220674-A1%' OR citation LIKE '%US-2003112494-A1%' OR citation LIKE '%AU-2010214112-B2%' OR citation LIKE '%IL-236725-A%' OR citation LIKE '%EP-4284234-A1%' OR citation LIKE '%US-2021101879-A1%' OR citation LIKE '%CA-3027364-A1%' OR citation LIKE '%EP-1224461-B1%' OR citation LIKE '%US-11072681-B2%' OR citation LIKE '%US-2022018060-A1%' OR citation LIKE '%WO-2023225482-A3%' OR citation LIKE '%US-2021181673-A1%' OR citation LIKE '%EP-3866867-A1%' OR citation LIKE '%ZA-200802422-B%' OR citation LIKE '%US-2020283856-A1%' OR citation LIKE '%AU-2008329628-B2%' OR citation LIKE '%US-8361933-B2%' OR citation LIKE '%WO-2014152660-A1%' OR citation LIKE '%US-2023314781-A1%' OR citation LIKE '%WO-2018026404-A3%' OR citation LIKE '%US-2017087258-A1%' OR citation LIKE '%KR-20180041236-A%' OR citation LIKE '%AU-2001257114-A1%' OR citation LIKE '%WO-2019067860-A1%' OR citation LIKE '%WO-2024050335-A2%' OR citation LIKE '%IL-244029-A0%' OR citation LIKE '%US-5304932-A%' OR citation LIKE '%KR-20110004413-A%' OR citation LIKE '%US-11960018-B2%' OR citation LIKE '%WO-2012162563-A2%' OR citation LIKE '%KR-100228821-B1%' OR citation LIKE '%US-2023340506-A1%' OR citation LIKE '%WO-2024044766-A3%' OR citation LIKE '%WO-2020096950-A1%' OR citation LIKE '%AU-2007297661-A1%' OR citation LIKE '%CA-2718348-C%' OR citation LIKE '%US-2019209590-A1%' OR citation LIKE '%US-7745569-B2%' OR citation LIKE '%US-2017294981-A1%' OR citation LIKE '%WO-2010045542-A3%' OR citation LIKE '%KR-20200041324-A%' OR citation LIKE '%US-2021002329-A1%' OR citation LIKE '%WO-2018067976-A1%' OR citation LIKE '%US-11607427-B2%' OR citation LIKE '%AU-2005269556-A1%' OR citation LIKE '%US-11376346-B2%' OR citation LIKE '%US-2021282642-A1%' OR citation LIKE '%US-2019169580-A1%' OR citation LIKE '%US-9061071-B2%' OR citation LIKE '%US-10900049-B2%' OR citation LIKE '%WO-2023212447-A2%' OR citation LIKE '%HK-1052178-A1%' OR citation LIKE '%US-6980295-B2%' OR citation LIKE '%CN-101584047-A%' OR citation LIKE '%US-2021039104-A1%' OR citation LIKE '%IL-140140-A0%' OR citation LIKE '%US-11014955-B2%' OR citation LIKE '%AU-2003247814-A1%' OR citation LIKE '%PE-20130764-A1%' OR citation LIKE '%US-2023155090-A1%' OR citation LIKE '%US-2020025859-A1%' OR citation LIKE '%US-2023171142-A1%' OR citation LIKE '%US-2018243924-A1%' OR citation LIKE '%US-2018304537-A1%' OR citation LIKE '%US-2008047008-A1%' OR citation LIKE '%US-2019328740-A1%' OR citation LIKE '%WO-2012158833-A3%' OR citation LIKE '%EP-2210307-A4%' OR citation LIKE '%US-2017369950-A1%' OR citation LIKE '%US-6750960-B2%' OR citation LIKE '%AU-2001296493-B2%' OR citation LIKE '%HK-1250569-A1%' OR citation LIKE '%CA-3225295-A1%' OR citation LIKE '%WO-2017136335-A1%' OR citation LIKE '%US-2017050153-A1%' OR citation LIKE '%AU-2019275518-B2%' OR citation LIKE '%US-2022123166-A1%')", 'var_function-call-9403066083909934711': 'file_storage/function-call-9403066083909934711.json', 'var_function-call-6763954500062868455': {'subclasses': ['H01L', 'G01V', 'H01M', 'C30B'], 'records': [{'assignee': 'CALIFORNIA INST OF TECHN', 'subclass': 'G01V'}, {'assignee': 'BLOOM ENERGY CORP', 'subclass': 'H01M'}, {'assignee': 'CRYSTAL IS INC', 'subclass': 'C30B'}, {'assignee': 'SCHOWALTER LEO J', 'subclass': 'H01L'}]}}

exec(code, env_args)

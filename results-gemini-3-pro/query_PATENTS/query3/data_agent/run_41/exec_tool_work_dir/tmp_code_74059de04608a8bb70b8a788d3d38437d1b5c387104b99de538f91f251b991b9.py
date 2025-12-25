code = """import json
import re

uc_file_path = locals()['var_function-call-15762675750983783495']
with open(uc_file_path, 'r') as f:
    uc_records = json.load(f)

uc_pub_nums = set()
for rec in uc_records:
    # simple extraction
    parts = rec['Patents_info'].split('publication number ')
    if len(parts) > 1:
        num = parts[1].split(' ')[0].rstrip('.,')
        uc_pub_nums.add(num)
    else:
        parts = rec['Patents_info'].split('pub. number ')
        if len(parts) > 1:
            num = parts[1].split(' ')[0].rstrip('.,')
            uc_pub_nums.add(num)
        else:
             parts = rec['Patents_info'].split('publication no. ')
             if len(parts) > 1:
                 num = parts[1].split(' ')[0].rstrip('.,')
                 uc_pub_nums.add(num)

all_patents_path = locals()['var_function-call-3142653111375801446']
with open(all_patents_path, 'r') as f:
    all_patents = json.load(f)

results = []

def extract_assignee(text):
    text = text.replace('\n', ' ')
    # Case 1: Start with "X holds the"
    if ' holds the ' in text:
        return text.split(' holds the ')[0].strip()
    
    # Case 2: "is ... by X and/with"
    if ' by ' in text and (' and ' in text or ' with ' in text):
        start_idx = text.find(' by ') + 4
        end_idx = text.find(' and ', start_idx)
        if end_idx == -1: end_idx = text.find(' with ', start_idx)
        if end_idx != -1:
            return text[start_idx:end_idx].strip()
    
    # Case 3: "assigned to X and/with"
    if ' to ' in text and (' and ' in text or ' with ' in text):
        start_idx = text.find(' to ') + 4
        end_idx = text.find(' and ', start_idx)
        if end_idx == -1: end_idx = text.find(' with ', start_idx)
        if end_idx != -1:
            return text[start_idx:end_idx].strip()
            
    return None

for rec in all_patents:
    assignee = extract_assignee(rec['Patents_info'])
    if not assignee or "UNIV CALIFORNIA" in assignee:
        continue

    citations_str = rec.get('citation')
    if not citations_str or len(citations_str) < 5:
        continue
    
    try:
        citations = json.loads(citations_str)
    except:
        continue

    found = False
    for cit in citations:
        if cit.get('publication_number') in uc_pub_nums:
            found = True
            break
    
    if found:
        cpc_str = rec.get('cpc')
        subclass = ""
        if cpc_str and len(cpc_str) > 5:
            try:
                cpcs = json.loads(cpc_str)
                if cpcs and isinstance(cpcs, list) and len(cpcs) > 0:
                    code = cpcs[0].get('code')
                    if code and len(code) >= 4:
                        subclass = code[:4]
            except:
                pass
        
        if subclass:
            results.append({"assignee": assignee, "subclass": subclass})

# Deduplicate
unique = []
seen = set()
for r in results:
    k = (r['assignee'], r['subclass'])
    if k not in seen:
        seen.add(k)
        unique.append(r)

print("__RESULT__:")
print(json.dumps(unique))"""

env_args = {'var_function-call-4269469225090757360': 'file_storage/function-call-4269469225090757360.json', 'var_function-call-15762675750983783495': 'file_storage/function-call-15762675750983783495.json', 'var_function-call-1797959863285187110': [{'COUNT(*)': '277813'}], 'var_function-call-2253535946366971395': ['US-2018277766-A1', 'WO-2017214343-A1', 'WO-2018026404-A3', 'US-5547866-A', 'TW-201925402-A', 'JP-2014224156-A', 'US-2020283856-A1', 'AP-3334-A', 'AU-2005269556-A1', 'US-2006292670-A1', 'US-2009031436-A1', 'US-2023340506-A1', 'AU-5366398-A', 'CN-1120376-C', 'US-2019328740-A1', 'AU-2003297741-A1', 'AU-6535890-A', 'US-2022018060-A1', 'KR-20050085437-A', 'US-2018348310-A1', 'US-10744347-B2', 'WO-2023212447-A2', 'US-7745569-B2', 'ID-23426-A', 'US-2019169580-A1', 'CA-2283629-C', 'US-2003112494-A1', 'US-2021000566-A1', 'BR-9610580-A', 'US-11014955-B2', 'US-2005136639-A1', 'AU-7724398-A', 'US-2018304537-A1', 'US-6030830-A', 'WO-2020096950-A1', 'CA-3055214-A1', 'US-11607427-B2', 'US-8361933-B2', 'EP-3866867-A1', 'AU-2004253879-A1', 'US-2017281687-A1', 'KR-20160119166-A', 'AU-2003247814-A1', 'EP-1224461-B1', 'BR-112021021092-A8', 'EP-2029921-A4', 'US-2018080022-A1', 'WO-2012158833-A3', 'US-6750960-B2', 'WO-2018067976-A1', 'IL-274176-A', 'US-2017194630-A1', 'ZA-200802422-B', 'WO-2023239670-A1', 'WO-2019067860-A1', 'WO-2019173834-A1', 'US-6980295-B2', 'EP-4284234-A1', 'WO-2024112568-A1', 'EP-3668487-A4', 'JP-2005104983-A', 'US-5304932-A', 'US-2023279470-A1', 'CA-2550552-A1', 'CA-2220674-A1', 'US-11445941-B2', 'CA-3027364-A1', 'US-10900049-B2', 'CN-103189548-A', 'AU-2008329628-B2', 'US-2021039104-A1', 'KR-20200041324-A', 'AU-2001257114-A1', 'AU-2898989-A', 'HK-1250569-A1', 'US-6237292-B1', 'KR-20200084864-A', 'FR-2194760-A1', 'US-2022074631-A1', 'US-2017369950-A1', 'US-2004115131-A1', 'CA-2298540-A1', 'US-2021101879-A1', 'IL-236725-A', 'US-2023314781-A1', 'RO-70061-A', 'US-2023155090-A1', 'US-3666017-A', 'AU-2007297661-A1', 'PT-2970346-T', 'CN-101584047-A', 'WO-2017136335-A1', 'AU-3353000-A', 'US-2017050153-A1', 'US-2022123166-A1', 'AU-2409401-A', 'US-2006051790-A1', 'CN-103237558-A', 'US-11248107-B2', 'KR-20110004413-A', 'EP-1212462-A1', 'AU-2010214112-B2', 'US-10359432-B2', 'MX-2013002850-A', 'HK-1052178-A1', 'JP-2009260386-A', 'CN-102067370-B', 'IL-140140-A0', 'AU-2001296493-B2', 'HR-P20201231-T1', 'US-2019209590-A1', 'US-2021002329-A1', 'US-11421276-B2', 'US-12025581-B2', 'US-2023321419-A1', 'JP-S6163700-A', 'US-9061071-B2', 'WO-2022178138-A1', 'KR-20080078049-A', 'CA-2278751-A1', 'KR-100228821-B1', 'WO-2024050335-A2', 'US-2017087258-A1', 'US-11072681-B2', 'WO-2020055916-A9', 'CN-103687626-A', 'WO-2021102420-A1', 'US-2010025717-A1', 'CN-102584712-A', 'US-2017145219-A1', 'IL-244029-A0', 'EP-0826155-A4', 'US-2023171142-A1', 'CA-2562038-C', 'US-2008047008-A1', 'CA-3161617-A1', 'WO-2023225482-A3', 'US-2017294981-A1', 'US-6767662-B2', 'AU-2015364602-B2', 'US-11376346-B2', 'US-2021282642-A1', 'PE-20130764-A1', 'EP-2210307-A4', 'US-11546022-B2', 'US-10337029-B2', 'CA-3225295-A1', 'AU-2017356943-A1', 'US-7052856-B2', 'US-2018243924-A1', 'AU-2019275518-B2', 'US-2005234013-A1', 'CA-2718348-C', 'US-10765865-B2', 'AU-2002254753-B2', 'AU-2008349842-A1', 'AU-5938296-A', 'WO-2018152537-A1', 'US-11667770-B2', 'WO-2014152660-A1', 'US-3842373-A', 'WO-2010045542-A3', 'KR-20180041236-A', 'WO-2024044766-A3', 'US-11960018-B2', 'CN-100339724-C', 'US-2020025859-A1', 'WO-2012162563-A2', 'US-2021181673-A1'], 'var_function-call-3142653111375801446': 'file_storage/function-call-3142653111375801446.json'}

exec(code, env_args)

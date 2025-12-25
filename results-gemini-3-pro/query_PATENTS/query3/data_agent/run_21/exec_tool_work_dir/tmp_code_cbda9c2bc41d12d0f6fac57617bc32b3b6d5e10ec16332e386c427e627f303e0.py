code = """import json
import re

# Load UC patent numbers
uc_pub_nums_obj = locals()['var_function-call-5083934648255625172']
if isinstance(uc_pub_nums_obj, str):
    # Try to determine if it is a file path or json string
    if uc_pub_nums_obj.startswith('['):
        uc_pub_nums = set(json.loads(uc_pub_nums_obj))
    else:
        # Assume file path? Or check if it's a key?
        # If it's a file path, load it.
        try:
            with open(uc_pub_nums_obj, 'r') as f:
                uc_pub_nums = set(json.load(f))
        except:
             # Fallback, maybe it's just a string that looks like something else?
             uc_pub_nums = set()
elif isinstance(uc_pub_nums_obj, list):
    uc_pub_nums = set(uc_pub_nums_obj)
else:
    uc_pub_nums = set()

# Batch data
batch_file = locals()['var_function-call-13421429778795388183']
with open(batch_file, 'r') as f:
    batch_data = json.load(f)

results = []

pat1 = re.compile(r'^(.+?)\s+holds\s+the', re.IGNORECASE)
pat2 = re.compile(r'(?:belonging to|held by|owned by|assigned to)\s+([^,]+?)(?:,|\s+and\s|\s+with\s)', re.IGNORECASE)

def get_assignee(text):
    m1 = pat1.search(text)
    if m1:
        return m1.group(1).strip()
    m2 = pat2.search(text)
    if m2:
        return m2.group(1).strip()
    return None

for record in batch_data:
    p_info = record.get('Patents_info', '')
    if "UNIV CALIFORNIA" in p_info:
        continue
        
    cit_str = record.get('citation', '[]')
    try:
        cits = json.loads(cit_str)
    except:
        cits = []
    
    citing_match = False
    for c in cits:
        if c.get('publication_number') in uc_pub_nums:
            citing_match = True
            break
    
    if citing_match:
        assignee = get_assignee(p_info)
        if assignee and "UNIV CALIFORNIA" not in assignee:
            cpc_str = record.get('cpc', '[]')
            try:
                cpcs = json.loads(cpc_str)
            except:
                cpcs = []
            
            subclass = None
            for cpc in cpcs:
                if cpc.get('first'):
                    code = cpc.get('code', '')
                    if len(code) >= 4:
                        subclass = code[:4]
                    break
            if not subclass and cpcs:
                code = cpcs[0].get('code', '')
                if len(code) >= 4:
                    subclass = code[:4]

            if subclass:
                results.append({"assignee": assignee, "subclass": subclass})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-41443399722497184': 'file_storage/function-call-41443399722497184.json', 'var_function-call-398933142159382962': [{'count(*)': '277813'}], 'var_function-call-16171515325245813679': 'file_storage/function-call-16171515325245813679.json', 'var_function-call-1723883798483176096': ['US-3666017-A', 'IL-140140-A0', 'US-6030830-A', 'ID-23426-A', 'US-11445941-B2', 'US-10744347-B2', 'CN-103189548-A', 'EP-3668487-A4', 'WO-2012158833-A3', 'EP-2029921-A4'], 'var_function-call-5083934648255625172': ['FR-2194760-A1', 'KR-20050085437-A', 'US-2022018060-A1', 'US-2023171142-A1', 'AU-2001296493-B2', 'IL-274176-A', 'US-2021039104-A1', 'US-10900049-B2', 'PT-2970346-T', 'US-10744347-B2', 'JP-2014224156-A', 'AU-2010214112-B2', 'US-5547866-A', 'WO-2012162563-A2', 'US-2019209590-A1', 'KR-100228821-B1', 'WO-2018026404-A3', 'US-6980295-B2', 'US-2003112494-A1', 'AU-5938296-A', 'KR-20080078049-A', 'KR-20110004413-A', 'EP-3866867-A1', 'WO-2018067976-A1', 'AU-2898989-A', 'US-2017369950-A1', 'EP-4284234-A1', 'US-2023279470-A1', 'HK-1250569-A1', 'ID-23426-A', 'US-2010025717-A1', 'EP-2210307-A4', 'US-6750960-B2', 'AU-3353000-A', 'US-2004115131-A1', 'CN-100339724-C', 'IL-140140-A0', 'US-2021181673-A1', 'EP-3668487-A4', 'AU-2001257114-A1', 'AU-6535890-A', 'WO-2012158833-A3', 'EP-1224461-B1', 'AU-2017356943-A1', 'AU-2019275518-B2', 'CA-2278751-A1', 'WO-2017214343-A1', 'IL-244029-A0', 'US-2021282642-A1', 'PE-20130764-A1', 'EP-0826155-A4', 'US-9061071-B2', 'US-2018277766-A1', 'IL-236725-A', 'CN-101584047-A', 'WO-2024050335-A2', 'CN-103189548-A', 'CA-2550552-A1', 'HK-1052178-A1', 'WO-2017136335-A1', 'KR-20160119166-A', 'US-2018304537-A1', 'JP-S6163700-A', 'AU-2003297741-A1', 'CA-3161617-A1', 'WO-2021102420-A1', 'WO-2014152660-A1', 'US-11072681-B2', 'AU-2007297661-A1', 'US-2023321419-A1', 'AU-7724398-A', 'US-6030830-A', 'US-7052856-B2', 'CA-3055214-A1', 'US-8361933-B2', 'CA-2562038-C', 'US-12025581-B2', 'CA-2718348-C', 'WO-2020096950-A1', 'CN-102067370-B', 'US-2018243924-A1', 'MX-2013002850-A', 'US-3842373-A', 'AU-2015364602-B2', 'RO-70061-A', 'US-2019328740-A1', 'BR-112021021092-A8', 'US-2022074631-A1', 'KR-20200041324-A', 'US-2017050153-A1', 'US-2023155090-A1', 'US-2009031436-A1', 'WO-2023225482-A3', 'US-10765865-B2', 'US-11421276-B2', 'US-2017145219-A1', 'US-2023340506-A1', 'US-3666017-A', 'US-2021002329-A1', 'EP-1212462-A1', 'US-2023314781-A1', 'WO-2023212447-A2', 'TW-201925402-A', 'WO-2018152537-A1', 'US-11667770-B2', 'AU-2004253879-A1', 'US-2017281687-A1', 'KR-20200084864-A', 'US-11376346-B2', 'WO-2020055916-A9', 'US-6237292-B1', 'US-2017294981-A1', 'US-2017087258-A1', 'CA-2298540-A1', 'US-10359432-B2', 'CA-3225295-A1', 'US-10337029-B2', 'AU-2409401-A', 'AU-2008349842-A1', 'JP-2009260386-A', 'CN-102584712-A', 'KR-20180041236-A', 'US-2018348310-A1', 'WO-2024112568-A1', 'US-2008047008-A1', 'WO-2019067860-A1', 'US-11960018-B2', 'US-5304932-A', 'BR-9610580-A', 'AU-5366398-A', 'CN-103237558-A', 'CA-2220674-A1', 'US-11445941-B2', 'CA-2283629-C', 'US-2019169580-A1', 'WO-2023239670-A1', 'WO-2024044766-A3', 'US-2006292670-A1', 'US-2018080022-A1', 'EP-2029921-A4', 'JP-2005104983-A', 'US-2021000566-A1', 'US-2017194630-A1', 'CA-3027364-A1', 'US-2005136639-A1', 'US-11546022-B2', 'CN-103687626-A', 'US-2020283856-A1', 'WO-2022178138-A1', 'US-11014955-B2', 'US-11607427-B2', 'US-7745569-B2', 'US-6767662-B2', 'US-2005234013-A1', 'WO-2019173834-A1', 'WO-2010045542-A3', 'AP-3334-A', 'AU-2005269556-A1', 'US-2022123166-A1', 'HR-P20201231-T1', 'US-2020025859-A1', 'AU-2003247814-A1', 'CN-1120376-C', 'US-11248107-B2', 'AU-2008329628-B2', 'US-2006051790-A1', 'US-2021101879-A1', 'AU-2002254753-B2', 'ZA-200802422-B'], 'var_function-call-13421429778795388183': 'file_storage/function-call-13421429778795388183.json'}

exec(code, env_args)

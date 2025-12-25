code = """import json
import re
from collections import defaultdict

# Load UC patents
uc_file = locals()['var_function-call-13353732409083150801']
with open(uc_file, 'r') as f:
    uc_data = json.load(f)

pub_num_pattern = re.compile(r"publication no\.? ([\w-]+)\.?|pub\.? number ([\w-]+)\.?|publication number ([\w-]+)\.?")

uc_pub_nums = set()
for entry in uc_data:
    info = entry['Patents_info']
    match = pub_num_pattern.search(info)
    if match:
        p_num = next((g for g in match.groups() if g is not None), None)
        if p_num:
            uc_pub_nums.add(p_num.rstrip('.'))

# Load all patents
all_file = locals()['var_function-call-2194092693741157686']
with open(all_file, 'r') as f:
    all_data = json.load(f)

assignee_patterns = [
    re.compile(r"^(.*?) holds the"),
    re.compile(r"owned by (.*?),? with"),
    re.compile(r"owned by (.*?) and"),
    re.compile(r"assigned to (.*?),? with"),
    re.compile(r"assigned to (.*?) and"),
    re.compile(r"belonging to (.*?),? with"),
    re.compile(r"belonging to (.*?) and"),
    re.compile(r"held by (.*?),? with"),
    re.compile(r"held by (.*?) and"),
]

citing_info = []

for entry in all_data:
    pat_info = entry['Patents_info']
    
    # Extract Assignee
    assignee = None
    for p in assignee_patterns:
        m = p.search(pat_info)
        if m:
            val = m.group(1).strip()
            # If val contains comma, it might be "Company A, Company B" or "Company A, location".
            # Assuming the regex captures the name reasonable well.
            assignee = val
            break
    
    if not assignee and " holds the" in pat_info:
        assignee = pat_info.split(" holds the")[0].strip()

    if not assignee:
        continue

    # Exclude UNIV CALIFORNIA
    if "UNIV CALIFORNIA" in assignee:
        continue
    
    # Check citations
    try:
        citations = json.loads(entry['citation'])
    except:
        continue
        
    cited_nums = [c.get('publication_number') for c in citations if isinstance(c, dict) and c.get('publication_number')]
    
    if any(cn in uc_pub_nums for cn in cited_nums):
        try:
            cpc_list = json.loads(entry['cpc'])
        except:
            continue
            
        if cpc_list:
            # Handle list of dicts or list of strings
            primary = cpc_list[0]
            code = ""
            if isinstance(primary, dict):
                code = primary.get('code', '')
            elif isinstance(primary, str):
                code = primary
            
            if len(code) >= 4:
                subclass = code[:4]
                citing_info.append({"assignee": assignee, "subclass": subclass})

res_map = defaultdict(set)
for item in citing_info:
    res_map[item['assignee']].add(item['subclass'])

final_res = {k: list(v) for k, v in res_map.items()}

print("__RESULT__:")
print(json.dumps(final_res))"""

env_args = {'var_function-call-10578193635103741538': 'file_storage/function-call-10578193635103741538.json', 'var_function-call-13926955435789849247': [{'count(*)': '277813'}], 'var_function-call-13353732409083150801': 'file_storage/function-call-13353732409083150801.json', 'var_function-call-3737517469294994532': ['US-6237292-B1', 'US-6030830-A', 'WO-2023239670-A1', 'KR-20200041324-A', 'US-11014955-B2', 'CA-3225295-A1', 'CA-2550552-A1', 'US-2019169580-A1', 'US-2018348310-A1', 'US-10765865-B2', 'FR-2194760-A1', 'US-10359432-B2', 'KR-100228821-B1', 'US-12025581-B2', 'ID-23426-A', 'CA-3055214-A1', 'AU-3353000-A', 'US-11445941-B2', 'US-2023171142-A1', 'AU-2015364602-B2', 'JP-2014224156-A', 'WO-2024050335-A2', 'KR-20080078049-A', 'US-11960018-B2', 'US-2020283856-A1', 'AU-2898989-A', 'WO-2020096950-A1', 'US-2017281687-A1', 'CA-2298540-A1', 'CA-2718348-C', 'US-2018243924-A1', 'US-3666017-A', 'US-2022018060-A1', 'EP-2029921-A4', 'US-2010025717-A1', 'US-2017050153-A1', 'AU-2017356943-A1', 'US-2021282642-A1', 'IL-236725-A', 'US-2021000566-A1', 'AU-5938296-A', 'US-10900049-B2', 'AU-2003247814-A1', 'WO-2018067976-A1', 'WO-2024044766-A3', 'US-11421276-B2', 'WO-2017214343-A1', 'EP-2210307-A4', 'US-2021039104-A1', 'US-2008047008-A1', 'US-2018277766-A1', 'US-2018304537-A1', 'WO-2019173834-A1', 'US-2005136639-A1', 'CA-3161617-A1', 'CN-102067370-B', 'CN-101584047-A', 'US-2021002329-A1', 'WO-2014152660-A1', 'JP-S6163700-A', 'KR-20200084864-A', 'WO-2021102420-A1', 'AU-2008349842-A1', 'US-2023340506-A1', 'US-6767662-B2', 'US-2018080022-A1', 'CN-1120376-C', 'US-3842373-A', 'US-11376346-B2', 'KR-20180041236-A', 'AU-2007297661-A1', 'AU-2001257114-A1', 'US-2022074631-A1', 'WO-2023212447-A2', 'AU-6535890-A', 'US-2017087258-A1', 'US-6750960-B2', 'US-2017369950-A1', 'WO-2023225482-A3', 'CA-2278751-A1', 'US-2019209590-A1', 'ZA-200802422-B', 'US-9061071-B2', 'CA-2283629-C', 'US-2003112494-A1', 'AU-2019275518-B2', 'KR-20160119166-A', 'HK-1250569-A1', 'EP-1212462-A1', 'US-2006051790-A1', 'CN-102584712-A', 'HR-P20201231-T1', 'US-6980295-B2', 'US-2017145219-A1', 'IL-274176-A', 'JP-2005104983-A', 'US-2023155090-A1', 'US-2017294981-A1', 'IL-244029-A0', 'BR-112021021092-A8', 'MX-2013002850-A', 'US-10337029-B2', 'WO-2017136335-A1', 'US-11072681-B2', 'US-2021181673-A1', 'KR-20050085437-A', 'CN-100339724-C', 'AU-7724398-A', 'AU-2001296493-B2', 'WO-2018152537-A1', 'US-8361933-B2', 'US-5304932-A', 'US-2004115131-A1', 'WO-2019067860-A1', 'WO-2020055916-A9', 'JP-2009260386-A', 'US-2017194630-A1', 'US-2009031436-A1', 'US-10744347-B2', 'US-2005234013-A1', 'US-11667770-B2', 'AP-3334-A', 'US-11607427-B2', 'WO-2012158833-A3', 'US-2020025859-A1', 'EP-3866867-A1', 'WO-2012162563-A2', 'PT-2970346-T', 'AU-2005269556-A1', 'BR-9610580-A', 'WO-2018026404-A3', 'RO-70061-A', 'PE-20130764-A1', 'AU-2002254753-B2', 'US-2019328740-A1', 'CN-103189548-A', 'CA-3027364-A1', 'US-2021101879-A1', 'TW-201925402-A', 'EP-1224461-B1', 'EP-3668487-A4', 'AU-2008329628-B2', 'AU-2003297741-A1', 'US-2023279470-A1', 'US-7052856-B2', 'CA-2562038-C', 'CN-103687626-A', 'KR-20110004413-A', 'US-7745569-B2', 'WO-2010045542-A3', 'US-2023314781-A1', 'US-5547866-A', 'US-2022123166-A1', 'AU-5366398-A', 'CA-2220674-A1', 'AU-2409401-A', 'WO-2024112568-A1', 'AU-2010214112-B2', 'AU-2004253879-A1', 'US-2023321419-A1', 'EP-4284234-A1', 'US-11546022-B2', 'CN-103237558-A', 'WO-2022178138-A1', 'EP-0826155-A4', 'IL-140140-A0', 'HK-1052178-A1', 'US-2006292670-A1', 'US-11248107-B2'], 'var_function-call-2194092693741157686': 'file_storage/function-call-2194092693741157686.json'}

exec(code, env_args)

code = """import json
import re

# Load UC pub nums
uc_pub_nums_file = locals()['var_function-call-11457268664057568431']
# The previous result is a JSON string of a list
uc_pub_nums = set(json.loads(uc_pub_nums_file))

# Load citations data
citations_file = locals()['var_function-call-6584418003579723251']
with open(citations_file, 'r') as f:
    records = json.load(f)

found_records = []
# Regex for assignee extraction
assignee_patterns = [
    r"^(.*?) holds the",
    r"is owned by (.*?) and",
    r"is assigned to (.*?) and",
    r"belonging to (.*?) and",
    r"held by (.*?) and",
    r"held by (.*?),", # sometimes comma
]

def extract_assignee(text):
    for pat in assignee_patterns:
        match = re.search(pat, text, re.IGNORECASE)
        if match:
            # Clean up the assignee name
            name = match.group(1).strip()
            # sometimes the capture group might be too greedy or include "In US, ... " prefix
            # Example: "In US, the application ... is owned by X"
            # The regex "is owned by (.*?) and" should capture X.
            return name
    return None

cpc_subclasses = set()
results = []

for rec in records:
    # Check citations
    citations_str = rec.get('citation', '[]')
    try:
        citations = json.loads(citations_str)
    except:
        citations = []
        
    cited_uc = False
    for cit in citations:
        pub_num = cit.get('publication_number', '')
        if pub_num in uc_pub_nums:
            cited_uc = True
            break
    
    if cited_uc:
        # Extract assignee
        pat_info = rec.get('Patents_info', '')
        assignee = extract_assignee(pat_info)
        
        # Filter out UNIV CALIFORNIA (and self-citations usually implied)
        if assignee and "UNIV CALIFORNIA" not in assignee.upper():
            # Extract CPC
            cpc_str = rec.get('cpc', '[]')
            try:
                cpc_list = json.loads(cpc_str)
            except:
                cpc_list = []
            
            if cpc_list:
                # Assume first is primary
                # structure unknown, let's assume it's a dict with 'code' or 'symbol'
                primary_cpc = cpc_list[0]
                code = primary_cpc.get('code', primary_cpc.get('symbol', ''))
                # Subclass is first 4 chars
                if len(code) >= 4:
                    subclass = code[:4]
                    results.append({"assignee": assignee, "subclass": subclass})
                    cpc_subclasses.add(subclass)

print("__RESULT__:")
print(json.dumps({"matches": results, "subclasses": list(cpc_subclasses)}))"""

env_args = {'var_function-call-1646624266495231220': 'file_storage/function-call-1646624266495231220.json', 'var_function-call-1337059842938340613': [{'COUNT(*)': '277813'}], 'var_function-call-8863344319814314671': 'file_storage/function-call-8863344319814314671.json', 'var_function-call-11457268664057568431': ['WO-2024112568-A1', 'AU-6535890-A', 'WO-2019173834-A1', 'US-2019328740-A1', 'KR-20110004413-A', 'AU-2017356943-A1', 'US-2017281687-A1', 'US-2022123166-A1', 'WO-2024044766-A3', 'US-7052856-B2', 'IL-236725-A', 'US-2023171142-A1', 'CN-1120376-C', 'EP-2029921-A4', 'JP-2005104983-A', 'US-2018243924-A1', 'AU-2019275518-B2', 'KR-20160119166-A', 'US-6980295-B2', 'US-6030830-A', 'EP-3866867-A1', 'US-11546022-B2', 'US-2022074631-A1', 'WO-2018152537-A1', 'JP-2009260386-A', 'BR-9610580-A', 'US-2009031436-A1', 'CN-103687626-A', 'WO-2020055916-A9', 'CA-3225295-A1', 'CA-2278751-A1', 'US-11607427-B2', 'US-2023314781-A1', 'AU-2001257114-A1', 'US-11960018-B2', 'CA-3055214-A1', 'WO-2017136335-A1', 'WO-2010045542-A3', 'AU-2003247814-A1', 'US-6750960-B2', 'US-11072681-B2', 'WO-2023212447-A2', 'WO-2018026404-A3', 'EP-4284234-A1', 'PT-2970346-T', 'AU-3353000-A', 'IL-274176-A', 'CN-102067370-B', 'US-2020025859-A1', 'AU-2004253879-A1', 'US-2021039104-A1', 'US-10744347-B2', 'US-9061071-B2', 'US-10765865-B2', 'KR-20180041236-A', 'RO-70061-A', 'CN-101584047-A', 'AU-2003297741-A1', 'HR-P20201231-T1', 'US-2017194630-A1', 'KR-100228821-B1', 'MX-2013002850-A', 'WO-2023239670-A1', 'US-12025581-B2', 'IL-244029-A0', 'US-10359432-B2', 'WO-2021102420-A1', 'US-2021282642-A1', 'WO-2012158833-A3', 'US-2020283856-A1', 'CA-2550552-A1', 'WO-2017214343-A1', 'US-2023321419-A1', 'US-2005136639-A1', 'US-11376346-B2', 'CA-2298540-A1', 'ID-23426-A', 'US-6767662-B2', 'BR-112021021092-A8', 'US-11248107-B2', 'AU-5938296-A', 'US-2003112494-A1', 'IL-140140-A0', 'EP-2210307-A4', 'JP-2014224156-A', 'US-2018304537-A1', 'US-10900049-B2', 'AU-2898989-A', 'AU-2005269556-A1', 'AU-2002254753-B2', 'CA-3161617-A1', 'EP-1224461-B1', 'US-2017294981-A1', 'US-2022018060-A1', 'US-2021002329-A1', 'TW-201925402-A', 'EP-1212462-A1', 'US-2017087258-A1', 'AU-5366398-A', 'KR-20200041324-A', 'CN-103189548-A', 'US-2023340506-A1', 'US-2021181673-A1', 'HK-1052178-A1', 'US-2018080022-A1', 'US-11421276-B2', 'WO-2022178138-A1', 'CA-2220674-A1', 'US-2021101879-A1', 'US-2019209590-A1', 'US-2006292670-A1', 'AU-2008329628-B2', 'US-2010025717-A1', 'WO-2020096950-A1', 'US-2017369950-A1', 'EP-3668487-A4', 'AP-3334-A', 'US-2006051790-A1', 'US-11667770-B2', 'WO-2018067976-A1', 'PE-20130764-A1', 'WO-2014152660-A1', 'US-2023279470-A1', 'KR-20050085437-A', 'US-10337029-B2', 'US-2021000566-A1', 'ZA-200802422-B', 'US-3842373-A', 'KR-20080078049-A', 'CN-100339724-C', 'US-2005234013-A1', 'US-2004115131-A1', 'WO-2023225482-A3', 'CA-2718348-C', 'CN-103237558-A', 'US-6237292-B1', 'WO-2012162563-A2', 'AU-2008349842-A1', 'AU-2409401-A', 'WO-2019067860-A1', 'US-8361933-B2', 'US-2018348310-A1', 'AU-2007297661-A1', 'CA-2562038-C', 'CA-2283629-C', 'US-7745569-B2', 'US-2018277766-A1', 'CA-3027364-A1', 'US-2023155090-A1', 'US-2017050153-A1', 'KR-20200084864-A', 'US-11014955-B2', 'FR-2194760-A1', 'US-5304932-A', 'JP-S6163700-A', 'US-2017145219-A1', 'AU-2015364602-B2', 'AU-2001296493-B2', 'US-5547866-A', 'US-3666017-A', 'HK-1250569-A1', 'EP-0826155-A4', 'US-2019169580-A1', 'US-11445941-B2', 'AU-2010214112-B2', 'AU-7724398-A', 'CN-102584712-A', 'WO-2024050335-A2', 'US-2008047008-A1'], 'var_function-call-6584418003579723251': 'file_storage/function-call-6584418003579723251.json'}

exec(code, env_args)

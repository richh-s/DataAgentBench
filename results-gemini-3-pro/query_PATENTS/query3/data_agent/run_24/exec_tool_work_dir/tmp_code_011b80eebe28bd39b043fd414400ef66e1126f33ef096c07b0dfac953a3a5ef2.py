code = """import json
import re

# Load UC patents again
uc_patents_file = locals()['var_function-call-16018471667062703634']
with open(uc_patents_file, 'r') as f:
    uc_patents_data = json.load(f)

uc_pub_nums = set()
for row in uc_patents_data:
    info = row.get('Patents_info', '')
    match = re.search(r'(?:publication|pub\.)\s+(?:number|no\.)\s+([A-Za-z0-9\-]+)', info)
    if match:
        pub_num = match.group(1).rstrip('.')
        uc_pub_nums.add(pub_num)

# Load all patents with citations
citations_file = locals()['var_function-call-6025304599394944939']
# This file might be large, so we load it carefully. 
# It is a JSON list. `json.load` reads all into memory.
# 277k records * ~1KB = ~300MB. It should fit in memory.
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

results = []
subclasses = set()

for row in citations_data:
    p_info = row.get('Patents_info', '')
    if "UNIV CALIFORNIA" in p_info:
        continue

    # Parse citations
    c_str = row.get('citation', '[]')
    try:
        c_list = json.loads(c_str)
    except:
        c_list = []
    
    cited_uc = False
    for c in c_list:
        if c.get('publication_number') in uc_pub_nums:
            cited_uc = True
            break
    
    if cited_uc:
        # Extract Assignee
        # Format: "<Assignee> holds the ..." or "In <Country>, the application ... is owned by <Assignee> and ..."
        # Or "The <Country> patent filing ... is assigned to <Assignee> and ..."
        # Or "Patent filing ... held by <Assignee>, with ..."
        
        assignee = "Unknown"
        # Try different patterns
        # 1. Start with Assignee
        m1 = re.match(r'^(.+?)\s+holds the', p_info)
        if m1:
            assignee = m1.group(1)
        else:
            # 2. "is owned by <Assignee>"
            m2 = re.search(r'is owned by\s+(.+?)\s+and', p_info)
            if m2:
                assignee = m2.group(1)
            else:
                # 3. "is assigned to <Assignee>"
                m3 = re.search(r'is assigned to\s+(.+?)\s+and', p_info)
                if m3:
                    assignee = m3.group(1)
                else:
                    # 4. "held by <Assignee>"
                    m4 = re.search(r'held by\s+(.+?)(?:,|\s+and)', p_info)
                    if m4:
                        assignee = m4.group(1)
                    else:
                         # 5. "belonging to <Assignee>"
                        m5 = re.search(r'belonging to\s+(.+?)\s+and', p_info)
                        if m5:
                            assignee = m5.group(1)

        # Extract CPC Subclass
        # CPC field is JSON-like list.
        # Example: [{"code": "H04L 1/00", ...}]
        # Need primary subclass. I'll take the first code and extract subclass (first 4 chars).
        cpc_str = row.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_str)
        except:
            cpc_list = []
        
        subclass = ""
        if cpc_list and len(cpc_list) > 0:
            first_cpc = cpc_list[0].get('code', '')
            # Code format: "H04L 1/00" -> Subclass "H04L"
            # Split by space
            parts = first_cpc.split(' ')
            if parts:
                 subclass = parts[0]
                 # Ensure it is 4 chars for subclass (Section Class Subclass) e.g. H04L
                 if len(subclass) > 4:
                     subclass = subclass[:4] 
        
        if assignee != "Unknown" and subclass:
            results.append({"assignee": assignee, "subclass": subclass})
            subclasses.add(subclass)

print("__RESULT__:")
print(json.dumps({"matches": results, "subclasses": list(subclasses)}))"""

env_args = {'var_function-call-5580828402481591067': ['publicationinfo'], 'var_function-call-1301986690697536395': 'file_storage/function-call-1301986690697536395.json', 'var_function-call-16018471667062703634': 'file_storage/function-call-16018471667062703634.json', 'var_function-call-14041887104611603921': [{'COUNT(*)': '277813'}], 'var_function-call-6727023294372746694': 169, 'var_function-call-841670493808910707': ['CA-3225295-A1', 'AU-2898989-A', 'AU-5366398-A', 'EP-1212462-A1', 'CN-100339724-C', 'US-2021039104-A1', 'US-2022018060-A1', 'US-7745569-B2', 'CA-2550552-A1', 'US-2008047008-A1', 'WO-2017136335-A1', 'US-2019169580-A1', 'US-2019328740-A1', 'WO-2020096950-A1', 'TW-201925402-A', 'HK-1052178-A1', 'ID-23426-A', 'CN-102067370-B', 'US-6767662-B2', 'US-2021002329-A1', 'US-2020025859-A1', 'EP-2029921-A4', 'US-11014955-B2', 'US-10765865-B2', 'AU-2003297741-A1', 'US-6237292-B1', 'CA-2562038-C', 'AU-2010214112-B2', 'WO-2010045542-A3', 'JP-2009260386-A', 'US-2017294981-A1', 'AU-6535890-A', 'US-2023171142-A1', 'HR-P20201231-T1', 'CN-103189548-A', 'AU-2004253879-A1', 'US-2006051790-A1', 'EP-3866867-A1', 'US-11072681-B2', 'HK-1250569-A1', 'KR-20050085437-A', 'US-9061071-B2', 'US-2018348310-A1', 'KR-20110004413-A', 'CA-3027364-A1', 'US-10359432-B2', 'WO-2018026404-A3', 'US-2004115131-A1', 'US-2017145219-A1', 'EP-1224461-B1', 'US-10900049-B2', 'CA-3161617-A1', 'WO-2021102420-A1', 'US-2020283856-A1', 'US-2017087258-A1', 'WO-2020055916-A9', 'WO-2024050335-A2', 'IL-274176-A', 'CN-103687626-A', 'US-2023340506-A1', 'US-2017369950-A1', 'WO-2014152660-A1', 'US-5547866-A', 'US-2018304537-A1', 'CN-102584712-A', 'AU-5938296-A', 'US-2023279470-A1', 'JP-S6163700-A', 'WO-2023212447-A2', 'KR-20160119166-A', 'AU-2017356943-A1', 'EP-4284234-A1', 'KR-20200084864-A', 'AU-2001257114-A1', 'US-2017281687-A1', 'US-10337029-B2', 'US-5304932-A', 'WO-2024044766-A3', 'US-11421276-B2', 'US-3666017-A', 'US-11667770-B2', 'AU-2015364602-B2', 'WO-2018067976-A1', 'AU-2001296493-B2', 'MX-2013002850-A', 'US-2010025717-A1', 'KR-20180041236-A', 'US-2006292670-A1', 'US-2017050153-A1', 'US-2023314781-A1', 'CA-2718348-C', 'US-2023321419-A1', 'BR-9610580-A', 'US-2018277766-A1', 'KR-20080078049-A', 'AU-2019275518-B2', 'WO-2018152537-A1', 'CN-103237558-A', 'US-3842373-A', 'BR-112021021092-A8', 'US-2018243924-A1', 'CA-2220674-A1', 'ZA-200802422-B', 'IL-140140-A0', 'IL-236725-A', 'AU-2007297661-A1', 'AU-2008349842-A1', 'CA-2283629-C', 'US-2021181673-A1', 'US-7052856-B2', 'AP-3334-A', 'US-2021101879-A1', 'PT-2970346-T', 'US-2005234013-A1', 'US-8361933-B2', 'US-6030830-A', 'US-12025581-B2', 'AU-2002254753-B2', 'US-11445941-B2', 'US-11960018-B2', 'PE-20130764-A1', 'US-2005136639-A1', 'US-2018080022-A1', 'US-2021282642-A1', 'CA-2298540-A1', 'US-2022123166-A1', 'RO-70061-A', 'WO-2022178138-A1', 'KR-100228821-B1', 'US-11546022-B2', 'AU-2005269556-A1', 'AU-2008329628-B2', 'US-2019209590-A1', 'US-2003112494-A1', 'US-2021000566-A1', 'US-11607427-B2', 'IL-244029-A0', 'US-6980295-B2', 'JP-2005104983-A', 'US-2017194630-A1', 'US-2009031436-A1', 'US-2022074631-A1', 'WO-2012162563-A2', 'AU-7724398-A', 'WO-2017214343-A1', 'CA-3055214-A1', 'US-10744347-B2', 'US-11376346-B2', 'EP-2210307-A4', 'EP-0826155-A4', 'AU-2409401-A', 'WO-2024112568-A1', 'US-6750960-B2', 'CN-101584047-A', 'WO-2019067860-A1', 'JP-2014224156-A', 'WO-2019173834-A1', 'KR-20200041324-A', 'US-2023155090-A1', 'FR-2194760-A1', 'WO-2023239670-A1', 'US-11248107-B2', 'WO-2023225482-A3', 'CA-2278751-A1', 'CN-1120376-C', 'WO-2012158833-A3', 'AU-3353000-A', 'EP-3668487-A4', 'AU-2003247814-A1'], 'var_function-call-6025304599394944939': 'file_storage/function-call-6025304599394944939.json'}

exec(code, env_args)

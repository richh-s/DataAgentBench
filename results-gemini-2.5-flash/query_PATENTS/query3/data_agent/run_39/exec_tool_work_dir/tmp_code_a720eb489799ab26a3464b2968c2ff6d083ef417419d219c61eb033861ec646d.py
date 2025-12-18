code = """import json
import re

# Load UNIV CALIFORNIA patent info (publication_number: primary_cpc_code)
univ_california_cited_patent_info = json.loads(locals()['var_function-call-17205075467523861164'])

# Load all patents and their citations
with open(locals()['var_function-call-4733398871438009195'], 'r') as f:
    all_patents_data = json.load(f)

citing_assignees_info = []

for patent in all_patents_data:
    patents_info = patent.get('Patents_info', '')
    citation_str = patent.get('citation', '[]')
    
    # Extract assignee of the citing patent
    assignee_match = re.search(r'assignee_harmonized':\s*([A-Z0-9\s&\-]+)' , patents_info)
    # If 'assignee_harmonized' is not found, try to find 'owned by' or 'assigned to'
    if not assignee_match:
        assignee_match = re.search(r'owned by ([A-Z0-9\s&\-]+)', patents_info)
    if not assignee_match:
        assignee_match = re.search(r'assigned to ([A-Z0-9\s&\-]+)', patents_info)
        
    citing_assignee = assignee_match.group(1).strip() if assignee_match else "UNKNOWN"

    # Exclude UNIV CALIFORNIA as a citing assignee
    if "UNIV CALIFORNIA" in citing_assignee.upper():
        continue

    citations = json.loads(citation_str)
    for citation in citations:
        cited_pub_number = citation.get('publication_number')
        if cited_pub_number and cited_pub_number in univ_california_cited_patent_info:
            cited_cpc_code = univ_california_cited_patent_info[cited_pub_number]
            citing_assignees_info.append({
                'citing_assignee': citing_assignee,
                'cited_cpc_code': cited_cpc_code
            })

# Remove duplicates and format the result for the next step
unique_results = {}
for item in citing_assignees_info:
    key = (item['citing_assignee'], item['cited_cpc_code'])
    if key not in unique_results:
        unique_results[key] = item

final_citing_info = list(unique_results.values())

print("__RESULT__:")
print(json.dumps(final_citing_info))"""

env_args = {'var_function-call-9991954280777560525': ['publicationinfo'], 'var_function-call-17198847221600567673': [], 'var_function-call-10301112809646823471': 'file_storage/function-call-10301112809646823471.json', 'var_function-call-4997015473653672400': [], 'var_function-call-10862841933274024202': 'file_storage/function-call-10862841933274024202.json', 'var_function-call-7620258214686575354': 'file_storage/function-call-7620258214686575354.json', 'var_function-call-17586866852388310109': 'file_storage/function-call-17586866852388310109.json', 'var_function-call-17205075467523861164': {'US-2022074631-A1': 'Y02B30/00', 'TW-201925402-A': 'C09J11/04', 'AU-2019275518-B2': 'A61K31/357', 'JP-S6163700-A': 'C07K16/30', 'US-2017281687-A1': 'A61K31/52', 'US-9061071-B2': 'A61P3/10', 'EP-0826155-A4': 'G01T1/18', 'RO-70061-A': 'C07D295/26', 'WO-2021102420-A1': 'A61P35/00', 'WO-2012162563-A2': 'C12N15/1013', 'US-11376346-B2': 'A61L27/367', 'CN-100339724-C': 'G01V3/12', 'US-2017145219-A1': 'C09C1/3661', 'KR-20200041324-A': 'B01D2256/245', 'CN-103189548-A': 'C30B7/105', 'CA-2298540-A1': 'A61P25/04', 'US-2021000566-A1': 'A61F9/009', 'US-2006051790-A1': 'C12Q1/6883', 'US-2023171142-A1': 'G01S11/02', 'WO-2018026404-A3': 'H04B1/38', 'US-2006292670-A1': 'A61P43/00', 'US-2021101879-A1': 'A61P25/28', 'US-2023321419-A1': 'A61M37/0015', 'AU-2003297741-A1': 'G16B20/00', 'WO-2017214343-A1': 'A61P1/00', 'US-11667770-B2': 'C08J2205/10', 'CA-2562038-C': 'A61P35/00', 'US-6750960-B2': 'G01S7/4811', 'US-2020025859-A1': 'B64U2201/104', 'EP-1212462-A1': 'G01N33/48721', 'US-5547866-A': 'C12N5/04', 'US-2023279470-A1': 'C12Q1/6806', 'AU-2008349842-A1': 'H01M2008/1293', 'EP-4284234-A1': 'A61B5/4836', 'WO-2020055916-A9': 'C07H15/12', 'US-6767662-B2': 'Y02E60/10', 'AU-2015364602-B2': 'C12Q1/48', 'IL-274176-A': 'A61K9/5153', 'JP-2014224156-A': 'A61P9/12', 'IL-244029-A0': 'C07D405/12', 'AU-2010214112-B2': 'A61P37/06', 'MX-2013002850-A': 'A01N37/40', 'US-2019328740-A1': 'G01N2800/52', 'US-2022018060-A1': 'A61Q19/00', 'WO-2023225482-A3': 'C12N15/85', 'WO-2024044766-A3': 'C12N5/0647', 'AU-2007297661-A1': 'A61K38/1825', 'WO-2024112568-A1': 'C12N2310/315', 'CA-2550552-A1': 'H05H9/02', 'CN-102584712-A': 'A61P5/28', 'CN-102067370-B': 'H01M8/1226', 'US-11546022-B2': 'H04B7/0413', 'US-2023155090-A1': 'H01L2933/0025', 'WO-2010045542-A3': 'A61P43/00', 'HK-1250569-A1': 'A61K38/1732', 'ID-23426-A': 'A61B2017/12077', 'US-5304932-A': 'G01R33/421', 'US-2018243924-A1': 'G01L1/146', 'AU-6535890-A': 'G11B7/004'}, 'var_function-call-4733398871438009195': 'file_storage/function-call-4733398871438009195.json'}

exec(code, env_args)

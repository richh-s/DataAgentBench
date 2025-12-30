code = """import json

civic_key = 'var_function-call-10494056103338850643'
with open(locals()[civic_key], 'r') as f:
    civic_docs = json.load(f)

target_name = "Legacy Park"
found_lines = []

for doc in civic_docs:
    lines = doc['text'].splitlines()
    for i, line in enumerate(lines):
        if target_name in line:
            context = lines[i:i+10]
            found_lines.append(context)

print("__RESULT__:")
print(json.dumps(str(found_lines)))"""

env_args = {'var_function-call-17786645428432444760': ['civic_docs'], 'var_function-call-17786645428432443965': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-9932309007747960995': 'file_storage/function-call-9932309007747960995.json', 'var_function-call-10494056103338850643': 'file_storage/function-call-10494056103338850643.json', 'var_function-call-10332075929140261895': 'file_storage/function-call-10332075929140261895.json', 'var_function-call-17814162175572024946': {'completed_park_projects': ['Bluffs Park Shade Structure', 'Malibu Park Drainage Improvements'], 'total_funding': 38000.0}, 'var_function-call-17074296913641022749': "[['Malibu Park Drainage Improvements', '', '(cid:190) Updates: The Contractor completed the repairs to storm drains on Cuthbert', 'Road, Morning View Drive, Busch Drive, Harvester Road and Birdview', 'Avenue. This project is scheduled to be accepted by the Council at the', 'January 24, 2022 meeting.', '', 'Clover Heights Storm Drain (FEMA Project)', '', '(cid:190) Project Description: This project consists of design and construction of a few', 'storm drains on Clover Heights. The existing storm drain facility ends at the', 'intersection of Clover Heights and Harvester Road. During storms, this', 'intersection floods and causes debris to block the road. An extended storm', 'drain towards the end of Clover Heights will help eliminate this issue.', ''], ['Malibu Park Drainage Improvements', '', '(cid:190) Updates:', '', '(cid:131) Staff is making minor corrections to the project plans to reduce the', '', 'overall project costs.', '', 'Page 2 of 6', '', 'Agenda Item # 4.A.', '', '', '', ''], ['Malibu Park Drainage Improvements', '', '(cid:190) Updates:', '', '(cid:131) Staff is making minor modifications to the project plans to reduce the', '', 'overall project costs.', '', '(cid:131) Project is scheduled to go out to bid next week.', '', '(cid:190) Project Schedule:', '', '(cid:131) Complete Design: February 2021', '(cid:131) Begin Construction: April 2021', '']]"}

exec(code, env_args)

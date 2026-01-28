code = """import json

with open(locals()['var_function-call-6099601671334015320'], 'r') as f:
    civic_docs = json.load(f)

target = "2021 Annual Street Maintenance"
found_text = []

for doc in civic_docs:
    lines = doc['text'].splitlines()
    capturing = False
    for line in lines:
        if target in line:
            capturing = True
            found_text.append("HEADER: " + line)
            continue
        if capturing:
            if "Projects (" in line: # New section
                capturing = False
            else:
                found_text.append(line)

print("__RESULT__:")
print(json.dumps(found_text[:20]))"""

env_args = {'var_function-call-18312166134834260107': 'file_storage/function-call-18312166134834260107.json', 'var_function-call-6099601671334015320': 'file_storage/function-call-6099601671334015320.json', 'var_function-call-9845122995383564769': 'file_storage/function-call-9845122995383564769.json', 'var_function-call-6347418710872321306': {'total_funding': 209000, 'matched_projects': ['2021 Annual Street Maintenance', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Malibu Park Drainage Improvements']}, 'var_function-call-2894122064455046474': ['HEADER: Malibu Park Drainage Improvements', '', '(cid:190) Updates: The Contractor completed the repairs to storm drains on Cuthbert', 'Road, Morning View Drive, Busch Drive, Harvester Road and Birdview', 'Avenue. This project is scheduled to be accepted by the Council at the', 'January 24, 2022 meeting.', '', 'Clover Heights Storm Drain (FEMA Project)', '', '(cid:190) Project Description: This project consists of design and construction of a few', 'storm drains on Clover Heights. The existing storm drain facility ends at the', 'intersection of Clover Heights and Harvester Road. During storms, this', 'intersection floods and causes debris to block the road. An extended storm', 'drain towards the end of Clover Heights will help eliminate this issue.', '', '(cid:190) Updates:', '', '(cid:131) Staff is currently preparing consultant proposals for the design of this', '', 'project. Proposals will be due in February/March.']}

exec(code, env_args)

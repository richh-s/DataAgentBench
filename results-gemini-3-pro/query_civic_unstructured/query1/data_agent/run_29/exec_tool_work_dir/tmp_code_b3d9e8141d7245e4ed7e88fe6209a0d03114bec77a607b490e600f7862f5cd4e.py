code = """import json
import re

# Load funding data
with open(locals()['var_function-call-8365727956601891924'], 'r') as f:
    funding_records = json.load(f)

high_funding_projects = set()
for rec in funding_records:
    try:
        amt = int(rec['Amount'])
        if amt > 50000:
            high_funding_projects.add(rec['Project_Name'].strip())
    except:
        pass

# Load civic docs
with open(locals()['var_function-call-8365727956601890549'], 'r') as f:
    civic_docs = json.load(f)

extracted_design_projects = set()

start_header = "Capital Improvement Projects (Design)"
end_headers = [
    "Capital Improvement Projects (Construction)", 
    "Capital Improvement Projects (Not Started)", 
    "Disaster Recovery Projects"
]

footer_re = re.compile(r"Page \d+ of \d+|Agenda Item #.*", re.IGNORECASE)

for doc in civic_docs:
    text = doc['text']
    
    start_idx = text.find(start_header)
    if start_idx == -1:
        continue
    
    end_idx = len(text)
    for eh in end_headers:
        idx = text.find(eh, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    section_text = text[start_idx + len(start_header):end_idx]
    
    lines = section_text.splitlines()
    
    last_valid_line = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Trigger on the bullet (cid:190)
        if "(cid:190)" in line:
            if last_valid_line:
                extracted_design_projects.add(last_valid_line)
            last_valid_line = None 
        elif footer_re.search(line):
            continue
        else:
            last_valid_line = line

# Intersection
matching_projects = extracted_design_projects.intersection(high_funding_projects)

print("__RESULT__:")
print(json.dumps({
    "extracted_design_projects": list(extracted_design_projects),
    "count": len(matching_projects),
    "matching_projects": list(matching_projects)
}))"""

env_args = {'var_function-call-8365727956601891924': 'file_storage/function-call-8365727956601891924.json', 'var_function-call-8365727956601890549': 'file_storage/function-call-8365727956601890549.json', 'var_function-call-12646988407192400613': 'Capital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n(cid:131) Begin Construction: Fall 2023\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) On September 22, 2022, the City received four (4) construction bids\n\nand rejected all bids due to a budget shortfall\n\n(cid:131) City will work with the design consultant to review design alternatives\n\nor phasing out the project\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n\nPage 1 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n(cid:131) Begin Construction: Fall 2023\n\nWestward Beach Road Repair Project\n\n(cid:190) Updates:\n\n(cid:131) City working with consultant on the design of the shoulder repairs\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Summer 2023\n(cid:131) Begin Construction: Fall 2023\n\nWestward Beach Road Drainage Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) Plans are under review by Fish and Wildlife and City is expecting\ncomments mid-April. This project required their review since the project\nscope falls within Zuma Canyon Creek. Army Corp. of Engineers has\ncleared the project.\n\n(cid:190) Project Schedule:\n\n(cid:131) Advertise: Summer 2023\n(cid:131) Begin Construction: Fall 2023\n\nClover Heights Storm Drainage Improvements\n\n(cid:190) Updates:\n\n(cid:131) City submitted plans to CalOES for review and working with consultant\n\nto finalize plans and specifications\n\n(cid:190) Project Schedule:\n\n(cid:131) Final Design: Summer, 2023\n(cid:131) Advertise: Summer 2023\n(cid:131) Begin Construction: Fall 2023\n\nLatigo Canyon Road Retaining Wall Repair Project\n\n(cid:190) Updates:\n\n(cid:131) Plans and specifications have be', 'var_function-call-268358025602625105': {'extracted_design_projects': ['PCH Signal Synchronization System Improvements Project', 'Malibu Park Drainage Improvements', 'feasible traffic safety improvements can be constructed at this location.', 'PCH at Trancas Canyon Road Right Turn Lane', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'Permanent Skate Park', 'shade structures at Malibu Bluffs Park.', 'Malibu Bluffs Park South Walkway Repairs', 'Storm Drain Master Plan', 'amenities such as trash cans, benches, tables, and restrooms.', 'Trancas Canyon Park Playground', 'Westward Beach Road Repair Project', 'Civic Center Stormwater Diversion Structure', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Westward Beach Road Drainage Improvements Project', 'PCH Median Improvements Project', 'Latigo Canyon Road Retaining Wall Repair Project', 'Westward Beach Road Improvements Project', 'Civic Center Water Treatment Facility Phase 2', 'Clover Heights Storm Drainage Improvements', 'Marie Canyon Green Streets', 'Outdoor Warning Signs'], 'count': 9, 'matching_projects': ['Latigo Canyon Road Retaining Wall Repair Project', 'Civic Center Stormwater Diversion Structure', 'Malibu Bluffs Park South Walkway Repairs', 'Storm Drain Master Plan', 'Westward Beach Road Drainage Improvements Project', 'PCH at Trancas Canyon Road Right Turn Lane', 'PCH Median Improvements Project', 'Permanent Skate Park', 'Outdoor Warning Signs']}, 'var_function-call-11551658182784987721': [{'Funding_ID': '74', 'Project_Name': 'PCH Signal Synchronization System Improvements Project', 'Funding_Source': 'International Aid', 'Amount': '16000'}], 'var_function-call-9693350560002819618': [{'Funding_ID': '19', 'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Funding_Source': 'Crowdfunding', 'Amount': '45000'}, {'Funding_ID': '54', 'Project_Name': 'Malibu Canyon Road Traffic Study', 'Funding_Source': 'State Development Grant', 'Amount': '97000'}]}

exec(code, env_args)

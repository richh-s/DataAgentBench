code = """import json
import re
from datetime import datetime

funding_file = locals()['var_function-call-4872762091954436572']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

docs_file = locals()['var_function-call-4872762091954434845']
with open(docs_file, 'r') as f:
    civic_docs = json.load(f)

def parse_date(filename):
    match = re.search(r'(\d{8})', filename)
    if match:
        return datetime.strptime(match.group(1), "%m%d%Y")
    return datetime.min

latest_doc = max(civic_docs, key=lambda d: parse_date(d['filename']))

capital_design_projects = set()
target_header = "Capital Improvement Projects (Design)"
next_headers = [
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects"
]

text = latest_doc.get('text', '')
start_idx = text.find(target_header)
if start_idx != -1:
    start_idx += len(target_header)
    end_idx = len(text)
    for nh in next_headers:
        idx = text.find(nh, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    section_text = text[start_idx:end_idx]
    lines = [l.strip() for l in section_text.split(chr(10)) if l.strip()]
    
    for i in range(len(lines) - 1):
        line = lines[i]
        next_line = lines[i+1]
        
        if not line: continue
        
        is_start_of_block = False
        if "(cid:190)" in next_line:
            is_start_of_block = True
        elif "Updates:" in next_line or "Project Description:" in next_line or "Project Schedule:" in next_line or "Estimated Schedule:" in next_line:
            is_start_of_block = True
            
        if is_start_of_block:
            if "Page" in line and "of" in line: continue
            if "Agenda Item" in line: continue
            
            capital_design_projects.add(line)

matched_projects = set()

high_funding_db_names = set()
for item in funding_data:
    try:
        if float(item['Amount']) > 50000:
            high_funding_db_names.add(item['Project_Name'].strip())
    except:
        pass

for proj in capital_design_projects:
    found = False
    for db_name in high_funding_db_names:
        if proj == db_name:
            found = True
        elif len(proj) > 5 and len(db_name) > 5:
             if proj in db_name or db_name in proj:
                found = True
        
        if found:
            matched_projects.add(proj)
            break

print("__RESULT__:")
print(json.dumps({
    "count": len(matched_projects),
    "projects": list(matched_projects),
    "debug_extracted": list(capital_design_projects)
}))"""

env_args = {'var_function-call-4872762091954436572': 'file_storage/function-call-4872762091954436572.json', 'var_function-call-4872762091954434845': 'file_storage/function-call-4872762091954434845.json', 'var_function-call-14207660122880327924': {'count': 0, 'projects': []}, 'var_function-call-14847519188014513356': {'count': 10, 'projects': ['PCH at Trancas Canyon Road Right Turn Lane', 'Storm Drain Master Plan', 'Outdoor Warning Signs', 'Westward Beach Road Drainage Improvements Project', 'Latigo Canyon Road Retaining Wall Repair Project', 'Civic Center Stormwater Diversion Structure', 'Malibu Canyon Road Traffic Study', 'Malibu Bluffs Park South Walkway Repairs', 'PCH Median Improvements Project', 'Permanent Skate Park'], 'extracted_sample': ['March 2022', '(cid:131) Staff is currently working on the final design plans', 'PCH at Trancas Canyon Road Right Turn Lane', '(cid:131) Funding agreement is schedule for city council on March 27, 2023', 'Storm Drain Master Plan', '(cid:131) City to request proposal from consultant for design services', 'Latigo Canyon Road Retaining Wall Repair Project', 'the County and will be finalizing the design.', 'Trancas Canyon Park Playground', 'Metro.'], 'funding_sample': ['project_166', 'project_41', 'PCH at Trancas Canyon Road Right Turn Lane', 'Recommended Action', 'Storm Drain Master Plan', 'project_2', 'project_35', 'Harbor Vista Curb Return', 'project_216', 'Latigo Canyon Road Retaining Wall Repair Project'], 'debug_lines': ['2022 Morning View Resurfacing & Storm Drain Improvements', '(cid:190) Updates:', '(cid:131) Staff is working with the consultant to finalize the design plans for this', 'project and will submit to the County for review.', '(cid:190) Project Schedule:', '(cid:131) Complete Design: Summer 2023', '(cid:131) Advertise: Fall 2023', '(cid:131) Begin Construction: Fall 2023', 'PCH Median Improvements Project', '(cid:190) Updates:', '(cid:131) On September 22, 2022, the City received four (4) construction bids', 'and rejected all bids due to a budget shortfall', '(cid:131) City will work with the design consultant to review design alternatives', 'or phasing out the project', '(cid:190) Project Schedule:', '(cid:131) Complete Design: Summer 2023', '(cid:131) Advertise: Fall 2023', 'Page 1 of 6', 'Agenda Item # 4.B.', '(cid:131) Begin Construction: Fall 2023']}, 'var_function-call-16745084918213933828': {'matched_count': 10, 'matched_projects': ['Storm Drain Master Plan', 'Civic Center Stormwater Diversion Structure', 'Outdoor Warning Signs', 'Malibu Canyon Road Traffic Study', 'PCH Median Improvements Project', 'Latigo Canyon Road Retaining Wall Repair Project', 'PCH at Trancas Canyon Road Right Turn Lane', 'Malibu Bluffs Park South Walkway Repairs', 'Permanent Skate Park', 'Westward Beach Road Drainage Improvements Project'], 'missed_but_in_db (low funding)': [], 'missed_not_in_db (name mismatch or no funding record)': ['Trancas Canyon Park Playground', 'Clover Heights Storm Drainage Improvements', '(cid:131) Plans and specifications are being finalized by consultant', 'Malibu Park Drainage Improvements', '(cid:131) Funding agreement is schedule for city council on March 27, 2023', 'advertised for construction bids shortly after this date.', 'shade structures at Malibu Bluffs Park.', 'construction bids.', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'cleared the project.', 'Metro.', '(cid:131) Awaiting final FEMA/CalOES approval for scope modification', '(cid:131) Staff is currently working on the final design plans', 'to review', 'assessment district will be created.', '(cid:131) Staff has submitted a request for Federal funding', 'project will begin in conjunction with the PCH Median Improvement', 'feasible traffic safety improvements can be constructed at this location.', 'review by the Council.', 'property owners.', 'the Spring 2023.', 'Civic Center Water Treatment Facility Phase 2', 'March 2022', 'agreement will be sent to City Council in March.', 'management services was approved by Council on March 14, 2022.', 'Bluffs Park Shade Structure', '(cid:131) Consultant is working on final design documents.', 'the agreement.', 'management.', '(cid:131) Project is scheduled to go out to bid next week.', 'sending this project out to bid during the Spring of 2022.', "Council's direction.", 'the County and will be finalizing the design.', '(cid:131) Next public community meeting is scheduled for March 25th.', 'or phasing out the project', 'project and will submit to the County for review.', '(cid:131) City working with consultant on the design of the shoulder repairs', '(cid:131) City to request proposal from consultant for design services', 'Westward Beach Road Improvements Project', 'will begin in conjunction with the PCH Median Improvement', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Marie Canyon Green Streets', 'scheduled for the April 11, 2022 Council meeting.', 'to finalize plans and specifications', 'amenities such as trash cans, benches, tables, and restrooms.', 'project', 'PCH Signal Synchronization System Improvements Project', 'Westward Beach Road Repair Project', 'bidding.']}, 'var_function-call-13773452523351613889': ['malibucity_agenda_03222023-2060.txt', 'malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt']}

exec(code, env_args)

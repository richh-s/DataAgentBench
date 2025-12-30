code = """import json
import re
from datetime import datetime

funding_path = locals()["var_function-call-8778761271394130701"]
civic_path = locals()["var_function-call-17737362930517738246"]
with open(funding_path, 'r') as f: funding_data = json.load(f)
with open(civic_path, 'r') as f: civic_docs = json.load(f)

# Filter funding
funded_projects = set()
for r in funding_data:
    try:
        if float(r['Amount']) > 50000: funded_projects.add(r['Project_Name'])
    except: pass

# Find latest doc
latest_doc = None
latest_date = datetime.min

for doc in civic_docs:
    fname = doc['filename']
    # Extract date MMDDYYYY
    match = re.search(r'(\d{8})', fname)
    if match:
        dt_str = match.group(1)
        dt = datetime.strptime(dt_str, '%m%d%Y')
        if dt > latest_date:
            latest_date = dt
            latest_doc = doc

extracted_projects = set()

if latest_doc:
    lines = latest_doc['text'].split(chr(10))
    in_section = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            in_section = True
            continue
        
        if in_section:
            # End of section check
            if 'Capital Improvement Projects (' in line and 'Design' not in line:
                in_section = False
                continue
            
            if not line:
                continue
            
            # Skip metadata lines
            if line.startswith('Page ') or line.startswith('Agenda Item') or line.lower().startswith('prepared by') or line.lower().startswith('approved by'):
                continue
            
            if line.startswith('(cid:'):
                continue
            
            # Heuristic: Project name followed by bullet points
            is_proj = False
            for k in range(i+1, min(i+10, len(lines))):
                nxt = lines[k].strip()
                if not nxt:
                    continue
                if nxt.startswith('(cid:'):
                    is_proj = True
                    break
                else:
                    # If text appears before bullet, maybe it's multi-line title or description?
                    # In the preview, title is single line.
                    break
            
            if is_proj:
                extracted_projects.add(line)

final_projects = extracted_projects.intersection(funded_projects)

print('__RESULT__:')
print(json.dumps({
    'count': len(final_projects),
    'projects': list(final_projects),
    'latest_file': latest_doc['filename']
}))"""

env_args = {'var_function-call-8778761271394130701': 'file_storage/function-call-8778761271394130701.json', 'var_function-call-8778761271394130352': 'file_storage/function-call-8778761271394130352.json', 'var_function-call-17737362930517738246': 'file_storage/function-call-17737362930517738246.json', 'var_function-call-1995051770979697338': {'count': 10, 'projects': ['PCH at Trancas Canyon Road Right Turn Lane', 'Permanent Skate Park', 'Outdoor Warning Signs', 'Storm Drain Master Plan', 'Latigo Canyon Road Retaining Wall Repair Project', 'Malibu Canyon Road Traffic Study', 'Westward Beach Road Drainage Improvements Project', 'Civic Center Stormwater Diversion Structure', 'PCH Median Improvements Project', 'Malibu Bluffs Park South Walkway Repairs'], 'extracted': ['Permanent Skate Park', 'Malibu Canyon Road Traffic Study', 'project and will submit to the County for review.', 'PCH Signal Synchronization System Improvements Project', 'Canyon Road near Harbor Vista Drive and Potter Lane to determine if any', 'assessments.', 'selected a qualified consultant. It is anticipated that the agreement will', 'Civic Center Stormwater Diversion Structure', 'communicating with the property owners regarding their proposed', 'advertised for construction bids after this date. A construction manager', 'comments mid-April. This project required their review since the project', 'bicycles pavement markings, delineated parallel parking spaces and', 'Resources review for the SRF funding application', 'been finalized and incorporated into GIS.', 'agreement will be sent to City Council in March.', 'Clover Heights Storm Drainage Improvements', 'PCH at Trancas Canyon Road Right Turn Lane', 'or phasing out the project', 'assessment district will be created.', 'to review', 'and rejected all bids due to a budget shortfall', 'Commission will then review the project in Spring 2022 before final', 'the project', 'Storm Drain Master Plan', 'construction bids.', 'preliminary estimated assessments in July 2021. Staff has been', 'the County and will be finalizing the design.', 'property owners.', 'Bluffs Park Shade Structure', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Westward Beach Road Repair Project', 'Outdoor Warning Signs', 'consultant. It is anticipated that this agreement will go to Council in', 'of the assessment district to June 30, 2022.', 'PCH Median Improvements Project', 'Malibu Bluffs Park South Walkway Repairs', 'Marie Canyon Green Streets', 'Westward Beach Road Improvements Project', 'and Harbor. Staff is working out the final details of the project with', 'Metro.', 'Malibu Park Drainage Improvements', 'feasible traffic safety improvements can be constructed at this location.', 'shortly after final approval. If possible, the construction of this project', 'overall project costs.', 'to finalize plans and specifications', 'project. Staff is working on the project plans to prepare for public', 'go to Council in April 2022 after the Funding Agreement is issued by', 'to Malibu Bluffs Park. The project would include parking and additional site', 'Latigo Canyon Road Retaining Wall Repair Project', 'by March 2022. The project will be advertised for construction bids', 'March 2022', 'amenities such as trash cans, benches, tables, and restrooms.', 'project', 'seeking proposals', 'Project Schedule:', 'Civic Center Water Treatment Facility Phase 2', 'the County.', 'February 1, 2021.', 'manufacturers for filters that will work in the proposed project area. It is', 'the Spring 2023.', 'Trancas Canyon Park Playground', 'scope falls within Zuma Canyon Creek. Army Corp. of Engineers has', 'review by the Council.', 'speed humps. There is room to add a pathway within the R/W per', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Resources review.', 'sirens height and feedback from residents and the community.', 'construction bids after approval. An agreement for construction', 'advertised for construction bids shortly after this date.', 'management.', 'will begin in conjunction with the PCH Median Improvement', 'execution in July and has followed up with an additional letter to those', 'scheduled for the April 11, 2022 Council meeting.', 'bids shortly after final approval. If possible, the construction of this', 'with the property owners regarding their proposed assessments.', 'management services was approved by Council on March 14, 2022.', "Council's direction.", 'preliminary estimated assessments. Staff has been communicating', 'shade structures at Malibu Bluffs Park.', 'evaluating the project costs.', 'Fund program.', 'the agreement.', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'program.', 'final design is complete and the project will be advertised for', 'anticipated to have a final design by March 2022. The project will be', 'cleared the project.', 'the process of', 'modification of the schedule has been requested.', 'Individual letters were mailed to all properties within Phase 2 with their', 'sending this project out to bid during the Spring of 2022.', 'bidding.', 'project will begin in conjunction with the PCH Median Improvement', 'required for this project. Staff is waiting for the County’s approval of', 'Commission in February.', 'permanent skate park located on the Crummer/Case Court parcel adjacent', 'Westward Beach Road Drainage Improvements Project', 'manufacturers for filters that will work in the proposed project area. The', 'draft plans are expected to be completed in early 2022. The Planning', 'of the assessment district to June 30, 2022. A new request for further']}, 'var_function-call-8899588793837244616': ['malibucity_agenda_03222023-2060.txt', 'malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt']}

exec(code, env_args)

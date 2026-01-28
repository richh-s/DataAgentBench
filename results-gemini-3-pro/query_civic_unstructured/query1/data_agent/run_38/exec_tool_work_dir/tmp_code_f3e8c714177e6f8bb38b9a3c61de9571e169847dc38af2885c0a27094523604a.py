code = """import json
import pandas as pd
import re
from datetime import datetime

# Get file paths from storage
funding_path = locals()['var_function-call-5988651082647865980']
docs_path = locals()['var_function-call-9407752625735979853']

# Load funding data
funding_data = pd.read_json(funding_path)
# Filter for funding > 50,000
high_funding_projects = set(funding_data[funding_data['Amount'] > 50000]['Project_Name'].str.strip().tolist())

# Load civic docs
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

# Helper to parse date from filename
# filename example: "malibucity_agenda__01262022-1835.txt"
# Regex to find MMDDYYYY
def get_date(filename):
    match = re.search(r'(\d{8})', filename)
    if match:
        d_str = match.group(1)
        try:
            return datetime.strptime(d_str, "%m%d%Y")
        except:
            return datetime.min
    return datetime.min

# Store project status: { normalized_name: {'status': status, 'date': date, 'original_name': name} }
project_status_map = {}

for doc in civic_docs:
    doc_date = get_date(doc['filename'])
    text = doc['text']
    lines = text.splitlines()
    
    current_status = None # design, construction, completed, not_started
    current_type = None # capital, disaster
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check Headers
        if "Capital Improvement Projects" in line:
            current_type = "capital"
            if "Design" in line:
                current_status = "design"
            elif "Construction" in line:
                current_status = "construction"
            elif "Completed" in line:
                current_status = "completed"
            elif "Not Started" in line:
                current_status = "not started"
            else:
                current_status = None
            continue
        
        if "Disaster Recovery Projects" in line:
            current_type = "disaster"
            current_status = None # We don't care about status of disaster projects for this query
            continue
            
        if "Agenda Item" in line or "Page " in line:
            continue
            
        if current_type == "capital" and current_status:
            # Capture project
            # Skip metadata
            if line.startswith("(") or "Updates:" in line or "Project Schedule:" in line or "Complete Design:" in line or "Advertise:" in line or "Begin Construction:" in line:
                continue
            if len(line) < 5:
                continue
            
            project_name = line.strip()
            norm_name = project_name.lower().replace("project", "").strip()
            
            # Update map if this entry is newer
            if norm_name not in project_status_map or doc_date > project_status_map[norm_name]['date']:
                project_status_map[norm_name] = {
                    'status': current_status,
                    'date': doc_date,
                    'original_name': project_name
                }

# Now filter for status = "design" and funding > 50k
count = 0
matched_projects = []

hf_norm = {name.lower().replace("project", "").strip(): name for name in high_funding_projects}

# We need to map extracted projects to funding projects
# Iterate over our resolved projects
for p_norm, p_data in project_status_map.items():
    if p_data['status'] != 'design':
        continue
    
    # Check funding
    p_name = p_data['original_name']
    
    found_funding = False
    
    # Matching logic
    if p_name in high_funding_projects:
        found_funding = True
    elif p_norm in hf_norm:
        found_funding = True
    else:
        # Substring
        for hf_name in high_funding_projects:
            hf_n = hf_name.lower()
            p_n = p_name.lower()
            if (p_n in hf_n or hf_n in p_n) and len(p_n) > 10:
                found_funding = True
                break
    
    if found_funding:
        count += 1
        matched_projects.append(p_name)

print("__RESULT__:")
print(json.dumps({"count": count, "matched_projects": matched_projects}))"""

env_args = {'var_function-call-5988651082647865980': 'file_storage/function-call-5988651082647865980.json', 'var_function-call-9407752625735979853': 'file_storage/function-call-9407752625735979853.json', 'var_function-call-9633004668962151224': {'count': 12, 'matched_projects': ['Permanent Skate Park', 'Outdoor Warning Signs', 'Civic Center Stormwater Diversion Structure', 'PCH Median Improvements Project', 'Clover Heights Storm Drain', 'Malibu Canyon Road Traffic Study', 'PCH at Trancas Canyon Road Right Turn Lane', 'Trancas Canyon Park Playground Resurfacing', 'Storm Drain Master Plan', 'Malibu Bluffs Park South Walkway Repairs', 'Westward Beach Road Drainage Improvements Project', 'Latigo Canyon Road Retaining Wall Repair Project'], 'debug_extracted': ['scheduled for the April 11, 2022 Council meeting.', 'Commission in February.', 'project', 'scope falls within Zuma Canyon Creek. Army Corp. of Engineers has', 'the Spring 2023.', 'PCH at Trancas Canyon Road Right Turn Lane', 'comments mid-April. This project required their review since the project', 'the agreement.', 'present the recommended design alternatives to Council on March 28,', 'approval by March 2022. The project will be advertised for construction', 'Outdoor Warning Signs', 'Resources review.', 'alternatives. A joint Public Works and Public Safety Commission', 'Westward Beach Road Repair Project', 'Safety Commissions', 'amenities such as trash cans, benches, tables, and restrooms.', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'project and will submit to the County for review.', 'program.', 'Canyon Road near Harbor Vista Drive and Potter Lane to determine if any', 'the process of', 'required for this project. Staff is waiting for the County’s approval of', 'Storm Drain Master Plan', 'to develop project', 'project. Staff is working on the project plans to prepare for public', 'agreement will be sent to City Council in March.', 'modification of the schedule has been requested.', '2022.', 'or phasing out the project', 'manufacturers for filters that will work in the proposed project area. The', '8, 2021. This project requires Caltrans approval since the work will be', 'property owners.', 'to review', 'project will have final approval by March 2022. The project will be', 'This project requires Caltrans approval since the work will be on PCH.', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Individual letters were mailed to all properties within Phase 2 with their', 'sending this project out to bid during the Spring of 2022.', 'February 1, 2021.', 'approval by the end of the March. The project will be advertised for', 'sirens height and feedback from residents and the community.', 'the County.', 'Coastal Development Permit and directed the Public Works and Public', 'bidding.', 'and Harbor. Staff is working out the final details of the project with', 'Metro.', 'evaluating the project costs.', 'schedule will be developed upon the completion of the Cultural', 'routed through Caltrans for final approval. The project will have final', 'Trancas Canyon Park Playground', 'advertised for construction bids shortly after this date.', 'bids shortly after final approval. If possible, the construction of this', 'from consultants', 'consultant. It is anticipated that this agreement will go to Council in', 'The project reports and plans are being routed through Caltrans for', 'project alternatives were presented to the commissions. City staff will', 'draft plans are expected to be completed in early 2022. The Planning', 'for final approval. It is anticipated that the project will have final', 'Permanent Skate Park', 'with the property owners regarding their proposed assessments.', 'go to Council in April 2022 after the Funding Agreement is issued by', 'to Malibu Bluffs Park. The project would include parking and additional site', 'permanent skate park located on the Crummer/Case Court parcel adjacent', 'Malibu Park Drainage Improvements', 'manufactured biofilters. City staff', 'construction bids after approval. An agreement for construction', 'shade structures at Malibu Bluffs Park.', 'meeting was held on January 20, 2022. Project alternatives will be', 'by March 2022. The project will be advertised for construction bids', 'City will be issuing a RFQ/P for design services in the summer of 2023', 'Westward Beach Road Improvements Project', 'Bluffs Park Shade Structure', 'the past several months to complete the engineering work, and the final', 'management services was approved by Council on March 14, 2022.', 'overall project costs.', 'Civic Center Stormwater Diversion Structure', 'Marie Canyon Green Streets', 'selected a qualified consultant. It is anticipated that the agreement will', 'preliminary estimated assessments. Staff has been communicating', 'Council directed staff to withdraw the proposed project and associated', 'Clover Heights Storm Drainage Improvements', 'anticipated to have a final design by March 2022. The project will be', 'to perform construction', 'September 20, 2021. At the December 13, 2021, City Council meeting,', 'to finalize plans and specifications', 'final design is complete and the project will be advertised for', 'manufactured biofilters. City staff is reviewing multiple biofilter', 'review by the Council.', 'the County and will be finalizing the design.', 'communicating with the property owners regarding their proposed', 'project will begin in conjunction with the PCH Median Improvement', 'March 2022', "rehabilitation of the roadway to max 8' from R/W, add share road with", 'Westward Beach Road Drainage Improvements Project', 'advertised for construction bids after this date. A construction manager', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'assessments.', 'Commission meeting for project direction due to concerns regarding', 'PCH Median Improvements Project', 'PCH Signal Synchronization System Improvements Project', 'work related to the project. Staff has worked with the consultant over', 'cleared the project.', 'execution in July and has followed up with an additional letter to those', 'construction bids.', 'PCH. The project reports and plans are being routed through Caltrans', 'and rejected all bids due to a budget shortfall', 'manufacturers for filters that will work in the proposed project area. It is', 'Latigo Canyon Road Retaining Wall Repair Project', 'presented to the commissions at a future date.', 'Civic Center Water Treatment Facility Phase 2', 'final approval. It is anticipated that the project will have final approval', 'speed humps. There is room to add a pathway within the R/W per', 'Commission will then review the project in Spring 2022 before final', 'the project', 'Fund program.', 'preliminary estimated assessments in July 2021. Staff has been', 'will begin in conjunction with the PCH Median Improvement', 'of the assessment district to June 30, 2022.', 'Malibu Canyon Road Traffic Study', 'reviewed multiple biofilter', 'Resources review for the SRF funding application', '2022. This project requires Caltrans approval since the work will be on', 'seeking proposals', 'assessment district will be created.', "Council's direction.", 'shortly after final approval. If possible, the construction of this project', 'bicycles pavement markings, delineated parallel parking spaces and', 'of the assessment district to June 30, 2022. A new request for further', 'been finalized and incorporated into GIS.', 'on Pacific Coast Highway. The project reports and plans are being', 'routed through Caltrans for final approval. It is anticipated that the', 'Malibu Bluffs Park South Walkway Repairs', 'feasible traffic safety improvements can be constructed at this location.', 'meeting was held on January 20, 2022 and February 23, 2022 and', 'management.', 'In May 2021, the Council approved funding for additional engineering']}, 'var_function-call-754270318693394858': 'e project will also include the installation of new raised\nmedians on PCH in the areas where the double yellow lines exist in the vicinity\nof Zuma Beach, specifically where the yellow paddles are installed.\n\nCapital Improvement Projects (Completed)\n\nCivic Center Way Improvements\n\n(cid:190) Updates: The contractor has completed the planting material maintenance\nperiod as described within the project documents. Council accepted this\nproject as complete at the September 13th City Council Meeting.\n\nCivic Center Stormwater Diversion Structure\n\n(cid:190) Updates: The contractor has completed the storm drain improvements in the\nCivic Center Way are. The improvements modified the existing concrete\nchannel underneath Civic Center Way by adding a 3’ concrete curb adjacent\nto the existing flap gates. The new curb prevents brackish water intrusion\n\nPage 4 of 8\n\nAgenda Item # 4.A.\n\n\n\n\n\n\n\n\n\n\n\n\ninto the City’s Civic Center Stormwater Treatment Facility. This project is\nscheduled to be accepted by the', 'var_function-call-17124474351407961257': {'count': 13, 'matched_projects_list': ['PCH Median Improvements Project', 'Permanent Skate Park', 'Malibu Canyon Road Traffic Study', 'PCH at Trancas Canyon Road Right Turn Lane', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Malibu Bluffs Park South Walkway Repairs', 'Permanent Skate Park', 'Latigo Canyon Road Retaining Wall Repair Project', 'Trancas Canyon Park Playground Resurfacing', 'Storm Drain Master Plan', 'Outdoor Warning Signs', 'Westward Beach Road Drainage Improvements Project']}, 'var_function-call-17213820486225095639': [{'section': 'Capital Improvement Projects (Completed)', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'section': 'Capital Improvement Projects (Design)', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'section': 'Capital Improvement Projects (Design)', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'section': 'Capital Improvement Projects (Completed)', 'filename': 'malibucity_agenda__03232022-1869.txt'}]}

exec(code, env_args)

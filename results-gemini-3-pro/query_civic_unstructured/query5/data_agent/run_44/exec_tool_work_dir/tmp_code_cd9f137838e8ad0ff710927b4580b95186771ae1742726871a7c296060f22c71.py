code = """import json
import re

# Load data
path_civic = locals()['var_function-call-16455850891903614580']
path_funding = locals()['var_function-call-16455850891903614945']

with open(path_civic, 'r') as f:
    civic_docs = json.load(f)
with open(path_funding, 'r') as f:
    funding_records = json.load(f)

# Sort docs: Latest first
def get_date_key(fn):
    match = re.search(r'agenda_(\d{2})(\d{2})(\d{4})', fn)
    if match:
        m, d, y = match.groups()
        return y + m + d
    return "00000000"

civic_docs.sort(key=lambda x: get_date_key(x['filename']), reverse=True)

# Parse
project_data = {} # Name -> {section: set, start_date: str}
date_pattern = re.compile(r'Begin Construction:\s*(.*)', re.IGNORECASE)

def get_next_non_empty(lines, idx):
    for j in range(idx + 1, len(lines)):
        if lines[j].strip():
            return lines[j].strip()
    return None

for doc in civic_docs:
    lines = doc['text'].splitlines()
    current_section = "Unknown"
    current_project = None
    
    for i, line in enumerate(lines):
        line_strip = line.strip()
        if not line_strip: continue
        
        if "Disaster Recovery Projects" in line_strip:
            current_section = "Disaster"
            current_project = None
            continue
        elif "Capital Improvement Projects" in line_strip:
            current_section = "Capital"
            current_project = None
            continue
            
        # Project Name Detection
        next_line = get_next_non_empty(lines, i)
        if next_line:
            if "Updates" in next_line or "Project Description" in next_line:
                if "Projects" not in line_strip and "Report" not in line_strip:
                    current_project = line_strip
                    if current_project not in project_data:
                        project_data[current_project] = {"section": set(), "start_date": None}
                    
                    if current_section != "Unknown":
                        project_data[current_project]["section"].add(current_section)
    
        if current_project:
            m = date_pattern.search(line_strip)
            if m:
                # Store date only if we don't have one (Latest Wins)
                if project_data[current_project]["start_date"] is None:
                    project_data[current_project]["start_date"] = m.group(1).strip()

def normalize(name):
    name = re.sub(r'\s*\(.*?\)$', '', name)
    return name.strip()

disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Disaster"]
total_funding = 0
matched_log = []

for record in funding_records:
    amt = record['Amount']
    if isinstance(amt, str): amt = float(amt)
    fname = record['Project_Name']
    
    is_disaster = any(k in fname for k in disaster_keywords)
    norm_fname = normalize(fname)
    found_info = None
    
    # Fuzzy Matching
    if fname in project_data:
        found_info = project_data[fname]
    elif norm_fname in project_data:
        found_info = project_data[norm_fname]
    else:
        f_tokens = set(norm_fname.lower().split())
        best_k = None
        max_overlap = 0
        for k in project_data:
            k_tokens = set(normalize(k).lower().split())
            if not k_tokens: continue
            overlap = len(f_tokens.intersection(k_tokens))
            if overlap > max_overlap and overlap >= len(f_tokens) * 0.6: 
                max_overlap = overlap
                best_k = k
        if best_k:
            found_info = project_data[best_k]

    if found_info and 'Disaster' in found_info['section']:
        is_disaster = True
        
    if not is_disaster:
        continue
        
    started_2022 = False
    if found_info and found_info['start_date']:
        if "2022" in found_info['start_date']:
            started_2022 = True
            
    if started_2022:
        total_funding += amt
        matched_log.append(fname)

print("__RESULT__:")
print(json.dumps({
    "total_funding": total_funding, 
    "matched_projects": matched_log
}))"""

env_args = {'var_function-call-16455850891903611214': ['civic_docs'], 'var_function-call-16455850891903614945': 'file_storage/function-call-16455850891903614945.json', 'var_function-call-16455850891903614580': 'file_storage/function-call-16455850891903614580.json', 'var_function-call-14875208837087756201': {'total_funding': 0, 'matched_projects': []}, 'var_function-call-10353848816713242815': {'preview': ['Public Works Commission', 'Agenda Report', '', 'Public Works', 'Commission Meeting', '03-23-22', 'Item', '4.A.', '', 'To:', '', 'Chair Simmens and Members of the Public Works Commission', '', 'Prepared by:', '', 'Troy Spayd, Assistant Public Works Director/City Engineer', '', 'Approved by:', '', 'Rob DuBoux, Public Works Director/City Engineer', '', 'Date prepared: March 17, 2022', '', 'Meeting date: March 23, 2022', '', 'Subject:', '', 'Capital Improvement Projects and Disaster Recovery Projects Status', 'Report', '', 'RECOMMENDED ACTION: Receive and file report on the status of the City’s current and', 'upcoming Capital Improvements Projects and Disaster Recovery Projects.', '', 'DISCUSSION: Staff will provide a status update on the following active projects in the', 'Fiscal Year 2021-2022 Capital Improvement Program:', '', 'Capital Improvement Projects (Design)', '', 'Marie Canyon Green Streets', '(cid:190) Updates:', '', '(cid:131) A hydrology report was prepared and will be used to size the pre-', 'reviewed multiple biofilter', 'manufactured biofilters. City staff', 'manufacturers for filters that will work in the proposed project area. The', 'final design is complete and the project will be advertised for', 'construction bids.', '', '(cid:190) Project Schedule:', '', '(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Summer 2022', '', 'PCH Median Improvements Project', '', '(cid:190) Updates:', '', '(cid:131) The project was approved by the Planning Commission on September', '8, 2021. This project requires Caltrans approval since the work will be', 'on Pacific Coast Highway. The project reports and plans are being', 'routed through Caltrans for final approval. The project will have final', 'approval by the end of the March. The project will be advertised for', '', 'Page 1 of 8', '', 'Agenda Item # 4.A.', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'construction bids after approval. An agreement for construction', 'management services was approved by Council on March 14, 2022.', '', '(cid:190) Project Schedule:', '', '(cid:131) Complete Design: March 2022', '(cid:131) Advertise: Spring/Summer 2022', '(cid:131) Begin Construction: Summer 2022', '', 'PCH Signal Synchronization System Improvements Project', '', '(cid:190) Updates:', '', '(cid:131) This project will be presented to the Planning Commission in May 2022.', 'This project requires Caltrans approval since the work will be on PCH.', 'The project reports and plans are being routed through Caltrans for']}, 'var_function-call-17586832360516739618': {'total_funding': 99000.0, 'matched_projects': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)'], 'debug_missed': []}, 'var_function-call-6238217921976818581': {'total_funding': 99000.0, 'matched_projects': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)'], 'missed_match': ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Malibu Road Slope Repairs (CalOES Project)', 'Outdoor Warning Sirens (FEMA Project)', 'Outdoor Warning Sirens (FEMA)', 'Outdoor Warning Sirens - Design (FEMA Project)', 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Storm Drain Master Plan (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)'], 'matched_no_date': [{'name': 'Guardrail Replacement Citywide (FEMA Project)', 'dates': []}, {'name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'dates': []}]}, 'var_function-call-5561557172880903294': {'broad_beach_context': [['(cid:190) Updates:', '', '(cid:131) Construction was completed, January 2023', '(cid:131) Scheduled for Council acceptance on April 24, 2023', '', 'Broad Beach Road Water Quality Repair', '', '(cid:190) Updates:', '', '(cid:131) Construction was completed, November 2022', '(cid:131) Notice of completion filed January 2023', '', 'Point Dume Walkway Repairs', '(cid:190) Updates:', '']]}, 'var_function-call-10798817405730358139': {'total_funding': 0, 'matched_projects': [], 'missed_match_count': 0, 'missed_match_examples': []}, 'var_function-call-9587788539263788412': {'keys': ['Marie Canyon Green Streets', 'construction bids.', 'PCH Median Improvements Project', 'management services was approved by Council on March 14, 2022.', 'PCH Signal Synchronization System Improvements Project', 'will begin in conjunction with the PCH Median Improvement', 'Westward Beach Road Improvements Project', "Council's direction.", 'Civic Center Water Treatment Facility Phase 2', 'property owners.', 'Bluffs Park Shade Structure', 'shade structures at Malibu Bluffs Park.', 'scheduled for the April 11, 2022 Council meeting.', 'Permanent Skate Park', 'amenities such as trash cans, benches, tables, and restrooms.', 'review by the Council.', 'PCH at Trancas Canyon Road Right Turn Lane', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'Metro.', 'Vehicle Protection Devices']}, 'var_function-call-2130144800625504111': {'total_funding': 495000.0, 'matched_projects': ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)']}}

exec(code, env_args)

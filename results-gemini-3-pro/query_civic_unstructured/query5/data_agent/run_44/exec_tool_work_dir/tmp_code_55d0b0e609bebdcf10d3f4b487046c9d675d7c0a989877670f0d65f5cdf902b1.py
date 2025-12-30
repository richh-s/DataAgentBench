code = """import json
import re

# Load data
path_civic = locals()['var_function-call-16455850891903614580']
path_funding = locals()['var_function-call-16455850891903614945']

with open(path_civic, 'r') as f:
    civic_docs = json.load(f)
with open(path_funding, 'r') as f:
    funding_records = json.load(f)

# Date sort helper
def get_date_key(fn):
    # malibucity_agenda_03222023-2060.txt
    match = re.search(r'agenda_(\d{2})(\d{2})(\d{4})', fn)
    if match:
        m, d, y = match.groups()
        return y + m + d
    return "00000000"

civic_docs.sort(key=lambda x: get_date_key(x['filename']), reverse=True)

# Parse all docs
project_data = {} # Name -> {section: set(), start_dates: set()}

date_pattern = re.compile(r'Begin Construction:\s*(.*)', re.IGNORECASE)

for doc in civic_docs:
    lines = doc['text'].splitlines()
    current_section = "Unknown"
    current_project = None
    
    for i, line in enumerate(lines):
        line_strip = line.strip()
        if not line_strip:
            continue
            
        if "Disaster Recovery Projects" in line_strip:
            current_section = "Disaster"
            current_project = None
            continue
        elif "Capital Improvement Projects" in line_strip:
            current_section = "Capital"
            current_project = None
            continue
            
        # Project Name Detection
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            # Check for bullet indicators
            if next_line.startswith("(cid:190)") or next_line.startswith("Updates:") or next_line.startswith("Project Description:"):
                # Exclude headers
                if "Projects" not in line_strip and "Report" not in line_strip:
                    current_project = line_strip
                    if current_project not in project_data:
                        project_data[current_project] = {"section": set(), "start_dates": set()}
                    
                    if current_section != "Unknown":
                        project_data[current_project]["section"].add(current_section)
                        
        # Date Extraction
        if current_project:
            m = date_pattern.search(line_strip)
            if m:
                date_val = m.group(1).strip()
                project_data[current_project]["start_dates"].add(date_val)

def normalize(name):
    name = re.sub(r'\s*\(.*?\)$', '', name)
    return name.strip()

disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Disaster"]
total_funding = 0
matched_log = []
debug_missed = []

for record in funding_records:
    amt = record['Amount']
    if isinstance(amt, str):
        amt = float(amt)
    fname = record['Project_Name']
    
    # 1. Check Disaster Status
    is_disaster = False
    
    # Check Name Suffix
    if any(k in fname for k in disaster_keywords):
        is_disaster = True
        
    # Check Text Section
    norm_fname = normalize(fname)
    found_info = None
    
    # Try exact match first
    if fname in project_data:
        found_info = project_data[fname]
    # Try normalized match
    elif norm_fname in project_data:
        found_info = project_data[norm_fname]
    # Try finding fname in keys (substring)
    else:
        for k in project_data:
            if norm_fname == normalize(k):
                found_info = project_data[k]
                break
    
    if found_info and 'Disaster' in found_info['section']:
        is_disaster = True
        
    if not is_disaster:
        continue
        
    # 2. Check Start Date 2022
    # If found in text, check extracted dates.
    # If not found in text, we can't confirm date.
    
    started_2022 = False
    if found_info:
        for d in found_info['start_dates']:
            if "2022" in d:
                started_2022 = True
                break
    
    if started_2022:
        total_funding += amt
        matched_log.append(fname)
    else:
        if is_disaster and found_info:
            debug_missed.append({"name": fname, "dates": list(found_info['start_dates'])})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_projects": matched_log, "debug_missed": debug_missed[:5]}))"""

env_args = {'var_function-call-16455850891903611214': ['civic_docs'], 'var_function-call-16455850891903614945': 'file_storage/function-call-16455850891903614945.json', 'var_function-call-16455850891903614580': 'file_storage/function-call-16455850891903614580.json', 'var_function-call-14875208837087756201': {'total_funding': 0, 'matched_projects': []}, 'var_function-call-10353848816713242815': {'preview': ['Public Works Commission', 'Agenda Report', '', 'Public Works', 'Commission Meeting', '03-23-22', 'Item', '4.A.', '', 'To:', '', 'Chair Simmens and Members of the Public Works Commission', '', 'Prepared by:', '', 'Troy Spayd, Assistant Public Works Director/City Engineer', '', 'Approved by:', '', 'Rob DuBoux, Public Works Director/City Engineer', '', 'Date prepared: March 17, 2022', '', 'Meeting date: March 23, 2022', '', 'Subject:', '', 'Capital Improvement Projects and Disaster Recovery Projects Status', 'Report', '', 'RECOMMENDED ACTION: Receive and file report on the status of the City’s current and', 'upcoming Capital Improvements Projects and Disaster Recovery Projects.', '', 'DISCUSSION: Staff will provide a status update on the following active projects in the', 'Fiscal Year 2021-2022 Capital Improvement Program:', '', 'Capital Improvement Projects (Design)', '', 'Marie Canyon Green Streets', '(cid:190) Updates:', '', '(cid:131) A hydrology report was prepared and will be used to size the pre-', 'reviewed multiple biofilter', 'manufactured biofilters. City staff', 'manufacturers for filters that will work in the proposed project area. The', 'final design is complete and the project will be advertised for', 'construction bids.', '', '(cid:190) Project Schedule:', '', '(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Summer 2022', '', 'PCH Median Improvements Project', '', '(cid:190) Updates:', '', '(cid:131) The project was approved by the Planning Commission on September', '8, 2021. This project requires Caltrans approval since the work will be', 'on Pacific Coast Highway. The project reports and plans are being', 'routed through Caltrans for final approval. The project will have final', 'approval by the end of the March. The project will be advertised for', '', 'Page 1 of 8', '', 'Agenda Item # 4.A.', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'construction bids after approval. An agreement for construction', 'management services was approved by Council on March 14, 2022.', '', '(cid:190) Project Schedule:', '', '(cid:131) Complete Design: March 2022', '(cid:131) Advertise: Spring/Summer 2022', '(cid:131) Begin Construction: Summer 2022', '', 'PCH Signal Synchronization System Improvements Project', '', '(cid:190) Updates:', '', '(cid:131) This project will be presented to the Planning Commission in May 2022.', 'This project requires Caltrans approval since the work will be on PCH.', 'The project reports and plans are being routed through Caltrans for']}}

exec(code, env_args)

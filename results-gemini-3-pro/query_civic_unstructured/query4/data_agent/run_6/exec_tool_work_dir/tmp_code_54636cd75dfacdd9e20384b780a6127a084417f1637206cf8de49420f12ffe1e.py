code = """import json
import re

# Access file paths
civic_docs_path = locals()['var_function-call-8728366382386706787']
funding_data_path = locals()['var_function-call-8728366382386704966']

# Load data
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)
with open(funding_data_path, 'r') as f:
    funding_data = json.load(f)

# Funding names map
funding_map = {row['Project_Name'].strip(): row['Amount'] for row in funding_data}
funding_names = set(funding_map.keys())

# Helper to identify project name in a line
def get_project_name(line):
    line = line.strip()
    if not line: return None
    # Check exact
    if line in funding_names:
        return line
    # Check case-insensitive
    for name in funding_names:
        if line.lower() == name.lower():
            return name
        # Check if line contains name (and line is header-like)
        if name in line and len(line) < len(name) + 10:
            return name
    return None

def check_date_string(text):
    text = text.lower()
    # Check keywords
    if 'spring' in text and '2022' in text: return True
    if '2022' in text and ('march' in text or 'april' in text or 'may' in text): return True
    # Regex for 03/2022 etc
    if re.search(r'\b(03|04|05)[/-]2022', text): return True
    return False

found_projects = set()

for doc in civic_docs:
    lines = doc['text'].splitlines()
    curr_proj = None
    
    for line in lines:
        line = line.strip()
        if not line: continue
        
        # Check if project
        p_name = get_project_name(line)
        if p_name:
            curr_proj = p_name
            continue
        
        if curr_proj:
            # Check for start construction info
            low = line.lower()
            if 'construction' in low and ('begin' in low or 'start' in low):
                # Check if date is in this line
                if check_date_string(line):
                    found_projects.add(curr_proj)
            # Also check lines like "Project Schedule: Spring 2022" if keywords match?
            # But "Begin Construction" is key.
            # Maybe "Construction: Spring 2022"

# Calculate funding
total = 0
for p in found_projects:
    total += funding_map[p]

print("__RESULT__:")
print(json.dumps({
    "count": len(found_projects),
    "total_funding": total,
    "projects": list(found_projects)
}))"""

env_args = {'var_function-call-8728366382386706787': 'file_storage/function-call-8728366382386706787.json', 'var_function-call-8728366382386704966': 'file_storage/function-call-8728366382386704966.json', 'var_function-call-9080622112310942843': {'count': 0, 'total_funding': 0, 'projects': [], 'unmatched': [], 'debug_dates': {'project and will submit to the County for review.': ['131) Begin Construction'], 'or phasing out the project': ['131) Begin Construction'], '(cid:131) City working with consultant on the design of the shoulder repairs': ['131) Begin Construction'], 'cleared the project.': ['131) Begin Construction'], 'to finalize plans and specifications': ['131) Begin Construction'], '(cid:131) Awaiting final FEMA/CalOES approval for scope modification': ['131) Begin Construction'], '(cid:131) Plans and specifications are being finalized by consultant': ['131) Begin Construction'], 'Civic Center Water Treatment Facility Phase 2': ['131) Begin Construction'], 'project': ['131) Begin Construction'], 'the Spring 2023.': ['131) Begin Construction'], 'PCH Signal Synchronization System Improvements Project': ['131) Award Contract and Begin Construction'], 'Engineering, Inc.': ['131) Begin construction'], '(cid:131) Project is currently out to bid. Bids are due on March 23, 2023.': ['131) Begin construction'], 'advertised for construction bids shortly after this date.': ['131) Begin Construction'], 'agreement will be sent to City Council in March.': ['131) Begin Construction'], 'to review': ['131) Begin Construction'], 'sending this project out to bid during the Spring of 2022.': ['131) Begin Construction'], 'review by the Council.': ['131) Begin Construction', '131) Begin Construction'], 'is finalizing the bid documents.': ['131) Begin Construction', '131) Begin Construction'], 'timber with non-combustible materials.': ['131) Begin Construction', '131) Begin Construction', '131) Begin Construction', '131) Begin Construction'], '(cid:131) The project consultant has started the design of this project.': ['131) Begin Construction', '131) Begin Construction', '131) Begin Construction', '131) Begin Construction', '131) Begin Construction', '131) Begin Construction', '131) Begin Construction', '131) Begin Construction'], 'Malibu Park Drainage Improvements': ['131) Begin Construction'], 'drain towards the end of Clover Heights will help eliminate this issue.': ['131) Begin Construction', '131) Begin Construction'], 'beginning in April 2022.': ['131) Begin Construction'], 'started and is anticipated to be completed by the Spring of 2022.': ['131) Begin Construction'], 'beginning in Fall 2022.': ['131) Begin Construction', '131) Begin Construction'], 'bidding.': ['131) Begin Construction', '131) Begin Construction'], 'management.': ['131) Begin Construction', '131) Begin Construction'], '(cid:131) Consultant is working on final design documents.': ['131) Award Contract and Begin Construction', '131) Award Contract and Begin Construction'], 'the agreement.': ['131) Begin Construction', '131) Begin Construction'], 'the County and will be finalizing the design.': ['131) Begin Construction', '131) Begin Construction'], 'assessment district will be created.': ['131) Begin Construction'], 'maintenance of City streets.': ['131) Begin Construction', '131) Begin Construction'], 'post shade structures at Malibu Bluffs Park': ['131) Begin Construction', '131) Begin Construction'], 'require a vehicle impact protection device.': ['131) Begin Construction', '131) Begin Construction'], 'Road.': ['131) Begin Construction', '131) Begin Construction'], '(cid:131) The project consultant has started the design of the project.': ['131) Begin Construction', '131) Begin Construction'], 'Drainage Improvements project.': ['131) Begin Construction', '131) Begin Construction'], 'that was damaged by the Woolsey Fire.': ['131) Begin Construction', '131) Begin Construction'], 'Fire.': ['131) Begin Construction', '131) Begin Construction'], '(cid:131) Next public community meeting is scheduled for March 25th.': ['131) Begin Construction'], '(cid:131) Project is scheduled to go out to bid next week.': ['131) Begin Construction'], 'construction bids.': ['131) Begin Construction'], 'management services was approved by Council on March 14, 2022.': ['131) Begin Construction'], 'will begin in conjunction with the PCH Median Improvement': ['131) Award Contract and Begin Construction'], "Council's direction.": ['131) Begin Construction'], 'property owners.': ['131) Begin Construction'], 'scheduled for the April 11, 2022 Council meeting.': ['131) Begin Construction'], 'beginning in Spring 2022.': ['131) Begin Construction'], 'of 2022.': ['131) Begin Construction']}}, 'var_function-call-5579028219073098593': {'count': 0, 'total_funding': 0, 'projects': [], 'debug_extracted': {}}, 'var_function-call-16896492442447948674': {'sample_funding_names': ['2021 Annual Street Maintenance', '2022 Annual Street Maintenance', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Annual Street Maintenance', 'Birdview Avenue Improvements'], 'doc_lines_sample': ['Public Works Commission', 'Agenda Report', '', 'Public Works', 'Commission Meeting', '03-22-23', 'Item', '4.B.', '', 'To:', '', 'Chair Dittrich and Members of the Public Works Commission', '', 'Prepared by:', '', 'Jorge Rubalcava, Senior Civil Engineer', '', 'Approved by:', '', 'Rob DuBoux, Public Works Director/City Engineer', '', 'Date prepared: March 15, 2023', '', 'Meeting date: March 22, 2023', '', 'Subject:', '', 'Capital Improvement Projects and Disaster Recovery Projects Status', 'Report', '', 'RECOMMENDED ACTION: Receive and file report on the status of the City’s current and', 'upcoming Capital Improvement Projects and Disaster Recovery Projects.', '', 'DISCUSSION: Staff will provide a status update on the following active projects in the', 'Fiscal Year 2022-2023 Capital Improvement Program:', '', 'Capital Improvement Projects (Design)', '', '2022 Morning View Resurfacing & Storm Drain Improvements', '', '(cid:190) Updates:', '', '(cid:131) Staff is working with the consultant to finalize the design plans for this', '', 'project and will submit to the County for review.', '', '(cid:190) Project Schedule:', '', '(cid:131) Complete Design: Summer 2023', '(cid:131) Advertise: Fall 2023']}}

exec(code, env_args)

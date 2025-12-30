code = """import json

# Access file paths
civic_docs_path = locals()['var_function-call-8728366382386706787']
funding_data_path = locals()['var_function-call-8728366382386704966']

# Load data
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)
with open(funding_data_path, 'r') as f:
    funding_data = json.load(f)

# Create a set of funding project names for matching
funding_names = set()
funding_map = {}
for row in funding_data:
    name = row['Project_Name'].strip()
    funding_names.add(name)
    funding_map[name] = row['Amount']

# Normalize for fuzzy matching if needed
# But first try exact or 'in' match
# "2022 Morning View Resurfacing & Storm Drain Improvements" in text might be exact.

projects_found = {} # Name -> Start Date

def normalize(s):
    return s.lower().strip()

funding_names_norm = {normalize(n): n for n in funding_names}

def find_project_in_line(line):
    line_norm = normalize(line)
    # Check exact match
    if line_norm in funding_names_norm:
        return funding_names_norm[line_norm]
    # Check if a funding name is a substring of the line (or vice versa)
    # But be careful. "Road" is a substring of "Road Repair".
    # Project names are usually long.
    # Check if the line *starts* with a project name or *is* the project name
    for fname in funding_names:
        # If line is exactly the project name
        if line.strip() == fname:
            return fname
        # If line contains the project name and is not much longer
        # (e.g. "Project: X" or "X Project")
        if fname in line and len(line) < len(fname) + 10:
            return fname
    return None

def is_target_date(d_str):
    d = d_str.lower()
    if '2022' in d:
        if 'spring' in d: return True
        if 'march' in d or 'april' in d or 'may' in d: return True
        # "03-22", "04/2022"
        # Check simple pattern
        import re
        if re.search(r'\b(03|04|05)[/-]2022', d): return True
        if re.search(r'2022[/-](03|04|05)', d): return True
    return False

# Scan docs
for doc in civic_docs:
    lines = doc['text'].splitlines()
    curr_proj = None
    
    for line in lines:
        line = line.strip()
        if not line: continue
        
        # Check if line is a project name
        possible_proj = find_project_in_line(line)
        if possible_proj:
            curr_proj = possible_proj
            if curr_proj not in projects_found:
                projects_found[curr_proj] = []
            continue
        
        # If inside a project block, look for dates
        if curr_proj:
            low = line.lower()
            if 'begin construction' in low:
                # Extract
                parts = line.split(':')
                if len(parts) > 1:
                    val = parts[1].strip()
                    projects_found[curr_proj].append(val)

# Filter
spring_projects = set()
for p, dates in projects_found.items():
    for d in dates:
        if is_target_date(d):
            spring_projects.add(p)

# Calculate funding
total_funding = 0
for p in spring_projects:
    total_funding += funding_map.get(p, 0)

print("__RESULT__:")
print(json.dumps({
    "count": len(spring_projects),
    "total_funding": total_funding,
    "projects": list(spring_projects),
    "debug_extracted": {p: projects_found[p] for p in spring_projects}
}))"""

env_args = {'var_function-call-8728366382386706787': 'file_storage/function-call-8728366382386706787.json', 'var_function-call-8728366382386704966': 'file_storage/function-call-8728366382386704966.json', 'var_function-call-9080622112310942843': {'count': 0, 'total_funding': 0, 'projects': [], 'unmatched': [], 'debug_dates': {'project and will submit to the County for review.': ['131) Begin Construction'], 'or phasing out the project': ['131) Begin Construction'], '(cid:131) City working with consultant on the design of the shoulder repairs': ['131) Begin Construction'], 'cleared the project.': ['131) Begin Construction'], 'to finalize plans and specifications': ['131) Begin Construction'], '(cid:131) Awaiting final FEMA/CalOES approval for scope modification': ['131) Begin Construction'], '(cid:131) Plans and specifications are being finalized by consultant': ['131) Begin Construction'], 'Civic Center Water Treatment Facility Phase 2': ['131) Begin Construction'], 'project': ['131) Begin Construction'], 'the Spring 2023.': ['131) Begin Construction'], 'PCH Signal Synchronization System Improvements Project': ['131) Award Contract and Begin Construction'], 'Engineering, Inc.': ['131) Begin construction'], '(cid:131) Project is currently out to bid. Bids are due on March 23, 2023.': ['131) Begin construction'], 'advertised for construction bids shortly after this date.': ['131) Begin Construction'], 'agreement will be sent to City Council in March.': ['131) Begin Construction'], 'to review': ['131) Begin Construction'], 'sending this project out to bid during the Spring of 2022.': ['131) Begin Construction'], 'review by the Council.': ['131) Begin Construction', '131) Begin Construction'], 'is finalizing the bid documents.': ['131) Begin Construction', '131) Begin Construction'], 'timber with non-combustible materials.': ['131) Begin Construction', '131) Begin Construction', '131) Begin Construction', '131) Begin Construction'], '(cid:131) The project consultant has started the design of this project.': ['131) Begin Construction', '131) Begin Construction', '131) Begin Construction', '131) Begin Construction', '131) Begin Construction', '131) Begin Construction', '131) Begin Construction', '131) Begin Construction'], 'Malibu Park Drainage Improvements': ['131) Begin Construction'], 'drain towards the end of Clover Heights will help eliminate this issue.': ['131) Begin Construction', '131) Begin Construction'], 'beginning in April 2022.': ['131) Begin Construction'], 'started and is anticipated to be completed by the Spring of 2022.': ['131) Begin Construction'], 'beginning in Fall 2022.': ['131) Begin Construction', '131) Begin Construction'], 'bidding.': ['131) Begin Construction', '131) Begin Construction'], 'management.': ['131) Begin Construction', '131) Begin Construction'], '(cid:131) Consultant is working on final design documents.': ['131) Award Contract and Begin Construction', '131) Award Contract and Begin Construction'], 'the agreement.': ['131) Begin Construction', '131) Begin Construction'], 'the County and will be finalizing the design.': ['131) Begin Construction', '131) Begin Construction'], 'assessment district will be created.': ['131) Begin Construction'], 'maintenance of City streets.': ['131) Begin Construction', '131) Begin Construction'], 'post shade structures at Malibu Bluffs Park': ['131) Begin Construction', '131) Begin Construction'], 'require a vehicle impact protection device.': ['131) Begin Construction', '131) Begin Construction'], 'Road.': ['131) Begin Construction', '131) Begin Construction'], '(cid:131) The project consultant has started the design of the project.': ['131) Begin Construction', '131) Begin Construction'], 'Drainage Improvements project.': ['131) Begin Construction', '131) Begin Construction'], 'that was damaged by the Woolsey Fire.': ['131) Begin Construction', '131) Begin Construction'], 'Fire.': ['131) Begin Construction', '131) Begin Construction'], '(cid:131) Next public community meeting is scheduled for March 25th.': ['131) Begin Construction'], '(cid:131) Project is scheduled to go out to bid next week.': ['131) Begin Construction'], 'construction bids.': ['131) Begin Construction'], 'management services was approved by Council on March 14, 2022.': ['131) Begin Construction'], 'will begin in conjunction with the PCH Median Improvement': ['131) Award Contract and Begin Construction'], "Council's direction.": ['131) Begin Construction'], 'property owners.': ['131) Begin Construction'], 'scheduled for the April 11, 2022 Council meeting.': ['131) Begin Construction'], 'beginning in Spring 2022.': ['131) Begin Construction'], 'of 2022.': ['131) Begin Construction']}}}

exec(code, env_args)

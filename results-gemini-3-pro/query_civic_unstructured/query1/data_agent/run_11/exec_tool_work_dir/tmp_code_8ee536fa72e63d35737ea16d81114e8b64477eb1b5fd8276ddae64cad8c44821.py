code = """import json
import datetime
import re

# Load data
with open(locals()['var_function-call-9221482571475141474'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-17488906604846225691'], 'r') as f:
    civic_docs = json.load(f)

# Filter candidates: Capital projects with Funding > 50,000
# Note: Funding table doesn't have "Type". Type is in the text.
# So we filter by Amount here, and check Type (Capital) via the text section.
candidates = set()
for row in funding_data:
    try:
        amt = float(row['Amount'])
        if amt > 50000:
            candidates.add(row['Project_Name'].strip())
    except:
        pass

# Helper to parse date
def parse_date(filename):
    # format: malibucity_agenda__01262022-1835.txt
    # regex for MMDDYYYY
    match = re.search(r'(\d{8})', filename)
    if match:
        d_str = match.group(1)
        return datetime.datetime.strptime(d_str, "%m%d%Y")
    return datetime.datetime.min

# Sort docs by date (latest last)
civic_docs.sort(key=lambda x: parse_date(x['filename']))

# Tracking latest status
# project_status = { project_name: (status, type) }
project_status = {}

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_section = None
    # Section types: 'CAP_DESIGN', 'CAP_OTHER', 'DISASTER', 'OTHER'
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        # Check for headers
        # Use simple string checks as seen in the sample
        if "Capital Improvement Projects (Design)" in line_clean:
            current_section = 'CAP_DESIGN'
            continue
        elif "Capital Improvement Projects (Construction)" in line_clean:
            current_section = 'CAP_OTHER' # Construction
            continue
        elif "Capital Improvement Projects (Not Started)" in line_clean:
            current_section = 'CAP_OTHER' # Not Started
            continue
        elif "Disaster Recovery Projects" in line_clean:
            current_section = 'DISASTER'
            continue
        elif "Agenda Item" in line_clean and "Page" in line_clean:
            # Footer, ignore
            continue
            
        # If inside a section, check if line is a project name
        if current_section:
            if line_clean in candidates:
                # We found a project in a specific section
                # Determine status/type
                if current_section == 'CAP_DESIGN':
                    project_status[line_clean] = ('design', 'capital')
                elif current_section == 'CAP_OTHER':
                    project_status[line_clean] = ('other', 'capital')
                elif current_section == 'DISASTER':
                    project_status[line_clean] = ('other', 'disaster')
                # If section is unknown, keep previous or ignore?
                # We overwrite with the latest finding in the latest doc.

# Count projects with status 'design' and type 'capital'
count = 0
result_projects = []
for p, (stat, typ) in project_status.items():
    if stat == 'design' and typ == 'capital':
        count += 1
        result_projects.append(p)

print("__RESULT__:")
print(json.dumps({"count": count, "projects": result_projects}))"""

env_args = {'var_function-call-12957010085961315651': ['Funding'], 'var_function-call-12957010085961315256': ['civic_docs'], 'var_function-call-9221482571475141474': 'file_storage/function-call-9221482571475141474.json', 'var_function-call-9221482571475141387': 'file_storage/function-call-9221482571475141387.json', 'var_function-call-17488906604846225691': 'file_storage/function-call-17488906604846225691.json'}

exec(code, env_args)

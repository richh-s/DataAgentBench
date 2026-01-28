code = """import json
import re
from datetime import datetime

# Load funding data
# Variable names from previous outputs
funding_file = locals()['var_function-call-4778954659486180916']
docs_file = locals()['var_function-call-10827667462848878709']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Filter funding > 50,000
# Ensure Amount is parsed as int/float
funding_high = set()
for r in funding_data:
    try:
        amt = float(r['Amount'])
        if amt > 50000:
            funding_high.add(r['Project_Name'])
    except:
        continue

# Load docs
with open(docs_file, 'r') as f:
    docs = json.load(f)

# Tracker: ProjectName -> (Date, Status)
project_tracker = {}

# Regex to identify sections
# We look for "Capital Improvement Projects (Status)"
# And capture content until the next major header.
# Headers observed: 
# Capital Improvement Projects (Design)
# Capital Improvement Projects (Construction)
# Capital Improvement Projects (Not Started)
# Disaster Recovery Projects
# The lookahead checks for the start of another Capital/Disaster header or end of string.
section_pattern = re.compile(
    r'Capital Improvement Projects \((Design|Construction|Not Started)\)(.*?)(?=Capital Improvement Projects|Disaster Recovery Projects|Staff has also prepared|Agenda Item|$)', 
    re.DOTALL | re.IGNORECASE
)

for doc in docs:
    fname = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Parse date
    # malibucity_agenda_03222023-2060.txt -> 03222023
    # Use strict regex to avoid partial numbers
    date_match = re.search(r'_(\d{8})', fname)
    if not date_match:
        continue
    
    date_str = date_match.group(1)
    try:
        doc_date = datetime.strptime(date_str, "%m%d%Y")
    except ValueError:
        continue
        
    # Find all capital sections
    matches = section_pattern.findall(text)
    
    for status_str, content in matches:
        # status_str is 'Design', 'Construction', 'Not Started'
        current_status = status_str.lower() # 'design', 'construction', 'not started'
        
        # Split content into lines and find project names
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Check exact match
            if line in funding_high:
                # Update tracker
                # We want the status from the latest document
                if line not in project_tracker:
                    project_tracker[line] = (doc_date, current_status)
                else:
                    stored_date, stored_status = project_tracker[line]
                    if doc_date >= stored_date:
                        project_tracker[line] = (doc_date, current_status)

# Count projects with status 'design'
design_count = 0
design_projects = []
for name, (date, status) in project_tracker.items():
    if status == 'design':
        design_count += 1
        design_projects.append(name)

print("__RESULT__:")
print(json.dumps({"count": design_count, "projects": design_projects}))"""

env_args = {'var_function-call-4778954659486180916': 'file_storage/function-call-4778954659486180916.json', 'var_function-call-4778954659486182233': 'file_storage/function-call-4778954659486182233.json', 'var_function-call-10827667462848878709': 'file_storage/function-call-10827667462848878709.json'}

exec(code, env_args)

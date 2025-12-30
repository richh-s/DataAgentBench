code = """import json
import re
from datetime import datetime

# Load data
funding_data = json.load(open(locals()['var_function-call-6229700754411909413'])) # > 50k
civic_docs = json.load(open(locals()['var_function-call-10406381100276321723']))

# Prepare funding map: Name -> Amount (for > 50k projects)
# Normalize names for easier matching? Let's keep original for now and normalize during match.
target_projects = {}
for rec in funding_data:
    try:
        amt = float(rec['Amount'])
    except:
        amt = 0
    if amt > 50000:
        target_projects[rec['Project_Name']] = amt

# Sort docs by date
def get_date(filename):
    # malibucity_agenda_03222023-2060.txt
    match = re.search(r'(\d{8})', filename)
    if match:
        return datetime.strptime(match.group(1), '%m%d%Y')
    return datetime.min

civic_docs.sort(key=lambda x: get_date(x['filename']))

# Track status: name -> status
# We only care about projects in target_projects.
project_status = {name: None for name in target_projects}

def normalize(s):
    return re.sub(r'\s+', ' ', s).strip().lower()

# Pre-compute normalized target names
norm_targets = {name: normalize(name) for name in target_projects}

def find_matches(section_text, status_label):
    # Split into lines
    lines = section_text.split('\n')
    # Identify potential headers. 
    # A header is a line that is followed by a line starting with (cid:190) or Updates:
    # We iterate and check.
    
    # Actually, simpler approach:
    # Iterate over all target projects. Check if their name (fuzzy) appears in the section text.
    # BUT, we need to associate it with a specific "block" to be sure it's a project listing.
    # However, the sections are "Capital Projects (Design)". Anything listed there is a project in design.
    # So if "Project X" name is present in that section, it's likely the project.
    # Risk: "Project X" is mentioned in the description of "Project Y".
    # Structure:
    # Project Name
    # (cid:190) Updates:
    # So the project name is a distinct line.
    
    # Let's extract all "clean" lines that precede `(cid:190)` lines.
    found_names = []
    
    # Clean text to handle bullets
    # cid:190 is a bullet.
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        # Check if this line is a project header.
        # It should NOT start with `(cid:`.
        # It should be followed by a line starting with `(cid:190)` or `Updates:` or `Project Description:`
        # Look ahead (skip empty lines)
        is_header = False
        for j in range(i+1, len(lines)):
            next_line = lines[j].strip()
            if not next_line: continue
            if next_line.startswith('(cid:190)') or next_line.startswith('Updates:') or next_line.startswith('Project Description:'):
                is_header = True
            break
        
        if is_header:
            # This line is likely a project name.
            # Try to match with target_projects
            cleaned_line = normalize(line)
            
            # Find best match in norm_targets
            best_match = None
            max_len = 0
            
            for real_name, norm_name in norm_targets.items():
                # Check for containment
                # If extracted line contains DB name, or DB name contains extracted line (less likely for header)
                # "Clover Heights Storm Drainage Improvements" contains "clover heights storm drain"
                if norm_name in cleaned_line:
                    if len(norm_name) > max_len:
                        max_len = len(norm_name)
                        best_match = real_name
                elif cleaned_line in norm_name:
                     if len(cleaned_line) > max_len:
                        max_len = len(cleaned_line)
                        best_match = real_name
            
            if best_match:
                project_status[best_match] = status_label
                # print(f"Matched {best_match} in {status_label}")

# Sections to look for
SECTIONS = [
    ("Capital Improvement Projects (Design)", "design"),
    ("Capital Improvement Projects (Construction)", "construction"),
    ("Capital Improvement Projects (Not Started)", "not started")
]

for doc in civic_docs:
    text = doc['text']
    # Normalize text newlines
    text = text.replace('\r\n', '\n')
    
    # We need to find the sections.
    # They appear in order? Or just search for headers.
    # Headers are: "Capital Improvement Projects (Design)", "Capital Improvement Projects (Construction)", ...
    # We can use regex to find start indices.
    
    # Construct a map of section_start -> section_type
    starts = []
    for header, label in SECTIONS:
        # Case insensitive search
        matches = list(re.finditer(re.escape(header), text, re.IGNORECASE))
        for m in matches:
            starts.append((m.start(), label))
            
    # Also find "Disaster Recovery Projects" to mark end of Capital sections?
    # Or just "Agenda Item" or "Public Works" headers?
    # Let's find all section headers to determine boundaries.
    # We add a dummy end.
    starts.append((len(text), "END"))
    starts.sort()
    
    for k in range(len(starts) - 1):
        start_idx, label = starts[k]
        end_idx = starts[k+1][0]
        
        if label == "END": continue
        
        # Determine if this block is valid or just a mention?
        # The headers seem distinct.
        
        section_content = text[start_idx:end_idx]
        find_matches(section_content, label)

# Count 'design'
count = 0
design_projects = []
for name, status in project_status.items():
    if status == 'design':
        count += 1
        design_projects.append(name)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_function-call-6229700754411909413': 'file_storage/function-call-6229700754411909413.json', 'var_function-call-6229700754411910276': 'file_storage/function-call-6229700754411910276.json', 'var_function-call-10406381100276321723': 'file_storage/function-call-10406381100276321723.json'}

exec(code, env_args)

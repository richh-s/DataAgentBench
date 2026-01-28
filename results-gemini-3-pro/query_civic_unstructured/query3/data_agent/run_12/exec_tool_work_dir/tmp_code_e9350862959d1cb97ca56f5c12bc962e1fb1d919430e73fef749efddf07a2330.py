code = """import json
import re

# Load data
funding = json.load(open(locals()['var_function-call-11245625895433682474']))
civic_docs = json.load(open(locals()['var_function-call-11245625895433679723']))

# Combine text from all docs (though likely just one or a few)
full_text_lines = []
for doc in civic_docs:
    full_text_lines.extend(doc['text'].split('\n'))

# Parse text to extract projects
# Structure: Header -> Projects
# Project: Name (line) -> Bullets (text)
projects_extracted = {} # Name -> {status, text, type}

current_status = "unknown"
current_type = "capital" # Default or based on section
capture_mode = False

# Regex for headers
# "Capital Improvement Projects (Design)"
# "Capital Improvement Projects (Construction)"
# "Capital Improvement Projects (Not Started)"
# Maybe "Disaster Recovery Projects"?

current_project_name = None
current_project_text = []

ignore_lines = ["Public Works Commission", "Agenda Report", "Page ", "Agenda Item", "Prepared by", "Approved by", "Subject:", "RECOMMENDED ACTION", "DISCUSSION"]

def save_project(name, status, text_lines, p_type):
    if name and name not in projects_extracted:
        full_text = " ".join(text_lines)
        # Refine status based on text
        final_status = status
        if status == "construction":
            if "construction was completed" in full_text.lower() or "notice of completion" in full_text.lower():
                final_status = "completed"
            elif "project is currently under construction" in full_text.lower():
                 final_status = "construction" # Keep as construction or map to design? Keeping as construction.
        
        projects_extracted[name] = {
            "status": final_status,
            "text": full_text,
            "type": p_type
        }

for line in full_text_lines:
    line_stripped = line.strip()
    if not line_stripped:
        continue
        
    # Check headers
    if "Capital Improvement Projects (Design)" in line:
        current_status = "design"
        current_type = "capital"
        capture_mode = True
        current_project_name = None
        continue
    elif "Capital Improvement Projects (Construction)" in line:
        current_status = "construction"
        current_type = "capital"
        capture_mode = True
        current_project_name = None
        continue
    elif "Capital Improvement Projects (Not Started)" in line:
        current_status = "not started"
        current_type = "capital"
        capture_mode = True
        current_project_name = None
        continue
    elif "Disaster Recovery Projects" in line: # Hypothesis
        current_status = "design" # Assumption, or read text
        current_type = "disaster"
        capture_mode = True
        current_project_name = None
        continue
        
    if not capture_mode:
        continue
        
    # Check for noise
    if any(x in line for x in ignore_lines) or re.match(r'Page \d+ of \d+', line):
        continue
        
    # Check for bullets
    if line_stripped.startswith("(cid:190)") or line_stripped.startswith("(cid:131)"):
        if current_project_name:
            current_project_text.append(line_stripped)
    else:
        # Potential new project name
        # Save previous
        if current_project_name:
            save_project(current_project_name, current_status, current_project_text, current_type)
        
        current_project_name = line_stripped
        current_project_text = []

# Save last
if current_project_name:
    save_project(current_project_name, current_status, current_project_text, current_type)

# Match with Funding
results = []
keywords = ['emergency', 'fema']

# Helper to find status
def get_status_from_extracted(f_name):
    # 1. Exact match
    if f_name in projects_extracted:
        return projects_extracted[f_name]
    
    # 2. Strip suffixes
    # Suffixes: (FEMA Project), (CalOES Project), (CalJPIA Project), (FEMA/CalOES Project)
    # Also handle (FEMA), (CalOES)
    base_name = re.sub(r'\s*\((FEMA|CalOES|CalJPIA|FEMA/CalOES).*?\)', '', f_name).strip()
    if base_name in projects_extracted:
        return projects_extracted[base_name]
    
    # 3. Prefix match (longest extracted name that is a prefix of f_name)
    # This handles "Outdoor Warning Sirens - Design" vs "Outdoor Warning Sirens"
    # Actually, extracted might be shorter.
    # Extracted: "Outdoor Warning Sirens"
    # Funding: "Outdoor Warning Sirens - Design (FEMA Project)"
    # Base Name: "Outdoor Warning Sirens - Design"
    # Match? No.
    # Try finding extracted key that is substring of f_name?
    # But be careful of false positives.
    # "Outdoor Warning Sirens" is in "Outdoor Warning Sirens - Design"
    
    candidates = []
    for k in projects_extracted:
        if k in f_name:
            candidates.append(k)
    if candidates:
        # Pick longest match
        best = max(candidates, key=len)
        return projects_extracted[best]
        
    return None

for record in funding:
    p_name = record['Project_Name']
    p_source = record['Funding_Source']
    p_amount = record['Amount']
    
    # Check relevance
    is_related = False
    
    # Check name for keywords
    if any(k in p_name.lower() for k in keywords):
        is_related = True
        
    # Find info from text
    info = get_status_from_extracted(p_name)
    
    if info:
        # Check text/topic for keywords
        if any(k in info['text'].lower() for k in keywords) or any(k in p_name.lower() for k in keywords):
            is_related = True
            
        # Also, check if "Disaster" type
        if info['type'] == 'disaster':
            # Maybe relevant? Prompt says 'emergency' or 'FEMA'. Disaster is close. 
            # But let's stick to strict keywords unless inferred.
            pass
            
    if is_related:
        status = info['status'] if info else "not started" # Default if not found? Or "Unknown"?
        # If not in text, implies "not started" or just missing? 
        # "Projects have three statuses... not started (identified but not begun)".
        # If it's in funding but not in the agenda report, maybe it's not active/started?
        # I'll default to "not started" or "Unknown". "not started" is safer given the options.
        
        results.append({
            "Project_Name": p_name,
            "Funding_Source": p_source,
            "Amount": p_amount,
            "Status": status
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-11245625895433682474': 'file_storage/function-call-11245625895433682474.json', 'var_function-call-11245625895433679723': 'file_storage/function-call-11245625895433679723.json'}

exec(code, env_args)

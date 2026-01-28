code = """import json
import re

# Load Funding Data
with open(locals()['var_function-call-14368692439626518277'], 'r') as f:
    funding_data = json.load(f)

# Load Civic Docs Data
with open(locals()['var_function-call-10213598713218167790'], 'r') as f:
    civic_docs = json.load(f)

park_keywords = ["park", "playground", "recreation", "trail", "open space", "walkway"] 

completed_projects = set()
debug_log = []

for doc in civic_docs:
    text = doc['text']
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    current_section = None
    
    # Simple parser
    # We'll identify project blocks.
    # A project name is usually a line that does not start with bullet points.
    
    # Bullets in the text seem to be represented by (cid:190) which is \u00be (fraction 3/4) and (cid:131) which is \u0192 (function symbol) or similar?
    # The OCR text provided in preview has "(cid:190)" text literal.
    
    # Let's iterate and group lines by project.
    
    projects = []
    current_proj_name = None
    current_proj_text = []
    
    for line in lines:
        # Check for Section Headers
        if "Capital Improvement Projects" in line:
            current_section = line
            continue
        
        # Check for skip lines
        if "Agenda Item" in line or "Page " in line or line.startswith("To:") or line.startswith("From:") or line.startswith("Subject:"):
            continue
            
        # Check for Project Start
        # Heuristic: Line doesn't start with (cid:...) and is not a keyword line
        if not line.startswith("(cid:") and not line.startswith("Updates:") and not line.startswith("Project Schedule:") and not line.startswith("Project Description:") and not line.startswith("Complete Construction:") and not line.startswith("Begin Construction:"):
            # Also check length and casing to avoid noise?
            # Project names are usually significant length.
            # But let's assume any such line starts a new project block or is noise.
            # If we were collecting a project, save it.
            
            if current_proj_name:
                projects.append({'name': current_proj_name, 'text': "\n".join(current_proj_text)})
            
            current_proj_name = line
            current_proj_text = []
        else:
            # It's content for the current project
            if current_proj_name:
                current_proj_text.append(line)
    
    # Add last project
    if current_proj_name:
        projects.append({'name': current_proj_name, 'text': "\n".join(current_proj_text)})

    # Now analyze extracted projects
    for p in projects:
        p_name = p['name']
        p_text = p['text'].lower()
        
        # Cleanup name
        # Sometimes name might have trailing chars or be split?
        # Assuming the heuristic worked reasonably well.
        
        # Check if park related
        is_park = False
        if any(k in p_name.lower() for k in park_keywords):
            is_park = True
        
        # Check if completed in 2022
        is_completed_2022 = False
        
        # Look for specific phrases in the text
        # "Construction was completed November 2022"
        # "Construction was completed, November 2022"
        # "Notice of completion filed January 2023" (implies completion before)
        
        if "completed" in p_text and "2022" in p_text:
            # Check proximity or pattern
            if re.search(r"completed[,]? [a-z]+ 2022", p_text) or \
               re.search(r"completed [a-z]+ 2022", p_text) or \
               re.search(r"complete construction: [a-z]+ 2022", p_text):
                is_completed_2022 = True
                
        if is_park and is_completed_2022:
            completed_projects.add(p_name)
            debug_log.append({"name": p_name, "status": "MATCHED"})

# Match with Funding
total_funding = 0
matched_records = []

# Clean names
# Remove extra spaces
target_names = {n.strip() for n in completed_projects}

for record in funding_data:
    r_name = record['Project_Name'].strip()
    # Direct match?
    if r_name in target_names:
        total_funding += int(record['Amount'])
        matched_records.append(record)
    else:
        # Fuzzy match? Or partial match?
        # "Bluffs Park Shade Structure" vs "Bluffs Park Shade Structure"
        pass

print("__RESULT__:")
print(json.dumps({
    "target_projects": list(target_names),
    "total_funding": total_funding,
    "matched_records": matched_records
}))"""

env_args = {'var_function-call-2808116990881149214': ['Funding'], 'var_function-call-2808116990881151343': ['civic_docs'], 'var_function-call-14368692439626518277': 'file_storage/function-call-14368692439626518277.json', 'var_function-call-14368692439626518412': 'file_storage/function-call-14368692439626518412.json', 'var_function-call-10213598713218167790': 'file_storage/function-call-10213598713218167790.json'}

exec(code, env_args)

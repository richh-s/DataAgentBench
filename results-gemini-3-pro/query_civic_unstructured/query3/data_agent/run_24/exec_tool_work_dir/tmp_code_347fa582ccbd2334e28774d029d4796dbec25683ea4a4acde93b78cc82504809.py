code = """import json
import re

# Load data
with open(locals()['var_function-call-2028314322626917702'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-10132172204667131329'], 'r') as f:
    civic_docs = json.load(f)

projects_extracted = []

def get_status_from_section(section_name, text_block):
    # Hint: Projects have three statuses: "design", "completed", "not started"
    # Map section to status
    status = "Unknown"
    if "Design" in section_name:
        status = "design"
    elif "Not Started" in section_name:
        status = "not started"
    elif "Construction" in section_name:
        if "completed" in text_block.lower():
            status = "completed"
        elif "under construction" in text_block.lower():
            status = "construction" # Or map to 'design' if strict? keeping 'construction' is safer or 'design' if hint is strict. 
            # Hint says 'design' is 'planning/design phase'. Construction is execution.
            # I will use 'construction' if found, but note the hint might be incomplete or I should just report what I see.
            # However, looking at the result requirements, 'statuses' are asked.
            status = "construction"
    
    # Override if text explicitly says something else?
    if "notice of completion filed" in text_block.lower():
        status = "completed"
    
    return status

def is_emergency_or_fema(name, text):
    keywords = ['emergency', 'fema']
    content = (name + " " + text).lower()
    for k in keywords:
        if k in content:
            return True
    return False

# Regex patterns
header_pattern = re.compile(r"(Capital Improvement Projects|Disaster Recovery Projects)\s*\((Design|Construction|Not Started|Completed|.*)\)", re.IGNORECASE)
# Bullet pattern: (cid:190) is often decoded as something else or just text. In the preview it is (cid:190).
# We look for a line that is followed by a line starting with (cid:190) or Updates:
# Actually, we can iterate lines.

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_section = None
    current_status_hint = None
    
    # We need to group lines into projects.
    # A project starts with a Name line, followed by details.
    # Sections are headers.
    
    # Iterate and parse
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        
        # Check for Section Header
        match = header_pattern.search(line)
        if match:
            current_section = match.group(0)
            # e.g. "Capital Improvement Projects (Design)"
            i += 1
            continue
        
        if current_section:
            # Check if this line is a project name
            # Heuristic: The line is not empty, does not start with (cid:190) or (cid:131) (bullets), and next line starts with (cid:190) or "Updates:" or "Project Description:"
            is_project = False
            if i + 1 < len(lines):
                next_line = lines[i+1].strip()
                if next_line.startswith("(cid:190)") or next_line.startswith("Updates:") or next_line.startswith("Project Description:"):
                    is_project = True
            
            # Also sometimes there are empty lines between name and updates
            if not is_project and i + 2 < len(lines) and not lines[i+1].strip():
                 next_next_line = lines[i+2].strip()
                 if next_next_line.startswith("(cid:190)") or next_next_line.startswith("Updates:") or next_next_line.startswith("Project Description:"):
                     is_project = True

            if is_project:
                project_name = line
                # Extract block
                block_lines = []
                j = i + 1
                while j < len(lines):
                    l = lines[j].strip()
                    # Stop if we hit a new section header
                    if header_pattern.search(l):
                        break
                    # Stop if we hit a new project name?
                    # How to detect next project name? 
                    # Use the same heuristic: l is name if next line is bullet.
                    # But we need to be careful not to consume the next project's name.
                    
                    is_next_project = False
                    if l and not l.startswith("(cid:190)") and not l.startswith("(cid:131)"):
                         # Check ahead
                         # But wait, lines within a project can be just text.
                         # The key structure is the bullet points start the details.
                         # Project name is usually bold or standalone.
                         # Let's assume project name is followed by bullet.
                         # So if we see a line followed by bullet, it's a start of NEW project (unless it's the current one's start).
                         
                         # Check if l is start of new project
                         if j + 1 < len(lines):
                            nl = lines[j+1].strip()
                            if nl.startswith("(cid:190)") or nl.startswith("Updates:") or nl.startswith("Project Description:"):
                                is_next_project = True
                         elif j + 2 < len(lines) and not lines[j+1].strip():
                            nnl = lines[j+2].strip()
                            if nnl.startswith("(cid:190)") or nnl.startswith("Updates:") or nnl.startswith("Project Description:"):
                                is_next_project = True
                    
                    if is_next_project:
                        break
                    
                    block_lines.append(l)
                    j += 1
                
                block_text = "\n".join(block_lines)
                
                # Analyze
                if is_emergency_or_fema(project_name, block_text):
                    status = get_status_from_section(current_section, block_text)
                    projects_extracted.append({
                        "Project_Name": project_name,
                        "Status": status,
                        "Raw_Name": project_name,
                        "Text": block_text
                    })
                
                i = j - 1 # process the next line in next iteration (which is the new project name)
        
        i += 1

# Now join with funding
results = []
seen_funding_ids = set()

# Normalize function
def normalize(name):
    return name.lower().replace("(fema project)", "").replace("(caloes project)", "").replace("(fema/caloes project)", "").strip()

for p in projects_extracted:
    p_norm = normalize(p['Project_Name'])
    
    # Find matches in funding
    matched = False
    for f in funding_data:
        f_name = f['Project_Name']
        f_norm = normalize(f_name)
        
        # Match logic: Exact or Funding starts with Project (e.g. "Name (FEMA Project)")
        # or Project starts with Funding (unlikely if funding has suffixes)
        # or Fuzzy?
        
        # Check if project name is in funding name or vice versa
        # Given "Latigo Canyon Road Retaining Wall Repair Project" in text
        # Funding: "Latigo Canyon Road Retaining Wall Repair Project" (ID 45)
        # Funding: "Latigo Canyon Road Retaining Wall Repair Project (FEMA Project)" (ID 47 - wait, this is 'Roadway/Retaining Wall Improvements')
        # Let's look closer at ID 47: "Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)"
        # Text has: "Latigo Canyon Road Retaining Wall Repair Project"
        # Match ID 45? Yes.
        
        # What about "Outdoor Warning Sirens"?
        # Text: "Outdoor Warning Sirens"
        # Funding: "Outdoor Warning Sirens" (65), "Outdoor Warning Sirens (FEMA Project)" (66), "Outdoor Warning Sirens (FEMA)" (67).
        # Should we include all?
        # The query asks for "project names, funding sources... for projects related to 'emergency' or 'FEMA'".
        # The project in text IS related to FEMA/Emergency.
        # It maps to multiple funding entries. I should probably list all funding sources for that project name.
        
        is_match = False
        if p_norm == f_norm:
            is_match = True
        elif f_norm.startswith(p_norm):
             is_match = True
        elif p_norm.startswith(f_norm):
             is_match = True
        
        # Also check for " (FEMA Project)" suffix in original name handled by normalize
        # But if p_norm is "outdoor warning sirens" and f_norm is "outdoor warning sirens", match.
        
        if is_match:
            # Avoid duplicates? A project might be mentioned in multiple docs.
            # But we are iterating extracted projects.
            # We should dedup based on (Project Name, Funding Source, Amount) or just Funding ID.
            
            # Create result entry
            # Check if this funding record is already added for this project name (from another doc?)
            # I'll add all matches and then uniqueify.
            
            results.append({
                "Project_Name": f['Project_Name'], # Use Funding Name to be precise
                "Funding_Source": f['Funding_Source'],
                "Amount": f['Amount'],
                "Status": p['Status']
            })
            matched = True
            
    if not matched:
        # Maybe filtering was too strict?
        # Or project has no funding?
        pass

# Deduplicate results
unique_results = []
seen = set()
for r in results:
    key = (r['Project_Name'], r['Funding_Source'], r['Amount'], r['Status'])
    if key not in seen:
        seen.add(key)
        unique_results.append(r)

print("__RESULT__:")
print(json.dumps(unique_results))"""

env_args = {'var_function-call-2105256659697284702': ['civic_docs'], 'var_function-call-2105256659697283933': ['Funding'], 'var_function-call-2028314322626917702': 'file_storage/function-call-2028314322626917702.json', 'var_function-call-2028314322626917971': 'file_storage/function-call-2028314322626917971.json', 'var_function-call-4575957102787257553': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}], 'var_function-call-10132172204667131329': 'file_storage/function-call-10132172204667131329.json'}

exec(code, env_args)

code = """import json
import re

# Load data
with open(locals()['var_function-call-4694039731328856667'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-11052254391267769107'], 'r') as f:
    civic_docs = json.load(f)

# Create a map of Project Name to Funding Info
funding_map = {item['Project_Name']: item for item in funding_data}

# Prepare to extract projects from text
# We'll assume project names in text match keys in funding_map
# But we need to handle the structure of the document.

extracted_projects = []

# Known statuses from hint, we might use them for normalization
# "design", "completed", "not started"

# Regex to find section headers
section_regex = re.compile(r'(Capital Improvement Projects|Disaster Recovery Projects)\s*\((Design|Construction|Not Started)\)', re.IGNORECASE)

# Iterate over documents
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_status_section = None
    current_project_name = None
    current_project_text = []
    
    # We need to identify when a new project starts.
    # A project starts with a line that matches a project name in funding_map?
    # Or matches a known pattern?
    
    # Let's iterate line by line
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
            
        # Check for section header
        sec_match = section_regex.search(stripped)
        if sec_match:
            # New section
            # Save previous project if exists
            if current_project_name:
                extracted_projects.append({
                    'name': current_project_name,
                    'section_status': current_status_section,
                    'text': "\n".join(current_project_text)
                })
                current_project_name = None
                current_project_text = []
            
            # Determine status from header
            header_type = sec_match.group(2).lower()
            if 'design' in header_type:
                current_status_section = 'design'
            elif 'not started' in header_type:
                current_status_section = 'not started'
            elif 'construction' in header_type:
                current_status_section = 'construction' # Will refine later
            else:
                current_status_section = 'unknown'
            continue
        
        # Check if line is a project name
        # We check exact match or close match against funding_map keys
        # But there are many keys. 
        # Also project name usually appears on a line by itself.
        # Let's check if stripped line is in funding_map keys.
        
        is_project_start = False
        matched_name = None
        
        if stripped in funding_map:
            is_project_start = True
            matched_name = stripped
        else:
            # Try to see if the line is contained in a key or vice versa, but be careful of false positives.
            # "Outdoor Warning Signs" vs "Outdoor Warning Sirens"
            # In the text preview: "Outdoor Warning Signs" is a line.
            # "Outdoor Warning Sirens" is a line.
            # "2022 Morning View Resurfacing & Storm Drain Improvements" is a line.
            # Some names in DB have (FEMA Project). The text might not.
            # If text line matches the START of a DB name?
            # e.g. Text: "Outdoor Warning Sirens", DB: "Outdoor Warning Sirens (FEMA Project)"
            # But "Outdoor Warning Sirens" is also a DB entry.
            # We prefer exact match.
            pass

        if is_project_start:
            # Save previous
            if current_project_name:
                extracted_projects.append({
                    'name': current_project_name,
                    'section_status': current_status_section,
                    'text': "\n".join(current_project_text)
                })
            current_project_name = matched_name
            current_project_text = []
        else:
            # Append line to current project text
            if current_project_name:
                current_project_text.append(stripped)

    # Add last project
    if current_project_name:
        extracted_projects.append({
            'name': current_project_name,
            'section_status': current_status_section,
            'text': "\n".join(current_project_text)
        })

# Now process extracted projects to find 'emergency' or 'FEMA' related ones
results = []

for proj in extracted_projects:
    p_name = proj['name']
    p_text = proj['text'].lower()
    p_section = proj['section_status']
    
    # Determine Status
    # Default to section
    status = p_section
    
    # Refine status based on text
    if 'completed' in p_text and 'construction was completed' in p_text:
        status = 'completed'
    elif 'under construction' in p_text:
        if status == 'construction':
            pass # Keep as construction or map to design?
    
    # Map 'construction' to 'design' if we must strictly follow the 3 statuses?
    # The hint says "Projects have three statuses: 'design', 'completed', 'not started'".
    # So "construction" is likely not a valid final answer if strict.
    # But usually 'construction' is > 'design'. 
    # Let's keep 'construction' if specific, or mapped to 'design' if required.
    # I'll leave it as 'construction' (or 'design' if inferred) for now.
    # Actually, if the text says "Project is currently under construction", the status is "construction".
    # If the question implies strict adherence to the 3 types, I'd say "design" (as in Active).
    # But "Construction" is distinct.
    # Let's try to map to the 3 hints if possible.
    # "design" (in planning/design phase)
    # "completed" (finished)
    # "not started" (identified but not begun)
    # Where does construction fit? It's "begun" but not "finished". So it's NOT "not started" and NOT "completed".
    # So it must be "design" (active) or the hint is incomplete.
    # I will output the extracted status (e.g. "Construction") but knowing the user might expect one of the 3.
    # Actually, let's just output "Construction" if extracted.
    
    # Check relevance
    is_related = False
    
    # Check Name
    if 'fema' in p_name.lower() or 'emergency' in p_name.lower():
        is_related = True
    
    # Check Text
    if 'fema' in p_text or 'emergency' in p_text:
        is_related = True
        
    # Check topics (if we can derive them)
    # Common topics: "fire", "storm", "drain", etc.
    # The user specifically asked for "emergency" or "FEMA".
    
    if is_related:
        # Get funding info
        f_info = funding_map.get(p_name, {})
        
        results.append({
            "Project_Name": p_name,
            "Funding_Source": f_info.get("Funding_Source"),
            "Amount": f_info.get("Amount"),
            "Status": status
        })

# Also, some projects might be in Funding DB with "FEMA" in name but NOT in extracted text (maybe distinct entry?)
# If they are in DB, they are valid projects.
# If they are not in text, we don't know status.
# But we should check if we missed any.
# Loop through funding_map keys containing "FEMA" or "Emergency"
for name, info in funding_map.items():
    if ('fema' in name.lower() or 'emergency' in name.lower()) and not any(r['Project_Name'] == name for r in results):
        # This project is related but wasn't found in text (or name didn't match exactly)
        # Maybe it was covered by a base name in text?
        # e.g. "Outdoor Warning Sirens (FEMA Project)" vs "Outdoor Warning Sirens"
        # If we already have "Outdoor Warning Sirens" in results, do we add this one?
        # The user wants project names.
        # If the text describes "Outdoor Warning Sirens" and mentions FEMA, we added it.
        # "Outdoor Warning Sirens (FEMA Project)" might just be the funding name for the same project.
        # The prompt says: "The Project_Name in the Funding SQLite table matches the project names that can be extracted from the civic documents".
        # If extracted name is "Outdoor Warning Sirens", and SQLite has "Outdoor Warning Sirens" AND "Outdoor Warning Sirens (FEMA Project)".
        # We extracted the first one.
        # If the text mentions FEMA, we included it.
        # Should we also include the specific FEMA project entry?
        # If the text didn't explicitly name "Outdoor Warning Sirens (FEMA Project)", we didn't extract it as a project block.
        # However, if it's in the Funding DB, it's a project.
        # I'll rely on the extracted list for "Status".
        # If I can't find status, I won't include it or mark status as "Unknown".
        pass

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-4694039731328856667': 'file_storage/function-call-4694039731328856667.json', 'var_function-call-11052254391267769107': 'file_storage/function-call-11052254391267769107.json'}

exec(code, env_args)

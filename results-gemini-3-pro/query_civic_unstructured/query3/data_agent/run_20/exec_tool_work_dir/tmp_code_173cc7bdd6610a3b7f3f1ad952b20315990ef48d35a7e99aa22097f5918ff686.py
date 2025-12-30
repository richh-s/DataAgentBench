code = """import json
import re

# Load data
with open(locals()['var_function-call-18417564437237588666'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-2011440110474584919'], 'r') as f:
    civic_docs = json.load(f)

funding_map = {item['Project_Name']: item for item in funding_data}
project_names = set(funding_map.keys())

def extract_date(text, prefix):
    # Regex for Prefix: Month Year or Prefix: Season Year
    # Avoid complex regex constructs that might confuse the parser if passed as string
    # Pattern: Prefix + optional colon + space + (Word + space + 4 digits)
    p = re.escape(prefix) + r":?\s+([a-zA-Z0-9]+\s+\d{4})"
    match = re.search(p, text, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

keywords = ["park", "road", "FEMA", "fire", "emergency", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail"]

def extract_topics(text):
    found = []
    text_lower = text.lower()
    for kw in keywords:
        if kw.lower() in text_lower:
            found.append(kw)
    return ", ".join(found)

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_status = None
    
    current_project_name = None
    current_project_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Determine section status
        if "Capital Improvement Projects (Design)" in line:
            current_status = "design"
        elif "Capital Improvement Projects (Construction)" in line:
            current_status = "construction_section"
        elif "Capital Improvement Projects (Not Started)" in line:
            current_status = "not started"
            
        # Check for project name
        is_new_project = False
        matched_name = None
        
        # Check exact match first
        if line in project_names:
            is_new_project = True
            matched_name = line
        
        if is_new_project:
            # Save previous
            if current_project_name:
                blob = "\n".join(current_project_lines)
                
                # Determine final status
                final_status = "unknown"
                # Use saved status from when the project started
                # Wait, status changes as we scroll through file. 
                # Ideally we track status per project based on the section it was found in.
                # But here current_status is global to the loop.
                # We should capture current_status when we start the project.
                # But current_status is updated before we check for name. Correct.
                
                # However, for the previous project, we need the status that was active when IT started?
                # No, the headers are above the projects.
                # So current_status applies to subsequent projects until next header.
                pass
            
            # We can't easily save the 'previous' project with the correct status if we only update status on header.
            # We should save the current project before updating variables for the new one.
            # But the header comes before the project name.
            # So:
            # Header -> updates current_status
            # Project Name -> starts new project, using current_status.
            
            if current_project_name:
                # Process previous project
                blob = "\n".join(current_project_lines)
                topics = extract_topics(blob)
                
                # Logic for status
                p_status = current_project_status
                if p_status == "construction_section":
                    if "completed" in blob.lower() and "construction was completed" in blob.lower():
                        p_status = "completed"
                    else:
                        p_status = "design" # Fallback for 'under construction' as active
                
                extracted_projects.append({
                    "Project_Name": current_project_name,
                    "text": blob,
                    "topics": topics,
                    "status": p_status
                })

            current_project_name = matched_name
            current_project_status = current_status
            current_project_lines = []
        else:
            if current_project_name:
                current_project_lines.append(line)

    # Save last
    if current_project_name:
        blob = "\n".join(current_project_lines)
        topics = extract_topics(blob)
        p_status = current_project_status
        if p_status == "construction_section":
            if "completed" in blob.lower() and "construction was completed" in blob.lower():
                p_status = "completed"
            else:
                p_status = "design"
        
        extracted_projects.append({
            "Project_Name": current_project_name,
            "text": blob,
            "topics": topics,
            "status": p_status
        })

# Filter and Format
results = []
for p in extracted_projects:
    name = p['Project_Name']
    topics = p['topics']
    
    # Check "emergency" or "FEMA"
    is_relevant = False
    if "emergency" in name.lower() or "fema" in name.lower():
        is_relevant = True
    elif "emergency" in topics.lower() or "fema" in topics.lower():
        is_relevant = True
    
    if is_relevant:
        fund = funding_map.get(name, {})
        results.append({
            "Project_Name": name,
            "Funding_Source": fund.get("Funding_Source"),
            "Amount": fund.get("Amount"),
            "Status": p['status']
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-718083360351244279': ['Funding'], 'var_function-call-18180175954049714507': ['civic_docs'], 'var_function-call-18417564437237588666': 'file_storage/function-call-18417564437237588666.json', 'var_function-call-15750785103731277678': 'file_storage/function-call-15750785103731277678.json', 'var_function-call-2011440110474584919': 'file_storage/function-call-2011440110474584919.json'}

exec(code, env_args)

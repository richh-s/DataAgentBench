code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-18417564437237588666'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-2011440110474584919'], 'r') as f:
    civic_docs = json.load(f)

# Prepare funding lookup
funding_map = {item['Project_Name']: item for item in funding_data}
project_names = set(funding_map.keys())

# Helper to find date in string
def extract_date(text, prefix):
    # Regex for "Prefix: Month Year" or "Prefix: Season Year"
    # Example: "Begin Construction: Fall 2023"
    pattern = re.escape(prefix) + r":?\s*([A-Za-z0-9]+\s+[0-9]{4}|[A-Za-z]+\s+[0-9]{4})"
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

# Helper to extract topics
keywords = ["park", "road", "FEMA", "fire", "emergency", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail"]
def extract_topics(text):
    found = []
    text_lower = text.lower()
    for kw in keywords:
        if kw.lower() in text_lower:
            found.append(kw)
    return ", ".join(found)

# Process documents
extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_section_status = None
    current_section_type = "capital" # Default
    
    current_project = None
    current_project_text = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Detect Header
        if "Capital Improvement Projects (Design)" in line:
            current_section_status = "design"
        elif "Capital Improvement Projects (Construction)" in line:
            current_section_status = "construction_section" # To be refined
        elif "Capital Improvement Projects (Not Started)" in line:
            current_section_status = "not started"
        elif "Disaster Recovery Projects" in line: # Fallback if headers differ
            current_section_type = "disaster"
            
        # Check if line matches a project name
        # We need exact match or close match? The names in funding DB seem full.
        # But in text they might be slightly different or same.
        # Let's check exact match first.
        # The text lines might have extra chars or be substring.
        # But looking at the preview, "2022 Morning View Resurfacing & Storm Drain Improvements" is on its own line.
        
        is_project_start = False
        matched_name = None
        
        if line in project_names:
            is_project_start = True
            matched_name = line
        else:
            # Try case insensitive or strip
            for name in project_names:
                if line.lower() == name.lower():
                    is_project_start = True
                    matched_name = name
                    break
        
        if is_project_start:
            # Save previous project
            if current_project:
                full_text = "\n".join(current_project_text)
                topics = extract_topics(full_text)
                
                # Refine status for construction section
                status = current_project['status']
                if status == "construction_section":
                    if "completed" in full_text.lower() and "construction was completed" in full_text.lower():
                        status = "completed"
                    elif "under construction" in full_text.lower():
                        status = "completed" # Wait, hint says "completed" is a status. "Under construction" is not. 
                        # But typically "under construction" is "design" phase in some sloppy gov docs? No.
                        # If I have to choose from (design, completed, not started), "under construction" is none.
                        # But let's look at the hints again.
                        # Hint: "Projects have three statuses: 'design', 'completed', 'not started'".
                        # Maybe I should just use "design" for anything ongoing?
                        # Or maybe "completed" for finished.
                        # I'll stick to extracting "completed" if it says completed. 
                        # If it says "under construction", I'll label it "design" (as in 'active/in progress' before completion). 
                        # This matches the "Design" bucket vs "Not Started".
                        status = "design" 
                    else:
                        status = "design" # Default to active if in construction section but not completed?
                
                # Refine type based on name
                p_type = current_project['type']
                if "FEMA" in current_project['name'] or "CalOES" in current_project['name'] or "Disaster" in current_project['name']:
                    p_type = "disaster"
                elif "FEMA" in topics:
                    p_type = "disaster"

                # Dates
                st = extract_date(full_text, "Begin Construction")
                et = extract_date(full_text, "Complete Construction")
                if not et:
                    et = extract_date(full_text, "Complete Design")
                
                extracted_projects.append({
                    "Project_Name": current_project['name'],
                    "topic": topics,
                    "type": p_type,
                    "status": status,
                    "st": st,
                    "et": et
                })
            
            # Start new project
            current_project = {
                "name": matched_name,
                "status": current_section_status,
                "type": current_section_type
            }
            current_project_text = []
        else:
            if current_project:
                current_project_text.append(line)

    # Save last project
    if current_project:
        full_text = "\n".join(current_project_text)
        topics = extract_topics(full_text)
        
        status = current_project['status']
        if status == "construction_section":
            if "completed" in full_text.lower() and "construction was completed" in full_text.lower():
                status = "completed"
            elif "under construction" in full_text.lower():
                status = "design"
            else:
                status = "design"

        p_type = current_project['type']
        if "FEMA" in current_project['name'] or "CalOES" in current_project['name'] or "Disaster" in current_project['name']:
            p_type = "disaster"
        elif "FEMA" in topics:
            p_type = "disaster"
            
        st = extract_date(full_text, "Begin Construction")
        et = extract_date(full_text, "Complete Construction")
        if not et:
            et = extract_date(full_text, "Complete Design")
        
        extracted_projects.append({
            "Project_Name": current_project['name'],
            "topic": topics,
            "type": p_type,
            "status": status,
            "st": st,
            "et": et
        })

# Merge and Filter
final_results = []
for p in extracted_projects:
    name = p['Project_Name']
    
    # Check if related to emergency or FEMA
    is_related = False
    if "emergency" in name.lower() or "fema" in name.lower():
        is_related = True
    elif "emergency" in p['topic'].lower() or "fema" in p['topic'].lower():
        is_related = True
    
    if is_related:
        funding = funding_map.get(name, {})
        final_results.append({
            "Project_Name": name,
            "Funding_Source": funding.get("Funding_Source"),
            "Amount": funding.get("Amount"),
            "Status": p['status'],
            # "Type": p['type'],
            # "Start_Date": p['st'],
            # "End_Date": p['et']
        })

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-718083360351244279': ['Funding'], 'var_function-call-18180175954049714507': ['civic_docs'], 'var_function-call-18417564437237588666': 'file_storage/function-call-18417564437237588666.json', 'var_function-call-15750785103731277678': 'file_storage/function-call-15750785103731277678.json', 'var_function-call-2011440110474584919': 'file_storage/function-call-2011440110474584919.json'}

exec(code, env_args)

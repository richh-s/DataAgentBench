code = """import json
import re

# Load data
funding_path = locals()['var_function-call-3669555105511177724']
civic_path = locals()['var_function-call-3669555105511175475']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Build funding map
funding_map = {}
for item in funding_data:
    if item.get('Project_Name'):
        funding_map[item['Project_Name'].strip()] = item

results = []

# Keywords
relevant_keywords = {'emergency', 'fema'}
topic_keywords = ["park", "road", "fema", "fire", "emergency", "warning", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail"]

for doc in civic_data:
    text = doc.get('text', '')
    # Normalize
    text = text.replace('\u00be', 'BULLET1').replace('\u0083', 'BULLET2') # mapped from cid:190 and cid:131 if possible, but raw string might differ.
    # The preview showed (cid:190). Let's handle the string literal "(cid:190)" and "(cid:131)"
    text = text.replace('(cid:190)', 'BULLET1').replace('(cid:131)', 'BULLET2')
    
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    current_type = None
    current_status_hint = None
    
    # Store found projects to process
    # Structure: (name, type, status_hint, raw_text_lines)
    found_projects = []
    
    current_proj_name = None
    current_proj_lines = []
    
    active_section = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for Headers
        if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
            # Save previous project if any
            if current_proj_name:
                found_projects.append((current_proj_name, current_type, current_status_hint, current_proj_lines))
                current_proj_name = None
                current_proj_lines = []
            
            active_section = True
            # Parse Type
            if "Capital Improvement Projects" in line:
                current_type = "capital"
            elif "Disaster Recovery Projects" in line:
                current_type = "disaster"
                
            # Parse Status Hint
            if "(Design)" in line:
                current_status_hint = "design"
            elif "(Construction)" in line:
                current_status_hint = "construction"
            elif "(Not Started)" in line:
                current_status_hint = "not started"
            else:
                current_status_hint = "design" # Default or unknown
            
            i += 1
            continue
            
        if not active_section:
            i += 1
            continue
            
        # Detect Project Name
        # Assumption: Project Name line does not start with BULLET, is not a page number, is not a known header.
        # And usually followed by a BULLET line (Updates or Schedule).
        
        is_bullet = line.startswith('BULLET')
        is_page_num = line.startswith('Page ') or line.startswith('Agenda Item')
        
        if not is_bullet and not is_page_num:
            # Possible project name.
            # Check if next line is BULLET or if it looks like a name
            # For now, assume it's a new project if we are in a section.
            
            # Save previous
            if current_proj_name:
                found_projects.append((current_proj_name, current_type, current_status_hint, current_proj_lines))
            
            current_proj_name = line
            current_proj_lines = []
        else:
            if current_proj_name:
                current_proj_lines.append(line)
        
        i += 1
        
    # Save last project
    if current_proj_name:
        found_projects.append((current_proj_name, current_type, current_status_hint, current_proj_lines))

    # Process extracted projects
    for pname, ptype, pstat_hint, plines in found_projects:
        full_text = " ".join(plines)
        
        # Refine Status
        status = pstat_hint
        if status == "construction":
            if "Construction was completed" in full_text:
                status = "completed"
            elif "Project is currently under construction" in full_text:
                status = "design" # Based on hint "design" (in planning/design phase)? Or should I use "not started"?
                # Actually, "in planning/design phase" doesn't fit "under construction".
                # But "completed" is false. "not started" is false.
                # If I strictly follow the hint: "Projects have three statuses: 'design', 'completed', 'not started'".
                # I will map "under construction" to "design" as it is the active phase? 
                # Or maybe I should output "under construction" if the user accepts it.
                # Given strict hint, I'll default to 'design' for active construction if not completed.
                # Wait, "completed" (finished). "not started" (identified but not begun).
                # "design" (in planning/design phase). 
                # Is there a "construction" status?
                # Maybe I should check if I missed a hint.
                # "Projects have two types... Projects have three statuses..."
                # I'll output "design" for construction phase to correspond to "active/ongoing".
                status = "design"
            else:
                status = "design"

        # Extract Topics
        topics = []
        combined_text = (pname + " " + full_text).lower()
        for k in topic_keywords:
            if k in combined_text:
                topics.append(k)
        
        # Check relevance
        is_relevant = False
        if "emergency" in combined_text or "fema" in combined_text:
            is_relevant = True
        
        if not is_relevant:
            continue
            
        # Extract Dates
        # st: Start Date. et: End Date.
        # "Begin Construction: ..."
        # "Complete Design: ..."
        # "Complete Construction: ..."
        st = None
        et = None
        
        # Regex for dates
        # Look for "Begin Construction: <value>"
        m_begin = re.search(r'Begin Construction[:\s]+(.*?)(?=BULLET|\Z)', full_text, re.IGNORECASE)
        if m_begin:
            st = m_begin.group(1).strip()
        
        m_complete = re.search(r'Complete Construction[:\s]+(.*?)(?=BULLET|\Z)', full_text, re.IGNORECASE)
        if m_complete:
            et = m_complete.group(1).strip()
        
        # Fallbacks
        if not et:
            m_comp_des = re.search(r'Complete Design[:\s]+(.*?)(?=BULLET|\Z)', full_text, re.IGNORECASE)
            if m_comp_des:
                # If completed design is the only date, maybe use it?
                # But 'et' usually implies project end.
                pass
        
        # Funding join
        f_info = funding_map.get(pname)
        # Try simple normalization if not found
        if not f_info:
            # Try removing special chars or suffixes
            # e.g. " (FEMA Project)"
            pname_clean = re.sub(r'\s*\(.*?\)', '', pname)
            f_info = funding_map.get(pname_clean)
            
            if not f_info:
                # Try matching textual name in funding keys
                # This is O(N*M), but funding is small?
                # Funding preview showed ~70 items.
                pass
        
        project_record = {
            "Project_Name": pname,
            "Funding_Source": f_info['Funding_Source'] if f_info else None,
            "Amount": f_info['Amount'] if f_info else None,
            "Status": status,
            # "Topics": topics,
            # "Type": ptype,
            # "Start_Date": st,
            # "End_Date": et
        }
        
        # Add to results if not duplicate (by name)
        if not any(r['Project_Name'] == pname for r in results):
            results.append(project_record)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3669555105511177724': 'file_storage/function-call-3669555105511177724.json', 'var_function-call-3669555105511175475': 'file_storage/function-call-3669555105511175475.json'}

exec(code, env_args)

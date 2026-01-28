code = """import json
import re
import pandas as pd

# Load data
funding_path = locals()['var_function-call-15640139870961926103']
civic_path = locals()['var_function-call-15640139870961922644']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Create funding lookup
# Normalize project names: strip, maybe lower case for matching? 
# The hint says "Project_Name in the Funding SQLite table matches the project names that can be extracted".
# So exact match or simple strip should work.
funding_map = {item['Project_Name'].strip(): float(item['Amount']) for item in funding_data}

extracted_projects = []

def parse_document(text, filename):
    lines = text.split('\n')
    current_category = "Unknown" # capital or disaster
    current_status = "Unknown" # design, construction, not started
    
    current_project_name = None
    current_project_text = []
    
    projects = []
    
    def save_project(name, text_lines, category, status):
        if not name: return
        full_text = "\n".join(text_lines)
        
        # Extract Start Date
        # Look for "Begin Construction: <value>"
        st = None
        st_match = re.search(r'Begin Construction:\s*(.*)', full_text, re.IGNORECASE)
        if st_match:
            st = st_match.group(1).strip()
        else:
            # Maybe "Start Date" or just "Schedule:" lines
            pass
            
        # Determine Type
        p_type = category.lower()
        if "fema" in name.lower() or "caloes" in name.lower() or "caljpia" in name.lower() or "woolsey" in name.lower():
            p_type = "disaster"
        if "disaster" in category.lower():
            p_type = "disaster"
        elif "capital" in category.lower() and p_type != "disaster":
            p_type = "capital"
            
        projects.append({
            'Project_Name': name,
            'type': p_type,
            'st': st,
            'filename': filename,
            'raw_text': full_text[:200]
        })

    # Regex for section headers
    # "Capital Improvement Projects (Design)"
    # "Disaster Recovery Projects (Construction)"
    header_re = re.compile(r'^(Capital Improvement Projects|Disaster Recovery Projects)\s*(?:\((.*)\))?', re.IGNORECASE)
    
    # Regex to identify a new project name. 
    # Heuristic: A line that is not empty, not a known header, and followed by "Updates:" or "Project Description:" etc.
    # But checking "followed by" requires lookahead.
    # Simpler: If we see "Updates:" or "Project Description:", the PREVIOUS non-empty line was likely the project name.
    
    # Let's iterate and buffer lines.
    
    iterator = iter(range(len(lines)))
    for i in iterator:
        line = lines[i].strip()
        if not line: continue
        
        # Check for Section Header
        match = header_re.match(line)
        if match:
            # Save previous project
            save_project(current_project_name, current_project_text, current_category, current_status)
            current_project_name = None
            current_project_text = []
            
            current_category = match.group(1) # Capital... or Disaster...
            if match.group(2):
                current_status = match.group(2)
            continue
            
        # Check if this line is a start of a project block
        # Look ahead for "Updates:" or "Project Description:" or "Project Schedule:" or "(cid:190) Updates:"
        # In the preview, "Updates:" is often preceded by "(cid:190)" which is a bullet.
        # "PCH Median Improvements Project" -> next line "(cid:190) Updates:"
        
        is_project_start = False
        # Check next few lines for keywords
        for offset in range(1, 5):
            if i + offset >= len(lines): break
            next_l = lines[i+offset].strip()
            if "Updates:" in next_l or "Project Description:" in next_l or "Project Schedule:" in next_l or "Update:" in next_l:
                # Also ensure the current line isn't just "Updates:" itself
                if "Updates:" not in line and "Project Description:" not in line:
                    is_project_start = True
                    break
        
        if is_project_start:
            # Save previous
            save_project(current_project_name, current_project_text, current_category, current_status)
            current_project_name = line # This line is the name
            current_project_text = []
        else:
            if current_project_name:
                current_project_text.append(line)
    
    # Save last
    save_project(current_project_name, current_project_text, current_category, current_status)
    return projects

all_extracted = []
for doc in civic_data:
    all_extracted.extend(parse_document(doc['text'], doc['filename']))

# Filter for Disaster projects starting in 2022
target_projects = []
for p in all_extracted:
    if p['type'] == 'disaster' and p['st'] and '2022' in p['st']:
        target_projects.append(p)

# Join with funding
total_funding = 0
matched_projects = []
missing_projects = []

for p in target_projects:
    name = p['Project_Name'].strip()
    # Try exact match
    if name in funding_map:
        amount = funding_map[name]
        total_funding += amount
        matched_projects.append({'name': name, 'amount': amount})
    else:
        # Try finding a close match or substring? 
        # The prompt says names match. But maybe I extracted extra chars?
        # Let's check common issues.
        missing_projects.append(name)

print("__RESULT__:")
print(json.dumps({
    "total_funding": total_funding,
    "matched_projects": matched_projects,
    "missing_projects": missing_projects,
    "debug_extracted_count": len(all_extracted),
    "debug_target_count": len(target_projects)
}))"""

env_args = {'var_function-call-15640139870961926103': 'file_storage/function-call-15640139870961926103.json', 'var_function-call-15640139870961922644': 'file_storage/function-call-15640139870961922644.json'}

exec(code, env_args)

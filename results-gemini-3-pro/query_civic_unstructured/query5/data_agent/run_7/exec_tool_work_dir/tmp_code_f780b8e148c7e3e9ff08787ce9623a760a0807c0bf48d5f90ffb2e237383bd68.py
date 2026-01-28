code = """import json
import re

# Load data
funding_path = locals()['var_function-call-12062815889619764856']
civic_docs_path = locals()['var_function-call-9916471758806846480']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

projects = {} # name -> {is_disaster: bool, start_date_2022: bool, raw_date: str}

def is_disaster_text(text):
    keywords = ["FEMA", "CalOES", "CalJPIA", "Disaster", "Recovery", "Woolsey Fire"]
    return any(k.upper() in text.upper() for k in keywords)

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_section_disaster = False
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Detect section
        if "Disaster Recovery Projects" in line:
            current_section_disaster = True
        elif "Capital Improvement Projects" in line:
            current_section_disaster = False
            
        # Detect project name
        # Heuristic: line followed by "(cid:190) Updates:" or similar
        # Or line followed by "Project Description:"
        is_project = False
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if next_line.startswith("(cid:190)") or next_line.startswith("Updates:") or next_line.startswith("Project Description:"):
                is_project = True
            # Also check for Updates indented
            if "Updates:" in next_line and len(next_line) < 20:
                is_project = True
        
        if is_project and line and not line.startswith("(") and len(line) > 3:
            p_name = line
            # Clean name
            p_name = p_name.replace("(cid:190)", "").strip()
            
            # Extract block
            j = i + 1
            block_lines = []
            while j < len(lines):
                next_l = lines[j].strip()
                # Stop if next line looks like a project header (followed by marker)
                # But need to be careful not to stop on internal headers
                # We'll assume project headers are usually short and distinct
                if j + 1 < len(lines):
                    nn_l = lines[j+1].strip()
                    if (nn_l.startswith("(cid:190)") or nn_l.startswith("Updates:")) and next_l and not next_l.startswith("("):
                        # likely new project
                        break
                
                # Check for section headers
                if "Capital Improvement Projects" in next_l or "Disaster Recovery Projects" in next_l:
                    break
                
                block_lines.append(next_l)
                j += 1
            
            block_text = "\n".join(block_lines)
            
            # Analyze
            is_disaster = current_section_disaster or is_disaster_text(p_name) or is_disaster_text(block_text)
            
            # Start Date
            # Look for "Begin Construction: <date>"
            # Regex for date: flexible
            # We want to check if 2022 is in the start date
            start_date_2022 = False
            raw_date = ""
            
            # Regex patterns
            # 1. Begin Construction: ...
            match = re.search(r"Begin [Cc]onstruction:?\s*([A-Za-z0-9\s,]+)", block_text)
            if match:
                date_str = match.group(1)
                if "2022" in date_str:
                    start_date_2022 = True
                raw_date = date_str
            else:
                # 2. Start Date: ...
                match = re.search(r"Start [Dd]ate:?\s*([A-Za-z0-9\s,]+)", block_text)
                if match:
                    date_str = match.group(1)
                    if "2022" in date_str:
                        start_date_2022 = True
                    raw_date = date_str
                else:
                    # 3. Construction started ...
                    match = re.search(r"[Cc]onstruction started\s*([A-Za-z0-9\s,]+)", block_text)
                    if match:
                        date_str = match.group(1)
                        if "2022" in date_str:
                            start_date_2022 = True
                        raw_date = date_str
            
            # Store
            if p_name not in projects:
                projects[p_name] = {'is_disaster': False, 'start_2022': False, 'raw_date': ''}
            
            if is_disaster:
                projects[p_name]['is_disaster'] = True
            if start_date_2022:
                projects[p_name]['start_2022'] = True
            if raw_date:
                projects[p_name]['raw_date'] = raw_date
            
            i = j - 1 # skip processed lines
        i += 1

# Match with funding
total_amount = 0
matched_projects = []

for f in funding_data:
    fname = f['Project_Name']
    amount = float(f['Amount']) if f['Amount'] else 0
    
    # Check if this project is in our extracted list
    # Attempt exact match
    if fname in projects:
        p = projects[fname]
        if p['is_disaster'] and p['start_2022']:
            total_amount += amount
            matched_projects.append({'name': fname, 'amount': amount, 'extracted': p})
    else:
        # Maybe fuzzy match? 
        # But hint says "Project_Name ... matches ... extracted".
        # Let's check keys that contain fname or vice versa
        pass

print("__RESULT__:")
print(json.dumps({'total_amount': total_amount, 'matched_projects': matched_projects, 'extracted_count': len(projects)}))"""

env_args = {'var_function-call-1624468200300741529': ['Funding'], 'var_function-call-1624468200300743390': ['civic_docs'], 'var_function-call-12062815889619764856': 'file_storage/function-call-12062815889619764856.json', 'var_function-call-12062815889619765571': 'file_storage/function-call-12062815889619765571.json', 'var_function-call-9916471758806846480': 'file_storage/function-call-9916471758806846480.json'}

exec(code, env_args)

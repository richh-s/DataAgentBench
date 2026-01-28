code = """import re
import json

docs_filepath = locals()['var_function-call-10727724106832810456']
with open(docs_filepath, 'r') as f:
    docs_content = json.load(f)

extracted_projects = []

for doc in docs_content:
    text = doc['text']
    lines = text.splitlines()
    
    current_project_name = None
    
    for i, line in enumerate(lines):
        cleaned_line = line.strip().replace('(cid:190)', '').strip()

        # Attempt to identify project names. They are usually prominent and followed by details.
        # Look for lines that start with an uppercase letter and contain keywords like 'Project', 'Repairs', etc.
        # Also, filter out lines that are clearly not project names (e.g., agenda items, dates).
        if re.match(r'^[A-Z][A-Za-z0-9\s&\-,']*(?:Project|Improvements|Repair|Plan|Study|Facility|System|Screens|Shade Structure|Green Streets|Quality|Playground|Walkway|Bluffs)[A-Za-z0-9\s&\-,']*(?:\sProject)?$', cleaned_line) and \
           not any(keyword in cleaned_line for keyword in [
               "AGENDA", "RECOMMENDED ACTION", "Subject:", "To:", "Prepared by:", 
               "Approved by:", "Date prepared:", "Meeting date:", "DISCUSSION", 
               "Capital Improvement Projects", "Disaster Recovery Projects", 
               "Public Works Commission", "Fiscal Year", "Page ", "Item "]):
            
            current_project_name = cleaned_line
            # Now, look ahead in the next few lines for status and end date
            project_status = 'unknown'
            project_et = 'unknown'

            for j in range(i + 1, min(i + 10, len(lines))): # Look up to 10 lines ahead
                detail_line = lines[j].strip().lower()
                
                if re.search(r'updates:.*(?:construction was completed|completed|notice of completion filed)', detail_line):
                    project_status = 'completed'
                
                if project_status == 'completed' and '2022' in detail_line:
                    et_match = re.search(r'(january|february|march|april|may|june|july|august|september|october|november|december)?\s*2022', detail_line)
                    project_et = et_match.group(0).strip() if et_match else '2022'
                    break # Found the end date, stop looking in detail lines
            
            if project_status == 'completed' and '2022' in project_et:
                topic = "unknown"
                if "Park" in current_project_name or "Bluffs" in current_project_name or "Playground" in current_project_name:
                    topic = "park"
                
                if topic == "park":
                    extracted_projects.append({
                        'Project_Name': current_project_name,
                        'topic': topic,
                        'status': project_status,
                        'et': project_et
                    })
            current_project_name = None # Reset after processing a project block

# Filter for unique projects (to avoid duplicates if found in multiple lines)
unique_projects = []
seen_project_names = set()
for p in extracted_projects:
    if p['Project_Name'] not in seen_project_names:
        unique_projects.append(p)
        seen_project_names.add(p['Project_Name'])

print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-10727724106832810456': 'file_storage/function-call-10727724106832810456.json'}

exec(code, env_args)

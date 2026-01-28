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
    current_project_status = 'unknown'
    current_project_et = 'unknown'

    for line in lines:
        line = line.strip()

        # Reset project info if a new potential project title is encountered
        # Project titles are typically capitalized and followed by detail lines (e.g., (cid:190) Updates:)
        # Filtering out common headers/footers/non-project lines
        if re.match(r'^[A-Z][a-zA-Z0-9\s&\-]+(?:Project|Improvements|Repair|Plan|Study|Facility|System|Screens|Shade Structure|Green Streets|Quality)?[^\n]*?$', line) and \
           not any(keyword in line for keyword in ["COMMISSION", "AGENDA", "RECOMMENDED ACTION", "Subject:", "To:", "Prepared by:", "Approved by:", "Date prepared:", "Meeting date:", "DISCUSSION", "Capital Improvement Projects", "Fiscal Year"]):
            current_project_name = line.strip()
            current_project_status = 'unknown'
            current_project_et = 'unknown'
        
        # If we have a project name, try to extract status and end date
        if current_project_name:
            if re.search(r'(construction was completed|completed|notice of completion filed).*(2022)', line, re.IGNORECASE):
                current_project_status = 'completed'
                et_match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)?\s*2022', line, re.IGNORECASE)
                current_project_et = et_match.group(0).strip() if et_match else '2022'

            # If a project is identified as completed in 2022 and related to parks, add it.
            if current_project_status == 'completed' and '2022' in current_project_et:
                if "Park" in current_project_name or "Bluffs" in current_project_name or "Playground" in current_project_name:
                    extracted_projects.append({
                        'Project_Name': current_project_name,
                        'topic': 'park',
                        'status': current_project_status,
                        'et': current_project_et
                    })
                    current_project_name = None # Reset to avoid processing same project with subsequent lines
                    current_project_status = 'unknown'
                    current_project_et = 'unknown'

# Remove duplicates and refine project names
unique_projects = []
seen_project_names = set()
for p in extracted_projects:
    clean_name = p["Project_Name"].replace("(cid:190)", "").strip()
    if clean_name not in seen_project_names:
        p["Project_Name"] = clean_name
        unique_projects.append(p)
        seen_project_names.add(clean_name)

print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-10727724106832810456': 'file_storage/function-call-10727724106832810456.json'}

exec(code, env_args)

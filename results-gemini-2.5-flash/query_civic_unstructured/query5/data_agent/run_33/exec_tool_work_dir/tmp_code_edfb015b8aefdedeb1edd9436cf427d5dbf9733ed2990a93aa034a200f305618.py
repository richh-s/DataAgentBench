code = """import json
import re

with open(locals()['var_function-call-14330681698543489492'], 'r') as f:
    civic_docs = json.load(f)

disaster_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    current_type = None
    lines = text.split('\n')

    for i, line in enumerate(lines):
        if "Capital Improvement Projects" in line:
            current_type = "capital"
        elif "Disaster Recovery Projects" in line:
            current_type = "disaster"

        if current_type == "disaster":
            # Look for project names. Project names are usually capitalized and appear on their own line or before a schedule.
            # They often end with specific keywords like Project, Improvements, etc.
            project_name_match = re.search(r'^([A-Z][A-Za-z0-9&, -]+(?:Project|Improvements|Study|Plan|Repairs|System|Center|Park|Road|Walkway|Bridge|Drive|Lane|Way|Bluffs|Canyon|Heights|Trancas|Civic|PCH|Point Dume|Malibu|Encinal|Kanan Dume|Latigo|Morning View|Westward Beach|Clover Heights|Storm Drain|Traffic Signals|Outdoor Warning Signs|Crosswalk|Median|Shade Structure|Green Streets|Water Quality|Slope Repairs)(?: \(FEMA Project\)| \(CalJPIA Project\)| \(CalOES Project\))?)$|^([A-Z][A-Za-z0-9&, -]+)(?=\n\s*\(cid:190) Updates:)', line.strip())
            
            if project_name_match:
                project_name = project_name_match.group(1) if project_name_match.group(1) else project_name_match.group(2)
                project_name = project_name.strip()
                
                # Now check for '2022' in the schedule lines following this project name
                for j in range(i + 1, min(i + 10, len(lines))): # Check next 10 lines for schedule info
                    if "Project Schedule:" in lines[j] or "Estimated Schedule:" in lines[j] or "Complete Design:" in lines[j] or "Begin Construction:" in lines[j] or "Advertise:" in lines[j] or "Begin work:" in lines[j] or "Updates:" in lines[j]:
                        if "2022" in lines[j]:
                            disaster_projects_2022.append(project_name)
                            break # Found a 2022 date for this project, move to next project
                    # Stop if we hit another project name or a major section header
                    if re.match(r'^([A-Z][A-Za-z0-9&, -]+(?:Project|Improvements|Study|Plan))\s*$', lines[j].strip()) and not re.match(r'^([A-Z][A-Za-z0-9&, -]+(?:Project|Improvements|Study|Plan)(?: \(FEMA Project\)| \(CalJPIA Project\)| \(CalOES Project\))?)$|^([A-Z][A-Za-z0-9&, -]+)(?=\n\s*\(cid:190) Updates:)', lines[j].strip()):
                         break

# Remove duplicates
disaster_projects_2022 = list(set(disaster_projects_2022))

print("__RESULT__:")
print(json.dumps(disaster_projects_2022))"""

env_args = {'var_function-call-14330681698543489492': 'file_storage/function-call-14330681698543489492.json'}

exec(code, env_args)

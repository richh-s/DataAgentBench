code = """import json
import re

with open(locals()['var_function-call-14330681698543489492'], 'r') as f:
    civic_docs = json.load(f)

disaster_projects_2022 = []

for doc in civic_docs:
    text = doc['text']

    # Iterate through each line to find project schedules with '2022'
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if "Project Schedule:" in line or "Estimated Schedule:" in line:
            # Look for '2022' in the current or subsequent lines for schedule
            schedule_found = False
            schedule_info = ""
            for j in range(i + 1, min(i + 5, len(lines))): # Check next few lines for schedule
                if "(cid:131)" in lines[j] and "2022" in lines[j]:
                    schedule_info += lines[j]
                    schedule_found = True
                # Stop if we hit another project schedule or a major heading
                if "Project Schedule:" in lines[j] or "Capital Improvement Projects" in lines[j] or "Disaster Recovery Projects" in lines[j]:
                    break
            
            if schedule_found:
                # If schedule with '2022' is found, try to backtrack and find the project name
                project_name = None
                for k in range(i - 1, max(i - 10, -1), -1): # Look back up to 10 lines for a project name
                    # A project name is usually a capitalized phrase that doesn't start with (cid:190) or (cid:131)
                    if re.match(r'^[A-Z][A-Za-z0-9&, -]+\s*(?:Project|Improvements|Study|Plan|Repairs|System|Center|Park|Road|Walkway|Bridge|Drive|Lane|Way|Bluffs|Canyon|Heights|Trancas|Civic|PCH|Point Dume|Malibu|Encinal|Kanan Dume|Latigo|Morning View|Westward Beach|Clover Heights|Storm Drain|Traffic Signals|Outdoor Warning Signs|Crosswalk|Median|Shade Structure|Green Streets|Water Quality|Slope Repairs)(?: \(FEMA Project\)| \(CalJPIA Project\)| \(CalOES Project\))?$', lines[k].strip()):
                        project_name = lines[k].strip()
                        break
                    elif "Capital Improvement Projects" in lines[k] or "Disaster Recovery Projects" in lines[k]:
                        # If we hit a section header, the project name should be below it, or it's the section itself
                        break

                if project_name:
                    # Now, verify if this project is a "Disaster Recovery Project"
                    # Check if "Disaster Recovery Projects" appears before this project's schedule block
                    # This is a heuristic: check if "Disaster Recovery Projects" occurs more recently than "Capital Improvement Projects"
                    
                    # Find the last occurrence of these keywords before the current project schedule line
                    last_disaster_idx = -1
                    last_capital_idx = -1
                    for l in range(0, i):
                        if "Disaster Recovery Projects" in lines[l]:
                            last_disaster_idx = l
                        if "Capital Improvement Projects" in lines[l]:
                            last_capital_idx = l

                    if last_disaster_idx > last_capital_idx:
                        disaster_projects_2022.append(project_name)

# Remove duplicates
disaster_projects_2022 = list(set(disaster_projects_2022))

print("__RESULT__:")
print(json.dumps(disaster_projects_2022))"""

env_args = {'var_function-call-14330681698543489492': 'file_storage/function-call-14330681698543489492.json'}

exec(code, env_args)

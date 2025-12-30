code = """import re
import json

def extract_project_info(text):
    projects = []
    lines = text.split('\n')
    current_project_type = None
    
    project_pattern = re.compile(r'^([A-Za-z0-9][A-Za-z0-9\s&,-]+?)(?:\\s\\((?:FEMA|CalJPIA|CalOES) Project\\))?$')
    schedule_start_pattern = re.compile(r'^\\(cid:190\\)\\s*(?:Project|Estimated) Schedule:$')
    begin_construction_pattern = re.compile(r'^\\(cid:131\\)\\s*Begin Construction:\\s*(.*)$' )
    complete_construction_pattern = re.compile(r'^\\(cid:131\\)\\s*Complete Construction:\\s*(.*)$' )
    construction_completed_update_pattern = re.compile(r'^\\(cid:190\\)\\s*Updates:\\s*Construction was completed,\\s*(.*)$' )
    under_construction_update_pattern = re.compile(r'^\\(cid:190\\)\\s*Updates:\\s*Project is currently under construction$' )
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if "Disaster Recovery Projects" in line:
            current_project_type = "disaster"
        elif "Capital Improvement Projects" in line:
            current_project_type = "capital" # Reset if we enter a capital section
        
        if current_project_type == "disaster":
            project_match = project_pattern.match(line)
            if project_match:
                project_name = project_match.group(1).strip()
                start_date = ""
                
                # Look for schedule or update in subsequent lines
                j = i + 1
                while j < len(lines):
                    sub_line = lines[j].strip()
                    if not sub_line.startswith("(cid:190)") and not sub_line.startswith("(cid:131)"):
                        break # End of current project details
                    
                    if schedule_start_pattern.match(sub_line):
                        k = j + 1
                        while k < len(lines) and lines[k].strip().startswith("(cid:131)"):
                            schedule_detail_line = lines[k].strip()
                            begin_match = begin_construction_pattern.match(schedule_detail_line)
                            if begin_match:
                                start_date = begin_match.group(1).strip()
                                break
                            complete_match = complete_construction_pattern.match(schedule_detail_line)
                            if complete_match and not start_date:
                                start_date = complete_match.group(1).strip() # Use complete if begin not found
                            k += 1
                        if start_date: break # Found a date, move to next project

                    update_completed_match = construction_completed_update_pattern.match(sub_line)
                    if update_completed_match:
                        start_date = update_completed_match.group(1).strip()
                        break
                    
                    under_construction_match = under_construction_update_pattern.match(sub_line)
                    if under_construction_match:
                        start_date = "under construction"
                        break
                    
                    j += 1
                
                if project_name and start_date:
                    projects.append({"Project_Name": project_name, "st": start_date, "type": "disaster"})
                i = j # Move index past current project's details
            else:
                i += 1
        else:
            i += 1
    return projects

file_path = locals()['var_function-call-9117459986810486534']
with open(file_path, 'r') as f:
    documents_data = json.load(f)

all_projects = []
for doc_entry in documents_data['query_db_response']['results']:
    all_projects.extend(extract_project_info(doc_entry['text']))


disaster_projects_2022_names = set()
for project in all_projects:
    if project['type'] == 'disaster' and project['st'] and '2022' in project['st']:
        disaster_projects_2022_names.add(project['Project_Name'])

print("__RESULT__:")
print(json.dumps(list(disaster_projects_2022_names)))"""

env_args = {'var_function-call-9117459986810486534': 'file_storage/function-call-9117459986810486534.json'}

exec(code, env_args)

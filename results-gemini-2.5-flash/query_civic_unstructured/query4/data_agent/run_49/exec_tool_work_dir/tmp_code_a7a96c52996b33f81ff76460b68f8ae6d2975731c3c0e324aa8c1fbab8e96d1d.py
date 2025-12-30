code = """import json
import re

file_path = locals()['var_function-call-12362344962025889815']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

projects_data = []

for doc in civic_docs:
    text = doc['text']
    
    # Find all schedule sections
    schedule_matches = list(re.finditer(r'(?:Project Schedule:|Estimated Schedule:|Schedule:)\s*\n', text))
    
    for match in schedule_matches:
        schedule_start_index = match.start()
        
        # Look backwards for project name
        text_before_schedule = text[:schedule_start_index]
        
        # Split into lines and reverse to find the last meaningful line
        lines_before = [line.strip() for line in text_before_schedule.split('\n') if line.strip()]
        
        project_name = None
        for i in reversed(range(len(lines_before))):
            current_line = lines_before[i]
            if not current_line.startswith('(cid:') and not any(keyword in current_line.lower() for keyword in [
                "updates:", "discussion:", "subject:", "recommended action:", "prepared by:", "approved by:", "date prepared:", "meeting date:", "to:", "public works commission", "capital improvement projects", "disaster recovery projects", "agenda item", "page"
            ]):
                project_name = current_line
                break
        
        if not project_name:
            continue
            
        # Look forwards from schedule_start_index for "Begin Construction:" or "Complete Design:"
        # and extract the date
        text_after_schedule = text[schedule_start_index:]
        
        # Search for date in the next few lines
        date_match = re.search(r'(?:Begin Construction:|Complete Design:)\s*(.*?)(?=\n|\Z)', text_after_schedule, re.DOTALL)
        
        if date_match:
            date_str = date_match.group(1).strip()
            projects_data.append({"Project_Name": project_name, "st": date_str})

# Filter for projects starting in Spring 2022
spring_2022_projects = []
for project in projects_data:
    st_date = project.get("st", "")
    if st_date and ("2022-Spring" in st_date or "March 2022" in st_date or "April 2022" in st_date or "May 2022" in st_date):
        spring_2022_projects.append(project)

# Remove duplicates based on Project_Name
unique_spring_2022_projects = {}
for project in spring_2022_projects:
    unique_spring_2022_projects[project["Project_Name"]] = project

final_projects = list(unique_spring_2022_projects.values())

print('__RESULT__:')
print(json.dumps(final_projects))"""

env_args = {'var_function-call-2014731755342720335': ['civic_docs'], 'var_function-call-12362344962025889815': 'file_storage/function-call-12362344962025889815.json'}

exec(code, env_args)

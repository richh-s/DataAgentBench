code = """import json
import re

file_path = locals()['var_function-call-12362344962025889815']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

projects_data = []

for doc in civic_docs:
    text = doc['text']
    # Regex to find project names and their schedules/updates
    # It looks for a line that could be a project name, then captures the following lines
    # until it finds another potential project name or a major section heading.
    project_sections = re.findall(r'\n\n(.*?)\n\n(?:\(cid:190\)|\(cid:131\)) Updates:|\n\n(.*?)\n\n(?:\(cid:190\)|\(cid:131\)) Project Description:', text, re.DOTALL)
    
    # Let's try a more robust approach: iterate through lines and identify project names by context
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue

        # Check for major section headings
        if any(keyword in line for keyword in ["Capital Improvement Projects", "Disaster Recovery Projects"]):
            current_project = None
            continue
            
        # Look for project names (usually followed by updates or schedules)
        # A project name is likely a line that is not too short, not a heading, and doesn't contain common list item markers
        if not current_project and len(line) > 5 and not any(keyword in line.lower() for keyword in ["updates", "schedule", "design", "construction", "project description"]) and not line.startswith('(cid:'):
            # Check if the next few lines contain project schedule or update keywords to confirm it's a project name
            potential_project_name = line
            for j in range(1, min(10, len(lines) - i)): # Look at next 10 lines
                if any(keyword in lines[i+j].lower() for keyword in ["updates", "schedule", "design", "construction", "project description"]):
                    current_project = {"Project_Name": potential_project_name, "st": None}
                    break
            
        if current_project and "Schedule:" in line and ("Begin Construction:" in lines[i+1] or "Complete Design:" in lines[i+1]):
            # Extract the date from the line after "Begin Construction:" or "Complete Design:"
            for j in range(i + 1, min(i + 5, len(lines))): # Look at next few lines for 'Begin Construction' or 'Complete Design'
                if "Begin Construction:" in lines[j] or "Complete Design:" in lines[j]:
                    date_match = re.search(r'(?:Begin Construction:|Complete Design:)\s*(.*)', lines[j])
                    if date_match:
                        date_str = date_match.group(1).strip()
                        current_project["st"] = date_str
                        projects_data.append(current_project)
                        current_project = None # Reset for the next project
                        break
        elif current_project and "Project Schedule:" in line:
             for j in range(i + 1, min(i + 5, len(lines))): # Look at next few lines for 'Begin Construction' or 'Complete Design'
                if "Begin Construction:" in lines[j] or "Complete Design:" in lines[j]:
                    date_match = re.search(r'(?:Begin Construction:|Complete Design:)\s*(.*)', lines[j])
                    if date_match:
                        date_str = date_match.group(1).strip()
                        current_project["st"] = date_str
                        projects_data.append(current_project)
                        current_project = None # Reset for the next project
                        break
        elif current_project and "Estimated Schedule:" in line:
             for j in range(i + 1, min(i + 5, len(lines))): # Look at next few lines for 'Begin Construction' or 'Complete Design'
                if "Begin Construction:" in lines[j] or "Complete Design:" in lines[j]:
                    date_match = re.search(r'(?:Begin Construction:|Complete Design:)\s*(.*)', lines[j])
                    if date_match:
                        date_str = date_match.group(1).strip()
                        current_project["st"] = date_str
                        projects_data.append(current_project)
                        current_project = None # Reset for the next project
                        break


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

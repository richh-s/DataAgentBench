code = """import json
import re

with open(locals()['var_function-call-17133822943557678886'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_2022 = []
for doc in civic_docs_data:
    text = doc['text']
    
    # Regex to find project names and their details
    # This regex is an example and might need adjustment based on typical document structure
    # Looking for lines starting with '(cid:190) ' followed by project name and then details
    # Also looking for "Disaster Recovery Projects" section
    
    # Extracting "Disaster Recovery Projects" section first to narrow down the search
    disaster_section_match = re.search(r"Disaster Recovery Projects\n(.+?)(?=\nCapital Improvement Projects|\n\n|$)", text, re.DOTALL)
    if disaster_section_match:
        disaster_section_text = disaster_section_match.group(1)
        
        # Regex to find projects within the disaster section
        project_pattern = re.compile(r"\n([A-Za-z0-9][^\n]+?)(?:\n\(cid:190\) Updates:([^\n]+))?(?:\n\(cid:190\) Project Schedule:([^\n]+(?:\n\(cid:131\)[^\n]+)*))?", re.DOTALL)
        
        for match in project_pattern.finditer(disaster_section_text):
            project_name = match.group(1).strip()
            project_schedule_text = match.group(3) if match.group(3) else ""
            
            # Check if project type is disaster (explicitly from the section or keywords)
            project_type = "disaster"
            
            # Check for start date in 2022
            started_in_2022 = False
            if "Begin Construction: 2022" in project_schedule_text or \
               "Advertise: 2022" in project_schedule_text or \
               "Start: 2022" in project_schedule_text: # Add more date formats if necessary
                started_in_2022 = True
            
            # Flexible date matching for 2022
            # Spring = March-May, Summer = June-August, Fall = September-November, Winter = Dec-Feb
            if not started_in_2022:
                for month_str in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "Winter", "Spring", "Summer", "Fall"]:
                    if f"{month_str} 2022" in project_schedule_text:
                        started_in_2022 = True
                        break
                if re.search(r"2022-(Spring|Fall|Summer|Winter|0[1-9]|1[0-2])", project_schedule_text):
                    started_in_2022 = True

            if started_in_2022:
                disaster_projects_2022.append(project_name)

# Remove duplicates
disaster_projects_2022 = list(set(disaster_projects_2022))

print('__RESULT__:')
print(json.dumps(disaster_projects_2022))"""

env_args = {'var_function-call-17133822943557678886': 'file_storage/function-call-17133822943557678886.json'}

exec(code, env_args)

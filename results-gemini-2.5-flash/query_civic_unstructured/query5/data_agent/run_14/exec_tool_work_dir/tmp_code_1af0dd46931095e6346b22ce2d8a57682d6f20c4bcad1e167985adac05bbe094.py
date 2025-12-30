code = """import pandas as pd
import re
import json

with open(locals()['var_function-call-18289057968177726091'], 'r') as f:
    civic_docs = json.load(f)

disaster_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    # Regex to find project names and their details
    # Look for "Project Name" followed by updates or schedules.
    # Capture the project name, and then look for "type" and "st" (start time)
    
    # This regex attempts to capture project names (usually bold or title-cased)
    # and then looks for 'Disaster Recovery Projects' or 'FEMA' within the text
    # and then tries to extract dates.
    
    # A more robust approach might be to identify sections related to "Disaster Recovery Projects"
    # and then extract project details within those sections.
    
    # Given the unstructured nature, I will start by looking for "Disaster Recovery Projects" sections
    # and then try to extract project names and their schedules within those sections.

    # Identify Disaster Recovery Projects section
    disaster_section_match = re.search(r'Disaster Recovery Projects(?:\n|.)*?(Capital Improvement Projects|RECOMMENDED ACTION|Page \d of \d|$)', text, re.DOTALL)
    if disaster_section_match:
        disaster_section_text = disaster_section_match.group(0)
        
        # Regex to find project names and their schedules within the disaster section
        # Project names are usually followed by bullet points (cid:190) for updates and schedules.
        project_matches = re.findall(r'\n([A-Z].*? Project)(?:\n|.)*?(?:Project Schedule:|Estimated Schedule:)(?:\n|.)*?(?:Begin Construction: (.*?)|Complete Design: (.*?)|Advertise: (.*?)|Final Design: (.*?)|Project is delayed due to the Cultural Resource review)', disaster_section_text, re.DOTALL)

        for match in project_matches:
            project_name = match[0].strip()
            
            # Extract the first non-empty date that indicates a start.
            start_date = next((date for date in match[1:] if date), None)
            
            if start_date and '2022' in start_date:
                disaster_projects_2022.append({"Project_Name": project_name, "type": "disaster", "st": start_date})
    
    # Also look for project names that include "FEMA", "CalJPIA", or "CalOES" in the overall text
    # and check if their start date is in 2022.
    
    # This is a general project extraction, not specifically tied to "Disaster Recovery Projects" section
    general_project_matches = re.findall(r'\n([A-Z].*? Project)(?:\n|.)*?(?:Project Schedule:|Estimated Schedule:)(?:\n|.)*?(?:Begin Construction: (.*?)|Complete Design: (.*?)|Advertise: (.*?)|Final Design: (.*?)|Project is delayed due to the Cultural Resource review)', text, re.DOTALL)

    for match in general_project_matches:
        project_name = match[0].strip()
        start_date = next((date for date in match[1:] if date), None)

        if "FEMA" in project_name or "CalJPIA" in project_name or "CalOES" in project_name:
            if start_date and '2022' in start_date:
                disaster_projects_2022.append({"Project_Name": project_name, "type": "disaster", "st": start_date})

# Remove duplicates
unique_disaster_projects_2022 = pd.DataFrame(disaster_projects_2022).drop_duplicates().to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(unique_disaster_projects_2022))"""

env_args = {'var_function-call-18289057968177726091': 'file_storage/function-call-18289057968177726091.json'}

exec(code, env_args)

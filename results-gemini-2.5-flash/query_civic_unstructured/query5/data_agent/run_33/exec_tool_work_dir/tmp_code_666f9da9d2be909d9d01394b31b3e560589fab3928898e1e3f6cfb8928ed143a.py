code = """import json
import re

with open(locals()['var_function-call-14330681698543489492'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-12198994683327414611'], 'r') as f:
    funding_project_names_raw = json.load(f)

funding_project_names = [item['Project_Name'] for item in funding_project_names_raw]

disaster_projects_2022 = set() # Use a set to automatically handle duplicates

for doc in civic_docs:
    text = doc['text']
    
    # Split the document into sections based on project type headers
    # This helps to scope the search for 'disaster' projects.
    sections = re.split(r'(Capital Improvement Projects|Disaster Recovery Projects)', text)
    
    current_section_type = None
    
    for i, section_part in enumerate(sections):
        if section_part == "Disaster Recovery Projects":
            current_section_type = "disaster"
            continue
        elif section_part == "Capital Improvement Projects":
            current_section_type = "capital"
            continue
        
        if current_section_type == "disaster":
            # Now, within this disaster section, look for project names from the funding list
            for project_name in funding_project_names:
                # Look for the project name and then check for '2022' in its vicinity
                # Create a regex pattern to find the project name and capture some context around it.
                # Using a non-greedy match for '.*?' to not span too far.
                
                # Escape project_name for regex to handle special characters
                escaped_project_name = re.escape(project_name)
                
                # Look for the project name and then within a reasonable window (e.g., 200 chars after it) for 2022
                # or before it, if schedule comes first.
                # The pattern looks for the project name and then a schedule keyword with 2022
                # or a schedule keyword with 2022 then the project name. 
                # This attempts to associate 2022 with the project if it's close by.

                # Refined regex to capture project context to find 2022 date specifically for schedule.
                # Look for the project name within a section and then keywords related to schedule/start in 2022.
                pattern = re.compile(rf'{escaped_project_name}.{{0,200}}?(?:Begin Construction|Advertise|Project Schedule|Estimated Schedule|st:|Date prepared:|Complete Design|Start Date)[^\n]*?2022', re.DOTALL | re.IGNORECASE)
                
                if pattern.search(section_part):
                    disaster_projects_2022.add(project_name)
                    
                # Also check if 2022 is found right after the project name in a schedule context
                pattern_alt = re.compile(rf'(?:Begin Construction|Advertise|Project Schedule|Estimated Schedule|st:|Date prepared:|Complete Design|Start Date)[^\n]*?2022.*?.{{0,200}}?{escaped_project_name}', re.DOTALL | re.IGNORECASE)
                if pattern_alt.search(section_part):
                    disaster_projects_2022.add(project_name)


print("__RESULT__:")
print(json.dumps(list(disaster_projects_2022)))"""

env_args = {'var_function-call-14330681698543489492': 'file_storage/function-call-14330681698543489492.json', 'var_function-call-4615177353133977083': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an', 'var_function-call-6360808465177343412': 'file_storage/function-call-6360808465177343412.json', 'var_function-call-11720092496161089352': 'file_storage/function-call-11720092496161089352.json', 'var_function-call-12198994683327414611': 'file_storage/function-call-12198994683327414611.json'}

exec(code, env_args)

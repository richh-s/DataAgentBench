code = """import json
import re

with open(locals()['var_function-call-14330681698543489492'], 'r') as f:
    civic_docs = json.load(f)

disaster_projects_2022 = []

# Regex to capture potential project names. This pattern is less restrictive initially.
project_name_capture_pattern = re.compile(r'^\s*([A-Z][A-Za-z0-9&, -]+(?:Project|Improvements|Study|Plan|Repairs|System|Center|Park|Road|Walkway|Bridge|Drive|Lane|Way|Bluffs|Canyon|Heights|Trancas|Civic|PCH|Point Dume|Malibu|Encinal|Kanan Dume|Latigo|Morning View|Westward Beach|Clover Heights|Storm Drain|Traffic Signals|Outdoor Warning Signs|Crosswalk|Median|Shade Structure|Green Streets|Water Quality|Slope Repairs)(?: \(FEMA Project\)| \(CalJPIA Project\)| \(CalOES Project\))?)\s*$')

# Keywords to look for in schedule/updates to confirm a 2022 start/activity
schedule_keywords = ["2022-Spring", "2022-Fall", "2022-02", "2022-March", "Begin Construction: 2022", "Advertise: 2022", "Project Schedule: 2022", "Estimated Schedule: 2022", "st: 2022"]

for doc in civic_docs:
    text = doc['text']
    
    # Split the document into sections based on major project type headers
    sections = re.split(r'(Capital Improvement Projects|Disaster Recovery Projects)', text)
    
    is_disaster_section = False
    for i, section_content in enumerate(sections):
        if section_content == "Disaster Recovery Projects":
            is_disaster_section = True
            continue
        elif section_content == "Capital Improvement Projects":
            is_disaster_section = False
            continue

        if is_disaster_section and section_content.strip(): # Only process if it's a disaster section and not empty
            lines = section_content.split('\n')
            current_project = None
            for line_idx, line in enumerate(lines):
                line_stripped = line.strip()
                
                # Try to identify a project name. It should not be a sub-bullet (cid:190) or (cid:131)
                if project_name_capture_pattern.match(line_stripped):
                    current_project = line_stripped
                    # Reset for the next project
                    
                elif current_project and any(keyword in line for keyword in schedule_keywords):
                    disaster_projects_2022.append(current_project)
                    current_project = None # Reset after finding a matching project and date
                elif current_project and re.match(r'^\s*\(cid:\d+\)', line): # If we hit a bullet point, it's likely details for the current project
                    pass # Continue to check for 2022 in detail lines
                elif current_project and not line_stripped: # Blank line can separate projects or project details
                    pass
                elif current_project and project_name_capture_pattern.match(line_stripped): # If a new project name appears, previous project did not have 2022 date in scope
                    current_project = line_stripped
                elif current_project and line_stripped and not re.match(r'^\s*\(cid:\d+\)', line) and not any(keyword in line for keyword in schedule_keywords): # If we have a project but the line is not a bullet, and no schedule keyword, it's likely a description line.
                    pass

# Remove duplicates and filter out None values
disaster_projects_2022 = list(filter(None, list(set(disaster_projects_2022))))

print("__RESULT__:")
print(json.dumps(disaster_projects_2022))"""

env_args = {'var_function-call-14330681698543489492': 'file_storage/function-call-14330681698543489492.json', 'var_function-call-4615177353133977083': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an', 'var_function-call-6360808465177343412': 'file_storage/function-call-6360808465177343412.json'}

exec(code, env_args)

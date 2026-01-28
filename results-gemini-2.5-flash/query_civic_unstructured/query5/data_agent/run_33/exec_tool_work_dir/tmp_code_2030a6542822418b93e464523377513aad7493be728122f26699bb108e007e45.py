code = """import json
import re

with open(locals()['var_function-call-14330681698543489492'], 'r') as f:
    civic_docs = json.load(f)

disaster_projects_2022 = []

project_name_pattern = re.compile(r'^\s*([A-Z][A-Za-z0-9&, -]+(?:Project|Improvements|Study|Plan|Repairs|System|Center|Park|Road|Walkway|Bridge|Drive|Lane|Way|Bluffs|Canyon|Heights|Trancas|Civic|PCH|Point Dume|Malibu|Encinal|Kanan Dume|Latigo|Morning View|Westward Beach|Clover Heights|Storm Drain|Traffic Signals|Outdoor Warning Signs|Crosswalk|Median|Shade Structure|Green Streets|Water Quality|Slope Repairs)(?: \(FEMA Project\)| \(CalJPIA Project\)| \(CalOES Project\))?)(?:\s*\n|$)')

for doc in civic_docs:
    text = doc['text']
    current_project_type = None
    lines = text.split('\n')
    
    # Iterate through lines to identify sections and projects
    for i, line in enumerate(lines):
        if "Capital Improvement Projects" in line:
            current_project_type = "capital"
        elif "Disaster Recovery Projects" in line:
            current_project_type = "disaster"
        
        if current_project_type == "disaster":
            match = project_name_pattern.match(line)
            if match:
                project_name = match.group(1).strip()
                
                # Check subsequent lines for '2022' in schedule/update information
                found_2022 = False
                for j in range(i + 1, min(i + 10, len(lines))): # Look up to 10 lines ahead
                    if "2022" in lines[j] and (
                        "Begin Construction" in lines[j] or 
                        "Advertise" in lines[j] or 
                        "Project Schedule" in lines[j] or 
                        "Estimated Schedule" in lines[j] or 
                        "st: 2022" in lines[j] or 
                        "Date prepared: 2022" in lines[j] or
                        "Complete Design: 2022" in lines[j]
                    ):
                        found_2022 = True
                        break
                    # If we hit another project name before a 2022 date, this project doesn't qualify
                    if project_name_pattern.match(lines[j]):
                        break
                    # If we hit a new section header, this project doesn't qualify (it's for the previous section)
                    if "Capital Improvement Projects" in lines[j] or "Disaster Recovery Projects" in lines[j]:
                        break
                        
                if found_2022:
                    disaster_projects_2022.append(project_name)

# Remove duplicates and filter out any potential empty strings
disaster_projects_2022 = list(filter(None, list(set(disaster_projects_2022))))

print("__RESULT__:")
print(json.dumps(disaster_projects_2022))"""

env_args = {'var_function-call-14330681698543489492': 'file_storage/function-call-14330681698543489492.json', 'var_function-call-4615177353133977083': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an', 'var_function-call-6360808465177343412': 'file_storage/function-call-6360808465177343412.json', 'var_function-call-11720092496161089352': 'file_storage/function-call-11720092496161089352.json'}

exec(code, env_args)

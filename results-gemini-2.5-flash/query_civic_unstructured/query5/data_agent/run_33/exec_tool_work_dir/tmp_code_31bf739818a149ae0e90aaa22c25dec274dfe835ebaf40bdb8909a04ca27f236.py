code = """import json
import re

with open(locals()['var_function-call-14330681698543489492'], 'r') as f:
    civic_docs = json.load(f)

disaster_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    
    # Split the document by major sections to isolate 'Disaster Recovery Projects'
    sections = re.split(r'(Capital Improvement Projects|Disaster Recovery Projects)', text)
    
    is_disaster_section = False
    for i, section_part in enumerate(sections):
        if section_part == "Disaster Recovery Projects":
            is_disaster_section = True
            # The actual content of the disaster projects will be in the next section_part
            continue
        elif section_part == "Capital Improvement Projects": # Stop processing if we hit another major section type
            is_disaster_section = False
            continue

        if is_disaster_section:
            # Process the block of text assumed to contain disaster projects
            lines = section_part.split('\n')
            current_project_name = None
            for line_idx, line in enumerate(lines):
                # A simple heuristic for project names: starts with a capital letter, contains 'Project' or similar
                # and is not an update/schedule line.
                if re.match(r'^[A-Z][A-Za-z0-9&, -]+\s*(?:Project|Improvements|Study|Plan|Repairs|System|Center|Park|Road|Walkway|Bridge|Drive|Lane|Way|Bluffs|Canyon|Heights|Trancas|Civic|PCH|Point Dume|Malibu|Encinal|Kanan Dume|Latigo|Morning View|Westward Beach|Clover Heights|Storm Drain|Traffic Signals|Outdoor Warning Signs|Crosswalk|Median|Shade Structure|Green Streets|Water Quality|Slope Repairs)(?: \(FEMA Project\)| \(CalJPIA Project\)| \(CalOES Project\))?$', line.strip()) and not re.match(r'^\s*\(cid:\d+\)', line):
                    current_project_name = line.strip()
                elif current_project_name and ("2022" in line) and ("Begin Construction" in line or "Advertise" in line or "Project Schedule" in line or "Estimated Schedule" in line or "st: 2022" in line):
                    disaster_projects_2022.append(current_project_name)
                    current_project_name = None # Reset after finding a matching project and date

# Remove duplicates and filter out None values if any crept in
disaster_projects_2022 = list(filter(None, list(set(disaster_projects_2022))))

print("__RESULT__:")
print(json.dumps(disaster_projects_2022))"""

env_args = {'var_function-call-14330681698543489492': 'file_storage/function-call-14330681698543489492.json', 'var_function-call-4615177353133977083': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}

exec(code, env_args)

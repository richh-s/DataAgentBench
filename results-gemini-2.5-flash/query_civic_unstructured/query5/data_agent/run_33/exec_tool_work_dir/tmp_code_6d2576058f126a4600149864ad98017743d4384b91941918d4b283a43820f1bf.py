code = """import json
import re

with open(locals()['var_function-call-14330681698543489492'], 'r') as f:
    civic_docs = json.load(f)

disaster_projects_2022 = []

project_name_pattern = re.compile(r'^([A-Z][A-Za-z0-9&, -]+(?:Project|Improvements|Study|Plan|Repairs|System|Center|Park|Road|Walkway|Bridge|Drive|Lane|Way|Bluffs|Canyon|Heights|Trancas|Civic|PCH|Point Dume|Malibu|Encinal|Kanan Dume|Latigo|Morning View|Westward Beach|Clover Heights|Storm Drain|Traffic Signals|Outdoor Warning Signs|Crosswalk|Median|Shade Structure|Green Streets|Water Quality|Slope Repairs)(?: \(FEMA Project\)| \(CalJPIA Project\)| \(CalOES Project\))?)$|^([A-Z][A-Za-z0-9&, -]+)(?=\n\s*\(cid:190) Updates:)')

for doc in civic_docs:
    text = doc['text']
    current_type = None
    lines = text.split('\n')

    for i, line in enumerate(lines):
        if "Capital Improvement Projects" in line:
            current_type = "capital"
        elif "Disaster Recovery Projects" in line:
            current_type = "disaster"

        if current_type == "disaster":
            match = project_name_pattern.match(line.strip())
            if match:
                project_name = match.group(1) if match.group(1) else match.group(2)
                project_name = project_name.strip()

                # Look for '2022' in the next few lines for schedule/updates
                for j in range(i + 1, min(i + 10, len(lines))):
                    if "2022" in lines[j]:
                        disaster_projects_2022.append(project_name)
                        break # Found a 2022 date, move to the next project search

# Remove duplicates
disaster_projects_2022 = list(set(disaster_projects_2022))

print("__RESULT__:")
print(json.dumps(disaster_projects_2022))"""

env_args = {'var_function-call-14330681698543489492': 'file_storage/function-call-14330681698543489492.json', 'var_function-call-4615177353133977083': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}

exec(code, env_args)

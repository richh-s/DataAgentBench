code = """import json
import re

with open(locals()['var_function-call-14330681698543489492'], 'r') as f:
    civic_docs = json.load(f) # Directly load the content of the file.

disaster_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    
    # Split the document into sections based on project headings or similar patterns
    # This is a heuristic approach and might need refinement based on actual document structure
    project_sections = re.split(r'\n\n(?=[A-Z][A-Za-z ]+(?:Project|Improvements|Study|Plan))\n', text)

    for section in project_sections:
        project_name_match = re.search(r'([A-Z][A-Za-z0-9&, -]+(?:Project|Improvements|Study|Plan|Repairs|System|Center|Park|Road|Walkway|Bridge|Drive|Lane|Way|Bluffs|Canyon|Heights|Trancas|Civic|PCH|Point Dume|Malibu|Encinal|Kanan Dume|Latigo|Morning View|Westward Beach|Clover Heights|Storm Drain|Traffic Signals|Outdoor Warning Signs|Crosswalk|Median|Shade Structure|Green Streets|Water Quality|Slope Repairs)(?: \(FEMA Project\)| \(CalJPIA Project\)| \(CalOES Project\))?)', section)
        project_type_match = re.search(r'(Capital Improvement Projects|Disaster Recovery Projects)', section)
        start_date_match = re.search(r'(?:Begin Construction|Advertise|Start Date|Begin work):\s*(.*?2022.*?)\n', section)
        
        project_name = project_name_match.group(1).strip() if project_name_match else None
        project_type = project_type_match.group(1).strip() if project_type_match else None
        start_date = start_date_match.group(1).strip() if start_date_match else None

        if project_name and project_type and "Disaster Recovery Projects" in project_type and start_date and "2022" in start_date:
            disaster_projects_2022.append(project_name)

# Remove duplicates
disaster_projects_2022 = list(set(disaster_projects_2022))

print("__RESULT__:")
print(json.dumps(disaster_projects_2022))"""

env_args = {'var_function-call-14330681698543489492': 'file_storage/function-call-14330681698543489492.json'}

exec(code, env_args)

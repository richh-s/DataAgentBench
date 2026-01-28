code = """import json
import re

def parse_project_details(text):
    projects = []
    # Split the document into sections based on project headings
    project_sections = re.split(r"\n\n([A-Za-z0-9][A-Za-z0-9\\s&,-_\\\\/()]+?(?:Project|Improvements|Plan|Repair|Study|System|Power|Signal|Biofilter|Screens|Structure|Slopes|Facility|Park|Traffic Signals)\n\n(?:\\(cid:190\\)|\\(cid:131\\)) Updates:)", text)

    # The first split part is usually header info, skip it or handle if needed
    if len(project_sections) > 1:
        # Iterate through project sections, each project has a name followed by its details
        for i in range(1, len(project_sections), 2):
            project_name = project_sections[i].strip()
            details_text = project_sections[i+1]

            project_type = "capital" if "Capital Improvement Projects" in text and project_name in details_text or "Capital Improvement Program" in text and project_name in details_text else None
            if not project_type:
                project_type = "disaster" if "Disaster Recovery Projects" in text and project_name in details_text else None

            start_time = None
            start_time_match = re.search(r"(?:Begin Construction|Advertise|Complete Design|Final Design|Estimated Schedule|Project Schedule):\n\n(?:\\(cid:131\\))\\s*(.*?)(?=\n(?:\\(cid:131\\)|\\(cid:190\\)|\\Z))", details_text, re.DOTALL)
            if start_time_match:
                # Take the first date as start_time. If multiple dates are present, take the earliest one.
                all_dates = re.findall(r"\\b(20\\d{2}(?:-\w+)?)\\b", start_time_match.group(1))
                if all_dates:
                    start_time = all_dates[0] # Assuming the first date is the start date.

            # More robust type extraction, looking for keywords
            if "FEMA" in details_text or "CalOES" in details_text or "Disaster Recovery" in details_text:
                project_type = "disaster"
            elif "Capital Improvement" in details_text:
                project_type = "capital"

            if project_name and project_type == "disaster" and start_time and "2022" in start_time:
                projects.append({
                    "Project_Name": project_name,
                    "type": project_type,
                    "st": start_time
                })
    return projects


all_docs = locals()['var_function-call-998581038436713793'] # this is a file path since the result was too large

# Load the full JSON data from the file
with open(all_docs, 'r') as f:
    data = json.load(f)


all_projects = []
for doc in data:
    all_projects.extend(parse_project_details(doc['text']))


# Filter for unique projects (Project_Name, type, st) as there might be duplicates across documents or within a document due to parsing.
unique_projects = []
seen = set()
for p in all_projects:
    project_tuple = (p['Project_Name'], p['type'], p['st'])
    if project_tuple not in seen:
        unique_projects.append(p)
        seen.add(project_tuple)

print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-998581038436713793': 'file_storage/function-call-998581038436713793.json'}

exec(code, env_args)

code = """import re
import json

with open(locals()['var_function-call-12019545950990235535'], 'r') as f:
    civic_docs_data = json.load(f)

def extract_project_details(text):
    projects = []
    # Regular expression to find project names and their details.
    # It looks for a project name (usually on a new line, capitalized),
    # followed by 'Updates:' or 'Project Description:', then 'Project Schedule:' or 'Estimated Schedule:' or 'Updates:' (for start date)
    # and tries to capture the project type and start date/year.

    # This pattern attempts to be more robust by looking for common project headings
    # and then capturing the lines that follow to find keywords and dates.
    # It assumes project names are typically followed by "Updates:" or "Project Schedule:" etc.

    project_pattern = re.compile(r"\n\n([A-Z][a-zA-Z0-9&,\- ]+?)\n(?:\(cid:190\) Updates:|\(cid:190\) Project Description:|\(cid:190\) Project Schedule:|\(cid:190\) Estimated Schedule:)(.*?)(?=\n\n[A-Z][a-zA-Z0-9&,\- ]+?\n(?:\(cid:190\) Updates:|\(cid:190\) Project Description:|\(cid:190\) Project Schedule:|\(cid:190\) Estimated Schedule:)|$)", re.DOTALL)

    # Specific patterns to extract info within each project's block
    type_pattern = re.compile(r"(Capital Improvement Projects|Disaster Recovery Projects)", re.IGNORECASE)
    start_date_pattern = re.compile(r"(?:Begin Construction|Advertise|Start|st):\s*(?:Spring|Summer|Fall|Winter|\d{4}-\d{2}|\d{4}-?(?:January|February|March|April|May|June|July|August|September|October|November|December)?|\d{4})", re.IGNORECASE)

    matches = project_pattern.findall(text)

    for name, details_block in matches:
        project_name = name.strip()
        project_type = "unknown"
        start_year = None

        type_match = type_pattern.search(details_block)
        if type_match:
            if "Disaster Recovery Projects" in type_match.group(0):
                project_type = "disaster"
            elif "Capital Improvement Projects" in type_match.group(0):
                project_type = "capital"

        start_date_match = start_date_pattern.search(details_block)
        if start_date_match:
            date_str = start_date_match.group(0)
            year_match = re.search(r"(\d{4})", date_str)
            if year_match:
                start_year = int(year_match.group(1))
            else:
                if "Spring" in date_str or "Summer" in date_str or "Fall" in date_str or "Winter" in date_str:
                    year_in_block = re.search(r"(\d{4})", details_block)
                    if year_in_block:
                        start_year = int(year_in_block.group(1))

        if project_type != "unknown" and start_year: # Only include projects where type and start year are found
            projects.append({"Project_Name": project_name, "type": project_type, "st_year": start_year})
    return projects

all_projects = []
for doc in civic_docs_data:
    all_projects.extend(extract_project_details(doc['text']))

# Filter for disaster projects starting in 2022
disaster_projects_2022 = [p for p in all_projects if p['type'] == 'disaster' and p['st_year'] == 2022]

# Remove duplicates if any (same project name might appear in multiple docs or multiple times in one doc)
unique_disaster_projects_2022 = []
seen_project_names = set()
for project in disaster_projects_2022:
    if project['Project_Name'] not in seen_project_names:
        unique_disaster_projects_2022.append(project)
        seen_project_names.add(project['Project_Name'])

print('__RESULT__:')
print(json.dumps(unique_disaster_projects_2022)))"""

env_args = {'var_function-call-14391641347540383494': ['civic_docs'], 'var_function-call-12019545950990235535': 'file_storage/function-call-12019545950990235535.json'}

exec(code, env_args)

code = """import json
import re

with open(locals()['var_function-call-16813778080259091819'], 'r') as f:
    civic_docs = json.load(f)

extracted_projects = []

for doc in civic_docs:
    text = doc['text']

    # Use a simpler regex to extract potential project blocks. This looks for a string that is likely a project name
    # followed by a newline and then '(cid:190) Updates:' and captures the text until the next similar pattern or end of document.
    # The regex is carefully escaped for use within a Python string literal.
    project_block_matches = re.finditer(
        '\\n\\n(.*?)\\n\\s*\\(cid:190\\) Updates:(.*?)(?=\\n\\n|$)',
        text, re.DOTALL
    )

    for match in project_block_matches:
        project_name = match.group(1).strip()
        details_text = match.group(2).strip()

        project_type = "capital" # Default type

        # Check for keywords to determine if it's a disaster project
        if "disaster" in project_name.lower() or "fema" in project_name.lower() or \
           "caljpia" in project_name.lower() or "caloes" in project_name.lower():
            project_type = "disaster"
        elif "disaster" in details_text.lower() or "fema" in details_text.lower() or \
             "caljpia" in details_text.lower() or "caloes" in details_text.lower():
            project_type = "disaster"
        # Additionally, if the entire document text contains "Disaster Recovery Projects", it's a strong indicator
        elif "disaster recovery projects" in text.lower():
            project_type = "disaster"

        start_date = None
        # Search for explicit "Begin Construction: DATE" or similar patterns
        start_date_match = re.search(r'Begin (?:Construction|Work|Project):\\s*(\\w+\\s*\\d{4}|\\d{4}-\\w+)', details_text)
        if start_date_match:
            start_date = start_date_match.group(1)
        else:
            # A fallback if a direct "Begin Construction" is not found, looking for 2022 in general schedule context
            # This is a less precise match, assuming if 2022 is present in schedule info, it's a start date.
            year_in_schedule_match = re.search(r'\\b(2022(?:-\\w+)?|\\w+ 2022)\\b', details_text)
            if year_in_schedule_match:
                start_date = year_in_schedule_match.group(0)

        if project_name:
            extracted_projects.append({
                'Project_Name': project_name,
                'type': project_type,
                'st': start_date
            })

# Filter for disaster projects that started in 2022
disaster_projects_2022_filtered = []
for project in extracted_projects:
    if project['type'] == 'disaster' and project['st'] and '2022' in project['st']:
        disaster_projects_2022_filtered.append(project)

print('__RESULT__:')
print(json.dumps(disaster_projects_2022_filtered)))"""

env_args = {'var_function-call-13790590049181057957': ['civic_docs'], 'var_function-call-3607000441821407365': 'file_storage/function-call-3607000441821407365.json', 'var_function-call-3146719146564769422': ['Funding'], 'var_function-call-16813778080259091819': 'file_storage/function-call-16813778080259091819.json'}

exec(code, env_args)

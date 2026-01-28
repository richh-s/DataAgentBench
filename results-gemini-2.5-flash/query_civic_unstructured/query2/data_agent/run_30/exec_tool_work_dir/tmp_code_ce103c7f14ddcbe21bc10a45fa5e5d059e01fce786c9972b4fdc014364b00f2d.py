code = """import json
import re

with open(locals()['var_function-call-7990474508499764104'], 'r') as f:
    civic_docs = json.load(f)

completed_park_projects_2022_names = []

for doc in civic_docs:
    text = doc['text']
    
    # Split the document by lines that start with a capital letter, which often indicates a new project.
    # This is a heuristic and might not be perfect for all documents, but should capture most.
    # Using a non-greedy match for the details block.
    project_blocks = re.findall(
        r'(?m)^([A-Z][a-zA-Z0-9&\\s\\-]+(?:Project|Park|Playground|Improvements)?(?:\\s\\(FEMA Project\\))?)\n'
        r'((?:(?!^[A-Z][a-zA-Z0-9&\\s\\-]+(?:Project|Park|Playground|Improvements)?(?:\\s\\(FEMA Project\\))?).)*)',
        text, re.DOTALL
    )

    for project_name_raw, details_raw in project_blocks:
        project_name = project_name_raw.strip()
        details = details_raw.strip()

        is_park_project = False
        if 'Park' in project_name or 'Playground' in project_name:
            is_park_project = True
        # Also check in details if a topic field or similar explicitly mentions park/playground
        elif re.search(r'topic:\\s*.*?park|playground', details, re.IGNORECASE):
            is_park_project = True

        if is_park_project:
            # Check for completion status and 2022 in the details block
            # This pattern is refined to capture various phrases indicating completion in 2022.
            # We are looking for 'completed' or 'construction was completed' or 'notice of completion filed'
            # along with '2022' either directly or within a date phrase.
            if re.search(r'(completed|Construction was completed|Notice of completion filed).*?2022', details, re.IGNORECASE) or \
               re.search(r'2022.*?(completed|Construction was completed|Notice of completion filed)', details, re.IGNORECASE) or \
               re.search(r'(Complete Construction|Complete Design):.*?2022', details, re.IGNORECASE) or \
               re.search(r'(November|December).*?2022', details, re.IGNORECASE):
                completed_park_projects_2022_names.append(project_name)

# Remove duplicates and clean up project names (e.g., remove '(cid:190)')
unique_completed_park_projects_2022 = []
for name in list(set(completed_park_projects_2022_names)):
    cleaned_name = re.sub(r'\\(cid:190\\)|\\s\\(cid:131\\)', '', name).strip()
    unique_completed_park_projects_2022.append(cleaned_name)

print("__RESULT__:")
print(json.dumps(unique_completed_park_projects_2022)))"""

env_args = {'var_function-call-2531287041203044027': ['civic_docs'], 'var_function-call-7990474508499764104': 'file_storage/function-call-7990474508499764104.json', 'var_function-call-16366149949085286234': ['test'], 'var_function-call-18034137513589187498': ['Funding']}

exec(code, env_args)

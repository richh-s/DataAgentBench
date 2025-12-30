code = """import json
import re

def extract_project_info(text):
    projects = []
    # This regex is for the `code` argument, so single quotes are escaped with `\'`.
    # Raw string `r\'...\'` is used, and backslashes inside are double escaped `\\n` for `\n`.
    project_blocks_raw = re.findall(r'\\n\\n([A-Z][^\\n]+?)(?:\\n\\n|\\n)(?:\\(cid:190\\)|Updates:|Project Schedule:|Estimated Schedule:|Project Description:|RECOMMENDED ACTION:)(.*?)(?=\\n\\n[A-Z][^\\n]+?(?:\\n\\n|\\n)(?:\\(cid:190\\)|Updates:|Project Schedule:|Estimated Schedule:|Project Description:|RECOMMENDED ACTION:)|\\Z)', text, re.DOTALL)

    for project_name, details in project_blocks_raw:
        project_name = project_name.strip()
        details = details.strip()

        topic = 'N/A'
        project_type = 'N/A'
        status = 'N/A'
        et = 'N/A'

        if re.search(r'park|playground', project_name, re.IGNORECASE) or re.search(r'park|playground', details, re.IGNORECASE):
            topic = 'park'

        if re.search(r'Capital Improvement Projects', details, re.IGNORECASE):
            project_type = 'capital'
        elif re.search(r'Disaster Recovery Projects', details, re.IGNORECASE):
            project_type = 'disaster'

        if re.search(r'construction was completed|complete construction|notice of completion filed', details, re.IGNORECASE):
            status = 'completed'
        elif re.search(r'project is currently under construction', details, re.IGNORECASE):
            status = 'under construction'
        elif re.search(r'preliminary design phase|complete design|design plans for this project|final design', details, re.IGNORECASE):
            status = 'design'
        elif re.search(r'not started', details, re.IGNORECASE):
            status = 'not started'

        et_match = re.search(r'(?:Complete Construction|construction was completed|Complete design|advertise|begin construction):.*?((?:\\d{4}|Spring|Summer|Fall|Winter).*?)(?:\\n|$)', details, re.IGNORECASE)
        if et_match:
            et = et_match.group(1).strip()
            
        projects.append({
            'Project_Name': project_name,
            'topic': topic,
            'type': project_type,
            'status': status,
            'et': et
        })
    return projects

all_projects = []
with open(locals()['var_function-call-10538662838025527717'], 'r') as f:
    data = json.load(f)
    for doc in data:
        all_projects.extend(extract_project_info(doc['text']))

filtered_projects = [
    p for p in all_projects 
    if p['topic'] == 'park' and 
       p['status'] == 'completed' and 
       '2022' in str(p['et'])
]

unique_project_names = list(set([p['Project_Name'] for p in filtered_projects]))

print('__RESULT__:')
print(json.dumps(unique_project_names)))"""

env_args = {'var_function-call-6798812027977815214': ['civic_docs'], 'var_function-call-10538662838025527717': 'file_storage/function-call-10538662838025527717.json'}

exec(code, env_args)

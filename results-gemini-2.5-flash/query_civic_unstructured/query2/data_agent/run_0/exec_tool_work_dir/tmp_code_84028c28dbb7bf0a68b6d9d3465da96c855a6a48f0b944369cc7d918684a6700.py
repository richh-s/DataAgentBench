code = """import re
import json

docs_filepath = locals()['var_function-call-10727724106832810456']
with open(docs_filepath, 'r') as f:
    docs_content = json.load(f)

projects = []

for doc in docs_content:
    text = doc['text']

    # Regex to find project blocks
    project_blocks = re.findall(r'\n\n(.*?)\n\n(?:\(cid:190\)|Project Description:|Updates:)', text, re.DOTALL)
    
    for block in project_blocks:
        project_name_match = re.search(r'^(.*?)(?:\n|\(cid:190\))', block)
        if project_name_match:
            project_name = project_name_match.group(1).strip()

            # Extracting status, topic, and end date
            status_match = re.search(r'Updates: (Construction was completed|Project is currently under construction|Project is in the preliminary design phase|City to request proposal from consultant for design services|Project to be discussed during a joint Public Works and Public Safety\nCommission meeting for project direction|City submitted plans to Caltrans for review|Staff is currently working on the final design plans|City submitted plans to CalOES for review|Plans are under review by Fish and Wildlife|City working with consultant on the design of the shoulder repairs|On September 22, 2022, the City received four \(4\) construction bids|Staff is working with the consultant to finalize the design plans|Field data collection has been completed|Plans and specifications have been completed|Staff is working with the State Water Board regarding the Cultural\nResources review|Funding agreement is schedule for city council on March 27, 2023|Project is currently under construction|Project is currently out to bid|Construction was completed|Notice of completion filed|Project is in the preliminary design phase|City has submitted an application through Measure R and is\nwaiting for the agreement.)', block)
            status = status_match.group(1).strip() if status_match else 'unknown'

            et_match = re.search(r'(?:Complete Construction|Construction was completed),?\s*(\w+\s*\d{4}|\d{4}-\w+|\w+ \d{4}|\d{4})', block)
            et = et_match.group(1).strip() if et_match else 'unknown'

            topic_match = re.search(r'^(.*?)(?:\n|\(cid:190\))', block)
            topic = "park" if "Park" in project_name or "Playground" in project_name or "Bluffs" in project_name else "unknown"
            
            if project_name and topic != "unknown" and status.lower().startswith('construction was completed') and '2022' in et:
                projects.append({'Project_Name': project_name, 'topic': topic, 'status': 'completed', 'et': et})


# Filter for projects completed in 2022 and related to parks
filtered_projects = [
    p for p in projects 
    if p['topic'] == 'park' and p['status'] == 'completed' and '2022' in p['et']
]

print("__RESULT__:")
print(json.dumps(filtered_projects))"""

env_args = {'var_function-call-10727724106832810456': 'file_storage/function-call-10727724106832810456.json'}

exec(code, env_args)

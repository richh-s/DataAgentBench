code = """import json
import re

with open(locals()['var_function-call-13241760497320549299'], 'r') as f:
    civic_docs = json.load(f)
with open(locals()['var_function-call-8006204082577017619'], 'r') as f:
    funding = json.load(f)

project_map = {p['Project_Name']: int(p['Amount']) for p in funding}
found_projects = set()

for doc in civic_docs:
    text = doc['text']
    for proj_name in project_map:
        if proj_name in found_projects:
            continue
        if proj_name in text:
            idx = text.find(proj_name)
            # Limit chunk size
            chunk = text[idx:idx+2000]
            
            # Find Begin Construction line
            # Look for "Begin Construction" followed by anything until newline
            match = re.search("Begin Construction[:\\s]+([^\\n]+)", chunk, re.IGNORECASE)
            if match:
                date_str = match.group(1)
                # Check for Spring 2022
                if "Spring 2022" in date_str or "March 2022" in date_str or "April 2022" in date_str or "May 2022" in date_str:
                    found_projects.add(proj_name)
            
            # Also check for "Advertise: Spring 2022" if Begin Construction is not found?
            # Or maybe "Start: Spring 2022"
            if proj_name not in found_projects:
                match_adv = re.search("Advertise[:\\s]+([^\\n]+)", chunk, re.IGNORECASE)
                if match_adv:
                    date_str = match_adv.group(1)
                    # If Advertise is Spring 2022, is that "started"?
                    # Usually Advertise is before Construction.
                    # But if the project is "Design", Advertise might be the next step.
                    pass

count = len(found_projects)
total_funding = sum(project_map[p] for p in found_projects)

print("__RESULT__:")
print(json.dumps({"count": count, "total_funding": total_funding, "projects": list(found_projects)}))"""

env_args = {'var_function-call-14343582955729451491': 'file_storage/function-call-14343582955729451491.json', 'var_function-call-8006204082577017619': 'file_storage/function-call-8006204082577017619.json', 'var_function-call-13241760497320549299': 'file_storage/function-call-13241760497320549299.json', 'var_function-call-857092213890831436': 5}

exec(code, env_args)

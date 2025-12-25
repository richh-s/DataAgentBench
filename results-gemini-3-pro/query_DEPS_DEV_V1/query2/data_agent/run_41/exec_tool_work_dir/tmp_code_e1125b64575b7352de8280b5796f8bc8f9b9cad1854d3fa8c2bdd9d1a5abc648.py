code = """import json
import re

path_info = locals()['var_function-call-10398229597847549706']
with open(path_info, 'r') as f:
    project_info_data = json.load(f)

# Parse info to get list of (ProjectName, Forks)
project_list = []
name_pattern = re.compile(r'\b([a-zA-Z0-9\-\.]+\/[a-zA-Z0-9\-\.]+)\b')
fork_patterns = [
    re.compile(r'and ([\d,]+) forks'),
    re.compile(r'forks count of ([\d,]+)'),
    re.compile(r'forked ([\d,]+) times'),
    re.compile(r'([\d,]+) forks')
]

for row in project_info_data:
    info = row.get('Project_Information', '')
    if not info:
        continue
    
    # Extract names
    # Usually the first match is the project name, or we look for specific patterns
    # "The project <name> is hosted"
    # "The GitHub project <name>"
    names = name_pattern.findall(info)
    # Filter out common non-project strings if any (like 'open-source', 'github.com')
    # But usually owner/repo has a slash.
    
    # Extract forks
    forks = 0
    for pat in fork_patterns:
        m = pat.search(info)
        if m:
            try:
                forks = int(m.group(1).replace(',', ''))
                break
            except:
                pass
    
    # We associate this fork count with ALL names found in the description?
    # Or just the first one?
    # Usually the description talks about one project.
    if names:
        # Heuristic: the project name usually appears early or after "project"
        # Let's take the first one that looks like owner/repo
        # We can also keep all of them as candidates.
        for n in names:
            if '/' in n and not n.startswith('github.com'):
                project_list.append({'ProjectName': n, 'Forks': forks})

print("__RESULT__:")
print(json.dumps(project_list))"""

env_args = {'var_function-call-11065893993173379102': ['project_info', 'project_packageversion'], 'var_function-call-15361139508270201429': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-40608375882137146': [{'cid': '0', 'name': 'Project_Information', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'Licenses', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'Description', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'Homepage', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'OSSFuzz', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_function-call-2678515795771401501': 'file_storage/function-call-2678515795771401501.json', 'var_function-call-8867938047833477408': 'file_storage/function-call-8867938047833477408.json', 'var_function-call-10398229597847549706': 'file_storage/function-call-10398229597847549706.json', 'var_function-call-12200236935107415748': [], 'var_function-call-15138716392146612001': 'debug done', 'var_function-call-5922763594562684266': {'total_packages': 391228, 'valid_packages': 85158, 'candidate_projects': 5477, 'sample_candidates': ['ecomclub/search-engine', 'sindresorhus/caller-path', 'dobuzi/nooks', 'economist-components/react-i13n-tealium', 'donotjs/donot-transform-stylus'], 'matched_projects_in_info': 0, 'total_info_rows': 770, 'sample_info_row': {'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}}, 'var_function-call-2797303438942603563': [{'count_star()': '770'}]}

exec(code, env_args)

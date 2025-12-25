code = """import json
import re

path_pkg = locals()['var_function-call-2678515795771401501']
path_pv = locals()['var_function-call-8867938047833477408']
path_info = locals()['var_function-call-10398229597847549706']

# Load data (only taking partial if needed, but loading all for stats)
with open(path_pkg, 'r') as f:
    package_data = json.load(f)
with open(path_pv, 'r') as f:
    project_pv_data = json.load(f)
with open(path_info, 'r') as f:
    project_info_data = json.load(f)

stats = {}
stats['total_packages'] = len(package_data)

valid_packages = set()
for pkg in package_data:
    licenses = pkg.get('Licenses', '[]')
    if 'MIT' not in licenses:
        continue
    vinfo = pkg.get('VersionInfo', '{}')
    if '"IsRelease": true' in vinfo or '"IsRelease":true' in vinfo:
         valid_packages.add((pkg['Name'], pkg['Version']))
    elif 'true' in vinfo: 
         try:
             v_obj = json.loads(vinfo)
             if v_obj.get('IsRelease'):
                 valid_packages.add((pkg['Name'], pkg['Version']))
         except:
             pass
stats['valid_packages'] = len(valid_packages)

candidate_projects = set()
for row in project_pv_data:
    if (row['Name'], row['Version']) in valid_packages:
        if row.get('ProjectName'):
            candidate_projects.add(row['ProjectName'])
stats['candidate_projects'] = len(candidate_projects)
stats['sample_candidates'] = list(candidate_projects)[:5]

name_pattern = re.compile(r'\b([a-zA-Z0-9\-\.]+\/[a-zA-Z0-9\-\.]+)\b')
matched_count = 0
for row in project_info_data:
    info = row.get('Project_Information', '')
    found_names = set(name_pattern.findall(info))
    matched = found_names.intersection(candidate_projects)
    if matched:
        matched_count += 1

stats['matched_projects_in_info'] = matched_count
stats['total_info_rows'] = len(project_info_data)
stats['sample_info_row'] = project_info_data[0] if project_info_data else None

print("__RESULT__:")
print(json.dumps(stats))"""

env_args = {'var_function-call-11065893993173379102': ['project_info', 'project_packageversion'], 'var_function-call-15361139508270201429': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-40608375882137146': [{'cid': '0', 'name': 'Project_Information', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'Licenses', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'Description', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'Homepage', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'OSSFuzz', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_function-call-2678515795771401501': 'file_storage/function-call-2678515795771401501.json', 'var_function-call-8867938047833477408': 'file_storage/function-call-8867938047833477408.json', 'var_function-call-10398229597847549706': 'file_storage/function-call-10398229597847549706.json', 'var_function-call-12200236935107415748': [], 'var_function-call-15138716392146612001': 'debug done'}

exec(code, env_args)

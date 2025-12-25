code = """import json
import re

# Load data again
with open(locals()['var_function-call-4091625522379036388']) as f:
    package_rows = json.load(f)
with open(locals()['var_function-call-4091625522379036045']) as f:
    mapping_rows = json.load(f)
with open(locals()['var_function-call-4091625522379035702']) as f:
    info_rows = json.load(f)

# Re-run logic step by step with prints

valid_pkg_keys = set()
for r in package_rows:
    valid_pkg_keys.add((r['Name'], r['Version']))
print(f"Valid packages count: {len(valid_pkg_keys)}")

relevant_projects = set()
for r in mapping_rows:
    if (r['Name'], r['Version']) in valid_pkg_keys:
        relevant_projects.add(r['ProjectName'])
print(f"Relevant projects count: {len(relevant_projects)}")
print(f"Sample relevant projects: {list(relevant_projects)[:5]}")

project_stats = {}
fork_patterns = [
    r'(\d+)\s+forks?',
    r'forks? count of (\d+)',
    r'forked (\d+) times'
]
name_pattern = re.compile(r'\b(?=[a-zA-Z0-9\-\.]*[a-zA-Z])[a-zA-Z0-9\-\.]+\/(?=[a-zA-Z0-9\-\.]*[a-zA-Z])[a-zA-Z0-9\-\.]+\b')

sample_parse = []

for i, row in enumerate(info_rows):
    text = row['Project_Information']
    
    forks = 0
    for pat in fork_patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            try:
                forks = int(m.group(1).replace(',', ''))
                break
            except:
                pass
                
    candidates = name_pattern.findall(text)
    project_name = None
    for cand in candidates:
        if cand.lower() in ['github/project', 'github/repository', 'project/name']: continue
        project_name = cand
        break
    
    if project_name:
        project_stats[project_name.lower()] = {'real_name': project_name, 'forks': forks}
        if i < 5:
            sample_parse.append(f"Text: {text[:50]}... -> Name: {project_name}, Forks: {forks}")

print(f"Project stats count: {len(project_stats)}")
print(f"Sample stats keys: {list(project_stats.keys())[:5]}")
print("Sample parses:")
for s in sample_parse:
    print(s)

# Check overlap
overlap = 0
for p in relevant_projects:
    if p.lower() in project_stats:
        overlap += 1
print(f"Overlap count: {overlap}")

print('__RESULT__:')
print('"done"')"""

env_args = {'var_function-call-6485848890492900329': ['packageinfo'], 'var_function-call-6485848890492900454': ['project_info', 'project_packageversion'], 'var_function-call-474351073472527354': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-17329601053264025037': [{'count_star()': '770'}], 'var_function-call-15234202801282220009': [{'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Licenses': '[\n  "EUPL-1.2"\n]'}, {'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Licenses': '[]'}, {'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Licenses': '[]'}, {'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'Licenses': '[\n  "ISC"\n]'}, {'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Licenses': '[\n  "MIT"\n]'}], 'var_function-call-3894250662162695542': [{'COUNT(*)': '661372'}], 'var_function-call-543603203718078934': [{'COUNT(*)': '176170'}], 'var_function-call-13912716373860961398': [{'count_star()': '597602'}], 'var_function-call-4091625522379036388': 'file_storage/function-call-4091625522379036388.json', 'var_function-call-4091625522379036045': 'file_storage/function-call-4091625522379036045.json', 'var_function-call-4091625522379035702': 'file_storage/function-call-4091625522379035702.json', 'var_function-call-12052291588044334746': []}

exec(code, env_args)

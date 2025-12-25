code = """import json
import re
import pandas as pd

# Load previous results
with open(locals()['var_function-call-4091625522379036388']) as f:
    package_rows = json.load(f)
with open(locals()['var_function-call-4091625522379036045']) as f:
    mapping_rows = json.load(f)
with open(locals()['var_function-call-4091625522379035702']) as f:
    info_rows = json.load(f)

# 1. Valid packages set (Name, Version)
valid_pkg_keys = set()
for r in package_rows:
    valid_pkg_keys.add((r['Name'], r['Version']))

# 2. Get relevant projects from mapping
relevant_projects = set()
for r in mapping_rows:
    if (r['Name'], r['Version']) in valid_pkg_keys:
        relevant_projects.add(r['ProjectName'])

# 3. Parse project info to get forks
# Map lower_case_name -> {real_name, forks}
project_stats = {}

fork_patterns = [
    r'(\d+)\s+forks?',
    r'forks? count of (\d+)',
    r'forked (\d+) times'
]

# Regex for project name: owner/repo
# Avoid matches like "N/A" or date "1/2" if possible, though repo names usually have letters.
# Pattern: word chars, dots, dashes / word chars, dots, dashes
# Must contain at least one letter?
name_pattern = re.compile(r'\b(?=[a-zA-Z0-9\-\.]*[a-zA-Z])[a-zA-Z0-9\-\.]+\/(?=[a-zA-Z0-9\-\.]*[a-zA-Z])[a-zA-Z0-9\-\.]+\b')

for row in info_rows:
    text = row['Project_Information']
    if not text:
        continue
        
    # Extract Forks
    forks = 0
    found_forks = False
    for pat in fork_patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            try:
                forks = int(m.group(1).replace(',', ''))
                found_forks = True
                break
            except:
                pass
    
    # Extract Name
    # Find all candidates, pick the first one that looks like a repo (not a url part)
    # The regex above excludes http:// because of the colon check (implied by \b and char set)
    
    candidates = name_pattern.findall(text)
    
    project_name = None
    for cand in candidates:
        # Heuristic: Filter out obvious non-repos
        if cand.lower() in ['github/project', 'github/repository', 'project/name']:
            continue
        project_name = cand
        break
    
    if project_name:
        # Store
        # Handle duplicate info rows? Just overwrite or keep max?
        # Assuming unique project_info rows per project.
        project_stats[project_name.lower()] = {'real_name': project_name, 'forks': forks}

# 4. Join relevant_projects with stats
final_projects = []
for proj in relevant_projects:
    p_lower = proj.lower()
    if p_lower in project_stats:
        final_projects.append({
            'ProjectName': project_stats[p_lower]['real_name'],
            'Forks': project_stats[p_lower]['forks']
        })
    else:
        # Fallback: maybe the name in info was parsed differently?
        # Or maybe info is missing for this project?
        # If missing, forks=0 or ignore? The prompt implies we should find the highest forks.
        # If we can't find stats, we can't count it.
        pass

# 5. Sort and top 5
df = pd.DataFrame(final_projects)
if not df.empty:
    df = df.sort_values(by='Forks', ascending=False)
    top_5 = df.head(5)['ProjectName'].tolist()
else:
    top_5 = []

print('__RESULT__:')
print(json.dumps(top_5))"""

env_args = {'var_function-call-6485848890492900329': ['packageinfo'], 'var_function-call-6485848890492900454': ['project_info', 'project_packageversion'], 'var_function-call-474351073472527354': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-17329601053264025037': [{'count_star()': '770'}], 'var_function-call-15234202801282220009': [{'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Licenses': '[\n  "EUPL-1.2"\n]'}, {'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Licenses': '[]'}, {'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Licenses': '[]'}, {'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'Licenses': '[\n  "ISC"\n]'}, {'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Licenses': '[\n  "MIT"\n]'}], 'var_function-call-3894250662162695542': [{'COUNT(*)': '661372'}], 'var_function-call-543603203718078934': [{'COUNT(*)': '176170'}], 'var_function-call-13912716373860961398': [{'count_star()': '597602'}], 'var_function-call-4091625522379036388': 'file_storage/function-call-4091625522379036388.json', 'var_function-call-4091625522379036045': 'file_storage/function-call-4091625522379036045.json', 'var_function-call-4091625522379035702': 'file_storage/function-call-4091625522379035702.json'}

exec(code, env_args)

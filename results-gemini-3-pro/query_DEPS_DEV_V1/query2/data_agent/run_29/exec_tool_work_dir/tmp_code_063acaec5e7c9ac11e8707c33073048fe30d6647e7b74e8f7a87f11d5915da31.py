code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-4091625522379036388']) as f:
    package_rows = json.load(f)
with open(locals()['var_function-call-4091625522379036045']) as f:
    mapping_rows = json.load(f)
with open(locals()['var_function-call-4091625522379035702']) as f:
    info_rows = json.load(f)

# 1. Valid pkgs (Name, Version)
valid_pkg_keys = set()
for r in package_rows:
    valid_pkg_keys.add((r['Name'], r['Version']))

# 2. Relevant projects
relevant_projects = set()
for r in mapping_rows:
    if (r['Name'], r['Version']) in valid_pkg_keys:
        relevant_projects.add(r['ProjectName'])

# 3. Parse info
project_stats = {}
fork_patterns = [
    r'(\d+)\s+forks?',
    r'forks? count of (\d+)',
    r'forked (\d+) times',
    r'forks?: (\d+)'
]

# Simple regex: characters that make up a repo name, with a slash in middle.
# No boundaries, just find the pattern.
name_pat = r'[a-zA-Z0-9\-\.]+\/[a-zA-Z0-9\-\.]+'

for row in info_rows:
    text = row['Project_Information']
    if not text:
        continue
        
    # Extract Forks
    forks = 0
    for pat in fork_patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            try:
                forks = int(m.group(1).replace(',', ''))
                break
            except:
                pass
    
    # Extract Name
    candidates = re.findall(name_pat, text)
    project_name = None
    for cand in candidates:
        # Filter unwanted
        # Check if it looks like a url part (e.g. part of http://...)
        # If the text has "http://github.com/owner/repo", the regex might catch "github.com/owner" or "owner/repo" depending on implementation.
        # But here the regex [chars]/[chars] will match "github.com/owner".
        # We want to skip "github.com/..."
        if 'github.com' in cand: continue
        if cand.lower() in ['github/project', 'github/repository', 'project/name', 'github/com']: continue
        
        project_name = cand
        break
    
    if project_name:
        project_stats[project_name.lower()] = {'real_name': project_name, 'forks': forks}

# 4. Join
final_list = []
for proj in relevant_projects:
    p_lower = proj.lower()
    if p_lower in project_stats:
        final_list.append({
            'ProjectName': project_stats[p_lower]['real_name'],
            'Forks': project_stats[p_lower]['forks']
        })

# 5. Sort
df = pd.DataFrame(final_list)
if not df.empty:
    df = df.sort_values(by='Forks', ascending=False)
    result = df.head(5)['ProjectName'].tolist()
else:
    result = []

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-6485848890492900329': ['packageinfo'], 'var_function-call-6485848890492900454': ['project_info', 'project_packageversion'], 'var_function-call-474351073472527354': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-17329601053264025037': [{'count_star()': '770'}], 'var_function-call-15234202801282220009': [{'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Licenses': '[\n  "EUPL-1.2"\n]'}, {'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Licenses': '[]'}, {'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Licenses': '[]'}, {'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'Licenses': '[\n  "ISC"\n]'}, {'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Licenses': '[\n  "MIT"\n]'}], 'var_function-call-3894250662162695542': [{'COUNT(*)': '661372'}], 'var_function-call-543603203718078934': [{'COUNT(*)': '176170'}], 'var_function-call-13912716373860961398': [{'count_star()': '597602'}], 'var_function-call-4091625522379036388': 'file_storage/function-call-4091625522379036388.json', 'var_function-call-4091625522379036045': 'file_storage/function-call-4091625522379036045.json', 'var_function-call-4091625522379035702': 'file_storage/function-call-4091625522379035702.json', 'var_function-call-12052291588044334746': [], 'var_function-call-809749469135880200': 'done', 'var_function-call-4428019070161265216': {'valid_pkgs_count': 84744, 'relevant_projects_count': 5430, 'sample_relevant': ['goosedefi/goose-uikit', 'rackt/async-props', 'floatdrop/pinkie', 'dotnetautor/easm', 'dominictarr/crypto-browserify'], 'project_stats_count': 0, 'sample_stats_keys': [], 'sample_parse': [], 'overlap_count': 0}, 'var_function-call-2928250688251336945': 'debug done', 'var_function-call-11631268150816156068': {'rows_count': 770, 'example_text': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'simple_matches': ['lberrocal/npm-packages-template'], 'complex_matches': []}, 'var_function-call-18071086887894786939': [], 'var_function-call-1195652897400837475': {'relevant_projects_sample': ['foregon/cobalto', 'julliandev/dynablox_opencloud', 'abuinitski/redux-bundler-async-resources', 'jqestate/eslint-config-dtrussia', 'sindresorhus/pify', 'blakeembrey/pluralize', 'edge-hub/router', 'ledgerproject/keypairoom', 'sindresorhus/loud-rejection', 'dschewchenko/nativescript-svg'], 'parsed_projects_sample': [], 'intersection_count': 0, 'intersection_sample': []}}

exec(code, env_args)

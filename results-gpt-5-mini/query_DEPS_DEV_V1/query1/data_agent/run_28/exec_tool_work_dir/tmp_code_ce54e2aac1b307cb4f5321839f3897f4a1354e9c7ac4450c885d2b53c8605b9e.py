code = """import json, re

# Load data from storage file paths
with open(var_call_Y7acS5lO8NnWSMMwK9Jyy7Co, 'r') as f:
    latest_packages = json.load(f)
with open(var_call_sUMbI0eo4YS5PbWUNOOt5Otz, 'r') as f:
    project_pkgvers = json.load(f)
with open(var_call_fMMs46CLMF7tQ6AJirJdA37M, 'r') as f:
    project_info = json.load(f)

# Build lookup for package keys (Name, Version)
pkg_keys = set((p['Name'], p['Version']) for p in latest_packages if p.get('System') == 'NPM')

# Map package (Name,Version) -> set of ProjectName(s)
pkg_to_projects = {}
for row in project_pkgvers:
    if row.get('System') != 'NPM':
        continue
    key = (row.get('Name'), row.get('Version'))
    if key in pkg_keys:
        pkg_to_projects.setdefault(key, set()).add(row.get('ProjectName'))

# Extract repo -> stars from project_info
repo_to_stars = {}

# Patterns to find stars
star_patterns = [
    r"([\d,]+)\s+stars",
    r"a total of\s+([\d,]+)\s+stars",
    r"stars\s+count\s+of\s+([\d,]+)",
    r"stars\s*:\s*([\d,]+)",
    r"has garnered a total of\s+([\d,]+)\s+stars",
    r"has\s+a\s+stars\s+count\s+of\s+([\d,]+)",
]

# Repo pattern
repo_pattern = re.compile(r"([A-Za-z0-9_.\-]+\/[A-Za-z0-9_.\-]+)")

for rec in project_info:
    info = rec.get('Project_Information')
    if not info:
        continue
    # find first repo-like token
    repo_match = repo_pattern.search(info)
    if not repo_match:
        continue
    repo = repo_match.group(1)
    # find stars
    stars = None
    for pat in star_patterns:
        m = re.search(pat, info)
        if m:
            try:
                stars = int(m.group(1).replace(',', ''))
            except:
                stars = None
            break
    # Additional fallback: look for patterns like 'has X open issues, Y stars, and Z forks' capture the middle number
    if stars is None:
        m = re.search(r"open issues[,\s\w]*?([\d,]+)\s+stars", info)
        if m:
            try:
                stars = int(m.group(1).replace(',', ''))
            except:
                stars = None
    if stars is None:
        # try any number followed by 'stars' later
        m = re.search(r"([\d,]+)\s+star[s]?", info)
        if m:
            try:
                stars = int(m.group(1).replace(',', ''))
            except:
                stars = None
    if stars is not None:
        # keep maximum if multiple entries
        if repo in repo_to_stars:
            repo_to_stars[repo] = max(repo_to_stars[repo], stars)
        else:
            repo_to_stars[repo] = stars

# For each package, determine its max stars among associated projects
pkg_list = []
for key in pkg_keys:
    projects = pkg_to_projects.get(key, None)
    if not projects:
        continue
    max_stars = None
    matched_repos = []
    for proj in projects:
        if proj in repo_to_stars:
            matched_repos.append((proj, repo_to_stars[proj]))
            if max_stars is None or repo_to_stars[proj] > max_stars:
                max_stars = repo_to_stars[proj]
    if max_stars is not None:
        pkg_list.append({
            'Name': key[0],
            'Version': key[1],
            'Stars': max_stars,
            'Projects': [p for p,s in matched_repos]
        })

# Sort and take top 5 by Stars
pkg_list_sorted = sorted(pkg_list, key=lambda x: x['Stars'], reverse=True)
top5 = pkg_list_sorted[:5]

# Prepare output
output = top5

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_Y7acS5lO8NnWSMMwK9Jyy7Co': 'file_storage/call_Y7acS5lO8NnWSMMwK9Jyy7Co.json', 'var_call_sUMbI0eo4YS5PbWUNOOt5Otz': 'file_storage/call_sUMbI0eo4YS5PbWUNOOt5Otz.json', 'var_call_fMMs46CLMF7tQ6AJirJdA37M': 'file_storage/call_fMMs46CLMF7tQ6AJirJdA37M.json'}

exec(code, env_args)

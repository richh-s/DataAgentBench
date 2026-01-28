code = """import json, re
# Load data from storage-provided file paths
with open(var_call_HKZlEGpTjMfm6bAchrBQloNX, 'r') as f:
    pkg_records = json.load(f)
with open(var_call_GSjHKQZXIywhAk487Tu3AWDE, 'r') as f:
    ppv_records = json.load(f)
with open(var_call_sprPoE6cEh4bFhgHsLMK4QDS, 'r') as f:
    projinfo_records = json.load(f)

# Create lookup for project_info entries
# We'll store list of entries for quick search
projinfo_list = projinfo_records

# Index project_info entries by lowercased Project_Information for searching
# But we'll just iterate

# Merge package records with project_packageversion on Name and Version
pkg_set = set((r['Name'], r['Version']) for r in pkg_records)

# Filter ppv_records where Name, Version match and System == 'NPM'
matched_projects = set()
for r in ppv_records:
    if r.get('System') == 'NPM' and (r.get('Name'), r.get('Version')) in pkg_set:
        if r.get('ProjectName'):
            matched_projects.add(r.get('ProjectName'))

matched_projects = sorted(matched_projects)

# For each matched project, find project_info rows containing that project name and with MIT license
results = []

# regex patterns to extract fork counts
patterns = [r'([0-9][0-9,]*)\s*(?:forks|fork)\b', r'forked\s*([0-9][0-9,]*)', r'forks count of\s*([0-9][0-9,]*)', r'forks count.*?(\d[0-9,]*)']

for proj in matched_projects:
    best_forks = None
    best_info = None
    for info in projinfo_list:
        pi = info.get('Project_Information') or ''
        lic = info.get('Licenses') or ''
        if proj in pi and 'MIT' in lic:
            # try to extract fork count
            forks = None
            for pat in patterns:
                m = re.search(pat, pi, flags=re.IGNORECASE)
                if m:
                    try:
                        forks = int(m.group(1).replace(',', ''))
                        break
                    except:
                        continue
            if forks is None:
                # try to find all numbers and take the one near 'fork'
                # fallback: find last number in string
                nums = re.findall(r'(\d[0-9,]*)', pi)
                if nums:
                    forks = int(nums[-1].replace(',', ''))
            if forks is not None:
                if best_forks is None or forks > best_forks:
                    best_forks = forks
                    best_info = pi
    if best_forks is not None:
        results.append({'ProjectName': proj, 'Forks': best_forks, 'Project_Information': best_info})

# Sort results by Forks desc and take top 5
results_sorted = sorted(results, key=lambda x: x['Forks'], reverse=True)[:5]

# Prepare JSON-serializable output
output = results_sorted

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_HKZlEGpTjMfm6bAchrBQloNX': 'file_storage/call_HKZlEGpTjMfm6bAchrBQloNX.json', 'var_call_GSjHKQZXIywhAk487Tu3AWDE': 'file_storage/call_GSjHKQZXIywhAk487Tu3AWDE.json', 'var_call_sprPoE6cEh4bFhgHsLMK4QDS': 'file_storage/call_sprPoE6cEh4bFhgHsLMK4QDS.json'}

exec(code, env_args)

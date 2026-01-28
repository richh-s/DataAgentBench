code = """import json, re

# Load project names (list) and project_info records
with open(var_call_kZjiw49rRA1EtP0O5lTo2FtZ, 'r') as f:
    project_names = json.load(f)
with open(var_call_6PqHednemVscPZYBx7CgK1Yq, 'r') as f:
    projinfo = json.load(f)

# Normalize project_names to set for faster lookup
proj_set = set(project_names)

# Build a mapping from project_name -> forks
results = {}

# Precompile regexes
regexes = [re.compile(r'([0-9][0-9,]*)\s+forks', re.IGNORECASE),
           re.compile(r'forks count of\s*([0-9,]+)', re.IGNORECASE),
           re.compile(r'been forked\s*([0-9,]+)\s*times', re.IGNORECASE),
           re.compile(r'and\s*([0-9][0-9,]*)\s*forks', re.IGNORECASE)]

# For each project_info record, try to detect the project_name and forks
for rec in projinfo:
    pi = rec.get('Project_Information') or ''
    lic = rec.get('Licenses') or ''
    # Only consider project_info entries that indicate MIT license
    if 'MIT' not in lic:
        continue
    # Try to find any project_name present in this Project_Information
    # Iterate over proj_set but to speed up, check tokens in pi
    # We'll check all project_names; if very large this may be slow but acceptable here
    for pname in proj_set:
        if pname in pi:
            # Try regexes to extract forks
            forks = None
            for rg in regexes:
                m = rg.search(pi)
                if m:
                    try:
                        forks = int(m.group(1).replace(',',''))
                        break
                    except:
                        continue
            if forks is None:
                # Try generic search for "stars, and X forks" pattern
                m = re.search(r'stars[,\s]*and[,\s]*([0-9][0-9,]*)\s*forks', pi, re.IGNORECASE)
                if m:
                    forks = int(m.group(1).replace(',',''))
            if forks is None:
                # Try pattern like 'has been forked 12 times' alternative
                m = re.search(r'forked\s*([0-9,]+)', pi, re.IGNORECASE)
                if m:
                    forks = int(m.group(1).replace(',',''))
            if forks is not None:
                # Keep the maximum if multiple entries map to same project
                prev = results.get(pname)
                if prev is None or forks > prev:
                    results[pname] = forks
            # Once matched, don't try matching other project_names in same pi to avoid duplicates
            # but some Project_Information might include multiple repos; we'll continue

# Now filter results to only those projects that were in the original project_names list
final_list = [{'project': k, 'forks': v} for k,v in results.items()]
# Sort by forks desc
final_list.sort(key=lambda x: x['forks'], reverse=True)
# Take top 5
top5 = final_list[:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_rNmnhECaaLnU0NkbPqzziZpa': 'file_storage/call_rNmnhECaaLnU0NkbPqzziZpa.json', 'var_call_VYsnH3VHoutas1uQRAJH0NED': 'file_storage/call_VYsnH3VHoutas1uQRAJH0NED.json', 'var_call_XXsSx4B5pKCeNjXQ88rDo9OT': 'file_storage/call_XXsSx4B5pKCeNjXQ88rDo9OT.json', 'var_call_kZjiw49rRA1EtP0O5lTo2FtZ': 'file_storage/call_kZjiw49rRA1EtP0O5lTo2FtZ.json', 'var_call_6PqHednemVscPZYBx7CgK1Yq': 'file_storage/call_6PqHednemVscPZYBx7CgK1Yq.json'}

exec(code, env_args)

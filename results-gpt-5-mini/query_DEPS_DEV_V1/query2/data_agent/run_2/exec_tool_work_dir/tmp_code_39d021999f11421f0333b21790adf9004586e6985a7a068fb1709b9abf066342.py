code = """import json, re

# Load data files created by previous tool calls
with open(var_call_ysJS0k7S8uOWRnHAFwKZT3Nt, 'r') as f:
    pkgs = json.load(f)
with open(var_call_h0brtFIisYruRnVV3XIjjHOm, 'r') as f:
    ppv = json.load(f)
with open(var_call_yuOtWjhwXoYOee2g9qoXC9Wd, 'r') as f:
    pinfo = json.load(f)

# Build set of package tuples (System, Name, Version) from packageinfo (already filtered for NPM, MIT, IsRelease)
pkg_tuples = set()
for rec in pkgs:
    s = rec.get('System')
    n = rec.get('Name')
    v = rec.get('Version')
    if s and n and v:
        pkg_tuples.add((s, n, v))

# Map matched package tuples to project names via project_packageversion
project_names = set()
for rec in ppv:
    key = (rec.get('System'), rec.get('Name'), rec.get('Version'))
    if key in pkg_tuples:
        pn = rec.get('ProjectName')
        if pn:
            project_names.add(pn)

# Helper to extract fork count from a Project_Information string
def extract_forks(text):
    if not text:
        return None
    # Try pattern 'forks count of <num>'
    m = re.search(r'forks count of\s*([0-9][0-9,]*)', text, re.I)
    if m:
        return int(m.group(1).replace(',', ''))
    # Try pattern '<num> forks' or '<num> forked'
    m2 = re.search(r'([0-9][0-9,]*)\s*(?:forks|forked)\b', text, re.I)
    if m2:
        return int(m2.group(1).replace(',', ''))
    # Try pattern 'been forked <num> times'
    m3 = re.search(r'been\s+forked\s+([0-9][0-9,]*)', text, re.I)
    if m3:
        return int(m3.group(1).replace(',', ''))
    return None

# Build mapping from project_info Project_Information to forks
# For faster lookup, we'll check for presence of project_name in Project_Information
project_forks = {}
for pn in project_names:
    max_forks = None
    for rec in pinfo:
        info = rec.get('Project_Information') or ''
        # Simple substring match of owner/repo
        if pn in info:
            forks = extract_forks(info)
            if forks is not None:
                if (max_forks is None) or (forks > max_forks):
                    max_forks = forks
    if max_forks is not None:
        project_forks[pn] = max_forks

# Prepare sorted top 5 by forks
items = sorted(project_forks.items(), key=lambda x: x[1], reverse=True)
top5 = [{'ProjectName': k, 'Forks': v} for k, v in items[:5]]

# Output result as JSON string
print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_ysJS0k7S8uOWRnHAFwKZT3Nt': 'file_storage/call_ysJS0k7S8uOWRnHAFwKZT3Nt.json', 'var_call_hnxDF6mton5qJUP5QftKPIfJ': 'file_storage/call_hnxDF6mton5qJUP5QftKPIfJ.json', 'var_call_aEWOXWjwDpSKHVEWuog5gFxU': ['project_info', 'project_packageversion'], 'var_call_h0brtFIisYruRnVV3XIjjHOm': 'file_storage/call_h0brtFIisYruRnVV3XIjjHOm.json', 'var_call_yuOtWjhwXoYOee2g9qoXC9Wd': 'file_storage/call_yuOtWjhwXoYOee2g9qoXC9Wd.json'}

exec(code, env_args)

code = """import json
# load intermediate unique_projects
fp_unique = var_call_RvxZemrM7Zy6YgWKjluTo5QN
fp_projinfo = var_call_x1IMOYdf6h3JXSJiZRuUt4FV
with open(fp_unique, 'r', encoding='utf-8') as f:
    unique_projects = json.load(f)
with open(fp_projinfo, 'r', encoding='utf-8') as f:
    projinfo = json.load(f)
# Build mapping from ProjectName to Project_Information and Licenses
projname_to_info = {}
for r in projinfo:
    pi = r.get('Project_Information')
    lic = r.get('Licenses')
    # Try to extract repo path from Project_Information: it starts with 'The project <owner/repo>' or 'The GitHub project <owner/repo>' or 'The project <owner/repo> on GitHub'
    # We'll search for patterns like 'project ' followed by something like owner/repo
    # Also sometimes the string may contain many words; we'll store by repo if we can find owner/repo, else store full info under None
    import re
    m = re.search(r'project\s+([A-Za-z0-9_.\-]+\/[A-Za-z0-9_.\-]+)', pi)
    if not m:
        m = re.search(r'GitHub project\s+([A-Za-z0-9_.\-]+\/[A-Za-z0-9_.\-]+)', pi)
    key = m.group(1) if m else None
    if key:
        projname_to_info[key] = {'Project_Information': pi, 'Licenses': lic}
# Now, for each unique project, find matching project info by exact match of ProjectName
matched = []
for up in unique_projects:
    pn = up['ProjectName']
    info = projname_to_info.get(pn)
    if info:
        matched.append({'ProjectName': pn, 'Name': up['Name'], 'Version': up['Version'], 'Project_Information': info['Project_Information'], 'Licenses': info['Licenses']})
# For matched entries, extract forks count by regex
results = []
import re
for r in matched:
    pi = r['Project_Information']
    m = re.search(r'([0-9,]+)\s+forks', pi)
    if not m:
        m = re.search(r'forks\s+count\s+of\s+([0-9,]+)', pi)
    if not m:
        # sometimes 'and 5782 forks' pattern
        m = re.search(r'and\s+([0-9,]+)\s+forks', pi)
    forks = int(m.group(1).replace(',', '')) if m else None
    # Parse Licenses JSON-like
    lic = r['Licenses']
    try:
        lic_list = json.loads(lic)
    except Exception:
        lic_list = []
    results.append({'ProjectName': r['ProjectName'], 'Forks': forks, 'Licenses': lic_list, 'Name': r['Name'], 'Version': r['Version']})
# Filter to MIT-licensed projects where Forks is not None
mit_projects = [r for r in results if any('MIT' in s for s in r['Licenses']) and r['Forks'] is not None]
# Sort by Forks desc and take top 5
mit_projects_sorted = sorted(mit_projects, key=lambda x: x['Forks'], reverse=True)[:5]
print('__RESULT__:')
print(json.dumps(mit_projects_sorted))"""

env_args = {'var_call_OEReunzHmE74cZY4WNSIkfET': ['packageinfo'], 'var_call_o5zSgoYFYlDqAiCwnnXLwH5B': ['project_info', 'project_packageversion'], 'var_call_sYGEyX5JrMt2dOgtF3WlNf4f': 'file_storage/call_sYGEyX5JrMt2dOgtF3WlNf4f.json', 'var_call_6wivde3LLZKivV7PoIz7h2oI': 'file_storage/call_6wivde3LLZKivV7PoIz7h2oI.json', 'var_call_hOu0eUEw9QMltxlq4dHpjw1h': 'file_storage/call_hOu0eUEw9QMltxlq4dHpjw1h.json', 'var_call_RvxZemrM7Zy6YgWKjluTo5QN': 'file_storage/call_RvxZemrM7Zy6YgWKjluTo5QN.json', 'var_call_x1IMOYdf6h3JXSJiZRuUt4FV': 'file_storage/call_x1IMOYdf6h3JXSJiZRuUt4FV.json'}

exec(code, env_args)

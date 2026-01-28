code = """import json
path = var_call_EkXd752NRanRt05GIewLqfZS
with open(path, 'r') as f:
    proj_info = json.load(f)
# We need to extract project repo path and fork counts from Project_Information text.
# The text seems like: 'The project owner/repo on GitHub ... has X open issues, Y stars, and Z forks.'
import re
records = []
pattern = re.compile(r"project\s+([\w\-\.]+/[\w\-\.]+).*?has\s+(\d+[\d,]*)\s+open issues,\s+(\d+[\d,]*)\s+stars?,\s+and\s+(\d+[\d,]*)\s+forks", re.IGNORECASE)
for r in proj_info:
    text = r.get('Project_Information','')
    m = pattern.search(text)
    if m:
        repo = m.group(1)
        open_issues = int(m.group(2).replace(',',''))
        stars = int(m.group(3).replace(',',''))
        forks = int(m.group(4).replace(',',''))
        records.append({'repo': repo, 'open_issues': open_issues, 'stars': stars, 'forks': forks, 'text': text})
# Also some lines have different phrasing; try another pattern
pattern2 = re.compile(r"The project (?:is hosted on GitHub under the name|on GitHub, named)\s+([\w\-\.]+/[\w\-\.]+).*?has\s+(\d+[\d,]*)\s+stars?\s+and\s+been forked\s+(\d+[\d,]*)\s+times", re.IGNORECASE)
for r in proj_info:
    text = r.get('Project_Information','')
    m = pattern2.search(text)
    if m:
        repo = m.group(1)
        stars = int(m.group(2).replace(',',''))
        forks = int(m.group(3).replace(',',''))
        records.append({'repo': repo, 'open_issues': None, 'stars': stars, 'forks': forks, 'text': text})
# Deduplicate by repo keeping max forks
d = {}
for rec in records:
    repo = rec['repo']
    if repo not in d or (rec['forks'] is not None and (d[repo].get('forks') is None or rec['forks']>d[repo]['forks'])):
        d[repo]=rec
# Build list sorted by forks desc
lst = list(d.values())
lst_sorted = sorted(lst, key=lambda x: (x['forks'] if x['forks'] is not None else -1), reverse=True)
# take top 20 for inspection
top20 = lst_sorted[:20]
print('__RESULT__:')
print(json.dumps({'total_extracted': len(lst), 'top20': top20}, default=str))"""

env_args = {'var_call_DVz30QS38OPrjRQdXuHLEkI5': ['packageinfo'], 'var_call_ADQ91SZxih62Z859qz1fgKUp': ['project_info', 'project_packageversion'], 'var_call_oy7rkcqUhosdoleV1S5dixVk': 'file_storage/call_oy7rkcqUhosdoleV1S5dixVk.json', 'var_call_S7VM1YWlDVqhFnG8TysEIgvV': {'num_rows': 176998, 'unique_names': 10486, 'unique_pairs': 85158}, 'var_call_I9REvBUjaV8FcUHZHINzvScE': 'file_storage/call_I9REvBUjaV8FcUHZHINzvScE.json', 'var_call_wVNb1WzE2pfGjziOg9zRdVXT': {'total_rows': 591699, 'unique_mappings': 321836}, 'var_call_EkXd752NRanRt05GIewLqfZS': 'file_storage/call_EkXd752NRanRt05GIewLqfZS.json'}

exec(code, env_args)

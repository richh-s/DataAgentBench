code = """import json, pandas as pd

res = var_call_aceBuxNJuGvxAOKEvO96S8RZ
# dedupe by package Name
if isinstance(res, str) and res.endswith('.json'):
    with open(res,'r',encoding='utf-8') as f:
        res=json.load(f)

df=pd.DataFrame(res)
df=df.drop_duplicates(subset=['Name','Version','Repo','Stars'])
# still may have same logical package names due to dependency path; take unique by Repo or by exact Name.
df=df.sort_values('Stars', ascending=False)
# keep unique by Repo first, then Name
seen=set(); rows=[]
for r in df.to_dict('records'):
    key=r['Repo']
    if key in seen: continue
    seen.add(key)
    rows.append(r)
# if fewer than 5, keep adding by Name unique
if len(rows)<5:
    seen_names=set([r['Name'] for r in rows])
    for r in df.to_dict('records'):
        if r['Name'] in seen_names: continue
        seen_names.add(r['Name'])
        rows.append(r)
        if len(rows)>=5: break

print('__RESULT__:')
print(json.dumps(rows))"""

env_args = {'var_call_LajdCAPb2uSJ0SAz2kAU0WNQ': 'file_storage/call_LajdCAPb2uSJ0SAz2kAU0WNQ.json', 'var_call_1wT6UAnDXOxcDNXdx6YiPsiG': 'file_storage/call_1wT6UAnDXOxcDNXdx6YiPsiG.json', 'var_call_KKvwj99qU3IZ0eecUYNC9Fr4': ['project_info', 'project_packageversion'], 'var_call_xrPfzgfEouypZYLKHF9PnS3g': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_call_vIQvk5bGQo5Ph1wraClQmUfy': 'file_storage/call_vIQvk5bGQo5Ph1wraClQmUfy.json', 'var_call_aceBuxNJuGvxAOKEvO96S8RZ': [{'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Repo': 'microsoft/typescript', 'Stars': 94931.0}, {'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Repo': 'microsoft/typescript', 'Stars': 94931.0}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Repo': 'microsoft/typescript', 'Stars': 94931.0}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Repo': 'microsoft/typescript', 'Stars': 94931.0}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Repo': 'sveltejs/svelte', 'Stars': 73499.0}]}

exec(code, env_args)

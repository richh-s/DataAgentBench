code = """import json

# projects
proj = var_call_EBZxEfxahspyUW0fpvomYJBj
if isinstance(proj, str):
    proj = json.loads(proj)
projects = proj['spring_2022_projects']

# funding totals per project
raw = var_call_xDRMasDvk3erhtu6bJ1vyy9L
if isinstance(raw, str):
    with open(raw, 'r', encoding='utf-8') as f:
        funding_rows = json.load(f)
else:
    funding_rows = raw
funding_map = {r['Project_Name']: int(r['Total_Amount']) for r in funding_rows}

total = sum(funding_map.get(p, 0) for p in projects)
missing = [p for p in projects if p not in funding_map]

print('__RESULT__:')
print(json.dumps({"count": len(projects), "total_funding": total, "projects": projects, "missing_funding_projects": missing}))"""

env_args = {'var_call_WF7nOmUatVD8vw8PJCkI3sVH': ['Funding'], 'var_call_wRmXiS5fuWvTjHJBViejlb7C': ['civic_docs'], 'var_call_RU0Eeenz3jeZ4nl37lbeV0m4': 'file_storage/call_RU0Eeenz3jeZ4nl37lbeV0m4.json', 'var_call_hfv6gVDdrgKpYyCiZVl8LQPr': 'file_storage/call_hfv6gVDdrgKpYyCiZVl8LQPr.json', 'var_call_HWhFLWT6n0CRM4VBlAo3cr4K': {'spring_2022_projects': ['Fire.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'advertised for construction bids shortly after this date.', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.'], 'count': 14}, 'var_call_EBZxEfxahspyUW0fpvomYJBj': {'spring_2022_projects': ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)'], 'count': 2}, 'var_call_xDRMasDvk3erhtu6bJ1vyy9L': 'file_storage/call_xDRMasDvk3erhtu6bJ1vyy9L.json'}

exec(code, env_args)

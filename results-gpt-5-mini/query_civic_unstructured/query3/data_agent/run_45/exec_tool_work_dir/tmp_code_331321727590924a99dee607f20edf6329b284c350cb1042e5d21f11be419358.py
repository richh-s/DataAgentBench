code = """import json
path = var_call_ndCXcgESAlmHDXPVtl7NyB5w
with open(path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize funding amounts to integers and filter for FEMA or emergency-related project names
results = []
for r in funding:
    name = r.get('Project_Name','')
    src = r.get('Funding_Source','')
    amt = r.get('Amount', None)
    try:
        amt_int = int(amt)
    except:
        try:
            amt_int = int(float(amt))
        except:
            amt_int = None
    # match project names containing FEMA or Outdoor Warning (emergency) or Emergency
    if 'fema' in name.lower() or 'outdoor warning' in name.lower() or 'emergency' in name.lower():
        results.append({'Project_Name': name, 'Funding_Source': src, 'Amount': amt_int})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_uqzI9WhyYiig4Zo5laqd7bQk': ['civic_docs'], 'var_call_KVKlIYloVTvXJ6fo0ZGDdXai': ['Funding'], 'var_call_tbBFwe7x7VueL51tEf2jx0fE': 'file_storage/call_tbBFwe7x7VueL51tEf2jx0fE.json', 'var_call_nddO8DIJpuAGL7UXnLHEA9Ay': [{'Project_Name': '', 'status': 'not started', 'topics': ['FEMA']}, {'Project_Name': 'Begin Construction: Spring 2022', 'status': 'design', 'topics': ['FEMA', 'highway']}, {'Project_Name': 'Staff is finalizing the design of this project.', 'status': 'design', 'topics': ['FEMA', 'park']}, {'Project_Name': 'Begin Construction: April 2022', 'status': 'design', 'topics': ['FEMA', 'park']}, {'Project_Name': 'Agenda Item # 4.A.', 'status': 'not started', 'topics': ['FEMA']}, {'Project_Name': 'Completion Date: Spring 2022', 'status': 'not started', 'topics': ['FEMA', 'road', 'fire', 'bridge', 'guardrail']}, {'Project_Name': 'Project Description: This project consisted of replacing the damag', 'status': 'not started', 'topics': ['FEMA', 'road', 'fire', 'bridge', 'guardrail']}, {'Project_Name': 'fencing and repairing the damaged embankment adjacent to the bridge.', 'status': 'not started', 'topics': ['FEMA', 'bridge']}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'status': 'not started', 'topics': ['FEMA', 'park', 'drainage', 'drain']}, {'Project_Name': 'Avenue. This project is scheduled to be accepted by the Council at th', 'status': 'design', 'topics': ['FEMA', 'road', 'storm drain', 'drain']}, {'Project_Name': 'project. Proposals will be due in February/March.', 'status': 'not started', 'topics': ['FEMA', 'road', 'fire', 'storm drain', 'drain']}, {'Project_Name': 'Begin Construction: Fall 2022', 'status': 'design', 'topics': ['FEMA', 'park']}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'status': 'design', 'topics': ['emergency', 'emergency warning', 'warning']}, {'Project_Name': 'environmental compliance needed for a shovel ready project. Phase Two of', 'status': 'design', 'topics': ['emergency', 'emergency warning', 'warning']}, {'Project_Name': 'Begin Construction: Summer 2021', 'status': 'design', 'topics': ['FEMA']}, {'Project_Name': 'Begin Construction: Summer/Fall 2021', 'status': 'design', 'topics': ['FEMA', 'park']}, {'Project_Name': 'Disaster Projects (Completed)', 'status': 'completed', 'topics': ['FEMA', 'road', 'fire', 'bridge', 'guardrail']}, {'Project_Name': 'Disaster Projects (Not Started)', 'status': 'design', 'topics': ['FEMA', 'road', 'storm drain', 'drain']}, {'Project_Name': 'Begin Construction: Summer 2022', 'status': 'design', 'topics': ['FEMA', 'road', 'fire', 'drainage', 'storm drain', 'drain']}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'status': 'design', 'topics': ['FEMA', 'fire', 'warning']}, {'Project_Name': 'Estimated Schedul', 'status': 'design', 'topics': ['FEMA']}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'status': 'design', 'topics': ['FEMA', 'fire', 'drainage', 'storm drain', 'warning', 'drain']}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'status': 'not started', 'topics': ['FEMA', 'fire', 'drainage', 'storm drain', 'drain']}, {'Project_Name': 'poor cell service. Phase One of the project included a sound study to', 'status': 'design', 'topics': ['FEMA']}, {'Project_Name': 'included the repair of a storm drainage facility on Birdview Avenue. The project w', 'status': 'not started', 'topics': ['FEMA', 'park', 'drainage', 'drain']}], 'var_call_ndCXcgESAlmHDXPVtl7NyB5w': 'file_storage/call_ndCXcgESAlmHDXPVtl7NyB5w.json'}

exec(code, env_args)

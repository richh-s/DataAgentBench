code = """import json
# var_call_nddO8DIJpuAGL7UXnLHEA9Ay is already a Python list stored in the environment; use it directly
projects = var_call_nddO8DIJpuAGL7UXnLHEA9Ay
funding = var_call_m6fJvlMHdrRs2zXuAL75LRHH

# Normalize names for matching
def norm(s):
    return ''.join(e for e in s.lower() if e.isalnum())

fund_map = {norm(r['Project_Name']): r for r in funding}

matches = []
for p in projects:
    pname = p.get('Project_Name','')
    npname = norm(pname)
    if npname in fund_map and pname.strip():
        f = fund_map[npname]
        matches.append({'Project_Name': pname, 'Funding_Source': f['Funding_Source'], 'Amount': f['Amount'], 'status': p.get('status')})
    else:
        for key, f in fund_map.items():
            if pname.strip() and npname and npname in key:
                matches.append({'Project_Name': pname, 'Funding_Source': f['Funding_Source'], 'Amount': f['Amount'], 'status': p.get('status')})
                break

# Deduplicate
seen = set()
uniq = []
for m in matches:
    key = (m['Project_Name'], m['Funding_Source'], m['Amount'])
    if key in seen:
        continue
    seen.add(key)
    uniq.append(m)

print('__RESULT__:')
print(json.dumps(uniq))"""

env_args = {'var_call_uqzI9WhyYiig4Zo5laqd7bQk': ['civic_docs'], 'var_call_KVKlIYloVTvXJ6fo0ZGDdXai': ['Funding'], 'var_call_tbBFwe7x7VueL51tEf2jx0fE': 'file_storage/call_tbBFwe7x7VueL51tEf2jx0fE.json', 'var_call_nddO8DIJpuAGL7UXnLHEA9Ay': [{'Project_Name': '', 'status': 'not started', 'topics': ['FEMA']}, {'Project_Name': 'Begin Construction: Spring 2022', 'status': 'design', 'topics': ['FEMA', 'highway']}, {'Project_Name': 'Staff is finalizing the design of this project.', 'status': 'design', 'topics': ['FEMA', 'park']}, {'Project_Name': 'Begin Construction: April 2022', 'status': 'design', 'topics': ['FEMA', 'park']}, {'Project_Name': 'Agenda Item # 4.A.', 'status': 'not started', 'topics': ['FEMA']}, {'Project_Name': 'Completion Date: Spring 2022', 'status': 'not started', 'topics': ['FEMA', 'road', 'fire', 'bridge', 'guardrail']}, {'Project_Name': 'Project Description: This project consisted of replacing the damag', 'status': 'not started', 'topics': ['FEMA', 'road', 'fire', 'bridge', 'guardrail']}, {'Project_Name': 'fencing and repairing the damaged embankment adjacent to the bridge.', 'status': 'not started', 'topics': ['FEMA', 'bridge']}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'status': 'not started', 'topics': ['FEMA', 'park', 'drainage', 'drain']}, {'Project_Name': 'Avenue. This project is scheduled to be accepted by the Council at th', 'status': 'design', 'topics': ['FEMA', 'road', 'storm drain', 'drain']}, {'Project_Name': 'project. Proposals will be due in February/March.', 'status': 'not started', 'topics': ['FEMA', 'road', 'fire', 'storm drain', 'drain']}, {'Project_Name': 'Begin Construction: Fall 2022', 'status': 'design', 'topics': ['FEMA', 'park']}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'status': 'design', 'topics': ['emergency', 'emergency warning', 'warning']}, {'Project_Name': 'environmental compliance needed for a shovel ready project. Phase Two of', 'status': 'design', 'topics': ['emergency', 'emergency warning', 'warning']}, {'Project_Name': 'Begin Construction: Summer 2021', 'status': 'design', 'topics': ['FEMA']}, {'Project_Name': 'Begin Construction: Summer/Fall 2021', 'status': 'design', 'topics': ['FEMA', 'park']}, {'Project_Name': 'Disaster Projects (Completed)', 'status': 'completed', 'topics': ['FEMA', 'road', 'fire', 'bridge', 'guardrail']}, {'Project_Name': 'Disaster Projects (Not Started)', 'status': 'design', 'topics': ['FEMA', 'road', 'storm drain', 'drain']}, {'Project_Name': 'Begin Construction: Summer 2022', 'status': 'design', 'topics': ['FEMA', 'road', 'fire', 'drainage', 'storm drain', 'drain']}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'status': 'design', 'topics': ['FEMA', 'fire', 'warning']}, {'Project_Name': 'Estimated Schedul', 'status': 'design', 'topics': ['FEMA']}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'status': 'design', 'topics': ['FEMA', 'fire', 'drainage', 'storm drain', 'warning', 'drain']}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'status': 'not started', 'topics': ['FEMA', 'fire', 'drainage', 'storm drain', 'drain']}, {'Project_Name': 'poor cell service. Phase One of the project included a sound study to', 'status': 'design', 'topics': ['FEMA']}, {'Project_Name': 'included the repair of a storm drainage facility on Birdview Avenue. The project w', 'status': 'not started', 'topics': ['FEMA', 'park', 'drainage', 'drain']}], 'var_call_ndCXcgESAlmHDXPVtl7NyB5w': 'file_storage/call_ndCXcgESAlmHDXPVtl7NyB5w.json', 'var_call_m6fJvlMHdrRs2zXuAL75LRHH': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000}, {'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': 92000}, {'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': 28000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000}]}

exec(code, env_args)

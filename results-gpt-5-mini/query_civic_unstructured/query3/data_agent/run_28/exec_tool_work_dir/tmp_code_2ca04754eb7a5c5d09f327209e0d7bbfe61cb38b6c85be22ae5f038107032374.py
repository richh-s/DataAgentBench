code = """import json
path = var_call_YK2GTFjaALiJRyaiqJp1v5Gu
with open(path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Filter funding records where project name contains 'fema' or 'outdoor warning' or 'guardrail' or 'Latigo' etc that we identified
keywords = ['fema','fema/','fema project','outdoor warning','sirens','guardrail','latigo','corral canyon','clover heights','trancas canyon','storm drain','culvert','bridge','birdview']
matches = []
for r in funding:
    name = r.get('Project_Name','')
    lname = name.lower()
    for k in keywords:
        if k in lname:
            matches.append({'Project_Name': name, 'Funding_Source': r.get('Funding_Source'), 'Amount': int(r.get('Amount')) if r.get('Amount') and str(r.get('Amount')).isdigit() else r.get('Amount')})
            break

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_call_QxtrsIHo3FAzElPyUC4rh1RS': 'file_storage/call_QxtrsIHo3FAzElPyUC4rh1RS.json', 'var_call_nk3UJd1gvwIdkU5NgDjoZ9tX': 'file_storage/call_nk3UJd1gvwIdkU5NgDjoZ9tX.json', 'var_call_f6c4OrX1ADPiRK3XZqSwT77I': ['Awaiting final FEMA/CalOES approval for scope modification', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Staff is also working with FEMA/CalOES to substitute the existing', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Project Description: This project will be funded through a grant from FEMA', 'drains, culverts, debris basins, manholes, and other drainage structures', 'Guardrail Replacement Citywide (FEMA Project)', 'guardrail throughout the City as a result of the Woolsey Fire.', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'fencing and repairing the damaged embankment adjacent to the bridge.', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Project Description: This project has been cancelled as it could not get FEMA', 'Clover Heights Storm Drain (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Project Description: This project consists of repairing the existing storm drain', 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Project Description: An Emergency Warning Siren system will improve the', 'the Emergency Warning Sirens project will be implementation of the design', 'awarded a FEMA Hazard Mitigation grant to fund the design, engineering and', 'plan, including purchasing, installing, and testing the sirens. The City will', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Outdoor Warning Sirens (FEMA)', 'Complete Design: Dependent upon final grant approval from FEMA', 'Outdoor Warning Sirens (FEMA Project)', 'Storm Drain Master Plan (FEMA Project)', 'infrastructure requirements, and siren sound range. The City has been', 'determine the optimal number and locations of individual sirens, power and', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES', 'Updates: This project will be funded through a grant from FEMA after the', 'bridge.', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Staff is working with FEMA/CalOES to substitute the existing timber', 'guardrails within the project limits.', 'Outdoor Warning Sirens - Design (FEMA Project)', 'Advertise: Fall 2023 (dependent upon FEMA/CalOES approval)', 'Project close out process has been initiated with FEMA/CalOES.', 'Advertise: Spring 2024 (dependent upon FEMA/CalOES approval)', 'Begin Construction: Summer 2024 (dependent upon FEMA/CalOES', 'Advertise: (dependent upon FEMA/CalOES approval)', 'Begin Construction: (dependent upon FEMA/CalOES approval)', 'Project Description: This project is funded through a grant from FEMA after'], 'var_call_iNpkxmKmPItNk2kCNqBKXSom': ['Funding'], 'var_call_YK2GTFjaALiJRyaiqJp1v5Gu': 'file_storage/call_YK2GTFjaALiJRyaiqJp1v5Gu.json'}

exec(code, env_args)

code = """import json
# Load results from storage variables provided by previous calls
funding = var_call_IUN6ZnkR4EPNOcvuokxuho4F
extracted = var_call_hdh8dhT6bQSyf4wQcG1ovh6v

# Normalize project names for matching
def norm(s):
    return s.strip().lower()

ex_names = {norm(p['Project_Name']): p.get('Status') for p in extracted}

# Merge: for each funding record, if its project matches an extracted project, include it
merged = []
matched_projects = set()
for f in funding:
    fn = norm(f['Project_Name'])
    if fn in ex_names:
        merged.append({
            'Project_Name': f['Project_Name'],
            'Funding_Source': f['Funding_Source'],
            'Amount': int(f['Amount']) if f.get('Amount') not in (None, '') else None,
            'Status': ex_names[fn]
        })
        matched_projects.add(fn)

# Also include extracted projects that had no funding records
for en, status in ex_names.items():
    if en not in matched_projects:
        # find original Project_Name text from extracted list
        original = next((p['Project_Name'] for p in extracted if norm(p['Project_Name'])==en), en)
        merged.append({
            'Project_Name': original,
            'Funding_Source': None,
            'Amount': None,
            'Status': status
        })

# Sort merged by Project_Name
merged = sorted(merged, key=lambda x: x['Project_Name'].lower())

print("__RESULT__:")
print(json.dumps(merged))"""

env_args = {'var_call_YgTnLjoJw69LVcdnv0lyQzQZ': 'file_storage/call_YgTnLjoJw69LVcdnv0lyQzQZ.json', 'var_call_hdh8dhT6bQSyf4wQcG1ovh6v': [{'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Status': 'completed'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Status': 'completed'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Status': 'design'}], 'var_call_IUN6ZnkR4EPNOcvuokxuho4F': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)

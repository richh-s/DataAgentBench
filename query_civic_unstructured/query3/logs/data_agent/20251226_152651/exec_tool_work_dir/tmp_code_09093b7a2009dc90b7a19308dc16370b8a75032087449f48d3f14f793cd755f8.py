code = """import json
import pandas as pd
with open(var_call_JaydfUjNRVLEEh5sWHcbhbcD, 'r') as f:
    civic_docs = json.load(f)
funding_records = var_call_N152nn5E54GDTTdb9f4Co8EW
relevant_projects = []
for doc in civic_docs:
    text = doc.get('text','').lower()
    if ('warning' in text) or ('emergency' in text) or ('fema' in text):
        lines = text.split("\n")
        for line in lines:
            if (('warning' in line) or ('fema' in line) or ('emergency' in line)) and (('project' in line) or ('sirens' in line)):
                relevant_projects.append(line)
fdf = pd.DataFrame(funding_records)
results = []
for idx, fund in fdf.iterrows():
    pname = fund['Project_Name'].lower()
    status = 'unknown'
    for ptext in relevant_projects:
        if pname.split('(')[0].strip()[:24] in ptext or ('warning' in ptext and 'sirens' in ptext):
            if 'design' in ptext:
                status = 'design'
            elif 'construction' in ptext:
                status = 'construction'
            elif 'completed' in ptext:
                status = 'completed'
            elif 'not started' in ptext:
                status = 'not started'
            elif 'repair' in ptext:
                status = 'repair'
            elif 'advertise' in ptext:
                status = 'advertising'
            elif 'preliminary' in ptext:
                status = 'preliminary design'
            break
    results.append({
        'Project_Name': fund['Project_Name'],
        'Funding_Source': fund['Funding_Source'],
        'Amount': fund['Amount'],
        'Status': status
    })
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_JaydfUjNRVLEEh5sWHcbhbcD': 'file_storage/call_JaydfUjNRVLEEh5sWHcbhbcD.json', 'var_call_N152nn5E54GDTTdb9f4Co8EW': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)

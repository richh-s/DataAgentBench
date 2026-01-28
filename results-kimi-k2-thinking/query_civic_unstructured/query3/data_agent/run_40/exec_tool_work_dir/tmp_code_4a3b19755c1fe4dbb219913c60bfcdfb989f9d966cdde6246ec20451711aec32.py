code = """import json, pandas as pd, re

# Load funding data
funding_file = locals()['var_functions.query_db:0']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:2']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

df_funding = pd.DataFrame(funding_data)

# Find projects with emergency/FEMA keywords
keywords = ['fema', 'emergency', 'warning']
emergency_funding = df_funding[df_funding['Project_Name'].str.contains('|'.join(keywords), case=False)]

results = []
for _, row in emergency_funding.iterrows():
    results.append({'Project_Name': row['Project_Name'], 'Funding_Source': row['Funding_Source'], 'Amount': int(row['Amount']), 'Status': 'Unknown'})

# Sort and output
results = sorted(results, key=lambda x: x['Project_Name'])

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000, 'Status': 'Unknown'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000, 'Status': 'Unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000, 'Status': 'Unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000, 'Status': 'Unknown'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000, 'Status': 'Unknown'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000, 'Status': 'Unknown'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000, 'Status': 'Unknown'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000, 'Status': 'Unknown'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000, 'Status': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000, 'Status': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000, 'Status': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000, 'Status': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000, 'Status': 'Unknown'}, {'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': 92000, 'Status': 'Unknown'}, {'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': 28000, 'Status': 'Unknown'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000, 'Status': 'Unknown'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000, 'Status': 'Unknown'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000, 'Status': 'Unknown'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000, 'Status': 'Unknown'}, {'Project_Name': 'PCH Overhead Warning Signs', 'Funding_Source': 'International Organization Grant', 'Amount': 73000, 'Status': 'Unknown'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000, 'Status': 'Unknown'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000, 'Status': 'Unknown'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000, 'Status': 'Unknown'}]}

exec(code, env_args)

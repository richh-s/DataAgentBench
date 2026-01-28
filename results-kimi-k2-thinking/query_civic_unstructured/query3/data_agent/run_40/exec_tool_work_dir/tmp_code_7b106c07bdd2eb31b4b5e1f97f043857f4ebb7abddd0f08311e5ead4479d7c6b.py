code = """import json
import pandas as pd
import re

# Load civic documents data
civic_file = locals()['var_functions.query_db:2']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_file = locals()['var_functions.query_db:0']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Create DataFrame for funding
df_funding = pd.DataFrame(funding_data)

# Define emergency/FEMA project names to look for
emergency_project_names = [
    'Birdview Avenue Improvements (FEMA/CalOES Project)',
    'Clover Heights Storm Drain (FEMA Project)',
    'Corral Canyon Culvert Repairs (FEMA Project)',
    'Corral Canyon Culvert Repairs (FEMA/CalOES Project)',
    'Corral Canyon Road Bridge Repairs (FEMA Project)',
    'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)',
    'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)',
    'Guardrail Replacement Citywide (FEMA Project)',
    'Guardrail Replacement Citywide (FEMA/CalOES Project)',
    'Latigo Canyon Road Culvert Repairs (FEMA Project)',
    'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)',
    'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)',
    'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)',
    'Outdoor Warning Signs',
    'Outdoor Warning Sirens',
    'Outdoor Warning Sirens (FEMA Project)',
    'Outdoor Warning Sirens (FEMA)',
    'Outdoor Warning Sirens - Design (FEMA Project)',
    'Outdoor Warningn Sirens - Design (FEMA Project)',
    'PCH Overhead Warning Signs',
    'Storm Drain Master Plan (FEMA Project)',
    'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)',
    'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)'
]

# Extract status information for these specific projects from civic documents
project_status = {}

for proj_name in emergency_project_names:
    proj_name_lower = proj_name.lower()
    
    for doc in civic_docs:
        text = doc.get('text', '')
        text_lower = text.lower()
        
        # Check if this document mentions the project
        if proj_name_lower in text_lower:
            # Extract status information
            status = 'Unknown'
            
            # Look for status indicators near the project name
            lines = text.split('\n')
            for i, line in enumerate(lines):
                line_lower = line.lower()
                if proj_name_lower in line_lower:
                    # Look at this line and next few lines for status
                    context = ' '.join(lines[i:min(i+5, len(lines))]).lower()
                    
                    # Determine status from keywords
                    if 'design' in context:
                        status = 'design'
                        break
                    elif any(word in context for word in ['construction', 'under construction', 'construct', 'bid']):
                        status = 'construction'
                        break
                    elif 'completed' in context:
                        status = 'completed'
                        break
                    elif 'not started' in context:
                        status = 'not started'
                        break
                    elif 'schedule' in context and 'advertise' in context:
                        status = 'design'
                        break
                        
            project_status[proj_name] = status

# Create final results with enhanced status information
results = []

for proj_name in emergency_project_names:
    # Find corresponding funding record
    matching_funds = df_funding[df_funding['Project_Name'].str.lower() == proj_name.lower()]
    
    if not matching_funds.empty:
        for _, fund in matching_funds.iterrows():
            status = project_status.get(proj_name, 'Unknown')
            
            results.append({
                'Project_Name': fund['Project_Name'],
                'Funding_Source': fund['Funding_Source'],
                'Amount': int(fund['Amount']),
                'Status': status
            })

# Sort by project name
results = sorted(results, key=lambda x: x['Project_Name'])

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000, 'Status': 'Unknown'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000, 'Status': 'Unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000, 'Status': 'Unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000, 'Status': 'Unknown'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000, 'Status': 'Unknown'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000, 'Status': 'Unknown'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000, 'Status': 'Unknown'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000, 'Status': 'Unknown'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000, 'Status': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000, 'Status': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000, 'Status': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000, 'Status': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000, 'Status': 'Unknown'}, {'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': 92000, 'Status': 'Unknown'}, {'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': 28000, 'Status': 'Unknown'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000, 'Status': 'Unknown'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000, 'Status': 'Unknown'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000, 'Status': 'Unknown'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000, 'Status': 'Unknown'}, {'Project_Name': 'PCH Overhead Warning Signs', 'Funding_Source': 'International Organization Grant', 'Amount': 73000, 'Status': 'Unknown'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000, 'Status': 'Unknown'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000, 'Status': 'Unknown'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000, 'Status': 'Unknown'}]}

exec(code, env_args)

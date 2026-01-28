code = """import json
import pandas as pd
import re

# Load MongoDB documents to extract status information
mongo_file = locals()['var_functions.query_db:0']
with open(mongo_file, 'r') as f:
    mongo_docs = json.load(f)

# Load funding data (already filtered for emergency/fema projects)
prev_result_key = 'var_functions.execute_db:16'  # This doesn't exist, let me use the direct result

# Since the previous result is not in a variable, let me re-calculate it
funding_file = locals()['var_functions.query_db:2']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

df_funding = pd.DataFrame(funding_records)

# Filter for emergency/FEMA projects
mask = df_funding['Project_Name'].str.contains('emergency|fema', case=False, na=False)
emergency_fema_df = df_funding[mask].copy()

print('Processing', len(emergency_fema_df), 'emergency/FEMA projects')

# Extract status and additional info from MongoDB documents
project_statuses = {}

# Create a mapping of project bases to full names
for doc in mongo_docs:
    text = doc.get('text', '')
    
    # Look for each project in the text
    for _, proj in emergency_fema_df.iterrows():
        proj_name = proj['Project_Name']
        base_name = re.sub(r'\s*\([^)]*\)', '', proj_name).strip()
        
        # Check if project is mentioned in text
        if base_name in text or proj_name in text:
            # Extract status from surrounding context
            # Look for status keywords
            status = 'Not specified'
            if 'construction was completed' in text.lower() or 'completed' in text.lower():
                status = 'completed'
            elif 'under construction' in text.lower() or 'construction' in text.lower():
                status = 'construction'
            elif 'design' in text.lower() or 'finalize design' in text.lower():
                status = 'design'
            elif 'not started' in text.lower():
                status = 'not started'
            
            # Look for schedule/timeline info
            timeline_info = []
            # Find patterns like "2023-Spring", "2023-Fall", etc.
            date_patterns = re.findall(r'20\d{2}-\w+', text)
            if date_patterns:
                timeline_info.extend(date_patterns[:2])  # Take first 2 dates
            
            project_statuses[proj_name] = {
                'status': status,
                'timeline': timeline_info
            }

# Combine funding data with status information
results = []
for _, row in emergency_fema_df.iterrows():
    proj_name = row['Project_Name']
    status_info = project_statuses.get(proj_name, {'status': 'Not specified', 'timeline': []})
    
    result = {
        'Project_Name': proj_name,
        'Funding_Source': row['Funding_Source'],
        'Amount': float(row['Amount']),
        'Status': status_info['status'],
        'Project_Type': 'disaster'
    }
    
    # Add timeline if available
    if status_info['timeline']:
        result['Timeline'] = ', '.join(status_info['timeline'])
    
    results.append(result)

# Format output
output_json = json.dumps(results, indent=2)
print('__RESULT__:')
print(output_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)

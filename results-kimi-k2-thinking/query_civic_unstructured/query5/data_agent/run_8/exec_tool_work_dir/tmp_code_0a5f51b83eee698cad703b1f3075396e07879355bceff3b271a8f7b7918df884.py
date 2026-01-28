code = """import json
import pandas as pd
import re

# Load data from storage
civic_docs_file = locals()['var_functions.query_db:2']
with open(civic_docs_file) as f:
    civic_docs = json.load(f)

funding_data = locals()['var_functions.query_db:24']
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Extract disaster projects with 2022 start dates from civic documents
disaster_2022_projects = []

def extract_disaster_projects(text, filename):
    projects = []
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check if line indicates a disaster/FEMA project
        is_disaster = False
        if any(keyword in line for keyword in ['FEMA', 'CalOES', 'CalJPIA']):
            is_disaster = True
        elif 'disaster' in line.lower() or 'fire recovery' in line.lower():
            is_disaster = True
        
        if is_disaster:
            # Look for project name (previous lines that are capitalized)
            project_name = None
            for j in range(max(0, i-5), i):
                prev_line = lines[j].strip()
                if len(prev_line) > 10 and not prev_line.startswith('('):
                    # Check if it looks like a project name (capitalized, not a heading)
                    if sum(1 for c in prev_line if c.isupper()) > len(prev_line) * 0.4:
                        project_name = prev_line
                        break
            
            if not project_name:
                # Use current line as project name
                project_name = line[:100]
            
            # Look for 2022 dates in nearby lines
            start_date = ''
            for k in range(max(0, i-3), min(len(lines), i+8)):
                near_line = lines[k]
                if '2022' in near_line:
                    near_lower = near_line.lower()
                    # Check for start/begin indicators
                    if any(word in near_lower for word in ['begin', 'start', 'advertise', 'design', 'construction', 'complete design']):
                        start_date = '2022'
                        break
            
            if start_date:
                projects.append({
                    'Project_Name': project_name,
                    'start_year': start_date,
                    'source': 'civic_doc'
                })
    
    return projects

# Process all documents
for doc in civic_docs:
    projects = extract_disaster_projects(doc['text'], doc['filename'])
    disaster_2022_projects.extend(projects)

# Create DataFrame
disaster_df = pd.DataFrame(disaster_2022_projects)
print('Found', len(disaster_df), 'disaster projects with 2022 start')

# Remove duplicates
disaster_df = disaster_df.drop_duplicates(subset=['Project_Name'])
print('Unique disaster projects:', len(disaster_df))

# Show sample
if not disaster_df.empty:
    print('\nSample projects:')
    print(disaster_df.head())

# Now match with funding data
matched_funding = []
total_amount = 0

for _, disaster_proj in disaster_df.iterrows():
    disaster_name = disaster_proj['Project_Name'].lower()
    
    # Find matching funding records
    for _, fund_record in funding_df.iterrows():
        fund_name = fund_record['Project_Name'].lower()
        amount = fund_record['Amount']
        
        # Check for direct match or partial match
        if (disaster_name == fund_name or 
            disaster_name in fund_name or 
            fund_name in disaster_name or
            any(word in fund_name for word in disaster_name.split() if len(word) > 5)):
            
            matched_funding.append({
                'disaster_project': disaster_proj['Project_Name'],
                'funding_project': fund_record['Project_Name'],
                'amount': float(amount)
            })
            total_amount += amount

# Remove duplicate funding matches (same funding record might match multiple times)
matched_df = pd.DataFrame(matched_funding)
if not matched_df.empty:
    matched_df = matched_df.drop_duplicates(subset=['funding_project'])
    total_amount = matched_df['amount'].sum()

result = {
    'total_funding': float(total_amount),
    'matched_projects': len(matched_df) if not matched_df.empty else 0
}

print('\nResult:', result)
__RESULT__: json.dumps(result)"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:24': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '59', 'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '37000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '99', 'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000'}]}

exec(code, env_args)

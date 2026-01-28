code = """import json, pandas as pd, re
from collections import defaultdict

# Load civic documents
civic_file = locals()['var_functions.query_db:2']
with open(civic_file) as f:
    civic_docs = json.load(f)

# Load ALL funding data (not just disaster subset)
funding_file = locals()['var_functions.query_db:40']
with open(funding_file) as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

print(f'START: {len(civic_docs)} civic docs, {len(funding_df)} funding records')

# Step 1: Identify disaster-related projects that mention 2022 in civic docs
potential_disaster_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Skip if no 2022 or disaster keywords
    if not ('2022' in text and ('FEMA' in text or 'CalOES' in text or 'CalJPIA' in text)):
        continue
    
    # Split into lines and look for project patterns
    lines = text.split('\n')
    for idx, line in enumerate(lines):
        line = line.strip()
        
        # Look for disaster indicators
        if any(kw in line for kw in ['FEMA', 'CalOES', 'CalJPIA']) or 'disaster' in line.lower():
            # Look back for what might be the project name
            for back_idx in range(idx-1, max(-1, idx-8), -1):
                back_line = lines[back_idx].strip()
                
                # Heuristic: likely a project name if:
                # - More than 15 chars
                # - At least 3 words
                # - Starts with capital letter or mixed case (not all caps)
                # - Not a common heading
                if (len(back_line) > 15 and 
                    len(back_line.split()) >= 3 and 
                    not back_line.isupper() and
                    not any(skip in back_line.upper() for skip in ['PAGE', 'AGENDA', 'ITEM', 'PUBLIC', 'DISCUSSION'])):
                    
                    # Check for 2022 in nearby context
                    context_start = max(0, back_idx-2)
                    context_end = min(len(lines), idx+5)
                    context = ' '.join(lines[context_start:context_end])
                    
                    if '2022' in context and any(indicator in context.lower() for indicator in ['begin', 'start', 'design', 'construction', 'advertise']):
                        potential_disaster_2022.append({
                            'Project_Name': back_line,
                            'filename': filename
                        })
                        break

# Create DataFrame
projects_df = pd.DataFrame(potential_disaster_2022)

# Remove obvious duplicates
if not projects_df.empty:
    projects_df = projects_df.drop_duplicates(subset=['Project_Name'])
    
print(f'Extracted {len(projects_df)} disaster projects starting in 2022')

# Step 2: Match with funding data
total_funding = 0.0
matches = []

for _, proj in projects_df.iterrows():
    proj_name = proj['Project_Name'].strip().lower()
    
    # Skip very short or generic names
    if len(proj_name) < 10:
        continue
    
    # Find matching funding
    for _, fund in funding_df.iterrows():
        fund_name = fund['Project_Name'].strip().lower()
        amount = fund['Amount']
        
        # Skip if amount is NaN
        if pd.isna(amount):
            continue
            
        # Match criteria
        match = False
        
        # 1. Direct contains
        if proj_name in fund_name or fund_name in proj_name:
            match = True
        # 2. Key word match (first 3 significant words)
        else:
            proj_words = [w for w in proj_name.split() if len(w) > 4][:3]
            fund_words = fund_name.split()
            
            if len(proj_words) >= 2:
                matching = sum(1 for pw in proj_words if any(pw in fw for fw in fund_words))
                if matching >= 2:
                    match = True
        
        if match:
            total_funding += amount
            matches.append({
                'project': proj['Project_Name'],
                'funding_project': fund['Project_Name'],
                'amount': float(amount)
            })
            # Remove matched to avoid duplicates
            funding_df = funding_df[funding_df.index != fund.name]
            break

print(f'Matched {len(matches)} projects, total funding: ${total_funding:,.2f}')

# Also check for any disaster project that explicitly has a 2022 date in its name
explicit_2022_disaster = funding_df[
    funding_df['Project_Name'].str.contains('2022', case=False, na=False) &
    funding_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA|disaster', case=False, na=False)
]

if not explicit_2022_disaster.empty:
    print(f'Found {len(explicit_2022_disaster)} explicit 2022 disaster projects')
    total_funding += explicit_2022_disaster['Amount'].sum()
    matches.extend(explicit_2022_disaster.to_dict('records'))

result = {
    'total_funding': float(total_funding),
    'projects_matched': len(matches)
}

print('FINAL RESULT:', result)
__RESULT__: json.dumps(result)"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:24': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '59', 'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '37000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '99', 'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)

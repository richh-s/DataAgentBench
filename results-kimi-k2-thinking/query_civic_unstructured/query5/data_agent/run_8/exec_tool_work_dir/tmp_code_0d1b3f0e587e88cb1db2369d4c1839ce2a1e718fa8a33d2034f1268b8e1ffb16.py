code = """import json
import pandas as pd
import re

# Load civic documents file
civic_docs_file = locals()['var_functions.query_db:2']
print('Reading civic docs from:', civic_docs_file)

with open(civic_docs_file) as f:
    civic_docs = json.load(f)

print('Loaded', len(civic_docs), 'civic documents')

# Load disaster funding data
funding_data = locals()['var_functions.query_db:24']
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

print('Loaded', len(funding_df), 'disaster funding records')

# Function to extract disaster projects with 2022 start dates
def extract_disaster_projects_2022(text, filename):
    projects = []
    lines = text.split('\n')
    
    # Look for patterns that indicate projects
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines
        if not line:
            i += 1
            continue
        
        # Look for lines that might be project names (contain FEMA/CalOES/disaster or nearby)
        project_candidates = []
        
        # Check if current line or nearby lines mention disaster keywords
        has_disaster_keyword = False
        window_lines = lines[max(0, i-5):min(len(lines), i+10)]
        
        for window_line in window_lines:
            if ('FEMA' in window_line or 
                'CalOES' in window_line or
                'CalJPIA' in window_line or
                'disaster' in window_line.lower() or
                'fire recovery' in window_line.lower()):
                has_disaster_keyword = True
                break
        
        if has_disaster_keyword:
            # Try to find a descriptive line (potential project name)
            # Usually within a few lines before the keyword
            start_idx = max(0, i-5)
            end_idx = min(len(lines), i+2)
            
            for j in range(start_idx, end_idx):
                candidate = lines[j].strip()
                if (len(candidate) > 15 and 
                    not candidate.startswith('(') and
                    not any(skip in candidate for skip in ['PAGE', '---', '===']) and
                    len(candidate.split()) >= 3):
                    # This looks like a descriptive line, could be project name
                    project_candidates.append(candidate)
        
        if project_candidates:
            # Check for 2022 dates after the project name
            has_2022_start = False
            for j in range(i, min(i+15, len(lines))):
                check_line = lines[j]
                if '2022' in check_line:
                    check_lower = check_line.lower()
                    # Look for start indicators
                    if any(word in check_lower for word in ['begin', 'start', 'advertise', 'design', 'construction']):
                        has_2022_start = True
                        break
            
            if has_2022_start:
                # Use the most descriptive line as project name
                best_name = max(project_candidates, key=len) if project_candidates else 'Unknown Project'
                projects.append({
                    'Project_Name': best_name,
                    'source_file': filename
                })
                
                # Skip ahead to avoid duplicate detections
                i += 10
                continue
        
        i += 1
    
    return projects

# Extract all disaster projects starting in 2022
all_disaster_projects = []
for doc in civic_docs:
    projects = extract_disaster_projects_2022(doc['text'], doc['filename'])
    all_disaster_projects.extend(projects)

disaster_2022_df = pd.DataFrame(all_disaster_projects)
print('Found', len(disaster_2022_df), 'disaster projects with 2022 start dates')

# Remove duplicates by name
disaster_2022_df = disaster_2022_df.drop_duplicates(subset=['Project_Name'])
print('After deduplication:', len(disaster_2022_df), 'projects')

# Match with funding data
total_funding = 0.0
matched_count = 0

if not disaster_2022_df.empty:
    for _, proj in disaster_2022_df.iterrows():
        project_name = proj['Project_Name']
        project_name_lower = project_name.lower()
        
        # Try to match with each funding record
        for _, fund in funding_df.iterrows():
            fund_name = fund['Project_Name']
            fund_name_lower = fund_name.lower()
            amount = fund['Amount']
            
            # Match strategies
            match_found = False
            
            # Direct match
            if project_name == fund_name:
                match_found = True
            # One contains the other
            elif project_name_lower in fund_name_lower:
                match_found = True
            elif fund_name_lower in project_name_lower:
                match_found = True
            # Partial match (if project name has at least 3 words, check first few words)
            elif len(project_name.split()) >= 3:
                key_words = project_name_lower.split()[:3]
                if all(word in fund_name_lower for word in key_words):
                    match_found = True
            
            if match_found:
                print(f'MATCH: {project_name[:50]}... == {fund_name[:50]}... (${amount})')
                total_funding += amount
                matched_count += 1
                # Remove matched funding to prevent duplicates
                funding_df.drop(fund.name, inplace=True)
                break

print(f'\nTotal matched funding: ${total_funding:,.2f}')
print(f'Projects matched: {matched_count}')

result = {
    'total_disaster_funding_2022': float(total_funding),
    'projects_matched': matched_count,
    'civic_projects_found': len(disaster_2022_df)
}

__RESULT__: json.dumps(result)"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:24': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '59', 'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '37000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '99', 'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000'}]}

exec(code, env_args)

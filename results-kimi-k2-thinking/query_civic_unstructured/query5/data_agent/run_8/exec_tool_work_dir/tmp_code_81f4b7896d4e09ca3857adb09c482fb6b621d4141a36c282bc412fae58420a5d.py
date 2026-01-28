code = """# Load the civic documents from the file path
import json
import pandas as pd
import re

# Read civic documents
civic_docs_file = locals()['var_functions.query_db:2']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents")

# Load all funding data
funding_file = locals()['var_functions.query_db:34']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

print(f"Loaded {len(funding_df)} funding records")

# Function to extract project information from civic document text
def extract_projects_from_text(text, filename):
    projects = []
    lines = text.split('\n')
    
    # Pattern to identify project sections
    # Look for lines that are likely project names (capitalized, not too short)
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
            
        # Skip common header/footer lines
        if any(skip in line for skip in ['PAGE', 'AGENDA', 'ITEM', '---', '===']):
            continue
            
        # Check if this line might be a project name
        # Heuristic: contains some capital letters, not all lowercase, reasonable length
        if sum(1 for c in line if c.isupper()) > 2 and len(line) > 15:
            
            # Look for disaster indicators in this line or nearby lines
            window_start = max(0, i-5)
            window_end = min(len(lines), i+10)
            window_text = ' '.join(lines[window_start:window_end]).lower()
            
            is_disaster = any(keyword in window_text for keyword in 
                            ['fema', 'caloes', 'caljpia', 'disaster', 'fire recovery', 'woolsey'])
            
            # Check for 2022 start date indicators
            has_2022_start = False
            for j in range(window_start, window_end):
                check_line = lines[j]
                if '2022' in check_line:
                    # Check if it's a start indicator
                    lower_line = check_line.lower()
                    if any(indicator in lower_line for indicator in 
                          ['start', 'begin', 'advertise', 'design', 'construction', 'st:', 'start:']):
                        has_2022_start = True
                        break
            
            if is_disaster and has_2022_start:
                # Extract project name (clean it up)
                project_name = line.strip()
                
                # Remove common suffixes that might be in the document but not in funding
                project_name = re.sub(r'\s*(Project|Program)\s*$', '', project_name, flags=re.IGNORECASE)
                
                projects.append({
                    'Project_Name': project_name,
                    'source_file': filename,
                    'disaster_type': True,
                    'start_2022': True
                })
    
    return projects

# Extract all disaster projects starting in 2022
disaster_projects_2022 = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'], doc['filename'])
    disaster_projects_2022.extend(projects)

# Create DataFrame and deduplicate
disaster_df = pd.DataFrame(disaster_projects_2022)
if not disaster_df.empty:
    # Remove duplicates by project name
    disaster_df = disaster_df.drop_duplicates(subset=['Project_Name'])
    
print(f"Found {len(disaster_df)} disaster projects starting in 2022")

# Now match with funding data
# Create a mapping for easier matching
matched_funding = []
total_funding = 0

for _, proj in disaster_df.iterrows():
    proj_name = proj['Project_Name'].strip().lower()
    
    # Try different matching strategies
    for _, fund in funding_df.iterrows():
        fund_name = fund['Project_Name'].strip().lower()
        fund_amount = fund['Amount']
        
        match = False
        
        # Strategy 1: Exact match (after cleaning)
        if proj_name == fund_name:
            match = True
        # Strategy 2: One contains the other
        elif proj_name in fund_name or fund_name in proj_name:
            match = True
        # Strategy 3: Check if project name is at the beginning of funding name
        elif fund_name.startswith(proj_name[:30]):
            match = True
        # Strategy 4: Check for key components matching
        else:
            # Extract key words (remove common words)
            proj_words = [w for w in proj_name.split() if len(w) > 4 and w not in ['project', 'improvements', 'repairs', 'and']]
            fund_words = [w for w in fund_name.split() if len(w) > 4]
            
            # If at least 2 key words match, consider it a match
            matching_words = sum(1 for pw in proj_words if any(pw in fw for fw in fund_words))
            if matching_words >= 2:
                match = True
        
        if match:
            matched_funding.append({
                'civic_project': proj['Project_Name'],
                'funding_project': fund['Project_Name'],
                'amount': fund_amount
            })
            total_funding += fund_amount
            # Remove matched funding to avoid double counting
            funding_df = funding_df[funding_df.index != fund.name]
            break

result = {
    'total_funding': float(total_funding),
    'matched_projects': len(matched_funding)
}

print(f"Total funding: ${total_funding:,.2f}")
print(f"Matched {len(matched_funding)} projects")

__RESULT__: json.dumps(result)"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:24': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '59', 'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '37000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '99', 'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)

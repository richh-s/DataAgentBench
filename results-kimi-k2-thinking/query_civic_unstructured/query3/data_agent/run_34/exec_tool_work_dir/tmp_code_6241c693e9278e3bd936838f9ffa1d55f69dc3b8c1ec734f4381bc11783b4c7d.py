code = """import json
import re

# Read civic documents data
civic_path = locals()['var_functions.query_db:34']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Read funding data
funding_path = locals()['var_functions.query_db:35']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Function to extract project status from text
def extract_status(text):
    text_lower = text.lower()
    if 'construction was completed' in text_lower or 'completed' in text_lower:
        return 'completed'
    elif 'currently under construction' in text_lower or 'under construction' in text_lower:
        return 'construction'
    elif 'design' in text_lower or 'awaiting' in text_lower or 'pending' in text_lower:
        return 'design'
    elif 'not started' in text_lower:
        return 'not started'
    return 'unknown'

# Extract projects from civic documents
civic_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Split by double newlines to find project sections
    sections = text.split('\n\n')
    
    for section in sections:
        section = section.strip()
        if not section:
            continue
            
        # Check if section mentions FEMA or emergency
        if 'FEMA' in section or 'emergency' in section.lower() or 'Emergency' in section:
            # Extract project name (first line that's not a marker)
            lines = section.split('\n')
            project_name = None
            
            for line in lines:
                line = line.strip()
                if line and not line.startswith('(cid:') and not line.startswith('Page') and len(line) < 100:
                    # Check if this looks like a project name by looking ahead
                    if 'Updates:' in section or 'Project Schedule:' in section:
                        project_name = line
                        break
            
            if project_name:
                status = extract_status(section)
                project_type = 'disaster' if 'FEMA' in section or 'disaster' in section.lower() else 'capital'
                
                civic_projects.append({
                    'Project_Name': project_name,
                    'status': status,
                    'type': project_type
                })

# Create a mapping of project names to funding info
funding_map = {}
for fund in funding_data:
    project_name = fund['Project_Name']
    funding_map[project_name] = {
        'Funding_Source': fund['Funding_Source'],
        'Amount': fund['Amount']
    }

# Also create a mapping for base project names (without FEMA/CalOES suffixes)
base_funding_map = {}
for fund in funding_data:
    project_name = fund['Project_Name']
    # Remove FEMA/CalOES suffixes for matching
    base_name = re.sub(r'\s*\((?:FEMA|CalOES|CalJPIA)[^)]*\)', '', project_name).strip()
    if base_name not in base_funding_map:
        base_funding_map[base_name] = []
    base_funding_map[base_name].append({
        'Project_Name': project_name,
        'Funding_Source': fund['Funding_Source'],
        'Amount': fund['Amount']
    })

# Combine information
results = []

# First, add all funding records with FEMA/emergency in their name
for project_name, funding_info in funding_map.items():
    # Find matching civic project
    matching_civic = None
    for civic_proj in civic_projects:
        civic_name = civic_proj['Project_Name']
        # Check for exact match or base name match
        if (project_name.lower() in civic_name.lower() or 
            civic_name.lower() in project_name.lower() or
            re.sub(r'\s*\((?:FEMA|CalOES|CalJPIA)[^)]*\)', '', project_name).strip().lower() in civic_name.lower()):
            matching_civic = civic_proj
            break
    
    if matching_civic:
        results.append({
            'Project_Name': project_name,
            'Funding_Source': funding_info['Funding_Source'],
            'Amount': funding_info['Amount'],
            'Status': matching_civic['status'],
            'Type': matching_civic['type']
        })
    else:
        # Project only in funding data, not in civic docs
        results.append({
            'Project_Name': project_name,
            'Funding_Source': funding_info['Funding_Source'],
            'Amount': funding_info['Amount'],
            'Status': 'unknown',
            'Type': 'disaster' if 'FEMA' in project_name else 'unknown'
        })

# Add civic projects that might not have funding records (with missing funding info)
for civic_proj in civic_projects:
    civic_name = civic_proj['Project_Name']
    
    # Check if already added
    already_added = False
    for result in results:
        if civic_name.lower() in result['Project_Name'].lower() or result['Project_Name'].lower() in civic_name.lower():
            already_added = True
            break
    
    if not already_added:
        # Find funding by base name match
        funding_info = None
        for base_name, fund_records in base_funding_map.items():
            if base_name.lower() in civic_name.lower() or civic_name.lower() in base_name.lower():
                funding_info = fund_records[0]  # Take first match
                break
        
        if funding_info:
            results.append({
                'Project_Name': civic_name,
                'Funding_Source': funding_info['Funding_Source'],
                'Amount': funding_info['Amount'],
                'Status': civic_proj['status'],
                'Type': civic_proj['type']
            })
        else:
            results.append({
                'Project_Name': civic_name,
                'Funding_Source': 'Not found',
                'Amount': 0,
                'Status': civic_proj['status'],
                'Type': civic_proj['type']
            })

# Sort by project name for consistency
results = sorted(results, key=lambda x: x['Project_Name'])

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:32': {'projects_from_civic_docs': [{'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'status': 'completed', 'type': 'disaster'}], 'funding_records': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)

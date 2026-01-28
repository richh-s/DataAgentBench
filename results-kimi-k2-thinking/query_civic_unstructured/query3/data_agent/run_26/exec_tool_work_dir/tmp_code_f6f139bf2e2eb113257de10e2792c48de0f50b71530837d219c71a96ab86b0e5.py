code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:12']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Create a mapping of base project names to funding info
funding_lookup = {}
for item in funding_data:
    project_name = item['Project_Name']
    base_name = project_name.split('(')[0].strip().lower()
    if base_name not in funding_lookup:
        funding_lookup[base_name] = []
    funding_lookup[base_name].append({
        'Full_Project_Name': project_name,
        'Funding_Source': item['Funding_Source'],
        'Amount': int(item['Amount'])
    })

# Projects to look for (base names)
target_projects = []
for name in funding_lookup.keys():
    if 'fema' in name or 'caloes' in name.lower() or 'caljpia' in name.lower():
        target_projects.append(name)

print(f"Looking for {len(target_projects)} target projects")

# Search through civic documents for project information
project_status_info = {}

for doc in civic_docs:
    text = doc['text']
    filename = doc.get('filename', '')
    
    # Look for sections about projects
    lines = text.split('\n')
    
    # First, identify the current section type and status
    current_section = None
    section_status = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Detect section headers
        if 'Capital Improvement Projects (Design)' in line:
            current_section = 'capital'
            section_status = 'design'
        elif 'Capital Improvement Projects (Construction)' in line:
            current_section = 'capital'
            section_status = None  # Will determine from text
        elif 'Capital Improvement Projects (Not Started)' in line:
            current_section = 'capital'
            section_status = 'not started'
        elif 'Disaster Recovery Projects' in line:
            current_section = 'disaster'
            section_status = None
            
        # Look for project names that match our target projects
        for target in target_projects:
            # Check if this line contains the project name (case-insensitive)
            if target in line.lower() and len(line) < 200 and not line.startswith('('):
                # Check if this is likely a project name line (not a bullet point)
                if not line.startswith('•') and not line.startswith('-') and not line.startswith('□'):
                    clean_line = line.split('(')[0].strip().lower()
                    if target in clean_line:
                        status = section_status or 'Not specified'
                        
                        # Try to find more specific status in following lines
                        for j in range(i+1, min(i+6, len(lines))):
                            next_line = lines[j].strip().lower()
                            if 'complete construction' in next_line or 'construction was completed' in next_line:
                                status = 'completed'
                                break
                            elif 'currently under construction' in next_line:
                                status = 'in construction'
                                break
                            elif 'complete design' in next_line:
                                status = 'design'
                                break
                            elif 'advertise' in next_line and 'not started' not in status:
                                status = 'bidding'
                                break
                        
                        if target not in project_status_info:
                            project_status_info[target] = []
                        project_status_info[target].append({
                            'status': status,
                            'section_type': current_section,
                            'filename': filename
                        })

# Create final results
final_results = []

for target in target_projects:
    # Find the most common status for this project
    if target in project_status_info:
        # Get the status that appears most frequently
        status_counts = {}
        for info in project_status_info[target]:
            status = info['status']
            status_counts[status] = status_counts.get(status, 0) + 1
        most_common_status = max(status_counts, key=status_counts.get)
    else:
        most_common_status = 'Status not found in civic documents'
    
    # Get funding information
    for funding in funding_lookup.get(target, []):
        final_results.append({
            'Project_Name': funding['Full_Project_Name'],
            'Funding_Source': funding['Funding_Source'],
            'Amount': funding['Amount'],
            'Status': most_common_status,
            'Type': 'Disaster Recovery (FEMA/CalOES/CalJPIA)'
        })

# Sort by project name
final_results.sort(key=lambda x: x['Project_Name'])

print(f"Found {len(final_results)} projects with complete information")
print('__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}], 'var_functions.execute_python:10': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 81000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': 18000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 37000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 43000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': 32000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': 77000, 'Status': 'Not found in civic documents', 'Type': 'Unknown'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 81000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': 18000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 37000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 43000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': 32000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': 77000, 'Status': 'Status information not available in current data extract', 'Type': 'Disaster Recovery'}]}

exec(code, env_args)

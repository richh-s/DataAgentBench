code = """import json

# Load the filtered emergency/FEMA funding data
funding_emergency = locals()['var_functions.query_db:40']

# Load the civic documents related to emergency/FEMA/project status
civic_docs_path = locals()['var_functions.query_db:42']
with open(civic_docs_path) as f:
    civic_docs = json.load(f)

# Create a dictionary of funding projects for easy lookup
funding_dict = {item['Project_Name']: item for item in funding_emergency}

print("Found", len(funding_emergency), "emergency/FEMA projects in funding database")

# Extract project status information from civic documents
project_status_info = {}

for doc in civic_docs:
    text = doc['text']
    text_lower = text.lower()
    lines = text.split('\n')
    
    # Track current project being discussed
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Look for project names that might be in our emergency list
        # Check if this line looks like a project name
        line_lower = line.lower()
        
        # Check for exact matches or near matches with our funding projects
        for funded_proj_name in funding_dict.keys():
            funded_proj_lower = funded_proj_name.lower()
            
            # Check if this line contains the project name (or a substantial part of it)
            # Remove the suffixes for matching
            base_name = funded_proj_name.replace(' (FEMA Project)', '').replace(' (FEMA/CalOES Project)', '').replace(' (CalJPIA/FEMA Project)', '').strip()
            base_name_lower = base_name.lower()
            
            if (base_name_lower in line_lower or line_lower in funded_proj_lower) and len(line) > 10:
                current_project = funded_proj_name
                
                # Determine status
                status = 'not started'
                
                # Check for design phase indicators
                if 'design' in text_lower or 'working with consultant' in text_lower:
                    if 'complete design' not in text_lower or 'finalizing design' in text_lower:
                        status = 'design'
                
                # Check for construction/completed indicators
                if 'under construction' in text_lower or 'construction was completed' in text_lower:
                    if base_name_lower in text_lower:
                        status = 'completed'
                        
                # Check for completed phases
                if 'construction was completed' in text_lower or 'construction completed' in text_lower:
                    if base_name_lower in text_lower:
                        status = 'completed'
                        
                # Store the status
                if current_project:
                    project_status_info[current_project] = status
                    
                break  # Found a match, no need to check other projects for this line

# Now compile the final results with all information
final_results = []

for proj_name, funding_info in funding_dict.items():
    # Get status from our extracted info, default to 'not started'
    status = project_status_info.get(proj_name, 'not started')
    
    # Determine type (disaster vs capital)
    proj_type = 'disaster' if 'fema' in proj_name.lower() else 'capital'
    
    final_results.append({
        'Project_Name': proj_name,
        'Funding_Source': funding_info['Funding_Source'],
        'Amount': int(funding_info['Amount']),
        'Status': status,
        'Type': proj_type
    })

# Format output
output_text = "EMERGENCY/FEMA RELATED PROJECTS\n"
output_text += "=" * 60 + "\n\n"

for project in final_results:
    output_text += f"Project: {project['Project_Name']}\n"
    output_text += f"  Funding Source: {project['Funding_Source']}\n"
    output_text += f"  Amount: ${project['Amount']:,}\n"
    output_text += f"  Status: {project['Status']}\n"
    output_text += f"  Type: {project['Type']}\n"
    output_text += "\n"

print('__RESULT__:')
print(output_text)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:22': {'funding_type': "<class 'str'>", 'docs_type': "<class 'str'>"}, 'var_functions.execute_python:34': {'funding_count': 500, 'docs_count': 5}, 'var_functions.execute_python:38': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000, 'Status': 'not started', 'Type': 'disaster'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000, 'Status': 'not started', 'Type': 'disaster'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000, 'Status': 'not started', 'Type': 'disaster'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000, 'Status': 'not started', 'Type': 'disaster'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000, 'Status': 'not started', 'Type': 'disaster'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000, 'Status': 'not started', 'Type': 'disaster'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000, 'Status': 'not started', 'Type': 'disaster'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000, 'Status': 'not started', 'Type': 'disaster'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000, 'Status': 'not started', 'Type': 'disaster'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000, 'Status': 'not started', 'Type': 'disaster'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000, 'Status': 'not started', 'Type': 'disaster'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000, 'Status': 'not started', 'Type': 'disaster'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000, 'Status': 'not started', 'Type': 'disaster'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000, 'Status': 'not started', 'Type': 'disaster'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000, 'Status': 'not started', 'Type': 'disaster'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000, 'Status': 'not started', 'Type': 'disaster'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000, 'Status': 'not started', 'Type': 'disaster'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000, 'Status': 'not started', 'Type': 'disaster'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000, 'Status': 'not started', 'Type': 'disaster'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000, 'Status': 'not started', 'Type': 'disaster'}], 'var_functions.query_db:40': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)

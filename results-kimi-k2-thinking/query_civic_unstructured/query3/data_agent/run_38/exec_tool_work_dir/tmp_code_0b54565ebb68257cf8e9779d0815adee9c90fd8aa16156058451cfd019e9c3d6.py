code = """import json
import re

# Load the funding data with FEMA projects
fema_funding = locals()['var_functions.query_db:46']

# Load civic documents to extract status information
civic_docs_path = locals()['var_functions.query_db:42']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Create a list to hold final results
results = []

# Process each FEMA project from funding
for project in fema_funding:
    project_name = project['Project_Name']
    funding_source = project['Funding_Source']
    amount = int(project['Amount'])
    
    # Default status
    status = 'Unknown'
    
    # Try to find status in civic documents
    for doc in civic_docs:
        text = doc.get('text', '')
        if project_name in text:
            # Found the project, determine status
            if 'under construction' in text.lower():
                status = 'construction'
            elif 'design' in text.lower():
                status = 'design'
            elif 'complete' in text.lower() or 'completed' in text.lower():
                status = 'completed'
            else:
                status = 'not started'
            break
        else:
            # Try partial matching for projects with suffixes
            base_name = project_name.split('(')[0].strip()
            if base_name in text:
                # Same status checks
                if 'under construction' in text.lower():
                    status = 'construction'
                elif 'design' in text.lower():
                    status = 'design'
                elif 'complete' in text.lower() or 'completed' in text.lower():
                    status = 'completed'
                else:
                    status = 'not started'
                break
    
    results.append({
        'Project_Name': project_name,
        'Funding_Source': funding_source,
        'Amount': amount,
        'Status': status,
        'Topic': 'FEMA',
        'Type': 'disaster'
    })

# Also look for projects with "emergency" in civic docs
# Extract projects from documents containing "emergency"
emergency_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    if 'emergency' in lower_text:
        # Extract project names
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if len(line) > 10:
                # Skip headers
                if any(header in line for header in ['Capital Improvement', 'Disaster Recovery', 'Agenda Report', 'Public Works Commission']):
                    continue
                # Check if this is a project name (followed by cid:190)
                if i + 1 < len(lines) and '(cid:190)' in lines[i+1]:
                    project_name = line
                    
                    # Check if we already have this project
                    already_have = False
                    for result in results:
                        if project_name in result['Project_Name'] or result['Project_Name'] in project_name:
                            already_have = True
                            break
                    
                    if not already_have:
                        # Determine status
                        status = 'not started'
                        context = ' '.join(lines[i:i+15]).lower()
                        if 'under construction' in context:
                            status = 'construction'
                        elif 'design' in context:
                            status = 'design'
                        elif 'complete' in context or 'completed' in context:
                            status = 'completed'
                        
                        # Look for funding
                        funding_source = 'No funding record'
                        amount = 0
                        
                        # Add to results
                        results.append({
                            'Project_Name': project_name,
                            'Funding_Source': funding_source,
                            'Amount': amount,
                            'Status': status,
                            'Topic': 'emergency',
                            'Type': 'capital'  # Default to capital unless FEMA is mentioned
                        })

# Format output
output_lines = []
for r in results:
    output_lines.append(f"Project: {r['Project_Name']}")
    output_lines.append(f"  Funding Source: {r['Funding_Source']}")
    output_lines.append(f"  Amount: ${r['Amount']:,}")
    output_lines.append(f"  Status: {r['Status']}")
    output_lines.append(f"  Topic: {r['Topic']}")
    output_lines.append(f"  Type: {r['Type']}")
    output_lines.append('')

final_output = '\n'.join(output_lines)
print('__RESULT__:')
print(final_output)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'name': 'Funding'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.list_db:44': ['civic_docs'], 'var_functions.query_db:46': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_functions.query_db:48': []}

exec(code, env_args)

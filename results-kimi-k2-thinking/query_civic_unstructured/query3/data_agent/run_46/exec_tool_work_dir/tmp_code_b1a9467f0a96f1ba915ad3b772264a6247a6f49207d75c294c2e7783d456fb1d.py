code = """import json
import re

# Read funding data
funding_path = locals()['var_functions.query_db:16']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Read civic_docs data
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Filter funding for FEMA/emergency projects
fema_projects = []
for record in funding_data:
    project_name = record['Project_Name'].lower()
    if 'fema' in project_name or 'emergency' in project_name:
        fema_projects.append(record)

# Extract project information from text
def extract_project_info(text, project_names):
    """Extract project status and details from text"""
    results = {}
    
    # Normalize text for searching
    text_lower = text.lower()
    
    for project in project_names:
        proj_lower = project.lower()
        
        # Find if project is mentioned in text
        if proj_lower in text_lower:
            # Determine status based on section headers
            status = "Unknown"
            
            # Look for section headers
            if "capital improvement projects (design)" in text_lower and proj_lower in text_lower:
                status = "design"
            elif "capital improvement projects (construction)" in text_lower and proj_lower in text_lower:
                status = "construction"
            elif "capital improvement projects (not started)" in text_lower and proj_lower in text_lower:
                status = "not started"
            elif "disaster recovery projects" in text_lower and proj_lower in text_lower:
                status = "disaster recovery"
            
            # Check for completion indicators
            if "completed" in text_lower or "construction was completed" in text_lower:
                if proj_lower in text_lower:
                    status = "completed"
            
            results[project] = status
    
    return results

# Get project names from funding data
project_names = [p['Project_Name'] for p in fema_projects]

# Extract info from all documents
all_project_info = {}
for doc in civic_docs:
    info = extract_project_info(doc['text'], project_names)
    for proj, status in info.items():
        if proj not in all_project_info or status != "Unknown":
            all_project_info[proj] = status

# Combine funding and status info
final_results = []
for project in fema_projects:
    project_name = project['Project_Name']
    status = all_project_info.get(project_name, "Not found in civic docs")
    
    final_results.append({
        'Project_Name': project_name,
        'Funding_Source': project['Funding_Source'],
        'Amount': int(project['Amount']),
        'Status': status
    })

# Sort by project name
final_results.sort(key=lambda x: x['Project_Name'])

print('__RESULT__:')
print(json.dumps({
    'count': len(final_results),
    'projects': final_results
}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_projects': 500, 'emergency_fema_count': 20, 'projects': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}, 'var_functions.execute_python:22': 'file_storage/functions.execute_python:22.json'}

exec(code, env_args)

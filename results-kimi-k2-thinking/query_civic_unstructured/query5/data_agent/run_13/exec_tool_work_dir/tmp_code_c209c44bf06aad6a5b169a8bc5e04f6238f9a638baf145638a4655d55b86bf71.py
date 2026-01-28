code = """import json
import re

# Load the disaster-related funding data
disaster_funding_path = locals()['var_functions.query_db:36']
if isinstance(disaster_funding_path, str):
    with open(disaster_funding_path, 'r') as f:
        disaster_funding = json.load(f)
else:
    disaster_funding = locals()['var_functions.query_db:36']

# Load the civic documents data
civic_docs_path = locals()['var_functions.query_db:34']
if isinstance(civic_docs_path, str):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = locals()['var_functions.query_db:34']

# Create a dictionary of disaster projects for easy lookup
disaster_projects_dict = {proj['Project_Name']: int(proj['Amount']) for proj in disaster_funding}

# Initialize results
projects_started_2022 = []

# Parse each civic document
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check each disaster project
        for project_name in disaster_projects_dict.keys():
            # Check if this line mentions the project
            if project_name in line or (len(line) > 10 and project_name.startswith(line)):
                # Look for 2022 start dates in the next few lines
                context_start = max(0, i)
                context_end = min(len(lines), i + 8)
                context = '\n'.join(lines[context_start:context_end])
                
                # Check for various start date patterns with 2022
                start_patterns = [
                    r'2022[-\s]\w+',  # 2022-Spring, 2022-Fall, etc.
                    r'\w+\s*2022',    # Spring 2022, Fall 2022, etc.
                    r'Begin[^\n]*2022',
                    r'Start[^\n]*2022',
                    r'Complete[^\n]*2022',
                    r'2022\s*\w+'
                ]
                
                has_2022_start = False
                for pattern in start_patterns:
                    if re.search(pattern, context, re.IGNORECASE):
                        has_2022_start = True
                        break
                
                # Also check if project name itself contains 2022
                if '2022' in project_name:
                    has_2022_start = True
                
                if has_2022_start and project_name not in [p['project_name'] for p in projects_started_2022]:
                    projects_started_2022.append({
                        'project_name': project_name,
                        'amount': disaster_projects_dict[project_name]
                    })

# Calculate total funding
total_funding = sum(proj['amount'] for proj in projects_started_2022)

print('__RESULT__')
print(json.dumps({
    'total_disaster_projects_in_funding': len(disaster_projects_dict),
    'projects_started_in_2022': len(projects_started_2022),
    'total_funding_2022': total_funding,
    'project_details': projects_started_2022
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': 'file_storage/functions.execute_python:4.json', 'var_functions.execute_python:12': {'funding_records': 500, 'civic_docs': 5}, 'var_functions.execute_python:14': {'civic_docs_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'civic_docs_full_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:20': {'civic_docs_total': 5, 'funding_records_total': 500, 'sample_doc_filename': 'malibucity_agenda_03222023-2060.txt'}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000'}, {'Project_Name': 'Outdoor Warning Signs', 'Amount': '92000'}, {'Project_Name': 'Outdoor Warning Sirens', 'Amount': '28000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Amount': '84000'}, {'Project_Name': 'PCH Overhead Warning Signs', 'Amount': '73000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Amount': '77000'}]}

exec(code, env_args)

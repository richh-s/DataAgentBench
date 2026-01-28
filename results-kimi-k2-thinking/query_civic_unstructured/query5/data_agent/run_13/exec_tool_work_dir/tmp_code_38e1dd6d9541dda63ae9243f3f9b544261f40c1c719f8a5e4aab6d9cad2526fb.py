code = """import json

# Load disaster funding data
disaster_funding_path = locals()['var_functions.query_db:36']
if isinstance(disaster_funding_path, str) and disaster_funding_path.endswith('.json'):
    with open(disaster_funding_path, 'r') as f:
        disaster_funding = json.load(f)
else:
    disaster_funding = disaster_funding_path

# Load civic documents data
civic_docs_path = locals()['var_functions.query_db:34']
if isinstance(civic_docs_path, str) and civic_docs_path.endswith('.json'):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_path

# Create mapping of disaster project names to amounts
project_amounts = {item['Project_Name']: int(item['Amount']) for item in disaster_funding}

# Find projects that started in 2022
projects_started_2022 = set()

for doc in civic_docs:
    text = doc.get('text', '')
    for project_name in project_amounts.keys():
        # Check if project is mentioned in text
        if project_name in text:
            # Look for 2022 in the context
            # Search around the project name for date references
            index = text.find(project_name)
            if index >= 0:
                context = text[index:min(len(text), index + 500)]
                if '2022' in context or '2022' in project_name:
                    # Verify it's a disaster project
                    for keyword in ['FEMA', 'CalOES', 'CalJPIA', 'fire']:
                        if keyword.lower() in project_name.lower():
                            projects_started_2022.add(project_name)
                            break

# Calculate total funding
total_funding = sum(project_amounts[proj] for proj in projects_started_2022)

# Prepare result
result = {
    'disaster_projects_total': len(project_amounts),
    'started_in_2022': len(projects_started_2022),
    'total_funding': total_funding
}

print('__RESULT__')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': 'file_storage/functions.execute_python:4.json', 'var_functions.execute_python:12': {'funding_records': 500, 'civic_docs': 5}, 'var_functions.execute_python:14': {'civic_docs_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'civic_docs_full_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:20': {'civic_docs_total': 5, 'funding_records_total': 500, 'sample_doc_filename': 'malibucity_agenda_03222023-2060.txt'}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000'}, {'Project_Name': 'Outdoor Warning Signs', 'Amount': '92000'}, {'Project_Name': 'Outdoor Warning Sirens', 'Amount': '28000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Amount': '84000'}, {'Project_Name': 'PCH Overhead Warning Signs', 'Amount': '73000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Amount': '77000'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)

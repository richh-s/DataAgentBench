code = """import json
import re

# Get the funding data
funding_path = locals()['var_functions.query_db:44']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Get the civic documents
civic_path = locals()['var_functions.query_db:26']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# First, identify all disaster-related funding records
disaster_funding = {}
for rec in funding_records:
    proj_name = rec['Project_Name']
    if any(indicator in proj_name for indicator in ['(FEMA', '(CalJPIA', '(CalOES']):
        disaster_funding[proj_name] = int(rec['Amount'])

print('Disaster funding records:', len(disaster_funding))

# Now search civic docs for disaster projects with 2022 start dates
disaster_2022 = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find all disaster project names in this document
    for proj_name in disaster_funding.keys():
        if proj_name in text and '2022' in text:
            # Check if there's date context indicating start
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if proj_name in line:
                    # Look at surrounding lines for start/begin/advertise
                    start = max(0, i-3)
                    end = min(len(lines), i+6)
                    context = ' '.join(lines[start:end])
                    
                    # Check for 2022 in context
                    if '2022' in context:
                        # Check for start-related keywords
                        if any(keyword in context.lower() for keyword in ['start', 'begin', 'advertise', 'design', 'complete']):
                            disaster_2022.add(proj_name)

print('Found disaster projects starting in 2022:', len(disaster_2022))
for proj in sorted(disaster_2022):
    print(' -', proj, ': $', disaster_funding[proj])

# Calculate total funding
total_funding = sum(disaster_funding[proj] for proj in disaster_2022)
print('Total funding for 2022 disaster projects: $', total_funding)

result = {
    'total_funding': total_funding,
    'project_count': len(disaster_2022),
    'projects': sorted(disaster_2022)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['civic_docs'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': [{'total_disaster_funding': '1410000'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Amount': '77000'}], 'var_functions.query_db:34': [{'total_disaster_funding': '1410000'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'disaster_project_names': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Guardrail Replacement Citywide (FEMA Project)', 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Malibu Road Slope Repairs (CalOES Project)', 'Outdoor Warning Sirens (FEMA Project)', 'Outdoor Warning Sirens (FEMA)', 'Outdoor Warning Sirens - Design (FEMA Project)', 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Storm Drain Master Plan (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)'], 'count': 27}, 'var_functions.query_db:48': [{'total_2022_disaster_funding': 'None'}], 'var_functions.query_db:54': [{'total': 'None'}]}

exec(code, env_args)

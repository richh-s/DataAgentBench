code = """import json
import re

# Load all disaster project funding records
funding_data_str = locals()['var_functions.query_db:52']

# Convert string to actual data structure
if isinstance(funding_data_str, str):
    try:
        funding_records = json.loads(funding_data_str)
    except:
        import ast
        funding_records = ast.literal_eval(funding_data_str)
else:
    funding_records = funding_data_str

# Create a dictionary to track total funding per base project name
base_project_funding = {}
for record in funding_records:
    project_name = record['Project_Name']
    amount = int(record['total_amount'])
    
    # Extract base name (remove suffixes)
    base_name = project_name.split(' (')[0]
    
    if base_name not in base_project_funding:
        base_project_funding[base_name] = 0
    base_project_funding[base_name] += amount

# Load civic documents to find projects starting in 2022
civic_docs_str = locals()['var_functions.query_db:32']

# Convert string to actual data structure
if isinstance(civic_docs_str, str):
    try:
        civic_docs = json.loads(civic_docs_str)
    except:
        import ast
        civic_docs = ast.literal_eval(civic_docs_str)
else:
    civic_docs = civic_docs_str

# Find projects that mention both disaster keywords and 2022
projects_starting_2022 = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Split into lines and look for project names
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Skip empty lines and very short ones
        if not line or len(line) < 5:
            continue
            
        # Check if this looks like a project name (starts with capital letters/numbers)
        if re.match(r'^[A-Z0-9][A-Za-z0-9\s\-&]+', line):
            base_name = line.split(' (')[0].strip()
            
            # Check if this is a disaster project we have funding for
            if base_name in base_project_funding:
                # Check context for 2022 start date
                context_start = max(0, i-5)
                context_end = min(len(lines), i+5)
                context = ' '.join(lines[context_start:context_end])
                
                # Look for 2022 in the surrounding context
                if '2022' in context:
                    projects_starting_2022.add(base_name)

# Calculate total funding for disaster projects that started in 2022
total_2022_funding = 0
for project in projects_starting_2022:
    if project in base_project_funding:
        total_2022_funding += base_project_funding[project]

print('__RESULT__:')
print(json.dumps({
    'total_disaster_funding_2022': total_2022_funding,
    'project_count': len(projects_starting_2022),
    'projects': list(projects_starting_2022),
    'all_disaster_funding': sum(base_project_funding.values()),
    'all_disaster_count': len(base_project_funding)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'status': 'loaded', 'count': 0}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': {'status': 'checked_types'}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:42': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000', 'Funding_Source': 'International Aid'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000', 'Funding_Source': 'Research Institution Funding'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000', 'Funding_Source': 'Government Grant'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000', 'Funding_Source': 'Local NGO Fund'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000', 'Funding_Source': 'Municipal Fund'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000', 'Funding_Source': 'Taxpayer Contribution'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000', 'Funding_Source': 'Local Business Support'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000', 'Funding_Source': 'Cultural Heritage Grant'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000', 'Funding_Source': 'Educational Sponsorship'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000', 'Funding_Source': 'Private Sponsor'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000', 'Funding_Source': 'Impact Investment Fund'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000', 'Funding_Source': 'Development Bank Loan'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000', 'Funding_Source': 'Federal Assistance'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000', 'Funding_Source': 'National Foundation Fund'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000', 'Funding_Source': 'Municipal Fund'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000', 'Funding_Source': 'Community Fund'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000', 'Funding_Source': 'International Aid'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000', 'Funding_Source': 'Environmental Grant'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000', 'Funding_Source': 'State Development Grant'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000', 'Funding_Source': 'Local Business Support'}], 'var_functions.query_db:44': [{'total_funding': '1410000'}], 'var_functions.query_db:46': [], 'var_functions.query_db:52': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'total_amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'total_amount': '14000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'total_amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'total_amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'total_amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'total_amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'total_amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'total_amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'total_amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'total_amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'total_amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'total_amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'total_amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'total_amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'total_amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'total_amount': '78000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'total_amount': '37000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'total_amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'total_amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'total_amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'total_amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'total_amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'total_amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'total_amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'total_amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'total_amount': '32000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'total_amount': '77000'}]}

exec(code, env_args)

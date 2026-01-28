code = """import json, re

with open('funding_data.json', 'w') as f:
    json.dump(var_functions.query_db:54, f, indent=2)

with open('civic_data.json', 'w') as f:
    json.dump(var_functions.query_db:55, f, indent=2)

with open('funding_data.json') as f:
    funding_data = json.load(f)

with open('civic_data.json') as f:
    civic_data = json.load(f)

# Direct analysis: projects with 2022 in name and disaster keywords
from collections import defaultdict
project_funding = defaultdict(int)

# Check funding data directly for 2022 disaster projects
for item in funding_data:
    name = item.get('Project_Name', '')
    amount = int(item.get('Amount', 0))
    
    # Look for 2022 in the name
    has_2022 = '2022' in name
    is_disaster = any(kw in name.upper() for kw in ['FEMA', 'CALOES', 'CALJPIA'])
    
    if has_2022 and is_disaster:
        project_funding[name] = amount

# Check civic documents for projects mentioned with 2022
disaster_names_from_docs = set()

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find disaster projects in the text
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if not line or '2022' not in line:
            continue
            
        # Check if this line mentions a disaster project
        if any(kw in line.upper() for kw in ['FEMA', 'CALOES', 'CALJPIA']):
            # Try to extract the project name before any parentheses
            name_match = re.match(r'([A-Z][^\(]*)', line)
            if name_match:
                base_name = name_match.group(1).strip()
                if base_name and len(base_name) > 5:
                    # Look for this base name in funding data
                    for fund_item in funding_data:
                        fund_name = fund_item.get('Project_Name', '')
                        fund_amount = int(fund_item.get('Amount', 0))
                        if base_name in fund_name:
                            disaster_names_from_docs.add(fund_name)

# Add projects found in civic docs that have "2022" in their context
additional_projects = {}
for name in disaster_names_from_docs:
    # For now, we can't guarantee they started in 2022, so we'll note them but not count
    # We need to be conservative and only count those we can verify
    pass

# Also check for project 2022 Morning View which clearly started in 2022
for item in funding_data:
    name = item.get('Project_Name', '')
    amount = int(item.get('Amount', 0))
    
    if name == '2022 Morning View Resurfacing & Storm Drain Improvements':
        # Check if disaster-related context exists
        for doc in civic_data:
            text = doc.get('text', '')
            if '2022 Morning View' in text:
                # Check surrounding context for disaster keywords
                context_start = max(0, text.index('2022 Morning View') - 200)
                context_end = min(len(text), text.index('2022 Morning View') + 200)
                context = text[context_start:context_end]
                if 'storm drain' in context.lower():
                    project_funding[name] = amount

final_result = {
    'total_funding': sum(project_funding.values()),
    'project_count': len(project_funding),
    'projects': [{'name': k, 'amount': v} for k, v in project_funding.items()]
}

# If no projects found with direct criteria, let's be more flexible
total = final_result['total_funding']

if total == 0:
    # Try broader search: any project with 2022 that might be disaster-related
    for item in funding_data:
        name = item.get('Project_Name', '')
        amount = int(item.get('Amount', 0))
        
        if '2022' in name and ('storm' in name.lower() or 'drain' in name.lower() or 'repair' in name.lower()):
            project_funding[name] = amount
    
    final_result['total_funding'] = sum(project_funding.values())
    final_result['project_count'] = len(project_funding)
    final_result['projects'] = [{'name': k, 'amount': v} for k, v in project_funding.items()]

print('__RESULT__:')
print(json.dumps(final_result, indent=2))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:24': {'test': 'hello'}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:41': 'file_storage/functions.query_db:41.json', 'var_functions.query_db:52': [], 'var_functions.query_db:54': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Amount': '77000'}], 'var_functions.query_db:55': 'file_storage/functions.query_db:55.json'}

exec(code, env_args)

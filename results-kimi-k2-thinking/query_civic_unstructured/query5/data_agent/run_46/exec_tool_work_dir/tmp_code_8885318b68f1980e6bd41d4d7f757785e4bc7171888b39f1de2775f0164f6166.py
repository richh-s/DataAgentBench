code = """import json
import re

# Access the stored data correctly
funding_data_str = locals()['var_functions.query_db:2']

# Try to parse it as JSON if it's in string format
if isinstance(funding_data_str, str):
    try:
        # Try to parse the string as JSON
        funding_records = json.loads(funding_data_str)
    except:
        # If direct parsing fails, try to evaluate as Python literal
        import ast
        funding_records = ast.literal_eval(funding_data_str)
else:
    funding_records = funding_data_str

print(f"Type: {type(funding_records)}")
print(f"Length: {len(funding_records) if hasattr(funding_records, '__len__') else 'N/A'}")

# Process disaster projects
disaster_funding = 0
disaster_projects = []

for record in funding_records:
    project_name = record.get('Project_Name', '')
    if '(FEMA' in project_name or '(CalOES' in project_name or '(CalJPIA' in project_name:
        amount = int(record.get('Amount', 0))
        disaster_funding += amount
        base_name = project_name.split(' (')[0]
        if base_name not in disaster_projects:
            disaster_projects.append(base_name)

print(f"Total disaster funding: ${disaster_funding:,}")
print(f"Disaster projects: {len(disaster_projects)}")

print('__RESULT__:')
print(json.dumps({
    "total_disaster_funding": disaster_funding,
    "disaster_project_count": len(disaster_projects),
    "sample_projects": disaster_projects[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'status': 'loaded', 'count': 0}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': {'status': 'checked_types'}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:42': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000', 'Funding_Source': 'International Aid'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000', 'Funding_Source': 'Research Institution Funding'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000', 'Funding_Source': 'Government Grant'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000', 'Funding_Source': 'Local NGO Fund'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000', 'Funding_Source': 'Municipal Fund'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000', 'Funding_Source': 'Taxpayer Contribution'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000', 'Funding_Source': 'Local Business Support'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000', 'Funding_Source': 'Cultural Heritage Grant'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000', 'Funding_Source': 'Educational Sponsorship'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000', 'Funding_Source': 'Private Sponsor'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000', 'Funding_Source': 'Impact Investment Fund'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000', 'Funding_Source': 'Development Bank Loan'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000', 'Funding_Source': 'Federal Assistance'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000', 'Funding_Source': 'National Foundation Fund'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000', 'Funding_Source': 'Municipal Fund'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000', 'Funding_Source': 'Community Fund'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000', 'Funding_Source': 'International Aid'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000', 'Funding_Source': 'Environmental Grant'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000', 'Funding_Source': 'State Development Grant'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000', 'Funding_Source': 'Local Business Support'}], 'var_functions.query_db:44': [{'total_funding': '1410000'}], 'var_functions.query_db:46': []}

exec(code, env_args)

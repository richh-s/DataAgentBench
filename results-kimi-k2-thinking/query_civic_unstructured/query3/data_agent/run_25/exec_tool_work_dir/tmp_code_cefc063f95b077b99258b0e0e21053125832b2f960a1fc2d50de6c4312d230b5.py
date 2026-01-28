code = """import json
import os

# Load the extracted projects from civic documents
python_result_key = 'var_functions.execute_python:12'
civic_projects_file = python_result_key

if os.path.exists(civic_projects_file):
    with open(civic_projects_file, 'r') as f:
        civic_projects = json.load(f)
else:
    civic_projects = []

# Load the funding data
funding_result_key = 'var_functions.query_db:14'
funding_records = funding_result_key if isinstance(funding_result_key, list) else []

# If funding_records is a string (file path), load it
if isinstance(funding_result_key, str) and os.path.exists(funding_result_key):
    with open(funding_result_key, 'r') as f:
        funding_records = json.load(f)
else:
    # Try to get from locals
    try:
        funding_records = locals()[funding_result_key]
    except:
        funding_records = []

print(f'Found {len(civic_projects)} civic projects and {len(funding_records)} funding records')

# Build a mapping of project names from civic documents for lookup
civic_projects_map = {}
for proj in civic_projects:
    name = proj.get('Project_Name', '').strip()
    if name:
        civic_projects_map[name] = proj

# Merge funding data with civic project information
merged_results = []

for funding in funding_records:
    fund_name = funding.get('Project_Name', '').strip()
    fund_source = funding.get('Funding_Source', '')
    fund_amount = funding.get('Amount', 0)
    
    # Find matching civic project
    matching_project = None
    
    # Direct match
    if fund_name in civic_projects_map:
        matching_project = civic_projects_map[fund_name]
    else:
        # Fuzzy match - check if any civic project name contains the funding project name or vice versa
        for civic_name, civic_proj in civic_projects_map.items():
            if (fund_name in civic_name) or (civic_name in fund_name):
                matching_project = civic_proj
                break
    
    # Extract status and topic from matching project
    if matching_project:
        status = matching_project.get('status', 'Unknown')
        topic = matching_project.get('topic', '')
    else:
        status = 'Unknown'
        topic = 'FEMA' if 'FEMA' in fund_name else 'emergency' if 'emergency' in fund_name.lower() else ''
    
    merged_results.append({
        'Project_Name': fund_name,
        'Funding_Source': fund_source,
        'Amount': fund_amount,
        'Status': status,
        'Topic': topic
    })

# Sort by amount descending
merged_results.sort(key=lambda x: x['Amount'], reverse=True)

# Format results for display
output_lines = []
output_lines.append("Projects related to 'emergency' or 'FEMA':")
output_lines.append("=" * 80)
output_lines.append("")

for result in merged_results:
    output_lines.append(f"Project: {result['Project_Name']}")
    output_lines.append(f"Funding Source: {result['Funding_Source']}")
    output_lines.append(f"Amount: ${result['Amount']:,}")
    output_lines.append(f"Status: {result['Status']}")
    output_lines.append(f"Topic: {result['Topic']}")
    output_lines.append("-" * 80)
    output_lines.append("")

final_output = "\n".join(output_lines)
print('__RESULT__:')
print(json.dumps(final_output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.query_db:14': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '59', 'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '37000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '99', 'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000'}]}

exec(code, env_args)

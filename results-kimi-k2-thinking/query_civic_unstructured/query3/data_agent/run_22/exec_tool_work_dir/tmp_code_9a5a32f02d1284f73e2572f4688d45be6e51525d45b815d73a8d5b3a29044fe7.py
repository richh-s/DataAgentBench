code = """import json
import re

# Read the FEMA project list
fema_projects = [
    "Birdview Avenue Improvements (FEMA/CalOES Project)",
    "Clover Heights Storm Drain (FEMA Project)", 
    "Corral Canyon Culvert Repairs (FEMA Project)",
    "Corral Canyon Culvert Repairs (FEMA/CalOES Project)",
    "Corral Canyon Road Bridge Repairs (FEMA Project)",
    "Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)",
    "Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)",
    "Guardrail Replacement Citywide (FEMA Project)",
    "Guardrail Replacement Citywide (FEMA/CalOES Project)",
    "Latigo Canyon Road Culvert Repairs (FEMA Project)",
    "Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)",
    "Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)",
    "Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)",
    "Outdoor Warning Sirens (FEMA Project)",
    "Outdoor Warning Sirens (FEMA)",
    "Outdoor Warning Sirens - Design (FEMA Project)",
    "Outdoor Warningn Sirens - Design (FEMA Project)",
    "Storm Drain Master Plan (FEMA Project)",
    "Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)",
    "Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)"
]

# Read the full funding data
funding_file_path = locals()['var_functions.query_db:2']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Create a dictionary for easy lookup
funding_dict = {item['Project_Name']: item for item in funding_data}

# Read the civic documents that mention FEMA
civic_docs_file_path = locals()['var_functions.query_db:16']
with open(civic_docs_file_path, 'r') as f:
    civic_docs = json.load(f)

# Helper function to extract status from text
def extract_status(project_name, text):
    # Common status indicators
    status_patterns = {
        'design': r'\b(design|planning|preliminary design|finalizing plans|working with consultant)\b',
        'construction': r'\b(construction|under construction|construction was completed|construction is completed)\b',
        'completed': r'\b(completed|construction was completed|notice of completion|finished)\b',
        'not started': r'\b(not started|identified|waiting for|pending|delayed)\b'
    }
    
    # Look for the project name in the text
    base_name = project_name.split('(')[0].strip()
    if base_name.lower() in text.lower():
        for status, pattern in status_patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                return status
    return "unknown"

# For each FEMA project, get funding info and try to find status
results = []
for project in fema_projects:
    # Get funding info
    funding_info = funding_dict.get(project, {})
    
    # Try to find status in civic documents
    status = "unknown"
    for doc in civic_docs:
        extracted_status = extract_status(project, doc['text'])
        if extracted_status != "unknown":
            status = extracted_status
            break
    
    results.append({
        'Project_Name': project,
        'Funding_Source': funding_info.get('Funding_Source', 'Not found'),
        'Amount': int(funding_info.get('Amount', 0)) if funding_info.get('Amount') else 'Not found',
        'Status': status
    })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000}], 'var_functions.execute_python:14': ['Birdview Avenue Improvements (FEMA/CalOES Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Guardrail Replacement Citywide (FEMA Project)', 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Outdoor Warning Sirens (FEMA Project)', 'Outdoor Warning Sirens (FEMA)', 'Outdoor Warning Sirens - Design (FEMA Project)', 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Storm Drain Master Plan (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)

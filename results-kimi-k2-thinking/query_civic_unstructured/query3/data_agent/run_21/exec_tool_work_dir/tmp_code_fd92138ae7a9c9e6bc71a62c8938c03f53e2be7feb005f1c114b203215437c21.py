code = """import json
import re

# Load the filtered funding data
funding_data = var_functions.query_db:5

# Load civic documents from the file path
civic_docs_path = var_functions.query_db:0
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Create a mapping of base project names to their statuses
project_status_map = {}

# Combine all civic document texts for searching
all_civic_text = "\n\n".join([doc.get('text', '') for doc in civic_docs])

# Function to find project status in text
def find_project_status(project_name, text):
    # Extract base name (without suffixes like (FEMA Project))
    base_name = project_name.split(' (')[0].strip()
    
    # Find the section about this project
    # Look for the project name and capture surrounding context
    pattern = rf"({re.escape(base_name)}.*?)(?=\n\s*\n|\Z)"
    matches = re.findall(pattern, text, re.DOTALL | re.IGNORECASE)
    
    if not matches:
        return None
    
    # Use the first match (most relevant)
    project_section = matches[0]
    
    # Determine status based on keywords
    section_lower = project_section.lower()
    
    if any(keyword in section_lower for keyword in ['completed', 'notice of completion', 'construction was completed']):
        return 'completed'
    elif any(keyword in section_lower for keyword in ['under construction', 'construction is currently', 'project is currently under construction']):
        return 'construction'
    elif any(keyword in section_lower for keyword in ['design:', 'complete design', 'design is', 'design plans', 'finalizing design']):
        return 'design'
    elif any(keyword in section_lower for keyword in ['not started', 'identified but not begun', 'will be identified']):
        return 'not started'
    
    return None

# Analyze each funding project
results = []

for funding in funding_data:
    project_name = funding['Project_Name']
    funding_source = funding['Funding_Source']
    amount = int(funding['Amount'])
    
    # Find status for this project
    status = find_project_status(project_name, all_civic_text)
    
    # Determine type (all these are disaster/FEMA projects)
    project_type = 'Disaster Recovery'
    
    results.append({
        'Project_Name': project_name,
        'Funding_Source': funding_source,
        'Amount': f"${amount:,}",
        'Status': status if status else 'Status not found in civic documents',
        'Type': project_type
    })

# Sort by project name
results = sorted(results, key=lambda x: x['Project_Name'])

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_functions.execute_python:8': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '$14,000', 'Status': 'Not specified in documents', 'Project_Type': 'disaster'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '$21,000', 'Status': 'Not specified in documents', 'Project_Type': 'disaster'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '$43,000', 'Status': 'Not specified in documents', 'Project_Type': 'disaster'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '$15,000', 'Status': 'Not specified in documents', 'Project_Type': 'disaster'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '$25,000', 'Status': 'Not specified in documents', 'Project_Type': 'disaster'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '$58,000', 'Status': 'Not specified in documents', 'Project_Type': 'disaster'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '$94,000', 'Status': 'Not specified in documents', 'Project_Type': 'disaster'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '$22,000', 'Status': 'Not specified in documents', 'Project_Type': 'disaster'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '$45,000', 'Status': 'Not specified in documents', 'Project_Type': 'disaster'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '$36,000', 'Status': 'Not specified in documents', 'Project_Type': 'disaster'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '$44,000', 'Status': 'Not specified in documents', 'Project_Type': 'disaster'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '$91,000', 'Status': 'Not specified in documents', 'Project_Type': 'disaster'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '$78,000', 'Status': 'Not specified in documents', 'Project_Type': 'disaster'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '$27,000', 'Status': 'Not specified in documents', 'Project_Type': 'disaster'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '$81,000', 'Status': 'Not specified in documents', 'Project_Type': 'disaster'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '$43,000', 'Status': 'Not specified in documents', 'Project_Type': 'disaster'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '$84,000', 'Status': 'Not specified in documents', 'Project_Type': 'disaster'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '$80,000', 'Status': 'Not specified in documents', 'Project_Type': 'disaster'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '$44,000', 'Status': 'Not specified in documents', 'Project_Type': 'disaster'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '$92,000', 'Status': 'Not specified in documents', 'Project_Type': 'disaster'}]}

exec(code, env_args)

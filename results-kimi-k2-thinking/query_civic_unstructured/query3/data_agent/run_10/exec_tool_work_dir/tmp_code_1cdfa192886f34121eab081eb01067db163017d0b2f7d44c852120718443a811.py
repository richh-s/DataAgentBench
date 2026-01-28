code = """import json
import re

# Load data
funding_data = locals()["var_functions.query_db:0"]
civic_docs_data = locals()["var_functions.query_db:4"]

# If they're file paths, load them
if isinstance(funding_data, str):
    with open(funding_data) as f:
        funding_data = json.load(f)
if isinstance(civic_docs_data, str):
    with open(civic_docs_data) as f:
        civic_docs_data = json.load(f)

print(f"Funding records: {len(funding_data)}")
print(f"Civic docs: {len(civic_docs_data)}")

# Extract projects with emergency/FEMA from civic docs
projects_from_docs = []

for doc in civic_docs_data:
    text = doc['text']
    
    # Look for project sections - they often start with project names in a specific format
    # Split by common project indicators
    sections = re.split(r'\n\s*(?=[A-Z][a-zA-Z\s&]+(?:\n|$))', text)
    
    for section in sections:
        section_lower = section.lower()
        if 'emergency' in section_lower or 'fema' in section_lower:
            # Try to extract project name (usually first line)
            lines = section.strip().split('\n')
            if lines:
                project_name = lines[0].strip()
                # Clean up project name
                project_name = re.sub(r'^[\d\s\.]+', '', project_name)
                project_name = re.sub(r'[\t]', ' ', project_name)
                project_name = project_name.strip()
                
                # Skip if it's just a header or too short
                if len(project_name) > 10 and 'commission' not in project_name.lower():
                    # Determine status from text
                    status = 'unknown'
                    if 'design' in section_lower and ('complete design' in section_lower or 'final design' in section_lower):
                        status = 'design'
                    elif 'construction' in section_lower:
                        if 'complete construction' in section_lower or 'construction was completed' in section_lower:
                            status = 'completed'
                        else:
                            status = 'construction'
                    elif 'not started' in section_lower:
                        status = 'not started'
                    elif 'advertise' in section_lower:
                        status = 'design'
                    
                    # Determine type
                    project_type = 'disaster' if 'fema' in section_lower or 'emergency' in section_lower else 'capital'
                    
                    projects_from_docs.append({
                        'Project_Name': project_name,
                        'status': status,
                        'type': project_type,
                        'source_doc': doc['filename']
                    })

print(f"\nProjects extracted from civic docs: {len(projects_from_docs)}")
for i, proj in enumerate(projects_from_docs[:10]):
    print(f"  {i+1}. {proj['Project_Name']} - {proj['status']} - {proj['type']}")

# Get projects with FEMA/emergency in name from funding data
funding_matches = []
for record in funding_data:
    name_lower = record['Project_Name'].lower()
    if 'emergency' in name_lower or 'fema' in name_lower:
        funding_matches.append(record)

print(f"\nDirect funding matches: {len(funding_matches)}")

# Merge funding data with status information
final_results = []

for funding_record in funding_matches:
    project_name = funding_record['Project_Name']
    
    # Look for matching project in civic docs
    matched_status = 'unknown'
    for doc_proj in projects_from_docs:
        doc_name = doc_proj['Project_Name']
        # Check if they're similar (funding name contains doc name or vice versa)
        if (project_name.lower() in doc_name.lower() or 
            doc_name.lower() in project_name.lower() or
            any(word in project_name.lower() for word in doc_name.lower().split() if len(word) > 5)):
            matched_status = doc_proj['status']
            break
    
    final_results.append({
        'Project_Name': project_name,
        'Funding_Source': funding_record['Funding_Source'],
        'Amount': funding_record['Amount'],
        'Status': matched_status
    })

print(f"\nFinal results count: {len(final_results)}")
for i, result in enumerate(final_results):
    print(f"  {i+1}. {result['Project_Name']}")
    print(f"     Funding: {result['Funding_Source']} - ${result['Amount']}")
    print(f"     Status: {result['Status']}")

result_json = json.dumps(final_results, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)

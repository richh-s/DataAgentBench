code = """import json
import re

# Read the civic documents file
with open('var_functions.query_db:42', 'r') as f:
    civic_docs = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents")

# Extract project information from documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project patterns in the text
    # Projects often appear with bullet points or specific headings
    
    # Find project names and their details
    # Pattern: Project name followed by updates and schedule
    project_blocks = re.findall(r'([^\\n]+?)\\n\\(cid:190\\) Updates:(.*?)(?=(?:\\n\\n|$))', text, re.DOTALL)
    
    for proj_info in project_blocks:
        proj_name = proj_info[0].strip()
        if proj_name and len(proj_name) < 200:  # Filter out obviously invalid names
            
            # Extract schedule information if available
            schedule_match = re.search(r'Project Schedule:.*?\\n(?:.*?\\n)*?(?=\\n|$)', text[text.find(proj_name):], re.DOTALL)
            schedule_text = schedule_match.group(0) if schedule_match else ''
            
            # Determine project type (disaster vs capital)
            is_disaster = any(keyword in proj_name.lower() for keyword in ['fema', 'caloes', 'caljpia', 'disaster', 'emergency', 'fire', 'recovery'])
            
            # Extract dates - look for 2022 specifically
            has_2022 = '2022' in schedule_text or '2022' in proj_name
            
            # Extract status
            status = 'unknown'
            if 'design' in schedule_text.lower() or 'complete design' in schedule_text.lower():
                status = 'design'
            elif 'construction' in schedule_text.lower() or 'complete construction' in schedule_text.lower():
                status = 'construction'
            elif 'not started' in schedule_text.lower():
                status = 'not started'
            
            projects.append({
                'project_name': proj_name,
                'is_disaster': is_disaster,
                'has_2022': has_2022,
                'status': status,
                'schedule_text': schedule_text[:200],  # Limit length
                'filename': filename
            })

# Filter for disaster projects that have 2022 in their dates
 disaster_projects_2022 = [p for p in projects if p['is_disaster'] and p['has_2022']]

print(f"Found {len(disaster_projects_2022)} disaster projects with 2022 dates")
print("\\nSample disaster projects with 2022:")
for proj in disaster_projects_2022[:10]:
    print(f"  - {proj['project_name']}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:14': [{'count': '500'}], 'var_functions.execute_python:18': {'available_variables': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.list_db:4', 'var_functions.query_db:6', 'var_functions.query_db:14', '__builtins__', 'json', 're']}, 'var_functions.execute_python:22': {'civic_data_type': "<class 'NoneType'>", 'funding_data_type': "<class 'NoneType'>", 'civic_data_preview': 'None', 'funding_data_preview': 'None'}, 'var_functions.query_db:24': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '59', 'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '37000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '99', 'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)

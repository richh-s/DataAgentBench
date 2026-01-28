code = """import json
import re

# Get file path from storage
file_info = globals()['var_functions.query_db:2']
print('File path type:', type(file_info))
print('File path value:', str(file_info)[:100])

# Load the JSON data
with open(file_info, 'r') as f:
    civic_docs = json.load(f)

print('Documents loaded:', len(civic_docs))

# Extract projects
projects = []
for doc in civic_docs:
    if 'text' in doc:
        text = doc['text']
        filename = doc.get('filename', '')
        
        # Check for emergency/FEMA keywords
        low_text = text.lower()
        if 'emergency' in low_text or 'fema' in low_text or 'fire' in low_text:
            
            # Find project names - look for lines that are likely project titles
            lines = text.split('\n')
            for i, line in enumerate(lines):
                line = line.strip()
                if line and 10 < len(line) < 80:
                    # Check if next lines contain project indicators
                    next_text = ' '.join(lines[i:i+15])
                    if 'Updates:' in next_text or 'Project Schedule:' in next_text:
                        
                        # Determine details
                        ptype = 'disaster' if 'FEMA' in text else 'capital'
                        status = 'design'
                        if 'completed' in next_text.lower():
                            status = 'completed'
                        elif 'construction' in next_text.lower():
                            status = 'construction'
                        
                        # Get topics
                        topics = []
                        if 'emergency' in low_text:
                            topics.append('emergency')
                        if 'FEMA' in text:
                            topics.append('FEMA')
                        if 'fire' in low_text:
                            topics.append('fire')
                        
                        if topics:
                            projects.append({
                                'Project_Name': line,
                                'topic': ','.join(topics),
                                'type': ptype,
                                'status': status,
                                'source_file': filename
                            })

# Remove duplicates
seen = set()
unique_projects = []
for p in projects:
    if p['Project_Name'] not in seen:
        seen.add(p['Project_Name'])
        unique_projects.append(p)

print('Unique projects found:', len(unique_projects))

# Create result
result = {'projects': unique_projects, 'count': len(unique_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.execute_python:16': {'test': 'data'}, 'var_functions.query_db:18': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)

code = """import json
import re

# Read the full results from the stored JSON files
with open('file_storage/functions.query_db:0.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:2.json', 'r') as f:
    civic_docs_data = json.load(f)

# Step 1: Identify all emergency/FEMA related funding records
emergency_fema_funding = []

for record in funding_data:
    project_name = record.get('Project_Name', '')
    funding_source = record.get('Funding_Source', '')
    
    project_name_lower = project_name.lower()
    funding_source_lower = funding_source.lower()
    
    # Check for emergency/FEMA indicators
    if (any(keyword in project_name_lower for keyword in ['emergency', 'fema']) or
        any(keyword in funding_source_lower for keyword in ['emergency', 'fema']) or
        any(suffix in project_name_lower for suffix in ['(fema project)', '(caloes project)', '(caljpia project)'])):
        emergency_fema_funding.append(record)

# Step 2: Create a comprehensive list from all sources
all_projects = []
processed_project_names = set()

# Process funding records
for funding_record in emergency_fema_funding:
    project_name = funding_record['Project_Name']
    if project_name.lower() not in processed_project_names:
        processed_project_names.add(project_name.lower())
        
        # Initialize project info
        project_info = {
            'Project_Name': project_name,
            'Funding_Source': funding_record['Funding_Source'],
            'Amount': int(funding_record['Amount']),
            'Status': 'Unknown',
            'Topic': 'Unknown',
            'Type': 'Unknown'
        }
        
        # Determine type from project name
        name_lower = project_name.lower()
        if 'fema' in name_lower or 'disaster' in name_lower or any(suffix in name_lower for suffix in ['(fema project)', '(caloes project)', '(caljpia project)']):
            project_info['Type'] = 'disaster'
        elif 'capital' in name_lower:
            project_info['Type'] = 'capital'
        
        # Determine topic from project name
        if 'storm' in name_lower or 'drain' in name_lower:
            project_info['Topic'] = 'storm drain'
        elif 'road' in name_lower or 'street' in name_lower or 'highway' in name_lower:
            project_info['Topic'] = 'road'
        elif 'siren' in name_lower or 'warning' in name_lower:
            project_info['Topic'] = 'emergency warning'
        elif 'bridge' in name_lower or 'culvert' in name_lower:
            project_info['Topic'] = 'bridge'
        elif 'park' in name_lower or 'playground' in name_lower:
            project_info['Topic'] = 'park'
        elif 'slope' in name_lower:
            project_info['Topic'] = 'slope repair'
        elif 'water' in name_lower:
            project_info['Topic'] = 'water infrastructure'
        
        all_projects.append(project_info)

# Step 3: Extract project statuses from civic documents
all_doc_text_combined = '\\n\\n'.join([doc.get('text', '') for doc in civic_docs_data])
all_doc_text_lower = all_doc_text_combined.lower()

# Update statuses based on document mentions
for project in all_projects:
    project_name_lower = project['Project_Name'].lower()
    
    # Look for the project in documents
    try:
        pattern = re.escape(project_name_lower)
        matches = list(re.finditer(pattern, all_doc_text_lower, re.IGNORECASE))
        
        if matches:
            for match in matches:
                start_pos = max(0, match.start() - 300)
                end_pos = min(len(all_doc_text_lower), match.end() + 300)
                context = all_doc_text_lower[start_pos:end_pos]
                
                if 'completed' in context or 'notice of completion' in context:
                    project['Status'] = 'completed'
                    break
                elif 'construction' in context or 'under construction' in context:
                    project['Status'] = 'construction'
                    break
                elif 'design' in context or 'final design' in context:
                    project['Status'] = 'design'
                    break
                elif 'advertise' in context or 'bids' in context:
                    project['Status'] = 'bidding'
                    break
                else:
                    project['Status'] = 'mentioned'
    except:
        pass

# Sort by project name
all_projects.sort(key=lambda x: x['Project_Name'])

# Create final output
final_output = {
    'projects': all_projects,
    'total_count': len(all_projects),
    'total_funding_amount': sum(p['Amount'] for p in all_projects)
}

result_json = json.dumps(final_output, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_result_type': "<class 'str'>", 'civic_docs_result_type': "<class 'str'>", 'funding_result_preview': 'file_storage/functions.query_db:0.json', 'civic_docs_result_preview': 'file_storage/functions.query_db:2.json'}, 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:24': {'projects': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000, 'Status': 'completed', 'Topic': 'infrastructure', 'Type': 'capital'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000, 'Status': 'construction', 'Topic': 'infrastructure', 'Type': 'disaster'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 81000, 'Status': 'design', 'Topic': 'road', 'Type': 'disaster'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000, 'Status': 'construction', 'Topic': 'storm drain', 'Type': 'disaster'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000, 'Status': 'mentioned', 'Topic': 'bridge', 'Type': 'disaster'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000, 'Status': 'mentioned', 'Topic': 'bridge', 'Type': 'disaster'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000, 'Status': 'design', 'Topic': 'road', 'Type': 'disaster'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000, 'Status': 'mentioned', 'Topic': 'road', 'Type': 'disaster'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': 18000, 'Status': 'construction', 'Topic': 'storm drain', 'Type': 'capital'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000, 'Status': 'construction', 'Topic': 'storm drain', 'Type': 'disaster'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000, 'Status': 'design', 'Topic': 'infrastructure', 'Type': 'disaster'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000, 'Status': 'completed', 'Topic': 'infrastructure', 'Type': 'disaster'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000, 'Status': 'design', 'Topic': 'road', 'Type': 'disaster'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000, 'Status': 'construction', 'Topic': 'road', 'Type': 'disaster'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000, 'Status': 'construction', 'Topic': 'road', 'Type': 'disaster'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000, 'Status': 'construction', 'Topic': 'road', 'Type': 'disaster'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 37000, 'Status': 'design', 'Topic': 'road', 'Type': 'disaster'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000, 'Status': 'construction', 'Topic': 'emergency warning', 'Type': 'disaster'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000, 'Status': 'construction', 'Topic': 'emergency warning', 'Type': 'disaster'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000, 'Status': 'construction', 'Topic': 'emergency warning', 'Type': 'disaster'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000, 'Status': 'construction', 'Topic': 'emergency warning', 'Type': 'disaster'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000, 'Status': 'construction', 'Topic': 'storm drain', 'Type': 'disaster'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000, 'Status': 'construction', 'Topic': 'park', 'Type': 'disaster'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000, 'Status': 'construction', 'Topic': 'park', 'Type': 'disaster'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 43000, 'Status': 'construction', 'Topic': 'park', 'Type': 'capital'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': 32000, 'Status': 'construction', 'Topic': 'park', 'Type': 'capital'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': 77000, 'Status': 'completed', 'Topic': 'road', 'Type': 'disaster'}], 'total_projects': 27, 'total_funding': 1410000}}

exec(code, env_args)

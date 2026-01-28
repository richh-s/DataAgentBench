code = """import json

# Load funding data
f_path = locals()['var_functions.query_db:10']
with open(f_path) as f:
    all_funding = json.load(f)

for r in all_funding:
    r['Amount'] = int(r['Amount'])

# Filter to only disaster-related funding
disaster_funding = [
    f for f in all_funding 
    if '(FEMA' in f['Project_Name'] or '(CalOES' in f['Project_Name'] or '(CalJPIA' in f['Project_Name']
]

# Load 2022 documents  
docs_path = locals()['var_functions.query_db:36']
with open(docs_path) as f:
    docs = json.load(f)

# More precise check for 2022 start dates
import re

matching_funds = []
for fund in disaster_funding:
    proj_name = fund['Project_Name']
    base_name = proj_name.split(' (')[0].strip()
    
    for doc in docs:
        text = doc['text']
        
        # Check if project is mentioned
        if base_name in text:
            # Look for 2022 start indicators near the project mention
            # Split by lines to find where the project is mentioned
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if base_name in line:
                    # Check surrounding lines for 2022 schedule info
                    start = max(0, i-5)
                    end = min(len(lines), i+10)
                    context = '\n'.join(lines[start:end]).lower()
                    
                    # Look for schedule indicators with 2022
                    schedule_patterns = [
                        r'begin.*2022',
                        r'start.*2022', 
                        r'advertise.*2022',
                        r'complete design.*2022',
                        r'construction.*2022',
                        r'spring 2022',
                        r'summer 2022',
                        r'fall 2022',
                        r'winter 2022'
                    ]
                    
                    if any(re.search(pattern, context) for pattern in schedule_patterns):
                        matching_funds.append(fund)
                        break
            
            # Also check if there's a standalone 2022 schedule section
            if '2022' in text:
                # Look for project in sections with year headers
                year_sections = re.split(r'\n\s*\n', text)
                for section in year_sections:
                    if base_name in section and '2022' in section:
                        # Check if this section has schedule language
                        section_lower = section.lower()
                        schedule_words = ['schedule', 'begin', 'start', 'advertise', 'construction']
                        if any(word in section_lower for word in schedule_words):
                            if fund not in matching_funds:
                                matching_funds.append(fund)
                            break

# Remove duplicates
unique_funds = []
seen_ids = set()
for f in matching_funds:
    if f['Funding_ID'] not in seen_ids:
        unique_funds.append(f)
        seen_ids.add(f['Funding_ID'])

total_amount = sum(f['Amount'] for f in unique_funds)

result = {
    'total_disaster_funding_2022': total_amount,
    'matching_projects': len(unique_funds),
    'project_names': [f['Project_Name'] for f in unique_funds]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'count': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_text': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'funding_count': 500, 'docs_count': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'sample_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:24': {'fund_count': 500, 'doc_count': 5}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:52': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '59', 'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '37000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '99', 'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000'}], 'var_functions.execute_python:58': {'matching_projects': 26, 'total_funding': 1367000}}

exec(code, env_args)

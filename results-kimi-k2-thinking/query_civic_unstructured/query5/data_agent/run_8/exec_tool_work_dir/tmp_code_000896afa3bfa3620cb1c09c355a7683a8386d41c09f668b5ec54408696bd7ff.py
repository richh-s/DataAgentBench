code = """import json
import pandas as pd
import re

# Read civic documents file
civic_docs_file = locals()['var_functions.query_db:2']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Read funding data
funding_data = locals()['var_functions.query_db:0']
funding_df = pd.DataFrame(funding_data)

# Initialize list for project data
projects_data = []

# Process all documents
for doc in civic_docs[:5]:  # Process fewer docs for debugging
    text = doc['text']
    filename = doc['filename']
    
    # Simple extraction - look for FEMA/disaster keywords
    if 'FEMA' in text or 'CalOES' in text or 'disaster' in text.lower():
        # Extract lines that mention these
        for line in text.split('\n'):
            if any(keyword in line for keyword in ['FEMA', 'CalOES', 'Disaster', 'disaster']):
                proj_info = {
                    'Project_Name': line.strip()[:200],
                    'topic': 'disaster',
                    'type': 'disaster',
                    'status': '',
                    'st': '',
                    'et': '',
                    'source_file': filename
                }
                
                # Check for 2022 dates
                if '2022' in line:
                    if any(word in line.lower() for word in ['start', 'begin', 'advertise']):
                        proj_info['st'] = '2022'
                    elif any(word in line.lower() for word in ['complete', 'end', 'finish']):
                        proj_info['et'] = '2022'
                
                projects_data.append(proj_info)

projects_df = pd.DataFrame(projects_data)
print('Projects found:', len(projects_df))
print(projects_df.head() if not projects_df.empty else 'No projects')

# Convert amount to numeric
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

result = {
    'project_count': len(projects_df),
    'sample_projects': projects_df.head(3).to_dict('records') if not projects_df.empty else []
}

__RESULT__: json.dumps(result)"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

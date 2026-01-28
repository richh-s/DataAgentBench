code = """import json
import re

# Read the civic documents data
civic_docs_path = locals()['var_functions.query_db:0']
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

# Function to extract project information from civic documents
def extract_projects_with_2022_completion(docs):
    projects_2022 = []
    
    for doc in docs:
        text = doc.get('text', '')
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            
            # Look for project names (heuristic: lines that are relatively short and don't start with common patterns)
            if (len(line) < 100 and 
                not line.startswith('Public Works') and 
                not line.startswith('Capital Improvement') and
                not line.startswith('Disaster Recovery') and
                not line.startswith('RECOMMENDED') and
                not line.startswith('DISCUSSION') and
                not line.startswith('To:') and
                not line.startswith('Prepared') and
                not line.startswith('Approved') and
                not line.startswith('Date') and
                not line.startswith('Meeting') and
                not line.startswith('Subject:') and
                not line.startswith('Page') and
                not line.startswith('Agenda Item')):
                
                # Check if this line and the following lines contain 2022 completion
                segment = '\n'.join(lines[i:i+10])
                if '2022' in segment and ('completed' in segment.lower() or 'construction was completed' in segment.lower()):
                    # Check if park-related
                    if 'park' in segment.lower():
                        # Extract completion date
                        et_match = re.search(r'(?:completed|construction was completed)[\s,]*([A-Za-z\d\-\s,]+2022[A-Za-z\d\-\s,]*)', segment, re.IGNORECASE)
                        et = et_match.group(1).strip() if et_match else '2022'
                        
                        projects_2022.append({
                            'Project_Name': line,
                            'topic': 'park',
                            'status': 'completed',
                            'et': et
                        })
    
    return projects_2022

# Extract park projects completed in 2022
park_projects_2022 = extract_projects_with_2022_completion(civic_docs_data)

print('__RESULT__:')
print(json.dumps({
    'park_projects_2022_from_docs': park_projects_2022,
    'count': len(park_projects_2022)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.execute_python:12': {'park_funding_projects_count': 20, 'sample_park_projects': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Funding_ID': '51', 'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Funding_ID': '52', 'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Funding_ID': '53', 'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Funding_ID': '55', 'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Funding_ID': '56', 'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Funding_ID': '57', 'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}]}}

exec(code, env_args)

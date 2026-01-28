code = """import json
import re

# Read the civic docs data from the stored file
civic_docs_file = locals()['var_functions.query_db:0']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Read the funding data from the stored file
funding_file = locals()['var_functions.query_db:2']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Find disaster-related projects that reference 2022
disaster_indicators = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'fire', 'emergency', 'recovery', 'Woolsey']
disaster_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text:
        # Check if this document contains disaster-related content
        if any(indicator in text for indicator in disaster_indicators):
            # Look for project names in the document
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                # Heuristic: project names are typically longer than 15 chars and not bullet points
                if len(line) > 15 and not line.startswith('•') and not line.startswith('('):
                    if any(keyword in line.lower() for keyword in ['project', 'improvements', 'repairs', 'replacement']):
                        disaster_projects_2022.append(line)

# Calculate total funding for disaster projects (with any 2022 reference)
total_funding = 0
funded_count = 0

for funding in funding_data:
    fund_project_name = funding.get('Project_Name', '')
    amount = int(funding.get('Amount', 0))
    
    # Check if this is a disaster project by name
    is_disaster = False
    
    # Direct indicators in project name
    for indicator in disaster_indicators:
        if indicator in fund_project_name:
            is_disaster = True
            break
    
    # Additional check for base project names without indicators
    if not is_disaster:
        # Map common base names
        base_projects = [
            'Encinal Canyon Road Drainage Improvements',
            'Corral Canyon Culvert Repairs',
            'Clover Heights Storm Drain',
            'Latigo Canyon Road',
            'Outdoor Warning Sirens',
            'Guardrail Replacement Citywide',
            'Broad Beach Road Water Quality',
            'Malibu Road Slope Repairs'
        ]
        for base in base_projects:
            if base in fund_project_name:
                is_disaster = True
                break
    
    if is_disaster:
        total_funding += amount
        funded_count += 1

result = {
    'total_funding': total_funding,
    'funded_projects_count': funded_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

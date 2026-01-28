code = """import json
import pandas as pd

# Load funding data
funding_path = locals()['var_functions.query_db:22']
if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_path

# Load civic documents
civic_path = locals()['var_functions.query_db:20']
if isinstance(civic_path, str) and civic_path.endswith('.json'):
    with open(civic_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_path

# Create funding DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

print(f"Total funding records: {len(funding_df)}")
print(f"Funding range: ${funding_df['Amount'].min()} - ${funding_df['Amount'].max()}")

# Extract capital projects with design status from civic documents
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Find the Capital Improvement Projects (Design) section
    import re
    
    # Look for the section header
    design_section_pattern = r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Disaster Recovery Projects|$)'
    design_match = re.search(design_section_pattern, text, re.DOTALL | re.IGNORECASE)
    
    if design_match:
        design_section = design_match.group(1)
        
        # Split into lines and process
        lines = design_section.split('\n')
        current_project = None
        
        for line in lines:
            line = line.strip()
            if not line or len(line) < 5:
                continue
            
            # Skip lines with markers that aren't project names
            if (line.startswith('(') or 
                line.startswith('•') or 
                line.startswith('-') or
                line.startswith('▪') or
                'cid:' in line or
                line.isupper() or
                line.lower().startswith('page') or
                'PROJECTS' in line.upper()):
                continue
            
            # Skip schedule/update lines
            lower_line = line.lower()
            skip_terms = ['updates:', 'project schedule:', 'complete design:', 'advertise:', 'begin construction:', 'project description:', 'estimated schedule:', 'complete construction:', 'project updates:']
            if any(term in lower_line for term in skip_terms):
                continue
            
            # Skip status labels and header/footer content
            if line.lower() in ['design', 'construction', 'not started']:
                continue
                
            skip_phrases = ['public works', 'commission', 'agenda', 'report', 'meeting', 'prepared by', 'approved by', 'subject', 'date prepared']
            if any(phrase in line.lower() for phrase in skip_phrases):
                continue
            
            # Skip dates and short numeric lines
            if any(char.isdigit() for char in line) and len(line) < 15:
                continue
            
            # Clean up line
            project_name = line
            for prefix in ['·', '•', '-', '▪']:
                if project_name.startswith(prefix):
                    project_name = project_name[1:].strip()
            
            # This looks like a project name
            current_project = project_name
            
            # Add to list
            capital_design_projects.append({
                'Project_Name': project_name,
                'status': 'design',
                'type': 'capital'
            })

# Remove duplicates
capital_design_df = pd.DataFrame(capital_design_projects)
capital_design_df = capital_design_df.drop_duplicates(subset=['Project_Name'])

print(f"\nCapital projects with design status: {len(capital_design_df)}")
print("Projects:")
for _, proj in capital_design_df.head(15).iterrows():
    print(f"  - {proj['Project_Name']}")

# Merge with funding data
merged_df = capital_design_df.merge(
    funding_df[['Project_Name', 'Amount']], 
    on='Project_Name', 
    how='inner'
)

print(f"\nProjects with funding data: {len(merged_df)}")

# Filter for funding > 50000
high_funding_df = merged_df[merged_df['Amount'] > 50000]

print(f"\nCapital design projects with funding > $50,000: {len(high_funding_df)}")
if len(high_funding_df) > 0:
    print("\nProjects meeting criteria:")
    for _, proj in high_funding_df.iterrows():
        print(f"  - {proj['Project_Name']}: ${proj['Amount']}")

# Result to return
result_count = len(high_funding_df)
result = json.dumps({"count": result_count, "projects": high_funding_df.to_dict('records')})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:18': ['Funding'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)

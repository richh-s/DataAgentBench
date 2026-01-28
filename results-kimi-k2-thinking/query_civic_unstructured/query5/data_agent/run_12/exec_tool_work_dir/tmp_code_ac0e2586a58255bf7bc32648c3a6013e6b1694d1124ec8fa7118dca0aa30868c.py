code = """import json
import pandas as pd
import re

# Load funding data
with open(locals()['var_functions.query_db:5'], 'r') as f:
    funding_data = json.load(f)

# Load civic documents
with open(locals()['var_functions.query_db:0'], 'r') as f:
    civic_data = json.load(f)

# Parse civic documents to find disaster projects with 2022 dates
project_names_2022 = []

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for project headers and associated information
    current_project = None
    
    for line_num, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) > 200:
            continue
        
        # Detect project title lines
        if any(keyword in line.lower() for keyword in ['project', 'repair', 'improvement']) and \
           not any(line.startswith(x) for x in ['(', '•', '-', '●']):
            current_project = line
        
        # Check if current project mentions disaster/FEMA and 2022
        if current_project:
            # Look for 2022 in nearby lines (within next 5 lines)
            search_window = '\n'.join(lines[line_num:min(line_num+5, len(lines))])
            
            has_disaster = bool(re.search(r'FEMA|Cal\.?OES|CalJPIA|disaster|recovery', search_window, re.IGNORECASE))
            has_2022 = '2022' in search_window
            
            if has_disaster and has_2022:
                clean_name = current_project.split('(')[0].strip()
                if clean_name not in project_names_2022 and len(clean_name) > 10:
                    project_names_2022.append(clean_name)

# Process funding data
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce').fillna(0).astype(int)

# Filter to disaster-related funding only
all_disaster_projects = funding_df[funding_df['Project_Name'].str.contains('FEMA|Cal\.?OES|CalJPIA|disaster|recovery', case=False, na=False)]

# Find exact matches for disaster projects that started in 2022
matched_funding = 0
matched_names = []

# Check projects with 2022 in the name
direct_2022 = all_disaster_projects[all_disaster_projects['Project_Name'].str.contains('2022', case=False, na=False)]
if not direct_2022.empty:
    matched_funding += direct_2022['Amount'].sum()
    matched_names.extend(direct_2022['Project_Name'].tolist())

# Check against extracted project names
for clean_name in project_names_2022:
    for _, row in all_disaster_projects.iterrows():
        fund_name = row['Project_Name']
        if fund_name in matched_names:
            continue
        
        fund_clean = fund_name.split('(')[0].strip()
        
        # Use matching heuristics
        name_words = set(clean_name.lower().replace('/',' ').replace('-',' ').split())
        fund_words = set(fund_clean.lower().replace('/',' ').replace('-',' ').split())
        
        # Check if they share important words (exclude common words)
        common_words = {'project', 'repair', 'improvement', 'replacement', 'road', 'canyon', 'storm', 'drain'}
        name_key = name_words - common_words
        fund_key = fund_words - common_words
        
        # Match if they share most key words
        if len(name_key) > 0 and len(fund_key) > 0:
            overlap = name_key & fund_key
            if len(overlap) >= min(len(name_key), len(fund_key)) * 0.6:  # 60% overlap
                matched_funding += row['Amount']
                matched_names.append(fund_name)

result = {
    'total_funding_2022': int(matched_funding),
    'num_projects': len(matched_names),
    'sample_projects': matched_names[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'total_funding_2022': 0, 'total_disaster_funding': 1410000, 'disaster_2022_projects_count': 0}, 'var_functions.execute_python:22': {'total_funding_2022': 0, 'project_count': 0}, 'var_functions.execute_python:26': 0}

exec(code, env_args)

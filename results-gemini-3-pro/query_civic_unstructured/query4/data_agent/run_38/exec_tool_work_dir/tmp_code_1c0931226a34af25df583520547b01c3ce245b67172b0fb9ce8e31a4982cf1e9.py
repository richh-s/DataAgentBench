code = """import json
import pandas as pd
import re

# Load funding data
funding_path = locals()['var_function-call-11668788458618260347']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

# Load civic docs
civic_path = locals()['var_function-call-11668788458618261250']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

extracted_projects = []

def parse_date(date_str):
    if not date_str:
        return None
    date_str = date_str.lower().strip()
    # Check for Spring 2022
    if 'spring 2022' in date_str or '2022-spring' in date_str:
        return 'Spring 2022'
    # Check for months
    if '2022' in date_str:
        if any(m in date_str for m in ['march', 'april', 'may', 'mar', 'apr', 'may']):
            return 'Spring 2022'
        # Check numeric 2022-03 etc
        if re.search(r'2022-(03|04|05)', date_str):
             return 'Spring 2022'
        if re.search(r'(03|04|05)/2022', date_str):
             return 'Spring 2022'
    return date_str # Return original if no match, or handle otherwise

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Identify project indices
    project_indices = []
    for i, line in enumerate(lines):
        if "(cid:190) Updates:" in line or "(cid:190) Project Description:" in line:
            # The project name should be the previous non-empty line
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0:
                project_name = lines[j].strip()
                # Clean up project name if it contains bullets or extra chars
                # Sometimes headers might be caught, but joining with funding db will filter them
                project_indices.append((j, project_name))
    
    # Process each project block
    for k in range(len(project_indices)):
        start_idx, p_name = project_indices[k]
        # End index is the start of the next project or end of text
        if k < len(project_indices) - 1:
            end_idx = project_indices[k+1][0]
        else:
            end_idx = len(lines)
        
        block_text = "\n".join(lines[start_idx:end_idx])
        
        # Extract Begin Construction date
        # Pattern: (cid:131) Begin Construction: <Date>
        # Note: The cid character might vary or be unicode. The preview shows (cid:131).
        # Let's use regex to be flexible.
        
        match = re.search(r'Begin Construction:\s*(.*)', block_text, re.IGNORECASE)
        start_date = None
        if match:
            start_date = match.group(1).strip()
        else:
            # Try "Begin construction:"
            match = re.search(r'Begin construction:\s*(.*)', block_text, re.IGNORECASE)
            if match:
                 start_date = match.group(1).strip()
        
        # If Begin Construction not found, check for "Start Date" or just look for dates in the schedule?
        # The prompt implies "projects started". Construction start is the best proxy.
        # Let's also check for "Construction Start"
        if not start_date:
             match = re.search(r'Construction Start:\s*(.*)', block_text, re.IGNORECASE)
             if match:
                 start_date = match.group(1).strip()

        # Clean Start Date
        parsed_st = parse_date(start_date)
        
        extracted_projects.append({
            'Project_Name': p_name,
            'raw_st': start_date,
            'st': parsed_st
        })

df_extracted = pd.DataFrame(extracted_projects)

# Join with funding
# Ensure Project_Name matches.
# Funding Amount is a string in the preview, need to convert to int/float.
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

# Merge
merged = pd.merge(df_funding, df_extracted, on='Project_Name', how='inner')

# Filter for Spring 2022
spring_2022_projects = merged[merged['st'] == 'Spring 2022']

# Calculate result
count = len(spring_2022_projects)
total_funding = spring_2022_projects['Amount'].sum()

print("__RESULT__:")
print(json.dumps({
    "count": count,
    "total_funding": total_funding,
    "projects": spring_2022_projects[['Project_Name', 'raw_st', 'Amount']].to_dict(orient='records')
}))"""

env_args = {'var_function-call-5073457582333833681': ['civic_docs'], 'var_function-call-5073457582333837024': ['Funding'], 'var_function-call-11668788458618260347': 'file_storage/function-call-11668788458618260347.json', 'var_function-call-11668788458618261250': 'file_storage/function-call-11668788458618261250.json'}

exec(code, env_args)

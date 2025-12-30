code = """import json
import pandas as pd
import re

# Load data
funding_path = locals()['var_function-call-15165357656390883116']
docs_path = locals()['var_function-call-13981208063081827307']

with open(funding_path, 'r') as f:
    funding_records = json.load(f)
df_funding = pd.DataFrame(funding_records)

with open(docs_path, 'r') as f:
    docs = json.load(f)

projects = []
status_map = {
    "Capital Improvement Projects (Design)": "design",
    "Capital Improvement Projects (Construction)": "construction",
    "Capital Improvement Projects (Not Started)": "not started"
}

# Regex to find project blocks
# Looking for ProjectName followed by (cid:190) Updates:
# We escape parenthesis for the bullet point
pattern = re.compile(r"(?:^|\n)\s*(?P<name>[^\n]+?)\s*\n+\s*\(cid:190\)\s*(?:Updates|Project Description):")

for doc in docs:
    text = doc['text']
    
    # Identify sections by header positions
    sections = []
    for header, status_code in status_map.items():
        idx = text.find(header)
        if idx != -1:
            sections.append({'start': idx, 'status': status_code, 'header_len': len(header)})
    
    sections.sort(key=lambda x: x['start'])
    
    for i in range(len(sections)):
        current_section = sections[i]
        start_pos = current_section['start'] + current_section['header_len']
        status = current_section['status']
        
        end_pos = sections[i+1]['start'] if i + 1 < len(sections) else len(text)
        section_text = text[start_pos:end_pos]
        
        # Parse projects in this section
        matches = list(pattern.finditer(section_text))
        
        for j, match in enumerate(matches):
            p_name = match.group('name').strip()
            
            # Content range
            c_start = match.end()
            c_end = matches[j+1].start() if j + 1 < len(matches) else len(section_text)
            p_content = section_text[c_start:c_end]
            
            # Refine status
            final_status = status
            if status == 'construction':
                if 'Construction was completed' in p_content or 'Notice of completion filed' in p_content:
                    final_status = 'completed'
            
            # Check relevance
            is_relevant_text = False
            combined_lower = (p_name + " " + p_content).lower()
            if 'emergency' in combined_lower or 'fema' in combined_lower:
                is_relevant_text = True
            
            projects.append({
                "Project_Name": p_name,
                "Status": final_status,
                "Is_Relevant_Text": is_relevant_text
            })

df_projects = pd.DataFrame(projects)

# Match with funding
# Normalize names
df_funding['norm_name'] = df_funding['Project_Name'].str.lower().str.strip()
df_projects['norm_name'] = df_projects['Project_Name'].str.lower().str.strip()

# Create fuzzy mapping
mapping = {}
funding_names = df_funding['norm_name'].unique()
project_names = df_projects['norm_name'].unique()

for p in project_names:
    for f in funding_names:
        # Check if one is contained in the other
        if p in f or f in p:
            # Simple containment check might be too broad for short words, but project names are usually long.
            if len(p) > 10 and len(f) > 10:
                mapping[p] = f
                break # Take first match
    if p not in mapping:
        mapping[p] = None # No match found

df_projects['matched_funding_name'] = df_projects['norm_name'].map(mapping)

# Merge
merged = pd.merge(df_projects, df_funding, left_on='matched_funding_name', right_on='norm_name', how='inner', suffixes=('_extracted', '_funding'))

# Filter relevance
merged['Is_Relevant_Funding'] = merged['Project_Name'].str.lower().str.contains('emergency|fema')
merged['Is_Relevant'] = merged['Is_Relevant_Text'] | merged['Is_Relevant_Funding']

final_results = merged[merged['Is_Relevant']].copy()

# Select output columns
out_cols = ['Project_Name', 'Funding_Source', 'Amount', 'Status']
# Ensure types are JSON serializable
final_results['Amount'] = final_results['Amount'].astype(int)

print("__RESULT__:")
print(final_results[out_cols].to_json(orient='records'))"""

env_args = {'var_function-call-4192215151994041760': 'file_storage/function-call-4192215151994041760.json', 'var_function-call-15165357656390883116': 'file_storage/function-call-15165357656390883116.json', 'var_function-call-13981208063081827307': 'file_storage/function-call-13981208063081827307.json'}

exec(code, env_args)

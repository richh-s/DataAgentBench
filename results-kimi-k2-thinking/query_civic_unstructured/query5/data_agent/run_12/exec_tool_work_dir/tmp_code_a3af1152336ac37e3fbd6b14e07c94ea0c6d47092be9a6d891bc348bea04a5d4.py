code = """import json
import pandas as pd

# Load funding data
funding_file_path = locals()['var_functions.query_db:5']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
civic_file_path = locals()['var_functions.query_db:0']
with open(civic_file_path, 'r') as f:
    civic_docs_data = json.load(f)

# Process funding data
funding_df = pd.DataFrame(funding_data)

# Convert amounts to integers
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce').fillna(0).astype(int)

# Find disaster-related projects in funding
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Cal OES', 'disaster', 'recovery', 'fire']
mask = funding_df['Project_Name'].str.contains('|'.join(disaster_keywords), case=False, na=False)
disaster_funding = funding_df[mask].copy()

result_str = 'Analysis Results:\n'
result_str += f'Total funding records: {len(funding_df)}\n'
result_str += f'Disaster-related projects in funding: {len(disaster_funding)}\n'
result_str += f'Total disaster funding available: ${disaster_funding["Amount"].sum():,}\n'

# Extract project information from civic documents
# We'll look for project mentions with start dates
all_project_mentions = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    # Look for common project patterns
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        # Look for project names and dates
        if any(keyword in line for keyword in ['Project', 'Updates', 'Schedule']):
            if len(line) < 200:  # Avoid long paragraphs
                all_project_mentions.append(line)

# Save key data for further analysis
analysis_data = {
    'disaster_funding': disaster_funding.to_dict('records'),
    'project_mentions': all_project_mentions[:50]  # First 50 mentions
}

result_str += '\nReady for detailed analysis'

print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

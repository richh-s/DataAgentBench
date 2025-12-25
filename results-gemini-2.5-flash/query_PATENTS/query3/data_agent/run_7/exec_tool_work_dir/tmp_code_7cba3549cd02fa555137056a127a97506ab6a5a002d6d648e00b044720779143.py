code = """import json
import re
import pandas as pd

# Load the full result from the file
with open(locals()['var_function-call-8448093354361830252'], 'r') as f:
    publication_data = json.load(f)

df = pd.DataFrame(publication_data)

# Function to extract assignee from Patents_info
def extract_assignee(patents_info):
    match = re.search(r'(.*?) holds the US patent', patents_info)
    if match:
        return match.group(1).strip()
    return None

# Apply the function to create a new 'assignee' column
df['assignee'] = df['Patents_info'].apply(extract_assignee)

# Filter patents assigned to UNIV CALIFORNIA
univ_california_patents = df[df['assignee'].str.contains('UNIV CALIFORNIA', na=False)]

# Extract publication numbers of UNIV CALIFORNIA patents
univ_california_publication_numbers = set()
for index, row in univ_california_patents.iterrows():
    match = re.search(r'publication number ([A-Z0-9-]+)', row['Patents_info'])
    if match:
        univ_california_publication_numbers.add(match.group(1))

# Initialize lists to store results
citing_assignees_info = []

# Iterate through all patents to find those citing UNIV CALIFORNIA patents
for index, row in df.iterrows():
    citing_assignee = row['assignee']
    if citing_assignee and citing_assignee != 'UNIV CALIFORNIA':
        try:
            citations = json.loads(row['citation'])
            for citation in citations:
                if citation.get('publication_number') in univ_california_publication_numbers:
                    # Extract primary CPC subclass
                    cpc_codes = json.loads(row['cpc'])
                    primary_cpc = None
                    for cpc_entry in cpc_codes:
                        # Assuming "first" and "inventive" true indicate primary or a good candidate
                        if cpc_entry.get('first', False) and cpc_entry.get('inventive', False):
                            primary_cpc = cpc_entry['code']
                            break
                        elif not primary_cpc and cpc_entry.get('code'): # If no primary, take the first available code
                            primary_cpc = cpc_entry['code']

                    if primary_cpc:
                        cpc_subclass = primary_cpc.split('/')[0]  # Get the subclass part (e.g., H01M10 from H01M10/0565)
                        if cpc_subclass not in [info['cpc_subclass'] for info in citing_assignees_info if info['assignee'] == citing_assignee]:
                            citing_assignees_info.append({
                                'assignee': citing_assignee,
                                'cpc_subclass': cpc_subclass
                            })
                    break # Only need to find one citation to a UNIV CALIFORNIA patent for this citing patent
        except json.JSONDecodeError:
            continue

print('__RESULT__:')
print(json.dumps(citing_assignees_info))"""

env_args = {'var_function-call-8448093354361830252': 'file_storage/function-call-8448093354361830252.json'}

exec(code, env_args)

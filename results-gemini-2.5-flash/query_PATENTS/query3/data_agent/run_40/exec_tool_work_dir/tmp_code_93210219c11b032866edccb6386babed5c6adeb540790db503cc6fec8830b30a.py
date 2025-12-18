code = """import json
import pandas as pd

with open(locals()['var_function-call-373891586094066339'], 'r') as f:
    publication_data = json.load(f)

# Convert to DataFrame for easier processing
df_publications = pd.DataFrame(publication_data)

# Function to extract assignee_harmonized
def extract_assignee(patents_info):
    try:
        # Assuming assignee_harmonized is always present after 'assignee_harmonized: ' and before a comma or end of string
        start_idx = patents_info.find('assignee_harmonized: ')
        if start_idx != -1:
            start_idx += len('assignee_harmonized: ')
            end_idx = patents_info.find(',', start_idx)
            if end_idx == -1:
                assignee = patents_info[start_idx:].strip()
            else:
                assignee = patents_info[start_idx:end_idx].strip()
            return assignee
    except:
        pass
    return None

df_publications['assignee_harmonized'] = df_publications['Patents_info'].apply(extract_assignee)

# Identify patents assigned to 'UNIV CALIFORNIA'
univ_california_patents = df_publications[df_publications['assignee_harmonized'] == 'UNIV CALIFORNIA']

# Extract publication numbers of UNIV CALIFORNIA patents
univ_california_publication_numbers = []
for _, row in univ_california_patents.iterrows():
    # Extract publication number from Patents_info
    patents_info = row['Patents_info']
    pub_num_start = patents_info.find('publication number ')
    if pub_num_start != -1:
        pub_num_start += len('publication number ')
        pub_num_end = patents_info.find('.', pub_num_start)
        if pub_num_end != -1:
            univ_california_publication_numbers.append(patents_info[pub_num_start:pub_num_end])

# Identify patents that cite UNIV CALIFORNIA patents
citing_patents_info = []
for _, row in df_publications.iterrows():
    citations = json.loads(row['citation']) if row['citation'] else []
    for citation in citations:
        if citation.get('publication_number') in univ_california_publication_numbers:
            citing_assignee = row['assignee_harmonized']
            if citing_assignee and citing_assignee != 'UNIV CALIFORNIA':
                cpc_codes = json.loads(row['cpc']) if row['cpc'] else []
                primary_cpc = None
                for cpc_item in cpc_codes:
                    if cpc_item.get('first') == True:
                        primary_cpc = cpc_item.get('code')
                        break
                if primary_cpc:
                    citing_patents_info.append({'assignee': citing_assignee, 'primary_cpc': primary_cpc})

result = pd.DataFrame(citing_patents_info).to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-15453717939236819502': [], 'var_function-call-373891586094066339': 'file_storage/function-call-373891586094066339.json'}

exec(code, env_args)

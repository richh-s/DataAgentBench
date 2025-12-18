code = """import json
import pandas as pd

# Load the data from the file
with open(locals()['var_function-call-3342722278808768487'], 'r') as f:
    publication_data = json.load(f)

# Convert to DataFrame for easier processing
df = pd.DataFrame(publication_data)

# Filter for patents assigned to 'UNIV CALIFORNIA'
univ_california_patents = df[df['Patents_info'].str.contains('UNIV CALIFORNIA', na=False)]

# Extract publication numbers of patents assigned to UNIV CALIFORNIA
univ_california_publication_numbers = set()
for index, row in univ_california_patents.iterrows():
    # Extract publication number from 'Patents_info'
    patents_info = row['Patents_info']
    pub_num_match = pd.Series(patents_info).str.extract(r'pub\\. number ([A-Z0-9-]+)')
    if not pub_num_match.empty:
        univ_california_publication_numbers.add(pub_num_match.iloc[0, 0])

# Initialize a list to store results
citing_assignees_and_cpc = []

# Iterate through all patents to find citations to 'UNIV CALIFORNIA' patents
for index, row in df.iterrows():
    citations = json.loads(row['citation']) if isinstance(row['citation'], str) else row['citation']
    if citations:
        for citation in citations:
            cited_publication_number = citation.get('publication_number')
            if cited_publication_number in univ_california_publication_numbers:
                # This patent cites a UNIV CALIFORNIA patent
                # Extract assignee of the citing patent
                citing_patents_info = row['Patents_info']
                assignee_match = pd.Series(citing_patents_info).str.extract(r'assigned to ([A-Z0-9\s]+?)(?: and has| and app. number| owns the| holds the| \(number| patent filing|\(no\\.)')
                citing_assignee = assignee_match.iloc[0,0].strip() if not assignee_match.empty else 'UNKNOWN'

                if citing_assignee != 'UNIV CALIFORNIA':
                    # Get the CPC code of the cited (UNIV CALIFORNIA) patent
                    # Need to find the original UNIV CALIFORNIA patent to get its CPC
                    cited_patent_row = univ_california_patents[
                        univ_california_patents['Patents_info'].str.contains(f'pub. number {cited_publication_number}', na=False)
                    ]
                    if not cited_patent_row.empty:
                        cpc_codes = json.loads(cited_patent_row.iloc[0]['cpc'])
                        primary_cpc = None
                        for cpc_entry in cpc_codes:
                            if cpc_entry.get('first'):
                                primary_cpc = cpc_entry['code']
                                break
                        if primary_cpc:
                            citing_assignees_and_cpc.append({'assignee': citing_assignee, 'cpc_symbol': primary_cpc})

print('__RESULT__:')
print(json.dumps(citing_assignees_and_cpc))"""

env_args = {'var_function-call-11763644540560458459': [], 'var_function-call-3342722278808768487': 'file_storage/function-call-3342722278808768487.json'}

exec(code, env_args)

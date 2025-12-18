code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-373891586094066339'], 'r') as f:
    publication_data = json.load(f)

df_publications = pd.DataFrame(publication_data)

def extract_assignee(patents_info):
    match = re.search(r'assignee_harmonized: ([^,;.]+)', patents_info)
    if match:
        return match.group(1).strip()
    return None

def extract_publication_number(patents_info):
    match = re.search(r'publication number ([^,;.]+)', patents_info)
    if match:
        return match.group(1).strip()
    return None

df_publications['assignee_harmonized'] = df_publications['Patents_info'].apply(extract_assignee)
df_publications['publication_number'] = df_publications['Patents_info'].apply(extract_publication_number)

univ_california_patents = df_publications[
    (df_publications['assignee_harmonized'] == 'UNIV CALIFORNIA') |
    (df_publications['assignee_harmonized'].str.contains('UNIV CALIFORNIA', na=False))
]

univ_california_publication_numbers = univ_california_patents['publication_number'].dropna().tolist()

citing_patents_info = []
for _, row in df_publications.iterrows():
    citing_assignee = row['assignee_harmonized']
    if citing_assignee and citing_assignee != 'UNIV CALIFORNIA':
        citations = json.loads(row['citation']) if pd.notna(row['citation']) else []
        for citation in citations:
            if citation.get('publication_number') in univ_california_publication_numbers:
                cpc_codes = json.loads(row['cpc']) if pd.notna(row['cpc']) else []
                primary_cpc = None
                for cpc_item in cpc_codes:
                    if cpc_item.get('first') == True:
                        primary_cpc = cpc_item.get('code')
                        break
                if primary_cpc:
                    citing_patents_info.append({'assignee': citing_assignee, 'primary_cpc': primary_cpc})

result_df = pd.DataFrame(citing_patents_info).drop_duplicates()

# Get unique CPC codes for definition lookup
unique_cpc_codes = result_df['primary_cpc'].unique().tolist()

print('__RESULT__:')
print(json.dumps(unique_cpc_codes))"""

env_args = {'var_function-call-15453717939236819502': [], 'var_function-call-373891586094066339': 'file_storage/function-call-373891586094066339.json', 'var_function-call-2533390639764278579': []}

exec(code, env_args)

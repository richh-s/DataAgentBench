code = """import pandas as pd
import json

# Load citation data from the file path stored under var_call_eQ4b55rLT6bzj3DERtAYONk9
with open('var_call_eQ4b55rLT6bzj3DERtAYONk9') as f:
    citation_data = json.load(f)

# Load paper data from the file path stored under var_call_lu219mWVFqif4srb6PRhjXkj
with open('var_call_lu219mWVFqif4srb6PRhjXkj') as f:
    paper_data = json.load(f)

# Creating dataframes
citation_df = pd.DataFrame(citation_data)
paper_df = pd.DataFrame(paper_data)

# Extracting titles from paper documents
paper_df['title'] = paper_df['filename'].str.replace('.txt', '', regex=False)

# Merging paper titles with citation data based on title
merged_df = pd.merge(citation_df, paper_df[['title']], on='title', how='inner')

# Selecting required columns
final_result = merged_df[['title', 'total_citations']].to_json(orient='records')

print('__RESULT__:')
print(final_result)"""

env_args = {'var_call_KusaN5PZR6ntjYTGIJYHpsbC': 'file_storage/call_KusaN5PZR6ntjYTGIJYHpsbC.json', 'var_call_Z9kVneAD5y8fjXNrBEVOikbE': 'file_storage/call_Z9kVneAD5y8fjXNrBEVOikbE.json', 'var_call_eQ4b55rLT6bzj3DERtAYONk9': 'file_storage/call_eQ4b55rLT6bzj3DERtAYONk9.json', 'var_call_lu219mWVFqif4srb6PRhjXkj': []}

exec(code, env_args)

code = """import pandas as pd

# Load the citation data and paper information
citation_data = pd.read_json('var_call_eQ4b55rLT6bzj3DERtAYONk9')
paper_data = pd.read_json('var_call_lu219mWVFqif4srb6PRhjXkj')

# Extracting titles from paper documents
paper_titles = paper_data['filename'].str.replace('.txt', '', regex=False)

# Merging paper titles with citation data based on title
merged_data = citation_data[citation_data['title'].isin(paper_titles)]

# Selecting required columns
final_result = merged_data[['title', 'total_citations']].to_json(orient='records')

print('__RESULT__:')
print(final_result)"""

env_args = {'var_call_KusaN5PZR6ntjYTGIJYHpsbC': 'file_storage/call_KusaN5PZR6ntjYTGIJYHpsbC.json', 'var_call_Z9kVneAD5y8fjXNrBEVOikbE': 'file_storage/call_Z9kVneAD5y8fjXNrBEVOikbE.json', 'var_call_eQ4b55rLT6bzj3DERtAYONk9': 'file_storage/call_eQ4b55rLT6bzj3DERtAYONk9.json', 'var_call_lu219mWVFqif4srb6PRhjXkj': []}

exec(code, env_args)

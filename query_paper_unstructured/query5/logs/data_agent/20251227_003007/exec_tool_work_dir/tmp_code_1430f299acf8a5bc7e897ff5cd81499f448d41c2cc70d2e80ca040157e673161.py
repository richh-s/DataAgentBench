code = """import pandas as pd
import json

# Load citation data from SQLite database
citation_data = json.loads(open(var_call_NAcyVrwk0Koyu0gefsTsZ6Lm).read())

# Load paper documents data from MongoDB database
paper_docs_data = []  # Empty list since query returned no results

# Create DataFrames from both citation and paper documents data
citation_df = pd.DataFrame(citation_data)
paper_df = pd.DataFrame(paper_docs_data)

# Combine the two DataFrames based on the title matching the filename (without .txt)
# First, let's ensure the title comparison is valid
citation_df['title'] = citation_df['title'].str.replace('.txt', '')  # Remove .txt for comparison

# Merging the DataFrames on title
merged_df = pd.merge(citation_df, paper_df, left_on='title', right_on='filename', how='inner')

# Group by the year and sum the citation counts
citation_count_totals = merged_df.groupby('year')['citation_count'].sum().to_json(orient='records')

# Prepare the final result to print
print('__RESULT__:')
print(citation_count_totals)"""

env_args = {'var_call_NAcyVrwk0Koyu0gefsTsZ6Lm': 'file_storage/call_NAcyVrwk0Koyu0gefsTsZ6Lm.json', 'var_call_OMPg1VJEfM2EEh8WZbL0I5UZ': []}

exec(code, env_args)

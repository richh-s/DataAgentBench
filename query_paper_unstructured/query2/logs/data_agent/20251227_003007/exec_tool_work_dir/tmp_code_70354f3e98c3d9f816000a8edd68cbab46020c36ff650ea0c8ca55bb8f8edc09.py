code = """import pandas as pd
import json

# Load citation data
citation_data = json.load(open('var_call_SNsS5ZhRzqYOTWnVaKI1Zydb'))
# Convert the citation data into DataFrame
citation_df = pd.DataFrame(citation_data)

# Load paper data, which has no results
paper_data = []

# Create a DataFrame for paper titles and citation counts
if len(paper_data) > 0:
    paper_df = pd.DataFrame(paper_data)
else:
    paper_df = pd.DataFrame(columns=['title', 'citation_count'])

# Join paper data with citation data on title
merged_df = pd.merge(paper_df, citation_df, left_on='title', right_on='title', how='left')

# Calculate average citation count
average_citation = merged_df['citation_count'].mean() if not merged_df.empty else 0

# Prepare the result
result = average_citation

print('__RESULT__:')
print(result)"""

env_args = {'var_call_SNsS5ZhRzqYOTWnVaKI1Zydb': 'file_storage/call_SNsS5ZhRzqYOTWnVaKI1Zydb.json', 'var_call_mQ2UYQayiESZ0Kb5UlneGsDe': []}

exec(code, env_args)

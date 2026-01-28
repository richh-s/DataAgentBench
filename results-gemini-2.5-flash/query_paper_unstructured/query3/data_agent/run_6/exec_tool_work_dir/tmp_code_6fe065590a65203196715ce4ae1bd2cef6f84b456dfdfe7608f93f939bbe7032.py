code = """import json
import pandas as pd

# Load the filtered papers with empirical contribution and year > 2016
filtered_papers = locals()['var_function-call-9706345335969969102']
df_papers = pd.DataFrame(filtered_papers)

# Load the citation data
file_path_citations = locals()['var_function-call-16153027709255841517']
with open(file_path_citations, 'r') as f:
    citations_data = json.load(f)
df_citations = pd.DataFrame(citations_data)

# Convert 'citation_count' to numeric, handling potential errors and non-numeric values
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'], errors='coerce').fillna(0)

# Group citations by title and sum the citation counts
df_citations_grouped = df_citations.groupby('title')['citation_count'].sum().reset_index()

# Merge the two dataframes on 'title'
merged_df = pd.merge(df_papers, df_citations_grouped, on='title', how='inner')

# Select and rename columns for the final output
final_result = merged_df[['title', 'citation_count']]
final_result = final_result.rename(columns={'citation_count': 'total_citation_count'})

print("__RESULT__:")
print(final_result.to_json(orient='records'))"""

env_args = {'var_function-call-15609089362044603763': ['paper_docs'], 'var_function-call-68838740435367397': 'file_storage/function-call-68838740435367397.json', 'var_function-call-3064361672336217427': [], 'var_function-call-9706345335969969102': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_function-call-16153027709255841517': 'file_storage/function-call-16153027709255841517.json'}

exec(code, env_args)

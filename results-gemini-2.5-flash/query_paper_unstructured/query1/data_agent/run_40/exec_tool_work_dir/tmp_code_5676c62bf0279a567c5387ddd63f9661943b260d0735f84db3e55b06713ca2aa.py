code = """import json
import pandas as pd

# Load the full results from the files
with open(locals()["var_function-call-13417281912679959008"], "r") as f:
    citations_data = json.load(f)

with open(locals()["var_function-call-9044705175670950622"], "r") as f:
    papers_data = json.load(f)

citations_df = pd.DataFrame(citations_data)
papers_df = pd.DataFrame(papers_data)

# Extract title from filename
papers_df['title'] = papers_df['filename'].str.replace('.txt', '')

# Function to extract domain from text
def extract_domain(text):
    if 'food' in text.lower():
        return ['food']
    return []

papers_df['domain'] = papers_df['text'].apply(extract_domain)

# Filter papers for 'food' domain
food_papers_df = papers_df[papers_df['domain'].apply(lambda x: 'food' in x)]

# Merge with citations data
merged_df = pd.merge(food_papers_df, citations_df, on='title', how='inner')

# Convert citation_count to numeric and sum
merged_df['citation_count'] = pd.to_numeric(merged_df['citation_count'])
total_citations_food = merged_df['citation_count'].sum()

print("__RESULT__:")
print(json.dumps(total_citations_food))"""

env_args = {'var_function-call-9150781744971923258': ['Citations', 'sqlite_sequence'], 'var_function-call-13417281912679959008': 'file_storage/function-call-13417281912679959008.json', 'var_function-call-7359045309041966630': ['paper_docs'], 'var_function-call-9044705175670950622': 'file_storage/function-call-9044705175670950622.json'}

exec(code, env_args)

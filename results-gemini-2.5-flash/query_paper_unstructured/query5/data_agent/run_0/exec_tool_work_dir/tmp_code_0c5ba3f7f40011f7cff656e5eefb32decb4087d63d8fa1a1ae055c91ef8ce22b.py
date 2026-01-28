code = """import pandas as pd
import json

citations_data_path = locals()['var_function-call-10408202181241436085']
paper_docs_data_path = locals()['var_function-call-6321380155565966315']

with open(citations_data_path, 'r') as f:
    citations_data = json.load(f)

with open(paper_docs_data_path, 'r') as f:
    paper_docs_data = json.load(f)

citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

paper_docs_df = pd.DataFrame(paper_docs_data)

# Extract title from filename
paper_docs_df['title'] = paper_docs_df['filename'].apply(lambda x: x.replace('.txt', ''))

# Function to extract venue
def extract_venue(text):
    if "CHI" in text:
        return "CHI"
    return None

paper_docs_df['venue'] = paper_docs_df['text'].apply(extract_venue)

# Filter for CHI papers
chi_papers_df = paper_docs_df[paper_docs_df['venue'] == 'CHI']

# Merge with citations data
merged_df = pd.merge(chi_papers_df, citations_df, on='title', how='inner')

# Calculate total citation count
total_citations = merged_df['citation_count'].sum()

print('__RESULT__:')
print(json.dumps(str(total_citations)))"""

env_args = {'var_function-call-10408202181241436085': 'file_storage/function-call-10408202181241436085.json', 'var_function-call-6321380155565966315': 'file_storage/function-call-6321380155565966315.json'}

exec(code, env_args)

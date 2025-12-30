code = """import pandas as pd
import json

citations_data_path = locals()['var_function-call-8920128789890613520']
paper_docs_data_path = locals()['var_function-call-415746246971213295']

with open(citations_data_path, 'r') as f:
    citations_data = json.load(f)

with open(paper_docs_data_path, 'r') as f:
    paper_docs_data = json.load(f)

citations_df = pd.DataFrame(citations_data)
paper_docs_df = pd.DataFrame(paper_docs_data)

# Extract title from filename (remove .txt extension)
paper_docs_df['title'] = paper_docs_df['filename'].str.replace('.txt', '', regex=False)

# Function to extract venue from text
def extract_venue(text):
    if "CHI" in text:
        return "CHI"
    return None

paper_docs_df['venue'] = paper_docs_df['text'].apply(extract_venue)

# Filter for CHI papers
chi_papers_df = paper_docs_df[paper_docs_df['venue'] == 'CHI']

# Join with citations data
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])
merged_df = pd.merge(chi_papers_df, citations_df, on='title', how='inner')

# Calculate total citation count
total_citations = merged_df['citation_count'].sum()

print('__RESULT__:')
print(json.dumps(str(total_citations)))"""

env_args = {'var_function-call-8920128789890613520': 'file_storage/function-call-8920128789890613520.json', 'var_function-call-415746246971213295': 'file_storage/function-call-415746246971213295.json'}

exec(code, env_args)

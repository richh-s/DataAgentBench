code = """import pandas as pd
import json

# Load citations data from 2020
citations_file = "var_functions.query_db:5"
print("Loading citations data...")
citations_df = pd.read_json(citations_file)
print(f"Citations shape: {citations_df.shape}")
print("Sample citations data:")
print(citations_df.head())

# Load paper documents data
paper_docs_file = "var_functions.query_db:6"
print("\nLoading paper docs data...")
paper_docs_df = pd.read_json(paper_docs_file)
print(f"Paper docs shape: {paper_docs_df.shape}")

# Extract title from filename (remove .txt extension)
paper_docs_df['title'] = paper_docs_df['filename'].str.replace('.txt', '', regex=False)

# Find CHI papers by searching for CHI in the text
# Look for patterns like CHI '15, CHI 2015, CHI'15, etc.
paper_docs_df['is_chi'] = paper_docs_df['text'].str.contains('CHI', case=False, na=False)
chi_papers = paper_docs_df[paper_docs_df['is_chi']].copy()

print(f"\nFound {len(chi_papers)} potential CHI papers")
print("Sample CHI papers:")
print(chi_papers[['title', 'filename']].head())

# Join with citations data on title
# Need to handle case sensitivity and minor differences
citations_df['title_lower'] = citations_df['title'].str.lower()
chi_papers['title_lower'] = chi_papers['title'].str.lower()

# Merge the datasets
merged_df = pd.merge(chi_papers, citations_df, on='title_lower', how='inner')

print(f"\nFound {len(merged_df)} CHI papers with citations in 2020")
print("Sample merged data:")
print(merged_df[['title_x', 'citation_count']].head())

# Calculate total citation counts
total_citations = merged_df['citation_count'].astype(int).sum()

print(f"\nTotal citation count for CHI papers in 2020: {total_citations}")

# Also show individual paper citations
print("\nIndividual CHI paper citations in 2020:")
result_df = merged_df[['title_x', 'citation_count']].copy()
result_df.columns = ['title', 'citation_count']
result_df['citation_count'] = result_df['citation_count'].astype(int)
result_df = result_df.sort_values('citation_count', ascending=False)
print(result_df.to_string(index=False))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

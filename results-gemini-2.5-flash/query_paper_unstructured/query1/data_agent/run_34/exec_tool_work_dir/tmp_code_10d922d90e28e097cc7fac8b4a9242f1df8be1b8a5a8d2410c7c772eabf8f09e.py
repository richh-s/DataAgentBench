code = """import pandas as pd
import json

citations_data = pd.read_json(locals()['var_function-call-15129328654268150143'])
paper_docs_path = locals()['var_function-call-12718121754203299934']

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

paper_info = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text'].lower() # Convert to lowercase for case-insensitive matching

    domain = []
    if "food" in text:
        domain.append("food")

    if domain: # Only add papers that have at least one domain identified
        paper_info.append({"title": title, "domain": domain})

paper_info_df = pd.DataFrame(paper_info)

# Merge citation data with paper domain information
merged_df = pd.merge(citations_data, paper_info_df, on="title", how="inner")

# Filter for papers in the 'food' domain
food_papers_df = merged_df[merged_df['domain'].apply(lambda x: 'food' in x)]

# Calculate the total citation count for food papers
total_citation_count = food_papers_df['citation_count'].astype(int).sum()

print("__RESULT__:")
print(json.dumps(str(total_citation_count)))"""

env_args = {'var_function-call-15129328654268150143': 'file_storage/function-call-15129328654268150143.json', 'var_function-call-12718121754203299934': 'file_storage/function-call-12718121754203299934.json'}

exec(code, env_args)

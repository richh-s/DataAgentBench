code = """import json
import pandas as pd

# Load citation data from the file
with open(locals()['var_function-call-12422329575642433269'], 'r') as f:
    citation_data = json.load(f)

# Convert citation data to DataFrame
citations_df = pd.DataFrame(citation_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Load paper documents from the file
with open(locals()['var_function-call-3331076471507752676'], 'r') as f:
    paper_docs = json.load(f)

paper_details = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # Extract venue (case-insensitive search for "CHI")
    venue = None
    if "CHI" in text:
        venue = "CHI"
    
    paper_details.append({'title': title, 'venue': venue})

paper_details_df = pd.DataFrame(paper_details)

# Merge citation data with paper details
merged_df = pd.merge(citations_df, paper_details_df, on='title', how='inner')

# Filter for papers presented at CHI
chi_papers_df = merged_df[merged_df['venue'] == 'CHI']

# Calculate total citation counts
total_citations = chi_papers_df['citation_count'].sum()

print('__RESULT__:')
print(json.dumps(int(total_citations)))"""

env_args = {'var_function-call-12422329575642433269': 'file_storage/function-call-12422329575642433269.json', 'var_function-call-3331076471507752676': 'file_storage/function-call-3331076471507752676.json'}

exec(code, env_args)

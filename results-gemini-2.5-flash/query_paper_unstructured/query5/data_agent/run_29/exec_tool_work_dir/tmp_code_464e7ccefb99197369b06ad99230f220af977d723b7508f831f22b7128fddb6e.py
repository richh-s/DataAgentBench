code = """import json
import re
import pandas as pd

# Load citation data
with open(locals()['var_function-call-9866274534013825103'], 'r') as f:
    citation_data = json.load(f)
citation_df = pd.DataFrame(citation_data)
citation_df['citation_count'] = pd.to_numeric(citation_df['citation_count'])

# Load all paper documents (preview showed this is a large file)
with open(locals()['var_function-call-7973633068397485439'], 'r') as f:
    paper_docs = json.load(f)

# Extract relevant information from paper documents
papers_info = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace(".txt", "")
    text = doc['text']

    venue_match = re.search(r'([A-Z]{3,}) \'\d{2}|Venue: ([A-Z]{3,})', text)
    venue = venue_match.group(1) if venue_match and venue_match.group(1) else (venue_match.group(2) if venue_match and venue_match.group(2) else 'N/A')

    papers_info.append({
        'title': title,
        'venue': venue
    })

papers_df = pd.DataFrame(papers_info)

# Filter for CHI papers
chi_papers_df = papers_df[papers_df['venue'].str.contains('CHI', case=False, na=False)]

# Join with citation data
merged_df = pd.merge(chi_papers_df, citation_df, on='title', how='inner')

# Calculate total citation count
total_citations = merged_df['citation_count'].sum()

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-9866274534013825103': 'file_storage/function-call-9866274534013825103.json', 'var_function-call-12458711442629031814': 'file_storage/function-call-12458711442629031814.json', 'var_function-call-16518493279907426009': 'file_storage/function-call-16518493279907426009.json', 'var_function-call-7973633068397485439': 'file_storage/function-call-7973633068397485439.json'}

exec(code, env_args)

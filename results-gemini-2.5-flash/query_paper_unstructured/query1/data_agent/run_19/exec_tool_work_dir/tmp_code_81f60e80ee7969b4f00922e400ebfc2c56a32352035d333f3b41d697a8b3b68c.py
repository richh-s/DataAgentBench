code = """import pandas as pd
import json
import re

# Load the paper documents data
with open(locals()['var_function-call-3565873005998525411'], 'r') as f:
    paper_docs_data = json.load(f)

# Load the citation data
with open(locals()['var_function-call-13776783906841665151'], 'r') as f:
    citations_data = json.load(f)

# Create DataFrame for paper documents
paper_docs_df = pd.DataFrame(paper_docs_data)

# Extract title from filename
paper_docs_df['title'] = paper_docs_df['filename'].apply(lambda x: x.replace('.txt', ''))

# Function to extract domain from text.
# The hint states "domain: Research domain/topic (e.g., "food", "physical activity", "sleep", "mental")"
# and "When matching domains or contributions, use substring/contains matching since values may be part of a list."
def extract_domain(text):
    domains = []
    if re.search(r'domain:\s*([^\\n]+)', text, re.IGNORECASE):
        # Specific patterns might indicate domain. Look for common domain keywords in context.
        # This is a heuristic approach, as the structure is unstructured text.
        # The prompt indicates 'domain' as a field to be extracted from the *document*, implying
        # it might be explicitly mentioned or inferable. Since it's unstructured, direct regex for "domain: X"
        # is a good starting point if such explicit mentions are expected.
        # However, the example shows "food [11]", implying domains could be mentioned in context.
        # A broader search for "food" keyword across text is more robust given "substring/contains matching" hint.
        if "food" in text.lower():
            domains.append("food")
        # Add other domains if needed for other queries
    elif "food" in text.lower(): # Broader search if "domain:" isn't explicit
        domains.append("food")
    return list(set(domains)) # Return unique domains

paper_docs_df['extracted_domain'] = paper_docs_df['text'].apply(extract_domain)

# Filter for papers in 'food' domain
food_papers_df = paper_docs_df[paper_docs_df['extracted_domain'].apply(lambda x: 'food' in x)]

# Create DataFrame for citations
citations_df = pd.DataFrame(citations_data)

# Convert citation_count to numeric
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Merge food papers with citation data
merged_df = pd.merge(food_papers_df, citations_df, on='title', how='inner')

# Calculate total citation count for food domain
total_citation_count = merged_df['citation_count'].sum()

print("__RESULT__:")
print(json.dumps(total_citation_count))"""

env_args = {'var_function-call-10843417409462739428': ['Citations', 'sqlite_sequence'], 'var_function-call-13776783906841665151': 'file_storage/function-call-13776783906841665151.json', 'var_function-call-15248009430255834493': ['paper_docs'], 'var_function-call-3565873005998525411': 'file_storage/function-call-3565873005998525411.json'}

exec(code, env_args)

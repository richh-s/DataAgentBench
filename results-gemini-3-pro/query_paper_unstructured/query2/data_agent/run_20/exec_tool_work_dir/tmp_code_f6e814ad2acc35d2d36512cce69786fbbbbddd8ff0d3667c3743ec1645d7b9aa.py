code = """import json
import pandas as pd

# Load Citations (Result of call-1)
# The key for call-1 (SQL query) is var_function-call-3572630192216415606
with open(locals()['var_function-call-3572630192216415606'], 'r') as f:
    citations_data = json.load(f)

citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Load Paper Docs (Result of call-2)
# The key for call-2 (Mongo query) is var_function-call-16031778060578504755
with open(locals()['var_function-call-16031778060578504755'], 'r') as f:
    paper_docs = json.load(f)

acm_titles = []
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check for ACM
    # Indicators:
    # - "© ACM"
    # - "Copyright" and "ACM" in close proximity
    # - "permissions@acm.org"
    # - "ACM Classification Keywords"
    # - "Association for Computing Machinery"
    
    # Broad check first
    is_acm = False
    if "ACM" in text:
        # Validate if it's likely the publisher
        if "© ACM" in text or \
           "Copyright" in text and "ACM" in text and text.find("ACM") < 5000 or \
           "permissions@acm.org" in text or \
           "ACM Classification Keywords" in text or \
           "Association for Computing Machinery" in text:
            is_acm = True
    
    if is_acm:
        acm_titles.append(title)

# Filter citations for ACM papers
acm_citations_df = citations_df[citations_df['title'].isin(acm_titles)]

# Calculate average
avg_citations = acm_citations_df['citation_count'].mean()

print("__RESULT__:")
print(json.dumps(avg_citations))"""

env_args = {'var_function-call-3572630192216415606': 'file_storage/function-call-3572630192216415606.json', 'var_function-call-16031778060578504755': 'file_storage/function-call-16031778060578504755.json'}

exec(code, env_args)

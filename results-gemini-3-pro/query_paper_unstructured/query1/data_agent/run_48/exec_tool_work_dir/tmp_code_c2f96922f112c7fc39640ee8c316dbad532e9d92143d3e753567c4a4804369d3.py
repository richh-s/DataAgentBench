code = """import json
import pandas as pd

# Load papers
with open(locals()['var_function-call-4672195044827894195'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-9265765399726123142'], 'r') as f:
    citations = json.load(f)

# Filter papers by domain 'food'
food_papers = []
for p in papers:
    text = p.get('text', '').lower()
    # Check for 'food' in text
    # The hint suggests substring matching for domain.
    if 'food' in text:
        # Extract title from filename
        filename = p.get('filename', '')
        if filename.endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        food_papers.append(title)

# Create a DataFrame for citations
df_citations = pd.DataFrame(citations)
# Ensure citation_count is numeric
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

# Filter citations for food papers
food_citations = df_citations[df_citations['title'].isin(food_papers)]

total_citations = food_citations['citation_count'].sum()

print("__RESULT__:")
print(json.dumps(int(total_citations)))"""

env_args = {'var_function-call-13370766090165900916': 'file_storage/function-call-13370766090165900916.json', 'var_function-call-9130405135784485262': 'file_storage/function-call-9130405135784485262.json', 'var_function-call-9265765399726123142': 'file_storage/function-call-9265765399726123142.json', 'var_function-call-4672195044827894195': 'file_storage/function-call-4672195044827894195.json'}

exec(code, env_args)

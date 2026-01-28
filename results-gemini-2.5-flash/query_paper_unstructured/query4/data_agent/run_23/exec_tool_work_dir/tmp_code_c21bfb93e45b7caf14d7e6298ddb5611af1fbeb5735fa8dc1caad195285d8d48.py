code = """import pandas as pd
import json
import re

# Load the full result from the JSON file
file_path = locals()['var_function-call-13583694419194179142']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

df_papers = pd.DataFrame(paper_docs)

# Extract title from filename
df_papers['title'] = df_papers['filename'].apply(lambda x: x.replace('.txt', ''))

# Function to extract year and domain from text
def extract_info(text):
    year_match = re.search(r'\\b(19|20)\\d{2}\\b', text)
    year = int(year_match.group(0)) if year_match else None

    domain_match = re.search(r'(?i)domain: ([^\\n]+)', text)
    domain_match_text = domain_match.group(1) if domain_match else ''
    domain = [d.strip() for d in domain_match_text.split(',')] if domain_match_text else []
    if not domain: # Try to find domain from the paper text itself, not just the "domain:" field
        if re.search(r'(?i)physical activity', text):
            domain.append('physical activity')

    return year, domain

df_papers[['year', 'domain']] = df_papers['text'].apply(lambda x: pd.Series(extract_info(x)))

# Filter for papers published in 2016 and in the 'physical activity' domain
filtered_papers = df_papers[(df_papers['year'] == 2016) & (df_papers['domain'].apply(lambda x: 'physical activity' in [d.lower() for d in x] if x else False))]

result = filtered_papers[['title']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-12002833206080555708': ['paper_docs'], 'var_function-call-13583694419194179142': 'file_storage/function-call-13583694419194179142.json'}

exec(code, env_args)

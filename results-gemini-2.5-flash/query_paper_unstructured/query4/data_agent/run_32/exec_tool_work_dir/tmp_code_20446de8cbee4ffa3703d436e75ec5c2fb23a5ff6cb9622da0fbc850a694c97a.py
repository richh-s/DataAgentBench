code = """import pandas as pd
import re
import json

papers_data = json.loads(open(locals()['var_function-call-15170204365258580789'], 'r').read())
processed_papers = []

for paper in papers_data:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Improved year extraction: search for common publication year patterns
    # e.g., in headers like 'PROCEEDINGS OF THE 2016 ACM CONFERENCE' or 'Vol. 1, No. 1, January 2016'
    year_match = re.search(r'(?:19|20)\d{2}', text)
    year = int(year_match.group(0)) if year_match else None
    
    # Check for 'physical activity' in the text to identify domain
    domain = 'physical activity' if 'physical activity' in text.lower() else None
    
    processed_papers.append({
        'title': title,
        'year': year,
        'domain': domain
    })

df_papers = pd.DataFrame(processed_papers)

# Filter for papers published in 2016 and in the 'physical activity' domain
filtered_papers_df = df_papers[
    (df_papers['year'] == 2016) & 
    (df_papers['domain'] == 'physical activity')
]

# Select only title for the next step (querying citations)
result = filtered_papers_df[['title']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-7039050370988840032': ['paper_docs'], 'var_function-call-15170204365258580789': 'file_storage/function-call-15170204365258580789.json', 'var_function-call-9037997024857941593': []}

exec(code, env_args)

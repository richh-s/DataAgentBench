code = """import pandas as pd
import re
import json

papers_data = json.loads(open(locals()['var_function-call-15170204365258580789'], 'r').read())
processed_papers = []

for paper in papers_data:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Try a different way to define the regex string for year
    year_pattern = "(19|20)\\d{2}"
    year_match = re.search(year_pattern, text)
    year = int(year_match.group(0)) if year_match else None
    
    # Use a different way to define the regex string for domain as well
    domain_pattern = "Domain:\\s*([^\\n]+)"
    domain_match = re.search(domain_pattern, text, re.IGNORECASE)
    domain = domain_match.group(1).strip() if domain_match else None
    
    if not domain:
        if "physical activity" in text.lower():
            domain = "physical activity"
    
    processed_papers.append({
        'title': title,
        'year': year,
        'domain': domain
    })

df_papers = pd.DataFrame(processed_papers)

filtered_papers_df = df_papers[
    (df_papers['year'] == 2016) & 
    (df_papers['domain'].str.contains('physical activity', case=False, na=False))
]

result = filtered_papers_df[['title']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-7039050370988840032': ['paper_docs'], 'var_function-call-15170204365258580789': 'file_storage/function-call-15170204365258580789.json'}

exec(code, env_args)

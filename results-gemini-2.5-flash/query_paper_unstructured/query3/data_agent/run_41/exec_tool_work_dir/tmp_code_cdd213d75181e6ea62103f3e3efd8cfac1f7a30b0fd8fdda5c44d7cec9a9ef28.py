code = """import pandas as pd
import re
import json

def extract_info(paper_text):
    year_match = re.search(r'(?:19|20)\d{2}', paper_text)
    year = int(year_match.group(0)) if year_match else None

    contribution_match = re.search(r'contribution: ([a-zA-Z, ]+)', paper_text, re.IGNORECASE)
    contribution = contribution_match.group(1).lower() if contribution_match else ''

    return year, contribution

all_papers_raw = json.loads(open(locals()['var_function-call-6785631912200159982'], 'r').read())

papers_data = []
for paper in all_papers_raw:
    title = paper['filename'].replace('.txt', '')
    year, contribution = extract_info(paper['text'])
    papers_data.append({'title': title, 'year': year, 'contribution': contribution})

papers_df = pd.DataFrame(papers_data)

filtered_papers_df = papers_df[
    (papers_df['year'].notna()) &
    (papers_df['year'] > 2016) &
    (papers_df['contribution'].str.contains('empirical', na=False))
].copy()

titles_to_query = filtered_papers_df['title'].tolist()
print('__RESULT__:')
print(json.dumps(titles_to_query))"""

env_args = {'var_function-call-6234541250907072384': ['paper_docs'], 'var_function-call-6785631912200159982': 'file_storage/function-call-6785631912200159982.json'}

exec(code, env_args)

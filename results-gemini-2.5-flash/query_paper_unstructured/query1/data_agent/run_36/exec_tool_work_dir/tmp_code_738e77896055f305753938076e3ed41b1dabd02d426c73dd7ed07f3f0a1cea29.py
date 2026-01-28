code = """import json
import pandas as pd

# Assuming locals()['var_function-call-13298366518058555331'] is already a Python list of dicts
food_papers_df = pd.DataFrame(locals()['var_function-call-13298366518058555331'])

with open(locals()['var_function-call-7863868404992433912'], 'r') as f:
    citations_data = json.load(f)
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = citations_df['citation_count'].astype(int)

merged_df = pd.merge(food_papers_df, citations_df, on='title', how='inner')
total_citations = merged_df['citation_count'].sum()

print('__RESULT__:')
print(json.dumps(int(total_citations)))"""

env_args = {'var_function-call-770696393874806011': ['paper_docs'], 'var_function-call-15880041372856478765': 'file_storage/function-call-15880041372856478765.json', 'var_function-call-13298366518058555331': [{'title': 'A Lived Informatics Model of Personal Informatics'}, {'title': 'A Stage-based Model of Personal Informatics Systems'}], 'var_function-call-7863868404992433912': 'file_storage/function-call-7863868404992433912.json'}

exec(code, env_args)

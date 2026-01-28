code = """import pandas as pd
import json

citations_data = pd.DataFrame(json.load(open(locals()['var_function-call-2554314523922120333'], 'r')))
paper_docs_data = json.load(open(locals()['var_function-call-12851751822495553569'], 'r'))

chi_papers = []
for doc in paper_docs_data:
    if "CHI" in doc['text']:
        title = doc['filename'].replace('.txt', '')
        chi_papers.append({'title': title})

chi_papers_df = pd.DataFrame(chi_papers)

merged_df = pd.merge(citations_data, chi_papers_df, on='title', how='inner')
merged_df['citation_count'] = pd.to_numeric(merged_df['citation_count'])

total_citations = merged_df['citation_count'].sum()

print("__RESULT__:")
print(json.dumps(str(total_citations)))"""

env_args = {'var_function-call-15172063648808244022': ['Citations', 'sqlite_sequence'], 'var_function-call-2554314523922120333': 'file_storage/function-call-2554314523922120333.json', 'var_function-call-12851751822495553569': 'file_storage/function-call-12851751822495553569.json'}

exec(code, env_args)

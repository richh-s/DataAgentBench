code = """import pandas as pd
import re
import json

papers_data = json.loads(open(locals()['var_function-call-14890926156089513429'], 'r').read())

extracted_papers = []
for paper in papers_data:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')

    # Check for 'physical activity' and '2016' anywhere in the text (case-insensitive)
    if 'physical activity' in text.lower() and '2016' in text:
        extracted_papers.append({
            'title': title
        })

df_filtered_papers = pd.DataFrame(extracted_papers).drop_duplicates(subset=['title'])

citations_data = json.loads(open(locals()['var_function-call-16257161724348090214'], 'r').read())
df_citations = pd.DataFrame(citations_data)

# Ensure 'citation_count' is numeric
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'], errors='coerce')

# Group by title and sum citation counts
df_total_citations = df_citations.groupby('title')['citation_count'].sum().reset_index()
df_total_citations.rename(columns={'citation_count': 'total_citation_count'}, inplace=True)

# Merge filtered papers with total citation counts
result = pd.merge(df_filtered_papers, df_total_citations, on='title', how='inner')

# Select and reorder columns for the final output
final_result = result[['title', 'total_citation_count']]

print('__RESULT__:')
print(final_result.to_json(orient='records'))"""

env_args = {'var_function-call-12243833719420803506': ['paper_docs'], 'var_function-call-12656719124189789220': [], 'var_function-call-14890926156089513429': 'file_storage/function-call-14890926156089513429.json', 'var_function-call-18429680994506560701': [], 'var_function-call-6495032645474842279': ['Citations', 'sqlite_sequence'], 'var_function-call-16257161724348090214': 'file_storage/function-call-16257161724348090214.json', 'var_function-call-8408877477184277707': []}

exec(code, env_args)

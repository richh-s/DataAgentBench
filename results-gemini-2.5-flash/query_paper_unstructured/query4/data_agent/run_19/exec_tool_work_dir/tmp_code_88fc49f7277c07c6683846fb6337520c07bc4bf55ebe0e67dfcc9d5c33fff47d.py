code = """import json
import pandas as pd

citations_data = locals()['var_function-call-1642100287304137362']
df_citations = pd.DataFrame(citations_data)

# Ensure 'citation_count' is numeric
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

# Group by title and sum citation counts
total_citations_by_title = df_citations.groupby('title')['citation_count'].sum().reset_index()

result = total_citations_by_title.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-14428271549656226849': ['paper_docs'], 'var_function-call-1819138674056248880': 'file_storage/function-call-1819138674056248880.json', 'var_function-call-15955492775391050376': [], 'var_function-call-8361182827540506550': ['Citations', 'sqlite_sequence'], 'var_function-call-1642100287304137362': [{'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'citation_count': '12'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity', 'citation_count': '65'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'citation_count': '36'}, {'title': 'SweatAtoms: Materializing Physical Activity', 'citation_count': '61'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity', 'citation_count': '39'}, {'title': 'Low Sampling Rate for Physical Activity Recognition', 'citation_count': '88'}], 'var_function-call-880522876073640375': 'file_storage/function-call-880522876073640375.json'}

exec(code, env_args)

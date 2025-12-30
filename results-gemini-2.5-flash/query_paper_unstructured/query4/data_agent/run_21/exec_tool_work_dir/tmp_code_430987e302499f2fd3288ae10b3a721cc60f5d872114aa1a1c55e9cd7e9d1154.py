code = """import json
import pandas as pd

physical_activity_2016_titles = locals()['var_function-call-6532722806137569957']
all_citations = pd.DataFrame(json.load(open(locals()['var_function-call-976136314626732420'], 'r')))

# Convert 'citation_count' to numeric, handling potential errors
all_citations['citation_count'] = pd.to_numeric(all_citations['citation_count'], errors='coerce')

# Filter for papers with titles matching our list
filtered_citations = all_citations[all_citations['title'].isin(physical_activity_2016_titles)]

# Group by title and sum citation counts
total_citations_per_paper = filtered_citations.groupby('title')['citation_count'].sum().reset_index()

result = total_citations_per_paper.to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-17798319154585505742': ['paper_docs'], 'var_function-call-12002591806772645320': 'file_storage/function-call-12002591806772645320.json', 'var_function-call-13349807814290358084': [], 'var_function-call-976136314626732420': 'file_storage/function-call-976136314626732420.json', 'var_function-call-12719539591056404857': 'file_storage/function-call-12719539591056404857.json', 'var_function-call-12927970392808823710': [], 'var_function-call-2017477155051187807': 'file_storage/function-call-2017477155051187807.json', 'var_function-call-6532722806137569957': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App']}

exec(code, env_args)

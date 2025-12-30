code = """import json
import pandas as pd

# The result from previous tool calls are directly available as variables
empirical_papers = locals()['var_function-call-4515139313189798668']
empirical_papers_df = pd.DataFrame(empirical_papers)

citations_data = locals()['var_function-call-5668481134127269008']
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Merge the two dataframes on 'title'
merged_df = pd.merge(empirical_papers_df, citations_df, on='title', how='inner')

# Group by title and sum the citation counts
total_citations = merged_df.groupby('title')['citation_count'].sum().reset_index()

# Convert the result to a list of dictionaries for the final answer
result = total_citations.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-11120416126101380269': ['paper_docs'], 'var_function-call-558217748425387803': 'file_storage/function-call-558217748425387803.json', 'var_function-call-18112218132182732411': [], 'var_function-call-6036035642582270495': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'contribution': ''}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'contribution': ''}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'contribution': ''}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'contribution': ''}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'contribution': ''}], 'var_function-call-4515139313189798668': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'contribution': 'empirical'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'contribution': 'empirical'}], 'var_function-call-5668481134127269008': 'file_storage/function-call-5668481134127269008.json'}

exec(code, env_args)

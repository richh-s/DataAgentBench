code = """import json
import pandas as pd

citations_data = locals()['var_function-call-4248888189195137632']
df_citations = pd.DataFrame(citations_data)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

total_citations = df_citations.groupby('title')['citation_count'].sum().reset_index()

result = total_citations.to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_function-call-894598418542309128': [{'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a870', 'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}, {'_id': '694f5530284b10b11dc0a871', 'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt"}, {'_id': '694f5530284b10b11dc0a873', 'filename': 'Charting Design Preferences on Wellness Wearables.txt'}], 'var_function-call-82359061990851726': 'file_storage/function-call-82359061990851726.json', 'var_function-call-2980401902330467936': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'var_function-call-4248888189195137632': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '49'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '11'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '71'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '38'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '81'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '65'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '98'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '23'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '65'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '14'}]}

exec(code, env_args)

code = """import json

# Get result from previous execution
result_key = 'var_functions.execute_python:22'
result_data = locals().get(result_key, [])

# Format the output
output = []
for paper in result_data:
    output.append(f"Title: {paper['title']}")
    output.append(f"Total Citation Count: {paper['total_citation_count']}")
    output.append("")

# Join all lines
final_text = "\n".join(output).strip()

print('__RESULT__:')
print(json.dumps(final_text))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:8': [{'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'filename': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System.txt", 'year': 2018, 'venue': 'CHI', 'source': 'ACM', 'contribution': ['empirical'], 'domains': ['productivity', 'social interactions', 'chronic', 'health_behavior', 'physical activity', 'screen time', 'food', 'mental', 'location', 'diabetes']}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': [{'title': 'Communicating Uncertainty in Fertility Prognosis', 'filename': 'Communicating Uncertainty in Fertility Prognosis.txt', 'year': 2019, 'venue': 'CHI', 'source': 'ACM', 'contribution': ['artifact', 'empirical', 'methodological'], 'domains': ['location', 'screen time', 'mental', 'physical activity', 'productivity', 'sleep', 'social interactions', 'chronic', 'health_behavior']}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'total_citation_count': 266}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'total_citation_count': 265}]}

exec(code, env_args)

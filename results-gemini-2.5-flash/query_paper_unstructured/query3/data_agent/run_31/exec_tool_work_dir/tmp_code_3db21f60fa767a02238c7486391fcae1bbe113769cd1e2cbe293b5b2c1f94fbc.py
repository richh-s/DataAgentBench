code = """import pandas as pd
import json

empirical_papers_titles = locals()['var_function-call-12624134951779882537']

# Convert the list of titles into a comma-separated string for the SQL IN clause
titles_str = ", ".join([f"'{title.replace("'", "''")}'" for title in empirical_papers_titles])

sql_query = f"SELECT title, SUM(citation_count) as total_citation_count FROM Citations WHERE title IN ({titles_str}) GROUP BY title;"

print('__RESULT__:')
print(json.dumps(sql_query))"""

env_args = {'var_function-call-3744194182005610721': ['paper_docs'], 'var_function-call-16572885030136982066': 'file_storage/function-call-16572885030136982066.json', 'var_function-call-16217772059205383965': [], 'var_function-call-10815164578185853792': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None}], 'var_function-call-10122900059300949010': [], 'var_function-call-13614726233522118016': [], 'var_function-call-14011783932993274675': ['Citations', 'sqlite_sequence'], 'var_function-call-3802482114764520810': 'file_storage/function-call-3802482114764520810.json', 'var_function-call-11167228524830664294': [], 'var_function-call-16752884826487934025': [], 'var_function-call-12624134951779882537': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App']}

exec(code, env_args)

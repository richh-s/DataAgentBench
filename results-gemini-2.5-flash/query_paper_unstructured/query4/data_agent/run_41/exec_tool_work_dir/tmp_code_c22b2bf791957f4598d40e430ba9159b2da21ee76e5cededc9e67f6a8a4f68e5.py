code = """import pandas as pd
import json

titles_for_sql = locals()['var_function-call-16886126537183334187']

# Construct the SQL query using the titles_for_sql string
query = f"SELECT title, SUM(citation_count) AS total_citation_count FROM Citations WHERE title IN ({titles_for_sql}) AND citation_year = 2016 GROUP BY title;"

print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_function-call-3869615726933000262': ['paper_docs'], 'var_function-call-4813969159932217082': 'file_storage/function-call-4813969159932217082.json', 'var_function-call-14316110536064693623': [], 'var_function-call-15112818109314081286': [], 'var_function-call-15130475667034523207': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'domain': 'physical activity'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'domain': 'physical activity'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'domain': 'physical activity'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'domain': 'physical activity'}], 'var_function-call-8875254147032335027': [], 'var_function-call-650437496942161048': [], 'var_function-call-15118086362885599179': [], 'var_function-call-13175390580521902847': [], 'var_function-call-15773914921340073216': [], 'var_function-call-709345038532913717': [], 'var_function-call-43256416273635476': [], 'var_function-call-481143422120979226': [], 'var_function-call-3354319114006429502': [], 'var_function-call-4486004858097618832': [{'title': 'A Lived Informatics Model of Personal Informatics'}, {'title': 'A Stage-based Model of Personal Informatics Systems'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'}], 'var_function-call-16886126537183334187': "'A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'"}

exec(code, env_args)

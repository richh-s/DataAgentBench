code = """import pandas as pd
import json

papers_in_domain = json.loads(locals()['var_function-call-4486004858097618832'])

titles = [paper['title'] for paper in papers_in_domain]

# Convert the list of titles to a JSON string compatible with SQL IN clause
titles_str = json.dumps(titles)

print('__RESULT__:')
print(titles_str)"""

env_args = {'var_function-call-3869615726933000262': ['paper_docs'], 'var_function-call-4813969159932217082': 'file_storage/function-call-4813969159932217082.json', 'var_function-call-14316110536064693623': [], 'var_function-call-15112818109314081286': [], 'var_function-call-15130475667034523207': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'domain': 'physical activity'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'domain': 'physical activity'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'domain': 'physical activity'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'domain': 'physical activity'}], 'var_function-call-8875254147032335027': [], 'var_function-call-650437496942161048': [], 'var_function-call-15118086362885599179': [], 'var_function-call-13175390580521902847': [], 'var_function-call-15773914921340073216': [], 'var_function-call-709345038532913717': [], 'var_function-call-43256416273635476': [], 'var_function-call-481143422120979226': [], 'var_function-call-3354319114006429502': [], 'var_function-call-4486004858097618832': [{'title': 'A Lived Informatics Model of Personal Informatics'}, {'title': 'A Stage-based Model of Personal Informatics Systems'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'}]}

exec(code, env_args)

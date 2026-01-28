code = """import json

paper_filenames_with_food = locals()['var_function-call-881789165318142022']
food_paper_titles = [doc['filename'].replace('.txt', '') for doc in paper_filenames_with_food]

print("__RESULT__:")
print(json.dumps(food_paper_titles))"""

env_args = {'var_function-call-8792593880583760035': ['paper_docs'], 'var_function-call-9978232910626699419': [], 'var_function-call-6497029258880074568': ['Citations', 'sqlite_sequence'], 'var_function-call-6893631717039984758': 'file_storage/function-call-6893631717039984758.json', 'var_function-call-9273036665786985738': [], 'var_function-call-14011650007027942934': [], 'var_function-call-14088742416694697934': [], 'var_function-call-16474795332048429470': 'file_storage/function-call-16474795332048429470.json', 'var_function-call-17548400387868776684': [], 'var_function-call-881789165318142022': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86e', 'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'_id': '694f5530284b10b11dc0a870', 'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}]}

exec(code, env_args)

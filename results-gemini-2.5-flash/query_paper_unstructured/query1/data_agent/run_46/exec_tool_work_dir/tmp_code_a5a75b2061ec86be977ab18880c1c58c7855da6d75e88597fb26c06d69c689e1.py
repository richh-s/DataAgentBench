code = """import json
import re

with open(locals()['var_function-call-16474795332048429470'], 'r') as f:
    paper_docs = json.load(f)

food_related_paper_titles = []
for doc in paper_docs:
    text = doc['text']
    title = doc['filename'].replace('.txt', '')
    
    # Search for the word 'food' (case-insensitive) anywhere in the text
    if re.search(r'\bfood\b', text, re.IGNORECASE):
        food_related_paper_titles.append(title)

food_related_paper_titles = list(set(food_related_paper_titles))

print("__RESULT__:")
print(json.dumps(food_related_paper_titles))"""

env_args = {'var_function-call-8792593880583760035': ['paper_docs'], 'var_function-call-9978232910626699419': [], 'var_function-call-6497029258880074568': ['Citations', 'sqlite_sequence'], 'var_function-call-6893631717039984758': 'file_storage/function-call-6893631717039984758.json', 'var_function-call-9273036665786985738': [], 'var_function-call-14011650007027942934': [], 'var_function-call-14088742416694697934': [], 'var_function-call-16474795332048429470': 'file_storage/function-call-16474795332048429470.json'}

exec(code, env_args)

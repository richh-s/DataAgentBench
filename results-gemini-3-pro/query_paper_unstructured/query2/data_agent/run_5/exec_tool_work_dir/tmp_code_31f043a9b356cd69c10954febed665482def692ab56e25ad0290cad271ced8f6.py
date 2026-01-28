code = """import json
import pandas as pd

# Load citations
with open(locals()['var_function-call-5217440467597246773'], 'r') as f:
    citations_data = json.load(f)

# Load mongo filenames
with open(locals()['var_function-call-17735979059542958878'], 'r') as f:
    mongo_files = json.load(f)

# Create a set of titles cited in 2018
citations_df = pd.DataFrame(citations_data)
# Ensure citation_count is int
citations_df['citation_count'] = citations_df['citation_count'].astype(int)
titles_2018 = set(citations_df['title'].tolist())

# Create a list of filenames to fetch
files_to_fetch = []
matched_titles = []

for doc in mongo_files:
    filename = doc.get('filename', '')
    if filename.endswith('.txt'):
        title_from_file = filename[:-4]
        if title_from_file in titles_2018:
            files_to_fetch.append(filename)
            matched_titles.append(title_from_file)

print("__RESULT__:")
print(json.dumps({"count": len(files_to_fetch), "files": files_to_fetch}))"""

env_args = {'var_function-call-5217440467597246773': 'file_storage/function-call-5217440467597246773.json', 'var_function-call-5217440467597249358': 'file_storage/function-call-5217440467597249358.json', 'var_function-call-759420094200622563': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-6271403078682451453': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}, {'_id': '694f5530284b10b11dc0a86e'}, {'_id': '694f5530284b10b11dc0a86f'}, {'_id': '694f5530284b10b11dc0a870'}, {'_id': '694f5530284b10b11dc0a871'}, {'_id': '694f5530284b10b11dc0a872'}, {'_id': '694f5530284b10b11dc0a873'}, {'_id': '694f5530284b10b11dc0a874'}, {'_id': '694f5530284b10b11dc0a875'}, {'_id': '694f5530284b10b11dc0a876'}, {'_id': '694f5530284b10b11dc0a877'}, {'_id': '694f5530284b10b11dc0a878'}, {'_id': '694f5530284b10b11dc0a879'}, {'_id': '694f5530284b10b11dc0a87a'}, {'_id': '694f5530284b10b11dc0a87b'}, {'_id': '694f5530284b10b11dc0a87c'}, {'_id': '694f5530284b10b11dc0a87d'}, {'_id': '694f5530284b10b11dc0a87e'}, {'_id': '694f5530284b10b11dc0a87f'}, {'_id': '694f5530284b10b11dc0a880'}, {'_id': '694f5530284b10b11dc0a881'}, {'_id': '694f5530284b10b11dc0a882'}, {'_id': '694f5530284b10b11dc0a883'}, {'_id': '694f5530284b10b11dc0a884'}, {'_id': '694f5530284b10b11dc0a885'}, {'_id': '694f5530284b10b11dc0a886'}, {'_id': '694f5530284b10b11dc0a887'}, {'_id': '694f5530284b10b11dc0a888'}, {'_id': '694f5530284b10b11dc0a889'}, {'_id': '694f5530284b10b11dc0a88a'}, {'_id': '694f5530284b10b11dc0a88b'}, {'_id': '694f5530284b10b11dc0a88c'}, {'_id': '694f5530284b10b11dc0a88d'}, {'_id': '694f5530284b10b11dc0a88e'}, {'_id': '694f5530284b10b11dc0a88f'}, {'_id': '694f5530284b10b11dc0a890'}, {'_id': '694f5530284b10b11dc0a891'}, {'_id': '694f5530284b10b11dc0a892'}, {'_id': '694f5530284b10b11dc0a893'}, {'_id': '694f5530284b10b11dc0a894'}, {'_id': '694f5530284b10b11dc0a895'}, {'_id': '694f5530284b10b11dc0a896'}, {'_id': '694f5530284b10b11dc0a897'}, {'_id': '694f5530284b10b11dc0a898'}, {'_id': '694f5530284b10b11dc0a899'}, {'_id': '694f5530284b10b11dc0a89a'}, {'_id': '694f5530284b10b11dc0a89b'}, {'_id': '694f5530284b10b11dc0a89c'}, {'_id': '694f5530284b10b11dc0a89d'}, {'_id': '694f5530284b10b11dc0a89e'}, {'_id': '694f5530284b10b11dc0a89f'}, {'_id': '694f5530284b10b11dc0a8a0'}, {'_id': '694f5530284b10b11dc0a8a1'}, {'_id': '694f5530284b10b11dc0a8a2'}, {'_id': '694f5530284b10b11dc0a8a3'}, {'_id': '694f5530284b10b11dc0a8a4'}, {'_id': '694f5530284b10b11dc0a8a5'}, {'_id': '694f5530284b10b11dc0a8a6'}, {'_id': '694f5530284b10b11dc0a8a7'}, {'_id': '694f5530284b10b11dc0a8a8'}, {'_id': '694f5530284b10b11dc0a8a9'}, {'_id': '694f5530284b10b11dc0a8aa'}, {'_id': '694f5530284b10b11dc0a8ab'}, {'_id': '694f5530284b10b11dc0a8ac'}, {'_id': '694f5530284b10b11dc0a8ad'}, {'_id': '694f5530284b10b11dc0a8ae'}, {'_id': '694f5530284b10b11dc0a8af'}, {'_id': '694f5530284b10b11dc0a8b0'}, {'_id': '694f5530284b10b11dc0a8b1'}, {'_id': '694f5530284b10b11dc0a8b2'}, {'_id': '694f5530284b10b11dc0a8b3'}, {'_id': '694f5530284b10b11dc0a8b4'}, {'_id': '694f5530284b10b11dc0a8b5'}, {'_id': '694f5530284b10b11dc0a8b6'}, {'_id': '694f5530284b10b11dc0a8b7'}, {'_id': '694f5530284b10b11dc0a8b8'}, {'_id': '694f5530284b10b11dc0a8b9'}, {'_id': '694f5530284b10b11dc0a8ba'}, {'_id': '694f5530284b10b11dc0a8bb'}, {'_id': '694f5530284b10b11dc0a8bc'}, {'_id': '694f5530284b10b11dc0a8bd'}, {'_id': '694f5530284b10b11dc0a8be'}, {'_id': '694f5530284b10b11dc0a8bf'}, {'_id': '694f5530284b10b11dc0a8c0'}, {'_id': '694f5530284b10b11dc0a8c1'}, {'_id': '694f5530284b10b11dc0a8c2'}, {'_id': '694f5530284b10b11dc0a8c3'}, {'_id': '694f5530284b10b11dc0a8c4'}, {'_id': '694f5530284b10b11dc0a8c5'}, {'_id': '694f5530284b10b11dc0a8c6'}, {'_id': '694f5530284b10b11dc0a8c7'}, {'_id': '694f5530284b10b11dc0a8c8'}, {'_id': '694f5530284b10b11dc0a8c9'}, {'_id': '694f5530284b10b11dc0a8ca'}, {'_id': '694f5530284b10b11dc0a8cb'}], 'var_function-call-17735979059542958878': 'file_storage/function-call-17735979059542958878.json'}

exec(code, env_args)

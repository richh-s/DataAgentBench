code = """import json
import pandas as pd
import re

docs_path = locals()['var_function-call-6365592025106147893']
with open(docs_path, 'r') as f:
    docs_data = json.load(f)
df_docs = pd.DataFrame(docs_data)
df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)

words_found = []

def find_food_words(row):
    text = row['text'].lower()[:3000]
    # Find all words containing 'food'
    matches = re.findall(r'[a-z]*food[a-z]*', text)
    if matches:
        words_found.extend(matches)
        return True
    return False

df_docs['has_food_substr'] = df_docs.apply(find_food_words, axis=1)

# Count frequency of each word
from collections import Counter
word_counts = Counter(words_found)

print("__RESULT__:")
print(json.dumps(word_counts))"""

env_args = {'var_function-call-4548718859833522719': 'file_storage/function-call-4548718859833522719.json', 'var_function-call-1373040785545021376': 'file_storage/function-call-1373040785545021376.json', 'var_function-call-14795720345132237503': 'file_storage/function-call-14795720345132237503.json', 'var_function-call-6365592025106147893': 'file_storage/function-call-6365592025106147893.json', 'var_function-call-3244531972049241208': 0, 'var_function-call-168795103559867264': 390, 'var_function-call-6799362587997118290': {'total_citations': 0, 'paper_count': 0, 'papers': []}}

exec(code, env_args)

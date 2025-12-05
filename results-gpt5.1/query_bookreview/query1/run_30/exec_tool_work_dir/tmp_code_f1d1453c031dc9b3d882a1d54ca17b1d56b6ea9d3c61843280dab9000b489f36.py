code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_KshLFUwbCSbeplb9ScB0maeo, 'r') as f:
    books = json.load(f)
with open(var_call_BHk2IHcgCXhb9vX856qgcPrF, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Extract publication year from details using regex for 4-digit years between 1800 and 2099
year_pattern = re.compile(r'(18|19|20)\d{2}')

def extract_year(text):
    if not isinstance(text, str):
        return None
    years = [int(y) for y in year_pattern.findall(text) if isinstance(y, str)]
    # year_pattern with groups returns tuples; adjust

print('__RESULT__:')
print(json.dumps('error'))"""

env_args = {'var_call_KshLFUwbCSbeplb9ScB0maeo': 'file_storage/call_KshLFUwbCSbeplb9ScB0maeo.json', 'var_call_LHUzTIG8UR2Wakp1c2fEiOKD': ['books_info'], 'var_call_q1aorycwM6QTrlIDzitq7Ga3': ['review'], 'var_call_BHk2IHcgCXhb9vX856qgcPrF': 'file_storage/call_BHk2IHcgCXhb9vX856qgcPrF.json'}

exec(code, env_args)

code = """import json, re, pandas as pd
from pathlib import Path

# Load full books details
path = Path(var_call_ZKj6lHIhrRdeYcuYlrjmiwSs)
with path.open() as f:
    books = json.load(f)

df_books = pd.DataFrame(books)[['book_id','details']]

# Extract publication year from details text using regex
year_pattern = re.compile(r'(19|20)\d{2}')

def extract_year(text):
    if not isinstance(text, str):
        return None
    years = [int(y) for y in year_pattern.findall(text) if isinstance(y, str)]
    # year_pattern with groups returns tuples, so adjust

# Fix: recompile without groups
year_pattern2 = re.compile(r'(?:19|20)\d{2}')

def extract_year2(text):
    if not isinstance(text, str):
        return None
    yrs = [int(y) for y in year_pattern2.findall(text)]
    return min(yrs) if yrs else None

df_books['year'] = df_books['details'].apply(extract_year2)

# compute decade
df_books['decade'] = (df_books['year'] // 10 * 10).astype('Int64')

# We cannot get review data table list, so stop here with message
result = 'Cannot access review data: table review_database is missing in SQLite DB.'

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ZKj6lHIhrRdeYcuYlrjmiwSs': 'file_storage/call_ZKj6lHIhrRdeYcuYlrjmiwSs.json'}

exec(code, env_args)

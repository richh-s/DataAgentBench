code = """import json
import pandas as pd

# Load the result from the previous query
with open('var_function-call-10727912544765417180.json', 'r') as f:
    books_data = json.load(f)

# Convert to DataFrame
df_books = pd.DataFrame(books_data)

# Filter for English books
# The details field is a string. We'll check if "English" is in it.
# We also check if 'Literature & Fiction' is in categories just in case the SQL LIKE wasn't precise enough (though it should be fine).
def is_english(details):
    if not isinstance(details, str):
        return False
    return "English" in details

# Filter
df_books_filtered = df_books[df_books['details'].apply(is_english)]

# We need book_id and title
english_lit_books = df_books_filtered[['book_id', 'title']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(english_lit_books))"""

env_args = {'var_function-call-10727912544765417180': 'file_storage/function-call-10727912544765417180.json'}

exec(code, env_args)

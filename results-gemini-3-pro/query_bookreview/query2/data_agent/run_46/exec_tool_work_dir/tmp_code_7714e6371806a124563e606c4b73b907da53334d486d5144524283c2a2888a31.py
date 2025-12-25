code = """import json
import pandas as pd

# Get the file path from the variable
file_path = locals()['var_function-call-10727912544765417180']

# Load the result
with open(file_path, 'r') as f:
    books_data = json.load(f)

# Convert to DataFrame
df_books = pd.DataFrame(books_data)

# Filter for English books
def is_english(details):
    if not isinstance(details, str):
        return False
    return "English" in details

# Filter
df_books_filtered = df_books[df_books['details'].apply(is_english)]

# We need book_id and title. 
# Storing book_ids to a list to use for intersection later.
english_lit_book_ids = df_books_filtered['book_id'].unique().tolist()
# Also keeping the mapping
english_lit_books_map = df_books_filtered.set_index('book_id')['title'].to_dict()

# Print the list of book_ids to be used in the next step (or just keep them in storage if possible, but I need to return something)
# I'll return the map so I can use it later.
print("__RESULT__:")
print(json.dumps(english_lit_books_map))"""

env_args = {'var_function-call-10727912544765417180': 'file_storage/function-call-10727912544765417180.json'}

exec(code, env_args)

code = """import json
import pandas as pd

# Load the books data
books_file = var_functions.query_db:2
with open(books_file, 'r') as f:
    books_data = json.load(f)

# Load the review data
reviews_file = var_functions.query_db:6
with open(reviews_file, 'r') as f:
    reviews_data = json.load(f)

# Convert to DataFrames
books_df = pd.DataFrame(books_data)
reviews_df = pd.DataFrame(reviews_data)

# Display the structure
print(f"Books dataframe shape: {books_df.shape}")
print(f"Books columns: {books_df.columns.tolist()}")
print(f"\nReviews dataframe shape: {reviews_df.shape}")
print(f"Reviews columns: {reviews_df.columns.tolist()}")

# Show a few sample rows
print("\nBooks data sample:")
print(books_df.head(2).to_string())
print("\nReviews data sample:")
print(reviews_df.head(5).to_string())"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

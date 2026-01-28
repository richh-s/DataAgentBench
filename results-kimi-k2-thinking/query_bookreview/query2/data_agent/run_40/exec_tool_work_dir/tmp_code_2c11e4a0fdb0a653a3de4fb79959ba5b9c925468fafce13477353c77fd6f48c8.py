code = """import json
import pandas as pd

# Read the full books data from the stored file
books_file_path = locals()['var_functions.query_db:0']
with open(books_file_path, 'r') as f:
    books_data = json.load(f)

# Read the filtered English Literature & Fiction books data
lit_fiction_books = locals()['var_functions.query_db:2']

# Create DataFrames
df_books = pd.DataFrame(books_data)
df_lit_fiction = pd.DataFrame(lit_fiction_books)

# Show basic info
print("__RESULT__:")
print(json.dumps({
    "total_books": len(df_books),
    "lit_fiction_books": len(df_lit_fiction),
    "sample_categories": df_books['categories'].head(3).tolist(),
    "sample_details": df_books['details'].head(3).tolist()
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'book_id': 'bookid_1', 'title': 'Chaucer'}, {'book_id': 'bookid_9', 'title': 'Reunion: The Children of Lauderdale Park'}, {'book_id': 'bookid_13', 'title': 'Girl Made of Glass'}, {'book_id': 'bookid_30', 'title': 'Sugary Sweets (A Taste of Love Series)'}, {'book_id': 'bookid_36', 'title': 'Therapy Mammals'}, {'book_id': 'bookid_37', 'title': "A Most Dangerous Book: Tacitus's Germania from the Roman Empire to the Third Reich"}, {'book_id': 'bookid_38', 'title': 'The Prophet: With Original 1923 Illustrations by the Author'}, {'book_id': 'bookid_39', 'title': 'The Melancholy Strumpet Master'}, {'book_id': 'bookid_44', 'title': 'Reptilian'}, {'book_id': 'bookid_49', 'title': 'Primeval: A Journal of the Uncanny - Issue #1'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)'}, {'book_id': 'bookid_69', 'title': 'Out of Sheer Rage: Wrestling with D. H. Lawrence'}, {'book_id': 'bookid_70', 'title': 'Polly and the Shadow Goblin: Book 2, Mother of Witches'}, {'book_id': 'bookid_74', 'title': 'Child Of The King A Journey of Hope Book 1: Earthly Story With A Heavenly Message'}, {'book_id': 'bookid_77', 'title': 'One September Morning'}, {'book_id': 'bookid_82', 'title': 'Fire Cracker'}, {'book_id': 'bookid_84', 'title': 'Local Honey'}, {'book_id': 'bookid_89', 'title': "I'll Ride For My Hood: A Salty Love Story"}, {'book_id': 'bookid_92', 'title': 'Outage'}, {'book_id': 'bookid_93', 'title': 'Simantov'}, {'book_id': 'bookid_98', 'title': 'Hollywood Confessions: Hollywood Headlines Book #3 (Hollywood Headlines Mysteries)'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear'}, {'book_id': 'bookid_101', 'title': 'Knowing When To Die: Uncollected Stories'}, {'book_id': 'bookid_106', 'title': 'Looking for Peyton Place: A Novel'}, {'book_id': 'bookid_109', 'title': 'All the Way to the Gallows'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?'}, {'book_id': 'bookid_122', 'title': 'Childe Harold of Dysna'}, {'book_id': 'bookid_137', 'title': 'Oligarchy'}, {'book_id': 'bookid_142', 'title': 'The Jordan Tracks'}, {'book_id': 'bookid_144', 'title': 'Forged in Blood (Freehold)'}, {'book_id': 'bookid_161', 'title': "Time's Demon: BOOK II OF THE ISLEVALE CYCLE"}, {'book_id': 'bookid_167', 'title': 'Dead Silence'}, {'book_id': 'bookid_171', 'title': 'Exits, Desires, & Slow Fires'}, {'book_id': 'bookid_177', 'title': 'Kennebago Moments'}, {'book_id': 'bookid_179', 'title': 'A Cherry Cola Christmas (A Cherry Cola Book Club Novel)'}, {'book_id': 'bookid_180', 'title': 'The Sludge'}, {'book_id': 'bookid_182', 'title': 'Liza of Lambeth'}, {'book_id': 'bookid_187', 'title': 'Consort (A Dark(ish) Faerie Tale Book 3)'}, {'book_id': 'bookid_188', 'title': "The Vampyre and Other Tales of the Macabre (Oxford World's Classics)"}, {'book_id': 'bookid_195', 'title': 'Something That Feels Like Truth (Switchgrass Books)'}], 'var_functions.list_db:4': ['review']}

exec(code, env_args)

code = """import json, pandas as pd
from pathlib import Path

# load reviews
path_rev = Path(var_call_RDugCTmYArNtQkNucSa9Sa1r)
reviews = json.loads(path_rev.read_text())
rev_df = pd.DataFrame(reviews)
rev_df['rating'] = rev_df['rating'].astype(float)

# load children's books list
child_books = pd.DataFrame(var_call_hPoETthYw6VF4D2pt1iPKvSO)

# average ratings per purchase_id
avg_rev = rev_df.groupby('purchase_id', as_index=False)['rating'].mean()

# join assuming purchase_id == book_id
merged = child_books.merge(avg_rev, left_on='book_id', right_on='purchase_id', how='left')

res = merged[merged['rating'] >= 4.5][['title','rating']].sort_values('rating', ascending=False)

result = res.to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_v1BnhDz5jM00TfZdLYAoJ9B1': 'file_storage/call_v1BnhDz5jM00TfZdLYAoJ9B1.json', 'var_call_buoKQxUhy2lg0wFK9XBGAH42': ['review'], 'var_call_RDugCTmYArNtQkNucSa9Sa1r': 'file_storage/call_RDugCTmYArNtQkNucSa9Sa1r.json', 'var_call_hPoETthYw6VF4D2pt1iPKvSO': [{'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still'}, {'book_id': 'bookid_14', 'title': 'The Old Man and the Pirate Princess'}, {'book_id': 'bookid_32', 'title': 'The Very Hungry Caterpillar (English and Arabic Edition)'}, {'book_id': 'bookid_40', 'title': 'Egypt (Enchantment of the World)'}, {'book_id': 'bookid_48', 'title': 'Clark the Shark: Tooth Trouble, No. 1'}, {'book_id': 'bookid_52', 'title': "I Hadn't Meant to Tell You This"}, {'book_id': 'bookid_54', 'title': 'Favorite Thorton W. Burgess Stories: 6 Books'}, {'book_id': 'bookid_55', 'title': 'Behind the Wheel (Choose Your Own Adventure #35)(Paperback/Revised)'}, {'book_id': 'bookid_57', 'title': "Goodnight Riley and the Moon, It's Almost Bedtime: Personalized Children’s Books, Personalized Gifts, and Bedtime Stories (A Magnificent Me! estorytime.com Series)"}, {'book_id': 'bookid_96', 'title': 'Cheer Up, Ben Franklin! (Young Historians)'}, {'book_id': 'bookid_99', 'title': 'Buddy the Soldier Bear'}, {'book_id': 'bookid_108', 'title': 'The Library Book'}, {'book_id': 'bookid_111', 'title': 'Can You Buy Me The Wind?'}, {'book_id': 'bookid_116', 'title': 'From the Earth to the Moon by Jules Verne, Fiction, Fantasy & Magic'}, {'book_id': 'bookid_120', 'title': "Caroline's Color Dreams: Los Sueños Coloridos De Carolina : Babl Children's Books in Spanish and English"}, {'book_id': 'bookid_124', 'title': 'Skeleton Play: A Fun, Rhyming Halloween Book for Kids! (1)'}, {'book_id': 'bookid_130', 'title': "Benny Goes To The Moon: The great new book from Top Children's entertainer Gerry Ogilvie (1)"}, {'book_id': 'bookid_132', 'title': 'Mae and Jane in the Rain'}, {'book_id': 'bookid_145', 'title': 'Kirsten: An American Girl : 1854 (The American Girls Collection/Boxed Set)'}, {'book_id': 'bookid_146', 'title': 'LunaLu the Llamacorn'}, {'book_id': 'bookid_149', 'title': 'Trouble in the CTC!: The Terra Prime Adventures Book 2'}, {'book_id': 'bookid_152', 'title': 'Around the World Mazes'}, {'book_id': 'bookid_158', 'title': 'Cleo Porter and the Body Electric'}, {'book_id': 'bookid_163', 'title': 'Monster Kisses'}, {'book_id': 'bookid_170', 'title': 'Pokémon: Sun & Moon, Vol. 8 (8)'}]}

exec(code, env_args)

code = """import pandas as pd
import json

citations_data_path = locals()['var_function-call-5799397423609889934']
with open(citations_data_path, 'r') as f:
    citations_data = json.load(f)
df_citations = pd.DataFrame(citations_data)

titles_from_citations_path = locals()['var_function-call-11018646388912384066']
with open(titles_from_citations_path, 'r') as f:
    titles_from_citations = json.load(f)

# Construct the MongoDB query
# The filename in paper_docs is title + ".txt"
filenames_to_query = [title + '.txt' for title in titles_from_citations]

# MongoDB query to get documents with matching filenames and containing 'ACM' in their text
# This query will fetch documents that match the title (filename) AND have 'ACM' in their text
# I will limit the projection to _id, filename, and text (to search for ACM)
mongo_query = {
    "collection": "paper_docs",
    "filter": {"filename": {"$in": filenames_to_query}, "text": {"$regex": "ACM"}},
    "projection": {"_id": 0, "filename": 1, "text": 1}
}
print('__RESULT__:')
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-5799397423609889934': 'file_storage/function-call-5799397423609889934.json', 'var_function-call-11018646388912384066': 'file_storage/function-call-11018646388912384066.json'}

exec(code, env_args)

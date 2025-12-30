code = """import json
import pandas as pd

with open(locals()['var_function-call-2744602299800751358'], 'r') as f:
    titles = json.load(f)

filenames = [title + '.txt' for title in titles]

# Construct MongoDB query to fetch documents by filename in batches
batch_size = 100
all_paper_docs = []
for i in range(0, len(filenames), batch_size):
    batch_filenames = filenames[i:i + batch_size]
    mongo_query = {
        'collection': 'paper_docs',
        'filter': {'filename': {'$in': batch_filenames}},
        'projection': {'_id': 0, 'filename': 1, 'text': 1}
    }
    # Calling query_db here would create multiple tool calls. It's better to make one tool call for all titles.
    # Let's assume a single query with $in will work for now, and if it fails, we'll try batching with separate tool calls.
    # For this exercise, I will generate a single query for all filenames. If it fails due to size, I'll revise.
    pass # I'll make the query_db call in the next step.

print('__RESULT__:')
print(json.dumps(filenames))"""

env_args = {'var_function-call-10626874306656494420': 'file_storage/function-call-10626874306656494420.json', 'var_function-call-2744602299800751358': 'file_storage/function-call-2744602299800751358.json'}

exec(code, env_args)

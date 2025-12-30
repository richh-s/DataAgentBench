code = """import json
import pandas as pd

with open(locals()['var_function-call-5369318911067814337'], 'r') as f:
    citations_2018_data = json.load(f)

df_citations = pd.DataFrame(citations_2018_data)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

titles = df_citations['title'].tolist()

# Construct a single MongoDB query to fetch all relevant paper documents.
# This will fetch documents where the filename (without .txt) is in the list of titles.
# This is more efficient than individual queries for each title.
# The filename field stores the title with a '.txt' extension.
# So, we need to add '.txt' to each title for the filter.

filenames_to_query = [title + '.txt' for title in titles]

# The query will be constructed in the next step to be passed to query_db.
# For now, let's prepare a list of titles for processing.

print('__RESULT__:')
print(json.dumps(filenames_to_query))"""

env_args = {'var_function-call-5369318911067814337': 'file_storage/function-call-5369318911067814337.json', 'var_function-call-14305652795573715301': 'file_storage/function-call-14305652795573715301.json'}

exec(code, env_args)

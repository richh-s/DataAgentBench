code = """import json
import pandas as pd

# Read the articles data - the variable contains the file path
with open(var_functions.query_db:4, 'r') as f:
    articles_data = json.load(f)

# Read the metadata data - the variable contains the file path  
with open(var_functions.query_db:6, 'r') as f:
    metadata_data = json.load(f)

# Convert to dataframes
articles_df = pd.DataFrame(articles_data)
metadata_df = pd.DataFrame(metadata_data)

# Basic info about the data
articles_info = f"Articles count: {len(articles_df)}, Columns: {list(articles_df.columns)}"
metadata_info = f"Metadata count: {len(metadata_df)}, Columns: {list(metadata_df.columns)}"

# Sample of data
sample_articles = articles_df.head(3).to_dict('records')
sample_metadata = metadata_df.head(3).to_dict('records')

result = {
    "articles_info": articles_info,
    "metadata_info": metadata_info,
    "sample_articles": sample_articles,
    "sample_metadata": sample_metadata
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

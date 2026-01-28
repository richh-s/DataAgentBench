code = """import json
import pandas as pd

# Load the metadata results from the file
metadata_file = var_functions.query_db:2

with open(metadata_file, 'r') as f:
    metadata = json.load(f)

# Convert to DataFrame
df_metadata = pd.DataFrame(metadata)

# Extract year from publication_date
df_metadata['year'] = pd.to_datetime(df_metadata['publication_date']).dt.year

# Count total articles per year
articles_per_year = df_metadata.groupby('year').size().reset_index(name='total_articles')

print('__RESULT__:')
print(json.dumps({
    'total_articles_by_year': articles_per_year.to_dict('records'),
    'unique_years': sorted(df_metadata['year'].unique()),
    'total_articles': len(df_metadata)
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

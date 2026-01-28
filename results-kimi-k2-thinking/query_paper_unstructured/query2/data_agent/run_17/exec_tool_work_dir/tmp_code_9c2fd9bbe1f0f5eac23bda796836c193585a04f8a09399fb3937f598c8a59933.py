code = """import json
import pandas as pd

# Read the file containing results from query 0
with open('/Users/Shared/wld9.json', 'r') as f:
    citations_2018 = json.load(f)

# Extract titles from the citation data
titles_2018 = [record['title'] for record in citations_2018]
print('Number of papers cited in 2018:', len(titles_2018))
print('First 10 titles:', titles_2018[:10])

# Also create a DataFrame for easier handling
df_citations = pd.DataFrame(citations_2018)
print('\nDataFrame shape:', df_citations.shape)
print('\nFirst few rows:')
print(df_citations.head())
__RESULT__: {
  "titles_count": len(titles_2018),
  "sample_titles": titles_2018[:10]
}"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

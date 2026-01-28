code = """import json
import pandas as pd

# Load the full citations data for 2020
with open('/tmp/tmpkfxl1v1z.json', 'r') as f:
    citations_2020 = json.load(f)

print(f"Total citations records for 2020: {len(citations_2020)}")

# Create a DataFrame for easier processing
df_citations = pd.DataFrame(citations_2020)
df_citations['citation_count'] = df_citations['citation_count'].astype(int)

# Show first few records
print("First few citation records:")
print(df_citations.head())

# Now let's query MongoDB for CHI papers
# We need to search the paper documents for CHI venue
print("\n=== Ready to query MongoDB for CHI papers ===")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

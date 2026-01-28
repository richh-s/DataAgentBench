code = """import json, re, pandas as pd

# Load full Mongo and SQL results if needed
mongo_path = var_call_hC5woDVdQZtTUWWsu2JQ5P7K
sql_path = var_call_ckjc81KzHWPkK4oBpFAlbXV1

with open(mongo_path, 'r') as f:
    mongo_records = json.load(f)
with open(sql_path, 'r') as f:
    sql_records = json.load(f)

# Build set of titles whose domain is 'food'
food_titles = set()
for doc in mongo_records:
    fname = doc.get('filename') or ''
    title = re.sub(r"\.txt$", "", fname).strip()
    text = (doc.get('text') or '').lower()
    # very rough domain inference: look for 'domain: food' style or strong food-tracking focus
    if 'domain: food' in text or ' food journaling' in text or ' food journal' in text or 'dietary self-tracking' in text or 'nutrition' in text or 'dietary' in text:
        if title:
            food_titles.add(title)

# Sum citations for food-domain titles
citations_df = pd.DataFrame(sql_records)
# citation counts are strings, convert
citations_df['total_citations'] = citations_df['total_citations'].astype(int)

food_citations = citations_df[citations_df['title'].isin(food_titles)]['total_citations'].sum()

result = json.dumps(int(food_citations))
print("__RESULT__:")
print(result)"""

env_args = {'var_call_hC5woDVdQZtTUWWsu2JQ5P7K': 'file_storage/call_hC5woDVdQZtTUWWsu2JQ5P7K.json', 'var_call_ckjc81KzHWPkK4oBpFAlbXV1': 'file_storage/call_ckjc81KzHWPkK4oBpFAlbXV1.json'}

exec(code, env_args)

code = """import json
import pandas as pd
with open(var_call_9CQTLa2tPxMrbUPXKsYcua73, 'r') as f:
    businesses = json.load(f)

biz_df = pd.DataFrame(businesses)
# get columns
cols = list(biz_df.columns)

# sample first 10 records
sample = biz_df.head(10).to_dict(orient='records')

# count how many have non-null categories
has_categories = biz_df['categories'].notnull().sum() if 'categories' in biz_df.columns else 0

# show distinct types of categories values (sample up to 20 unique)
unique_cats = None
if 'categories' in biz_df.columns:
    uniq = biz_df['categories'].dropna().unique().tolist()
    unique_cats = uniq[:20]

result = {
    'columns': cols,
    'has_categories_count': int(has_categories),
    'unique_categories_sample': unique_cats,
    'sample_records': sample
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_KJh4DBlhRfS7CFVVu8Hpsc9W': ['checkin', 'business'], 'var_call_qeaXw5PFvk6LbmOqVkjK6sii': ['review', 'tip', 'user'], 'var_call_9CQTLa2tPxMrbUPXKsYcua73': 'file_storage/call_9CQTLa2tPxMrbUPXKsYcua73.json', 'var_call_ujuxQXIXFWHgYM3XRFcu7bhu': 'file_storage/call_ujuxQXIXFWHgYM3XRFcu7bhu.json', 'var_call_lMev2pPOb85N2KUJnbPp4qir': {'category': None, 'business_count': 0, 'average_rating': None}}

exec(code, env_args)

code = """import json
import pandas as pd

# Load data from storage files
with open(var_call_NyANSHsT0pp50i9hthQm89mO, 'r') as f:
    businesses = json.load(f)
with open(var_call_RYSwkLtFyuvctp6g3elutqZP, 'r') as f:
    reviews = json.load(f)

# Helper to determine if business accepts credit cards
def accepts_credit(attr):
    if attr is None:
        return False
    try:
        # If it's a dict, convert to json string
        if isinstance(attr, dict):
            s = json.dumps(attr)
        else:
            s = str(attr)
    except Exception:
        s = str(attr)
    s_low = s.lower()
    return ('businessacceptscreditcards' in s_low) and ('true' in s_low)

# Build dataframe for businesses
b_df = pd.DataFrame(businesses)
# Ensure relevant columns exist
if 'business_id' not in b_df.columns:
    b_df['business_id'] = None
if 'categories' not in b_df.columns:
    b_df['categories'] = None
if 'attributes' not in b_df.columns:
    b_df['attributes'] = None

# Parse categories into list
def parse_categories(cat):
    if cat is None:
        return []
    if isinstance(cat, list):
        return [c.strip() for c in cat if c]
    if isinstance(cat, str):
        parts = [c.strip() for c in cat.split(',') if c.strip()]
        return parts
    return []

b_df['accepts_cc'] = b_df['attributes'].apply(accepts_credit)

b_df['category_list'] = b_df['categories'].apply(parse_categories)

# Filter businesses that accept credit cards and have at least one category
accepted = b_df[b_df['accepts_cc'] == True].copy()
accepted = accepted[accepted['category_list'].map(len) > 0]

# Explode categories
if not accepted.empty:
    exploded = accepted.explode('category_list')
    exploded = exploded.rename(columns={'category_list': 'category'})
    # Count unique businesses per category
    counts = exploded.groupby('category')['business_id'].nunique()
else:
    counts = pd.Series(dtype=int)

if counts.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    top_category = counts.idxmax()
    top_count = int(counts.max())

    # Get business_ids in this top category
    biz_ids = exploded[exploded['category'] == top_category]['business_id'].unique().tolist()
    # Convert to business_ref format
    biz_refs = [bid.replace('businessid_', 'businessref_') for bid in biz_ids]

    # Build reviews dataframe
    r_df = pd.DataFrame(reviews)
    if 'business_ref' not in r_df.columns or 'rating' not in r_df.columns:
        avg_rating = None
    else:
        r_df = r_df[r_df['business_ref'].isin(biz_refs)].copy()
        r_df['rating'] = pd.to_numeric(r_df['rating'], errors='coerce')
        if r_df['rating'].dropna().empty:
            avg_rating = None
        else:
            avg_rating = float(r_df['rating'].mean())

    result = {
        'category': top_category,
        'business_count': top_count,
        'average_rating': round(avg_rating, 2) if avg_rating is not None else None
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_M8u98Uy8RFv13XafDQjgabTI': ['business', 'checkin'], 'var_call_iE8J6ZLLldNRoFYaVzSWQny6': ['review', 'tip', 'user'], 'var_call_NyANSHsT0pp50i9hthQm89mO': 'file_storage/call_NyANSHsT0pp50i9hthQm89mO.json', 'var_call_RYSwkLtFyuvctp6g3elutqZP': 'file_storage/call_RYSwkLtFyuvctp6g3elutqZP.json'}

exec(code, env_args)

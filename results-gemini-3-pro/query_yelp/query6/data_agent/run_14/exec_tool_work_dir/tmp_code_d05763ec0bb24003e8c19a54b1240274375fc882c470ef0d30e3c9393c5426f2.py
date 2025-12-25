code = """import pandas as pd
import json

# Load the JSON file
file_path = locals()['var_function-call-15605530299019870726']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert rating to int
df['rating'] = df['rating'].astype(int)

# Convert date to datetime
# pd.to_datetime handles mixed formats if format is not specified, but might be slow or fail on weird ones.
# Given the formats, let's try allowing it to infer.
df['date_dt'] = pd.to_datetime(df['date'], errors='coerce')

# Check if any dates failed
failed = df[df['date_dt'].isna()]
if not failed.empty:
    print("Failed to parse some dates:", failed['date'].head().tolist())

# Filter by date range: Jan 1 2016 to June 30 2016
start_date = pd.Timestamp("2016-01-01")
end_date = pd.Timestamp("2016-06-30 23:59:59")
mask = (df['date_dt'] >= start_date) & (df['date_dt'] <= end_date)
filtered_df = df[mask]

# Aggregate
agg_df = filtered_df.groupby('business_ref').agg(
    avg_rating=('rating', 'mean'),
    review_count=('rating', 'count')
).reset_index()

# Filter count >= 5
valid_businesses = agg_df[agg_df['review_count'] >= 5]

# Find max avg rating
if valid_businesses.empty:
    result = "No businesses found with >= 5 reviews in the period."
else:
    top_business = valid_businesses.sort_values(by=['avg_rating', 'review_count'], ascending=[False, False]).iloc[0]
    result = top_business.to_dict()

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-13941239017043405944': ['review', 'tip', 'user'], 'var_function-call-14360248553740544898': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_count': '5'}], 'var_function-call-3147974840496666864': [{'date': 'August 01, 2016 at 03:44 AM'}], 'var_function-call-7083563283805629344': [{'count_star()': '2000'}], 'var_function-call-15605530299019870726': 'file_storage/function-call-15605530299019870726.json'}

exec(code, env_args)

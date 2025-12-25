code = """import pandas as pd
import json

# Load the reviews from the stored file
with open(locals()['var_function-call-7312146679102699008'], 'r') as f:
    reviews = json.load(f)

df = pd.DataFrame(reviews)

# Convert date column to datetime
# Using errors='coerce' to handle potential parsing errors, though we should inspect if many fail
df['date_dt'] = pd.to_datetime(df['date'], format='mixed')

# Filter by date range
start_date = pd.Timestamp('2016-01-01')
end_date = pd.Timestamp('2016-06-30')

# Extract date part only or compare timestamps?
# "between January 1, 2016 and June 30, 2016" usually implies the whole days.
# Check if time is included. The boundaries should probably be inclusive.
mask = (df['date_dt'] >= start_date) & (df['date_dt'] <= end_date + pd.Timedelta(days=1)) # To include the last day fully if timestamps have time
# Actually, strict between usually means >= start and <= end (end of day).
# Let's normalize to date for safer comparison or just use <= end_date 23:59:59.
# If I use date object comparison:
df['date_only'] = df['date_dt'].dt.date
mask = (df['date_only'] >= start_date.date()) & (df['date_only'] <= end_date.date())

filtered_df = df[mask]

# Group by business_ref
stats = filtered_df.groupby('business_ref').agg(
    avg_rating=('rating', lambda x: x.astype(int).mean()),
    count=('rating', 'count')
).reset_index()

# Filter count >= 5
candidates = stats[stats['count'] >= 5]

# Find highest average rating
if candidates.empty:
    print('__RESULT__:')
    print(json.dumps([]))
else:
    best = candidates.sort_values(by=['avg_rating', 'count'], ascending=[False, False])
    print('__RESULT__:')
    print(best.head(1).to_json(orient='records'))"""

env_args = {'var_function-call-10190353216909278636': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'num_reviews': '5'}], 'var_function-call-10190353216909275933': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-12823390688900469514': [{'date': 'August 01, 2016 at 03:44 AM'}, {'date': 'June 14, 2021 at 11:39 AM'}, {'date': '29 May 2013, 23:01'}, {'date': '21 May 2016, 18:48'}, {'date': 'November 01, 2021 at 05:11 PM'}], 'var_function-call-12823390688900469755': [{'count_star()': '38'}], 'var_function-call-8051533960699194059': [{'count_star()': '2000'}], 'var_function-call-7312146679102699008': 'file_storage/function-call-7312146679102699008.json'}

exec(code, env_args)

code = """import json
import pandas as pd
from datetime import datetime
import re

# Load the review data
file_path = locals()['var_functions.query_db:8']
if isinstance(file_path, str):
    with open(file_path, 'r') as f:
        review_data = json.load(f)
else:
    review_data = locals()['var_functions.query_db:8']

df_reviews = pd.DataFrame(review_data)

# Function to parse various date formats
def parse_date(date_str):
    if pd.isna(date_str) or date_str is None:
        return None
    
    date_str = str(date_str).strip()
    
    # Try different date formats
    formats = [
        '%B %d, %Y at %I:%M %p',  # August 01, 2016 at 03:44 AM
        '%d %B %Y, %H:%M',        # 29 May 2013, 23:01
        '%Y-%m-%d %H:%M:%S',      # 2013-07-08 21:47:00
        '%d %b %Y, %H:%M',        # 17 Apr 2017, 14:04
        '%Y-%m-%d %H:%M:%S.%f',   # With microseconds
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    
    # Try to extract date using regex patterns
    # Pattern for "Month DD, YYYY"
    match = re.search(r'(\w+)\s+(\d{1,2}),\s+(\d{4})', date_str)
    if match:
        try:
            month, day, year = match.groups()
            return datetime.strptime(f"{month} {day} {year}", '%B %d %Y')
        except:
            pass
    
    # Pattern for "DD Month YYYY"
    match = re.search(r'(\d{1,2})\s+(\w+)\s+(\d{4})', date_str)
    if match:
        try:
            day, month, year = match.groups()
            return datetime.strptime(f"{day} {month} {year}", '%d %B %Y')
        except:
            pass
    
    # Pattern for "YYYY-MM-DD"
    match = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_str)
    if match:
        try:
            year, month, day = match.groups()
            return datetime.strptime(f"{year}-{month}-{day}", '%Y-%m-%d')
        except:
            pass
    
    return None

# Parse dates and filter
df_reviews['parsed_date'] = df_reviews['date'].apply(parse_date)

# Filter for date range: January 1, 2016 to June 30, 2016
start_date = datetime(2016, 1, 1)
end_date = datetime(2016, 6, 30, 23, 59, 59)

mask = (df_reviews['parsed_date'] >= start_date) & (df_reviews['parsed_date'] <= end_date)
filtered_reviews = df_reviews[mask].copy()

# Count reviews per business (with at least 5 reviews)
review_counts = filtered_reviews['business_ref'].value_counts()
eligible_businesses = review_counts[review_counts >= 5].index

# Filter to only eligible businesses
filtered_reviews_eligible = filtered_reviews[filtered_reviews['business_ref'].isin(eligible_businesses)]

# Calculate average rating for each eligible business
avg_ratings = filtered_reviews_eligible.groupby('business_ref')['rating'].apply(
    lambda x: sum(map(int, x)) / len(x)
).reset_index()
avg_ratings.columns = ['business_ref', 'avg_rating']

# Sort by average rating descending
avg_ratings_sorted = avg_ratings.sort_values('avg_rating', ascending=False)

print('__RESULT__:')
print(json.dumps({
    'total_reviews': len(df_reviews),
    'reviews_in_range': len(filtered_reviews),
    'eligible_businesses_count': len(eligible_businesses),
    'business_with_avg_ratings': len(avg_ratings_sorted),
    'top_businesses': avg_ratings_sorted.head(10).to_dict('records'),
    'review_counts_preview': dict(list(review_counts.head(10).items()))
}))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool'}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar'}, {'business_id': 'businessid_88', 'name': 'Impact Guns'}, {'business_id': 'businessid_41', 'name': 'Palms Primary Care'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails'}, {'business_id': 'businessid_74', 'name': 'Candy Barrel'}, {'business_id': 'businessid_92', 'name': 'Luminosity'}, {'business_id': 'businessid_64', 'name': 'Nail Care Salon'}, {'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis'}, {'business_id': 'businessid_29', 'name': "Aster's Floral Shop"}], 'var_functions.list_db:5': ['review', 'tip', 'user'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'preview': ['August 01, 2016 at 03:44 AM', 'June 14, 2021 at 11:39 AM', '29 May 2013, 23:01', '21 May 2016, 18:48', 'November 01, 2021 at 05:11 PM', '2013-07-08 21:47:00', 'March 02, 2009 at 09:43 PM', 'March 16, 2014 at 12:40 AM', 'September 18, 2014 at 05:50 PM', '17 Apr 2017, 14:04'], 'total_reviews': 2000}}

exec(code, env_args)

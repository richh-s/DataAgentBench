code = """import json
import pandas as pd
from datetime import datetime
import re

# Read the review data from the file
file_path = var_functions.query_db:6
with open(file_path, 'r') as f:
    reviews = json.load(f)

# Convert to DataFrame
df_reviews = pd.DataFrame(reviews)

# Check the time formats and convert to datetime
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])

print("Sample of time field:")
print(df_reviews['time'].head(10).tolist())
print(f"Total reviews with rating >= 4.5: {len(df_reviews)}")

# Try to parse the time field to extract year from 2019
# The time format appears to be inconsistent. Let's try different approaches

def extract_year(time_str):
    if pd.isna(time_str):
        return None
    
    time_str = str(time_str)
    
    # Try various date patterns
    patterns = [
        r'\b2019\b',  # Just the year
        r'(\d{4})-\d{2}-\d{2}',  # YYYY-MM-DD
        r'(\d{4})-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',  # YYYY-MM-DD HH:MM:SS
        r'(\d{2}) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{4}',  # DD Mon YYYY with comma
        r'(\d{2}) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{4}\b',  # DD Mon YYYY without comma
        r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d{1,2}), (\d{4})',  # Mon DD, YYYY
        r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d{1,2}) (\d{4})',  # Mon DD YYYY
        r'(\d{1,2}) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{4}',  # DD Mon YYYY
    ]
    
    for pattern in patterns:
        match = re.search(pattern, time_str, re.IGNORECASE)
        if match:
            # Extract the year from the match
            groups = match.groups()
            for group in groups:
                if group and group.isdigit() and len(group) == 4:
                    return int(group)
    
    return None

# Apply the extraction
df_reviews['year'] = df_reviews['time'].apply(extract_year)

# Check unique years
unique_years = df_reviews['year'].value_counts().sort_index()
print("\nYear distribution:")
print(unique_years.head(20))

# Filter for 2019
reviews_2019 = df_reviews[df_reviews['year'] == 2019]
print(f"\nReviews from 2019: {len(reviews_2019)}")

# Count reviews per business for 2019
if len(reviews_2019) > 0:
    business_counts = reviews_2019.groupby('gmap_id').size().reset_index(name='high_rating_review_count')
    top_businesses = business_counts.sort_values('high_rating_review_count', ascending=False).head(3)
    print(f"\nTop 3 businesses by high-rating reviews in 2019:")
    print(top_businesses)
else:
    print("No reviews found for 2019")
    # Check what years we actually have
    print(f"Available years: {sorted(df_reviews['year'].dropna().unique())}")"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

code = """import json
import pandas as pd
from datetime import datetime
import re

# Load the review data
review_data_path = var_functions.query_db:7
print(f"Loading data from: {review_data_path}")

with open(review_data_path, 'r') as f:
    reviews = json.load(f)

print(f"Total reviews with rating >= 4.5: {len(reviews)}")

# Show sample of time formats
sample_times = [r['time'] for r in reviews[:10]]
print("Sample time formats:")
for t in sample_times:
    print(f"  '{t}'")

# Try to parse dates and filter for 2019
def parse_review_date(time_str):
    """Parse various time string formats from reviews"""
    if not time_str:
        return None
    
    # Try different patterns
    patterns = [
        # "September 03, 2020 at 04:15 PM"
        (r'(\w+)\s+(\d{1,2}),\s+(\d{4})\s+at\s+([\d:]+)\s+(AM|PM)', 
         lambda m: f"{m.group(3)}-{m.group(1)}-{m.group(2)} {m.group(4)} {m.group(5)}"),
        
        # "2021-04-12 17:07:52"
        (r'(\d{4})-(\d{2})-(\d{2})\s+([\d:]+)', 
         lambda m: f"{m.group(1)}-{m.group(2)}-{m.group(3)} {m.group(4)}"),
        
        # "2018-04-23 16:24:26"
        (r'(\d{4})-(\d{2})-(\d{2})\s+([\d:]+)', 
         lambda m: f"{m.group(1)}-{m.group(2)}-{m.group(3)} {m.group(4)}"),
        
        # "2017-07-10 22:12:19"
        (r'(\d{4})-(\d{2})-(\d{2})\s+([\d:]+)', 
         lambda m: f"{m.group(1)}-{m.group(2)}-{m.group(3)} {m.group(4)}"),
        
        # "18 Jan 2019, 03:19"
        (r'(\d{1,2})\s+(\w+)\s+(\d{4}),?\s+([\d:]+)', 
         lambda m: f"{m.group(3)}-{m.group(2)}-{m.group(1)} {m.group(4)}"),
        
        # "29 Sep 2020, 17:28"
        (r'(\d{1,2})\s+(\w+)\s+(\d{4}),?\s+([\d:]+)', 
         lambda m: f"{m.group(3)}-{m.group(2)}-{m.group(1)} {m.group(4)}"),
        
        # "06 Jan 2019, 02:45"
        (r'(\d{1,2})\s+(\w+)\s+(\d{4}),?\s+([\d:]+)', 
         lambda m: f"{m.group(3)}-{m.group(2)}-{m.group(1)} {m.group(4)}"),
        
        # "23 Jan 2021, 16:35"
        (r'(\d{1,2})\s+(\w+)\s+(\d{4}),?\s+([\d:]+)', 
         lambda m: f"{m.group(3)}-{m.group(2)}-{m.group(1)} {m.group(4)}"),
        
        # "19 Jan 2021, 20:17"
        (r'(\d{1,2})\s+(\w+)\s+(\d{4}),?\s+([\d:]+)', 
         lambda m: f"{m.group(3)}-{m.group(2)}-{m.group(1)} {m.group(4)}"),
    ]
    
    time_str_clean = time_str.strip()
    
    for pattern, formatter in patterns:
        match = re.match(pattern, time_str_clean, re.IGNORECASE)
        if match:
            try:
                formatted = formatter(match)
                # Try to parse with pandas
                return pd.to_datetime(formatted, errors='coerce')
            except:
                continue
    
    # Fallback: try pandas parser directly
    try:
        return pd.to_datetime(time_str_clean, errors='coerce')
    except:
        pass
    
    return None

# Test date parsing
print("\nTesting date parsing:")
for t in sample_times:
    parsed = parse_review_date(t)
    print(f"  '{t}' -> {parsed}")

# Process all reviews
reviews_2019 = []
for review in reviews:
    parsed_date = parse_review_date(review['time'])
    if parsed_date and parsed_date.year == 2019:
        reviews_2019.append({
            'gmap_id': review['gmap_id'],
            'rating': float(review['rating']),
            'time': review['time'],
            'parsed_date': parsed_date
        })

print(f"\nReviews from 2019 with rating >= 4.5: {len(reviews_2019)}")

# Count by gmap_id
from collections import Counter
business_counts = Counter([r['gmap_id'] for r in reviews_2019])
top_businesses = business_counts.most_common(5)

print("\nTop 5 businesses by high-rating review count:")
for gmap_id, count in top_businesses:
    print(f"  {gmap_id}: {count}")

# Save results for next steps
result = {
    'reviews_2019': reviews_2019,
    'top_business_ids': [b[0] for b in top_businesses]
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)

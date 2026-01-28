code = """import json
import re
from collections import Counter

# Get the file path from storage
result_file = locals()['var_functions.query_db:6']

# Read the full result from the file
with open(result_file, 'r') as f:
    reviews = json.load(f)

# Filter for 2019 reviews with rating >= 4.5
# The time field has various formats, so we need to be flexible
def extract_year(time_str):
    if not time_str:
        return None
    
    # Try different patterns
    patterns = [
        r'(\d{4})-\d{2}-\d{2}',  # 2021-04-12
        r'(\d{4})-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}',  # 2018-04-23 16:24:26
        r'(\d{1,2})\s+(\w+)\s+(\d{4})',  # 18 Jan 2019, 03:19
    ]
    
    for pattern in patterns:
        match = re.search(pattern, time_str, re.IGNORECASE)
        if match:
            if len(match.groups()) == 1:
                return int(match.group(1))
            elif len(match.groups()) == 3:
                # day month year format
                if match.group(3).isdigit() and len(match.group(3)) == 4:
                    return int(match.group(3))
    
    # Try format: February 21, 2020 at
    match = re.search(r'(\w+)\s+\d{1,2},\s+(\d{4})', time_str)
    if match:
        return int(match.group(2))
    
    # Try format: September 03, 2020
    match = re.search(r'(\w+)\s+\d{1,2},\s+(\d{4})', time_str)
    if match:
        return int(match.group(2))
    
    # Try format: May 19, 2021 at
    match = re.search(r'(\w+)\s+\d{1,2},\s+(\d{4})\s+at', time_str)
    if match:
        return int(match.group(2))
    
    return None

# Filter reviews
filtered_reviews = []
for review in reviews:
    try:
        rating = float(review.get('rating', 0))
        time_str = review.get('time', '')
        
        if rating >= 4.5:
            year = extract_year(time_str)
            if year == 2019:
                filtered_reviews.append({
                    'gmap_id': review.get('gmap_id'),
                    'rating': rating,
                    'time': time_str
                })
    except (ValueError, TypeError):
        continue

# Count by business
business_counts = Counter([r['gmap_id'] for r in filtered_reviews])

# Get top 3 businesses
top_3 = business_counts.most_common(3)

print('__RESULT__:')
print(json.dumps({
    'top_businesses': top_3,
    'total_filtered_reviews': len(filtered_reviews)
}))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}], 'var_functions.query_db:5': [{'time': 'September 03, 2020 at 04:15 PM'}, {'time': '2021-04-12 17:07:52'}, {'time': '2018-04-23 16:24:26'}, {'time': '2017-07-10 22:12:19'}, {'time': 'May 19, 2021 at 03:55 AM'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

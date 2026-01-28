code = """import json
import re
from datetime import datetime

# Read the full review data
file_path = locals()['var_functions.query_db:18']
with open(file_path, 'r') as f:
    all_reviews = json.load(f)

# Function to parse various date formats
def parse_date(date_str):
    formats = [
        '%Y-%m-%d %H:%M:%S',  # 2021-04-12 17:07:52
        '%B %d, %Y at %I:%M %p',  # September 03, 2020 at 04:15 PM
        '%Y-%m-%d %H:%M:%S',  # 2018-04-23 16:24:26
        '%Y-%m-%d %H:%M:%S',  # 2017-07-10 22:12:19
        '%d %b %Y, %H:%M',     # 18 Jan 2019, 03:19
        '%d %b %Y, %H:%M',     # 29 Sep 2020, 17:28
        '%B %d, %Y at %I:%M %p',  # June 10, 2018 at 02:23 AM
        '%B %d, %Y at %I:%M %p',  # March 07, 2019 at 12:56 AM
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    
    # Try to extract year from the string if parsing fails
    year_match = re.search(r'\b(201[5-9]|202[0-1])\b', date_str)
    if year_match:
        return datetime(int(year_match.group(1)), 1, 1)
    
    return None

# Filter reviews from 2019
reviews_2019 = []
for review in all_reviews:
    date_obj = parse_date(review['time'])
    if date_obj and date_obj.year == 2019:
        reviews_2019.append(review)

print(f"Total reviews with rating >= 4.5: {len(all_reviews)}")
print(f"Reviews from 2019 with rating >= 4.5: {len(reviews_2019)}")

# Group by gmap_id and count
from collections import Counter
counter = Counter()
for review in reviews_2019:
    counter[review['gmap_id']] += 1

# Get top 10 for preview
top_10 = counter.most_common(10)
print("__RESULT__:")
print(json.dumps([(gmap_id, count) for gmap_id, count in top_10]))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_29', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_16', 'rating': '5'}, {'gmap_id': 'gmap_26', 'rating': '5'}, {'gmap_id': 'gmap_2', 'rating': '5'}, {'gmap_id': 'gmap_2', 'rating': '5'}, {'gmap_id': 'gmap_2', 'rating': '5'}, {'gmap_id': 'gmap_30', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_72', 'rating': '5'}, {'gmap_id': 'gmap_72', 'rating': '5'}, {'gmap_id': 'gmap_72', 'rating': '5'}, {'gmap_id': 'gmap_72', 'rating': '5'}, {'gmap_id': 'gmap_72', 'rating': '5'}, {'gmap_id': 'gmap_63', 'rating': '5'}, {'gmap_id': 'gmap_65', 'rating': '5'}, {'gmap_id': 'gmap_51', 'rating': '5'}, {'gmap_id': 'gmap_59', 'rating': '5'}, {'gmap_id': 'gmap_59', 'rating': '5'}, {'gmap_id': 'gmap_57', 'rating': '5'}, {'gmap_id': 'gmap_57', 'rating': '5'}, {'gmap_id': 'gmap_13', 'rating': '5'}, {'gmap_id': 'gmap_14', 'rating': '5'}, {'gmap_id': 'gmap_3', 'rating': '5'}, {'gmap_id': 'gmap_3', 'rating': '5'}, {'gmap_id': 'gmap_35', 'rating': '5'}, {'gmap_id': 'gmap_35', 'rating': '5'}, {'gmap_id': 'gmap_35', 'rating': '5'}, {'gmap_id': 'gmap_35', 'rating': '5'}, {'gmap_id': 'gmap_35', 'rating': '5'}, {'gmap_id': 'gmap_35', 'rating': '5'}, {'gmap_id': 'gmap_7', 'rating': '5'}, {'gmap_id': 'gmap_7', 'rating': '5'}, {'gmap_id': 'gmap_5', 'rating': '5'}, {'gmap_id': 'gmap_5', 'rating': '5'}, {'gmap_id': 'gmap_34', 'rating': '5'}, {'gmap_id': 'gmap_11', 'rating': '5'}, {'gmap_id': 'gmap_11', 'rating': '5'}, {'gmap_id': 'gmap_11', 'rating': '5'}, {'gmap_id': 'gmap_62', 'rating': '5'}, {'gmap_id': 'gmap_62', 'rating': '5'}, {'gmap_id': 'gmap_62', 'rating': '5'}, {'gmap_id': 'gmap_62', 'rating': '5'}, {'gmap_id': 'gmap_62', 'rating': '5'}, {'gmap_id': 'gmap_58', 'rating': '5'}, {'gmap_id': 'gmap_56', 'rating': '5'}, {'gmap_id': 'gmap_56', 'rating': '5'}, {'gmap_id': 'gmap_56', 'rating': '5'}, {'gmap_id': 'gmap_46', 'rating': '5'}, {'gmap_id': 'gmap_46', 'rating': '5'}, {'gmap_id': 'gmap_46', 'rating': '5'}, {'gmap_id': 'gmap_46', 'rating': '5'}, {'gmap_id': 'gmap_46', 'rating': '5'}, {'gmap_id': 'gmap_47', 'rating': '5'}, {'gmap_id': 'gmap_47', 'rating': '5'}, {'gmap_id': 'gmap_71', 'rating': '5'}, {'gmap_id': 'gmap_69', 'rating': '5'}, {'gmap_id': 'gmap_69', 'rating': '5'}, {'gmap_id': 'gmap_69', 'rating': '5'}, {'gmap_id': 'gmap_64', 'rating': '5'}, {'gmap_id': 'gmap_64', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}], 'var_functions.execute_python:6': [{'gmap_id': 'gmap_20', 'high_rating_count': 8}, {'gmap_id': 'gmap_53', 'high_rating_count': 7}, {'gmap_id': 'gmap_35', 'high_rating_count': 6}, {'gmap_id': 'gmap_40', 'high_rating_count': 6}, {'gmap_id': 'gmap_72', 'high_rating_count': 5}, {'gmap_id': 'gmap_62', 'high_rating_count': 5}, {'gmap_id': 'gmap_46', 'high_rating_count': 5}, {'gmap_id': 'gmap_17', 'high_rating_count': 4}, {'gmap_id': 'gmap_2', 'high_rating_count': 3}, {'gmap_id': 'gmap_11', 'high_rating_count': 3}], 'var_functions.execute_python:8': ['gmap_20', 'gmap_53', 'gmap_35'], 'var_functions.query_db:10': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_35', 'name': 'Encino Dermatology & Laser: Alex Khadavi MD'}], 'var_functions.execute_python:12': [{'business_name': 'Aurora Massage', 'high_rating_review_count': 8}, {'business_name': 'The Boochyard @ Local Roots', 'high_rating_review_count': 7}, {'business_name': 'Encino Dermatology & Laser: Alex Khadavi MD', 'high_rating_review_count': 6}], 'var_functions.query_db:14': [{'gmap_id': 'gmap_11', 'rating': '5'}, {'gmap_id': 'gmap_11', 'rating': '5'}, {'gmap_id': 'gmap_11', 'rating': '5'}, {'gmap_id': 'gmap_13', 'rating': '5'}, {'gmap_id': 'gmap_14', 'rating': '5'}, {'gmap_id': 'gmap_16', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_2', 'rating': '5'}, {'gmap_id': 'gmap_2', 'rating': '5'}, {'gmap_id': 'gmap_2', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_26', 'rating': '5'}, {'gmap_id': 'gmap_29', 'rating': '5'}, {'gmap_id': 'gmap_3', 'rating': '5'}, {'gmap_id': 'gmap_3', 'rating': '5'}, {'gmap_id': 'gmap_30', 'rating': '5'}, {'gmap_id': 'gmap_34', 'rating': '5'}, {'gmap_id': 'gmap_35', 'rating': '5'}, {'gmap_id': 'gmap_35', 'rating': '5'}, {'gmap_id': 'gmap_35', 'rating': '5'}, {'gmap_id': 'gmap_35', 'rating': '5'}, {'gmap_id': 'gmap_35', 'rating': '5'}, {'gmap_id': 'gmap_35', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_46', 'rating': '5'}, {'gmap_id': 'gmap_46', 'rating': '5'}, {'gmap_id': 'gmap_46', 'rating': '5'}, {'gmap_id': 'gmap_46', 'rating': '5'}, {'gmap_id': 'gmap_46', 'rating': '5'}, {'gmap_id': 'gmap_47', 'rating': '5'}, {'gmap_id': 'gmap_47', 'rating': '5'}, {'gmap_id': 'gmap_5', 'rating': '5'}, {'gmap_id': 'gmap_5', 'rating': '5'}, {'gmap_id': 'gmap_51', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_56', 'rating': '5'}, {'gmap_id': 'gmap_56', 'rating': '5'}, {'gmap_id': 'gmap_56', 'rating': '5'}, {'gmap_id': 'gmap_57', 'rating': '5'}, {'gmap_id': 'gmap_57', 'rating': '5'}, {'gmap_id': 'gmap_58', 'rating': '5'}, {'gmap_id': 'gmap_59', 'rating': '5'}, {'gmap_id': 'gmap_59', 'rating': '5'}, {'gmap_id': 'gmap_62', 'rating': '5'}, {'gmap_id': 'gmap_62', 'rating': '5'}, {'gmap_id': 'gmap_62', 'rating': '5'}, {'gmap_id': 'gmap_62', 'rating': '5'}, {'gmap_id': 'gmap_62', 'rating': '5'}, {'gmap_id': 'gmap_63', 'rating': '5'}, {'gmap_id': 'gmap_64', 'rating': '5'}, {'gmap_id': 'gmap_64', 'rating': '5'}, {'gmap_id': 'gmap_65', 'rating': '5'}, {'gmap_id': 'gmap_69', 'rating': '5'}, {'gmap_id': 'gmap_69', 'rating': '5'}, {'gmap_id': 'gmap_69', 'rating': '5'}, {'gmap_id': 'gmap_7', 'rating': '5'}, {'gmap_id': 'gmap_7', 'rating': '5'}, {'gmap_id': 'gmap_71', 'rating': '5'}, {'gmap_id': 'gmap_72', 'rating': '5'}, {'gmap_id': 'gmap_72', 'rating': '5'}, {'gmap_id': 'gmap_72', 'rating': '5'}, {'gmap_id': 'gmap_72', 'rating': '5'}, {'gmap_id': 'gmap_72', 'rating': '5'}], 'var_functions.query_db:16': [{'gmap_id': 'gmap_44', 'rating': '5', 'time': 'September 03, 2020 at 04:15 PM'}, {'gmap_id': 'gmap_44', 'rating': '5', 'time': '2021-04-12 17:07:52'}, {'gmap_id': 'gmap_44', 'rating': '5', 'time': '2018-04-23 16:24:26'}, {'gmap_id': 'gmap_44', 'rating': '5', 'time': '2017-07-10 22:12:19'}, {'gmap_id': 'gmap_41', 'rating': '5', 'time': 'June 12, 2021 at 06:15 PM'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': [{'gmap_id': 'gmap_44', 'rating': '5', 'time': 'September 03, 2020 at 04:15 PM'}, {'gmap_id': 'gmap_44', 'rating': '5', 'time': '2021-04-12 17:07:52'}, {'gmap_id': 'gmap_44', 'rating': '5', 'time': '2018-04-23 16:24:26'}, {'gmap_id': 'gmap_44', 'rating': '5', 'time': '2017-07-10 22:12:19'}, {'gmap_id': 'gmap_41', 'rating': '5', 'time': 'June 12, 2021 at 06:15 PM'}]}

exec(code, env_args)

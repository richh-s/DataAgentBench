code = """import json
import re
from datetime import datetime

# Read the full review data from the file
with open('var_functions.query_db:10', 'r') as f:
    reviews_2016 = json.load(f)

print(f"Total reviews in 2016: {len(reviews_2016)}")

# Define date parsing function
def parse_date(date_str):
    if not date_str:
        return None
    
    date_str = date_str.strip()
    
    # Try different date formats
    formats = [
        '%Y-%m-%d %H:%M:%S',  # 2016-01-01 02:46:00
        '%d %b %Y, %H:%M',    # 21 May 2016, 18:48
        '%B %d, %Y at %I:%M %p',  # August 01, 2016 at 03:44 AM
        '%Y-%m-%d %H:%M:%S.%f',  # 2016-06-28 02:18:33.123
        '%d %b %Y, %H:%M:%S',  # 29 Sep 2016, 02:01:00
        '%Y-%m-%d %H:%M',     # 2016-03-12 14:19
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    
    # Try to extract date parts manually for edge cases
    try:
        # Extract year, month, day
        year_match = re.search(r'2016', date_str)
        if not year_match:
            return None
            
        # Look for month names or numbers
        month_match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December|[0-9]{1,2})', date_str)
        day_match = re.search(r'([0-9]{1,2})', date_str)
        
        if month_match and day_match:
            month_str = month_match.group(1)
            if month_str.isdigit():
                month = int(month_str)
            else:
                month_map = {
                    'January': 1, 'February': 2, 'March': 3, 'April': 4,
                    'May': 5, 'June': 6, 'July': 7, 'August': 8,
                    'September': 9, 'October': 10, 'November': 11, 'December': 12
                }
                month = month_map.get(month_str, 1)
            
            day = int(day_match.group(1))
            return datetime(2016, month, day)
    except:
        pass
    
    return None

# Parse dates and filter for Jan 1 - Jun 30, 2016
start_date = datetime(2016, 1, 1)
end_date = datetime(2016, 6, 30, 23, 59, 59)

filtered_reviews = []
for review in reviews_2016:
    parsed_date = parse_date(review['date'])
    if parsed_date and start_date <= parsed_date <= end_date:
        filtered_reviews.append({
            'business_ref': review['business_ref'],
            'rating': int(review['rating']),
            'date': str(parsed_date)
        })

print(f"Reviews in date range (Jan 1 - Jun 30, 2016): {len(filtered_reviews)}")

# Group by business and calculate average rating and review count
business_stats = {}
for review in filtered_reviews:
    biz_ref = review['business_ref']
    if biz_ref not in business_stats:
        business_stats[biz_ref] = {
            'ratings': [],
            'count': 0
        }
    business_stats[biz_ref]['ratings'].append(review['rating'])
    business_stats[biz_ref]['count'] += 1

# Calculate averages and filter for businesses with at least 5 reviews
business_averages = []
for biz_ref, stats in business_stats.items():
    if stats['count'] >= 5:
        avg_rating = sum(stats['ratings']) / len(stats['ratings'])
        business_averages.append({
            'business_ref': biz_ref,
            'avg_rating': avg_rating,
            'review_count': stats['count']
        })

# Sort by average rating (descending)
business_averages.sort(key=lambda x: x['avg_rating'], reverse=True)

print(f"Businesses with >= 5 reviews in date range: {len(business_averages)}")

# Display top 10 for debugging
print("Top 10 businesses by average rating:")
for i, biz in enumerate(business_averages[:10]):
    print(f"{i+1}. {biz['business_ref']}: avg={biz['avg_rating']:.2f}, count={biz['review_count']}")

# Store results for next step
result = {
    'filtered_reviews': filtered_reviews,
    'business_averages': business_averages
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.list_db:2': ['review', 'tip', 'user'], 'var_functions.query_db:4': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:6': [{'review_id': 'reviewid_135', 'user_id': 'userid_548', 'business_ref': 'businessref_34', 'rating': '2', 'useful': '0', 'funny': '0', 'cool': '0', 'text': "Sure, it's cheap, but there isn't much to see. I think you'd have to have a big interest in the topic to find it exciting, and kids would be bored. I think it only lasted maybe 10-15 minutes. Our tour person was somewhat knowledgeable and seemed into it, but he didn't give us much time to read the information on each level. I had to take photos of the plaques to read later, and half of them need replacing, as they are so sun-bleached they're virtually unreadable (tour guide said they're being replaced soon and that the other half were already replaced). I really thought it needed to be higher up to give a good view. The Lewis and Clark State Historic Site just down the road was more interesting and free. If you live around here like I do and have nothing better to do, you might want to give it a go if the topic interests you, but if you're a tourist, this is not something you should waste your time on.", 'date': 'August 01, 2016 at 03:44 AM'}, {'review_id': 'reviewid_1067', 'user_id': 'userid_213', 'business_ref': 'businessref_89', 'rating': '5', 'useful': '2', 'funny': '0', 'cool': '0', 'text': 'Very good service but a little pricey for the services your receive. Clean and sanitary too', 'date': 'June 14, 2021 at 11:39 AM'}, {'review_id': 'reviewid_871', 'user_id': 'userid_616', 'business_ref': 'businessref_82', 'rating': '4', 'useful': '0', 'funny': '0', 'cool': '0', 'text': 'My friend and I enjoyed a fantastic meal at Miles Table and I can\'t wait to return! Given that it was half-price-burger-day, I felt the need to give the falafel burger a shot. It was delicious! I\'m not always a falafel fan, but this "burger" was awesome. The brioche bun was the perfect consistency and the portion of fries was plentiful. My friend enjoyed the cobb salad (though she requested balsamic dressing instead of buttermilk and she received buttermilk). The restaurant is quaint and has ample seating. While you order at the counter, our "server" (I believe her name was Sarah) was fantastic and made sure we had everything we needed. Overall, this is a great spot and I will be back soon...I may have to make it a weekly lunch staple!', 'date': '29 May 2013, 23:01'}], 'var_functions.query_db:8': [{'business_ref': 'businessref_34', 'rating': '2', 'date': 'August 01, 2016 at 03:44 AM'}, {'business_ref': 'businessref_66', 'rating': '2', 'date': '21 May 2016, 18:48'}, {'business_ref': 'businessref_46', 'rating': '5', 'date': '2016-08-15 21:16:00'}, {'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-07-18 21:37:00'}, {'business_ref': 'businessref_68', 'rating': '2', 'date': 'October 26, 2016 at 03:04 PM'}, {'business_ref': 'businessref_37', 'rating': '5', 'date': '24 Mar 2016, 21:40'}, {'business_ref': 'businessref_10', 'rating': '5', 'date': '17 Feb 2016, 22:34'}, {'business_ref': 'businessref_16', 'rating': '1', 'date': '2016-01-01 02:46:00'}, {'business_ref': 'businessref_23', 'rating': '5', 'date': '2016-06-28 02:18:33'}, {'business_ref': 'businessref_42', 'rating': '5', 'date': '29 Sep 2016, 02:01'}, {'business_ref': 'businessref_18', 'rating': '1', 'date': '13 Dec 2016, 03:48'}, {'business_ref': 'businessref_53', 'rating': '5', 'date': 'November 18, 2016 at 10:05 PM'}, {'business_ref': 'businessref_8', 'rating': '5', 'date': '2016-07-22 15:56:00'}, {'business_ref': 'businessref_37', 'rating': '1', 'date': '28 Sep 2016, 17:19'}, {'business_ref': 'businessref_51', 'rating': '1', 'date': '2016-12-13 17:57:00'}, {'business_ref': 'businessref_9', 'rating': '5', 'date': '14 Nov 2016, 15:01'}, {'business_ref': 'businessref_77', 'rating': '1', 'date': '14 Dec 2016, 01:39'}, {'business_ref': 'businessref_57', 'rating': '1', 'date': 'June 03, 2016 at 09:43 PM'}, {'business_ref': 'businessref_25', 'rating': '4', 'date': 'February 13, 2016 at 03:47 AM'}, {'business_ref': 'businessref_8', 'rating': '5', 'date': '2016-03-12 14:19:00'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)

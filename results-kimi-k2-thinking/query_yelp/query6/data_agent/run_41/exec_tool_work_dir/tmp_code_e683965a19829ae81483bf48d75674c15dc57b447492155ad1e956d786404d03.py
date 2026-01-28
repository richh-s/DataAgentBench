code = """import json
import re
from datetime import datetime

# Load the 2016 reviews from the stored result
result_file = locals()['var_functions.query_db:10']
with open(result_file, 'r') as f:
    reviews_2016 = json.load(f)

print(f'Total 2016 reviews loaded: {len(reviews_2016)}')

# Parse dates and filter for range Jan 1, 2016 to June 30, 2016
# Date formats vary: "August 01, 2016 at 03:44 AM", "21 May 2016, 18:48", "2016-08-15 21:16:00"
def parse_date(date_str):
    try:
        # Try format: "2016-08-15 21:16:00"
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except:
        try:
            # Try format: "21 May 2016, 18:48"
            return datetime.strptime(date_str, "%d %b %Y, %H:%M")
        except:
            try:
                # Try format: "24 Mar 2016, 21:40"
                return datetime.strptime(date_str, "%d %b %Y, %H:%M")
            except:
                try:
                    # Try format: "August 01, 2016 at 03:44 AM"
                    # Remove "at" and make it consistent
                    clean_str = date_str.replace(' at', '')
                    return datetime.strptime(clean_str, "%B %d, %Y %I:%M %p")
                except:
                    return None

# Filter reviews for date range
start_date = datetime(2016, 1, 1)
end_date = datetime(2016, 6, 30, 23, 59, 59)

filtered_reviews = []
for review in reviews_2016:
    date_obj = parse_date(review['date'])
    if date_obj and start_date <= date_obj <= end_date:
        filtered_reviews.append({
            'business_ref': review['business_ref'],
            'rating': int(review['rating']),
            'date': review['date']
        })

print(f'Reviews in date range (Jan-Jun 2016): {len(filtered_reviews)}')

# Group by business and calculate average rating
from collections import defaultdict

business_stats = defaultdict(lambda: {'total_rating': 0, 'count': 0})
for review in filtered_reviews:
    business_ref = review['business_ref']
    business_stats[business_ref]['total_rating'] += review['rating']
    business_stats[business_ref]['count'] += 1

# Filter businesses with at least 5 reviews and calculate average
business_averages = []
for business_ref, stats in business_stats.items():
    if stats['count'] >= 5:
        avg_rating = stats['total_rating'] / stats['count']
        business_averages.append({
            'business_ref': business_ref,
            'avg_rating': avg_rating,
            'review_count': stats['count']
        })

# Sort by average rating descending
business_averages_sorted = sorted(business_averages, key=lambda x: x['avg_rating'], reverse=True)

print(f'Businesses with >=5 reviews in period: {len(business_averages_sorted)}')
if business_averages_sorted:
    top_business = business_averages_sorted[0]
    print(f'Top business: {top_business}')
else:
    print('No businesses found with >=5 reviews in the period')

result = json.dumps({'top_business': top_business if business_averages_sorted else None, 'all_businesses': business_averages_sorted[:10]})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': [{'review_id': 'reviewid_135', 'user_id': 'userid_548', 'business_ref': 'businessref_34', 'rating': '2', 'useful': '0', 'funny': '0', 'cool': '0', 'text': "Sure, it's cheap, but there isn't much to see. I think you'd have to have a big interest in the topic to find it exciting, and kids would be bored. I think it only lasted maybe 10-15 minutes. Our tour person was somewhat knowledgeable and seemed into it, but he didn't give us much time to read the information on each level. I had to take photos of the plaques to read later, and half of them need replacing, as they are so sun-bleached they're virtually unreadable (tour guide said they're being replaced soon and that the other half were already replaced). I really thought it needed to be higher up to give a good view. The Lewis and Clark State Historic Site just down the road was more interesting and free. If you live around here like I do and have nothing better to do, you might want to give it a go if the topic interests you, but if you're a tourist, this is not something you should waste your time on.", 'date': 'August 01, 2016 at 03:44 AM'}, {'review_id': 'reviewid_1067', 'user_id': 'userid_213', 'business_ref': 'businessref_89', 'rating': '5', 'useful': '2', 'funny': '0', 'cool': '0', 'text': 'Very good service but a little pricey for the services your receive. Clean and sanitary too', 'date': 'June 14, 2021 at 11:39 AM'}, {'review_id': 'reviewid_871', 'user_id': 'userid_616', 'business_ref': 'businessref_82', 'rating': '4', 'useful': '0', 'funny': '0', 'cool': '0', 'text': 'My friend and I enjoyed a fantastic meal at Miles Table and I can\'t wait to return! Given that it was half-price-burger-day, I felt the need to give the falafel burger a shot. It was delicious! I\'m not always a falafel fan, but this "burger" was awesome. The brioche bun was the perfect consistency and the portion of fries was plentiful. My friend enjoyed the cobb salad (though she requested balsamic dressing instead of buttermilk and she received buttermilk). The restaurant is quaint and has ample seating. While you order at the counter, our "server" (I believe her name was Sarah) was fantastic and made sure we had everything we needed. Overall, this is a great spot and I will be back soon...I may have to make it a weekly lunch staple!', 'date': '29 May 2013, 23:01'}, {'review_id': 'reviewid_314', 'user_id': 'userid_1903', 'business_ref': 'businessref_66', 'rating': '2', 'useful': '1', 'funny': '2', 'cool': '1', 'text': "This location is not one of my favorites people here get pretty rude sometimes no one looks happy it's hit or miss with the food sometimes it's awesome other times terrible I always get honey walnut shrimp for an extra 1.25 which is retarded and Beijing beef I enjoy the rice n the noodles but idk do if u dare", 'date': '21 May 2016, 18:48'}, {'review_id': 'reviewid_487', 'user_id': 'None', 'business_ref': 'businessref_95', 'rating': '1', 'useful': '0', 'funny': '0', 'cool': '0', 'text': 'Terrible service. I was charged twice for online order and they refused to refund me. Numerous times this has happened', 'date': 'November 01, 2021 at 05:11 PM'}], 'var_functions.list_db:4': ['review', 'tip', 'user'], 'var_functions.query_db:6': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}], 'var_functions.query_db:8': [{'business_ref': 'businessref_34', 'rating': '2', 'date': 'August 01, 2016 at 03:44 AM'}, {'business_ref': 'businessref_66', 'rating': '2', 'date': '21 May 2016, 18:48'}, {'business_ref': 'businessref_46', 'rating': '5', 'date': '2016-08-15 21:16:00'}, {'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-07-18 21:37:00'}, {'business_ref': 'businessref_68', 'rating': '2', 'date': 'October 26, 2016 at 03:04 PM'}, {'business_ref': 'businessref_37', 'rating': '5', 'date': '24 Mar 2016, 21:40'}, {'business_ref': 'businessref_10', 'rating': '5', 'date': '17 Feb 2016, 22:34'}, {'business_ref': 'businessref_16', 'rating': '1', 'date': '2016-01-01 02:46:00'}, {'business_ref': 'businessref_23', 'rating': '5', 'date': '2016-06-28 02:18:33'}, {'business_ref': 'businessref_42', 'rating': '5', 'date': '29 Sep 2016, 02:01'}, {'business_ref': 'businessref_18', 'rating': '1', 'date': '13 Dec 2016, 03:48'}, {'business_ref': 'businessref_53', 'rating': '5', 'date': 'November 18, 2016 at 10:05 PM'}, {'business_ref': 'businessref_8', 'rating': '5', 'date': '2016-07-22 15:56:00'}, {'business_ref': 'businessref_37', 'rating': '1', 'date': '28 Sep 2016, 17:19'}, {'business_ref': 'businessref_51', 'rating': '1', 'date': '2016-12-13 17:57:00'}, {'business_ref': 'businessref_9', 'rating': '5', 'date': '14 Nov 2016, 15:01'}, {'business_ref': 'businessref_77', 'rating': '1', 'date': '14 Dec 2016, 01:39'}, {'business_ref': 'businessref_57', 'rating': '1', 'date': 'June 03, 2016 at 09:43 PM'}, {'business_ref': 'businessref_25', 'rating': '4', 'date': 'February 13, 2016 at 03:47 AM'}, {'business_ref': 'businessref_8', 'rating': '5', 'date': '2016-03-12 14:19:00'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)

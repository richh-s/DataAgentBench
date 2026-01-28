code = """# Load the results from storage
import json

# Get the top businesses by high-rating review count
top_businesses = [
    {"gmap_id": "gmap_35", "high_rating_count": 19},
    {"gmap_id": "gmap_53", "high_rating_count": 17},
    {"gmap_id": "gmap_20", "high_rating_count": 14}
]

# Business names from the query
business_names = {
    "gmap_35": "Encino Dermatology & Laser: Alex Khadavi MD",
    "gmap_53": "The Boochyard @ Local Roots",
    "gmap_20": "Aurora Massage"
}

# Combine results
result = []
for business in top_businesses:
    result.append({
        "business_name": business_names[business["gmap_id"]],
        "high_rating_reviews_count": business["high_rating_count"]
    })

# Print in the required format
print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_functions.list_db:2': ['business_description'], 'var_functions.list_db:3': ['review'], 'var_functions.query_db:7': [{'gmap_id': 'gmap_0', 'rating': '5', 'time': '01 Mar 2019, 00:34'}, {'gmap_id': 'gmap_0', 'rating': '5', 'time': 'April 17, 2019 at 04:33 PM'}, {'gmap_id': 'gmap_1', 'rating': '5', 'time': 'May 02, 2019 at 07:06 PM'}, {'gmap_id': 'gmap_11', 'rating': '5', 'time': '2019-09-28 13:57:41'}, {'gmap_id': 'gmap_11', 'rating': '5', 'time': '2019-08-24 16:48:04'}, {'gmap_id': 'gmap_11', 'rating': '5', 'time': '21 Aug 2019, 10:05'}, {'gmap_id': 'gmap_11', 'rating': '5', 'time': '21 Jun 2019, 00:19'}, {'gmap_id': 'gmap_11', 'rating': '5', 'time': 'October 28, 2019 at 07:11 AM'}, {'gmap_id': 'gmap_11', 'rating': '5', 'time': '2019-11-13 12:02:42'}, {'gmap_id': 'gmap_11', 'rating': '5', 'time': '27 Jun 2019, 18:00'}, {'gmap_id': 'gmap_12', 'rating': '5', 'time': 'March 13, 2019 at 05:47 PM'}, {'gmap_id': 'gmap_13', 'rating': '5', 'time': 'January 02, 2019 at 03:42 PM'}, {'gmap_id': 'gmap_13', 'rating': '5', 'time': '2019-06-23 10:28:00'}, {'gmap_id': 'gmap_13', 'rating': '5', 'time': 'January 23, 2019 at 11:51 AM'}, {'gmap_id': 'gmap_14', 'rating': '5', 'time': '2019-06-20 15:59:41'}, {'gmap_id': 'gmap_14', 'rating': '5', 'time': '11 Nov 2019, 16:13'}, {'gmap_id': 'gmap_14', 'rating': '5', 'time': '30 Mar 2019, 14:52'}, {'gmap_id': 'gmap_15', 'rating': '5', 'time': 'November 01, 2019 at 02:36 PM'}, {'gmap_id': 'gmap_15', 'rating': '5', 'time': 'August 06, 2019 at 11:47 AM'}, {'gmap_id': 'gmap_15', 'rating': '5', 'time': '02 Feb 2019, 15:31'}], 'var_functions.query_db:8': [{'gmap_id': 'gmap_35', 'high_rating_count': '19'}, {'gmap_id': 'gmap_53', 'high_rating_count': '17'}, {'gmap_id': 'gmap_20', 'high_rating_count': '14'}, {'gmap_id': 'gmap_40', 'high_rating_count': '13'}, {'gmap_id': 'gmap_72', 'high_rating_count': '12'}, {'gmap_id': 'gmap_62', 'high_rating_count': '12'}, {'gmap_id': 'gmap_46', 'high_rating_count': '12'}, {'gmap_id': 'gmap_47', 'high_rating_count': '11'}, {'gmap_id': 'gmap_17', 'high_rating_count': '8'}, {'gmap_id': 'gmap_7', 'high_rating_count': '7'}], 'var_functions.query_db:10': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_35', 'name': 'Encino Dermatology & Laser: Alex Khadavi MD'}]}

exec(code, env_args)

code = """import json

reviews_data = [{"gmap_id": "gmap_35", "review_count": 19}, {"gmap_id": "gmap_53", "review_count": 17}, {"gmap_id": "gmap_20", "review_count": 14}]
business_data = [{"name": "Aurora Massage", "gmap_id": "gmap_20"}, {"name": "The Boochyard @ Local Roots", "gmap_id": "gmap_53"}, {"name": "Encino Dermatology & Laser: Alex Khadavi MD", "gmap_id": "gmap_35"}]

# Create a dictionary for business names
id_to_name = {b['gmap_id']: b['name'] for b in business_data}

results = []
for r in reviews_data:
    results.append({
        "name": id_to_name.get(r['gmap_id'], "Unknown"),
        "count": r['review_count']
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-11824539079501379141': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_function-call-9654438622628664072': [{'gmap_id': 'gmap_72', 'review_count': '12'}, {'gmap_id': 'gmap_35', 'review_count': '12'}, {'gmap_id': 'gmap_20', 'review_count': '11'}], 'var_function-call-6200737733866493101': [{'time': 'September 03, 2020 at 04:15 PM'}, {'time': '2021-04-12 17:07:52'}, {'time': '2018-04-23 16:24:26'}, {'time': '2017-07-10 22:12:19'}, {'time': 'May 19, 2021 at 03:55 AM'}, {'time': 'November 14, 2020 at 09:52 AM'}, {'time': 'June 12, 2021 at 06:15 PM'}, {'time': 'January 06, 2021 at 12:12 AM'}, {'time': 'February 09, 2021 at 12:47 AM'}, {'time': '08 Mar 2020, 00:04'}, {'time': 'March 07, 2019 at 12:56 AM'}, {'time': '2017-05-16 01:01:41'}, {'time': '18 Jan 2019, 03:19'}, {'time': '2021-08-03 19:36:39'}, {'time': '2021-03-28 23:53:53'}, {'time': '2021-06-20 11:19:30'}, {'time': '2017-11-25 13:19:44'}, {'time': '29 Sep 2020, 17:28'}, {'time': 'June 10, 2018 at 02:23 AM'}, {'time': '2017-04-23 13:17:21'}], 'var_function-call-5472830633498890926': [{'gmap_id': 'gmap_35', 'review_count': '19'}, {'gmap_id': 'gmap_53', 'review_count': '17'}, {'gmap_id': 'gmap_20', 'review_count': '14'}], 'var_function-call-12082169295497813404': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Encino Dermatology & Laser: Alex Khadavi MD', 'gmap_id': 'gmap_35'}]}

exec(code, env_args)

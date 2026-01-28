code = """import json

# Results from previous queries
high_rating_results = [
    {"gmap_id": "gmap_72", "high_rating_count": "12"},
    {"gmap_id": "gmap_35", "high_rating_count": "12"},
    {"gmap_id": "gmap_20", "high_rating_count": "11"},
    {"gmap_id": "gmap_62", "high_rating_count": "10"},
    {"gmap_id": "gmap_53", "high_rating_count": "10"}
]

business_results = [
    {"gmap_id": "gmap_20", "name": "Aurora Massage", "description": " Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body."},
    {"gmap_id": "gmap_35", "name": "Encino Dermatology & Laser: Alex Khadavi MD", "description": " Offering comprehensive medical care and personalized health solutions in Encino, CA 91436, this clinic specializes in diagnosing and treating a wide range of health conditions."},
    {"gmap_id": "gmap_53", "name": "The Boochyard @ Local Roots", "description": " This vibrant establishment in Vista, CA 92081 specializes in crafting a diverse selection of artisanal beers, offering a cozy atmosphere for tasting and enjoying unique local brews."},
    {"gmap_id": "gmap_62", "name": "Acuity Eye Group, Retina Institute & Acuity 360 Advanced Vision Center - Tustin", "description": " Located in Tustin, CA 92780, this eye care clinic offers expert vision assessments and advanced treatments for a wide range of eye conditions."},
    {"gmap_id": "gmap_72", "name": "Zuby's Brake Tires & Wheels", "description": " This auto service center in Garden Grove, CA 92843 specializes in providing high-quality wheels and tire-related services to ensure your vehicle runs smoothly and safely."}
]

# Create a mapping of gmap_id to business name
business_map = {biz['gmap_id']: biz['name'] for biz in business_results}

# Get top 3 businesses
top_3 = high_rating_results[:3]

# Build final result
result = []
for item in top_3:
    business_name = business_map.get(item['gmap_id'], 'Unknown Business')
    result.append({
        'business_name': business_name,
        'high_rating_reviews_count': int(item['high_rating_count'])
    })

final_json = json.dumps(result, indent=2)
print('__RESULT__:')
print(final_json)"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_functions.query_db:6': [{'total_reviews': '212', 'high_rating_reviews': '166', 'unique_businesses': '51'}], 'var_functions.query_db:8': [{'gmap_id': 'gmap_72', 'high_rating_count': '12'}, {'gmap_id': 'gmap_35', 'high_rating_count': '12'}, {'gmap_id': 'gmap_20', 'high_rating_count': '11'}, {'gmap_id': 'gmap_62', 'high_rating_count': '10'}, {'gmap_id': 'gmap_53', 'high_rating_count': '10'}, {'gmap_id': 'gmap_47', 'high_rating_count': '7'}, {'gmap_id': 'gmap_46', 'high_rating_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_count': '7'}, {'gmap_id': 'gmap_17', 'high_rating_count': '6'}, {'gmap_id': 'gmap_7', 'high_rating_count': '5'}], 'var_functions.query_db:10': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_35', 'name': 'Encino Dermatology & Laser: Alex Khadavi MD', 'description': ' Offering comprehensive medical care and personalized health solutions in Encino, CA 91436, this clinic specializes in diagnosing and treating a wide range of health conditions.'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots', 'description': ' This vibrant establishment in Vista, CA 92081 specializes in crafting a diverse selection of artisanal beers, offering a cozy atmosphere for tasting and enjoying unique local brews.'}, {'gmap_id': 'gmap_62', 'name': 'Acuity Eye Group, Retina Institute & Acuity 360 Advanced Vision Center - Tustin', 'description': ' Located in Tustin, CA 92780, this eye care clinic offers expert vision assessments and advanced treatments for a wide range of eye conditions.'}, {'gmap_id': 'gmap_72', 'name': "Zuby's Brake Tires & Wheels", 'description': ' This auto service center in Garden Grove, CA 92843 specializes in providing high-quality wheels and tire-related services to ensure your vehicle runs smoothly and safely.'}]}

exec(code, env_args)

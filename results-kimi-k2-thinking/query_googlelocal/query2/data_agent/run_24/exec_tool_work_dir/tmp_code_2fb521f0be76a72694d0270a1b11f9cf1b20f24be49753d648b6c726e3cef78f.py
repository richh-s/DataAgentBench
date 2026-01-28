code = """import json

# Massage businesses data
businesses = {
    "gmap_22": "Angel-A Massage",
    "gmap_25": "Elite Massage", 
    "gmap_33": "Happy Spa & Massage (Formerly Hawaii Massage & Spa)",
    "gmap_24": "SUSY massage",
    "gmap_20": "Aurora Massage",
    "gmap_21": "Orient Massage",
    "gmap_28": "Good Massage"
}

# Ratings data
ratings_data = [
    {"gmap_id": "gmap_20", "avg_rating": "4.178571428571429", "review_count": "56"},
    {"gmap_id": "gmap_21", "avg_rating": "3.933333333333333", "review_count": "15"},
    {"gmap_id": "gmap_22", "avg_rating": "4.333333333333333", "review_count": "6"},
    {"gmap_id": "gmap_24", "avg_rating": "3.875", "review_count": "8"},
    {"gmap_id": "gmap_25", "avg_rating": "5.0", "review_count": "1"},
    {"gmap_id": "gmap_28", "avg_rating": "3.875", "review_count": "8"},
    {"gmap_id": "gmap_33", "avg_rating": "2.125", "review_count": "8"}
]

# Filter businesses with avg_rating >= 4.0
high_rated_businesses = []
for rating in ratings_data:
    avg_rating = float(rating["avg_rating"])
    if avg_rating >= 4.0:
        gmap_id = rating["gmap_id"]
        business_name = businesses[gmap_id]
        high_rated_businesses.append({
            "business_name": business_name,
            "average_rating": round(avg_rating, 2),
            "review_count": int(rating["review_count"])
        })

# Sort by rating descending
high_rated_businesses.sort(key=lambda x: x["average_rating"], reverse=True)

result = json.dumps(high_rated_businesses, indent=2)
print("__RESULT__:")
print(result)"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_functions.execute_python:4': "'gmap_22', 'gmap_25', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_21', 'gmap_28'", 'var_functions.query_db:6': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'review_count': '8'}]}

exec(code, env_args)

code = """import json

def compute_average_ratings():
    # Get the file path from correct key
    review_file = locals()['var_functions.query_db:24']
    
    with open(review_file, 'r') as f:
        reviews = json.load(f)
    
    # Extract ratings and compute average
    ratings = []
    for review in reviews:
        rating = review.get('rating')
        if rating is not None:
            try:
                rating_int = int(rating)
                ratings.append(rating_int)
            except (ValueError, TypeError):
                continue
    
    if not ratings:
        return {"average_rating": None, "total_reviews": 0, "state": "MO"}
    
    average_rating = sum(ratings) / len(ratings)
    
    return {
        "state": "MO",
        "average_rating": round(average_rating, 2),
        "total_reviews": len(ratings),
        "ratings_distribution": {
            "1_star": ratings.count(1),
            "2_star": ratings.count(2),
            "3_star": ratings.count(3),
            "4_star": ratings.count(4),
            "5_star": ratings.count(5)
        }
    }

result = compute_average_ratings()
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.list_db:2': ['review', 'tip', 'user'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'record_count': 100}, 'var_functions.execute_python:14': {'top_state': None, 'total_reviews_top_state': 0, 'businesses_in_top_state': 0, 'state_review_sums': {}}, 'var_functions.execute_python:16': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young lear...', 'found_state': 'CA'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, inc...', 'found_state': 'MO'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination...', 'found_state': 'ID'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of ser...', 'found_state': 'FL'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services inclu...', 'found_state': 'IN'}, {'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightfu...', 'found_state': 'FL'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of service...', 'found_state': 'PA'}, {'business_id': 'businessid_64', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nai...', 'found_state': 'MO'}, {'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Anti...', 'found_state': 'IN'}, {'business_id': 'businessid_29', 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of service...', 'found_state': 'NJ'}], 'var_functions.execute_python:18': {'top_state': 'MO', 'top_state_total_reviews': 2243, 'total_businesses_in_top_state': 9, 'all_states_count': 13, 'top_10_states': {'MO': 2243, 'PA': 1804, 'FL': 565, 'NV': 304, 'LA': 255, 'IN': 226, 'ID': 209, 'CA': 92, 'AB': 45, 'TN': 39}}, 'var_functions.execute_python:20': {'missouri_business_count': 9, 'first_10_businesses': ['47', '64', '10', '24', '30', '96', '11', '4', '46']}, 'var_functions.execute_python:22': {'missouri_business_count': 9, 'business_refs': "'businessref_47', 'businessref_64', 'businessref_10', 'businessref_24', 'businessref_30', 'businessref_96', 'businessref_11', 'businessref_4', 'businessref_46'", 'business_refs_list': ['businessref_47', 'businessref_64', 'businessref_10', 'businessref_24', 'businessref_30', 'businessref_96', 'businessref_11', 'businessref_4', 'businessref_46']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)

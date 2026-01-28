code = """import json

# Get data
businesses = locals().get('var_functions.query_db:5', [])
reviews = locals().get('var_functions.query_db:14', [])

if not businesses or not reviews:
    print('__RESULT__:')
    print(json.dumps({'error': 'Missing data'}))
else:
    # Extract state from business descriptions
    def extract_state(description):
        if not description:
            return None
        import re
        patterns = [
            r'in [^,]+,\s*([A-Z]{2})[\.,\s]',
            r'at [^,]+ in [^,]+,\s*([A-Z]{2})[\.,\s]',
            r',\s*([A-Z]{2})\b',
        ]
        for pattern in patterns:
            match = re.search(pattern, description)
            if match:
                return match.group(1)
        return None
    
    # Map business_id (businessid_X) to state
    business_to_state = {}
    for business in businesses:
        business_id = business.get('business_id', '')
        description = business.get('description', '')
        state = extract_state(description)
        if business_id and state:
            business_to_state[business_id] = state
    
    # Map business_ref (businessref_X) to state
    # business_id_47 corresponds to business_ref_47
    business_ref_to_state = {}
    for business_ref_id, state in business_to_state.items():
        # Convert businessid_X to businessref_X
        if business_ref_id.startswith('businessid_'):
            ref_id = business_ref_id.replace('businessid_', 'businessref_')
            business_ref_to_state[ref_id] = state
    
    # Group reviews by state
    state_reviews = {}
    for review in reviews:
        business_ref = review.get('business_ref', '')
        rating = review.get('rating')
        
        # Get state for this business
        state = business_ref_to_state.get(business_ref)
        
        if state and rating is not None:
            try:
                rating = int(rating)
                if state not in state_reviews:
                    state_reviews[state] = []
                state_reviews[state].append(rating)
            except (ValueError, TypeError):
                continue
    
    # Find state with most reviews (from business collection)
    state_review_counts = {}
    for business in businesses:
        business_id = business.get('business_id', '')
        review_count = business.get('review_count', 0)
        
        try:
            review_count = int(review_count)
        except (ValueError, TypeError):
            review_count = 0
        
        state = business_to_state.get(business_id)
        if state:
            state_review_counts[state] = state_review_counts.get(state, 0) + review_count
    
    # Get top state
    if state_review_counts:
        top_state = max(state_review_counts, key=state_review_counts.get)
        top_state_review_count = state_review_counts[top_state]
        
        # Calculate average rating for top state
        top_state_ratings = state_reviews.get(top_state, [])
        avg_rating = None
        if top_state_ratings:
            avg_rating = sum(top_state_ratings) / len(top_state_ratings)
        
        result = {
            'top_state': top_state,
            'total_review_count_from_businesses': top_state_review_count,
            'average_rating': avg_rating,
            'rating_count': len(top_state_ratings),
            'state_review_counts': state_review_counts,
            'available_state_ratings': {state: len(ratings) for state, ratings in state_reviews.items()}
        }
    else:
        result = {'error': 'No state review counts found'}
    
    print('__RESULT__:')
    print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.execute_python:8': {'top_state': 'MO', 'total_reviews_in_state': 81, 'business_count_in_state': 1, 'top_state_business_ids': ['businessid_47']}, 'var_functions.list_db:10': ['review', 'tip', 'user'], 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_businesses_with_state': 5, 'states_found': 5, 'businesses_per_state': {'CA': 1, 'MO': 1, 'ID': 1, 'FL': 1, 'IN': 1}, 'business_to_state_mapping': {'businessid_49': 'CA', 'businessid_47': 'MO', 'businessid_88': 'ID', 'businessid_41': 'FL', 'businessid_33': 'IN'}}}

exec(code, env_args)

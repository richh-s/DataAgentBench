code = """import json

# Load data
file_path = locals()['var_function-call-3749794167030689373']
with open(file_path, 'r') as f:
    data = json.load(f)

# US States set
us_states = set([
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "DC"
])

def has_wifi(attr):
    if not attr:
        return False
    wifi = attr.get('WiFi')
    if not wifi:
        return False
    w = str(wifi).lower()
    return 'free' in w or 'paid' in w

def extract_state(desc):
    if not desc:
        return None
    # Strategy: split by comma, check tokens from end
    # "Located at ... in City, State, this ..."
    # "Located at ... in City, State ...."
    # Usually the state is the uppercase 2-letter token before "this" or at the end of location part.
    
    # Simple heuristic: Look for " XX, " or " XX " where XX is a state code.
    # Better: Split by "in " and take the last part? No, multiple "in".
    # Rely on the ", State," pattern.
    
    # Let's try to parse the string before "this"
    parts = desc.split("this")
    if len(parts) > 1:
        loc = parts[0] # "Located at ... in City, State, "
        # Remove trailing comma/space
        loc = loc.strip().rstrip(',')
        # Split by comma
        segments = loc.split(',')
        if segments:
            last = segments[-1].strip()
            # If last is a state code
            if last in us_states:
                return last
            # Sometimes it might be "City, State Zip"
            # Or "City, State"
            
            # Check for zip code at the end? "City, State 12345"
            # Split by space
            sub_segments = last.split()
            for token in sub_segments:
                token_clean = token.strip(',.')
                if token_clean in us_states:
                    return token_clean
            
            # If not in the last segment, check the second to last segment
            if len(segments) > 1:
                second_last = segments[-2].strip()
                if second_last in us_states:
                    return second_last
                
                # Check tokens in second last
                sub_segments_2 = second_last.split()
                for token in sub_segments_2:
                    token_clean = token.strip(',.')
                    if token_clean in us_states:
                        return token_clean
                        
    return None

wifi_businesses = []
state_counts = {}

for entry in data:
    if has_wifi(entry.get('attributes')):
        state = extract_state(entry.get('description'))
        if state:
            state_counts[state] = state_counts.get(state, 0) + 1
            wifi_businesses.append({'id': entry['business_id'], 'state': state})

if state_counts:
    top_state = max(state_counts, key=state_counts.get)
    count = state_counts[top_state]
    
    ids = [b['id'] for b in wifi_businesses if b['state'] == top_state]
    
    # Prepare IDs for SQL IN clause (quoted strings)
    # Convert 'businessid_X' to 'businessref_X'
    ref_ids = [id_str.replace('businessid_', 'businessref_') for id_str in ids]
    
    result = {
        "top_state": top_state,
        "count": count,
        "ref_ids": ref_ids
    }
else:
    result = {"error": "No states found"}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-10457212279556369061': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-15129643603376292417': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}], 'var_function-call-7706927622901924236': {'top_state': 'MO', 'count': 1, 'sample_ids': ['businessid_64'], 'total_ids': 1, 'all_ids': ['businessid_64']}, 'var_function-call-3749794167030689373': 'file_storage/function-call-3749794167030689373.json'}

exec(code, env_args)

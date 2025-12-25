code = """import pandas as pd
import json

# Load data
business_data = locals()['var_function-call-1177203977734142744']
rating_data = locals()['var_function-call-6301248741602847105']

df_business = pd.DataFrame(business_data)
df_ratings = pd.DataFrame(rating_data)

# Helper to check credit card acceptance
def accepts_credit_cards(attr):
    if attr is None or attr == "None":
        return False
    # If attr is a string representation of a dict
    if isinstance(attr, str):
        # The provided output showed attr as a dictionary in JSON, but sometimes it might be stringified?
        # In the query_db result for MongoDB, it appeared as actual dict objects in the list provided by the tool, 
        # except for "None" which was a string.
        # However, let's be safe.
        return False 
    if isinstance(attr, dict):
        # The key is "BusinessAcceptsCreditCards"
        val = attr.get("BusinessAcceptsCreditCards")
        if val == "True":
            return True
    return False

# Filter businesses
df_business['accepts_cc'] = df_business['attributes'].apply(accepts_credit_cards)
df_cc_business = df_business[df_business['accepts_cc']].copy()

# Extract categories
def extract_categories(desc):
    if not desc:
        return []
    # Keywords to look for
    keywords = ["services in ", "including "]
    categories_str = ""
    for kw in keywords:
        if kw in desc:
            # Split and take the part after the keyword
            parts = desc.split(kw)
            if len(parts) > 1:
                # Take the last part
                categories_str = parts[-1]
                break
    
    if not categories_str:
        return []
        
    # Remove trailing period
    categories_str = categories_str.strip().rstrip('.')
    
    # Split by comma and "and"
    # Example: "A, B, and C" -> ["A", "B", " and C"] -> clean up
    # A simple split by ',' might leave "and" in the last item.
    
    raw_cats = [c.strip() for c in categories_str.split(',')]
    final_cats = []
    for c in raw_cats:
        if c.lower().startswith("and "):
            c = c[4:]
        final_cats.append(c)
    return final_cats

df_cc_business['categories'] = df_cc_business['description'].apply(extract_categories)

# Prepare ratings
df_ratings['business_id'] = df_ratings['business_ref'].str.replace('businessref_', 'businessid_')
df_ratings['avg_rating'] = pd.to_numeric(df_ratings['avg_rating'])

# Merge
merged = pd.merge(df_cc_business, df_ratings, on='business_id', how='inner')

# Explode categories
exploded = merged.explode('categories')

# Group by category
# We want: largest number of businesses
# And average rating (average of business average ratings)
category_stats = exploded.groupby('categories').agg(
    business_count=('business_id', 'nunique'),
    category_avg_rating=('avg_rating', 'mean')
).reset_index()

# Find the category with the largest number of businesses
# If tie, picking one.
top_category = category_stats.sort_values(by=['business_count', 'category_avg_rating'], ascending=[False, False]).iloc[0]

result = {
    "category": top_category['categories'],
    "business_count": int(top_category['business_count']),
    "average_rating": top_category['category_avg_rating']
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8705707280335889974': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-1177203977734142744': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-6301248741602847105': [{'business_ref': 'businessref_47', 'avg_rating': '3.9047619047619047'}, {'business_ref': 'businessref_16', 'avg_rating': '3.024390243902439'}, {'business_ref': 'businessref_46', 'avg_rating': '4.181818181818182'}, {'business_ref': 'businessref_91', 'avg_rating': '4.911111111111111'}, {'business_ref': 'businessref_1', 'avg_rating': '4.333333333333333'}, {'business_ref': 'businessref_55', 'avg_rating': '4.918918918918919'}, {'business_ref': 'businessref_73', 'avg_rating': '5.0'}, {'business_ref': 'businessref_6', 'avg_rating': '4.0'}, {'business_ref': 'businessref_71', 'avg_rating': '3.268292682926829'}, {'business_ref': 'businessref_38', 'avg_rating': '3.1176470588235294'}, {'business_ref': 'businessref_32', 'avg_rating': '3.4285714285714284'}, {'business_ref': 'businessref_30', 'avg_rating': '3.6'}, {'business_ref': 'businessref_79', 'avg_rating': '4.627906976744186'}, {'business_ref': 'businessref_44', 'avg_rating': '2.9285714285714284'}, {'business_ref': 'businessref_13', 'avg_rating': '3.9166666666666665'}, {'business_ref': 'businessref_87', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_57', 'avg_rating': '1.9047619047619047'}, {'business_ref': 'businessref_85', 'avg_rating': '3.3863636363636362'}, {'business_ref': 'businessref_86', 'avg_rating': '3.739130434782609'}, {'business_ref': 'businessref_37', 'avg_rating': '3.2083333333333335'}, {'business_ref': 'businessref_42', 'avg_rating': '4.083333333333333'}, {'business_ref': 'businessref_97', 'avg_rating': '4.294117647058823'}, {'business_ref': 'businessref_8', 'avg_rating': '2.8222222222222224'}, {'business_ref': 'businessref_90', 'avg_rating': '1.0'}, {'business_ref': 'businessref_72', 'avg_rating': '4.6'}, {'business_ref': 'businessref_56', 'avg_rating': '2.3333333333333335'}, {'business_ref': 'businessref_62', 'avg_rating': '3.0'}, {'business_ref': 'businessref_34', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_21', 'avg_rating': '2.0285714285714285'}, {'business_ref': 'businessref_26', 'avg_rating': '1.7083333333333333'}, {'business_ref': 'businessref_68', 'avg_rating': '1.7619047619047619'}, {'business_ref': 'businessref_88', 'avg_rating': '3.212121212121212'}, {'business_ref': 'businessref_65', 'avg_rating': '3.8333333333333335'}, {'business_ref': 'businessref_4', 'avg_rating': '5.0'}, {'business_ref': 'businessref_95', 'avg_rating': '2.1666666666666665'}, {'business_ref': 'businessref_40', 'avg_rating': '4.476190476190476'}, {'business_ref': 'businessref_61', 'avg_rating': '2.4705882352941178'}, {'business_ref': 'businessref_92', 'avg_rating': '4.575757575757576'}, {'business_ref': 'businessref_94', 'avg_rating': '4.066666666666666'}, {'business_ref': 'businessref_7', 'avg_rating': '3.75'}, {'business_ref': 'businessref_63', 'avg_rating': '2.8333333333333335'}, {'business_ref': 'businessref_83', 'avg_rating': '4.833333333333333'}, {'business_ref': 'businessref_64', 'avg_rating': '3.7142857142857144'}, {'business_ref': 'businessref_10', 'avg_rating': '4.1875'}, {'business_ref': 'businessref_23', 'avg_rating': '3.4444444444444446'}, {'business_ref': 'businessref_49', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_84', 'avg_rating': '5.0'}, {'business_ref': 'businessref_11', 'avg_rating': '4.2'}, {'business_ref': 'businessref_41', 'avg_rating': '4.0'}, {'business_ref': 'businessref_82', 'avg_rating': '4.309523809523809'}, {'business_ref': 'businessref_35', 'avg_rating': '4.125'}, {'business_ref': 'businessref_45', 'avg_rating': '3.3863636363636362'}, {'business_ref': 'businessref_77', 'avg_rating': '2.5476190476190474'}, {'business_ref': 'businessref_27', 'avg_rating': '3.3214285714285716'}, {'business_ref': 'businessref_50', 'avg_rating': '2.4285714285714284'}, {'business_ref': 'businessref_76', 'avg_rating': '3.5555555555555554'}, {'business_ref': 'businessref_75', 'avg_rating': '4.0'}, {'business_ref': 'businessref_66', 'avg_rating': '2.1818181818181817'}, {'business_ref': 'businessref_9', 'avg_rating': '4.435897435897436'}, {'business_ref': 'businessref_25', 'avg_rating': '4.444444444444445'}, {'business_ref': 'businessref_2', 'avg_rating': '4.769230769230769'}, {'business_ref': 'businessref_74', 'avg_rating': '2.8333333333333335'}, {'business_ref': 'businessref_59', 'avg_rating': '4.6'}, {'business_ref': 'businessref_5', 'avg_rating': '1.6'}, {'business_ref': 'businessref_29', 'avg_rating': '3.9047619047619047'}, {'business_ref': 'businessref_58', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_39', 'avg_rating': '4.125'}, {'business_ref': 'businessref_100', 'avg_rating': '4.0'}, {'business_ref': 'businessref_96', 'avg_rating': '3.8863636363636362'}, {'business_ref': 'businessref_22', 'avg_rating': '2.8181818181818183'}, {'business_ref': 'businessref_20', 'avg_rating': '3.2142857142857144'}, {'business_ref': 'businessref_18', 'avg_rating': '1.8181818181818181'}, {'business_ref': 'businessref_14', 'avg_rating': '3.4'}, {'business_ref': 'businessref_3', 'avg_rating': '2.0'}, {'business_ref': 'businessref_69', 'avg_rating': '4.222222222222222'}, {'business_ref': 'businessref_98', 'avg_rating': '1.2'}, {'business_ref': 'businessref_28', 'avg_rating': '4.055555555555555'}, {'business_ref': 'businessref_70', 'avg_rating': '4.777777777777778'}, {'business_ref': 'businessref_31', 'avg_rating': '1.5'}, {'business_ref': 'businessref_78', 'avg_rating': '5.0'}, {'business_ref': 'businessref_99', 'avg_rating': '3.2'}, {'business_ref': 'businessref_51', 'avg_rating': '3.9714285714285715'}, {'business_ref': 'businessref_53', 'avg_rating': '3.7142857142857144'}, {'business_ref': 'businessref_80', 'avg_rating': '1.8888888888888888'}, {'business_ref': 'businessref_19', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_43', 'avg_rating': '3.0476190476190474'}, {'business_ref': 'businessref_48', 'avg_rating': '3.3846153846153846'}, {'business_ref': 'businessref_17', 'avg_rating': '3.9'}, {'business_ref': 'businessref_81', 'avg_rating': '3.6666666666666665'}, {'business_ref': 'businessref_93', 'avg_rating': '2.857142857142857'}, {'business_ref': 'businessref_67', 'avg_rating': '3.3260869565217392'}, {'business_ref': 'businessref_15', 'avg_rating': '3.5294117647058822'}, {'business_ref': 'businessref_54', 'avg_rating': '3.5'}, {'business_ref': 'businessref_33', 'avg_rating': '3.5217391304347827'}, {'business_ref': 'businessref_89', 'avg_rating': '3.04'}, {'business_ref': 'businessref_24', 'avg_rating': '3.289473684210526'}, {'business_ref': 'businessref_36', 'avg_rating': '4.090909090909091'}, {'business_ref': 'businessref_12', 'avg_rating': '3.730769230769231'}, {'business_ref': 'businessref_60', 'avg_rating': '2.0'}, {'business_ref': 'businessref_52', 'avg_rating': '4.166666666666667'}]}

exec(code, env_args)

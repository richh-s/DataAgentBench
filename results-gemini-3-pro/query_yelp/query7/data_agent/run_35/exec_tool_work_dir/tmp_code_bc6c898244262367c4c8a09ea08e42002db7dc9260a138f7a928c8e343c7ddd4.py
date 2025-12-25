code = """import json
import re
import pandas as pd

reviews_data = locals()['var_function-call-15270022369569266984']
reviews_df = pd.DataFrame(reviews_data)
reviews_df['cnt'] = pd.to_numeric(reviews_df['cnt'])
reviews_df['business_id'] = reviews_df['business_ref'].str.replace('businessref_', 'businessid_')

business_file = locals()['var_function-call-11467388034751646705']
with open(business_file, 'r') as f:
    business_data = json.load(f)
business_df = pd.DataFrame(business_data)
merged_df = pd.merge(reviews_df, business_df, on='business_id', how='inner')

def extract_categories(desc):
    keywords = [
        "including ", "services in ", "categories of ", "category of ",
        "fields of ", "destination for ", "specializes in ", "featuring ",
        "mix of ", "seeking ", "enjoying ", "ranging from ", "selection of ",
        "products in ", "within the "
    ]
    start_idx = -1
    best_keyword = ""
    for kw in keywords:
        idx = desc.rfind(kw)
        if idx > start_idx:
            start_idx = idx
            best_keyword = kw
    if start_idx == -1: return []
    content = desc[start_idx + len(best_keyword):]
    
    stop_phrases = [
        " making it", " providing", " to meet", " perfect for", 
        " along with", " options", " enthusiasts", " for all", " ranging to",
        " ensuring", " catering"
    ]
    min_stop_idx = len(content)
    if "." in content: min_stop_idx = content.find(".")
    for phrase in stop_phrases:
        idx = content.find(phrase)
        if idx != -1 and idx < min_stop_idx: min_stop_idx = idx
    content = content[:min_stop_idx]
    content = content.replace("'", "")
    
    # Split
    parts = re.split(r', | and | & ', content)
    # Re-merge "Beauty" and "Spas" if extracted as such?
    # Wait, Yelp category is "Beauty & Spas".
    # My regex `r', | and | & '` splits "Beauty & Spas" into "Beauty" and "Spas".
    # This is bad. I shouldn't split by ` & `.
    # The standard separator is `, ` or `, and ` or ` and `.
    
    parts = re.split(r', (?:and )?| and ', content)
    
    final_cats = []
    for p in parts:
        p = p.strip()
        # Clean leading "and " if it wasn't caught by regex
        if p.lower().startswith("and "):
            p = p[4:].strip()
        # Clean trailing comma
        p = p.strip(".,")
        
        if p and len(p) > 2:
            final_cats.append(p)
            
    return final_cats

category_counts = {}
for _, row in merged_df.iterrows():
    cnt = row['cnt']
    cats = extract_categories(row['description'])
    for c in cats:
        category_counts[c] = category_counts.get(c, 0) + cnt

sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)

print("__RESULT__:")
print(json.dumps(sorted_cats[:10]))"""

env_args = {'var_function-call-10810467887319225293': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-15270022369569266984': [{'business_ref': 'businessref_74', 'cnt': '2'}, {'business_ref': 'businessref_66', 'cnt': '2'}, {'business_ref': 'businessref_9', 'cnt': '1'}, {'business_ref': 'businessref_33', 'cnt': '3'}, {'business_ref': 'businessref_15', 'cnt': '1'}, {'business_ref': 'businessref_6', 'cnt': '2'}, {'business_ref': 'businessref_31', 'cnt': '1'}, {'business_ref': 'businessref_53', 'cnt': '1'}, {'business_ref': 'businessref_51', 'cnt': '2'}, {'business_ref': 'businessref_8', 'cnt': '1'}, {'business_ref': 'businessref_57', 'cnt': '2'}, {'business_ref': 'businessref_86', 'cnt': '1'}, {'business_ref': 'businessref_97', 'cnt': '1'}, {'business_ref': 'businessref_62', 'cnt': '1'}, {'business_ref': 'businessref_72', 'cnt': '1'}, {'business_ref': 'businessref_37', 'cnt': '1'}, {'business_ref': 'businessref_92', 'cnt': '2'}, {'business_ref': 'businessref_41', 'cnt': '1'}, {'business_ref': 'businessref_10', 'cnt': '1'}, {'business_ref': 'businessref_45', 'cnt': '3'}, {'business_ref': 'businessref_36', 'cnt': '2'}, {'business_ref': 'businessref_60', 'cnt': '2'}, {'business_ref': 'businessref_12', 'cnt': '1'}, {'business_ref': 'businessref_96', 'cnt': '2'}, {'business_ref': 'businessref_98', 'cnt': '1'}, {'business_ref': 'businessref_14', 'cnt': '1'}, {'business_ref': 'businessref_20', 'cnt': '1'}, {'business_ref': 'businessref_26', 'cnt': '1'}, {'business_ref': 'businessref_68', 'cnt': '1'}, {'business_ref': 'businessref_13', 'cnt': '1'}, {'business_ref': 'businessref_79', 'cnt': '1'}], 'var_function-call-15270022369569263637': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-15130111299802888071': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-3558505736593885810': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-11467388034751646705': 'file_storage/function-call-11467388034751646705.json', 'var_function-call-15854128855345954979': [['Restaurants', 16], ['Food', 12], ['Shopping', 9], ['American (New)', 7], ['Beauty & Spas', 6], ['Grocery', 6], ['Fast Food', 5], ['Chinese', 4], ['Hair Removal', 4], ['Wine Bars', 4]], 'var_function-call-16426860042278345878': [{'name': 'N/A', 'cats': ['Restaurants', 'Breakfast & Brunch', 'American (New)', 'Cafes,'], 'desc': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}, {'name': 'N/A', 'cats': ['Nail Salons', 'Hair Removal', 'Beauty & Spas', 'and Waxing'], 'desc': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'name': 'N/A', 'cats': ['Movers', 'American (New)', 'Landscape Architects', 'Food', 'Home Services', 'Self Storage', 'Local Services', 'Restaurants'], 'desc': 'Located at 13605 W Hillsborough Ave in Tampa, FL, this versatile establishment offers a range of services and dining options, including Movers, American (New), Landscape Architects, Food, Home Services, Self Storage, Local Services, Restaurants.'}, {'name': 'N/A', 'cats': ['American (New)', 'Restaurants', 'American (Traditional)', 'Asian Fusion', 'Noodles', 'Dim Sum', 'Fast Food', 'Chinese', 'catering to a variety of tastes', 'preferences'], 'desc': 'Located at 705 East Passyunk Ave in Philadelphia, PA, this vibrant eatery offers a diverse menu featuring American (New), Restaurants, American (Traditional), Asian Fusion, Noodles, Dim Sum, Fast Food, Chinese, catering to a variety of tastes and preferences.'}, {'name': 'N/A', 'cats': ['Photography Stores & Services', 'Shopping', 'Grocery', 'and Food'], 'desc': 'Located at 8424 Sheldon Rd in Tampa, FL, this establishment offers a diverse range of products and services, including Photography Stores & Services, Shopping, Grocery, and Food.'}, {'name': 'N/A', 'cats': ['Cosmetics & Beauty Supply', 'Cosmetic Dentists', 'Tanning', 'Teeth Whitening', 'Beauty & Spas', 'Dentists', 'Shopping', 'Blow Dry/Out Services', 'Health & Medical', 'Spray Tanning', 'and Hair Salons'], 'desc': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'name': 'N/A', 'cats': ['Food', 'Grocery', 'Shopping'], 'desc': 'Located at 2900 4th St N in St. Petersburg, FL, this establishment offers a diverse range of products and services in the categories of Food, Grocery, Shopping.'}, {'name': 'N/A', 'cats': ['Food', 'Shopping', 'Fashion', 'Discount Store', 'Grocery', 'Electronics', 'Drugstores', 'Department Stores', 'ensuring that visitors can find everything they need in one convenient location'], 'desc': 'Located at 8101 W Judge Perez Dr in Chalmette, LA, this versatile establishment offers a wide range of options for customers, including Food, Shopping, Fashion, Discount Store, Grocery, Electronics, Drugstores, Department Stores, ensuring that visitors can find everything they need in one convenient location.'}, {'name': 'N/A', 'cats': ['Wine Bars', 'American (New)', 'Cocktail Bars', 'Restaurants', 'American (Traditional)', 'Nightlife', 'and Bars'], 'desc': 'Located at 3257 Ivanhoe Ave in Saint Louis, MO, this establishment offers a vibrant atmosphere perfect for enjoying a diverse selection of experiences, including Wine Bars, American (New), Cocktail Bars, Restaurants, American (Traditional), Nightlife, and Bars.'}, {'name': 'N/A', 'cats': ['Restaurants', 'American (New)', 'Caterers', 'Fast Food', 'Chicken Shop', 'Event Planning & Services', 'and American (Traditional)'], 'desc': 'Located at 9040 State Road 54 in Trinity, FL, this establishment offers a diverse array of options, including Restaurants, American (New), Caterers, Fast Food, Chicken Shop, Event Planning & Services, and American (Traditional).'}]}

exec(code, env_args)

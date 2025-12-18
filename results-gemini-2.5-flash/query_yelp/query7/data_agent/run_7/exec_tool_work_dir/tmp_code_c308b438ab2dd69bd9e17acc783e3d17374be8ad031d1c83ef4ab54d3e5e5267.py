code = """import pandas as pd
import re

reviews_2016_users = pd.DataFrame(locals()['var_function-call-14957950743961238889'])
business_info = pd.DataFrame(locals()['var_function-call-2879866622492795804'])

# Convert business_ref to business_id format for merging
reviews_2016_users['business_id'] = reviews_2016_users['business_ref'].apply(lambda x: x.replace('businessref_', 'businessid_'))

# Merge the two dataframes
merged_df = pd.merge(reviews_2016_users, business_info, on='business_id', how='inner')

# Initialize a dictionary to store category review counts
category_review_counts = {}

# Process each business description to extract categories and sum review counts
for index, row in merged_df.iterrows():
    description = row['description']
    review_count = int(row['review_count'])

    # Extract categories from description
    # This regex looks for phrases like "in the fields of X, Y, Z" or "in the category of X, Y, Z"
    # and also handles cases where categories are directly listed after a general description.
    matches = re.findall(r'(?:in the fields of |in the category of |seeking |including )([^.]+)', description, re.IGNORECASE)
    categories_str = ''
    if matches:
        categories_str = matches[0]
    elif 'services in ' in description:
        start_index = description.find('services in ') + len('services in ')
        end_index = description.find('.', start_index)
        if end_index != -1:
            categories_str = description[start_index:end_index]
        else:
            categories_str = description[start_index:]
    elif 'offers a diverse range of services and products in the fields of ' in description:
        start_index = description.find('offers a diverse range of services and products in the fields of ') + len('offers a diverse range of services and products in the fields of ')
        end_index = description.find('.', start_index)
        if end_index != -1:
            categories_str = description[start_index:end_index]
        else:
            categories_str = description[start_index:]
    elif 'offers a range of services including ' in description:
        start_index = description.find('offers a range of services including ') + len('offers a range of services including ')
        end_index = description.find('.', start_index)
        if end_index != -1:
            categories_str = description[start_index:end_index]
        else:
            categories_str = description[start_index:]
    elif 'delightful selection of treats, making it a must-visit for anyone seeking ' in description:
        start_index = description.find('delightful selection of treats, making it a must-visit for anyone seeking ') + len('delightful selection of treats, making it a must-visit for anyone seeking ')
        end_index = description.find('.', start_index)
        if end_index != -1:
            categories_str = description[start_index:end_index]
        else:
            categories_str = description[start_index:]

    # Clean and split categories
    categories = [cat.strip() for cat in categories_str.replace(' and ', ', ').split(',') if cat.strip()]

    for category in categories:
        category_review_counts[category] = category_review_counts.get(category, 0) + review_count

# Sort categories by total review count and get the top 5
sorted_categories = sorted(category_review_counts.items(), key=lambda item: item[1], reverse=True)
top_5_categories = sorted_categories[:5]

print('__RESULT__:')
print(pd.Series(dict(top_5_categories)).to_json())"""

env_args = {'var_function-call-1472414689921903724': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_function-call-14957950743961238889': [{'user_id': 'userid_1101', 'business_ref': 'businessref_74'}, {'user_id': 'userid_1105', 'business_ref': 'businessref_57'}, {'user_id': 'userid_863', 'business_ref': 'businessref_96'}, {'user_id': 'userid_308', 'business_ref': 'businessref_45'}, {'user_id': 'userid_729', 'business_ref': 'businessref_74'}, {'user_id': 'userid_935', 'business_ref': 'businessref_53'}, {'user_id': 'userid_1856', 'business_ref': 'businessref_41'}, {'user_id': 'userid_435', 'business_ref': 'businessref_96'}, {'user_id': 'userid_1178', 'business_ref': 'businessref_10'}, {'user_id': 'userid_1109', 'business_ref': 'businessref_66'}, {'user_id': 'userid_593', 'business_ref': 'businessref_31'}, {'user_id': 'userid_1182', 'business_ref': 'businessref_92'}, {'user_id': 'userid_230', 'business_ref': 'businessref_26'}, {'user_id': 'userid_244', 'business_ref': 'businessref_98'}, {'user_id': 'userid_1316', 'business_ref': 'businessref_45'}, {'user_id': 'userid_324', 'business_ref': 'businessref_45'}, {'user_id': 'userid_1850', 'business_ref': 'businessref_36'}, {'user_id': 'userid_686', 'business_ref': 'businessref_14'}, {'user_id': 'userid_1950', 'business_ref': 'businessref_86'}, {'user_id': 'userid_945', 'business_ref': 'businessref_57'}, {'user_id': 'userid_1179', 'business_ref': 'businessref_13'}, {'user_id': 'userid_1879', 'business_ref': 'businessref_68'}, {'user_id': 'userid_850', 'business_ref': 'businessref_36'}, {'user_id': 'userid_958', 'business_ref': 'businessref_60'}, {'user_id': 'userid_1661', 'business_ref': 'businessref_20'}, {'user_id': 'userid_210', 'business_ref': 'businessref_15'}, {'user_id': 'userid_151', 'business_ref': 'businessref_62'}, {'user_id': 'userid_100', 'business_ref': 'businessref_33'}, {'user_id': 'userid_598', 'business_ref': 'businessref_37'}, {'user_id': 'userid_746', 'business_ref': 'businessref_92'}, {'user_id': 'userid_1675', 'business_ref': 'businessref_66'}, {'user_id': 'userid_1505', 'business_ref': 'businessref_33'}, {'user_id': 'userid_842', 'business_ref': 'businessref_6'}, {'user_id': 'userid_257', 'business_ref': 'businessref_12'}, {'user_id': 'userid_1333', 'business_ref': 'businessref_79'}, {'user_id': 'userid_711', 'business_ref': 'businessref_60'}], 'var_function-call-15920065654312307063': ['businessid_74', 'businessid_57', 'businessid_96', 'businessid_45', 'businessid_53', 'businessid_41', 'businessid_10', 'businessid_66', 'businessid_31', 'businessid_92', 'businessid_26', 'businessid_98', 'businessid_36', 'businessid_14', 'businessid_86', 'businessid_13', 'businessid_68', 'businessid_60', 'businessid_20', 'businessid_15', 'businessid_62', 'businessid_33', 'businessid_37', 'businessid_6', 'businessid_12', 'businessid_79'], 'var_function-call-16215448371619584834': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}], 'var_function-call-3271194984507839421': ['businessid_74', 'businessid_57', 'businessid_96', 'businessid_45', 'businessid_53', 'businessid_41', 'businessid_10', 'businessid_66', 'businessid_31', 'businessid_92', 'businessid_26', 'businessid_98', 'businessid_36', 'businessid_14', 'businessid_86', 'businessid_13', 'businessid_68', 'businessid_60', 'businessid_20', 'businessid_15', 'businessid_62', 'businessid_33', 'businessid_37', 'businessid_6', 'businessid_12', 'businessid_79'], 'var_function-call-17185824262128261817': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'review_count': '7', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'review_count': '39', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'review_count': '20', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}], 'var_function-call-1222725992263440432': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}], 'var_function-call-2879866622492795804': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'review_count': '7', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'review_count': '39', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'review_count': '20', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}]}

exec(code, env_args)

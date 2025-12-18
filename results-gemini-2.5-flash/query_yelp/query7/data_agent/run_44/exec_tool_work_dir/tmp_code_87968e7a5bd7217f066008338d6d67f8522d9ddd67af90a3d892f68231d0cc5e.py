code = """import json
business_reviews_map = locals()['var_function-call-6914520315834151222']
business_info = locals()['var_function-call-11903000774999534110']

category_review_counts = {}

for business in business_info:
    business_id = business['business_id']
    description = business['description']
    review_count = business_reviews_map.get(business_id, 0)

    # Extract categories from the description. Assuming categories are listed after 'in the fields of' or similar.
    # This is a simplified parsing and might need adjustment based on more description examples.
    categories_str_start = description.find('in the fields of')
    if categories_str_start == -1:
        categories_str_start = description.find('in the category of')
    if categories_str_start == -1:
        categories_str_start = description.find('offers a range of services in')
    if categories_str_start == -1:
        categories_str_start = description.find('offers a diverse range of services and products in the fields of')
    if categories_str_start == -1:
        categories_str_start = description.find('offers a delightful array of dishes in the category of')

    categories = []
    if categories_str_start != -1:
        # Adjust start index to get to the actual category list
        categories_str_start += len('in the fields of') # or other phrases, take the longest one to be safe
        if description.find('in the category of') != -1 and description.find('in the category of') < categories_str_start:
            categories_str_start = description.find('in the category of') + len('in the category of')
        if description.find('offers a range of services in') != -1 and description.find('offers a range of services in') < categories_str_start:
            categories_str_start = description.find('offers a range of services in') + len('offers a range of services in')
        if description.find('offers a diverse range of services and products in the fields of') != -1 and description.find('offers a diverse range of services and products in the fields of') < categories_str_start:
            categories_str_start = description.find('offers a diverse range of services and products in the fields of') + len('offers a diverse range of services and products in the fields of')
        if description.find('offers a delightful array of dishes in the category of') != -1 and description.find('offers a delightful array of dishes in the category of') < categories_str_start:
            categories_str_start = description.find('offers a delightful array of dishes in the category of') + len('offers a delightful array of dishes in the category of')

        categories_str = description[categories_str_start:].split('.')[0].strip()
        categories = [cat.strip() for cat in categories_str.split(',')]
    
    # Fallback if no specific phrase is found, try to extract any capitalized words as categories
    if not categories and description:
        potential_categories = [word.strip() for word in description.replace('-',' ').replace('/',' ').replace('&',' ').split() if word and word[0].isupper()]
        # Filter out common non-category words
        non_category_words = ["Located", "Ste", "Saint", "Petersburg", "FL", "King", "Prussia", "PA", "Dodecanese", "Blvd", "Tarpon", "Springs", "establishment", "selection", "treats", "Louis", "MO", "This", "facility", "Avon", "IN"]
        categories = [cat for cat in potential_categories if cat not in non_category_words]
        
    for category in categories:
        if category:
            category_review_counts[category] = category_review_counts.get(category, 0) + review_count

sorted_categories = sorted(category_review_counts.items(), key=lambda item: item[1], reverse=True)
top_5_categories = sorted_categories[:5]

print('__RESULT__:')
print(json.dumps(top_5_categories))"""

env_args = {'var_function-call-12579857255835530480': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_function-call-3997259010642589127': "'userid_746', 'userid_1109', 'userid_1950', 'userid_1316', 'userid_1182', 'userid_151', 'userid_1158', 'userid_508', 'userid_435', 'userid_958', 'userid_1879', 'userid_308', 'userid_1179', 'userid_324', 'userid_863', 'userid_100', 'userid_1333', 'userid_1636', 'userid_1850', 'userid_711', 'userid_729', 'userid_1505', 'userid_1315', 'userid_1708', 'userid_1661', 'userid_850', 'userid_1675', 'userid_227', 'userid_577', 'userid_257', 'userid_598', 'userid_847', 'userid_673', 'userid_1856', 'userid_384', 'userid_935', 'userid_210', 'userid_1101', 'userid_945', 'userid_842', 'userid_1351', 'userid_230', 'userid_593', 'userid_1431', 'userid_686', 'userid_527', 'userid_244', 'userid_393', 'userid_1178', 'userid_526', 'userid_90', 'userid_238', 'userid_1105'", 'var_function-call-6194666950827000179': [{'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_33', 'review_count': '3'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_51', 'review_count': '2'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_6', 'review_count': '2'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_8', 'review_count': '1'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_97', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_9', 'review_count': '1'}, {'business_ref': 'businessref_72', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}], 'var_function-call-6914520315834151222': {'businessid_45': 3, 'businessid_33': 3, 'businessid_74': 2, 'businessid_66': 2, 'businessid_51': 2, 'businessid_92': 2, 'businessid_96': 2, 'businessid_57': 2, 'businessid_36': 2, 'businessid_60': 2, 'businessid_6': 2, 'businessid_53': 1, 'businessid_8': 1, 'businessid_86': 1, 'businessid_97': 1, 'businessid_62': 1, 'businessid_13': 1, 'businessid_79': 1, 'businessid_9': 1, 'businessid_72': 1, 'businessid_37': 1, 'businessid_12': 1, 'businessid_31': 1, 'businessid_15': 1, 'businessid_26': 1, 'businessid_68': 1, 'businessid_41': 1, 'businessid_10': 1, 'businessid_98': 1, 'businessid_14': 1, 'businessid_20': 1}, 'var_function-call-7977288275688467560': ['businessid_45', 'businessid_33', 'businessid_74', 'businessid_66', 'businessid_51', 'businessid_92', 'businessid_96', 'businessid_57', 'businessid_36', 'businessid_60', 'businessid_6', 'businessid_53', 'businessid_8', 'businessid_86', 'businessid_97', 'businessid_62', 'businessid_13', 'businessid_79', 'businessid_9', 'businessid_72', 'businessid_37', 'businessid_12', 'businessid_31', 'businessid_15', 'businessid_26', 'businessid_68', 'businessid_41', 'businessid_10', 'businessid_98', 'businessid_14', 'businessid_20'], 'var_function-call-11903000774999534110': [{'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}]}

exec(code, env_args)

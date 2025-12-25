code = """import json
import pandas as pd

business_reviews_df = pd.DataFrame(locals()['var_function-call-743341897959759894'])
business_details_df = pd.DataFrame(locals()['var_function-call-13623862921968931342'])

# Standardize business_ref to business_id for merging
business_reviews_df['business_id'] = business_reviews_df['business_ref'].str.replace('businessref_', 'businessid_')

# Merge the two dataframes
merged_df = pd.merge(business_reviews_df, business_details_df, on='business_id')

# Function to extract categories from the description string
def extract_categories(description):
    if isinstance(description, str):
        parts = description.split(' in the fields of ')
        if len(parts) > 1:
            categories_str = parts[1].split('.')[0]
            return [cat.strip() for cat in categories_str.split(', ')]
        else:
            parts_after_category = description.split(' in the category of ')
            if len(parts_after_category) > 1:
                categories_str = parts_after_category[1].strip().replace('\'', '').replace('.', '')
                return [cat.strip() for cat in categories_str.split(', ')]
            else:
                # If the above patterns don't match, look for categories after 'services including', 'services', 'delightful selection of treats, making it a must-visit for anyone seeking' etc.
                if 'services including' in description:
                    start_index = description.find('services including') + len('services including')
                    end_index = description.find('.', start_index)
                    if end_index == -1: # if no period, take till end of string
                        end_index = len(description)
                    categories_str = description[start_index:end_index].strip()
                    return [cat.strip() for cat in categories_str.split(', ')]
                elif 'offers a range of services in' in description:
                    start_index = description.find('offers a range of services in') + len('offers a range of services in')
                    end_index = description.find('.', start_index)
                    if end_index == -1: # if no period, take till end of string
                        end_index = len(description)
                    categories_str = description[start_index:end_index].strip()
                    return [cat.strip() for cat in categories_str.split(', ')]
                elif 'delightful selection of treats, making it a must-visit for anyone seeking' in description:
                    start_index = description.find('delightful selection of treats, making it a must-visit for anyone seeking') + len('delightful selection of treats, making it a must-visit for anyone seeking')
                    end_index = description.find('.', start_index)
                    if end_index == -1: # if no period, take till end of string
                        end_index = len(description)
                    categories_str = description[start_index:end_index].strip()
                    return [cat.strip() for cat in categories_str.split(', ')]
                elif 'establishment offers a delightful array of dishes in the category of' in description:
                    start_index = description.find('establishment offers a delightful array of dishes in the category of') + len('establishment offers a delightful array of dishes in the category of')
                    end_index = description.find('.', start_index)
                    if end_index == -1: # if no period, take till end of string
                        end_index = len(description)
                    categories_str = description[start_index:end_index].strip().replace("'", "")
                    return [cat.strip() for cat in categories_str.split(', ')]
    return []

# Apply the function to extract categories
merged_df['categories'] = merged_df['description'].apply(extract_categories)

# Explode the categories list to have one category per row
exploded_df = merged_df.explode('categories')

# Convert total_reviews to numeric (it was a string from the DB query)
exploded_df['total_reviews'] = pd.to_numeric(exploded_df['total_reviews'])

# Group by category and sum the total reviews
category_reviews = exploded_df.groupby('categories')['total_reviews'].sum().reset_index()

# Sort and get the top 5
top_5_categories = category_reviews.sort_values(by='total_reviews', ascending=False).head(5)

print("__RESULT__:")
print(top_5_categories.to_json(orient='records'))"""

env_args = {'var_function-call-4711394474308098909': ['review', 'tip', 'user'], 'var_function-call-2580270759488346142': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_function-call-17818700405272798007': "'userid_746', 'userid_1109', 'userid_1950', 'userid_1316', 'userid_1182', 'userid_151', 'userid_1158', 'userid_508', 'userid_435', 'userid_958', 'userid_1879', 'userid_308', 'userid_1179', 'userid_324', 'userid_863', 'userid_100', 'userid_1333', 'userid_1636', 'userid_1850', 'userid_711', 'userid_729', 'userid_1505', 'userid_1315', 'userid_1708', 'userid_1661', 'userid_850', 'userid_1675', 'userid_227', 'userid_577', 'userid_257', 'userid_598', 'userid_847', 'userid_673', 'userid_1856', 'userid_384', 'userid_935', 'userid_210', 'userid_1101', 'userid_945', 'userid_842', 'userid_1351', 'userid_230', 'userid_593', 'userid_1431', 'userid_686', 'userid_527', 'userid_244', 'userid_393', 'userid_1178', 'userid_526', 'userid_90', 'userid_238', 'userid_1105'", 'var_function-call-743341897959759894': [{'business_ref': 'businessref_13', 'total_reviews': '1'}, {'business_ref': 'businessref_79', 'total_reviews': '1'}, {'business_ref': 'businessref_6', 'total_reviews': '1'}, {'business_ref': 'businessref_74', 'total_reviews': '2'}, {'business_ref': 'businessref_66', 'total_reviews': '2'}, {'business_ref': 'businessref_15', 'total_reviews': '1'}, {'business_ref': 'businessref_33', 'total_reviews': '2'}, {'business_ref': 'businessref_31', 'total_reviews': '1'}, {'business_ref': 'businessref_53', 'total_reviews': '1'}, {'business_ref': 'businessref_57', 'total_reviews': '2'}, {'business_ref': 'businessref_86', 'total_reviews': '1'}, {'business_ref': 'businessref_62', 'total_reviews': '1'}, {'business_ref': 'businessref_37', 'total_reviews': '1'}, {'business_ref': 'businessref_92', 'total_reviews': '2'}, {'business_ref': 'businessref_36', 'total_reviews': '2'}, {'business_ref': 'businessref_60', 'total_reviews': '2'}, {'business_ref': 'businessref_12', 'total_reviews': '1'}, {'business_ref': 'businessref_26', 'total_reviews': '1'}, {'business_ref': 'businessref_68', 'total_reviews': '1'}, {'business_ref': 'businessref_41', 'total_reviews': '1'}, {'business_ref': 'businessref_10', 'total_reviews': '1'}, {'business_ref': 'businessref_45', 'total_reviews': '3'}, {'business_ref': 'businessref_96', 'total_reviews': '2'}, {'business_ref': 'businessref_98', 'total_reviews': '1'}, {'business_ref': 'businessref_14', 'total_reviews': '1'}, {'business_ref': 'businessref_20', 'total_reviews': '1'}], 'var_function-call-9794601794960528341': ['businessid_13', 'businessid_79', 'businessid_6', 'businessid_74', 'businessid_66', 'businessid_15', 'businessid_33', 'businessid_31', 'businessid_53', 'businessid_57', 'businessid_86', 'businessid_62', 'businessid_37', 'businessid_92', 'businessid_36', 'businessid_60', 'businessid_12', 'businessid_26', 'businessid_68', 'businessid_41', 'businessid_10', 'businessid_45', 'businessid_96', 'businessid_98', 'businessid_14', 'businessid_20'], 'var_function-call-13623862921968931342': [{'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}]}

exec(code, env_args)

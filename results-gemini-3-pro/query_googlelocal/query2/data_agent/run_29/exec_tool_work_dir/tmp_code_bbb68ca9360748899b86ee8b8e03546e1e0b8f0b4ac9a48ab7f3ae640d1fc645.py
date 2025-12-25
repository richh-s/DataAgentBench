code = """import pandas as pd
import json

businesses = locals()['var_function-call-14264516201352559572']
ratings = locals()['var_function-call-10847421885010415895']

df_bus = pd.DataFrame(businesses)
df_rat = pd.DataFrame(ratings)

# Ensure rating is numeric
df_rat['average_rating'] = pd.to_numeric(df_rat['average_rating'])

# Merge
df = pd.merge(df_bus, df_rat, on='gmap_id')

# Filter
df_filtered = df[df['average_rating'] >= 4.0].copy()

# Format output: list of "Business Name: Rating"
results = []
for index, row in df_filtered.iterrows():
    results.append(f"{row['name']}: {row['average_rating']:.2f}")

# Sort for consistency? Not required but nice.
results.sort()

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-6029013321288534612': ['business_description'], 'var_function-call-3166015244451777807': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_function-call-17391159569479443656': [], 'var_function-call-12282010025662377281': [{'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_function-call-13963443842455720612': [{'count': '7'}], 'var_function-call-14264516201352559572': [{'name': 'Angel-A Massage', 'gmap_id': 'gmap_22'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28'}], 'var_function-call-10847421885010415895': [{'gmap_id': 'gmap_20', 'average_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'average_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'average_rating': '4.333333333333333'}, {'gmap_id': 'gmap_24', 'average_rating': '3.875'}, {'gmap_id': 'gmap_25', 'average_rating': '5.0'}, {'gmap_id': 'gmap_28', 'average_rating': '3.875'}, {'gmap_id': 'gmap_33', 'average_rating': '2.125'}]}

exec(code, env_args)

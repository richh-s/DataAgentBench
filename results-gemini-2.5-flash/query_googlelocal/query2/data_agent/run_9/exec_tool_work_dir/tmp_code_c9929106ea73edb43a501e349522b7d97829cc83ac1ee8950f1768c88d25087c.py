code = """import json
import pandas as pd
businesses_data = locals()['var_function-call-15778883051346157504']
ratings_data = locals()['var_function-call-16112281268932101041']

df_businesses = pd.DataFrame(businesses_data)
df_ratings = pd.DataFrame(ratings_data)

merged_df = pd.merge(df_businesses, df_ratings, on='gmap_id')

result = merged_df[merged_df['average_rating'] >= 4.0][['name', 'average_rating']].to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-667212993275766917': [], 'var_function-call-12998527350881197440': [], 'var_function-call-5504936304464255431': [{'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}, {'description': ' This inviting eatery in La Mirada, CA 90638 serves a diverse menu of delicious dishes, perfect for casual dining and family gatherings.'}, {'description': ' Offering a wide selection of winter sports equipment for hire, this service in Mammoth Lakes, CA 93546 ensures you’re fully equipped for an unforgettable day on the slopes.'}, {'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'description': 'Chain selling interior & exterior paints, primers & finishes, plus supplies. This vibrant shop in Roseville, CA 95661 offers a wide variety of high-quality coatings and supplies for all your home improvement and artistic needs.'}, {'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}], 'var_function-call-15778883051346157504': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}], 'var_function-call-7070165158624327311': ['gmap_22', 'gmap_25', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_21'], 'var_function-call-16112281268932101041': [{'gmap_id': 'gmap_20', 'average_rating': '4.178571428571429'}, {'gmap_id': 'gmap_22', 'average_rating': '4.333333333333333'}, {'gmap_id': 'gmap_25', 'average_rating': '5.0'}]}

exec(code, env_args)

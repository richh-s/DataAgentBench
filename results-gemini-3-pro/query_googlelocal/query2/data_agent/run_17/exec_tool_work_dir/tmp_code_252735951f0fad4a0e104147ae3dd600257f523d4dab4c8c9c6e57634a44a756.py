code = """import json
import pandas as pd

# Load ratings
ratings_data = locals()['var_function-call-13240606371245120866']
df_ratings = pd.DataFrame(ratings_data)
df_ratings['avg_rating'] = df_ratings['avg_rating'].astype(float)

# Load business descriptions again to get names
file_path = locals()['var_function-call-12456048630448416656']
with open(file_path, 'r') as f:
    businesses = json.load(f)
df_bus = pd.DataFrame(businesses)

# Merge
result_df = pd.merge(df_ratings, df_bus[['gmap_id', 'name']], on='gmap_id')

# Format results
results = []
for index, row in result_df.iterrows():
    results.append(f"{row['name']} (Average Rating: {row['avg_rating']:.2f})")

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-11714623949736088946': ['business_description'], 'var_function-call-5466828393828967677': [{'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'name': 'Matrix International Textiles', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}], 'var_function-call-5308975848173412316': [], 'var_function-call-4244075036364012384': [], 'var_function-call-15330369549704321649': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_function-call-2722946594529538049': [{'name': 'Angel-A Massage', 'MISC': 'None'}], 'var_function-call-5182497027438983040': [], 'var_function-call-16632169224067963326': [], 'var_function-call-5570078938788500447': [{'count': '79'}], 'var_function-call-12456048630448416656': 'file_storage/function-call-12456048630448416656.json', 'var_function-call-5827187141633292312': ['gmap_22', 'gmap_25', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_32', 'gmap_21', 'gmap_28'], 'var_function-call-9626455426182445019': "SELECT gmap_id, AVG(rating) as avg_rating FROM review WHERE gmap_id IN ('gmap_22', 'gmap_25', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_32', 'gmap_21', 'gmap_28') GROUP BY gmap_id HAVING AVG(rating) >= 4.0", 'var_function-call-13240606371245120866': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}]}

exec(code, env_args)

code = """import pandas as pd

la_businesses = locals()['var_function-call-7518171138648908887']
la_gmap_ids = [business['gmap_id'] for business in la_businesses]

# Prepare the gmap_ids for the SQL IN clause
gmap_ids_str = ', '.join(f"'{gmap_id}'" for gmap_id in la_gmap_ids)

# Construct the SQL query for review_database
query = f"SELECT gmap_id, rating FROM review WHERE gmap_id IN ({gmap_ids_str});"

print('__RESULT__:')
print(query)"""

env_args = {'var_function-call-8495085119743523882': ['business_description'], 'var_function-call-8495085119743522125': ['review'], 'var_function-call-3852781814920022347': [], 'var_function-call-6526109559000218106': [{'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}], 'var_function-call-3018724079792324598': [{'name': 'City Textile', 'gmap_id': 'gmap_44'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38'}, {'name': 'Beads and More', 'gmap_id': 'gmap_39'}, {'name': 'Ace Jewelry & Loan', 'gmap_id': 'gmap_42'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}], 'var_function-call-14492911187599790290': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_function-call-9184171315617095609': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_function-call-7518171138648908887': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)

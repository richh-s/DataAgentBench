code = """import pandas as pd
import json

# Load the full business data from the stored JSON file
with open(locals()['var_function-call-2056214235904761986'], 'r') as f:
    business_data = json.load(f)

business_df = pd.DataFrame(business_data)

# Filter for businesses related to massage therapy
massage_businesses_df = business_df[business_df['description'].str.contains('massage|bodywork|therapies', case=False, na=False)]

# Get the gmap_ids of these businesses
massage_gmap_ids = massage_businesses_df['gmap_id'].tolist()

print('__RESULT__:')
print(json.dumps(massage_gmap_ids))"""

env_args = {'var_function-call-18320300112929708067': ['business_description'], 'var_function-call-18308021375892395550': [], 'var_function-call-14762917165535927528': [{'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'name': 'City Textile'}, {'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'name': 'San Soo Dang'}, {'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'name': 'Nova Fabrics'}, {'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'name': 'Nobel Textile Co'}, {'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'name': 'Matrix International Textiles'}, {'description': ' This inviting eatery in La Mirada, CA 90638 serves a diverse menu of delicious dishes, perfect for casual dining and family gatherings.', 'name': 'Vons Chicken'}, {'description': ' Offering a wide selection of winter sports equipment for hire, this service in Mammoth Lakes, CA 93546 ensures you’re fully equipped for an unforgettable day on the slopes.', 'name': 'Black Tie Ski Rental Delivery of Mammoth'}, {'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.', 'name': 'Angel-A Massage'}, {'description': 'Chain selling interior & exterior paints, primers & finishes, plus supplies. This vibrant shop in Roseville, CA 95661 offers a wide variety of high-quality coatings and supplies for all your home improvement and artistic needs.', 'name': 'Dunn-Edwards Paints'}, {'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.', 'name': 'Elite Massage'}], 'var_function-call-12322790892699588211': [], 'var_function-call-2056214235904761986': 'file_storage/function-call-2056214235904761986.json'}

exec(code, env_args)

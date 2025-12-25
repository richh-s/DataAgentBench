code = """import json
import pandas as pd

# Load the business descriptions
file_path = locals()['var_function-call-12456048630448416656']
with open(file_path, 'r') as f:
    businesses = json.load(f)

df_bus = pd.DataFrame(businesses)

# Filter for massage therapy businesses
# Criteria: 'massage' in name OR 'massage' in description OR 'bodywork' in description
# Case insensitive
def is_massage_business(row):
    name = row.get('name', '').lower()
    desc = row.get('description', '').lower()
    
    if 'massage' in name:
        return True
    if 'massage' in desc:
        return True
    if 'bodywork' in desc:
        return True
    if 'therapies' in desc and 'treatments' in desc: # For J B Oriental Inc case
        return True
    return False

massage_businesses = df_bus[df_bus.apply(is_massage_business, axis=1)]

gmap_ids = massage_businesses['gmap_id'].tolist()
print(f"Found {len(gmap_ids)} massage businesses.")
print(gmap_ids)

# Prepare result for next step
print("__RESULT__:")
print(json.dumps(gmap_ids))"""

env_args = {'var_function-call-11714623949736088946': ['business_description'], 'var_function-call-5466828393828967677': [{'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'name': 'Matrix International Textiles', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}], 'var_function-call-5308975848173412316': [], 'var_function-call-4244075036364012384': [], 'var_function-call-15330369549704321649': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_function-call-2722946594529538049': [{'name': 'Angel-A Massage', 'MISC': 'None'}], 'var_function-call-5182497027438983040': [], 'var_function-call-16632169224067963326': [], 'var_function-call-5570078938788500447': [{'count': '79'}], 'var_function-call-12456048630448416656': 'file_storage/function-call-12456048630448416656.json'}

exec(code, env_args)

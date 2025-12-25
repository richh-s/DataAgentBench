code = """import json
import pandas as pd

# Get the file path from the variable
file_path = locals()['var_function-call-5166302132309812562']

# Load the full result from the file
with open(file_path, 'r') as f:
    businesses = json.load(f)

df = pd.DataFrame(businesses)

# Define a function to check for massage therapy business
# "massage therapy" is the key phrase. I'll look for "massage" or "therapy" related terms.
# Given the previous inspection, "massage" in name is strong.
# Description often has "therapists", "bodywork".
def is_massage_business(row):
    name = str(row['name']).lower()
    desc = str(row['description']).lower()
    
    # Primary check: "massage" in name
    if 'massage' in name:
        return True
    
    # Secondary check: description strongly implies it
    # "bodywork" is very specific to massage/chiropractic
    # "skilled therapists" + "soothing treatments"
    if 'massage' in desc:
        return True
    if 'bodywork' in desc:
        return True
    if 'reflexology' in desc:
        return True
    # "therapy" alone might be physical therapy or counseling, so maybe be careful
    # But user asked for "massage therapy".
    # If name doesn't have massage, and description has "therapy", check if context is body/wellness
    if 'therapy' in desc or 'therapist' in desc:
        if 'wellness' in desc or 'relax' in desc or 'body' in desc or 'spa' in desc or 'soothing' in desc:
            return True
            
    return False

massage_businesses = df[df.apply(is_massage_business, axis=1)]

# Prepare list of gmap_ids
gmap_ids = massage_businesses['gmap_id'].tolist()
names_map = massage_businesses.set_index('gmap_id')['name'].to_dict()

print("__RESULT__:")
print(json.dumps({'gmap_ids': gmap_ids, 'names_map': names_map}))"""

env_args = {'var_function-call-18232610896439523177': [], 'var_function-call-110036077417332400': [{'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'name': 'Matrix International Textiles', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}], 'var_function-call-7449773937608490170': [], 'var_function-call-9776069078872808730': [{'count': '79'}], 'var_function-call-5166302132309812562': 'file_storage/function-call-5166302132309812562.json'}

exec(code, env_args)

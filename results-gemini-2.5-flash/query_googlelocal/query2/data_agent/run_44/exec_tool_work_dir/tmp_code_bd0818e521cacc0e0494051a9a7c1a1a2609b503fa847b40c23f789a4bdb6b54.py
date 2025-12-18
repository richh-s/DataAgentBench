code = """import pandas as pd
import json

with open(locals()['var_function-call-2052708101499572230'], 'r') as f:
    business_data = json.load(f)

df_business = pd.DataFrame(business_data)

massage_therapy_businesses = df_business[df_business['description'].str.contains('massage|therapy', case=False, na=False)]

# Exclude businesses with "textile" or "fabric" in their description to avoid false positives
massage_therapy_businesses = massage_therapy_businesses[~massage_therapy_businesses['description'].str.contains('textile|fabric', case=False, na=False)]


__RESULT__:
print(massage_therapy_businesses.to_json(orient='records'))"""

env_args = {'var_function-call-5806132711522617287': [], 'var_function-call-2920753959660314623': [], 'var_function-call-3123390929511229942': ['business_description'], 'var_function-call-17070349829733189226': [{'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}], 'var_function-call-2352639253836709257': ['review'], 'var_function-call-12402395841031509992': [], 'var_function-call-11621653440149310878': [], 'var_function-call-932136603055988270': 'file_storage/function-call-932136603055988270.json', 'var_function-call-2052708101499572230': 'file_storage/function-call-2052708101499572230.json'}

exec(code, env_args)

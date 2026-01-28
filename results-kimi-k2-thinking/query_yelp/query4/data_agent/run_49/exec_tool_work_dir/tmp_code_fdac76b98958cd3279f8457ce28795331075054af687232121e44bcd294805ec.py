code = """import json
import pandas as pd
import re

# Read the business data from file
business_file = str(var_functions.query_db:9)
print("Reading file:", business_file)

with open(business_file, 'r') as f:
    business_data = json.load(f)

# Convert to DataFrame
df_business = pd.DataFrame(business_data)

# Parse categories from description
def extract_categories(description):
    if pd.isna(description) or description is None:
        return []
    
    # Common patterns in descriptions
    patterns = [
        r"in the (?:fields of|category of) '([^']+)'",
        r"services? in ([^\.\,]+)",
        r"offers? a range of services? in ([^\.\,]+)",
        r"offers? a delightful array of ([^\.\,]+)",
        r"offers? a wide range of ([^\.\,]+)",
        r"offers? a diverse (?:range of|selection of) ([^\.\,]+)",
        r"offers? a delightful mix of ([^\.\,]+)",
        r"offers? enthusiasts a premier destination for ([^\.\,]+)",
        r"specializes in ([^\.\,]+)",        
        r"categories? of ([^\.\,]+)",
    ]
    
    for pattern in patterns:
        match = re.search(pattern, description.lower(), re.IGNORECASE)
        if match:
            # Split by comma or 'and' and clean up
            categories_str = match.group(1)
            # Split by commas and 'and'
            split_categories = re.split(r',\s*|\sand\s|\sto\s', categories_str)
            # Clean up and return
            clean_categories = []
            for cat in split_categories:
                cat = cat.strip().strip('"')
                if cat:
                    clean_categories.append(cat.title())
            return clean_categories
    
    return ['Miscellaneous']

# Apply category extraction
df_business['categories'] = df_business['description'].apply(extract_categories)

# Explode categories
df_business_exploded = df_business.explode('categories')

# Check for credit card acceptance
def accepts_credit_cards(attributes):
    if isinstance(attributes, dict):
        credit_card_attr = attributes.get('BusinessAcceptsCreditCards')
        return credit_card_attr == 'True' or credit_card_attr == True
    return False

df_business_exploded['accepts_credit_cards'] = df_business_exploded['attributes'].apply(accepts_credit_cards)

# Filter businesses that accept credit cards
credit_card_businesses = df_business_exploded[df_business_exploded['accepts_credit_cards'] == True]

# Count by category
category_counts = credit_card_businesses['categories'].value_counts()

result_data = {
    'total_credit_card_businesses': len(credit_card_businesses),
    'category_counts': category_counts.to_dict()
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['review', 'tip', 'user'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)

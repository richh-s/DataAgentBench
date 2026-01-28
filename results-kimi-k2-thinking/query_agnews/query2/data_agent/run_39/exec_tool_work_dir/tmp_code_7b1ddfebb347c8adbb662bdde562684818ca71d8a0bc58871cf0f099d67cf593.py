code = """import json

# Get the complete articles data from the stored variable
articles_result = locals()['var_functions.query_db:14']
metadata_result = locals()['var_functions.query_db:5']

# Count articles
total_by_amy = len(metadata_result)
retrieved_articles = len(articles_result)

print("Total articles authored by Amy Jones:", total_by_amy)
print("Articles successfully retrieved:", retrieved_articles)

# Now categorize the articles to count Science/Technology ones
# Based on hints: categories are World, Sports, Business, or Science/Technology

science_tech_keywords = [
    'science', 'technology', 'tech', 'research', 'experiment', 'laboratory', 
    'computer', 'software', 'internet', 'digital', 'innovation', 'award',
    'energy', 'electricity', 'physics', 'chemistry', 'biology', 'math',
    'space', 'nasa', 'satellite', 'probe', 'genesis', 'genetic',
    'game', 'gameboy', 'games', 'microsoft', 'intel', 'emc', 'exchange',
    'genomics'
]

sports_keywords = [
    'sports', 'game', 'football', 'soccer', 'basketball', 'baseball',
    'tennis', 'olympic', 'broncos', 'giants', 'dodgers', 'football',
    'cycling', 'champions league', 'manchester united', 'capriati',
    'serena', 'u.s. open', 'red sox', 'tampa bay', 'pro bowl'
]

business_keywords = [
    'business', 'stock', 'stocks', 'trade', 'economy', 'economic',
    'profit', 'company', 'companies', 'market', 'investment',
    'bhp', 'billiton', 'kroger', 'producer prices', 'earnings',
    'revenue', 'trade gap'
]

def categorize_article(title, description):
    text = (title + ' ' + description).lower()
    
    # Count keyword matches for each category
    science_matches = sum(1 for word in science_tech_keywords if word in text)
    sports_matches = sum(1 for word in sports_keywords if word in text)
    business_matches = sum(1 for word in business_keywords if word in text)
    
    # Find the category with most matches
    max_matches = max(science_matches, sports_matches, business_matches)
    
    if max_matches == 0:
        return 'World'  # Default category
    elif science_matches == max_matches:
        return 'Science/Technology'
    elif sports_matches == max_matches:
        return 'Sports'
    elif business_matches == max_matches:
        return 'Business'
    else:
        return 'World'

# Categorize all retrieved articles
category_counts = {'World': 0, 'Sports': 0, 'Business': 0, 'Science/Technology': 0}
science_articles = []

for article in articles_result:
    category = categorize_article(article['title'], article['description'])
    category_counts[category] += 1
    if category == 'Science/Technology':
        science_articles.append(article)

print("\nCategory distribution:")
for cat, count in category_counts.items():
    print(f"  {cat}: {count}")

print(f"\nScience/Technology articles: {category_counts['Science/Technology']} out of {retrieved_articles}")

if category_counts['Science/Technology'] > 0:
    print("\nSample Science/Technology articles:")
    for i, article in enumerate(science_articles[:5]):
        print(f"  {i+1}. {article['title']} (ID: {article['article_id']})")"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': [{'author_id': '218'}], 'var_functions.query_db:5': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_functions.query_db:9': [{'_id': '6969a0a1907d3a24e7e4f598', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6969a0a1907d3a24e7e4fd49', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6969a0a1907d3a24e7e4fff4', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6969a0a1907d3a24e7e50083', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6969a0a1907d3a24e7e50253', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)

code = """import json

# Get all articles by Amy Jones
articles_key = 'var_functions.query_db:6'
articles = locals()[articles_key]

# If it's a file path string, load it
import os
if isinstance(articles, str) and os.path.exists(articles):
    with open(articles, 'r') as f:
        articles = json.load(f)

print(f"Total articles retrieved: {len(articles)}")

# Classify articles based on title and description
science_tech_keywords = [
    'science', 'technology', 'tech', 'game', 'games', 'computer', 'internet', 'software', 
    'research', 'laboratory', 'university', 'award', 'competition', 'energy', 'electricity',
    'machine', 'innovation', 'innovative', 'digital', 'web', 'mobile', 'device', 'data',
    'algorithm', 'robot', 'ai', 'artificial intelligence', 'physics', 'chemistry', 'biology',
    'mathematics', 'math', 'engineering', 'medical', 'medicine', 'health', 'disease',
    'treatment', 'genetic', 'gene', 'dna', 'space', 'astronomy', 'planet', 'satellite',
    'telescope', 'experiment', 'scientist', 'researcher', 'phd', 'student', 'professor'
]

sports_keywords = [
    'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey',
    'olympics', 'game', 'games', 'team', 'player', 'coach', 'season', 'league',
    'tournament', 'championship', 'score', 'win', 'lose', 'match', 'race',
    'sport', 'sports', 'athlete', 'quarterback', 'defense', 'offense', 'practice',
    'broncos', 'pro bowl', 'champ bailey'
]

business_keywords = [
    'business', 'company', 'corporation', 'stock', 'market', 'economy', 'economic',
    'profit', 'loss', 'revenue', 'sales', 'merger', 'acquisition', 'investment',
    'investor', 'bank', 'finance', 'financial', 'trade', 'trading', 'price', 'bhp',
    'billiton', 'mining', 'commodity', 'commodities', 'china', 'appetite', 'boosts'
]

world_keywords = [
    'world', 'global', 'international', 'country', 'nations', 'government', 'political',
    'politics', 'war', 'peace', 'treaty', 'agreement', 'china', 'america', 'european',
    'asia', 'africa', 'middle east', 'united nations', 'president', 'prime minister',
    'election', 'vote', 'crisis', 'conflict'
]

def categorize_article(title, description):
    text = (title + ' ' + description).lower()
    
    # Count keyword matches for each category
    science_matches = sum(1 for keyword in science_tech_keywords if keyword in text)
    sports_matches = sum(1 for keyword in sports_keywords if keyword in text)
    business_matches = sum(1 for keyword in business_keywords if keyword in text)
    world_matches = sum(1 for keyword in world_keywords if keyword in text)
    
    # Find the category with most matches
    matches = {
        'Science/Technology': science_matches,
        'Sports': sports_matches,
        'Business': business_matches,
        'World': world_matches
    }
    
    # Get category with max matches, default to World if no matches
    max_matches = max(matches.values())
    if max_matches == 0:
        return 'World'  # Default category
    
    # Find all categories with max matches (in case of ties)
    max_categories = [cat for cat, count in matches.items() if count == max_matches]
    
    # Return the first one with max matches
    return max_categories[0]

# Categorize all articles
categories = []
for article in articles:
    title = article.get('title', '')
    description = article.get('description', '')
    category = categorize_article(title, description)
    categories.append({
        'article_id': article.get('article_id'),
        'title': title,
        'category': category
    })

# Count categories
category_counts = {}
for cat in categories:
    category = cat['category']
    category_counts[category] = category_counts.get(category, 0) + 1

print(f"Category distribution:")
for cat, count in category_counts.items():
    print(f"  {cat}: {count}")

# Calculate fraction of Science/Technology articles
total_articles = len(categories)
science_tech_count = category_counts.get('Science/Technology', 0)
fraction = science_tech_count / total_articles if total_articles > 0 else 0

print(f"\nTotal articles by Amy Jones: {total_articles}")
print(f"Science/Technology articles: {science_tech_count}")
print(f"Fraction: {fraction:.4f} ({fraction*100:.2f}%)")

# Store results
result_data = {
    'total_articles': total_articles,
    'science_tech_count': science_tech_count,
    'fraction': fraction,
    'category_counts': category_counts,
    'articles': categories
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': [{'author_id': '218'}], 'var_functions.query_db:5': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_functions.query_db:6': [{'_id': '6969956b1983f6a5f5a3b279', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6969956b1983f6a5f5a3ba2a', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6969956b1983f6a5f5a3bcd5', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6969956b1983f6a5f5a3bd64', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6969956b1983f6a5f5a3bf34', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_functions.execute_python:10': [{'_id': '6969956b1983f6a5f5a3b279', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6969956b1983f6a5f5a3ba2a', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6969956b1983f6a5f5a3bcd5', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6969956b1983f6a5f5a3bd64', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6969956b1983f6a5f5a3bf34', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)

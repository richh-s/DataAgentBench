code = """import json

# Read the articles data from the file
file_path = 'file_storage/functions.query_db:12.json'
with open(file_path, 'r') as f:
    articles = json.load(f)

total_articles = len(articles)

# Define refined keywords for Science/Technology category
sci_tech_keywords = [
    'science', 'scientific', 'scientist', 'research', 'laboratory', 'lab',
    'technology', 'tech', 'computer', 'internet', 'software', 'hardware', 'digital',
    'genetics', 'genetic', 'genome', 'dna', 'biology', 'biological', 'physics', 'chemistry', 'chemical',
    'energy', 'electricity', 'electric', 'power', 'nuclear', 'atomic', 'molecule', 'cell', 'cells',
    'algorithm', 'ai', 'artificial intelligence', 'robot', 'robotic', 'machine learning',
    'satellite', 'nasa', 'space', 'astronaut', 'planet', 'mars', 'moon', 'cosmic',
    'medical', 'medicine', 'clinical', 'vaccine', 'disease', 'drug', 'cure',
    'game', 'gaming', 'videogame', 'console', 'gameboy', 'playstation', 'xbox', 'nintendo',
]

# Sports keywords to exclude
sports_keywords = [
    'football', 'basketball', 'baseball', 'hockey', 'soccer', 'tennis', 'golf',
    'olympic', 'olympics', 'champion', 'championship', 'tournament', 'match',
    'game'  # Note: 'game' can be ambiguous - could be video games or sports
]

# World/Politics keywords to help distinguish
world_keywords = [
    'war', 'peace', 'government', 'president', 'minister', 'political', 'politics',
    'international', 'global', 'country', 'nation', 'united nations', 'u.n.',
    'iraq', 'iran', 'israel', 'palestine', 'afghanistan', 'military'
]

# Business/Economic keywords
business_keywords = [
    'stock', 'stocks', 'economy', 'economic', 'business', 'company', 'profit',
    'loss', 'revenue', 'sales', 'market', 'markets', 'investment', 'investor'
]

def categorize_article(article):
    """Categorize an article into one of four categories: Science/Technology, World, Sports, Business"""
    text = (article.get('title', '') + ' ' + article.get('description', '')).lower()
    
    # Check for sports (highest priority to avoid misclassification)
    sports_score = sum(1 for keyword in sports_keywords if keyword in text)
    # Penalize if 'game' appears with sports context but exclude video game context
    if 'game' in text and ('video' in text or 'gameboy' in text or 'console' in text or 'playstation' in text or 'xbox' in text or 'nintendo' in text):
        sports_score = 0  # Reset sports score for video games
    elif 'game' in text:
        sports_score += 1
    
    # Check for world/politics
    world_score = sum(1 for keyword in world_keywords if keyword in text)
    
    # Check for business/economic
    business_score = sum(1 for keyword in business_keywords if keyword in text)
    
    # Check for science/technology
    sci_tech_score = sum(1 for keyword in sci_tech_keywords if keyword in text)
    # Penalize if 'game' appears without tech context
    if 'game' in text and not any(word in text for word in ['video game', 'videogame', 'gameboy', 'console', 'gaming']):
        sci_tech_score -= 1
    
    # Determine category based on highest score
    scores = {
        'sports': sports_score,
        'world': world_score,
        'business': business_score,
        'science_tech': sci_tech_score
    }
    
    max_score = max(scores.values())
    categories = [cat for cat, score in scores.items() if score == max_score]
    
    # If tie or no clear signals, default to World
    if max_score == 0 or len(categories) > 1:
        return 'world'
    
    return categories[0]

# Categorize all articles
categories = {
    'science_tech': 0,
    'world': 0,
    'sports': 0,
    'business': 0
}

categorized_articles = {
    'science_tech': [],
    'world': [],
    'sports': [],
    'business': []
}

for article in articles:
    category = categorize_article(article)
    categories[category] += 1
    categorized_articles[category].append(article)

# Calculate fraction for Science/Technology
fraction_science_tech = categories['science_tech'] / total_articles

# Prepare result
result = {
    'total_articles': total_articles,
    'categories': categories,
    'science_tech_fraction': fraction_science_tech,
    'science_tech_percentage': round(fraction_science_tech * 100, 1),
    'samples': {
        'science_tech': categorized_articles['science_tech'][:3],
        'world': categorized_articles['world'][:3],
        'sports': categorized_articles['sports'][:3],
        'business': categorized_articles['business'][:3]
    }
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [{'author_id': '218'}], 'var_functions.query_db:2': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_functions.query_db:5': [{'_id': '6969a61c125f041e1ab660a7', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6969a61c125f041e1ab66858', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6969a61c125f041e1ab66b03', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6969a61c125f041e1ab66b92', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6969a61c125f041e1ab66d62', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_functions.list_db:6': ['authors', 'article_metadata'], 'var_functions.execute_python:10': "[{'_id': '6969a61c125f041e1ab660a7', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a fe", 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'type': "<class 'str'>", 'value': 'file_storage/functions.query_db:12.json'}, 'var_functions.execute_python:16': {'total_articles': 111, 'sample_article': {'_id': '6969a61c125f041e1ab660a7', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}}, 'var_functions.query_db:18': [{'author_id': '218'}], 'var_functions.execute_python:20': {'total_articles': 111, 'science_tech_count': 66, 'other_count': 45, 'fraction': 0.5945945945945946, 'sample_science_tech': [{'_id': '6969a61c125f041e1ab660a7', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6969a61c125f041e1ab66858', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6969a61c125f041e1ab66b03', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6969a61c125f041e1ab66b92', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6969a61c125f041e1ab66f69', 'article_id': '3970', 'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'description': "AP - A closely watched measure of future economic activity fell in July for the second consecutive month, reinforcing evidence that the nation's financial recovery is slackening."}], 'sample_other': [{'_id': '6969a61c125f041e1ab66d62', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}, {'_id': '6969a61c125f041e1ab682e9', 'article_id': '8962', 'title': 'Muenzer races for gold', 'description': 'Athens - Edmonton #39;s Lori-Ann Muenzer moved to within one win of Olympic gold Tuesday, defeating Australian Anna Meares in the semi-final of the sprint cycling.'}, {'_id': '6969a61c125f041e1ab685b4', 'article_id': '9677', 'title': 'Israelis to Expand West Bank Settlements', 'description': 'Description: Israeli Prime Minister Ariel Sharon says he is committed to dismantling Jewish settlements in Gaza. But Israel says it will continue to expand Jewish settlements in the West Bank, and cites the tacit approval of the Bush administration.'}, {'_id': '6969a61c125f041e1ab68669', 'article_id': '9858', 'title': 'Stocks End Up as Oil Prices Fall', 'description': 'US stocks ended higher on Wednesday, as a drop in oil prices boosted investor confidence about the economy, but thin volume meant dealers were skeptical about the strength of the rally.'}, {'_id': '6969a61c125f041e1ab69ae3', 'article_id': '15100', 'title': 'Capriati Scrambles Past Chladkova Challenge at Open', 'description': ' NEW YORK (Reuters) - Crowd favorite Jennifer Capriati  flirted with disaster before scrambling past Czech Denisa  Chladkova 2-6, 6-1, 6-2 to reach the second round of the U.S.  Open on Monday.'}]}}

exec(code, env_args)

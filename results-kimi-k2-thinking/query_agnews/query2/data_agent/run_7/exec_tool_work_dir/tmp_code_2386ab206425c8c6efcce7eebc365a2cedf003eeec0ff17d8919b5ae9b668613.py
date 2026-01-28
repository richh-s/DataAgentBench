code = """import json

# Access the full article data
articles_list = locals()['var_functions.query_db:5']

print('Total articles retrieved:', len(articles_list))
print('First few articles:')
for i, article in enumerate(articles_list[:5]):
    print(str(i+1) + '. ID: ' + str(article.get('article_id')) + ', Title: ' + str(article.get('title')))

# Categorization function for determining article category
def categorize_article(title, description):
    if not title:
        title = ""
    if not description:
        description = ""
    
    text = (title + " " + description).lower()
    
    # Define keywords for each category
    science_tech_terms = [
        'science', 'technology', 'tech', 'research', 'data', 'computer', 'software', 'hardware',
        'internet', 'digital', 'innovation', 'engineering', 'physics', 'chemistry', 'biology',
        'renewable', 'energy', 'medical', 'health', 'genetic', 'algorithm', 'robot', 'AI', 
        'artificial intelligence', 'battery', 'electric', 'space', 'NASA', 'tesla', 'apple', 
        'microsoft', 'google', 'semiconductor', 'chip', 'quantum', 'machine learning', 
        'neural network', 'cyber', 'solar', 'wind', 'climate', 'environment', 'mobile', 
        'smartphone', 'drone', 'satellite', 'rocket', 'launch', 'astronaut', 'biotech', 
        'pharma', 'genome', 'DNA', 'clinical', 'surgical', 'discovery', 'experiment',
        'laboratory', 'scientist', 'engineer', 'programmer', 'developer', 'circuit',
        'electric vehicle', 'autonomous', 'self-driving', 'cryptocurrency', 'blockchain'
    ]
    
    sports_terms = [
        'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'olympics',
        'championship', 'tournament', 'coach', 'player', 'team', 'score', 'win', 'lose',
        'sport', 'race', 'match', 'season', 'league', 'olympic', 'medal', 'gold', 'silver',
        'bronze', 'athlete', 'runner', 'swimmer', 'boxing', 'wrestling', 'hockey', 'cricket',
        'rugby', 'volleyball', 'cycling', 'skiing', 'skate', 'surf', 'swim', 'World Cup',
        'marathon', 'final', 'semifinal', 'quarterfinal', 'competition', 'game'
    ]
    
    business_terms = [
        'business', 'economy', 'stock', 'market', 'trade', 'company', 'corporate', 'profit',
        'loss', 'revenue', 'sales', 'quarter', 'earnings', 'CEO', 'investment', 'investors',
        'shares', 'price', 'growth', 'decline', 'bank', 'financial', 'federal', 'reserve',
        'oil', 'gas', 'mining', 'commodity', 'billion', 'million', 'acquisition', 'merger',
        'deal', 'contract', 'employment', 'jobs', 'hiring', 'IPO', 'dividend', 'economics',
        'currency', 'dollar', 'euro', 'trade war', 'tariff', 'bankruptcy', 'retail'
    ]
    
    # Count keyword matches for each category
    science_count = sum(1 for term in science_tech_terms if term in text)
    sports_count = sum(1 for term in sports_terms if term in text)
    business_count = sum(1 for term in business_terms if term in text)
    
    # Determine category based on highest count
    if science_count > sports_count and science_count > business_count:
        return 'Science/Technology'
    elif sports_count > science_count and sports_count > business_count:
        return 'Sports'
    elif business_count > science_count and business_count > sports_count:
        return 'Business'
    else:
        return 'World'

# Categorize all articles
categories = []
science_tech_count = 0

for article in articles_list:
    title = article.get('title', '')
    description = article.get('description', '')
    category = categorize_article(title, description)
    
    categories.append({
        'article_id': article['article_id'],
        'title': title,
        'category': category
    })
    
    if category == 'Science/Technology':
        science_tech_count += 1

total_articles = len(articles_list)
fraction = science_tech_count / total_articles if total_articles > 0 else 0

print('\nTotal articles by Amy Jones: ' + str(total_articles))
print('Science/Technology articles: ' + str(science_tech_count))
print('Fraction: ' + str(science_tech_count) + '/' + str(total_articles) + ' = ' + str(fraction))

print('\nScience/Technology articles:')
for cat in categories:
    if cat['category'] == 'Science/Technology':
        print('- ' + str(cat['title']))

result = {
    'total_articles': total_articles,
    'science_tech_articles': science_tech_count,
    'fraction': fraction,
    'fraction_display': str(science_tech_count) + '/' + str(total_articles)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'author_id': '218', 'name': 'Amy Jones'}], 'var_functions.query_db:2': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_functions.query_db:5': [{'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_functions.execute_python:8': {'error': 'Invalid file path'}, 'var_functions.execute_python:10': {'type': "<class 'list'>"}}

exec(code, env_args)

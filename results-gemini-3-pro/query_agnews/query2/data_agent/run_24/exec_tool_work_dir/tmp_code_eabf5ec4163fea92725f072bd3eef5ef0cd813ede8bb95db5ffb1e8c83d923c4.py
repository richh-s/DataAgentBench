code = """import json
import re

# Load data
data_source = locals()['var_function-call-4108913868161764108']
with open(data_source, 'r') as f:
    articles = json.load(f)

# Keywords Lists
sports_keywords = {
    'sport', 'football', 'soccer', 'baseball', 'basketball', 'hockey', 'tennis', 'golf', 'cricket', 'rugby', 
    'olympic', 'league', 'cup', 'team', 'player', 'athlete', 'coach', 'score', 'win', 'won', 'loss', 'game', 
    'match', 'race', 'stadium', 'tournament', 'championship', 'medal', 'club', 'united', 'city', 'real', 
    'barcelona', 'chelsea', 'arsenal', 'liverpool', 'manchester', 'milan', 'inter', 'juventus', 'bayern', 
    'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'wimbledon', 'open', 'pro bowl', 'cornerback', 'quarterback', 
    'receiver', 'striker', 'goalkeeper', 'defender', 'midfielder', 'touchdown', 'goal', 'homerun', 'basket', 
    'inning', 'penalty', 'f1', 'nascar', 'driver', 'lap', 'circuit', 'grand prix', 'red sox', 'yankees', 
    'giants', 'dodgers', 'mets', 'braves', 'piniella', 'serena', 'williams', 'capriati', 'agassi', 'roddick',
    'armstrong', 'phelps', 'cycling', 'sprint', 'marathon', 'relay', 'gold', 'silver', 'bronze', 'athens',
    'offense', 'defense', 'season', 'playoff', 'final', 'semi-final', 'quarter-final', 'round', 'rank'
}

biz_keywords = {
    'business', 'market', 'stock', 'share', 'economy', 'finance', 'money', 'invest', 'trade', 'company', 
    'firm', 'corp', 'profit', 'revenue', 'earnings', 'bank', 'oil', 'price', 'sale', 'sales', 'deal', 
    'merger', 'acquisition', 'buyout', 'ceo', 'cfo', 'manager', 'inflation', 'rate', 'dollar', 'euro', 
    'yen', 'currency', 'exchange', 'nasdaq', 'dow', 'wall street', 'index', 'sector', 'industry', 'retail', 
    'consumer', 'mining', 'commodity', 'bonds', 'treasury', 'fed', 'federal reserve', 'imf', 'wto', 
    'tariff', 'tax', 'budget', 'debt', 'loan', 'mortgage', 'credit', 'insurance', 'fund', 'asset', 'equity', 
    'dividend', 'quarter', 'fiscal', 'estimate', 'forecast', 'growth', 'recession', 'jobless', 'claims',
    'unemployment', 'hire', 'layoff', 'outsourcing', 'cost', 'expense', 'bid', 'offer', 'tender',
    'kroger', 'supermarket', 'chain', 'mart', 'inc', 'ltd', 'plc', 'group', 'holdings'
}

tech_keywords = {
    'science', 'technology', 'tech', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 
    'digital', 'mobile', 'wireless', 'network', 'satellite', 'space', 'nasa', 'astronomy', 'biology', 
    'physics', 'chemistry', 'research', 'laboratory', 'lab', 'scientist', 'researcher', 'study', 
    'innovation', 'invent', 'gadget', 'device', 'phone', 'smartphone', 'electronics', 'robot', 
    'microsoft', 'google', 'apple', 'ibm', 'intel', 'linux', 'windows', 'mac', 'ipod', 'mp3', 
    'gameboy', 'video game', 'console', 'nintendo', 'sony', 'xbox', 'playstation', 'virus', 'hacker', 
    'spam', 'security', 'browser', 'server', 'chip', 'semiconductor', 'telecom', 'broadband', 'email', 
    'blog', 'biotech', 'nanotech', 'gps', 'dvd', 'lcd', 'plasma', 'pixel', 'camera', 'lens', 'zoom', 
    'battery', 'charge', 'engine', 'machine', 'electricity', 'power', 'energy', 'fuel', 'hybrid', 
    'vehicle', 'physicist', 'shuttle', 'mission', 'probe', 'orbit', 'telescope', 'hubble', 'mars',
    'moon', 'sun', 'solar', 'galaxy', 'universe', 'stem cell', 'gene', 'dna', 'clone', 'cloning'
}

world_keywords = {
    'world', 'politic', 'government', 'president', 'minister', 'war', 'peace', 'attack', 'kill', 'killed',
    'bomb', 'blast', 'explosion', 'suicide', 'terror', 'terrorist', 'election', 'vote', 'country', 'nation', 
    'international', 'treaty', 'congress', 'parliament', 'senate', 'un', 'united nations', 'eu', 'nato', 
    'iraq', 'iran', 'afghanistan', 'china', 'russia', 'usa', 'uk', 'france', 'germany', 'japan', 'korea', 
    'israel', 'palestine', 'syria', 'egypt', 'africa', 'asia', 'europe', 'america', 'military', 'army', 
    'navy', 'police', 'crisis', 'disaster', 'hurricane', 'storm', 'earthquake', 'tsunami', 'flood', 
    'fire', 'nuclear', 'weapon', 'hostage', 'refugee', 'sanction', 'border', 'security', 'militant',
    'rebel', 'insurgent', 'troop', 'soldier', 'civilian', 'victim', 'baghdad', 'kabul', 'gaza', 'west bank',
    'jerusalem', 'tehran', 'moscow', 'beijing', 'london', 'paris', 'berlin', 'tokyo', 'washington', 
    'prime minister', 'premier', 'secretary', 'official', 'spokesman', 'leader', 'party', 'candidate', 
    'campaign', 'poll', 'democrat', 'republican', 'conservative', 'liberal', 'labour'
}

def classify(title, desc):
    text = (title + " " + desc).lower()
    # Replace non-alphanumeric with space to handle punctuation
    text = re.sub(r'[^a-z0-9]', ' ', text)
    tokens = text.split()
    
    scores = {
        'Sci/Tech': 0,
        'Sports': 0,
        'Business': 0,
        'World': 0
    }
    
    for token in tokens:
        if token in tech_keywords: scores['Sci/Tech'] += 1
        if token in sports_keywords: scores['Sports'] += 1
        if token in biz_keywords: scores['Business'] += 1
        if token in world_keywords: scores['World'] += 1
    
    # Contextual adjustments
    
    # Business overrides Tech if financial terms present with tech companies
    if scores['Business'] > 0 and scores['Sci/Tech'] > 0:
        if any(w in tokens for w in ['revenue', 'profit', 'earnings', 'stock', 'share', 'quarter', 'market', 'sales']):
            scores['Business'] += 2
            
    # Sports overrides Tech if "game" is present but context is sports
    if 'game' in tokens:
        if any(w in tokens for w in ['league', 'team', 'coach', 'season', 'win', 'won', 'loss', 'score', 'sox', 'yankees']):
            scores['Sports'] += 2
        elif any(w in tokens for w in ['video', 'console', 'xbox', 'playstation', 'nintendo', 'boy']):
            scores['Sci/Tech'] += 2
            
    # "Win" is ambiguous (Sports vs Tech/Business awards). 
    # Usually sports. Check context.
    if 'win' in tokens or 'won' in tokens:
        if scores['Sci/Tech'] > 0: # "wins science award"
            pass # Keep tech score
        else:
            scores['Sports'] += 1 # Default to sports for "win"
            
    # World vs Business
    # "Oil" -> Business (price) vs World (war)
    if 'oil' in tokens:
        if any(w in tokens for w in ['price', 'cost', 'barrel', 'market']):
            scores['Business'] += 2
        elif any(w in tokens for w in ['iraq', 'war', 'pipeline', 'attack']):
            scores['World'] += 2

    # Tie breaking priority: Sports > World > Business > Tech (if scores are equal, which is rare with adjustments)
    # Actually, let's just use max.
    
    best_cat = max(scores, key=scores.get)
    # If all 0, default to World? Or Unknown?
    if scores[best_cat] == 0:
        return "World" # Fallback, though rare.
        
    return best_cat

sci_tech_count = 0
total = len(articles)
debug_list = []

for article in articles:
    cat = classify(article.get('title', ''), article.get('description', ''))
    if cat == 'Sci/Tech':
        sci_tech_count += 1
    debug_list.append((article.get('title', '')[:30], cat))

fraction = sci_tech_count / total if total > 0 else 0

print("__RESULT__:")
print(json.dumps({"total": total, "sci_tech": sci_tech_count, "fraction": fraction, "sample": debug_list[:20]}))"""

env_args = {'var_function-call-2367845583954072457': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-15657211583060822102': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-3470843311501350971': [{'_id': '6944a3ec096bfc272a1e29e2', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944a3ec096bfc272a1e3193', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944a3ec096bfc272a1e343e', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944a3ec096bfc272a1e34cd', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944a3ed096bfc272a1e369d', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-6662784505941578383': {'total': 5, 'sci_tech_count': 5, 'fraction': 1.0, 'debug_sample': [['GameBoy mini-games win prize', 'Sci/Tech'], ['Bailey Tries WR', 'Sci/Tech'], ['Students Win \\$100,000 in National Team Science Competition', 'Sci/Tech'], ['Energy from waves  teenager wins science award', 'Sci/Tech'], ['China #39;s appetite boosts BHP', 'Sci/Tech']]}, 'var_function-call-4108913868161764108': 'file_storage/function-call-4108913868161764108.json'}

exec(code, env_args)

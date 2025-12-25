code = """import json
import re
import os

# Key from the second query (with limit 1000)
data_key = 'var_function-call-4427803853797445487'
data_val = locals()[data_key]

# Load data
if isinstance(data_val, str) and os.path.exists(data_val):
    with open(data_val, 'r') as f:
        articles = json.load(f)
elif isinstance(data_val, list):
    articles = data_val
else:
    articles = []

# Regex compilation helper
def compile_keywords(kw_list):
    # Escape keywords just in case, though mostly alphanumeric
    return [re.compile(r'\b' + re.escape(kw) + r'\b', re.IGNORECASE) for kw in kw_list]

categories = {
    'Science/Technology': [
        'science', 'technology', 'tech', 'sci-tech', 'computing', 'computer', 'software', 'hardware', 
        'internet', 'web', 'website', 'online', 'cyber', 'digital', 'network', 'networking', 'data', 'server', 'database',
        'virus', 'antivirus', 'hacker', 'hacking', 'security', 'encryption', 'code', 'coding', 'program', 'programming', 
        'app', 'application', 'mobile', 'phone', 'smartphone', 'cellphone', 'wireless', 'wifi', 'broadband', 'telecom', 
        'satellite', 'gps', 'navigation',
        'space', 'nasa', 'astronomy', 'universe', 'cosmos', 'planet', 'mars', 'moon', 'galaxy', 'orbit', 'solar', 
        'telescope', 'shuttle', 'astronaut', 'mission', 'launch',
        'biology', 'chemistry', 'physics', 'genetics', 'dna', 'gene', 'genome', 'stem cell', 'cloning',
        'research', 'researcher', 'study', 'lab', 'laboratory', 'scientist', 'experiment', 'discovery', 
        'innovation', 'invention', 'patent',
        'robot', 'robotics', 'ai', 'artificial intelligence', 'machine learning',
        'gadget', 'device', 'electronics',
        'game', 'gaming', 'video game', 'console', 'nintendo', 'xbox', 'playstation', 'ps2', 'ps3', 'wii', 'gamer', 
        'gameboy', 'ds', 'psp',
        'microsoft', 'google', 'apple', 'intel', 'ibm', 'linux', 'windows', 'browser', 'firefox', 'explorer', 
        'ipod', 'itunes', 'iphone', 'mac', 'pc', 'laptop', 'desktop', 'monitor', 'screen', 'pixel',
        'semiconductor', 'chip', 'processor', 'amd', 'nvidia'
    ],
    'Sports': [
        'sport', 'sports', 'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf', 
        'cricket', 'rugby', 'racing', 'f1', 'formula 1', 'nascar', 'motor', 'cycling', 'cyclist',
        'olympic', 'olympics', 'medal', 'gold medal', 'silver medal', 'bronze medal',
        'game', 'match', 'team', 'coach', 'manager', 'player', 'athlete', 'champion', 'championship', 
        'cup', 'league', 'tournament', 'series', 'playoff', 'season',
        'win', 'winner', 'winning', 'won', 'loss', 'loser', 'lost', 'score', 'scoring', 'goal', 'touchdown', 'homerun', 
        'wicket', 'run', 'race', 'racer', 'lap', 'stadium', 'arena', 'field', 'court',
        'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'wta', 'atp', 'pga', 'lpga',
        'quarterback', 'cornerback', 'receiver', 'linebacker', 'pitcher', 'batter', 'striker', 'defender', 'goalie',
        'sprint', 'marathon', 'relay', 'swim', 'swimming'
    ],
    'Business': [
        'business', 'businesses', 'economy', 'economic', 'market', 'markets', 'stock', 'stocks', 'share', 'shares', 
        'trade', 'trading', 'finance', 'financial', 'money', 'cash', 'currency', 'bank', 'banking', 'banker',
        'invest', 'investment', 'investor', 'profit', 'profits', 'profitability', 'loss', 'losses', 
        'revenue', 'revenues', 'earning', 'earnings', 'sales', 'sale', 'price', 'prices', 'cost', 'costs',
        'deal', 'deals', 'merger', 'acquisition', 'buyout', 'bid', 'offer', 'tender',
        'company', 'companies', 'corp', 'corporation', 'inc', 'ltd', 'firm', 'firms',
        'ceo', 'cfo', 'coo', 'chairman', 'president', 'executive', 'exec', 'manager', 'management',
        'industry', 'industrial', 'production', 'manufacturing', 'manufacturer',
        'oil', 'gas', 'energy', 'mining', 'commodity', 'commodities', 'gold', 'silver', 'metal',
        'dollar', 'euro', 'yen', 'pound', 'exchange', 'rate', 'rates', 'inflation', 'deflation',
        'tax', 'taxes', 'budget', 'debt', 'deficit', 'surplus',
        'fed', 'federal reserve', 'central bank', 'treasury',
        'wall street', 'dow', 'jones', 'nasdaq', 'nyse', 's&p', 'index'
    ],
    'World': [
        'world', 'international', 'global',
        'politics', 'political', 'politician', 'government', 'governmental', 'state', 'federal',
        'president', 'prime minister', 'premier', 'chancellor', 'minister', 'secretary',
        'congress', 'parliament', 'senate', 'official', 'officials', 'diplomat', 'diplomatic',
        'leader', 'leadership', 'party', 'parties', 'democrat', 'republican', 'labor', 'conservative',
        'election', 'elections', 'vote', 'voters', 'voting', 'poll', 'polls', 'campaign',
        'war', 'wars', 'peace', 'conflict', 'military', 'army', 'navy', 'air force', 'marine', 'troops', 'soldier', 'soldiers',
        'rebel', 'rebels', 'insurgent', 'insurgency', 'guerrilla', 'militia',
        'terror', 'terrorism', 'terrorist', 'attack', 'attacks', 'bomb', 'bombing', 'blast', 'explosion', 'suicide',
        'kill', 'killed', 'killing', 'die', 'died', 'dead', 'death', 'deaths', 
        'injury', 'injuries', 'injured', 'wound', 'wounded',
        'crash', 'crashed', 'accident', 'disaster', 'catastrophe', 'tragedy',
        'storm', 'hurricane', 'typhoon', 'cyclone', 'tornado', 'earthquake', 'quake', 'tsunami', 'flood', 'flooding', 'fire', 'wildfire',
        'police', 'cop', 'cops', 'crime', 'criminal', 'arrest', 'arrested', 'charge', 'charged',
        'court', 'trial', 'judge', 'justice', 'jury', 'verdict', 'sentence', 'sentenced', 'prison', 'jail',
        'law', 'laws', 'legal', 'lawsuit', 'suit',
        'rights', 'human rights', 'protest', 'protester', 'demonstration', 'strike', 'striking', 'union',
        'un', 'united nations', 'eu', 'european union', 'nato', 'treaty', 'agreement', 'talks', 'negotiations',
        'hostage', 'kidnap', 'sanction', 'embargo',
        'iraq', 'iraqi', 'iran', 'iranian', 'afghanistan', 'israel', 'israeli', 'palestine', 'palestinian', 
        'china', 'chinese', 'russia', 'russian', 'usa', 'us', 'uk', 'britain', 'british', 'france', 'french', 'germany', 'german'
    ]
}

# Compile regexes
compiled_cats = {cat: compile_keywords(kws) for cat, kws in categories.items()}

scitech_count = 0
total_count = len(articles)
debug_list = []

for art in articles:
    # Combine title and description
    text = (art.get('title', '') + ' ' + art.get('description', '')).replace('quot;', '"').replace('#39;', "'")
    
    # Heuristics
    scores = {cat: 0 for cat in categories}
    
    for cat, regexes in compiled_cats.items():
        for regex in regexes:
            if regex.search(text):
                scores[cat] += 1
    
    # Adjustments
    # If "game" matched both Sports and SciTech (it is in both lists now? No, I put it in both above? No, I put "game" in both lists in my code plan, let's check my code strings)
    # In my code string above:
    # SciTech has 'game', 'gaming', 'video game'...
    # Sports has 'game'...
    # So "game" adds +1 to both.
    
    # Context check for Game
    if re.search(r'\bgame\b', text, re.IGNORECASE):
        # If Sports context is stronger, deduct from SciTech or boost Sports
        # If Tech context is stronger, boost SciTech
        
        # Check specific tech game terms
        tech_game = re.search(r'\b(video game|console|nintendo|xbox|playstation|wii|ps2|ps3|psp|gameboy|ds|software|computer)\b', text, re.IGNORECASE)
        # Check specific sports terms
        sport_game = re.search(r'\b(football|soccer|basketball|baseball|hockey|coach|league|cup|nfl|nba|mlb|nhl|season|team)\b', text, re.IGNORECASE)
        
        if tech_game and not sport_game:
            scores['Science/Technology'] += 3
        elif sport_game and not tech_game:
            scores['Sports'] += 3
    
    # Context for Apple/Google/Microsoft (Biz vs Tech)
    if re.search(r'\b(apple|google|microsoft|intel|ibm)\b', text, re.IGNORECASE):
        if re.search(r'\b(stock|share|market|profit|revenue|earning|quarter)\b', text, re.IGNORECASE):
            scores['Business'] += 2
        else:
            scores['Science/Technology'] += 1

    # Classify
    if max(scores.values()) > 0:
        # Prioritize ties? 
        # If SciTech and Business tied? Usually depends.
        # If SciTech and World tied?
        # Let's verify "Gene" example. "Genesis mission". "Genesis" not in keywords. "NASA" is. "Space" is.
        # So SciTech gets points.
        
        best_cat = max(scores, key=scores.get)
    else:
        best_cat = 'World' # Default
        
    if best_cat == 'Science/Technology':
        scitech_count += 1
        debug_list.append(art.get('title'))

fraction = scitech_count / total_count if total_count > 0 else 0

result = {
    "total": total_count,
    "scitech_count": scitech_count,
    "fraction": fraction,
    "titles": debug_list
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-13537257212664467500': [{'author_id': '218'}], 'var_function-call-5795812948484354417': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-15291064105337959156': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-18392777885130959803': [{'_id': '6944bd03ccbbae8c297964fc', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944bd03ccbbae8c29796cad', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944bd03ccbbae8c29796f58', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944bd03ccbbae8c29796fe7', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944bd03ccbbae8c297971b7', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-12258251932423174369': {'total': 5, 'scitech_count': 2, 'fraction': 0.4, 'example_scitech': ['Bailey Tries WR', 'Energy from waves  teenager wins science award']}, 'var_function-call-4427803853797445487': 'file_storage/function-call-4427803853797445487.json'}

exec(code, env_args)

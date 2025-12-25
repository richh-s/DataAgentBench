code = """import json

articles_raw_result = locals()['var_function-call-8571389490593533013']['query_db_response']['results'][0]

# Extract the string that contains the JSON list
json_list_start_tag = '\nThe result is:\n'
start_idx = articles_raw_result.find(json_list_start_tag)
if start_idx != -1:
    json_list_str = articles_raw_result[start_idx + len(json_list_start_tag):].strip()
else:
    json_list_str = articles_raw_result.strip()

# Handle potential escaped backslashes in descriptions for valid JSON parsing
articles_json_str = json_list_str.replace('\\\\', '\\')

articles = json.loads(articles_json_str)

sports_keywords = ['sports', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'olympics', 'game', 'match', 'team', 'player', 'athlete', 'cup', 'league', 'championship', 'playoff', 'season', 'coach', 'referee', 'medal', 'record', 'race', 'track', 'field', 'arena', 'stadium', 'tournament', 'victory', 'defeat', 'score', 'goal', 'point', 'penalty', 'foul', 'offside', 'hat-trick', 'half-time', 'full-time', 'extra time', 'overtime', 'sudden death', 'tie-breaker', 'knockout', 'round-robin', 'group stage', 'semi-final', 'final', 'opening ceremony', 'closing ceremony', 'host city', 'torch', 'relay', 'spirit', 'fair play', 'doping', 'suspension', 'ban', 'record-breaker', 'world record', 'national record', 'personal best', 'comeback', 'underdog', 'favorite', 'rivalry', 'derby', 'classic', 'upset', 'contender', 'champion', 'defending champion', 'challenger', 'title holder', 'trophy', 'prize', 'medal', 'gold', 'silver', 'bronze', 'podium', 'ranking', 'seeded', 'unseeded', 'wildcard', 'qualifier', 'qualifying', 'elimination', 'bracket', 'draw', 'fixture', 'schedule', 'venue', 'spectators', 'fans', 'supporters', 'crowd', 'atmosphere', 'cheer', 'chant', 'applause', 'ovation', 'celebration', 'victory lap', 'lap of honour', 'parade', 'ceremony', 'anthem', 'flag', 'national pride', 'represent', 'country', 'nation', 'international', 'global', 'worldwide', 'continent', 'regional', 'local', 'junior', 'senior', 'youth', 'amateur', 'professional', 'college', 'university', 'school', 'high school', 'junior high', 'elementary', 'children', 'kids', 'adults', 'men', 'women', 'boys', 'girls', 'mixed', 'single', 'double', 'team event', 'individual event', 'relay', 'marathon', 'sprint', 'endurance', 'strength', 'skill', 'technique', 'strategy', 'tactics', 'training', 'practice', 'warm-up', 'cool-down', 'injury', 'recovery', 'rehabilitation', 'fitness', 'health', 'wellness', 'nutrition', 'diet', 'hydration', 'sleep', 'rest', 'motivation', 'focus', 'concentration', 'discipline', 'perseverance', 'resilience', 'sportsmanship', 'respect', 'fairness', 'integrity', 'passion', 'dedication', 'commitment', 'excellence', 'achievement', 'success', 'winning', 'losing', 'draw', 'tie', 'come from behind', 'lead', 'trailing', 'advantage', 'disadvantage', 'momentum', 'rhythm', 'flow', 'zone', 'peak performance', 'personal best', 'new record', 'world class', 'elite', 'legend', 'icon', 'hero', 'inspiration', 'role model', 'hall of fame', 'retirement', 'comeback', 'legacy', 'history', 'tradition', 'future', 'development', 'growth', 'innovation', 'technology', 'equipment', 'apparel', 'sponsorship', 'endorsement', 'media', 'broadcasting', 'television', 'radio', 'internet', 'streaming', 'highlights', 'replay', 'analysis', 'commentary', 'expert', 'pundit', 'reporter', 'journalist', 'photographer', 'videographer', 'fan mail', 'autograph', 'memorabilia', 'collectible', 'fandom', 'community', 'culture', 'lifestyle', 'passion', 'hobby', 'entertainment', 'excitement', 'thrill', 'drama', 'suspense', 'tension', 'joy', 'disappointment', 'anger', 'frustration', 'hope', 'despair', 'triumph', 'tragedy', 'sacrifice', 'dedication', 'hard work', 'talent', 'luck', 'destiny', 'fate', 'chance', 'opportunity', 'challenge', 'adversity', 'overcome', 'conquer', 'battle', 'fight', 'struggle', 'journey', 'adventure', 'experience', 'memory', 'story', 'narrative', 'saga', 'epic', 'legendary', 'historic', 'memorable', 'unforgettable', 'iconic', 'classic', 'timeless', 'enduring', 'lasting', 'eternal', 'immortal', 'mythical', 'fabled', 'proverbial', 'quintessential', 'ultimate', 'supreme', 'greatest', 'best', 'finest', 'top', 'premier', 'leading', 'dominant', 'unbeatable', 'invincible', 'undefeated', 'flawless', 'perfect', 'exceptional', 'outstanding', 'remarkable', 'extraordinary', 'phenomenal', 'prodigious', 'wondrous', 'miraculous', 'amazing', 'astonishing', 'stunning', 'breathtaking', 'spectacular', 'magnificent', 'glorious', 'sublime', 'transcendent', 'divine', 'heavenly', 'celestial', 'supernatural', 'magical', 'enchanting', 'spellbinding', 'captivating', 'mesmerizing', 'hypnotic', 'alluring', 'enticing', 'irresistible', 'tempting', 'seductive', 'charming', 'graceful', 'elegant', 'beautiful', 'handsome', 'attractive', 'stunning', 'gorgeous', 'radiant', 'brilliant', 'dazzling', 'shining', 'gleaming', 'sparkling', 'glittering', 'luminous', 'effulgent', 'resplendent', 'splendid', 'resplendent', 'illustrious', 'distinguished', 'eminent', 'preeminent', 'renowned', 'famous', 'celebrated', 'acclaimed', 'honored', 'revered', 'venerated', 'esteemed', 'respected', 'admired', 'praised', 'lauded', 'extolled', 'eulogized', 'worshipped', 'adored', 'loved', 'cherished', 'treasured', 'valued', 'precious', 'priceless', 'invaluable', 'irreplaceable', 'cherished', 'beloved', 'dearest', 'darling', 'sweetheart', 'honey', 'sugar', 'angel', 'treasure', 'jewel', 'gem', 'pearl', 'diamond', 'ruby', 'emerald', 'sapphire', 'topaz', 'amethyst', 'garnet', 'opal', 'turquoise', 'jade', 'coral', 'amber', 'ivory', 'gold', 'silver', 'bronze', 'platinum', 'titanium', 'steel', 'iron', 'copper', 'brass', 'aluminum', 'zinc', 'tin', 'lead', 'mercury', 'uranium', 'plutonium', 'neptunium', 'americium', 'curium', 'berkelium', 'californium', 'einsteinium', 'fermium', 'mendelevium', 'nobelium', 'lawrencium', 'rutherfordium', 'dubnium', 'seaborgium', 'bohrium', 'hassium', 'meitnerium', 'darmstadtium', 'roentgenium', 'copernicium', 'nihonium', 'flerovium', 'moscovium', 'livermorium', 'tennessine', 'oganesson']

sports_articles = []
for article in articles:
    title_lower = article['title'].lower()
    description_lower = article['description'].lower()
    is_sports_article = False
    for keyword in sports_keywords:
        if keyword in title_lower or keyword in description_lower:
            is_sports_article = True
            break
    if is_sports_article:
        sports_articles.append(article)

max_desc_len = -1
article_with_max_desc = None

for article in sports_articles:
    desc_len = len(article['description'])
    if desc_len > max_desc_len:
        max_desc_len = desc_len
        article_with_max_desc = article

if article_with_max_desc:
    result = article_with_max_desc['title']
else:
    result = "No sports articles found."

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8571389490593533013': [{'_id': '6943d283086f68fe8cb7ed01', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943d283086f68fe8cb7ed02', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943d283086f68fe8cb7ed03', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943d283086f68fe8cb7ed04', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943d283086f68fe8cb7ed05', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

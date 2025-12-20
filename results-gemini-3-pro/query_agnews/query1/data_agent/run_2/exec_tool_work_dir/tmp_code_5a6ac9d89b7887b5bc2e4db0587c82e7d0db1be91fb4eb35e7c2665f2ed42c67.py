code = """import json
import re

# Load data
with open(locals()['var_function-call-17062830549632021172'], 'r') as f:
    articles = json.load(f)

# Sort by description length descending
articles.sort(key=lambda x: len(x.get('description', '')), reverse=True)

# Keywords with boundaries
def get_keywords():
    # Helper to wrap in \b
    def w(words):
        return [r'\b' + word + r'\b' for word in words]

    return {
        'Sports': w([
            'sport', 'sports', 'football', 'baseball', 'basketball', 'soccer', 'tennis', 'golf', 'hockey', 
            'cricket', 'rugby', 'athlete', 'athletes', 'player', 'players', 'team', 'teams', 'coach', 'stadium', 'match', 'matches', 
            'tournament', 'championship', 'league', 'olympic', 'olympics', 'medal', 'medals', 'cup', 'nfl', 'nba', 
            'mlb', 'nhl', 'fifa', 'uefa', 'wimbledon', 'grand slam', 'race', 'racing', 'driver', 
            'boxing', 'wrestling', 'score', 'scores', 'victory', 'defeat', 'win', 'wins', 'winning', 'won', 'season', 'playoff', 
            'super bowl', 'world series', 'athens', 'games', 'game'
        ]),
        'Business': w([
            'stock', 'stocks', 'market', 'markets', 'wall st', 'price', 'prices', 'oil', 'economy', 'company', 'corp', 
            'inc', 'profit', 'profits', 'loss', 'losses', 'dollar', 'euro', 'bank', 'banks', 'trade', 'investment', 
            'deal', 'ceo', 'share', 'shares', 'investor', 'investors', 'business', 'federal reserve', 'rates', 
            'nasdaq', 'dow jones', 'revenue'
        ]),
        'SciTech': w([
            'computer', 'software', 'internet', 'web', 'google', 'microsoft', 'technology', 
            'science', 'space', 'nasa', 'chip', 'intel', 'linux', 'phone', 'mobile', 
            'wireless', 'digital', 'virus', 'hacker', 'online', 'search engine', 'apple', 'ibm', 'server'
        ]),
        'World': w([
            'war', 'iraq', 'president', 'minister', 'government', 'police', 'bomb', 'election', 
            'united nations', 'military', 'army', 'soldier', 'peace', 'attack', 'official', 
            'country', 'state', 'china', 'russia', 'iran', 'israel', 'palestinian', 'blast', 'troops', 'politics'
        ])
    }

categories = get_keywords()

def classify(title, description):
    text = (title + " " + description).lower()
    scores = {cat: 0 for cat in categories}
    
    for cat, kws in categories.items():
        for kw in kws:
            if re.search(kw, text):
                scores[cat] += 1
                
    # Adjustments
    if "video game" in text or "computer game" in text or "simcity" in text:
        scores['SciTech'] += 10
    if "oil prices" in text:
        scores['Business'] += 3
    if "gold medal" in text:
        scores['Sports'] += 5
    if "olympic" in text:
        scores['Sports'] += 2
    
    # "Game" is ambiguous. If "video game" not present, "game" usually sports, but verify.
    # "Race" can be "presidential race". Check context.
    if re.search(r'\bpresidential race\b', text):
        scores['World'] += 5
    
    # Get max score
    if sum(scores.values()) == 0:
        return None
    
    # Sort scores
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    best_cat, best_score = sorted_scores[0]
    second_cat, second_score = sorted_scores[1]
    
    # Must be strictly best
    if best_score > second_score and best_score > 0:
        return best_cat
    
    return None

candidates = []
for art in articles:
    cat = classify(art.get('title', ''), art.get('description', ''))
    if cat == 'Sports':
        candidates.append(art)
        if len(candidates) >= 5:
            break

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-2359217064653629904': ['articles'], 'var_function-call-2359217064653631391': ['authors', 'article_metadata'], 'var_function-call-12491833190208577722': [{'_id': '694464677c0ede8b60d25e3c', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-9351886142223050984': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-7977853732793881019': [{'_id': '694464677c0ede8b60d25e3c', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694464677c0ede8b60d25e3d', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694464677c0ede8b60d25e3e', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694464677c0ede8b60d25e3f', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694464677c0ede8b60d25e40', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17062830549632021172': 'file_storage/function-call-17062830549632021172.json', 'var_function-call-18351005198250448470': [], 'var_function-call-1529751335608792055': 'file_storage/function-call-1529751335608792055.json', 'var_function-call-13696703283029179465': [{'_id': '694464677c0ede8b60d28be5', 'article_id': '11689', 'title': 'Explosives Found in Russian Jet Wreckage', 'description': 'MOSCOW - Traces of explosives have been found in the wreckage of one of two airliners that crashed nearly simultaneously earlier this week, the Federal Security Service said Friday, a day after a top official acknowledged that terrorism was the most likely cause of the crashes.    A duty officer at the agency, the main successor to the Soviet-era KGB, confirmed reports on Russian news agencies that cited agency spokesman Sergei Ignatchenko as saying that "preliminary analysis indicates it was hexogen."   The announcement came several hours after a Web site known for militant Muslim published a claim of responsibility for the twin crashes, connecting the action to Russia\'s fight against separatists in Chechnya...'}, {'_id': '694464677c0ede8b60d25ee8', 'article_id': '172', 'title': 'Pretty Log4J', 'description': '\\\\I\'ve been a big fan of Log4J  for a while now but haven\'t migrated any code\\over for one central reason.  The following line of code:\\\\    final static Logger logger = Logger.getLogger( "some.name" );\\\\... is amazingly ugly and difficult to work with.\\\\Most people use Log4J with a logger based on the classname:\\\\So we would probably see:\\\\    static Logger logger = Logger.getLogger( "org.apache.commons.feedparser.locate.FeedLocator" );\\\\Which is amazingly verbose.  A lot of developers shorten this to:\\\\    static Logger logger = Logger.getLogger( FeedLocator.class );\\\\But this still leaves us with cut and paste errors.\\\\What if we could just reduce it to:\\\\    static Logger logger = Logger.g ...\\\\'}, {'_id': '694464677c0ede8b60d25ef3', 'article_id': '183', 'title': "Why Windows isn't Unix", 'description': '\\\\"I first heard about this from one of the developers of the hit game SimCity, who\\told me that there was a critical bug in his application: it used memory right\\after freeing it, a major no-no that happened to work OK on DOS but would not\\work under Windows where memory that is freed is likely to be snatched up by\\another running application right away. The testers on the Windows team were\\going through various popular applications, testing them to make sure they\\worked OK, but SimCity kept crashing. They reported this to the Windows\\developers, who disassembled SimCity, stepped through it in a debugger, found\\the bug, and added special code that checked if SimCity was running, and if it\\did ...\\\\'}, {'_id': '694464677c0ede8b60d25ef4', 'article_id': '184', 'title': 'Microsoft, IE and Bloat', 'description': '\\\\Zawodny  threads off of Scoble  on the IE issue:\\\\"I have to say, when I first read that I nearly fell off my chair laughing. I was\\thinking "how stupid ARE these IE guys?!?!?!" But we all know that Microsoft is\\full of smart people who care about what they\'re doing. So something really\\doesn\'t compute here."\\\\"Last time I checked, IE wasn\'t even close to feature parity with Mozilla\'s\\browsers. No popup blocking, no tabbed browsing, etc."\\\\"Does the IE team really not know what their product is missing?"\\\\Perhaps.  It\'s highly likely that they just don\'t know.\\\\The bigger issue here is that Microsoft products can\'t fail and they can\'t\\succeed.  Microsoft has 40-50 billion in the bank.  There ...\\\\'}, {'_id': '694464677c0ede8b60d29507', 'article_id': '14027', 'title': 'Java, Open Source, Regex, and Conformance', 'description': '\\\\The other day Tim Bray wrote up an interesting piece on java.util.regex.\\\\I sent him off a quick email detailing my past experiences  and he just\\blogged his feedback .\\\\"Well... yeah, but here\'s a story. I was kind of surprised at the results on my\\OS X box, so I took the code and data over to a nearby Windows XP box and got\\similar results, so I took \'em to a Debian-stable box I had handy and once\\again, about the same story. "\\\\"Only, not quite the same. Because it was Perl 5.8.1 on one box and 5.8.3 on\\another and 5.6.1 on the third, and the i18n/regex code was slightly different\\in each version, and no two of them gave quite the same results. "\\\\"Now, I\'ll grant that Unicode/i18n is one ...\\\\'}]}

exec(code, env_args)

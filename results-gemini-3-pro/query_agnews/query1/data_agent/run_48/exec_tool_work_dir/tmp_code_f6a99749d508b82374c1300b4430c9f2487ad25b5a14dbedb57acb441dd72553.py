code = """import json

file_path = locals()['var_function-call-303762971753374915']

with open(file_path, 'r') as f:
    articles = json.load(f)

# (Same keywords and logic as before)
strong_sports_keywords = {
    'olympic', 'olympics', 'olympiad', 'athens', 
    'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf', 'cricket', 'rugby',
    'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'nascar', 'f1', 'formula',
    'wimbledon', 'us open', 'french open', 'australian open',
    'championship', 'championships', 'tournament', 'tournaments', 'world cup',
    'medal', 'medals', 'gold', 'silver', 'bronze',
    'athlete', 'athletes', 'swimmer', 'gymnast', 'sprinter', 'runner', 'marathon',
    'touchdown', 'quarterback', 'goalkeeper', 'striker', 'midfielder', 'defender',
    'lakers', 'yankees', 'red sox', 'pistons', 'spurs', 'patriots', 'eagles', 'real madrid', 'manchester united', 'arsenal', 'chelsea'
}

supportive_keywords = {
    'team', 'teams', 'player', 'players', 'coach', 'coaches', 'manager', 'season', 'league', 'game', 'games', 'match', 'matches', 'score', 'scores', 'win', 'wins', 'won', 'victory', 'defeat', 'loss', 'standings', 'rankings', 'final', 'finals', 'semi-final', 'quarter-final'
}

def is_sports_article(title, desc):
    text = (title + " " + desc).lower()
    words = set(text.replace('.', ' ').replace(',', ' ').replace('"', ' ').replace("'", " ").replace('-', ' ').replace('(', ' ').replace(')', ' ').split())
    
    strong_hits = 0
    for k in strong_sports_keywords:
        if k in words:
            strong_hits += 1
            
    supportive_hits = 0
    for k in supportive_keywords:
        if k in words:
            supportive_hits += 1
            
    if strong_hits >= 2: return True
    if strong_hits == 1 and supportive_hits >= 1: return True
    if strong_hits == 0 and supportive_hits >= 3: return True
    return False

candidates = []
for art in articles:
    if is_sports_article(art.get('title', ''), art.get('description', '')):
        candidates.append(art)

candidates.sort(key=lambda x: len(x.get('description', '')), reverse=True)

top_5 = []
for c in candidates[:5]:
    top_5.append({
        "title": c['title'],
        "len": len(c['description']),
        "desc_preview": c['description'][:100]
    })

print('__RESULT__:')
print(json.dumps(top_5))"""

env_args = {'var_function-call-13425849250340165156': ['articles'], 'var_function-call-13425849250340165453': ['authors', 'article_metadata'], 'var_function-call-17951318789273803263': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6587525704781607090': {'error': 'No sports articles found'}, 'var_function-call-11688380307488085183': [{'_id': '6944891d88e03095837aa408', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944891d88e03095837aa409', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944891d88e03095837aa40a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944891d88e03095837aa40b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944891d88e03095837aa40c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-303762971753374915': 'file_storage/function-call-303762971753374915.json', 'var_function-call-1054896516764720812': {'title': "Why Windows isn't Unix", 'len': 708, 'desc_preview': '\\\\"I first heard about this from one of the developers of the hit game SimCity, who\\told me that there was a critical bug in his application: it used memory right\\after freeing it, a major no-no that happened to work OK on DOS but would not\\work under Windows where memory that is freed is likely to be snatched up by\\another running application right away. The testers on the Windows team were\\going through various popular applications, testing them to make sure they\\worked OK, but SimCity kept crashing. They reported this to the Windows\\developers, who disassembled SimCity, stepped through it in a debugger, found\\the bug, and added special code that checked if SimCity was running, and if it\\did ...\\\\'}, 'var_function-call-17102203901169534494': {'title': 'Pretty Log4J', 'len': 708, 'desc_preview': '\\\\I\'ve been a big fan of Log4J  for a while now but haven\'t migrated any code\\over for one central reason.  The following line of code:\\\\    final static Logger logger = Logger.getLogger( "some.name" );\\\\... is amazingly ugly and difficult to work with.\\\\Most people use Log4J with a logger based on the classname:\\\\So we would probably see:\\\\    static Logger logger = Logger.getLogger( "org.apache.commons.feedparser.locate.FeedLocator" );\\\\Which is amazingly verbose.  A lot of developers shorten this to:\\\\    static Logger logger = Logger.getLogger( FeedLocator.class );\\\\But this still leaves us with cut and paste errors.\\\\What if we could just reduce it to:\\\\    static Logger logger = Logger.g ...\\\\'}, 'var_function-call-16546184093953620131': {'title': 'THECHAT', 'len': 631, 'desc_preview': '&lt;em&gt; Dean Cain has spent much of his life in a uniform. He\'s done time as an all-American safety at Princeton (where he established a since-broken single-season Division I-AA record for interceptions), an undrafted free agent with the Buffalo Bills (before a preseason knee injury ended his football career), a sportsman of the future (in the aptly named movie "Futuresport") and an iconic superhero (in television\'s "Lois and Clark: The New Adventures of Superman"). Next up is a set of pinstripes -- Cain plays star third baseman Conrad Dean in the CBS drama "Clubhouse," which is scheduled to debut next month. &lt;/em&gt;'}}

exec(code, env_args)

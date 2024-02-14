class Game:

    all_games = []

    def __init__(self, title):
        self.title = title
        type(self).all_games.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title):
        # if isinstance(title,str) and len(title) > 0:
        if isinstance(title, str) and not hasattr(self, "title") and title:
            self._title = title
        # else:
        #     raise Exception("Title property must be of istance string, and more than 0 characters ")

    def results(self):
        '''Returns a list of all results for that game. Results must be of type Result'''
        # return [r for r in Result.all_results if r.game is self]
        return [result for result in Result.all_results if result.game is self]

    def players(self):
        '''Returns a unique list of all players that played a particular game. Players must be of type Player'''
        #return list(set([r.player for r in self.results() if r.game is self]))
        return list({result.player for result in self.results()})

    def average_score(self, player):
        '''Returns the average of all the player's scores for a particular game instance'''
        d = [r.score for r in self.results() if r.player is player]
        if len(d) == 0:
            return 0
        else:
            avg_score = sum(d)/len(d)
            return avg_score

class Player:

    all_players = []

    def __init__(self, username):
        self.username = username
        type(self).all_players.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self,username):
        if isinstance(username,str) and (2 <= len(username) <=16):
            self._username = username
        # else:
        #     raise Exception("Title property must be of istance string, and more than 0 characters ")

    def results(self):
        '''Returns a list of all results for that player. must be of type Result'''
        return [r for r in Result.all_results if r.player is self]

    def games_played(self):
        '''Returns a unique list of all games played by a particular player. Games must be of type Game'''
        #return [r.game for r in Result.all_results if r.player is self]
        return list({r.game for r in self.results()})

    def played_game(self, game):
        '''Returns True if the player has played the game object provided'''
        x = game in self.games_played()
        return x

    def num_times_played(self, game):
        '''Returns the number of times the player has played the game instance provided'''
        #x = [r.game for r in self.results() if r.game is self ]
        # if x != []:
        #     return len(x)
        # else:
        #     return 0
        games_played = [result.game for result in self.results()]
        return games_played.count(game)

class Result:
    all_results = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all_results.append(self)

    @property
    def score(self):
        return self._score 
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and not hasattr(self, "score") and  (1<= score <=5000):
            self._score = score
        # else:
        #     raise Exception("Title property must be of istance string, and more than 0 characters ")

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self,player):
        if isinstance(player, Player):
            self._player = player
        # else:
        #   raise Exception("not instance of Player")

    @property
    def game(self):
        return self._game 
    
    @game.setter
    def game(self,game):
        if isinstance(game, Game):
            self._game = game
        # else:
        #   raise Exceptions("not instance of Game")
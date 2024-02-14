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
        pass

    def players(self):
        pass

    def average_score(self, player):
        pass

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
        pass

    def games_played(self):
        pass

    def played_game(self, game):
        pass

    def num_times_played(self, game):
        pass

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
        return self.all_players

    @player.setter
    def player(self,player):
        if isinstance(player, Player):
            self._player = player
        # else:
        #   raise Exception("asf")
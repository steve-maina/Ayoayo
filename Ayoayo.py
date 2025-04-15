from my_list import MyLinkedList

class Ayoayo:
    __seed = 1
    __winner = None
    __players = []
    __game_over = False

    def __init__ (self,num_seeds = 4):
        self.linked_list = MyLinkedList(num_seeds=num_seeds)

    def get_players(self):
        return self.__players
    def createPlayer(self,name):
        if len(self.__players)>=2:
            print("Only two players can play")
            return
        new_player = Player(name)
        self.__players.append(new_player)
        return new_player
    def printBoard(self):
        player_1 = self.linked_list.get_player_seeds(0)
        player_2 = self.linked_list.get_player_seeds(1)
        game_over = self.is_game_over()
        if game_over in [0,1,2]:
            print(f"player1:\nstore: {sum(player_1)}\n[{0}, {0}, {0}, {0}, {0}, {0}]\nplayer2:\nstore: {sum(player_2)}\n[{0}, {0}, {0}, {0}, {0}, {0}]\n")
        print(f"player1:\nstore: {player_1[6]}\n[{player_1[0]}, {player_1[1]}, {player_1[2]}, {player_1[3]}, {player_1[4]}, {player_1[5]}]\nplayer2:\nstore: {player_2[6]}\n[{player_2[0]}, {player_2[1]}, {player_2[2]}, {player_2[3]}, {player_2[4]}, {player_2[5]}]\n")
    def returnWinner(self):
        game_over = self.is_game_over()
        if game_over in [0,1,2]:
           if game_over == 0:
               return f"Winner is player 1: {self.__players[0].get_name()}"
           if game_over == 1:
               return f"Winner is player 2: {self.__players[1].get_name()}"
           if game_over == 2:
               return "It's a tie"
        return "Game has not ended"
    def playGame(self,player_index,pit_index):
        game_over = self.is_game_over()
        if game_over in [0,1,2]:
            self.__game_over = True
            return "Game is ended"
        if pit_index > 6 or pit_index <= 0:
            return "Invalid number for pit index"
        return self.linked_list.play_game(player_index=player_index -1 ,pit_index=pit_index - 1)
    def is_game_over(self):
        if self.__game_over:
            return  self.__winner
        player_1 = self.linked_list.get_player_seeds(0)
        player_2 = self.linked_list.get_player_seeds(1)
        player_1_empty_pits = 0
        player_2_empty_pits = 0
        for i in range(len(player_1) - 1):
            if player_1[i] == 0 :
                player_1_empty_pits += 1
        for i in range(len(player_2) - 1):
            if player_2[i] == 0 :
                player_2_empty_pits += 1
        if player_1_empty_pits == 6 or player_2_empty_pits == 6:
            player_1_seeds = sum(player_1)
            player_2_seeds = sum(player_2)
            self.linked_list.setup_list()
            print("linked list", self.printBoard())
            store1 = self.linked_list.get_node(0,6).data = [self.__seed for i in range(player_1_seeds)]
            print("store1 ", store1)
            store2 = self.linked_list.get_node(1,6).data = [self.__seed for i in range(player_2_seeds)]

            if player_1_seeds > player_2_seeds:
                self.__game_over = True
                self.__winner = 0
                return 0
            elif player_2_seeds > player_1_seeds:
                self.__game_over = True
                self.__winner = 1
                print("got here")
                return 1
            else:
                self.__game_over = True
                self.__winner = 2
                return 2


class Player:
    def __init__(self,name):
        self.__name = name
    def __repr__(self):
        return self.__name
    def get_name(self):
        return self.__name


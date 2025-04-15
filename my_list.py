class Node:
    def __init__(self,is_store, player_num,data,index):
        self.is_store = is_store
        self.player_num = player_num
        self.data = data
        self.next = None
        self.index = index
class MyLinkedList:
    def __init__(self, num_seeds,seed=1):
        self.head = None
        self.num_seeds = num_seeds
        self.seed = seed
        self.setup_list()
    def setup_list(self):
        index = 0
        data = [self.seed for i in range(self.num_seeds)]
        for i in range(2):
            for j in range(7):
                if j == 6 :
                    node = Node(is_store=True,player_num=i,data=[],index=index)
                    self.insert_node(node)
                    index += 1
                    continue
                node = Node(is_store=False, player_num=i, data=data.copy(),index = index)
                self.insert_node(node)
                index +=1
    def get_player_seeds(self, player_num):
        list =[]
        first_node = self.head
        if first_node.player_num == player_num:
            list.append(len(first_node.data))
        next_node = self.head.next
        while next_node != first_node:
            if next_node.player_num == player_num:
                print(next_node.data, next_node.index)
                list.append(len(next_node.data))
            next_node = next_node.next
        return list
    def insert_node(self,node):
        if self.head is None:
            self.head = node
            node.next = self.head
            return
        last_node = self.head.next
        while last_node.next != self.head:
            last_node = last_node.next
        last_node.next = node
        node.next = self.head
    def print_list(self):
        first_node = self.head
        if first_node is None:
            return
        print(first_node.data,first_node.player_num, first_node.is_store, first_node.index)
        next_node = self.head.next
        while next_node != first_node:
            print(next_node.data, next_node.player_num, next_node.is_store, next_node.index)
            next_node = next_node.next
        if next_node == first_node:
            return
    def play_game(self, player_index,pit_index):
        desired_node = None
        first_node = self.head
        if(first_node.player_num == player_index and pit_index == first_node.index):
            self.move_seeds(player_index=player_index,node=first_node)
        next_node = first_node.next
        while True:
            if(next_node.player_num == player_index and pit_index == next_node.index % 7):
                desired_node= next_node
                break
            else:
                next_node = next_node.next
        self.move_seeds(player_index=player_index,node=desired_node)
        player_1_seeds =  self.get_player_seeds(0)
        print("player1 seeds ", player_1_seeds)
        player2_seeds = self.get_player_seeds(1)
        return player_1_seeds + player2_seeds
    def move_seeds(self, player_index,node):
        num_seeds = len(node.data)
        node.data = []
        next_node = node.next
        while num_seeds > 0:
            if next_node.player_num != player_index and next_node.is_store:
                next_node = next_node.next
                continue
            if num_seeds == 1 and next_node.is_store and next_node.player_num == player_index:
                next_node.data.append(self.seed)
                print(f"player {player_index + 1} take another turn")
                break
            if num_seeds == 1 and len(next_node.data) == 0 and next_node.player_num == player_index:
                # capture opponent
                p_index = 1 if player_index == 0 else 0
                opposite_index = [i for i in range(6)][-next_node.index-1]
                opposite_node = self.get_node(player_index = p_index, positional_index=opposite_index)
                opposite_node_len = len(opposite_node.data)
                opposite_node.data = []
                pos_index = 6 if player_index == 0 else 13
                store_node = self.get_node(player_index=player_index,positional_index=pos_index)
                for i in range(opposite_node_len):
                    store_node.data.append(self.seed)
                store_node.data.append(self.seed)
                num_seeds -= 1
                continue
            next_node.data.append(self.seed)
            next_node = next_node.next
            num_seeds -=1
    def get_node(self, player_index, positional_index):
        first_node = self.head
        if first_node.player_num == player_index and positional_index == first_node.index:
            return first_node
        next_node = first_node.next
        while next_node != first_node:
            if next_node.player_num == player_index and positional_index == next_node.index % 7:
                return next_node
            next_node = next_node.next
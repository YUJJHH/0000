#  도전 p7~~
'''class Zergling :
    def __init__(self):
        self.hp =20
        self.mana =50

    def run(self):
        print("뛴다")
        self.hp -= 1
        self.mana += 1
        

    def show_status(self):
        print(f'HP : {self.hp}')
        print(f'mana : {self.mana}')

    # def z1(self):
        # run()

z1 = Zergling()
z2 = Zergling()

z1.run()
z1.show_status()

for i in range(5):
    z2.run()
z2.show_status()

'''

''' 이건 틀린 방법
tes = Zergling()
tes.run()
z1 = tes.show_status()
print('------------')
tes.run()
tes.run()
tes.run()
tes.run()
tes.run()
z2 = tes.show_status()
'''

'''
class GameMachine:
    def __init__(self):
        self.coins = 0  # 현재 보유 코인
        # self.coin_status = 0
    
    def input_coin(self,amout):
        if amout > 5:
            return
        if self.coins + amout > 10:
            return
        self.coins += amout
        # self.coin_status += 1
        # if self.coin

    def play_game(self):
        if self.coins <1 :
            print('코인을 넣어주세요')
            return
        self.coins -= 1
        print('게임 재밌다')

    def show_status(self):
        print(f'남아있는 코인은 {self.coins}')

gm = GameMachine()
gm.input_coin(2)
gm.show_status()
gm.play_game()
gm.show_status()

'''



'''# 도전 p19

    
class super():
    def run(self): print("run")

class elec(super):
    def ran(self): print("ran")

class mountain(super):
    def ron(self): print("ron")
    def run(self): print("rrrun")    

# s = super()
m = mountain()
m.ron()
m.run()  # 부모 메서드 변경

e = elec()
e.run()  #부모 메서드 사용

'''

'''
import numpy as np

lst = [1,2, 3, 4, 5]
result_lst = lst *2  # 각 인덱스 마다 곱하기 2 하고 싶은데 안됨 리스트는

print(result_lst)

numpy_array = np.array([1, 2, 3, 4, 5])
result_array= numpy_array *2
print(result_array)
'''





print('ssssss')


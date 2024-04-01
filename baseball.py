import random

First_base = 0
Second_base = 0
Third_base = 0
Fourth_base = 0
Red_point = 0
Blue_point = 0
Out_count = 0

class Pitcher:
    def __init__(self, FastBall, BreakingBall, HP, Ability):
        self.FastBall = FastBall
        self.BreakingBall = BreakingBall
        self.HP = HP
        self.Ability = Ability
        
class Hitter:
    def __init__(self, BallCount, StrikeCount, Hit, Ability):
        self.BallCount = BallCount
        self.StrikeCount = StrikeCount
        self.Hit = Hit
        self.Ability = Ability
        
P1 = Pitcher(random.randint(140,150), random.randint(120,130), 100, 90)
P1.FastBall = random.randint(140,150)
P1.BreakingBall = random.randint(120,130)
P1.HP = 100
P1.Ability = 90

P2 = Pitcher(random.randint(150,160), random.randint(130,140), 50, 150)
P2.FastBall = random.randint(155,165)
P2.BreakingBall = random.randint(135,145)
P2.HP = 50
P2.Ability = 150

P3 = Pitcher(random.randint(150,160), random.randint(130,140), 60, 130)
P3.FastBall = random.randint(150,160)
P3.BreakingBall = random.randint(130,140)
P3.HP = 60
P3.Ability = 130

P4 = Pitcher(random.randint(135,145), random.randint(115,125), 100, 70)
P4.FastBall = random.randint(135,145)
P4.BreakingBall = random.randint(115,125)
P4.HP = 100
P4.Ability = 70

P5 = Pitcher(random.randint(135,145), random.randint(120,130), 80, 80)
P5.FastBall = random.randint(135,145)
P5.BreakingBall = random.randint(120,130)
P5.HP = 80
P5.Ability = 80

H1_2 = Hitter(0, 0, random.randint(1,100), 100)
H1_2.BallCount = 0
H1_2.StrikeCount = 0
H1_2.Hit = random.randint(1,100)
H1_2.Ability = 100

H3_5 = Hitter(0, 0, random.randint(1,100), 120)
H3_5.BallCount = 0
H3_5.StrikeCount = 0
H3_5.Hit = random.randint(1,100)
H3_5.Ability = 120

H6_9 = Hitter(0, 0, random.randint(1,100), 80)
H6_9.BallCount = 0
H6_9.StrikeCount = 0
H6_9.Hit = random.randint(1,100)
H6_9.Ability = 80

a = H1_2.Ability - P1.Ability
b = H3_5.Ability - P1.Ability
c = H6_9.Ability - P1.Ability

def H1_2():
    for i in range(2):#H1_2가 1번, 2번타자이므로 2번 실행
        while True:
            if Out_count == 3: #3아웃이 된다면
                print("이닝 종료!") #이닝 종료를 표시
                break #반복문 종료
            elif H1_2.StrikeCount == 3: #스트라이크를 3번 먹으면
                Out_count += 1 #아웃카운트에 1 더하기
                break #while 반복문 끝내기
            elif H1_2.Hit >= a+40: #타자에서 투수의 능력치를 뺀 것에 40을 더한 %의 확률로 안타를 친다면
                print("Hit!") #안타를 쳤음을 표시
                break #while 반복문 끝내기
            else: #안타를 치지 못한다면
                H1_2.StrikeCount += 1 #스트라이크 카운트에 1 더하기
    H1_2.StrikeCount = 0 #반복문이 끝나면 변수 값 초기화
H1_2()
def H3_5():
    for i in range(3): #H3_5가 3번, 4번, 5번 타자이므로 3번 실행
        while True: 
            if Out_count == 3:
                print("이닝 종료!")
                break
            elif H3_5.StrikeCount == 3:
                Out_count += 1
                break
            elif H3_5.Hit >= b+40:
                print("Hit!")
                break
            else:
                H3_5.StrikeCount += 1
    H3_5.StrikeCount = 0 #반복문이 끝나면 변수 값 초기화
    if Out_count == 3:
        Out_count = 0
H3_5()

print(Out_count)






'''
for i in range(20):
    Fastball = random.randint(145,155)
    Breakingball = random.randint(125,135)
    print(Fastball)
    print(Breakingball)
'''
'''
First_base += 1
if F
irst_base == 1:
    Second_base += 1
print(First_base)
print(Second_base)
Third_base += 1
if Third_base == 1 and Second_base == 0 and First_base == 0:
    First_base += 1
if Third_base
print(First_base)
print(Third_base)
'''


if Fourth_base >= 1: #득점
    Red_point =+ Fourth_base
    Fourth_base = 0


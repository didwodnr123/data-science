class SoccerPlayer(object):
    # Attribute
    # __main__, __add__ : 맨글링
    # self : 생성된 인스턴스 자기 자신. self는 son 과 park 에서 다르다.
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number
    def __str__(self):
        return "Hello, My name is %s. I play in %s in center " % (self.name, self.position)
    # Action
    def change_back_number(self, new_number):
        print("선수의 등번호를 변경합니다 : From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number

son = SoccerPlayer('Son', 'FW', 7)
park = SoccerPlayer('Park', 'MF', 13)

son.change_back_number(13)
park.change_back_number(7)

print(son)
print(park)

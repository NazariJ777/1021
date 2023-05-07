import random
class Student:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.alive=True
        self.money=50

    def to_study(self):
        print('Час вчитись')
        self.progress+=0.12
        self.gladness-=3
    def to_sleep(self):
        print('Час спати')
        self.gladness+=3
    def to_chill(self):
        print('Час відпочивати')
        self.gladness+=5
        self.progress-=0.1
        self.money-=10
    def to_work(self):
        print('Час працювати')
        self.gladness-=3
        self.money+=40
        self.progress+=0.05
    def is_alive(self):
        if self.progress<-0.5:
            print('Відрахували...')
            self.alive=False
        elif self.gladness<=0:
            print('Дипресія...')
            self.alive=False
        elif self.progress>5:
            print('Закінчив Екстерном')
            self.alive=False
        elif self.money<-100:
            print('Банкрот...')
            self.alive=False

    def end_of_day(self):
        print(f'Gladness - {self.gladness}')
        print(f'Progress - {round(self.progress,2)}')
        print(f'Money - {round(self.money,3)}')

    def live(self,day):
        if self.money<-30:
            self.to_work()
        day='Day' +str(day) + 'of' + self.name + 'live'
        print(f'{day:^50}')
        live_cube=random.randint(1,4)
        if live_cube==1:
            self.to_study()
        elif live_cube==2:
            self.to_sleep()
        elif live_cube==3:
            self.to_chill()
        elif live_cube==4:
            self.to_work()
        self.end_of_day()
        self.is_alive()

makaka=Student(name='Makaka')
for day in range(365):
    if makaka.alive==False:
        break
    makaka.live(day)






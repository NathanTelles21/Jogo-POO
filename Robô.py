#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Point(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '<%s, %s>' % (self.x, self.y)

class Reward(Point):
    
    def __init__(self, x, y, name):
        super(Reward, self).__init__(x, y)
        self.name = name
    
    def __str__(self):
        return '<%s, %s>: %s' % (self.x, self.y, self.name)
    
    def __repr__(self):
        return '<Reward> %s' % str(self)

class Robot(Point):
    
    def move_up(self):
        if self.y < 10:
            self.y = self.y + 1
        else:
            print('Movimento proibido')
    
    def move_down(self):
        if self.y > 0:
            self.y = self.y - 1
        else:
            print('Movimento proibido')
    
    def move_left(self):
        if self.x > 0:
            self.x = self.x - 1
        else:
            print('Movimento proibido')
    
    def move_right(self):
        if self.x < 10:
            self.x = self.x + 1
        else:
            print('Movimento proibido')


# In[2]:


def check_reward(robot, rewards):
    ok = False
    for reward in rewards:
        if reward.x == robot.x and reward.y == robot.y:
            print("O robô achou a recompensa: %s" % reward.name)
            ok = True
    return ok


# In[3]:


import random
r1 = Reward(random.randint(0, 10), random.randint(0, 10), 'moeda')
r2 = Reward(random.randint(0, 10), random.randint(0, 10), 'gasolina')
r3 = Reward(random.randint(0, 10), random.randint(0, 10), 'arma')
r4 = Reward(random.randint(0, 10), random.randint(0, 10), 'moeda')
r5 = Reward(random.randint(0, 10), random.randint(0, 10), 'gasolina')
r6 = Reward(random.randint(0, 10), random.randint(0, 10), 'arma')
r7 = Reward(random.randint(0, 10), random.randint(0, 10), 'moeda')
r8 = Reward(random.randint(0, 10), random.randint(0, 10), 'gasolina')
r9 = Reward(random.randint(0, 10), random.randint(0, 10), 'arma')
rewards = [r1, r2, r3, r4, r5, r6, r7, r8, r9]


# In[4]:


robot = Robot(random.randint(0, 10), random.randint(0, 10))


# In[5]:


for i in range(10):
    moviment = input("Digite up, down, left ou right para o movimento: ")
    if moviment == 'up':
        robot.move_up()
    elif moviment == 'down':
        robot.move_down()
    elif moviment == 'left':
        robot.move_left()
    elif moviment == 'right':
        robot.move_right()
    else:
        print('Movimento inválido')
        continue
    print(robot)
    check_reward(robot, rewards)


# In[6]:


rewards


# In[ ]:





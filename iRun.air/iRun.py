
__author__ = "cgq8xm5d"

from airtest.core.api import *
import random
import datetime
import os



auto_setup(__file__)

current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d-")
current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = '/'.join(current_dir.split('\\'))
accounts = []
passwords = []
remainingCounts = []
flags_to_run = []
finished_accounts = []
config = {}


with open('config.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        key, value = line.split('=')
        config[key] = bool(int(value))

with open('repo.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    line = line.strip()
    account, password, remainingCount = line.split(' ')
    accounts.append(account)
    passwords.append(password)
    remainingCounts.append(int(remainingCount))
    print(f'account: {account} password: {password} remainingCount: {remainingCount}')

with open('finished_accounts.txt', 'r', encoding='utf-8') as f:  
    for line in f:  
        account = line.strip()  
        finished_accounts.append(account)  

for i in range(len(accounts)):
    if accounts[i] not in finished_accounts:
        if remainingCounts[i] != 0:
            print(f"Add account {accounts[i]} in waitlist.")
            flags_to_run.append(1)
        else:
            flags_to_run.append(0)
    else:
        flags_to_run.append(0)

print(f"init_flag = {config['init_flag']}")
if config['init_flag']:
    home()
    # open fakelocation
    touch(Template(current_dir + r"/PositioningImages/tpl1683810469972.png", record_pos=(0.344, -0.296), resolution=(1080, 1920)))
    print(current_dir + r"/PositioningImages/tpl1683810469972.png")
    # open menu of fakelocation
    touch(Template(current_dir + r"/PositioningImages/tpl1683647750297.png", record_pos=(-0.426, -0.756), resolution=(1080, 1920)))
    # open route simulation
    touch(Template(current_dir + r"/PositioningImages/tpl1683647757054.png", record_pos=(-0.264, -0.06), resolution=(1080, 1920)))
    # wait system initialization
    for time in range(160, 0, -1):
        print(time, end=' ')
        if time % 10 == 1:
            print()
        sleep(1)
    # run simulation
    touch(Template(current_dir + r"/PositioningImages/tpl1683647762584.png", record_pos=(-0.305, 0.14), resolution=(1080, 1920)))
    # wait simulating success
    wait(Template(current_dir + r"/PositioningImages/tpl1683722040632.png", record_pos=(-0.122, 0.137), resolution=(1080, 1920)))
    home()

    # open run app
    wait(Template(current_dir + r"/PositioningImages/tpl1683810488818.png", record_pos=(0.113, -0.301), resolution=(1080, 1920)))
    touch(Template(current_dir + r"/PositioningImages/tpl1683810493914.png", record_pos=(0.113, -0.301), resolution=(1080, 1920)))


# main loop
for i in range(len(accounts)):
    try:
        if flags_to_run[i] == 0:
            continue
        account = accounts[i]
        password = passwords[i]
        print(f'{account} {remainingCounts[i]}')

        # student login
        wait(Template(current_dir + r"/PositioningImages/tpl1683722850936.png", record_pos=(-0.006, 0.09), resolution=(1080, 1920)))
        touch(Template(current_dir + r"/PositioningImages/tpl1683647064588.png", record_pos=(0.007, 0.093), resolution=(1080, 1920)))
        
        # input account
        touch(Template(current_dir + r"/PositioningImages/tpl1683647076456.png", record_pos=(-0.22, -0.188), resolution=(1080, 1920)))
        sleep(1.0)
        text(account, enter=False)

        # input password
        touch(Template(current_dir + r"/PositioningImages/tpl1683647113113.png", record_pos=(-0.216, -0.044), resolution=(1080, 1920)))
        sleep(1.0)
        text(password)
        # login
        touch(Template(current_dir + r"/PositioningImages/tpl1683647236235.png", record_pos=(0.004, 0.256), resolution=(1080, 1920)))

        # begin to run
        try:
            wait(Template(current_dir + r"/PositioningImages/tpl1685843517329.png", record_pos=(0.003, 0.101), resolution=(1080, 1920)))
            touch(Template(current_dir + r"/PositioningImages/tpl1685843528616.png", record_pos=(-0.005, 0.104), resolution=(1080, 1920)))


        except:
            touch(Template(current_dir + r"/PositioningImages/tpl1685782140026.png", record_pos=(-0.419, -0.742), resolution=(1080, 1920)))
            sleep(2)
            continue
        wait(Template(current_dir + r"/PositioningImages/tpl1683723118649.png", record_pos=(-0.006, 0.775), resolution=(1080, 1920)))
        touch(Template(current_dir + r"/PositioningImages/tpl1683722276727.png", record_pos=(-0.006, 0.771), resolution=(1080, 1920)))
        wait(Template(current_dir + r"/PositioningImages/tpl1683797443468.png", record_pos=(0.312, 0.285), resolution=(1080, 1920)))
        touch(Template(current_dir + r"/PositioningImages/tpl1683797449823.png", record_pos=(0.306, 0.294), resolution=(1080, 1920)))

        try:
            
            
            touch(Template(current_dir + r"/PositioningImages/tpl1683797449823.png", record_pos=(0.306, 0.294), resolution=(1080, 1920)))
        except Exception as e:
            
            
            print("ERROR:", str(e))

        try:
            
            
            sleep(5)
            wait(Template(current_dir + r"/PositioningImages/tpl1683797443468.png", record_pos=(0.312, 0.285), resolution=(1080, 1920)))
            touch(Template(current_dir + r"/PositioningImages/tpl1683797449823.png", record_pos=(0.306, 0.294), resolution=(1080, 1920)))
        except Exception as e:
            
            
            print("ERROR:", str(e))
            
        
        for time in range(random.randint(640, 680)+1, 0, -1):
            print(time, end=' ')
            if time % 10 == 1:
                print()
            sleep(1)
        wait(Template(current_dir + r"/PositioningImages/tpl1683722612055.png", record_pos=(0.001, 0.722), resolution=(1080, 1920)))
        touch(Template(current_dir + r"/PositioningImages/tpl1683722604266.png", record_pos=(-0.001, 0.719), resolution=(1080, 1920)))

        wait(Template(current_dir + r"/PositioningImages/tpl1683722650261.png", record_pos=(0.308, 0.171), resolution=(1080, 1920)))
        touch(Template(current_dir + r"/PositioningImages/tpl1683722632440.png", record_pos=(0.308, 0.168), resolution=(1080, 1920)))
        try:
            sleep(3)
            wait(Template(current_dir + r"/PositioningImages/tpl1683791836893.png", record_pos=(0.128, 0.167), resolution=(1080, 1920)))
            touch(Template(current_dir + r"/PositioningImages/tpl1683791845445.png", record_pos=(0.122, 0.163), resolution=(1080, 1920)))

            wait(Template(current_dir + r"/PositioningImages/tpl1683791869071.png", record_pos=(-0.423, -0.747), resolution=(1080, 1920)))
            snapshot(filename=current_dir + '/RecordImages/speed' + formatted_datetime + account + '.png')
            touch(Template(current_dir + r"/PositioningImages/tpl1683791881022.png", record_pos=(-0.425, -0.749), resolution=(1080, 1920)))
        except:
            wait(Template(current_dir + r"/PositioningImages/tpl1683722612055.png", record_pos=(0.001, 0.722), resolution=(1080, 1920)))
            touch(Template(current_dir + r"/PositioningImages/tpl1683722604266.png", record_pos=(-0.001, 0.719), resolution=(1080, 1920)))

            wait(Template(current_dir + r"/PositioningImages/tpl1683722650261.png", record_pos=(0.308, 0.171), resolution=(1080, 1920)))
            touch(Template(current_dir + r"/PositioningImages/tpl1683722632440.png", record_pos=(0.308, 0.168), resolution=(1080, 1920)))

        wait(Template(current_dir + r"/PositioningImages/tpl1683722313335.png", record_pos=(0.403, 0.807), resolution=(1080, 1920)))
        snapshot(filename=current_dir + '/RecordImages/snapshot' + formatted_datetime + account + '.png', msg=account)

        touch(Template(current_dir + r"/PositioningImages/tpl1683722317490.png", record_pos=(0.395, 0.817), resolution=(1080, 1920)))

        try:
            wait(Template(current_dir + r"/PositioningImages/tpl1683799661964.png", record_pos=(0.124, -0.372), resolution=(1080, 1920)))
            touch(Template(current_dir + r"/PositioningImages/tpl1683799669723.png", record_pos=(0.122, -0.367), resolution=(1080, 1920)))
            wait(Template(current_dir + r"/PositioningImages/tpl1683799738168.png", record_pos=(-0.215, -0.433), resolution=(1080, 1920)))
            snapshot(filename=current_dir + '/RecordImages/record' + formatted_datetime + account + '.png')
            touch(Template(current_dir + r"/PositioningImages/tpl1683799791793.png", record_pos=(-0.457, -0.769), resolution=(1080, 1920)))
        except:
            pass
        
        
        with open('finished_accounts.txt', 'a', encoding='utf-8') as file:
            file.write(account + '\n')
        remainingCounts[i] = remainingCounts[i] - 1
        with open('repo.txt', 'w', encoding='utf-8') as file:
            for m in range(len(accounts)):
                file.writelines(f'{accounts[m]} {passwords[m]} {remainingCounts[m]}\n')
                
        touch(Template(current_dir + r"/PositioningImages/tpl1683722330526.png", record_pos=(0.381, -0.75), resolution=(1080, 1920)))
        touch(Template(current_dir + r"/PositioningImages/tpl1683722335676.png", record_pos=(-0.268, -0.49), resolution=(1080, 1920)))
        wait(Template(current_dir + r"/PositioningImages/tpl1683723146060.png", record_pos=(-0.003, 0.217), resolution=(1080, 1920)))

        touch(Template(current_dir + r"/PositioningImages/tpl1683722341796.png", record_pos=(0.003, 0.215), resolution=(1080, 1920)))
    except:
        pass
    
print("finished!")







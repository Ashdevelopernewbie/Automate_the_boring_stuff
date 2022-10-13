# simple timer program
print('This is a simple timer of 10 ticks.')

timer = 0
print("Do you want to start the timer?(on/off)")
mode = input()

while(mode == 'on'):
    print('Timer is on')
    timer = timer + 1
    if(timer == 10):
        break

print('Timer is off')

if(timer == 'off'):
    print('Timer did not start')
bool = True
while(bool):
    numbers = input()
    
    arrayNumber = numbers.split()
    projectType = ""
    for number in arrayNumber:
        if(float(number) < 0):
            raise Exception("Sorry, no numbers below zero")
    
    h = float(arrayNumber[0])
    c = float(arrayNumber[1])
    l = float(arrayNumber[2])
    if(h == 0.0 and c == 0.0 and l == 0.0):
        bool = False
        break
    
    i = (h * 100) / c
    if(i <= 8.334 and l >= 0.8):
        print('PROJETO SIMPLES')
    else:
        print('PROJETO ESPECIAL')

def indefinido(*args):
    contador = 0
    for arg in args:
        if contador + 1 == len(args):
            return False
        if args[contador] == 0 and args[contador+1] == 0:
            return True
        else:
            contador +=1
    return False
        

    

print(indefinido(0,2,5,0,0,8))
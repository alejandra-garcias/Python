from collections import defaultdict
mi_dic =defaultdict(lambda: 'nada') ## es para que cuando mi dic no tiene la clave se le cambia por la palabra nada
mi_dic['uno']= 'verde'
print(mi_dic['dos'])
print(mi_dic) ### me ha construido una segunda clave dos y la ha igualado a nada

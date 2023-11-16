from tkinter import *
import random
import datetime
from tkinter import filedialog,messagebox
operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_boton(numero):
    global operador
    operador = operador+numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END,operador)


def borrar():
    global operador 
    operador= ''
    visor_calculadora.delete(0,END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0,resultado)
    operador = ''

def revisar_check():
    x = 0
    for c in cuadros_comidas:
        if variables_comidas[x].get()==1:
            cuadros_comidas[x].config(state=NORMAL)
            if cuadros_comidas[x].get()=='0':
                cuadros_comidas[x].delete(0,END)
            cuadros_comidas[x].focus()
        else:
            cuadros_comidas[x].config(state=DISABLED)
            texto_comidas[x].set('0')
        x+=1
    x = 0
    for c in cuadros_bebidas:
        if variables_bebidas[x].get()==1:
            cuadros_bebidas[x].config(state=NORMAL)
            if cuadros_bebidas[x].get()=='0':
                cuadros_bebidas[x].delete(0,END)
            cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set('0')
        x+=1
    x = 0
    for c in cuadros_postres:
        if variables_postres[x].get()==1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get()=='0':
                cuadros_postres[x].delete(0,END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x+=1

def total():
    p=0
    sub_total_comida = 0
    for cantidad in texto_comidas:
        sub_total_comida=sub_total_comida+(float(cantidad.get())*precios_comida[p])
        p+=1
    p=0
    sub_total_bebida = 0
    for cantidad in texto_bebidas:
        sub_total_bebida=sub_total_bebida+(float(cantidad.get())*precios_bebida[p])
        p+=1
    p=0
    sub_total_postres = 0
    for cantidad in texto_postres:
        sub_total_postres=sub_total_postres+(float(cantidad.get())*precios_postres[p])
        p+=1
    subtotal=sub_total_postres+sub_total_bebida+sub_total_comida
    impuestos = subtotal*0.07
    total = subtotal+impuestos
    
    var_costo_comida.set(f'${round(sub_total_comida,2)} ')
    var_costo_bebida.set(f'${round(sub_total_bebida,2)} ')
    var_costo_postres.set(f'${round(sub_total_postres,2)} ')
    var_costo_subtotal.set(f'${round(subtotal,2)} ')
    var_costo_impuestos.set(f'${round(impuestos,2)} ')
    var_costo_total.set(f'${round(total,2)} ')


def recibo():
    texto_recibo.delete(1.0,END)
    num_recibo=f'N#-{random.randint(1000,9999)}'
    fecha=datetime.datetime.now()
    fecha_recibo =f'{fecha.day}/{fecha.month}/{fecha.year}-{fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END,f'Datos:\t{num_recibo}\t\t{fecha_recibo} \n')
    texto_recibo.insert(END,f'*'*153+'' '\n')
    texto_recibo.insert(END, 'Items\t\tCant\tCosto Items\n')
    texto_recibo.insert(END,f'-'*180+'' '\n')

    x=0
    for comida in texto_comidas:
        if comida.get() !='0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t${int(comida.get())*precios_comida[x]}\n')
        x+=1
    x=0
    for bebida in texto_bebidas:
        if bebida.get() !='0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t${int(bebida.get())*precios_bebida[x]}\n')
        x+=1
    x=0
    for postres in texto_postres:
        if postres.get() !='0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postres.get()}\t${int(postres.get())*precios_postres[x]}\n')
        x+=1
    texto_recibo.insert(END,f'-'*180+'' '\n')
    texto_recibo.insert(END,f'Costo de la comida:\t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END,f'Costo de la bebida:\t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END,f'Costo del postre:\t\t\t{var_costo_postres.get()}\n')
    texto_recibo.insert(END,f'-'*180+'' '\n')
    texto_recibo.insert(END,f'Subtotal:\t\t\t{var_costo_subtotal.get()}\n')
    texto_recibo.insert(END,f'Impuestos:\t\t\t{var_costo_impuestos.get()}\n')
    texto_recibo.insert(END,f'Total:\t\t\t{var_costo_total.get()}\n')
    texto_recibo.insert(END,f'*'*153+'' '\n')
    texto_recibo.insert(END,f'Te esperamos pronto' '\n')

def guardar():
    info_recibo=texto_recibo.get(1.0,END)
    archivo=filedialog.asksaveasfile(mode='w',
                                     defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close
    messagebox.showinfo('Informacion','Su recibo ha sido guardado')

def resetear():
    texto_recibo.delete(0.1,END)
    for texto in texto_comidas:
        texto.set('0')
    for texto in texto_bebidas:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')
    for cuadro in cuadros_comidas:
        cuadro.set(state=DISABLED)
    for cuadro in cuadros_bebidas:
        cuadro.set(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.set(state=DISABLED)

    for v in variables_comidas:
        v.set(0)
    for v in variables_bebidas:
        v.set(0)
    for v in variables_postres:
        v.set(0)
        
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postres.set('')
    var_costo_subtotal.set('')
    var_costo_total.set('')
    var_costo_impuestos.set('')

#iniciar tkinter
aplicacion =  Tk()

#tamaño de la ventana
aplicacion.geometry('1600x680+0+0')

#titulo de la ventana
aplicacion.title("Nina's dinning - Invoicing System")

#color fondo
aplicacion.config(bg='bisque')

#evitar maximizar
#aplicacion.resizable(0,0)

#panel_superior
panel_superior  = Frame(aplicacion, bd=1,relief=FLAT)
panel_superior.pack(side=TOP)

#etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de facturacion',fg='azure',
                        font=('Dosis',58),bg='bisque',width=27)
etiqueta_titulo.grid(row=0,column=0)

#panel izquierdo
panel_izquierdo=Frame(aplicacion, bd=1,relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#panel costos 
panel_costos = Frame(panel_izquierdo,bd=1,relief=FLAT,bg='azure')
panel_costos.pack(side=BOTTOM)

#panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', fg='azure',font=('Dosis',30),bg='bisque',width=14, bd=1,relief=FLAT)
panel_comidas.pack(side=LEFT)

#panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='bebidas', fg='azure',font=('Dosis',30),bg='bisque',width=14, bd=1,relief=FLAT)
panel_bebidas.pack(side=LEFT)

#panel postres
panel_postres = LabelFrame(panel_izquierdo, text='postres', fg='azure',font=('Dosis',30),bg='bisque',width=14, bd=1,relief=FLAT)
panel_postres.pack(side=LEFT)

#panel derecha
panel_derecha=Frame(aplicacion, bd=1,relief=FLAT)
panel_derecha.pack(side=RIGHT)

#panel calculadora
panel_calculadora =Frame(panel_derecha, bd=1,relief=FLAT,bg='bisque')
panel_calculadora.pack()

#panel recibo
panel_recibo =Frame(panel_derecha, bd=1,relief=FLAT,bg='bisque')
panel_recibo.pack()

#panel botones
panel_botones =Frame(panel_derecha, bd=1,relief=FLAT,bg='bisque')
panel_botones.pack()


#lista de ptoductos
lista_comidas = ["Hamburguesa", "Pizza", "Sushi", "Ensalada César", "Tacos", "Pasta Alfredo", "Pollo a la Parrilla", "Burrito"]
lista_bebidas = ["Agua", "Refresco de Cola", "Jugo de Naranja", "Cerveza", "Vino tinto", "Café", "Té Verde", "Limonada"]
lista_postres = ["Pastel de Chocolate", "Helado de Vainilla", "Tarta de Manzana", "Brownie", "Flan", "Tiramisú", "Gelatina", "Crema Brulee"]

#generar items comida
variables_comidas = []
cuadros_comidas=[]
texto_comidas = []
contador = 0
for alimento in lista_comidas:
    #crear checkbuttons
    variables_comidas.append('')
    variables_comidas[contador]=IntVar()
    comida = Checkbutton(panel_comidas,
                         text=alimento.title(),
                         font=('Dosis',19,'bold'),
                         onvalue=1, 
                         offvalue=0,variable=variables_comidas[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)
    
    #crear los cuadros de entrada comida
    cuadros_comidas.append('')
    texto_comidas.append('')
    texto_comidas[contador]=StringVar()
    texto_comidas[contador].set('0')

    cuadros_comidas[contador] = Entry(panel_comidas,
                                      font=('Dosis',18,'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_comidas[contador])
    cuadros_comidas[contador].grid(row=contador,
                                   column=1)
    contador+=1





#generar items bebida
variables_bebidas = []
cuadros_bebidas = []
texto_bebidas =[]
contador = 0
for bebida in lista_bebidas:
    #crear checkbuttons
    variables_bebidas.append('')
    variables_bebidas[contador]=IntVar()
    bebidas = Checkbutton(panel_bebidas,
                          text=bebida.title(),
                          font=('Dosis',19,'bold'),
                          onvalue=1, 
                          offvalue=0,variable=variables_bebidas[contador],
                          command=revisar_check)
    bebidas.grid(row=contador,
                 column=0,
                 sticky=W)
    #crear los cuadros de entrada
    cuadros_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador]=StringVar()
    texto_bebidas[contador].set('0')
    cuadros_bebidas[contador]=Entry(panel_bebidas,
                                    font=('Dosis',18,'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_bebidas[contador])
    cuadros_bebidas[contador].grid(row=contador,
                                   column=1)
    contador+=1

#generar items postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postre in lista_postres:
    #crear checkbuttons
    variables_postres.append('')
    variables_postres[contador]=IntVar()
    postres = Checkbutton(panel_postres,
                          text=postre.title(),
                          font=('Dosis',19,'bold'),onvalue=1, 
                          offvalue=0,variable=variables_postres[contador],
                          command=revisar_check)
    postres.grid(row=contador,
                 column=0,
                 sticky=W)
    
    #crear los cuadros de entrada de postres
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador]=StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador]=Entry(panel_postres,
                                    font=('Dosis',18,'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,
                                   column=1)
    contador+=1

#variables
var_costo_comida=StringVar()
var_costo_bebida=StringVar()
var_costo_postres=StringVar()
var_costo_subtotal = StringVar()
var_costo_impuestos = StringVar()
var_costo_total = StringVar()

#etiquetas costos y campos entrada comida
etiqueta_costo_comida=Label(panel_costos,
                            text='Precio',
                            font=('Dosis',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_comida.grid(row=0,column=0,padx=41)
texto_costo_comidas = Entry(panel_costos,
                            font=('Dosis',12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_comida)
texto_costo_comidas.grid(row=0,
                         column=1)

#etiquetas costos y campos entrada bebida
etiqueta_costo_bebida=Label(panel_costos,
                            text='Precio',
                            font=('Dosis',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_bebida.grid(row=1,column=0,padx=41)
texto_costo_bebidas = Entry(panel_costos,
                            font=('Dosis',12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_bebida)
texto_costo_bebidas.grid(row=1,
                         column=1)
#etiquetas costos y campos entrada postres
etiqueta_costo_postres=Label(panel_costos,
                            text='Precio',
                            font=('Dosis',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_postres.grid(row=2,column=0,padx=41)
texto_costo_postres = Entry(panel_costos,
                            font=('Dosis',12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_postres)
texto_costo_postres.grid(row=2,
                         column=1)
#etiquetas costos y campos entrada subtotal
etiqueta_costo_subtotal=Label(panel_costos,
                            text='Subtotal',
                            font=('Dosis',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_subtotal.grid(row=3,column=0,padx=41)
texto_costo_subtotal = Entry(panel_costos,
                            font=('Dosis',12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_subtotal)
texto_costo_subtotal.grid(row=3,
                         column=1)
#etiquetas costos y campos entrada impuestos
etiqueta_costo_impuestos=Label(panel_costos,
                            text='Impuestos',
                            font=('Dosis',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_impuestos.grid(row=4,column=0,padx=41)
texto_costo_impuestos = Entry(panel_costos,
                            font=('Dosis',12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_impuestos)
texto_costo_impuestos.grid(row=4,
                         column=1)
#etiquetas costos y campos entrada total
etiqueta_costo_total=Label(panel_costos,
                            text='Total a pagar',
                            font=('Dosis',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_total.grid(row=5,column=0,padx=41)
texto_costo_total = Entry(panel_costos,
                            font=('Dosis',12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_total)
texto_costo_total.grid(row=5,
                         column=1)

#botones
botones = ['total','recibo','guardar','resetear']
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis',14,'bold'),
                   fg='black',
                   bg='azure',
                   bd=1,
                   width=9)
    botones_creados.append(boton)
    boton.grid(row=0,
               column=columnas)
    columnas+=1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)
#area recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis',12,'bold'),
                    bd=1,
                    width=102,
                    height=20)
texto_recibo.grid(row=0,
                  column=0)

    
#calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis',16,'bold'),
                          width=72,
                          bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = [
    "7",'8','9','+',
    '4','5','6','-',
    '1','2','3','x',
    'Total',"Borrar",'0','/'
]
botones_guardados=[]

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis',16,'bold'),
                   fg='black',
                   bg='Azure',
                   bd=1,
                   width=18)
    botones_guardados.append(boton)
    boton.grid(row=fila,
               column=columna)
    if columna == 3:
        fila+=1
    columna+=1
    if columna == 4:
        columna =0    

botones_guardados[0].config(command=lambda:click_boton('7'))
##command sirve para agregar una funcion
##lambda sirve para poder pasarle un argumento a la funcion
botones_guardados[1].config(command=lambda:click_boton('8'))
botones_guardados[2].config(command=lambda:click_boton('9'))
botones_guardados[3].config(command=lambda:click_boton('+'))
botones_guardados[4].config(command=lambda:click_boton('4'))
botones_guardados[5].config(command=lambda:click_boton('5'))
botones_guardados[6].config(command=lambda:click_boton('6'))
botones_guardados[7].config(command=lambda:click_boton('-'))
botones_guardados[8].config(command=lambda:click_boton('1'))
botones_guardados[9].config(command=lambda:click_boton('2'))
botones_guardados[10].config(command=lambda:click_boton('3'))
botones_guardados[11].config(command=lambda:click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda:click_boton('0'))
botones_guardados[15].config(command=lambda:click_boton('/'))
































#evitar que la pantalla se cierre
aplicacion.mainloop()
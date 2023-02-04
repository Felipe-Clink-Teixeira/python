import tkinter
from molmass import Formula
from tkinter import *

class app():
    def __init__(self):
        self.NReg = 1
        self.NProd = 1
        self.pagina1 = Tk()
        self.pagina1.geometry('1200x600')
        self.pagina1.configure(background='#808080')
        self.texto = Label(self.pagina1,text = 'Estequiometria do capeta',background= '#C0C0C0',foreground='#000000')
        self.texto.place(x= 20,y=50,width=200,height=30)
        self.texto7 = Label(self.pagina1,text = self.NReg,background= '#C0C0C0',foreground='#000000')
        self.texto7.place(x= 59,y=150,width=25,height=26)
        self.texto1 = Label(self.pagina1,text = 'Insira o reagente',background= '#C0C0C0',foreground='#000000',width=200,height=30)
        self.texto1.place(x=55,y=112,width=175,height=25)
        self.sub_reg1 = Entry(self.pagina1)
        self.sub_reg1.place(x=110,y=150)
        self.texto8 = Label(self.pagina1,text = self.NProd,background= '#C0C0C0',foreground='#000000')
        self.texto8.place(x= 59,y=230,width=25,height=26)
        self.texto2 = Label(self.pagina1,text = 'Insira o produto',background= '#C0C0C0',foreground='#000000',width=200,height=30)
        self.texto2.place(x=55,y=182,width=175,height=25)
        self.sub_prod = Entry(self.pagina1)
        self.sub_prod.place(x=110,y=230)
        self.botao1 = Button(self.pagina1,text = 'Inserir informação de produto',command=self.produto1)
        self.botao1.place(x=270,y=150)
        self.botao2 = Button(self.pagina1,text='Inserir informação de reagente',command=self.reg1)
        self.botao2.place(x=270,y=190)
        self.botao5 = Button(self.pagina1,text='Inserir informações sobre pureza e rendimento',command=self.pur_rend)
        self.botao5.place(x=270,y=230)
        self.botao13 = Button(self.pagina1,text='Descobrir pureza',command=self.src_pur)
        self.botao13.place(x=450,y=150)
        self.botao16 = Button(self.pagina1,text='Descobrir rendimento',command=self.src_rend)
        self.botao16.place(x=450,y=190)
        self.botao18 = Button(self.pagina1,text='Problemas envolvendo volume de gás',background= '#B0C4DE',command=self.gas)
        self.botao18.place(x=535,y=230)
        self.botao9 = Button(self.pagina1,text='+',command=self.contagem_aditiva_reg)
        self.botao9.place(x=85,y=150)
        self.botao10 = Button(self.pagina1,text='-',command=self.contagem_subtrativa_reg)
        self.botao10.place(x=45,y=150)
        self.botao11 = Button(self.pagina1,text='+',command=self.contagem_aditiva_prod)
        self.botao11.place(x=85,y=230)
        self.botao12 = Button(self.pagina1,text='-',command=self.contagem_subtrativa_prod)
        self.botao12.place(x=45,y=230)
    def contagem_aditiva_reg (self):
        self.NReg = self.NReg + 1
        self.texto7 = Label(self.pagina1,text = self.NReg,background= '#C0C0C0',foreground='#000000')
        self.texto7.place(x= 59,y=150,width=25,height=26)
    def contagem_subtrativa_reg (self):
        self.NReg = self.NReg - 1
        self.texto7 = Label(self.pagina1,text = self.NReg,background= '#C0C0C0',foreground='#000000')
        self.texto7.place(x= 59,y=150,width=25,height=26)
    def contagem_aditiva_prod (self):
        self.NProd = self.NProd + 1
        self.texto8 = Label(self.pagina1,text = self.NProd,background= '#C0C0C0',foreground='#000000')
        self.texto8.place(x= 59,y=230,width=25,height=26)
    def contagem_subtrativa_prod (self):
        self.NProd = self.NProd - 1
        self.texto8 = Label(self.pagina1,text = self.NProd,background= '#C0C0C0',foreground='#000000')
        self.texto8.place(x= 59,y=230,width=25,height=26)
    def pur_rend(self):
        self.botao1.destroy()
        self.botao2.destroy()
        self.botao5.destroy()
        self.botao13.destroy()
        self.botao18.destroy()
        self.texto5 = Label(self.pagina1,text = 'Nível de pureza',background= '#C0C0C0',foreground='#000000',width=200,height=30)
        self.texto5.place(x=252,y=195,width=89,height=25)
        self.info_pur = Entry(self.pagina1,background='#C0C0C0',foreground='#000000')
        self.info_pur.place(x=270,y=230,width=50,height=30)
        self.texto6 = Label(self.pagina1,text = 'Nível de rendimento',background= '#C0C0C0',foreground='#000000',width=200,height=30)
        self.texto6.place(x=240,y=309,width=113,height=25)
        self.info_rend = Entry(self.pagina1,background='#C0C0C0',foreground='#000000')
        self.info_rend.place(x=270,y=270,width=50,height=30)
        self.botao6 = Button(self.pagina1,text='Inserir informações sobre produto',command=self.produto2)
        self.botao6.place(x=350,y=270)
        self.botao7 = Button(self.pagina1,text='Inserir informações sobre reagente',command=self.reg2)
        self.botao7.place(x=350,y=230)
    def src_pur(self):
        self.botao1.destroy()
        self.botao2.destroy()
        self.botao5.destroy()
        self.botao13.destroy()
        self.botao16.destroy()
        self.botao18.destroy()
        self.texto6 = Label(self.pagina1,text = 'informação do reagente',background= '#C0C0C0',foreground='#000000',width=200,height=30)
        self.texto6.place(x=260,y=150,height=25,width=180)
        self.info_reg3 = Entry(self.pagina1,background='#C0C0C0',foreground='#000000')
        self.info_reg3.place(x=450,y=150,width=70,height=30)
        self.texto6 = Label(self.pagina1,text ='Informação do produto',background= '#C0C0C0',foreground='#000000',width=200,height=30)
        self.texto6.place(x=260,y=190,height=25,width=180)
        self.info_prod3 = Entry(self.pagina1,background='#C0C0C0',foreground='#000000')
        self.info_prod3.place(x=450,y=190,width=70,height=30)
        self.botao14 = Button(self.pagina1,text= 'Finalizar',command=self.finalizar5)
        self.botao14.place(x= 530,y=170)
    def src_rend(self):
        self.botao1.destroy()
        self.botao2.destroy()
        self.botao5.destroy()
        self.botao16.destroy()
        self.botao13.destroy()
        self.botao18.destroy()
        self.texto6 = Label(self.pagina1,text = 'informação do reagente',background= '#C0C0C0',foreground='#000000',width=200,height=30)
        self.texto6.place(x=260,y=150,height=25,width=180)
        self.info_reg4 = Entry(self.pagina1,background='#C0C0C0',foreground='#000000')
        self.info_reg4.place(x=450,y=150,width=70,height=30)
        self.texto6 = Label(self.pagina1,text ='Informação do produto',background= '#C0C0C0',foreground='#000000',width=200,height=30)
        self.texto6.place(x=260,y=190,height=25,width=180)
        self.info_prod4 = Entry(self.pagina1,background='#C0C0C0',foreground='#000000')
        self.info_prod4.place(x=450,y=190,width=70,height=30)
        self.botao15 = Button(self.pagina1,text= 'Finalizar',command=self.finalizar4)
        self.botao15.place(x= 530,y=170)
    def produto2 (self):
        self.botao7.destroy()
        self.botao6.destroy()
        self.info_prod1 = Entry(self.pagina1,background='#C0C0C0',foreground='#000000')
        self.info_prod1.place(x=350,y=270,width=70,height=30)
        self.botao8 = Button(self.pagina1,text='Finalizar',command=self.finalizar3)
        self.botao8.place(x=440,y=270)
    def reg2(self):
        self.botao7.destroy()
        self.botao6.destroy()
        self.info_reg1 = Entry(self.pagina1,background='#C0C0C0',foreground='#000000')
        self.info_reg1.place(x=350,y=230,width=70,height=30)
        self.botao8 = Button(self.pagina1,text='Finalizar',command=self.finalizar2)
        self.botao8.place(x=440,y=230)
    def gas(self):
        self.botao1.destroy()
        self.botao2.destroy()
        self.botao5.destroy()
        self.botao16.destroy()
        self.botao13.destroy()
        self.botao18.destroy()
        self.botao19 = Button(self.pagina1,text= 'Dentro da CNTP',command=self.InCNTP)
        self.botao19.place(x=535,y=230)
        self.botao20 = Button(self.pagina1,text= 'Fora da CNTP',command=self.finalizar4)
        self.botao20.place(x=535,y=270)
    def InCNTP(self):
        self.botao19.destroy()
        self.botao20.destroy()
        self.botao21 = Button(self.pagina1,text= 'Descobrir volume',command=self.finalizar4)
        self.botao21.place(x=535,y=230)
        self.botao22 = Button(self.pagina1,text= 'Descobrir pressão',command=self.finalizar4)
        self.botao22.place(x=535,y=270)
    def reg1(self):
        self.botao1.destroy()
        self.botao2.destroy()
        self.botao5.destroy()
        self.botao13.destroy()
        self.botao16.destroy()
        self.botao18.destroy()
        self.info_reg = Entry(self.pagina1,background='#C0C0C0',foreground='#000000')
        self.info_reg.place(x=270,y=190)
        self.botao4 = Button(self.pagina1,text='Finalizar',command=self.finalizar1)
        self.botao4.place(x=410,y=190)
    def produto1(self):
        self.botao1.destroy()
        self.botao2.destroy()
        self.botao5.destroy()
        self.botao13.destroy()
        self.botao16.destroy()
        self.botao18.destroy()
        self.texto4 = Label(self.pagina1,text = 'Informação dada sobre produto',background= '#C0C0C0',foreground='#000000',width=200,height=30)
        self.texto4.place(x=270,y=182,width=175,height=25)
        self.info_prod = Entry(self.pagina1,background='#C0C0C0',foreground='#000000')
        self.info_prod.place(x=270,y=150)
        self.botao3 = Button(self.pagina1,text='Finalizar',command=self.finalizar)
        self.botao3.place(x=400,y=150)
    def finalizar(self):
        self.f1 = Formula(self.sub_reg1.get())
        self.f2 = Formula(self.sub_prod.get())
        self.m1 = self.f1.mass * self.NReg
        self.m2 = self.f2.mass * self.NProd
        self.info_valor = float(self.info_prod.get())
        self.r1= ((self.info_valor*self.m1)/self.m2)
        self.r1 = str(self.r1)
        self.texto3 = Label(self.pagina1,text = self.r1 + ' g' ,background= '#C0C0C0',foreground='#000000')
        self.texto3.place(x=470,y=145,height=30)
    def finalizar1(self):
        self.f1 = Formula(self.sub_reg1.get())
        self.f2 = Formula(self.sub_prod.get())
        self.m1 = self.f1.mass * self.NReg
        self.m2 = self.f2.mass * self.NProd
        self.info_valor2 = float(self.info_reg.get())
        self.r2 = (self.info_valor2*self.m2)/self.m1
        self.r2 = str(self.r2)
        self.texto3 = Label(self.pagina1,text = self.r2 + ' g',background= '#C0C0C0',foreground='#000000')
        self.texto3.place(x=480,y=190,height=30)
    def finalizar2 (self):
        self.f1 = Formula(self.sub_reg1.get())
        self.f2 = Formula(self.sub_prod.get())
        self.m1 = self.f1.mass * self.NReg
        self.m2 = self.f2.mass * self.NProd
        self.info_pur_valor = float(self.info_pur.get())/100
        self.info_rend_valor = float(self.info_rend.get())/100
        self.info_valor3 = float(self.info_reg1.get())
        self.r3 = (self.info_valor3*self.m2* self.info_rend_valor)/self.m1
        self.r3 = str(self.r3)
        self.texto3 = Label(self.pagina1,text = self.r3 + ' g' ,background= '#C0C0C0',foreground='#000000')
        self.texto3.place(x=515,y=230,width=180,height=30)
    def finalizar3 (self):
        self.f1 = Formula(self.sub_reg1.get())
        self.f2 = Formula(self.sub_prod.get())
        self.m1 = self.f1.mass * self.NReg
        self.m2 = self.f2.mass * self.NProd
        self.info_pur_valor = float(self.info_pur.get())/100
        self.info_rend_valor = float(self.info_rend.get())/100
        self.info_valor4 = float(self.info_prod1.get())
        self.r4 = (self.info_valor4*self.m1*self.info_pur_valor)/self.m2
        self.r4 = str(self.r4)
        self.texto3 = Label(self.pagina1,text = self.r4 + ' g' ,background= '#C0C0C0',foreground='#000000')
        self.texto3.place(x=515,y = 270,height=30)
    def finalizar4 (self):
        self.f1 = Formula(self.sub_reg1.get())
        self.f2 = Formula(self.sub_prod.get())
        self.m1 = self.f1.mass * self.NReg
        self.m2 = self.f2.mass * self.NProd
        self.reg_scr_rend = float(self.info_reg4.get())
        self.prod_scr_rend = float(self.info_prod4.get())
        self.valorreal = (self.reg_scr_rend*self.m2)/self.m1
        self.r6 = (100*self.prod_scr_rend)/self.valorreal
        self.r6 = str(self.r6)
        self.texto9 = Label(self.pagina1,text = self.r6 + ' g' ,background= '#C0C0C0',foreground='#000000')
        self.texto9.place(x= 590,y=170,height=30)
    def finalizar5 (self):
        self.f1 = Formula(self.sub_reg1.get())
        self.f2 = Formula(self.sub_prod.get())
        self.m1 = self.f1.mass * self.NReg
        self.m2 = self.f2.mass * self.NProd
        self.reg_scr_pur = float(self.info_reg3.get())
        self.prod_scr_pur = float(self.info_prod3.get())
        self.r5 = ((self.m1*self.prod_scr_pur)/(self.reg_scr_pur*self.m2))*100
        self.r5 = str(self.r5)
        self.texto10 = Label(self.pagina1,text = self.r5 + ' g' ,background= '#C0C0C0',foreground='#000000')
        self.texto10.place(x= 590,y=170,height=30)
    def start(self):
        self.pagina1.mainloop()

app().start()
    
    

        
    





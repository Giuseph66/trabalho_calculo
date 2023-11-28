import tkinter as tk
from tkinter import ttk
from tkinter import *
import matplotlib.pyplot as plt
from fractions import Fraction
import numpy as np
from cmath import *
import cmath

class trabalho():
    def __init__(self):
        self.dunf=tk.Tk()
        self.dunf.geometry("800x500+200+100")
        self.dunf.title("Geogebra-lite")
        self.dunf.iconbitmap("icone.ico")
        self.dunf.resizable(0,0)
        self.ini()
        self.dunf.mainloop()
    def ini(self):
        self.fundo = LabelFrame(self.dunf, bg="#d2f5f7",width=800,height=500,bd=3,labelanchor="n")
        self.fundo.place(x=0,y=0)
        self.txt=Label(self.fundo, bg="#d2f5f7",text="Função:",width=10,height=1,font="Arial 12 bold",bd=3)
        self.txt.place(x=2,y=2)
        self.funcao_=Entry(self.fundo, bg="white",width=20,font="Arial 12 bold",fg="black")
        self.funcao_.bind("<Return>",lambda event:self.est_ini.focus())
        self.funcao_.bind("<KeyRelease>",lambda event:self.test())
        self.funcao_.place(x=1,y=30,height=25)
        self.error=StringVar()
        self.error.set("0.000001")
        self.txt=Label(self.fundo, bg="#d2f5f7",text="Error:",width=10,height=1,font="Arial 12 bold",bd=3)
        self.txt.place(x=2,y=60)
        self.txt=Label(self.fundo, bg="#d2f5f7",text="(Recomendado)",width=12,height=1,font="Arial 10 bold",bd=3)
        self.txt.place(x=145,y=100)
        self.txt=Label(self.fundo, bg="#d2f5f7",text="(Demora +)",width=12,height=1,font="Arial 10 bold",bd=3)
        self.txt.place(x=400,y=100)
        self.A=Radiobutton(self.fundo,font="Arial 10 bold",variable=self.error,value="1",text="1",bg="#d2f5f7",bd=1,fg="black")
        self.A.place(x=2,y=80)
        self.B=Radiobutton(self.fundo,font="Arial 10 bold",variable=self.error,value="0.01",text="0.01",bg="#d2f5f7",bd=1,fg="black")
        self.B.place(x=50,y=80)
        self.C=Radiobutton(self.fundo,font="Arial 10 bold",variable=self.error,value="0.000001",text="0.000001",bg="#d2f5f7",bd=1,fg="black")
        self.C.place(x=150,y=80)
        self.D=Radiobutton(self.fundo,font="Arial 10 bold",variable=self.error,value="0.00000000001",text="0.00000000001",bg="#d2f5f7",bd=1,fg="black")
        self.D.place(x=250,y=80)
        self.E=Radiobutton(self.fundo,font="Arial 10 bold",variable=self.error,value="0.00000000000000001",text="0.00000000000000001",bg="#d2f5f7",bd=1,fg="black")
        self.E.place(x=400,y=80)
        self.funcao_.focus()
        self.Grafico=Button(self.fundo,font="Arial 8 bold",text="Gerar Grafico(Teste)",command=self.atalhu,bg="white",bd=2,fg="black",height=1,width=20)
        self.Grafico.place(x=430,y=150)

        self.txt=Label(self.fundo, bg="#d2f5f7",text="Estimativas:",width=10,height=1,font="Arial 12 bold",bd=3)
        self.txt.place(x=2,y=150)
        self.f_call=LabelFrame(self.fundo, bg="#baf7f3",width=600,height=315,bd=3,labelanchor="n")
        self.f_call.place(x=1,y=180)
        self.f_resp=LabelFrame(self.f_call, bg="#baf7f3",width=590,height=248,bd=0,labelanchor="n")
        self.f_resp.place(x=1,y=60)
        self.txt=Label(self.f_call, bg="#baf7f3",text="Estimativas Inicial :",width=15,height=1,font="Arial 12 bold",bd=3)
        self.txt.place(x=2,y=2)
        self.txt=Label(self.f_call, bg="#baf7f3",text="Estimativas Final :",width=15,height=1,font="Arial 12 bold",bd=3)
        self.txt.place(x=200,y=2)
        self.est_ini=Entry(self.f_call, bg="white",width=5,font="Arial 10 bold",fg="black")
        self.est_ini.bind("<Return>",lambda event:self.est_final.focus())
        self.est_ini.bind("<Escape>",lambda event:self.funcao_.focus())
        self.est_ini.place(x=51,y=30,height=20)
        self.est_final=Entry(self.f_call, bg="white",width=5,font="Arial 10 bold",fg="black")
        self.est_final.bind("<Return>",lambda event:self.call.focus())
        self.est_final.bind("<Escape>",lambda event:self.est_ini.focus())
        self.est_final.place(x=250,y=30,height=20)
        self.call=Button(self.f_call,font="Arial 10 bold",text="Calcular",bg="white",bd=2,fg="black",command=self.sla1,height=1,width=10)
        self.call.bind("<Return>",lambda event:self.sla1())
        self.call.bind("<Escape>", lambda event: self.est_final.focus())
        self.call.place(x=485,y=2)

        self.f_r=LabelFrame(self.dunf, bg="#c4ffe3",width=200,height=495,bd=3,labelanchor="n")
        self.f_r.place(x=600,y=0)
        self.espo=Button(self.f_r, bg="white",text="Expoente = **",width=18,command=self.inserir_esp,font="Arial 12 bold",fg="black")
        self.espo.place(x=1,y=0)
        self.sen=Button(self.f_r, bg="white",text="Seno = sen()",width=18,command=self.inserir_sen,font="Arial 12 bold",fg="black")
        self.sen.place(x=1,y=38)
        self.cos=Button(self.f_r, bg="white",text="Cosseno = cos()",width=18,command=self.inserir_cos,font="Arial 12 bold",fg="black")
        self.cos.place(x=1,y=76)
        self.tang=Button(self.f_r, bg="white",text="Tang = tan()",width=18,command=self.inserir_tang,font="Arial 12 bold",fg="black")
        self.tang.place(x=1,y=114)
        self.loga=Button(self.f_r, bg="white",text="Log = log()",width=18,command=self.inserir_loga,font="Arial 12 bold",fg="black")
        self.loga.place(x=1,y=152)
        self.oler=Button(self.f_r, bg="white",text="e = e",width=18,command=self.inserir_e,font="Arial 12 bold",fg="black")
        self.oler.place(x=1,y=190)
        self.raiz=Button(self.f_r, bg="white",text="Raiz = raiz",width=18,command=self.inserir_raix,font="Arial 12 bold",fg="black")
        self.raiz.place(x=1,y=228)
        self.pi=Button(self.f_r, bg="white",text="pi = π",width=18,command=self.inserir_pi,font="Arial 12 bold",fg="black")
        self.pi.place(x=1,y=266)
        self.Modulo=Button(self.f_r, bg="white",text="Modulo = abs()",width=18,command=self.inserir_abs,font="Arial 12 bold",fg="black")
        self.Modulo.place(x=1,y=304)
        self.mais=Button(self.f_r, bg="white",text="Mais",width=18,command=self.inserir_mais,font="Arial 12 bold",fg="black")
        self.mais.place(x=1,y=456)
    def inserir_esp(self):
        self.funcao_.insert(100,"**")
    def inserir_sen(self):
        self.funcao_.insert(100,"sen()")
    def inserir_cos(self):
        self.funcao_.insert(100,"cos()")
    def inserir_tang(self):
        self.funcao_.insert(100,"tan()")
    def inserir_loga(self):
        self.funcao_.insert(100,"log()")
    def inserir_e(self):
        self.funcao_.insert(100,"e")
    def inserir_raix(self):
        self.funcao_.insert(100,"raiz")
    def inserir_pi(self):
        self.funcao_.insert(100,"π")
    def inserir_abs(self):
        self.funcao_.insert(100,"abs()")
        

    def inserir_mais(self):
        self.dunf.geometry("1000x500+200+100")
        self.mais.destroy()
        self.f_r.configure(width=400)
        self.f_call.configure(width=1000)
        self.fundo.configure(width=1000)
        self.oler.place(x=1,y=38)
        self.raiz.place(x=1,y=76)
        self.loga.place(x=1,y=114)
        self.pi.place(x=1,y=152)
        self.Modulo.place(x=1,y=190)
        self.sen.place(x=201,y=0)
        self.cos.place(x=201,y=38)
        self.tang.place(x=201,y=76)
        self.asin=Button(self.f_r, bg="white",text=" Arcosseno = asin()",width=18,command=self.inserir_asin,font="Arial 12 bold",fg="black")
        self.asin.place(x=201,y=114)
        self.acos=Button(self.f_r, bg="white",text="Arcocosseno = acos()",width=18,command=self.inserir_acos,font="Arial 12 bold",fg="black")
        self.acos.place(x=201,y=152)
        self.atan=Button(self.f_r, bg="white",text="Arcotangente = atan()",width=18,command=self.inserir_atan,font="Arial 12 bold",fg="black")
        self.atan.place(x=201,y=190)

        self.sinh=Button(self.f_r, bg="white",text="Seno hiperbólico = sinh()",width=30,command=self.inserir_sinh,font="Arial 12 bold",fg="black")
        self.sinh.place(x=44,y=228)
        self.cosh=Button(self.f_r, bg="white",text="Cosseno hiperbólico = cosh()",width=30,command=self.inserir_cosh,font="Arial 12 bold",fg="black")
        self.cosh.place(x=44,y=266)
        self.tanh=Button(self.f_r, bg="white",text="Tangente hiperbólica = tanh()",width=30,command=self.inserir_tanh,font="Arial 12 bold",fg="black")
        self.tanh.place(x=44,y=304)
        self.asinh=Button(self.f_r, bg="white",text="Arcoseno hiperbólico = asinh()",width=30,command=self.inserir_asinh,font="Arial 12 bold",fg="black")
        self.asinh.place(x=44,y=342)
        self.acosh=Button(self.f_r, bg="white",text="Arcocosseno hiperbólico = acosh()",width=30,command=self.inserir_acosh,font="Arial 12 bold",fg="black")
        self.acosh.place(x=44,y=380)
        self.atanh=Button(self.f_r, bg="white",text="Artangente hiperbólica = atanh()",width=30,command=self.inserir_atanh,font="Arial 12 bold",fg="black")
        self.atanh.place(x=44,y=418)

        self.Menos=Button(self.f_r, bg="white",text="Menos",width=38,command=self.inserir_Menos,font="Arial 12 bold",fg="black")
        self.Menos.place(x=1,y=456)
    def inserir_Menos(self):
        self.dunf.geometry("800x500+200+100")
        self.Menos.destroy()
        self.sinh.destroy()
        self.cosh.destroy()
        self.tanh.destroy()
        self.asinh.destroy()
        self.acosh.destroy()
        self.atanh.destroy()
        self.sen.place(x=1,y=38)
        self.cos.place(x=1,y=76)
        self.tang.place(x=1,y=114)
        self.loga.place(x=1,y=152)
        self.oler.place(x=1,y=190)
        self.raiz.place(x=1,y=228)
        self.pi.place(x=1,y=266)
        self.Modulo.place(x=1,y=304)
        self.mais=Button(self.f_r, bg="white",text="Mais",width=18,command=self.inserir_mais,font="Arial 12 bold",fg="black")
        self.mais.place(x=1,y=456)

    def inserir_asin(self):
        self.funcao_.insert(100,"asin()")
    def inserir_acos(self):
        self.funcao_.insert(100,"acos()")
    def inserir_atan(self):
        self.funcao_.insert(100,"atan()")
    def inserir_sinh(self):
        self.funcao_.insert(100,"sinh()")
    def inserir_cosh(self):
        self.funcao_.insert(100,"cosh()")
    def inserir_tanh(self):
        self.funcao_.insert(100,"tanh()")
    def inserir_asinh(self):
        self.funcao_.insert(100,"asinh()")
    def inserir_acosh(self):
        self.funcao_.insert(100,"acosh()")
    def inserir_atanh(self):
        self.funcao_.insert(100,"atanh()")

    def dele(self, x):
        self.expr_str = self.funcao_.get() 
        todas_fun = {
            'x': x, 
            'sen': np.sin,
            'cos': np.cos,
            'tan': np.tan,
            'asin': np.arcsin,
            'acos': np.arccos,
            'atan': np.arctan,
            'sinh': np.sinh,
            'cosh': np.cosh,
            'tanh': np.tanh,
            'asinh': np.arcsinh,
            'acosh': np.arccosh,
            'atanh': np.arctanh,
            'log': np.log10,
            'e': np.exp(1),
            'raiz': np.sqrt,
            'π': np.pi, 
            'pi': np.pi,
        }
        return eval(self.expr_str, todas_fun)

    def atalhu(self):
        funcao = self.dele
        self.desenha_func(funcao)
    def desenha_func(self, func, x_range=(-200, 200), num_points=10000):
        x_values = np.linspace(x_range[0], x_range[1], num_points)
        y_values = func(x_values)
        plt.plot(x_values, y_values)
        plt.axhline(0, color='black', linewidth=1)  
        plt.axvline(0, color='red', linewidth=1)
        plt.title(f"Gráfico da Função: {self.expr_str}")
        plt.xlabel("Eixo X")
        plt.ylabel("Eixo Y")
        plt.grid(True)
        plt.axis('equal')  
        plt.legend("FXY")
        plt.xlim(-10,10)  
        plt.ylim(-10, 10) 
        plt.show()
    def sla1(self):
        self.apaga()
        self.call.config(relief=tk.SUNKEN)
        _ini_ = self.est_ini.get()
        _final = self.est_final.get()
        self.ini_ = Fraction(_ini_)
        self.final = Fraction(_final)
        tamanho=(abs(self.ini_)+abs(self.final))*10
        canvas = tk.Canvas(self.f_resp,bg="#baf7f3")
        canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        scrollbar_y = ttk.Scrollbar(self.f_call, orient="vertical", command=canvas.yview)
        scrollbar_y.place(relx=0, rely=0.1, relheight=0.9)
        self.f_resp.update()
        canvas.configure(yscrollcommand=scrollbar_y.set)
        f_scrool = tk.LabelFrame(canvas, bg="#baf7f3", width=590, height=tamanho, bd=0)
        canvas.create_window((0, 0), window=f_scrool, anchor="nw")
        f_scrool.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))
        self.carregando = ttk.Progressbar(self.f_resp, length=550, mode="determinate")
        self.carregando.place(x=20, y=225)
        y = 2
        me = min(self.ini_, self.final)
        ma = max(self.ini_, self.final)
        ac = False
        while True:
            if me > ma:
                break
            self.carregando["maximum"] = ma
            self.carregando["value"] = me
            self.f_resp.update()
            va = me
            me += 0.3
            self.fi = self.funcao(va)
            fd = self.funcao(me)
            if fd.real * self.fi.real < 0:
                if fd.imag and self.fi.imag:
                    print("img")
                else:
                    raiz = self.encontrar_raiz(float(va), float(me))
                    qnt, erru, raix = raiz
                    txt = tk.Label(f_scrool, bg="#baf7f3", text=f'Tentativas = {qnt} , erro = {abs(erru):.11f} , Raiz aproximada = {raix:.20f}', width=70, height=1, font="Arial 10 bold", bd=3)
                    txt.place(x=5, y=y)
                    y += 30
                    print(f"raiz entre {va} e {me}")
                    print(f"A raiz  da função é aproximadamente {raix:.20f}.\n")
                    ac = True
            else:
                continue
        if ac:
            print("e")
        else:
            txt = tk.Label(self.f_resp, bg="#baf7f3", text=f'Os valores entre {self.ini_} e {self.final} estão fora da possível raiz da função {self.funcao_.get()}. \nTente novamente.', width=60, height=2, font="Arial 13 bold", bd=3)
            txt.place(x=1, y=30)
        self.call.config(relief=tk.RAISED)
    def test(self):
        _ini_=-100
        _final=100
        self.ini_=Fraction(_ini_)
        self.final=Fraction(_final)
        cont=0
        try:
            cont+=1
            me=min(self.ini_,self.final)
            ma=max(self.ini_,self.final)
            raiz=False
            while True:
                if me>ma:
                    break
                va=me
                me+=0.3
                self.fi = self.funcao(va)
                fd = self.funcao(me)
                if fd.real * self.fi.real <0:
                    if fd.imag and self.fi.imag:
                        print("img")
                    else:
                        raiz= True
                        break
        except:
            raiz="sla"
        if raiz== True:
            self.resul=Label(self.fundo, bg="green",text=f'✔',fg="white",width=1,height=1,font="Arial 10 bold",bd=3)
            self.resul.place(x=190,y=30)
        elif raiz=="sla":
            self.resul=Label(self.fundo, bg="black",text=f'✘',fg="white",width=1,height=1,font="Arial 10 bold",bd=3)
            self.resul.place(x=190,y=30)
        else:
            self.resul=Label(self.fundo, bg="red",text=f'✘',fg="black",width=1,height=1,font="Arial 10 bold",bd=3)
            self.resul.place(x=190,y=30)
    def apaga(self):
        self.f_resp.destroy()
        self.f_resp=LabelFrame(self.f_call, bg="#baf7f3",width=590,height=248,bd=0,labelanchor="n")
        self.f_resp.place(x=1,y=60)
    def funcao(self, x): 
        if np.all(x == 0):
            x = -0.00000000001 
        self.expr_str = self.funcao_.get() 
        todas_fun = {'x': x, 
    'sen': cmath.sin,
    'cos': cmath.cos,
    'tan': cmath.tan,
    'asin': cmath.asin,
    'acos': cmath.acos,
    'atan': cmath.atan,
    'sinh': cmath.sinh,
    'cosh': cmath.cosh,
    'tanh': cmath.tanh,
    'asinh': cmath.asinh,
    'acosh': cmath.acosh,
    'atanh': cmath.atanh,
    'log': cmath.log10,
    'e': cmath.exp(1),
    'raiz': cmath.sqrt,
    'π': cmath.pi, 
    'pi': cmath.pi,}
        return  eval(self.expr_str,todas_fun)
    def encontrar_raiz(self, a, b):
        cnt = 0
        c = 0
        erro=float(self.error.get())
        while True:
            c = (a + b) / 2

            fc = self.funcao(c)
            e = b - a
            if abs(e) < erro:
                break
            if self.fi.real * fc.real < 0:
                b = c
            else:
                a = c
            cnt += 1
            if cnt > 5000:
                break
        return cnt,e,c
trabalho()
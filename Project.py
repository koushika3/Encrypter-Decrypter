from tkinter import *
from caesarcipher import CaesarCipher


def s1():
    def b():
        if(ch.get()==1):
            def morse():
                import morseCipher
                c=Toplevel()
                c.geometry('300x100')
                c.title("MORSE ENCODER")
                txt=exp.encrypt(mc1.get())
                S33=Label(c,text="Output After Encoding",font=("Centaur",20)).grid(row=2,column=0)
                out=Label(c,text=txt,font=("Candara",15))
                out.grid(row=4,column=0)
                but2=Button(c,text='Close',bg='black',fg='white',command=c.destroy).grid(row=5,column=0,pady=4)
            mc=Tk()
            mc.geometry('400x100')
            mc.title("MORSE ENCRYPTOR")
            S21=Label(mc,text="Input",font=("Centaur",20)).grid(column=0,row=0)
            mc1=Entry(mc)
            mc1.grid(column=1,row=0)
            but=Button(mc,text='Convert',command=morse).grid(row=3,column=1,pady=4)
            but3=Button(mc,text='Cancel',bg='black',fg='white',command=mc.destroy).grid(row=5,column=1)
            

        elif(ch.get()==2):
            def caesar():
                c=Toplevel()
                c.geometry('300x100')
                c.title("CAESAR ENCODER")
                cip=CaesarCipher(cc1.get(),offset=int(cc2.get()))
                txt=cip.encoded
                S33=Label(c,text="Output After Encoding",font=("Centaur",20)).grid(column=0,row=2)
                out=Label(c,text=txt,font=("Candara",15))
                out.grid(row=5,column=0)
                but2=Button(c,text='Close',bg='black',fg='white',command=c.destroy).grid(row=6,column=0,pady=4)
            cc=Tk()
            cc.geometry('400x150')
            cc.title("CAESAR ENCRYPTOR")
            S31=Label(cc,text="Input",font=("Centaur",20)).grid(row=0,column=0)
            S32=Label(cc,text="Offset",font=("Centaur",20)).grid(row=1,column=0)
            cc1=Entry(cc)
            cc2=Entry(cc)
            cc1.grid( column=1,row=0)
            cc2.grid( column=1,row=1)
            but=Button(cc,text="Convert",command=caesar).grid(row=3,column=1,pady=4)
            but3=Button(cc,text='Cancel',bg='black',fg='white',command=cc.destroy).grid(row=6,column=1)

        elif(ch.get()==3):
            def qwer():
                import qwerty
                c=Toplevel()
                c.geometry('300x100')
                c.title("QWERTY ENCODER")
                txt=''
                txt=qwerty.encrypt(qc1.get())
                S33=Label(c,text="Output After Encoding",font=("Centaur",20)).grid(column=0,row=2)
                out=Label(c,text=txt,font=("Candara",15))
                out.grid(row=5,column=0)
                but2=Button(c,text='Close',bg='black',fg='white',command=c.destroy).grid(row=6,column=0,pady=4)
            qc=Tk()
            qc.geometry('400x100')
            qc.title("QWERTY ENCRYPTOR")
            S41=Label(qc,text="Input",font=("Centaur",20)).grid(column=0,row=0)
            qc1=Entry(qc)
            qc1.grid(row=0, column=1)
            but=Button(qc,text='Convert',command=qwer).grid(row=3,column=1,pady=4)
            but3=Button(qc,text='Cancel',bg='black',fg='white',command=qc.destroy).grid(row=5,column=1)

        elif(ch.get()==4):
            def trans():
                import transpositionCipher
                c=Toplevel()
                c.geometry('300x100')
                c.title("TRANSPOSITION ENCODER")
                S33=Label(c,text="Output After Encoding",font=("Centaur",20)).grid(row=2,column=0)
                txt=transpositionCipher.encrypt(tc1.get(),int(tc2.get()))
                out=Label(c,text=txt,font=("Candara",15))
                out.grid(row=5,column=0)
                but2=Button(c,text='Close',bg='black',fg='white',command=c.destroy).grid(row=6,column=0,pady=4)
            tc=Tk()
            tc.geometry('400x150')
            tc.title("TRANSPOSTION ENCRYPTOR")
            S51=Label(tc,text="Input",font=("Centaur",20)).grid(row=0,column=0)
            S51=Label(tc,text="Offset",font=("Centaur",20)).grid(row=1,column=0)
            tc1=Entry(tc)
            tc2=Entry(tc)
            tc1.grid(row=0, column=1)
            tc2.grid(row=1, column=1)
            but=Button(tc,text='Convert',command=trans).grid(row=3,column=1,pady=4)
            but3=Button(tc,text='Cancel',bg='black',fg='white',command=tc.destroy).grid(row=6,column=1)

        elif(ch.get()==5):
            def rev():
                import reverseCipher
                c=Toplevel()
                c.geometry('300x100')
                c.title("TRANSPOSITION ENCODER")
                txt=reverseCipher.reverseCipher(rc1.get())
                S33=Label(c,text="Output After Encoding",font=("Centaur",20)).grid(row=2,column=0)
                out=Label(c,text=txt,font=("Candara",15))
                out.grid(row=5,column=0)
                but2=Button(c,text='Close',bg='black',fg='white',command=c.destroy).grid(row=6,column=0,pady=4)
            rc=Tk()
            rc.geometry('400x100')
            rc.title("REVERSE ENCRYPTOR")
            S61=Label(rc,text="Input",font=("Centaur",20)).grid(row=0,column=0)
            rc1=Entry(rc)
            rc1.grid(row=0, column=1)
            but=Button(rc,text='Convert',command=rev).grid(row=3,column=1,pady=4)
            but3=Button(rc,text='Cancel',bg='black',fg='white',command=rc.destroy).grid(row=5,column=1)

    E=Toplevel()
    E.geometry('800x500')
    ch=IntVar()
    E1=Label(E,text="Choose One Cipher From The Following : ",font=("Candara",20))
    E1.pack()
    rd1=Radiobutton(E,text='Morse Code',indicatoron = 0,width = 20,padx = 20,value='1',variable=ch,command=b,font=("Centaur",20)).pack()
    rd2=Radiobutton(E,text='Caesar Cipher',indicatoron = 0,width = 20,padx = 20,value='2',variable=ch,command=b,font=("Centaur",20)).pack(pady=5)
    rd3=Radiobutton(E,text='Qwerty Cipher',indicatoron = 0,width = 20,padx = 20,value='3',variable=ch,command=b,font=("Centaur",20)).pack(pady=5)
    rd4=Radiobutton(E,text='Transposition Cipher',indicatoron = 0,width = 20,padx = 20,value='4',variable=ch,command=b,font=("Centaur",20)).pack(pady=5)
    rd5=Radiobutton(E,text='Reverse Cipher',indicatoron = 0,width = 20,padx = 20,value='5',variable=ch,command=b,font=("Centaur",20)).pack(pady=5)
    b=Button(E,text='Exit',bg='black',fg='white',command=E.destroy,font=("Centaur",15)).pack(pady=50)

def s0():
    def a():
        if(ch.get()==1):
            def morse():
                import exp
                c=Toplevel()
                c.geometry('300x100')
                c.title("MORSE DECODER")
                txt=exp.decrypt(mc1.get())
                S33=Label(c,text="Output After Decoding",font=("Centaur",20)).grid(row=2,column=0)
                out=Label(c,text=txt,font=("Candara",15))
                out.grid(row=4,column=0)
                but2=Button(c,text='Close',bg='black',fg='white',command=c.destroy).grid(row=5,column=0,pady=4)
            mc=Tk()
            mc.geometry('400x100')
            mc.title("MORSE DECRYPTOR")
            S21=Label(mc,text="Input",font=("Centaur",20)).grid(column=0,row=0)
            mc1=Entry(mc)
            mc1.grid(column=1,row=0)
            but=Button(mc,text='Convert',command=morse).grid(row=3,column=1,pady=4)
            but3=Button(mc,text='Cancel',bg='black',fg='white',command=mc.destroy).grid(row=5,column=1)
            
        elif(ch.get()==2):
            def caesar():
                c=Toplevel()
                c.geometry('300x100')
                c.title("CAESAR DECODER")
                cip=CaesarCipher(cc1.get(),offset=int(cc2.get()))
                txt=cip.decoded
                S33=Label(c,text="Output After Decoding",font=("Centaur",20)).grid(column=0,row=2)
                out=Label(c,text=txt,font=("Candara",15))
                out.grid(row=5,column=0)
                but2=Button(c,text='Close',bg='black',fg='white',command=c.destroy).grid(row=6,column=0,pady=4)
            cc=Tk()
            cc.geometry('400x150')
            cc.title("CAESAR DECRYPTOR")
            S31=Label(cc,text="Input",font=("Centaur",20)).grid(row=0,column=0)
            S32=Label(cc,text="Offset",font=("Centaur",20)).grid(row=1,column=0)
            cc1=Entry(cc)
            cc2=Entry(cc)
            cc1.grid( column=1,row=0)
            cc2.grid( column=1,row=1)
            but=Button(cc,text="Convert",command=caesar).grid(row=3,column=1,pady=4)
            but3=Button(cc,text='Cancel',bg='black',fg='white',command=cc.destroy).grid(row=6,column=1)

        elif(ch.get()==3):
            def qwer():
                import qwerty
                c=Toplevel()
                c.geometry('300x100')
                c.title("QWERTY DECODER")
                txt=''
                txt=qwerty.decrypt(qc1.get())
                S33=Label(c,text="Output After Decoding",font=("Centaur",20)).grid(column=0,row=2)
                out=Label(c,text=txt,font=("Candara",15))
                out.grid(row=5,column=0)
                but2=Button(c,text='Close',bg='black',fg='white',command=c.destroy).grid(row=6,column=0,pady=4)
            qc=Tk()
            qc.geometry('400x100')
            qc.title("QWERTY DECRYPTOR")
            S41=Label(qc,text="Input",font=("Centaur",20)).grid(column=0,row=0)
            qc1=Entry(qc)
            qc1.grid(row=0, column=1)
            but=Button(qc,text='Convert',command=qwer).grid(row=3,column=1,pady=4)
            but3=Button(qc,text='Cancel',bg='black',fg='white',command=qc.destroy).grid(row=5,column=1)

        elif(ch.get()==4):
            def trans():
                import transpositionCipher
                c=Toplevel()
                c.geometry('300x100')
                c.title("TRANSPOSITION DECODER")
                S33=Label(c,text="Output After Decoding",font=("Centaur",20)).grid(row=2,column=0)
                txt=transpositionCipher.decrypt(tc1.get(),int(tc2.get()))
                out=Label(c,text=txt,font=("Candara",15))
                out.grid(row=5,column=0)
                but2=Button(c,text='Close',bg='black',fg='white',command=c.destroy).grid(row=6,column=0,pady=4)
            tc=Tk()
            tc.geometry('400x150')
            tc.title("TRANSPOSTION DECRYPTOR")
            S51=Label(tc,text="Input",font=("Centaur",20)).grid(row=0,column=0)
            S51=Label(tc,text="Offset",font=("Centaur",20)).grid(row=1,column=0)
            tc1=Entry(tc)
            tc2=Entry(tc)
            tc1.grid(row=0, column=1)
            tc2.grid(row=1, column=1)
            but=Button(tc,text='Convert',command=trans).grid(row=3,column=1,pady=4)
            but3=Button(tc,text='Cancel',bg='black',fg='white',command=tc.destroy).grid(row=6,column=1)

        elif(ch.get()==5):
            def rev():
                import reverseCipher
                c=Toplevel()
                c.geometry('300x100')
                c.title("REVERSE DECODER")
                txt=reverseCipher.reverseCipher(rc1.get())
                S33=Label(c,text="Output After Decoding",font=("Centaur",20)).grid(row=2,column=0)
                out=Label(c,text=txt,font=("Candara",15))
                out.grid(row=5,column=0)
                but2=Button(c,text='Close',bg='black',fg='white',command=c.destroy).grid(row=6,column=1,pady=4)
            rc=Tk()
            rc.geometry('400x100')
            rc.title("REVERSE DECRYPTOR")
            S61=Label(rc,text="Input",font=("Centaur",20)).grid(row=0,column=0)
            rc1=Entry(rc)
            rc1.grid(row=0, column=1)
            but=Button(rc,text='Convert',command=rev).grid(row=3,column=1,pady=4)
            but3=Button(rc,text='Cancel',bg='black',fg='white',command=rc.destroy).grid(row=5,column=1)

    E=Toplevel()
    E.geometry('800x500')
    ch=IntVar()
    E1=Label(E,text="Choose One Cipher From The Following : ",font=("Candara",20))
    E1.pack()
    rd1=Radiobutton(E,text='Morse Code',indicatoron = 0,width = 20,padx = 20,value='1',variable=ch,command=a,font=("Centaur",20)).pack()
    rd2=Radiobutton(E,text='Caesar Cipher',indicatoron = 0,width = 20,padx = 20,value='2',variable=ch,command=a,font=("Centaur",20)).pack(pady=5)
    rd3=Radiobutton(E,text='Qwerty Cipher',indicatoron = 0,width = 20,padx = 20,value='3',variable=ch,command=a,font=("Centaur",20)).pack(pady=5)
    rd4=Radiobutton(E,text='Transposition Cipher',indicatoron = 0,width = 20,padx = 20,value='4',variable=ch,command=a,font=("Centaur",20)).pack(pady=5)
    rd5=Radiobutton(E,text='Reverse Cipher',indicatoron = 0,width = 20,padx = 20,value='5',variable=ch,command=a,font=("Centaur",20)).pack(pady=5)
    b=Button(E,text='Exit',bg='black',fg='white',command=E.destroy,font=("Centaur",15)).pack(pady=50)
    
pj=Tk()
pj.geometry("900x400")
pj.title("ENCRYPTOR-DECRYPTOR")
L1=Label(pj,text="WELCOME TO ENCRYPTOR-DECRYPTOR",font=("Broadway",30))
L1.pack()
L2=Label(pj,text="Select Your Option : ",font=("Candara",20))
L2.pack()
b1=Button(pj,bd=20,text="Encrypt",width=30,command=s1)
b1.pack(pady=15)
b2=Button(pj,bd=20,text="Decrypt",width=30,command=s0)
b2.pack(pady=15)
b3=Button(pj,text='Quit',bg='black',fg='white',command=pj.destroy,font=("Candara",20)).pack(pady=40)

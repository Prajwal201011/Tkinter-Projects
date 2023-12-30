from customtkinter import *
import math

app = CTk()
app.title("Interest Calculator")

def cal():
    princip = int(p.get())
    Term = int(t.get())
    Rate = int(r.get())
    amt = (princip*Term*Rate)/100
    amtl = CTkLabel(interest, text=f"Amount is: {amt}")
    amtl.pack(pady= 15)    
    
HEAD = CTkLabel(app, text="Calculators", font=("Helvetica", 28), text_color="#1dc444")
HEAD.pack(pady=10)
#----------------------  TABS -------------------------------------------
tabv = CTkTabview(app)
tabv.pack(padx=20, pady=20)

interest = tabv.add("Interest")
speed = tabv.add("Speed")
#------------------------------------
tvalue = StringVar()
pvalue = StringVar()
rvalue = StringVar()

pt = CTkLabel(interest, text="Principal", anchor="w")
p = CTkEntry(interest, textvariable=pvalue)
tt = CTkLabel(interest, text="Term", anchor="w")
t = CTkEntry(interest, textvariable=tvalue)
rt = CTkLabel(interest, text="Rate", anchor="w")
r = CTkEntry(interest, textvariable=rvalue)
pt.pack()
t.pack(padx=10, pady=10)
tt.pack()
p.pack(padx=10, pady=10)
rt.pack()
r.pack(padx=10, pady=10)

btn = CTkButton(interest, text="Calculate", fg_color="#1dc444", command=cal)
btn.pack(pady=10)
#-------------------------------------------------------------------------
CTKLabel(speed, text="Speed")


app.mainloop()
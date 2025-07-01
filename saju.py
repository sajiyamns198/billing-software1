import random
import random
import time
import datetime
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog


root=Tk()
root.geometry("1270x690+0+0")
root.resizable(0,0)
root.title("Restaurant Management System")
root.configure(background= 'purple')

Tops= Frame(root, bg='white', bd=10, relief=RIDGE)
Tops.pack(side=TOP)
lblTitle =Label(Tops, font=('arial',30,'bold'),text='Restaurant Management System',bg='black',fg='white',bd=9,justify=CENTER,width=51)
lblTitle.grid(row=0,column=0)


rightframe= Frame(root, bg='purple', bd=14, relief=RIDGE)
rightframe.pack(side=RIGHT)

Buttons_F=Frame(rightframe, bg='purple', bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

calculatorFrame=Frame(rightframe, bg='purple', bd=1, relief=RIDGE)
calculatorFrame.pack(side=TOP)

Receipt_F=Frame(rightframe, bg='purple', bd=4, relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame= Frame(root, bg='purple', bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT)

Cost_F=Frame(MenuFrame, bg='purple', bd=4)
Cost_F.pack(side=BOTTOM)


foodFrame=LabelFrame(MenuFrame,text="Food",font=('arial',18,'bold'),bd=10,relief=RIDGE,fg='black')
foodFrame.pack(side=LEFT)


drinksFrame=LabelFrame(MenuFrame,text="Drinks",font=('arial',18,'bold'),bd=10,relief=RIDGE,fg='black')
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(MenuFrame,text="Cakes",font=('arial',18,'bold'),bd=10,relief=RIDGE,fg='black')
cakesFrame.pack(side=LEFT)


#===========================================Variables==============================================

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()


DateofOrder= StringVar()
Receipt_Ref= StringVar()
PaidTax= StringVar()
SubTotal= StringVar()
TotalCost= StringVar()
costoffood= StringVar()
costofdrink= StringVar()
costofcake=StringVar()
ServiceCharge= StringVar()

text_Input= StringVar()
operator=""

E_roti=StringVar()
E_daal=StringVar()
E_sabji=StringVar()
E_rice=StringVar()
E_paneer=StringVar()
E_kebab=StringVar()
E_fish=StringVar()
E_mutton=StringVar()
E_ButterChicken=StringVar()

E_Thumbsup=StringVar()
E_Redbull=StringVar()
E_Sevenup=StringVar()
E_Lassi=StringVar()
E_Corona=StringVar()
E_Slice=StringVar()
E_Cocacola=StringVar()
E_Drinkwater=StringVar()
E_Tea=StringVar()

E_Oreocake=StringVar()
E_Applecake=StringVar()
E_Kitkatcake=StringVar()
E_Vanillacake=StringVar()
E_bananacake=StringVar()
E_Brownicecake=StringVar()
E_Pineapplecake=StringVar()
E_Chocolatecake=StringVar()
E_Blackforestcake=StringVar()

E_roti.set("0")
E_daal.set("0")
E_sabji.set("0")
E_rice.set("0")
E_paneer.set("0")
E_kebab.set("0")
E_fish.set("0")
E_mutton.set("0")
E_ButterChicken.set("0")

E_Thumbsup.set("0")
E_Redbull.set("0")
E_Sevenup.set("0")
E_Lassi.set("0")
E_Corona.set("0")
E_Slice.set("0")
E_Cocacola.set("0")
E_Drinkwater.set("0")
E_Tea.set("0")

E_Oreocake.set("0")
E_Applecake.set("0")
E_Kitkatcake.set("0")
E_Vanillacake.set("0")
E_bananacake.set("0")
E_Brownicecake.set("0")
E_Pineapplecake.set("0")
E_Chocolatecake.set("0")
E_Blackforestcake.set("0")



DateofOrder.set(time.strftime("%d/%m/%Y"))
#===========================================Function Declaration======================================
class funcdeclare:
 def exit():
        exit = tkinter.messagebox.askyesno("Exit", "Are you sure?")
        if exit>0:
            root.destroy()
            return

def Reset():
    E_roti.set("0")
    E_daal.set("0")
    E_rice.set("0")
    E_fish.set("0")
    E_kebab.set("0")
    E_sabji.set("0")
    E_paneer.set("0")
    E_mutton.set("0")
    E_ButterChicken.set("0")

    E_Thumbsup.set("0")
    E_Redbull.set("0")
    E_Sevenup.set("0")
    E_Lassi.set("0")
    E_Corona.set("0")
    E_Slice.set("0")
    E_Cocacola.set("0")
    E_Drinkwater.set("0")
    E_Tea.set("0")

    E_Oreocake.set("0")
    E_Applecake.set("0")
    E_Kitkatcake.set("0")
    E_Vanillacake.set("0")
    E_bananacake.set("0")
    E_Brownicecake.set("0")
    E_Pineapplecake.set("0")
    E_Chocolatecake.set("0")
    E_Blackforestcake.set("0")
        
    costoffood.set("0")
    costofdrink.set("0")
    costofcake.set("0")
    ServiceCharge.set("0")
    SubTotal.set("0")
    PaidTax.set("0")
    TotalCost.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    txtroti.configure(state=DISABLED)
    txtdaal.configure(state=DISABLED)
    txtrice.configure(state=DISABLED)
    txtfish.configure(state=DISABLED)
    txtkebab.configure(state=DISABLED)
    txtsabji.configure(state=DISABLED)
    txtpaneer.configure(state=DISABLED)
    txtmutton.configure(state=DISABLED)
    txtButterChicken.configure(state=DISABLED)
        

    txtThumbsup.configure(state =DISABLED)
    txtRedbull.configure(state=DISABLED)
    txtSevenup.configure(state=DISABLED)
    txtLassi.configure(state=DISABLED)
    txtCorona.configure(state=DISABLED)
    txtSlice.configure(state=DISABLED)
    txtCocacola.configure(state=DISABLED)
    txtDrinkwater.configure(state=DISABLED)
    txtTea.configure(state=DISABLED)

    txtOreocake.configure(state=DISABLED)
    txtApplecake.configure(state=DISABLED)
    txtKitkatcake.configure(state=DISABLED)
    txtVanillacake.configure(state=DISABLED)
    txtbananacake.configure(state=DISABLED)
    txtBrownicecake.configure(state=DISABLED)
    txtPineapplecake.configure(state=DISABLED)
    txtChocolatecake.configure(state=DISABLED)
    txtBlackforestcake.configure(state=DISABLED)
     
def CostofItem():
     Item1=float(E_roti.get())
     Item2=float(E_daal.get())
     Item3=float(E_sabji.get())
     Item4=float(E_rice.get())
     Item5=float(E_paneer.get())
     Item6=float(E_kebab.get())
     Item7=float(E_fish.get())
     Item8=float(E_mutton.get())
     Item9=float(E_ButterChicken.get())

     
     Item10=float(E_Thumbsup.get())
     Item11=float(E_Redbull.get())
     Item12=float(E_Sevenup.get())
     Item13=float(E_Lassi.get())
     Item14=float(E_Corona.get())
     Item15=float(E_Cocacola.get())
     Item16=float(E_Drinkwater.get())
     Item17=float(E_Tea.get())
     Item18=float(E_Slice.get())
        
     Item19=float(E_Oreocake.get())
     Item20=float(E_bananacake.get())
     Item21=float(E_Applecake.get())
     Item22=float(E_Brownicecake.get())
     Item23=float(E_Blackforestcake.get())
     Item24=float(E_Vanillacake.get())
     Item25=float(E_Chocolatecake.get())
     Item26=float(E_Pineapplecake.get())
     Item27=float(E_Kitkatcake.get())
     
     
     PriceofFoods=((Item1 * 20) + (Item2 * 150) + (Item3 * 130) + (Item4 * 100)
                       + (Item5 * 300) + (Item6 * 280) + (Item7 * 200) + (Item8 * 400) + (Item9 * 400))

     PriceofDrinks=((Item10 * 40 ) + (Item11 * 20) + (Item12 * 40) + (Item13 * 30)
                       + (Item14 * 70) + (Item15 * 40) + (Item16 * 70) + (Item17 * 30) + (Item18 * 40))
     
     PriceofCakes=((Item19 * 200) + (Item20 * 250) + (Item21 * 230) + (Item22 * 200)
                       + (Item23 * 300) + (Item24 * 280) + (Item25 * 200) + (Item26 * 400) + (Item27*300))
     
     DishesPrice="Rs", str('%.2f'%(PriceofFoods))
     DrinksPrice="Rs", str('%.2f'%(PriceofDrinks))
     CakesPrice="Rs", str('%.2f'%(PriceofCakes))

     costoffood.set(DishesPrice)
     costofdrink.set(DrinksPrice)
     costofcake.set(CakesPrice)
     SC="Rs", str('%.2f'%(2.5))
     ServiceCharge.set(SC)

     SubTotalofITEMS="Rs", str('%.2f'%(PriceofFoods+ PriceofDrinks + PriceofCakes + 2.5))
     SubTotal.set(SubTotalofITEMS)

     Tax="Rs", str('%.2f'%((PriceofFoods+ PriceofDrinks + PriceofCakes + 2.5)*0.5))
     PaidTax.set(Tax)
     TT=((PriceofFoods+ PriceofDrinks + PriceofCakes + 2.5) * 0.5)
     TC="Rs", str('%.2f'%(PriceofFoods+ PriceofDrinks + PriceofCakes + 2.5 + TT))
     TotalCost.set(TC)



def roti():
        if(var1.get()==1):
            txtroti.configure(state= NORMAL)
            txtroti.focus()
            txtroti.delete('0', END)
            E_roti.set("")
        elif(var1.get()==0):
            txtroti.configure(state= DISABLED)
            E_roti.set("0")

def daal():
        if(var2.get()==1):
            txtdaal.configure(state= NORMAL)
            txtdaal.focus()
            txtdaal.delete('0', END)
            E_daal.set("")
        elif(var2.get()==0):
            txtdaal.configure(state= DISABLED)
            E_daal.set("0")

def rice():
        if(var3.get()==1):
            txtrice.configure(state= NORMAL)
            txtrice.focus()
            txtrice.delete('0', END)
            E_rice.set("")
        elif(var3.get()==0):
            txtrice.configure(state= DISABLED)
            E_rice.set("0")

def fish():
        if(var4.get()==1):
            txtfish.configure(state= NORMAL)
            txtfish.focus()
            txtfish.delete('0', END)
            E_fish.set("")
        elif(var4.get()==0):
            txtfish.configure(state= DISABLED)
            E_fish.set("0")

def kebab():
        if(var5.get()==1):
            txtkebab.configure(state= NORMAL)
            txtkebab.focus()
            txtkebab.delete('0', END)
            E_kebab.set("")
        elif(var5.get()==0):
            txtkebab.configure(state= DISABLED)
            E_kebab.set("0")  

def sabji():
        if(var6.get()==1):
            txtsabji.configure(state= NORMAL)
            txtsabji.focus()
            txtsabji.delete('0', END)
            E_sabji.set("")
        elif(var6.get()==0):
            txtsabji.configure(state= DISABLED)
            E_sabji.set("0")     

def paneer():
        if(var7.get()==1):
            txtpaneer.configure(state= NORMAL)
            txtpaneer.focus()
            txtpaneer.delete('0', END)
            E_paneer.set("")
        elif(var7.get()==0):
            txtpaneer.configure(state= DISABLED)
            E_paneer.set("0")     

def mutton():
        if(var8.get()==1):
            txtmutton.configure(state= NORMAL)
            txtmutton.focus()
            txtmutton.delete('0', END)
            E_mutton.set("")
        elif(var8.get()==0):
            txtmutton.configure(state= DISABLED)
            E_mutton.set("0")

def ButterChicken():
        if(var9.get()==1):
            txtButterChicken.configure(state= NORMAL)
            txtButterChicken.focus()
            txtButterChicken.delete('0', END)
            E_ButterChicken.set("")
        elif(var9.get()==0):
            txtButterChicken.configure(state= DISABLED)
            E_ButterChicken.set("0")

def Thumbsup():
        if(var10.get()==1):
            txtThumbsup.configure(state= NORMAL)
            txtThumbsup.focus()
            txtThumbsup.delete('0', END)
            E_Thumbsup.set("")
        elif(var10.get()==0):
            txtThumbsup.configure(state= DISABLED)
            E_Thumbsup.set("0")
def Redbull():
        if(var11.get()==1):
            txtRedbull.configure(state= NORMAL)
            txtRedbull.focus()
            txtRedbull.delete('0', END)
            E_Redbull.set("")
        elif(var11.get()==0):
            txtRedbull.configure(state= DISABLED)
            E_Redbull.set("0")
            
def Sevenup():
        if(var12.get()==1):
            txtSevenup.configure(state= NORMAL)
            txtSevenup.focus()
            txtSevenup.delete('0', END)
            E_Sevenup.set("")
        elif(var12.get()==0):
            txtSevenup.configure(state= DISABLED)
            E_Sevenup.set("0")

def Lassi():
        if(var13.get()==1):
            txtLassi.configure(state= NORMAL)
            txtLassi.focus()
            txtLassi.delete('0', END)
            E_Lassi.set("")
        elif(var13.get()==0):
            txtLassi.configure(state= DISABLED)
            E_Lassi.set("0")

def Corona():
        if(var14.get()==1):
            txtCorona.configure(state= NORMAL)
            txtCorona.focus()
            txtCorona.delete('0', END)
            E_Corona.set("")
        elif(var14.get()==0):
            txtCorona.configure(state= DISABLED)
            E_Corona.set("0")

def Slice():
        if(var15.get()==1):
            txtSlice.configure(state= NORMAL)
            txtSlice.focus()
            txtSlice.delete('0', END)
            E_Slice.set("")
        elif(var15.get()==0):
            txtSlice.configure(state= DISABLED)
            E_Slice.set("0")

def Cocacola():
        if(var16.get()==1):
            txtCocacola.configure(state= NORMAL)
            txtCocacola.focus()
            txtCocacola.delete('0', END)
            E_Cocacola.set("")
        elif(var16.get()==0):
            txtCocacola.configure(state= DISABLED)
            E_Cocacola.set("0")

def Drinkwater():
        if(var17.get()==1):
            txtDrinkwater.configure(state= NORMAL)
            txtDrinkwater.focus()
            txtDrinkwater.delete('0', END)
            E_Drinkwater.set("")
        elif(var17.get()==0):
            txtDrinkwater.configure(state= DISABLED)
            E_Drinkwater.set("0")

def Tea():
        if(var18.get()==1):
            txtTea.configure(state= NORMAL)
            txtTea.focus()
            txtTea.delete('0', END)
            E_Tea.set("")
        elif(var18.get()==0):
            txtTea.configure(state= DISABLED)
            E_Tea.set("0")

   

def Oreocake():
        if(var19.get()==1):
            txtOreocake.configure(state= NORMAL)
            txtOreocake.focus()
            txtOreocake.delete('0', END)
            E_Oreocake.set("")
        elif(var19.get()==0):
            txtOreocake.configure(state= DISABLED)
            E_Oreocake.set("0")

def Applecake():
        if(var20.get()==1):
            txtApplecake.configure(state= NORMAL)
            txtApplecake.focus()
            txtApplecake.delete('0', END)
            E_Applecake.set("")
        elif(var20.get()==0):
            txtApplecake.configure(state= DISABLED)
            E_Applecake.set("0")

def Kitkatcake():
        if(var21.get()==1):
            txtKitkatcake.configure(state= NORMAL)
            txtKitkatcake.focus()
            txtKitkatcake.delete('0', END)
            E_Kitkatcake.set("")
        elif(var21.get()==0):
            txtKitkatcake.configure(state= DISABLED)
            E_Kitkatcake.set("0")
def Vanillacake():
        if(var22.get()==1):
            txtVanillacake.configure(state= NORMAL)
            txtVanillacake.focus()
            txtVanillacake.delete('0', END)
            E_Vanillacake.set("")
        elif(var22.get()==0):
            txtVanillacake.configure(state= DISABLED)
            E_Vanillacake.set("0")

def bananacake():
        if(var23.get()==1):
            txtbananacake.configure(state= NORMAL)
            txtmutton.focus()
            txtbananacake.delete('0', END)
            E_bananacake.set("")
        elif(var23.get()==0):
            txtbananacake.configure(state= DISABLED)
            E_bananacake.set("0")

def Brownice():
        if(var24.get()==1):
            txtBrownicecake.configure(state= NORMAL)
            txtBrownicecake.focus()
            txtBrownicecake.delete('0', END)
            E_Brownicecake.set("")
        elif(var24.get()==0):
            txtBrownicecake.configure(state= DISABLED)
            E_Brownicecake.set("0")

def Pineapplecake():
        if(var25.get()==1):
            txtPineapplecake.configure(state= NORMAL)
            txtPineapplecake.focus()
            txtPineapplecake.delete('0', END)
            E_Pineapplecake.set("")
        elif(var25.get()==0):
            txtPineapplecake.configure(state= DISABLED)
            E_Pineapplecake.set("0")

def Chocolatecake():
        if(var26.get()==1):
            txtChocolatecake.configure(state= NORMAL)
            txtChocolatecake.focus()
            txtChocolatecake.delete('0', END)
            E_Chocolatecake.set("")
        elif(var26.get()==0):
            txtChocolatecake.configure(state= DISABLED)
            E_Chocolatecake.set("0")

def Blackforest():
        if(var27.get()==1):
            txtBlackforestcake.configure(state= NORMAL)
            txtBlackforestcake.focus()
            txtBlackforestcake.delete('0', END)
            E_Blackforestcake.set("")
        elif(var27.get()==0):
            txtBlackforestcake.configure(state= DISABLED)
            E_Blackforestcake.set("0")


def save():
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')

        bill_data=txtReceipt.get(1.0, END)
        url.write(bill_data)
        url.close()
        tkinter.messagebox.showinfo('your file is successfully save')

     
def Receipt():
        txtReceipt.delete("1.0",END)
        x= random.randint(10903, 609235)
        randomRef= str(x)
        Receipt_Ref.set("BILL" + randomRef)
        

        txtReceipt.insert(END, 'Receipt Ref:' +Receipt_Ref.get() + "\t\t\tDate:" + DateofOrder.get() + "\n")
        txtReceipt.insert(END,'**************************************************************\n')
        txtReceipt.insert(END, 'Items(Rs.):         No of Items        Cost of Items(Rs)\n')
        txtReceipt.insert(END,'**************************************************************\n')
        
        if E_roti.get()!='0':
           txtReceipt.insert(END, 'Roti(20): \t\t' + E_roti.get() +  f'\t\t{int (E_roti.get())*20} \n')
        if E_daal.get()!='0':
           txtReceipt.insert(END, 'Daal(150): \t\t' + E_daal.get() +  f' \t\t{int (E_daal.get())*150} \n')
        if E_rice.get()!='0':
           txtReceipt.insert(END, 'Rice(130): \t\t' + E_rice.get() +  f' \t\t{int (E_rice.get())*130} \n')
        if E_fish.get()!='0':
           txtReceipt.insert(END, 'Fish(100): \t\t' + E_fish.get() +  f' \t\t{int (E_fish.get())*100} \n')
        
        if E_kebab.get()!='0':
           txtReceipt.insert(END, 'Kebab(300): \t\t' + E_kebab.get() +  f' \t\t{int (E_kebab.get())*300} \n')
        if E_sabji.get()!='0':
           txtReceipt.insert(END, 'Sabji(280): \t\t' + E_sabji.get() +  f' \t\t{int (E_sabji.get())*280} \n')
        if E_paneer.get()!='0':
           txtReceipt.insert(END, 'Paneer(200): \t\t' + E_paneer.get() +  f' \t\t{int (E_paneer.get())*200} \n')
        if E_mutton.get()!='0':
           txtReceipt.insert(END, 'Mutton(400): \t\t' + E_mutton.get() +  f' \t\t{int (E_mutton.get())*400} \n')
        
        if E_ButterChicken.get()!='0':
           txtReceipt.insert(END, 'ButerChicken\n(400) \t\t' + E_ButterChicken.get() +  f' \t\t{int (E_ButterChicken.get())*400} \n')
        if E_Thumbsup.get()!='0':
           txtReceipt.insert(END, 'Thumbsup(40): \t\t' + E_Thumbsup.get() +  f' \t\t{int (E_Thumbsup.get())*40} \n')
        if E_Oreocake.get()!='0':
           txtReceipt.insert(END, 'OreoCake(200): \t\t' + E_Oreocake.get() +  f' \t\t{int (E_Oreocake.get())*200} \n')
        
        


        
obj=funcdeclare()


#============================================food===================================================================#
      
roti=Checkbutton(foodFrame,text="Roti",font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var1,command=roti)
roti.grid(row=0,column=0)
daal=Checkbutton(foodFrame,text="Daal",font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var2,command=daal)
daal.grid(row=1,column=0)
rice=Checkbutton(foodFrame,text="Rice",font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var3,command=rice)
rice.grid(row=2,column=0)
fish=Checkbutton(foodFrame,text="Fish",font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var4,command=fish)
fish.grid(row=3,column=0)
kebab=Checkbutton(foodFrame,text="Kebab",font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var5,command=kebab)
kebab.grid(row=4,column=0)
sabji=Checkbutton(foodFrame,text="Sabji",font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var6,command=sabji)
sabji.grid(row=5,column=0)
paneer=Checkbutton(foodFrame,text="Paneer",font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var7,command=paneer)
paneer.grid(row=6,column=0)
mutton=Checkbutton(foodFrame,text="Mutton",font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var8,command=mutton)
mutton.grid(row=7,column=0)
ButterChicken=Checkbutton(foodFrame,text="ButterChicken",font=('arial',16,'bold'),onvalue=1,offvalue=0,variable=var9,command=ButterChicken)
ButterChicken.grid(row=8,column=0)

#=============================================================================================================================
txtroti= Entry(foodFrame,font=('arial',16,'bold'),bd=6,width=6, justify=LEFT, state= DISABLED, textvariable=E_roti)
txtroti.grid(row=0,column=1)

txtdaal= Entry(foodFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_daal)
txtdaal.grid(row=1,column=1)

txtrice= Entry(foodFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_rice)
txtrice.grid(row=2,column=1)


txtfish= Entry(foodFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_fish)
txtfish.grid(row=3,column=1)

txtkebab= Entry(foodFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_kebab)
txtkebab.grid(row=4,column=1)

txtsabji= Entry(foodFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_sabji)
txtsabji.grid(row=5,column=1)


txtpaneer= Entry(foodFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_paneer)
txtpaneer.grid(row=6,column=1)


txtmutton= Entry(foodFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_mutton)
txtmutton.grid(row=7,column=1)

txtButterChicken= Entry(foodFrame,font=('arial',16,'bold'),bd=6,width=6, justify=LEFT, state= DISABLED, textvariable=E_ButterChicken)
txtButterChicken.grid(row=8,column=1)

#===========================================Drinks========================================================

#===========================================Drinks========================================================

Thumbsup=Checkbutton(drinksFrame, text='Thumbs Up',font= ('arial',16,'bold'), variable=var10,command=Thumbsup,onvalue=1, offvalue=0)
Thumbsup.grid(row=0,column=0,sticky=W)

Redbull=Checkbutton(drinksFrame, text='Red Bull',variable=var11,command=Redbull, onvalue=1, offvalue=0, font=('arial',16,'bold'))
Redbull.grid(row=1,sticky=W)

Sevenup=Checkbutton(drinksFrame, text='7 Up' ,variable=var12,command=Sevenup, onvalue=1, offvalue=0, font=('arial',16,'bold'))
Sevenup.grid(row=2,sticky=W)
Lassi=Checkbutton(drinksFrame, text='Lassi',variable=var13,command=Lassi, onvalue=1, offvalue=0, font=('arial',16,'bold'))
Lassi.grid(row=3,sticky=W),
Corona=Checkbutton(drinksFrame, text='Corona',variable=var14,command=Corona, onvalue=1, offvalue=0, font=('arial',16,'bold'))
Corona.grid(row=4,sticky=W)
Slice=Checkbutton(drinksFrame, text='Slice',variable=var15,command=Slice, onvalue=1, offvalue=0, font=('arial',16,'bold'))
Slice.grid(row=5,sticky=W)
Cocacola=Checkbutton(drinksFrame, text='Cocacola',variable=var16, command=Cocacola,onvalue=1, offvalue=0, font=('arial',16,'bold'))
Cocacola.grid(row=6,sticky=W)
Drinkwater=Checkbutton(drinksFrame, text='Drink Water',variable=var17,command=Drinkwater, onvalue=1, offvalue=0, font=('arial',16,'bold'))
Drinkwater.grid(row=7,sticky=W)
Tea=Checkbutton(drinksFrame, text='Tea',variable=var18,command=Tea, onvalue=1, offvalue=0, font=('arial',16,'bold'))
Tea.grid(row=8,sticky=W)

#===========================================Entry Box for Drinks========================================================

txtThumbsup= Entry(drinksFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_Thumbsup)
txtThumbsup.grid(row=0,column=1)

txtRedbull= Entry(drinksFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_Redbull)
txtRedbull.grid(row=1,column=1)

txtSevenup= Entry(drinksFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_Sevenup)
txtSevenup.grid(row=2,column=1)

txtLassi= Entry(drinksFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_Lassi)
txtLassi.grid(row=3,column=1)

txtCorona= Entry(drinksFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_Corona)
txtCorona.grid(row=4,column=1)

txtSlice= Entry(drinksFrame,font=('arial',18,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_Slice)
txtSlice.grid(row=5,column=1)

txtCocacola= Entry(drinksFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_Cocacola)
txtCocacola.grid(row=6,column=1)

txtDrinkwater= Entry(drinksFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_Drinkwater)
txtDrinkwater.grid(row=7,column=1)

txtTea= Entry(drinksFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_Tea)
txtTea.grid(row=8,column=1)
#===========================================Cakes===================================================

Oreocake=Checkbutton(cakesFrame, text='Oreo',font= ('arial',16,'bold'),variable=var19,command=Oreocake, onvalue=1, offvalue=0)
Oreocake.grid(row=0,column=0,sticky=W)

Applecake=Checkbutton(cakesFrame, text='Apple',variable=var20, command=Applecake,onvalue=1, offvalue=0, font=('arial',16,'bold'))
Applecake.grid(row=1,sticky=W)

Kitkatcake=Checkbutton(cakesFrame, text='Kitkat' ,variable=var21, command=Kitkatcake,onvalue=1, offvalue=0, font=('arial',16,'bold'))
Kitkatcake.grid(row=2,sticky=W)

Vanillacake=Checkbutton(cakesFrame, text='Vanilla',variable=var22,command=Vanillacake, onvalue=1, offvalue=0, font=('arial',16,'bold'))
Vanillacake.grid(row=3,sticky=W),

bananacake=Checkbutton(cakesFrame, text='Banana',variable=var23,command=bananacake, onvalue=1, offvalue=0, font=('arial',16,'bold'))
bananacake.grid(row=4,sticky=W)

Brownice=Checkbutton(cakesFrame, text='Brownice' ,variable=var24,command=Brownice, onvalue=1, offvalue=0, font=('arial',16,'bold'))
Brownice.grid(row=5,sticky=W)

Pineapplecake=Checkbutton(cakesFrame, text='Pineapple', variable=var25,command=Pineapplecake, onvalue=1, offvalue=0, font=('arial',16,'bold'))
Pineapplecake.grid(row=6,sticky=W)

Chocolatecake=Checkbutton(cakesFrame, text='Chocolate',variable=var26,command=Chocolatecake, onvalue=1, offvalue=0, font=('arial',16,'bold'))
Chocolatecake.grid(row=7,sticky=W)

Blackforest=Checkbutton(cakesFrame, text='Blackforest',variable=var27,command=Blackforest, onvalue=1, offvalue=0, font=('arial',16,'bold'))
Blackforest.grid(row=8,sticky=W)

#===========================================Cakes===========================================================
#===========================================Cakes===========================================================

txtOreocake= Entry(cakesFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_Oreocake)
txtOreocake.grid(row=0,column=1)

txtApplecake= Entry(cakesFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_Applecake)
txtApplecake.grid(row=1,column=1)

txtKitkatcake= Entry(cakesFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_Kitkatcake)
txtKitkatcake.grid(row=2,column=1)

txtVanillacake= Entry(cakesFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_Vanillacake)
txtVanillacake.grid(row=3,column=1)

txtbananacake= Entry(cakesFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_bananacake)
txtbananacake.grid(row=4,column=1)

txtBrownicecake= Entry(cakesFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_Brownicecake)
txtBrownicecake.grid(row=5,column=1)

txtPineapplecake= Entry(cakesFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_Pineapplecake)
txtPineapplecake.grid(row=6,column=1)

txtChocolatecake= Entry(cakesFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_Chocolatecake)
txtChocolatecake.grid(row=7,column=1)

txtBlackforestcake= Entry(cakesFrame,font=('arial',16,'bold'),bd=6, width=6, justify=LEFT, state= DISABLED, textvariable=E_Blackforestcake)
txtBlackforestcake.grid(row=8,column=1)

#=======================================================Total Cost=========================================================
lblCostofFood =Label(Cost_F, font=('arial',16,'bold'),bg='purple',text='Cost of Foods\t',fg='white')
lblCostofFood.grid(row=0,column=0,padx=41)
txtCostofFood= Entry(Cost_F, width=14, bg='white', bd=6, font=('arial',16,'bold'), justify=RIGHT,state='readonly',textvariable=costoffood )
txtCostofFood.grid(row=0, column=1)

lblCostofDrinks =Label(Cost_F, font=('arial',16,'bold'),bg='purple',text='Cost of Drinks\t',fg='white')
lblCostofDrinks.grid(row=1,column=0,padx=41)
txtCostofDrinks= Entry(Cost_F, width=14, bg='white', bd=6, font=('arial',16,'bold'), justify=RIGHT,state='readonly',textvariable=costofdrink)
txtCostofDrinks.grid(row=1, column=1)


lblCostofcake =Label(Cost_F, font=('arial',16,'bold'),bg='purple',text='Cost of Cakes\t',fg='white')
lblCostofcake.grid(row=2,column=0,padx=41)
txtCostofDrinks= Entry(Cost_F, width=14, bg='white', bd=6, font=('arial',16,'bold'), justify=RIGHT,state='readonly',textvariable=costofcake)
txtCostofDrinks.grid(row=2, column=1)


lblServiceCharge =Label(Cost_F, font=('arial',16,'bold'),text='\tService Charge\t',bg='Purple',fg='white')
lblServiceCharge.grid(row=3,column=0, sticky=W)
txtServiceCharge= Entry(Cost_F, width=14, bg='white', bd=6, font=('arial',16,'bold'), justify=RIGHT,state='readonly',textvariable=ServiceCharge)
txtServiceCharge.grid(row=3, column=1)

#=======================================================Payment Information================================================


lblPaidTax =Label(Cost_F, font=('arial',14,'bold'),text='\tPaidTax',bg='Purple',fg='white')
lblPaidTax.grid(row=0,column=2, sticky=W)
txtPaidTax= Entry(Cost_F, width=18, bg='white', bd=7, font=('arial',10,'bold'), justify=RIGHT,state='readonly',textvariable=PaidTax)
txtPaidTax.grid(row=0, column=3)



lblSubTotal =Label(Cost_F, font=('arial',14,'bold'),text='\tSub Total',bg='purple',fg='white')
lblSubTotal.grid(row=1,column=2, sticky=W)
txtSubTotal= Entry(Cost_F, width=18, bg='white', bd=7, font=('arial',10,'bold'), justify=RIGHT, textvariable=SubTotal)
txtSubTotal.grid(row=1, column=3)

lblTotalCost =Label(Cost_F, font=('arial',14,'bold'),text='\tTotal Cost',bg='purple',fg='white')
lblTotalCost.grid(row=2,column=2, sticky=W)
txtTotalCost= Entry(Cost_F, width=18, bg='white', bd=7, font=('arial',10,'bold'), justify=RIGHT, textvariable=TotalCost)
txtTotalCost.grid(row=2, column=3)


#=======================================================Receipt============================================================

txtReceipt= Text(Receipt_F, width=42, height=12, bg='white', bd=4, font=('arial',12,'bold'))
txtReceipt.grid(row=0, column=0)

#=======================================================Buttons============================================================

btnTotal=Button(Buttons_F, padx=5, pady=1, bd=3, fg='white', font= ('arial',12,'bold'),width=4, text="Total", bg="purple",
                 command=CostofItem)
btnTotal.grid(row=0,column=0)


btnReceipt=Button(Buttons_F, padx=10, pady=1, bd=3, fg='white', font=('arial',12,'bold'),width=4, text="Receipt",bg="purple",
                  command=Receipt)
btnReceipt.grid(row=0,column=1)


btnreset=Button(Buttons_F, padx=10, pady=1, bd=3, fg='white', font=('arial',12,'bold'),width=4, text="Reset", bg="purple",
                command=Reset)
btnreset.grid(row=0,column=4)



btnExit=Button(Buttons_F, padx=10, pady=1, bd=3, fg='white', font=('arial',12,'bold'),
                width=4, text="Exit", bg="purple",
                 command=exit)
btnExit.grid(row=1,column=2)

btnSave=Button(Buttons_F ,padx=10, pady=1, bd=3, fg='white', font=('arial',12,'bold'), width=4, text="Save", bg="purple",
               command=save)
btnSave.grid(row=0,column=2)





#=======================================================Calculator Display=================================================

operator=""
def btnClick(numbers):
        global operator
        operator= operator + numbers
        calculatorField.delete(0,END)
        calculatorField.insert(END,operator)
        
def clear():
        global operator
        operator = ""
        calculatorField.delete(0,END)

def answer():
        global operator
        result=str(eval(operator))
        calculatorField.delete(0,END)
        calculatorField.insert(0,result)
        operator=""


def btnEquals(self):
        global operator
        sumup = str(eval(operator))
        text_Input.set(sumup)
        operator = ""

        txtDisplay= Entry(calculatorFrame, width=45, bg='white', bd=4, font=('arial',12,'bold'), justify=RIGHT, textvariable= text_Input)
        txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
        txtDisplay.insert(0,"0")

     

#=======================================================Calculator Buttons=================================================
calculatorField=Entry(calculatorFrame,font=('arial',15,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)


btn7=Button(calculatorFrame,bd=6, fg='white', font=('arial',15,'bold'),width=6,command=lambda:btnClick('7') ,text="7", bg="purple")
btn7.grid(row=1,column=0)

btn8=Button(calculatorFrame,bd=6, fg='white', font=('arial',15,'bold'),width=6, command=lambda:btnClick('8'),text="8", bg="purple")
btn8.grid(row=1,column=1)

btn9=Button(calculatorFrame,bd=6, fg='white', font=('arial',15,'bold'),width=6,command=lambda:btnClick('8'), text="9", bg="purple")
btn9.grid(row=1,column=2)

btnplus=Button(calculatorFrame,bd=6, fg='white', font=('arial',15,'bold'),width=6,command=lambda:btnClick('+'), text="+", bg="purple")
btnplus.grid(row=1,column=3)

#=======================================================Calculator Buttons=================================================

btn4=Button(calculatorFrame,bd=6, fg='white', font=('arial',15,'bold'),width=6,command=lambda:btnClick('4') , text="4", bg="purple")
btn4.grid(row=2,column=0)

btn5=Button(calculatorFrame,bd=6, fg='white', font=('arial',15,'bold'),width=6,command=lambda:btnClick('5') , text="5", bg="purple")
btn5.grid(row=2,column=1)

btn6=Button(calculatorFrame,bd=6, fg='white', font=('arial',15,'bold'),width=6, command=lambda:btnClick('6') ,text="6", bg="purple")
btn6.grid(row=2,column=2)

btnsub=Button(calculatorFrame,bd=6, fg='white', font=('arial',15,'bold'),width=6,command=lambda:btnClick('-') , text="-", bg="purple")
btnsub.grid(row=2,column=3)
#=======================================================Calculator Buttons=================================================

btn1=Button(calculatorFrame,bd=6, fg='white', font=('arial',15,'bold'),width=6, command=lambda:btnClick('1') ,text="1", bg="purple")
btn1.grid(row=3,column=0)

btn2=Button(calculatorFrame,bd=6, fg='white', font=('arial',15,'bold'),width=6,command=lambda:btnClick('2') , text="2", bg="purple")
btn2.grid(row=3,column=1)

btn3=Button(calculatorFrame,bd=6, fg='white', font=('arial',15,'bold'),width=6,command=lambda:btnClick('3') , text="3", bg="purple")
btn3.grid(row=3,column=2)

btnmul=Button(calculatorFrame,bd=6, fg='white', font=('arial',15,'bold'),width=6,command=lambda:btnClick('*') , text="*", bg="purple")
btnmul.grid(row=3,column=3)
#=======================================================Calculator Buttons=================================================

btnAns=Button(calculatorFrame,bd=6, fg='white', font=('arial',15,'bold'),width=6,command=answer , text="Ans", bg="purple")
btnAns.grid(row=4,column=0)

btnClear=Button(calculatorFrame,bd=6, fg='white', font=('arial',15,'bold'),width=6,command=clear, text="Clear", bg="purple")
btnClear.grid(row=4,column=1)

btn0=Button(calculatorFrame,bd=6, fg='white', font=('arial',15,'bold'),width=6,command=lambda:btnClick('0') , text="0", bg="purple")
btn0.grid(row=4,column=2)

btndiv=Button(calculatorFrame,bd=6, fg='white', font=('arial',15,'bold'),width=6,command=lambda:btnClick('/') , text="/", bg="purple")
btndiv.grid(row=4,column=3)

root.mainloop()





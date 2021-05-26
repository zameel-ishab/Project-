from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
         self.root=root
         self.root.geometry("1200x700+0+0")
         self.root.title("Billing Software")
         bg_color="#074463"
         title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
         #==========variables=========
         #==========Cosmetics=========
         self.soap=IntVar()
         self.face_cream=IntVar()
         self.face_wash=IntVar()
         self.spray=IntVar()
         self.gell=IntVar()
         self.loshan=IntVar()
         #===========grocery======
         self.rice=IntVar()
         self.food_oil=IntVar()
         self.daal=IntVar()
         self.wheat=IntVar()
         self.sugar=IntVar()
         self.tea=IntVar()
         
         #==========cold drinks=========
         self.maaza=IntVar()
         self.cock=IntVar()
         self.frooti=IntVar()
         self.thumsup=IntVar()
         self.limca=IntVar()
         self.sprit=IntVar()
         #======Totel Product Price &Tax Variable=====
         self.cosmetic_price=StringVar()
         self.grocery_price=StringVar()
         self.cold_drink_price=StringVar()


         self.cosmetic_tax=StringVar()
         self.grocery_tax=StringVar()
         self.cold_drink_tax=StringVar()

         #=======Customer====
         self.c_name=StringVar()
         self.c_phon=StringVar()
         self.bill_no=StringVar()
         x=random.randint(1000,9999)
         self.bill_no.set(str(x))
         self.search_bill=StringVar()
         
         #==============customer Detail Frame
         F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new romen",15,"bold"),fg="gold",bg=bg_color)
         F1.place(x=0,y=80,relwidth=1)

         cname_lbl=Label(F1,text="cutomer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
         cname_text=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

         cphn_lbl=Label(F1,text=" Phon No",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
         cphn_text=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

         c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
         c_bill_text=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

         bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=5,pady=10)



         #==========Cosmetics Frame=============
         F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new romen",15,"bold"),fg="gold",bg=bg_color)
         F2.place(x=5,y=180,width=325,height=380)


         bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
         bath_text=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

         Face_cream_lbl=Label(F2,text="Face cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
         Face_cream_text=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

         Face_w_lbl=Label(F2,text="Face wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
         Face_w_text=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

         Haire_s_lbl=Label(F2,text="Haire sparey",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
         Haire_s_text=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)


         Haire_g_lbl=Label(F2,text="Haire gell",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
         Haire_g_text=Entry(F2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

         Body_lbl=Label(F2,text="Body Loshan",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
         Body_text=Entry(F2,width=10,textvariable=self.loshan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)




         #==========GroceryFrame=============
         F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Gorocery",font=("times new romen",15,"bold"),fg="gold",bg=bg_color)
         F3.place(x=340,y=180,width=325,height=380)


         g1_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
         g1_text=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

         g2_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
         g2_text=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

         g3_lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
         g3_text=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

         g4_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
         g4_text=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)


         g5_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
         g5_text=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

         g6_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
         g6_text=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


         
         #==========Cold drinksFrame=============
         F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold drink",font=("times new romen",15,"bold"),fg="gold",bg=bg_color)
         F4.place(x=670,y=180,width=325,height=380)


         c1_lbl=Label(F4,text="Maaza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
         c1_text=Entry(F4,width=10,textvariable=self.maaza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

         c2_lbl=Label(F4,text="Cock",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
         c2_text=Entry(F4,width=10,textvariable=self.cock,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

         c3_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
         c3_text=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

         c4_lbl=Label(F4,text="Thumbs Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
         c4_text=Entry(F4,width=10,textvariable=self.thumsup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)


         c5_lbl=Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
         c5_text=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

         c6_lbl=Label(F4,text="sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
         c6_text=Entry(F4,width=10,textvariable=self.sprit,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #======Bill Area=====

         F5=Frame(self.root,bd=10,relief=GROOVE)
         F5.place(x=1010,y=180,width=190,height=380)
         bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
         scrol_y=Scrollbar(F5,orient=VERTICAL)
         self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
         scrol_y.pack(side=RIGHT,fill=Y)
         scrol_y.config(command=self.txtarea.yview)
         self.txtarea.pack(fill=BOTH,expand=1)

         #======ButtonFrame======
         F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Main menu",font=("times new romen",15,"bold"),fg="gold",bg=bg_color)
         F6.place(x=0,y=560,relwidth=1,height=140)
         m1_lbl=Label(F6,text="Totel cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0)
         m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

         m2_lbl=Label(F6,text="Totel Gorocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0)
         m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

         m3_lbl=Label(F6,text="Totel Cold Drink Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0)
         m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

         c1_lbl=Label(F6,text="Totel cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2)
         c1_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.cosmetic_tax,bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

         c2_lbl=Label(F6,text="Totel Gorocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2)
         c2_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.grocery_tax,bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

         c3_lbl=Label(F6,text="Totel Cold Drink Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2)
         c3_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.cold_drink_tax,bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

         btn_F=Frame(F6,bd=7,relief=GROOVE)
         btn_F.place(x=750,width=580,height=105)

         total_btn=Button(btn_F,command=self.total,text="Totel",bg="cadetblue",fg="white",bd=1,pady=9,width=6,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
         Gbill_btn=Button(btn_F,text="Genrate bill",command=self.bill_area,bg="cadetblue",fg="white",bd=1,pady=9,width=6,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
         clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=1,pady=9,width=6,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
         Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",bd=1,pady=9,width=6,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
         self.welcome_bill()
    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.spray.get()*180
        self.c_hg_p=self.gell.get()*140
        self.c_bl_p=self.loshan.get()*180

        self.total_cosmetic_price=float(
                                        self.c_s_p+
                                        self.c_fc_p+
                                        self.c_fw_p+
                                        self.c_hs_p+
                                        self.c_hg_p+
                                        self.c_bl_p
                                        )

        self.cosmetic_price.set("Rs."+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs."+str(self.c_tax))

        self.g_r_p=self.rice.get()*40
        self.g_f_p=self.food_oil.get()*120
        self.g_d_p=self.daal.get()*60
        self.g_w_p=self.wheat.get()*180
        self.g_s_p=self.sugar.get()*140
        self.g_t_p=self.tea.get()*180
        self.total_grocery_price=float(
                                    self.g_r_p+
                                    self.g_f_p+
                                    self.g_d_p+
                                    self.g_w_p+
                                    self.g_s_p+
                                    self.g_t_p
                                    )

        self.grocery_price.set("RS."+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.05),2)
        self.grocery_tax.set("Rs."+str(self.g_tax))
           
        self.d_m_p=self.maaza.get()*60
        self.d_c_p=self.cock.get()*60
        self.d_f_p=self.frooti.get()*50
        self.d_t_p=self.thumsup.get()*45
        self.d_l_p=self.limca.get()*40
        self.d_s_p=self.sprit.get()*60
        self.total_cold_drink_price=float(
                                          self.d_m_p+
                                          self.d_c_p+
                                          self.d_f_p+
                                          self.d_t_p+
                                          self.d_l_p+
                                          self.d_s_p
                                          )

        self.cold_drink_price.set("Rs."+str(self.total_cold_drink_price))
        self.d_tax=round((self.total_cold_drink_price*0.05),2)
        self.cold_drink_tax.set("Rs."+str(self.d_tax))

        self.Total_bill=float(
                             self.total_cosmetic_price+
                             self.total_grocery_price+
                             self.total_grocery_price+
                             self.c_tax+
                             self.g_tax+
                             self.d_tax
                             )
                              

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome webcode Reatail\n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name :{self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n===================================")
        self.txtarea.insert(END,f"\n Products\t\tQTY\tprice")
        self.txtarea.insert(END,f"\n===================================")

    def bill_area(self):
        if self.c_name.get()==""or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmetic_price.get()=="Rs.0,0" and self.grocery_price.get()=="Rs.0,0" and self.cold_drink_price.get()=="Rs.0,0" :
         messagebox.showerror("Error","No Purchased")
             
        else:
          self.welcome_bill()
        #=====cosmetic========
        if self.soap.get()!=0:
           self.txtarea.insert(END,f"\Bath soap\t\t{self.soap.get()}\t\t{self.c_s_p}")  
        if self.face_cream.get()!=0:
           self.txtarea.insert(END,f"\face cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")  
        if self.face_wash.get()!=0:
           self.txtarea.insert(END,f"\face wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")  
        if self.spray.get()!=0:
           self.txtarea.insert(END,f"\spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")  
        if self.gell.get()!=0:
           self.txtarea.insert(END,f"\gell\t\t{self.gell.get()}\t\t{self.c_hg_p}")  
        if self.loshan.get()!=0:
           self.txtarea.insert(END,f"\body loshan\t\t{self.loshan.get()}\t\t{self.c_bl_p}")  

           #=====grocery========
        if self.rice.get()!=0:
           self.txtarea.insert(END,f"\rice\t\t{self.rice.get()}\t\t{self.g_r_p}")  
        if self.food_oil.get()!=0:
           self.txtarea.insert(END,f"\Food oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")  
        if self.daal.get()!=0:
           self.txtarea.insert(END,f"\daal\t\t{self.daal.get()}\t\t{self.g_d_p}")  
        if self.wheat.get()!=0:
           self.txtarea.insert(END,f"\wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")  
        if self.sugar.get()!=0:
           self.txtarea.insert(END,f"\sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")  
        if self.tea.get()!=0:
           self.txtarea.insert(END,f"\tea\t\t{self.tea.get()}\t\t{self.g_t_p}")  

           #=====cold drink========
        if self.maaza.get()!=0:
           self.txtarea.insert(END,f"\maaza\t\t{self.maaza.get()}\t\t{self.d_m_p}")  
        if self.cock.get()!=0:
           self.txtarea.insert(END,f"\cock\t\t{self.cock.get()}\t\t{self.d_c_p}")  
        if self.frooti.get()!=0:
           self.txtarea.insert(END,f"\frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")  
        if self.thumsup.get()!=0:
           self.txtarea.insert(END,f"\thumsup\t\t{self.thumsup.get()}\t\t{self.d_t_p}")  
        if self.limca.get()!=0:
           self.txtarea.insert(END,f"\limca\t\t{self.limca.get()}\t\t{self.d_l_p}")  
        if self.sprit.get()!=0:
           self.txtarea.insert(END,f"\sprit\t\t{self.sprit.get()}\t\t{self.d_s_p}")

  
           self.txtarea.insert(END,f"\n-----------------------------------")
           if self.cosmetic_tax.get()!="Rs. 0,0":
              self.txtarea.insert(END,f"\n cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
           self.txtarea.insert(END,f"\n-----------------------------------")

           self.txtarea.insert(END,f"\n-----------------------------------")
           if self.grocery_tax.get()!="Rs. 0,0":
              self.txtarea.insert(END,f"\n grocery Tax\t\t\t{self.grocery_tax.get()}")
           self.txtarea.insert(END,f"\n-----------------------------")
            
           if self.cold_drink_tax.get()!="Rs. 0,0":
              self.txtarea.insert(END,f"\n cold drink Tax\t\t\t{self.cold_drink_tax.get()}")

           self.txtarea.insert(END,f"\n Total Bill : \t\t\t Rs. {str(self.Total_bill)}")
           self.txtarea.insert(END,f"\n-----------------------------")
           self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
          self.bill_data=self.txtarea.get('1.0',END)
          f1=open("bills/"+str(self.bill_no.get())+".txt","w")
          f1.write(self.bill_data)
          f1.close()
          messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} saved Successfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listedir("bills/"):
           if i.split('.')[0]==self.search_bill.get():
               f1=open(f"bills/(i)","r")
               self.txtarea.delete('1.0',END)
               for d in f1:
                       self.txtarea.insert(END,d)
               f1.close()
               present="yes"
        if present=="no":
           messagebox.showerror("Error","Invalid Bil No.")

    def clear_data(self):
         op=messagebox.askyesno("clear","Do you want to clear?")
         if op>0:



        #==========Cosmetics=========
          self.soap.set(0)
         self.face_cream.set(0)
         self.face_wash.set(0)
         self.spray.set(0)
         self.gell.set(0)
         self.loshan.set(0)
         #===========grocery======
         self.rice.set(0)
         self.food_oil.set(0)
         self.daal.set(0)
         self.wheat.set(0)
         self.sugar.set(0)
         self.tea.set(0)
         
         #==========cold drinks=========
         self.maaza.set(0)
         self.cock.set(0)
         self.frooti.set(0)
         self.thumsup.set(0)
         self.limca.set(0)
         self.sprit.set(0)
         #======Totel Product Price &Tax Variable=====
         self.cosmetic_price.set("")
         self.grocery_price.set("")
         self.cold_drink_price.set("")


         self.cosmetic_tax.set("")
         self.grocery_tax.set("")
         self.cold_drink_tax.set("")

         #=======Customer====
         self.c_name.set("")
         self.c_phon.set("")
         self.bill_no.set("")
         x=random.randint(1000,9999)
         self.bill_no.set(str(x))


         self.search_bill.set("")
         self.Welcome_bill()

    def Exit_app(self):
       op=messagebox.askyesno("Exit","Do you want to exit?")
       if op>0:
            self.root.destroy()


            


root=Tk()
obj = Bill_App(root)
root.mainloop()
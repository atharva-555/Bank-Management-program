from tkinter import*
from tkinter import messagebox
from tkinter import Entry
from tkinter import ttk
root=Tk()





#--------------------------------------------------------------#

#-------------------------UPDATE------------------------#
#------------------------DETAILS------------------------#
def updatewindow():
	updatewindow=Toplevel(root)
	updatewindow.resizable(0,0)
	updatewindow.title('ENTER ACCOUNT DETAILS')
	updatewindow.geometry("1190x460")
	
	space31=Label(text="")
	space31.grid(row=0)
	space32=Label(updatewindow,text="")
	space32.grid(row=1)
	space33=Label(updatewindow,text="")
	space33.grid(row=2)
	space34=Label(updatewindow,text="")
	space34.grid(row=12)
	
	centacc=Label(updatewindow,text="ENTER ACCOUNT NUMBER",font='Futura 16 bold underline',relief="ridge",borderwidth=6,width=22)
	
	centacc.grid(row=7,column=0,sticky='nsew')
	
	centpass=Label(updatewindow,text="ENTER PASSWORD",font='Futura 16 bold underline',relief="ridge",borderwidth=6)
	
	space39=Label(updatewindow,text="")
	space39.grid(row=9)
	space40=Label(updatewindow,text="")
	space40.grid(row=10)
	
	centpass.grid(row=11,column=0,sticky='nsew')
	
	global updateacc
	updateacc= Entry(updatewindow, width=69,bd=4)
	updateacc.grid(row=7, column=1,sticky='nsew')
	
	global updateenterpass
	
	updateenterpass= Entry(updatewindow,width=69,bd=4,show="*")
	updateenterpass.grid(row=11,column=1,sticky='nsew')
	
	Nxt4=Button(updatewindow,command=checkaccnumber11111,text='NEXT',borderwidth = 6,width =49,relief="raised",font='Futura 16 bold underline',justify=CENTER)
	Nxt4.grid(row=14,column=0,columnspan=20,sticky='nsew')
	spc0=Label(updatewindow,text="")
	spc0.grid(row=13)

def checkaccnumber11111 ():
	import sqlite3
	global con   
	con=sqlite3.connect('globalbank.db')
	global c
	c=con.cursor()           
	c.execute("SELECT name FROM sqlite_master WHERE type='table';")
	global upla
	upla=c.fetchall()
	global ujnkl	
	ujnkl=(''.join(map(str,upla)))
	
	global uop111
	uop111=updateacc.get()
	global UOP111
	UOP111=updateenterpass.get()
	
	if uop111 in ujnkl:
		con=sqlite3.connect('globalbank.db')
		c=con.cursor()  
		c.execute("SELECT * FROM "+"\'"+uop111+"\'"+"WHERE Account_number="+"\'"+uop111+"\'")
		crecords=c.fetchall()
		print(crecords)
		for urow in crecords:
			global ujjjjj
			ujjjjj=(urow[1])
			global ummmmm
			ummmmm=(urow[14])
			print(ujjjjj)			
		if UOP111==ujjjjj:
#			c.execute("DROP TABLE"+"\'"+dop111+"\'")
			updatewindow1()
			
		else:
			messagebox.showwarning("ERROR", "YOUR ACCOUNT NUMBER\n           AND\nPASSWORD DON'T MATCH") 
			
	else:
		messagebox.showwarning("ERROR", "PLEASE ENTER \nCORRECT ACCOUNT NUMBER") 
		

	
	con.commit()

 
	con.close() 
def updatefunc():
	inputocc=uOccupation1.get()
	inputpinc=upincode1.get()
	inputemail=uemailid1.get()
	inputtempadd=utempadd1.get()
	inputpermadd=upermanentadd1.get()
	inputphonenum=uphone1.get()
	inputmobinum=umobile1.get()
	inputlandnum=ulandline1.get()
	
	if inputocc !="" and inputpinc !="" and inputemail !="" and inputtempadd !="" and inputpermadd !="" and inputphonenum !="" and inputmobinum !="":
		con=sqlite3.connect('globalbank.db')
		c=con.cursor()
		c.execute("UPDATE "+"\'"+uop111+"\'"+" SET Occupation=?,Pincode=?,Email_id=?,Temporary_address=?,Permanent_address=?,Phone_number=?,Mobile_number=?,Landline_number=? WHERE Account_number="+"\'"+uop111+"\'",(inputocc,inputpinc,inputemail,inputtempadd,inputpermadd,inputphonenum,inputmobinum,inputlandnum))
		con.commit()
		updatewindowlast()
	else:
		messagebox.showwarning("ERROR", "PLEASE FILL ALL THE DETAILS!") 
	
	
	

def updatewindow1():
	updatewindow1=Toplevel(root)
	updatewindow1.resizable(0,0)
	updatewindow1.title('UPDATE DETAILS')
	updatewindow1.geometry("1275x675")
	
	
	con=sqlite3.connect('globalbank.db')
	c=con.cursor()
	c.execute("SELECT * FROM "+"\'"+uop111+"\'"+"WHERE Account_number="+"\'"+uop111+"\'")
	records=c.fetchall()
	for row in records:
		foroccu=row[10]
		forpinco=row[8]
		foremail=row[9]
		fortempad=row[6]
		forpermad=row[7]
		forphnnum=row[11]
		formobnum=row[12]
		forlandno=row[13]
		

	updatestatement=Label(updatewindow1,borderwidth =14,width =50,pady="10",relief="ridge",bg="#FFF1A5",font='Futura 20 bold underline',text="UDATE INFORMATION")
	updatestatement.grid(row="0",column="0",columnspan="3",sticky='nsew')
	spc=Label(updatewindow1,text="")
	spc.grid(row=1)
	uOccupation= Label(updatewindow1,text="Occupation",borderwidth =3,width =32,relief="sunken",font='Futura 12')
	uOccupation.grid(row=2,column=1,sticky='nsew')
	global uOccupation1
	uOccupation1= Entry(updatewindow1, width=82,bd=3)
	uOccupation1.insert(0,foroccu)
	uOccupation1.grid(row=2,column=2,sticky='nsew')
	
	upincode= Label(updatewindow1,text="Pincode",borderwidth =3,width =32,relief="sunken",font='Futura 12')
	upincode.grid(row=3,column=1,sticky='nsew')
	global upincode1
	upincode1= Entry(updatewindow1, width=82,bd=3)
	upincode1.insert(0,forpinco)
	upincode1.grid(row=3,column=2,sticky='nsew')
	
	uemailid= Label(updatewindow1,text="Email id",borderwidth =3,width =32,relief="sunken",font='Futura 12')
	uemailid.grid(row=4,column=1,sticky='nsew')
	
	
	global uemailid1
	uemailid1= Entry(updatewindow1, width=82,bd=3)
	uemailid1.insert(0,foremail)
	uemailid1.grid(row=4,column=2,sticky='nsew')
	
	
	utempadd= Label(updatewindow1,text="Temporary Adress",borderwidth =3,width =32,relief="sunken",font='Futura 12')
	utempadd.grid(row=5,column=1,sticky='nsew')
	
	global utempadd1
	utempadd1= Entry(updatewindow1, width=82,bd=3)
	utempadd1.insert(0,fortempad)
	utempadd1.grid(row=5,column=2,sticky='nsew')
	
	upermanentadd= Label(updatewindow1,text="Permanent Adress",borderwidth =3,width =32,relief="sunken",font='Futura 12')
	upermanentadd.grid(row=6,column=1,sticky='nsew')
	
	global upermanentadd1
	upermanentadd1= Entry(updatewindow1, width=82,bd=3)
	upermanentadd1.insert(0,forpermad)
	upermanentadd1.grid(row=6,column=2,sticky='nsew')
	
	
	uphone= Label(updatewindow1,text="Phone number",borderwidth =3,width =32,relief="sunken",font='Futura 12')
	uphone.grid(row=7,column=1,sticky='nsew')
	
	global uphone1
	uphone1= Entry(updatewindow1, width=82,bd=3)
	uphone1.insert(0,forphnnum)
	uphone1.grid(row=7,column=2,sticky='nsew')
	
	umobile= Label(updatewindow1,text="Mobile number",borderwidth =3,width =32,relief="sunken",font='Futura 12')
	umobile.grid(row=8,column=1,sticky='nsew')
	
	global umobile1
	umobile1= Entry(updatewindow1, width=82,bd=3)
	umobile1.insert(0,formobnum)
	umobile1.grid(row=8,column=2,sticky='nsew')
	
	ulandline= Label(updatewindow1,text="Landline number",borderwidth =3,width =32,relief="sunken",font='Futura 12')
	ulandline.grid(row=9,column=1,sticky='nsew')
	
	global ulandline1
	ulandline1= Entry(updatewindow1, width=82,bd=3)
	ulandline1.insert(0,forlandno)
	ulandline1.grid(row=9,column=2,sticky='nsew')
	
	
	spc1=Label(updatewindow1,text="")
	spc1.grid(row=10)
	
	updatebut=Button(updatewindow1,font='Futura 15 bold underline',text="UPDATE DETAILS",relief="raised",width=26,borderwidth=5,command=updatefunc)
	updatebut.grid(row=11,column=1,sticky='nsw')
	
	updatepassbut=Button(updatewindow1,font='Futura 15 bold underline',text="CHANGE PASSWORD",relief="raised",width=19,borderwidth=6,command=changepass)
	updatepassbut.grid(row=11,column=2,sticky='nsw')
	
	updatequitbut=Button(updatewindow1,font='Futura 15 bold underline',text="CLICK TO  QUIT",relief="raised",width=19,borderwidth=5,command=root.destroy)
	updatequitbut.grid(row=11,column=2,sticky='nse')
	
def updatewindowlast():
	updatewindowlast=Toplevel(root)
	updatewindowlast.resizable(0,0)
	updatewindowlast.title('THANK YOU FOR USING OUR SERVICES')
	updatewindowlast.geometry("965x320")
	
	spcclose=Label(updatewindowlast,text="")
	spcclose.grid(row=0,column=0)
	
	prodone=Label(updatewindowlast,font='Futura 15 bold underline',text="PROCESS DONE!",relief="ridge",borderwidth=6,width=48)
	prodone.grid(row=1,column=0,columnspan=14,sticky='nsew')
	
	spcclose7=Label(updatewindowlast,text="")
	spcclose7.grid(row=3,column=0)
	youtrans=("YOUR DETAILS ARE UPDATED.")
	
	spcclose3=Label(updatewindowlast,text="")
	spcclose3.grid(row=4,column=0)
	
	prodone3=Label(updatewindowlast,font='Futura 15 bold underline',text="THANK YOU FOR USING OUR SERVICES",relief="ridge",borderwidth=6,width=48)
	prodone3.grid(row=6,column=0,columnspan=14,sticky='nsew')
	
	clicktocut=Button(updatewindowlast,font='Futura 15 bold underline',text="CLICK TO QUIT",relief="raised",width=48,borderwidth=6,command=root.destroy)
	clicktocut.grid(row=8,column=0,columnspan=14,sticky='nsew')
	
	spcclose6=Label(updatewindowlast,text="")
	spcclose7.grid(row=7,column=0)
	
def changepass():
	changepass=Toplevel(root)
	changepass.resizable(0,0)
	changepass.title('ENTER ACCOUNT DETAILS')
	changepass.geometry("1190x460")
	
	space31=Label(text="")
	space31.grid(row=0)
	space32=Label(changepass,text="")
	space32.grid(row=1)
	space33=Label(changepass,text="")
	space33.grid(row=2)
	space34=Label(changepass,text="")
	space34.grid(row=12)
	
	centacc=Label(changepass,text="ENTER CURRENT PASSWORD",font='Futura 16 bold underline',relief="ridge",borderwidth=6,width=26)
	
	centacc.grid(row=7,column=0,sticky='nsew')
	
	centpass=Label(changepass,text="NEW PASSWORD",font='Futura 16 bold underline',relief="ridge",borderwidth=6)
	
	space39=Label(changepass,text="")
	space39.grid(row=9)
	space40=Label(changepass,text="")
	space40.grid(row=10)
	
	centpass.grid(row=11,column=0,sticky='nsew')
	
	global updatepass
	updatepass= Entry(changepass, width=65,bd=4,show="*")
	updatepass.grid(row=7, column=1,sticky='nsew')
	
	global updatepasscon
	
	updatepasscon= Entry(changepass,width=65,bd=4,show="*")
	updatepasscon.grid(row=11,column=1,sticky='nsew')
	
	Nxt4=Button(changepass,command=checkpass11111,text='SAVE AND QUIT',borderwidth = 6,width =49,relief="raised",font='Futura 16 bold underline',justify=CENTER)
	Nxt4.grid(row=14,column=0,columnspan=20,sticky='nsew')
	spc0=Label(changepass,text="")
	spc0.grid(row=13)
		
	
def checkpass11111():
	previouspass=updatepass.get()
	confirmpass=updatepasscon.get()
	print(confirmpass)
	
	con=sqlite3.connect('globalbank.db')
	c=con.cursor()  
	c.execute("SELECT * FROM "+"\'"+uop111+"\'"+"WHERE Account_number="+"\'"+uop111+"\'")
	crecords=c.fetchall()
	for urow in crecords:
		global pjjjjj
		pjjjjj=(urow[1])			
	if previouspass==pjjjjj:
		if confirmpass!="":
			c.execute("UPDATE "+"\'"+uop111+"\'"+" SET Password=? WHERE Account_number="+"\'"+uop111+"\'",(confirmpass,))
			con.commit()
			root.destroy()
		else:
			messagebox.showwarning("ERROR", "PLEASE ENTER YOUR NEW PASSWORD") 
	else:
		messagebox.showwarning("ERROR", "OLD PASSWORD DON'T MATCH") 
			
	
	
	
#----------------DEFINING FUNCTION------------#
#___________FOR PASSBOOK LIST_______#
def divide_chunks(l, n): 
    # looping till length l
    for i in range(0, len(l), n):
    	 yield l[i:i + n] 
  

#--------------------------------------------------------------#

#-------------------------PASS------------------------#
#------------------------BOOK--------------------------#

def passbookwindow():
	passbookwindow=Toplevel(root)
	passbookwindow.resizable(0,0)
	passbookwindow.title('ENTER ACCOUNT DETAILS')
	passbookwindow.geometry("1190x460")
	
	space31=Label(text="")
	space31.grid(row=0)
	space32=Label(passbookwindow,text="")
	space32.grid(row=1)
	space33=Label(passbookwindow,text="")
	space33.grid(row=2)
	space34=Label(passbookwindow,text="")
	space34.grid(row=12)
	
	centacc=Label(passbookwindow,text="ENTER ACCOUNT NUMBER",font='Futura 16 bold underline',relief="ridge",borderwidth=6,width=22)
	
	centacc.grid(row=7,column=0,sticky='nsew')
	
	centpass=Label(passbookwindow,text="ENTER PASSWORD",font='Futura 16 bold underline',relief="ridge",borderwidth=6)
	
	space39=Label(passbookwindow,text="")
	space39.grid(row=9)
	space40=Label(passbookwindow,text="")
	space40.grid(row=10)
	
	centpass.grid(row=11,column=0,sticky='nsew')
	
	global passenteracc
	passenteracc= Entry(passbookwindow, width=69,bd=4)
	passenteracc.grid(row=7, column=1,sticky='nsew')
	
	global passcenterpass
	
	passcenterpass= Entry(passbookwindow,width=69,bd=4,show="*")
	passcenterpass.grid(row=11,column=1,sticky='nsew')
	
	Nxt4=Button(passbookwindow,command=showpassbook,text='SEE PASSBOOK',borderwidth = 6,width =49,relief="raised",font='Futura 16 bold underline',justify=CENTER)
	Nxt4.grid(row=14,column=0,columnspan=20,sticky='nsew')
	spc0=Label(passbookwindow,text="")
	spc0.grid(row=13)
	
def showpassbook():
	global con   
	con=sqlite3.connect('globalbank.db')
	global c
	c=con.cursor()           
	c.execute("SELECT name FROM sqlite_master WHERE type='table';")
	global abcd
	abcd=c.fetchall()
	global jklmno	
	jklmno=(''.join(map(str,abcd)))
	


		
			
	global opq
	opq=passenteracc.get()
	
	global OPQ
	OPQ=passcenterpass.get()
	
	if opq in jklmno:
		
		con=sqlite3.connect('globalbank.db')
		c=con.cursor()  
		c.execute("SELECT * FROM "+"\'"+opq+"\'"+"WHERE Account_number="+"\'"+opq+"\'")
		records=c.fetchall()
		for row in records:
			jjj=(row[1])
			

		
		if OPQ==jjj:
			showpassbookwindow1()
		else:
			messagebox.showwarning("ERROR", "YOUR ACCOUNT NUMBER\n           AND\nPASSWORD DON'T MATCH") 
			
	else:
		messagebox.showwarning("ERROR", "PLEASE ENTER \nCORRECT ACCOUNT NUMBER") 
		

	
		con.commit()

 
		con.close() 

def showpassbookwindow1():
	showpassbookwindow1 = Tk()
	showpassbookwindow1.resizable(0,0)
	showpassbookwindow1.title('DIGITAL PASSBOOK')	
	showpassbookwindow1.geometry("1280x760")

# Add some style
	style = ttk.Style()
	#Pick a theme
	style.theme_use("default")
	# Configure our treeview colors
	
	style.configure("Treeview", 
		background="#D3D3D3",
		foreground="black",
		rowheight=48,
		fieldbackground="#D3D3D3"
		)
	# Change selected color
	style.map('Treeview', 
		background=[('selected', 'blue')])
	
	# Create Treeview Frame
	tree_frame = Frame(showpassbookwindow1)
	tree_frame.pack(pady=20)
	
	# Treeview Scrollbar
	tree_scroll = Scrollbar(tree_frame)
	tree_scroll.pack(side=RIGHT, fill=Y)
	
	# Create Treeview
	my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
	# Pack to the screen
	my_tree.pack()
	
	#Configure the scrollbar
	tree_scroll.config(command=my_tree.yview)
	
	# Define Our Columns
	my_tree['columns'] = ("DATE","|", "TRANSACTIONS(PARTICULARS)","|", "BALANCE REMAING")
	
	# Formate Our Columns
	my_tree.column("#0", width=0, stretch=NO)
	my_tree.column("DATE", anchor=CENTER, width=120)
	my_tree.column("|",anchor=CENTER,width=10)
	my_tree.column("TRANSACTIONS(PARTICULARS)",anchor=CENTER, width=780)
	my_tree.column("|", anchor=CENTER, width=10)
	my_tree.column("BALANCE REMAING", anchor=CENTER, width=220)
	
	# Create Headings 
	my_tree.heading("#0", text="", anchor=W)
	my_tree.heading("DATE", text="DATE",anchor=CENTER)
	my_tree.heading("|", text="| ",anchor=CENTER)
	my_tree.heading("TRANSACTIONS(PARTICULARS)", text="TRANSACTIONS(PARTICULARS)", anchor=CENTER)
	my_tree.heading("|", text="|",anchor=CENTER)
	my_tree.heading("BALANCE REMAING", text="BALANCE REMAING", anchor=CENTER)
	con=sqlite3.connect('globalbank.db')
	c=con.cursor()
	c.execute("SELECT * FROM "+"\'"+opq+"\'"+"WHERE Account_number="+"\'"+opq+"\'")
	records=c.fetchall()
	for row in records:
		global opopop
		opopop=(row[2])
		global opopop1
		opopop1=(row[5])
		global opopop2
		opopop2=(row[0])
		global opopop3
		opopop3=(row[3])
		global opopop4
		opopop4=(row[4])
		global opopop5
		opopop5=(row[7])
		global opopop6
		opopop6=(row[8])
		global opopop7
		opopop7=(row[9])
		global opopop8
		opopop8=(row[10])
		global opopop9
		opopop9=(row[11])
		global opopop10
		opopop10=(row[12])
		global opopop11
		opopop11=(row[14])
	row=c.execute("SELECT Date_of_transaction,last_transaction,Balance FROM "+"\'"+opq+"\'")
	keyword=[]
	a=["|"]
	for records in row:
		keyword.append(records[0])
		keyword.append(a)
		keyword.append(records[1])
		keyword.append(a)
		keyword.append(records[2])
	n=5
	x=list(divide_chunks(keyword,n))
	print(x)
	
	global count
	count=0
	my_tree.tag_configure('oddrow', background="white")
	my_tree.tag_configure('evenrow', background="lightblue")

	for record in x:
		if count % 2 == 0:
			my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2],record[3],record[4]), tags=('evenrow',))
		else:
			my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2],record[3],record[4]), tags=('oddrow',))
	
		count += 1
		
	# Create striped row tags
		add_frame=Frame(showpassbookwindow1)
	add_frame.pack(pady=20)
	
	#Labels
	nl = Label(add_frame, text="Account Holder's Name",borderwidth=6,relief='sunken',width=21)
	nl.grid(row=0, column=0)
	
	il = Label(add_frame, text=opopop)
	il.grid(row=0, column=1,sticky='w')
	
	tl = Label(add_frame, text="Date of Birth",borderwidth=6,relief='sunken',width=21)
	tl.grid(row=1, column=0)
	
	tl1 =Label(add_frame, text=opopop1)
	tl1.grid(row=1, column=1,sticky='w')
	
	tl3 =Label(add_frame, text="Account number",borderwidth=6,relief='sunken',width=21)
	tl3.grid(row=2, column=0)
	
	tl2 =Label(add_frame, text=opopop2)
	tl2.grid(row=2,column=1,sticky='w')
	
	tl4 =Label(add_frame, text="Mother's Name",borderwidth=6,relief='sunken',width=21)
	tl4.grid(row=3,column=0)
	
	tl5 =Label(add_frame, text=opopop3)
	tl5.grid(row=3,column=1,sticky='w')	
	tl6=Label(add_frame, text="Father's Name",borderwidth=6,relief='sunken',width=21)
	tl6.grid(row=4,column=0)
	tl7 =Label(add_frame, text=opopop4)
	tl7.grid(row=4,column=1,sticky='w')
	tl8=Label(add_frame, text="Permanent Adress",borderwidth=6,relief='sunken',width=21)
	tl8.grid(row=5,column=0)
	tl9 =Label(add_frame, text=opopop5)
	tl9.grid(row=5,column=1,sticky='w')
	tl10=Label(add_frame, text="Pincode",borderwidth=6,relief='sunken',width=21)
	tl10.grid(row=0,column=2,sticky='w')
	tl11=Label(add_frame, text=opopop6)
	tl11.grid(row=0,column=3,sticky='w')
	tl12=Label(add_frame, text="Email id",borderwidth=6,relief='sunken',width=21)
	tl12.grid(row=1,column=2,sticky='w')
	tl13=Label(add_frame, text=opopop7)
	tl13.grid(row=1,column=3,sticky='w')
	tl14=Label(add_frame, text="Occupation",borderwidth=6,relief='sunken',width=21)
	tl14.grid(row=2,column=2,sticky='w')
	tl15=Label(add_frame, text=opopop8)
	tl15.grid(row=2,column=3,sticky='w')
	tl16=Label(add_frame, text="Phone number",borderwidth=6,relief='sunken',width=21)
	tl16.grid(row=3,column=2,sticky='w')
	tl17=Label(add_frame, text=opopop9)
	tl17.grid(row=3,column=3,sticky='w')
	tl18=Label(add_frame, text="Mobile number",borderwidth=6,relief='sunken',width=21)
	tl18.grid(row=4,column=2,sticky='w')
	tl19=Label(add_frame, text=opopop10)
	tl19.grid(row=4,column=3,sticky='w')
	tl20=Label(add_frame, text="Status",borderwidth=6,relief='sunken',width=21)
	tl20.grid(row=5,column=2,sticky='w')
	tl21=Label(add_frame, text=opopop11)
	tl21.grid(row=5,column=3,sticky='w')	

	# Button
	quitpassbook= Button(add_frame, text="CLICK TO QUIT",command=lambda:[showpassbookwindow1.destroy(),root.destroy()],relief='raised',borderwidth=6,width=89,font='Futura 16 bold underline',justify=CENTER)
	quitpassbook.grid(row=7,column=0,columnspan=14,pady=10,sticky='nsew')
	showpassbookwindow1.mainloop()
	
	 
#-------------------------END------------------------------#

#-------------------------PASS------------------------#
#------------------------BOOK--------------------------#	






#--------------------------------------------------------------#

#--------------------- ACCOUNT-----------------------#
#------------------------DELETION--------------------------#

def deletewindow():
	deletewindow=Toplevel(root)
	deletewindow.resizable(0,0)
	deletewindow.title('ENTER ACCOUNT DETAILS')
	deletewindow.geometry("1190x460")
	
	space31=Label(text="")
	space31.grid(row=0)
	space32=Label(deletewindow,text="")
	space32.grid(row=1)
	space33=Label(deletewindow,text="")
	space33.grid(row=2)
	space34=Label(deletewindow,text="")
	space34.grid(row=12)
	
	centacc=Label(deletewindow,text="ENTER ACCOUNT NUMBER",font='Futura 16 bold underline',relief="ridge",borderwidth=6,width=22)
	
	centacc.grid(row=7,column=0,sticky='nsew')
	
	centpass=Label(deletewindow,text="ENTER PASSWORD",font='Futura 16 bold underline',relief="ridge",borderwidth=6)
	
	space39=Label(deletewindow,text="")
	space39.grid(row=9)
	space40=Label(deletewindow,text="")
	space40.grid(row=10)
	
	centpass.grid(row=11,column=0,sticky='nsew')
	
	global delenteracc
	delenteracc= Entry(deletewindow, width=69,bd=4)
	delenteracc.grid(row=7, column=1,sticky='nsew')
	
	global delenterpass
	
	delenterpass= Entry(deletewindow,width=69,bd=4,show="*")
	delenterpass.grid(row=11,column=1,sticky='nsew')
	
	Nxt4=Button(deletewindow,command=checkaccnumber1111,text='DELETE ACCOUNT',borderwidth = 6,width =49,relief="raised",font='Futura 16 bold underline',justify=CENTER)
	Nxt4.grid(row=14,column=0,columnspan=20,sticky='nsew')
	spc0=Label(deletewindow,text="")
	spc0.grid(row=13)

def checkaccnumber1111 ():
	import sqlite3
	global con   
	con=sqlite3.connect('globalbank.db')
	global c
	c=con.cursor()           
	c.execute("SELECT name FROM sqlite_master WHERE type='table';")
	global cpla
	cpla=c.fetchall()
	global cjnkl	
	cjnkl=(''.join(map(str,cpla)))
	
	global dop111
	dop111=delenteracc.get()
	global DOP111
	DOP111=delenterpass.get()
	
	if dop111 in cjnkl:
		con=sqlite3.connect('globalbank.db')
		c=con.cursor()  
		c.execute("SELECT * FROM "+"\'"+dop111+"\'"+"WHERE Account_number="+"\'"+dop111+"\'")
		crecords=c.fetchall()
		print(crecords)
		for crow in crecords:
			global cjjjjj
			cjjjjj=(crow[1])
			global cmmmmm
			cmmmmm=(crow[14])
			print(cjjjjj)			
		if DOP111==cjjjjj:
			c.execute("DROP TABLE"+"\'"+dop111+"\'")
			deletewindow1()
			
		else:
			messagebox.showwarning("ERROR", "YOUR ACCOUNT NUMBER\n           AND\nPASSWORD DON'T MATCH") 
			
	else:
		messagebox.showwarning("ERROR", "PLEASE ENTER \nCORRECT ACCOUNT NUMBER") 
		

	
	con.commit()

 
	con.close() 
	
def deletewindow1():
	deletewindow1=Toplevel(root)
	deletewindow1.resizable(0,0)
	deletewindow1.title('ACCOUNT DELETION')
	deletewindow1.geometry("960x360")
	
	spcclose=Label(deletewindow1,text="")
	spcclose.grid(row=0,column=0)
	
	prodone=Label(deletewindow1,font='Futura 15 bold underline',text="PROCESS DONE",relief="ridge",borderwidth=6,width=47)
	prodone.grid(row=1,column=0,columnspan=14,sticky='nsew')
	
	spcclose7=Label(deletewindow1,text="")
	spcclose7.grid(row=3,column=0)
	
	prodone1=Label(deletewindow1,font='Futura 15 bold underline',text="YOUR ACCOUNT DELETED",relief="ridge",borderwidth=6,width=49)
	prodone1.grid(row=5,column=0)
	
	spcclose3=Label(deletewindow1,text="")
	spcclose3.grid(row=4,column=0)
	
	prodone3=Label(deletewindow1,font='Futura 15 bold underline',text="Sad to see you going!",relief="ridge",borderwidth=6,width=49)
	prodone3.grid(row=6,column=0)
	
	clicktocut=Button(deletewindow1,font='Futura 15 bold underline',text="CLICK TO QUIT",relief="raised",width=47,borderwidth=6,command=root.destroy)
	clicktocut.grid(row=8,column=0,columnspan=14,sticky='nsew')
	
	spcclose6=Label(deletewindow1,text="")
	spcclose7.grid(row=7,column=0)
	
	
	
	
	
	
	
	
#--------------------------------------------------------------#

#---------------------CHEQUE -----------------------#
#------------------------BOOK--------------------------#

def chequebookwindow():
	chequebookwindow=Toplevel(root)
	chequebookwindow.resizable(0,0)
	chequebookwindow.title('ENTER ACCOUNT DETAILS')
	chequebookwindow.geometry("1190x460")
	
	space31=Label(text="")
	space31.grid(row=0)
	space32=Label(chequebookwindow,text="")
	space32.grid(row=1)
	space33=Label(chequebookwindow,text="")
	space33.grid(row=2)
	space34=Label(chequebookwindow,text="")
	space34.grid(row=12)
	
	centacc=Label(chequebookwindow,text="ENTER ACCOUNT NUMBER",font='Futura 16 bold underline',relief="ridge",borderwidth=6,width=22)
	
	centacc.grid(row=7,column=0,sticky='nsew')
	
	centpass=Label(chequebookwindow,text="ENTER PASSWORD",font='Futura 16 bold underline',relief="ridge",borderwidth=6)
	
	space39=Label(chequebookwindow,text="")
	space39.grid(row=9)
	space40=Label(chequebookwindow,text="")
	space40.grid(row=10)
	
	centpass.grid(row=11,column=0,sticky='nsew')
	
	global centeracc
	centeracc= Entry(chequebookwindow, width=69,bd=4)
	centeracc.grid(row=7, column=1,sticky='nsew')
	
	global centerpass
	
	centerpass= Entry(chequebookwindow,width=69,bd=4,show="*")
	centerpass.grid(row=11,column=1,sticky='nsew')
	
	Nxt4=Button(chequebookwindow,command=checkaccnumber111,text='NEXT',borderwidth = 6,width =49,relief="raised",font='Futura 16 bold underline',justify=CENTER)
	Nxt4.grid(row=14,column=0,columnspan=20,sticky='nsew')
	spc0=Label(chequebookwindow,text="")
	spc0.grid(row=13)
	
def checkaccnumber111():
	import sqlite3
	global con   
	con=sqlite3.connect('globalbank.db')
	global c
	c=con.cursor()           
	c.execute("SELECT name FROM sqlite_master WHERE type='table';")
	global cpla
	cpla=c.fetchall()
	global cjnk	
	cjnk=(''.join(map(str,cpla)))
	
	global cop111
	cop111=centeracc.get()
	global OP111
	cOP111=centerpass.get()
	
	if cop111 in cjnk:
		con=sqlite3.connect('globalbank.db')
		c=con.cursor()  
		c.execute("SELECT * FROM "+"\'"+cop111+"\'"+"WHERE Account_number="+"\'"+cop111+"\'")
		crecords=c.fetchall()
		print(crecords)
		for crow in crecords:
			global cjjjj
			cjjjj=(crow[1])
			global cmmmm
			cmmmm=(crow[14])
			print(cjjjj)			
		if cOP111==cjjjj:
			chequebookwindow1()
			
		else:
			messagebox.showwarning("ERROR", "YOUR ACCOUNT NUMBER\n           AND\nPASSWORD DON'T MATCH") 
			
	else:
		messagebox.showwarning("ERROR", "PLEASE ENTER \nCORRECT ACCOUNT NUMBER") 
		

	
	con.commit()

 
	con.close() 
	
	
def chequebookwindow1():
	chequebookwindow1=Toplevel(root)
	chequebookwindow1.resizable(0,0)
	chequebookwindow1.title('THANK YOU FOR USING OUR SERVICES')
	chequebookwindow1.geometry("965x360")
	
	
	spcclose=Label(chequebookwindow1,text="")
	spcclose.grid(row=0,column=0)
	
	askradio=Label(chequebookwindow1,font='Futura 15 bold underline',text="WHERE DO YOU WANT TO RECIEVE CHEQUEBOOK?",relief="ridge",borderwidth=6,width=48)
	askradio.grid(row=1,column=0,columnspan=14,sticky='nsew')
	spcclose=Label(chequebookwindow1,text="")
	spcclose.grid(row=2,column=0)
	global radio	
	radio=IntVar()
	rb=Radiobutton(chequebookwindow1,text="Permanent Address                                                      ",variable=radio,value=1,anchor=CENTER,font="futura 12 bold",justify=LEFT)
	rb.grid(row=3,column=1)
	rb1=Radiobutton(chequebookwindow1,text="Temporary Adress                                                        ",variable=radio,value=2,anchor=CENTER,font="futura 12 bold",justify=LEFT)
	rb1.grid(row=4,column=1)
	rb2=Radiobutton(chequebookwindow1,text="YOU WILL COLLECT IT FROM NEAREST BRANCH",variable=radio,font="futura 12 bold",value=3,anchor=CENTER,justify=LEFT)
	rb2.grid(row=5,column=1)
	
	spcclose=Label(chequebookwindow1,text="")
	spcclose.grid(row=6,column=0)
	next=Button(chequebookwindow1,font='Futura 15 bold underline',text="NEXT",relief="raised",width=48,borderwidth=6,command=done)
	next.grid(row=7,column=0,columnspan=14,sticky='nsew')

def done():
	if radio.get()==1:
		done=Toplevel(root)
		done.resizable(0,0)
		done.title('THANK YOU FOR USING OUR SERVICES')
		done.geometry("965x360")
	
		spcclose=Label(done,text="")
		spcclose.grid(row=0,column=0)
	
		prodone=Label(done,font='Futura 15 bold underline',text="PROCESS DONE!",relief="ridge",borderwidth=6,width=48)
		prodone.grid(row=1,column=0,columnspan=14,sticky='nsew')
	
		spcclose7=Label(done,text="")
		spcclose7.grid(row=3,column=0)
		youtrans=("YOU WILL RECIEVE YOU CHEQUE BOOK ON YOUR\nPERMANENT ADDRESS WITHIN 7 WORKING DAYS.")
		tanscomplete1=Label(done,font='Futura 15 bold underline',text=youtrans,relief="ridge",borderwidth=6,width=48)
		tanscomplete1.grid(row=5,column=0,columnspan=14,sticky='nsew')
	
		spcclose3=Label(done,text="")
		spcclose3.grid(row=4,column=0)
	
		prodone3=Label(done,font='Futura 15 bold underline',text="THANK YOU FOR USING OUR SERVICES",relief="ridge",borderwidth=6,width=48)
		prodone3.grid(row=6,column=0,columnspan=14,sticky='nsew')
	
		clicktocut=Button(done,font='Futura 15 bold underline',text="CLICK TO QUIT",relief="raised",width=48,borderwidth=6,command=root.destroy)
		clicktocut.grid(row=8,column=0,columnspan=14,sticky='nsew')
	
		spcclose6=Label(done,text="")
		spcclose7.grid(row=7,column=0)
#		global con   
#		con=sqlite3.connect('globalbank.db')
#		global c
#		c=con.cursor()           
#		c.execute("SELECT name FROM sqlite_master WHERE type='table';")
#		c.execute("ALTER TABLE "+"\'"+cop111+"\'"+"ADD COLUMN CHEQUE_BOOK_STATUS")
#		c.execute("UPDATE "+"\'"+cop111+"\'"+" SET CHEQUE_BOOK_STATUS='IT WILL BE SENT TO YOUR PERMANENT ADRRESS WITHIN 7 WORKING DAYS' WHERE Account_number="+"\'"+cop111+"\'")
#	else:
#		pass
	if radio.get()==2:
		done=Toplevel(root)
		done.resizable(0,0)
		done.title('THANK YOU FOR USING OUR SERVICES')
		done.geometry("965x360")
	
		spcclose=Label(done,text="")
		spcclose.grid(row=0,column=0)
	
		prodone=Label(done,font='Futura 15 bold underline',text="PROCESS DONE!",relief="ridge",borderwidth=6,width=48)
		prodone.grid(row=1,column=0,columnspan=14,sticky='nsew')
	
		spcclose7=Label(done,text="")
		spcclose7.grid(row=3,column=0)
		youtrans=("YOU WILL RECIEVE YOU CHEQUE BOOK ON YOUR\n TEMPORARY ADRESS WITHIN 7 WORKING DAYS.")
		tanscomplete1=Label(done,font='Futura 15 bold underline',text=youtrans,relief="ridge",borderwidth=6,width=48)
		tanscomplete1.grid(row=5,column=0,columnspan=14,sticky='nsew')
	
		spcclose3=Label(done,text="")
		spcclose3.grid(row=4,column=0)
	
		prodone3=Label(done,font='Futura 15 bold underline',text="THANK YOU FOR USING OUR SERVICES",relief="ridge",borderwidth=6,width=48)
		prodone3.grid(row=6,column=0,columnspan=14,sticky='nsew')
	
		clicktocut=Button(done,font='Futura 15 bold underline',text="CLICK TO QUIT",relief="raised",width=48,borderwidth=6,command=root.destroy)
		clicktocut.grid(row=8,column=0,columnspan=14,sticky='nsew')
	
		spcclose6=Label(done,text="")
		spcclose7.grid(row=7,column=0)
#		c.execute("SELECT name FROM sqlite_master WHERE type='table';")
#		c.execute("ALTER TABLE "+"\'"+cop111+"\'"+"ADD COLUMN CHEQUE_BOOK_STATUS")

#		c.execute("UPDATE "+"\'"+cop111+"\'"+" SET CHEQUE_BOOK_STATUS='IT WILL BE SENT TO YOUR TEMPORARY ADRRESS WITHIN 7 WORKING DAYS' WHERE Account_number="+"\'"+cop111+"\'")
#	else:
#		pass
	if radio.get()==3:
		done=Toplevel(root)
		done.resizable(0,0)
		done.title('THANK YOU FOR USING OUR SERVICES')
		done.geometry("965x360")
	
		spcclose=Label(done,text="")
		spcclose.grid(row=0,column=0)
	
		prodone=Label(done,font='Futura 15 bold underline',text="PROCESS DONE!",relief="ridge",borderwidth=6,width=48)
		prodone.grid(row=1,column=0,columnspan=14,sticky='nsew')
	
		spcclose7=Label(done,text="")
		spcclose7.grid(row=3,column=0)
		youtrans=("PLEASE COLLECT CHEQUE BOOK FROM\nNEAREST BRANCH WITHIN 7 DAYS")
		tanscomplete1=Label(done,font='Futura 15 bold underline',text=youtrans,relief="ridge",borderwidth=6,width=48)
		tanscomplete1.grid(row=5,column=0,columnspan=14,sticky='nsew')
	
		spcclose3=Label(done,text="")
		spcclose3.grid(row=4,column=0)
	
		prodone3=Label(done,font='Futura 15 bold underline',text="THANK YOU FOR USING OUR SERVICES",relief="ridge",borderwidth=6,width=48)
		prodone3.grid(row=6,column=0,columnspan=14,sticky='nsew')
	
		clicktocut=Button(done,font='Futura 15 bold underline',text="CLICK TO QUIT",relief="raised",width=48,borderwidth=6,command=root.destroy)
		clicktocut.grid(row=8,column=0,columnspan=14,sticky='nsew')
	
		spcclose6=Label(done,text="")
		spcclose7.grid(row=7,column=0)	
			          
#		c.execute("SELECT name FROM sqlite_master WHERE type='table';")
#		c.execute("ALTER TABLE "+"\'"+cop111+"\'"+"ADD COLUMN CHEQUE_BOOK_STATUS")
#		c.execute("UPDATE "+"\'"+cop111+"\'"+" SET CHEQUE_BOOK_STATUS='COLLECT IT FROM NEAREST BRANCH WITHIN 7 WORKING DAYS' WHERE Account_number="+"\'"+cop111+"\'")
#		con.commit()
 
#		con.close()
#	else:
#		pass




#---------------------------END----------------------------#

#---------------------CHEQUE -----------------------#
#------------------------BOOK--------------------------#







#--------------------------------------------------------------#

#---------------------TRANSFER --------------------#
#------------------------MONEY------------------------#





#--------------------------------------------------------------#
	
def transferwindowp():
	transferwindowp= Toplevel(root)
	transferwindowp.resizable(0,0)
	transferwindowp.title('TRANSFER MONEY')
	transferwindowp.geometry("1190x520")

	space31=Label(transferwindowp,text="")
	space31.grid(row=0)
	space32=Label(transferwindowp,text="")
	space32.grid(row=1)
	space33=Label(transferwindowp,text="")
	space33.grid(row=2)
	space34=Label(transferwindowp,text="")
	space34.grid(row=12)
	
	entaccpp=Label(transferwindowp,text="ENTER YOUR ACCOUNT NO.",font='Futura 16 bold underline',relief="ridge",borderwidth=6,width=23)
	
	entaccpp.grid(row=7,column=0,sticky='nsew')
	
	entpasspp=Label(transferwindowp,text="ENTER YOUR PASSWORD",font='Futura 16 bold underline',relief="ridge",borderwidth=6)
	
	space39=Label(transferwindowp,text="")
	space39.grid(row=9)
	space40=Label(transferwindowp,text="")
	space40.grid(row=10)
	
	entpasspp.grid(row=11,column=0,sticky='nsew')
	
	global enteraccppp
	enteraccppp= Entry(transferwindowp, width=68,bd=4)
	enteraccppp.grid(row=7, column=1,sticky='nsew')
	
	global enterpassppp
	
	enterpassppp= Entry(transferwindowp,width=68,bd=4,show="*")
	enterpassppp.grid(row=11,column=1,sticky='nsew')
	
	Nxt4=Button(transferwindowp,command=checkacc3,text='NEXT',borderwidth = 6,width =48,relief="raised",font='Futura 16 bold underline',justify=CENTER)
	Nxt4.grid(row=14,column=0,columnspan=20,sticky='nsew')
	spc0=Label(transferwindowp,text="")
	spc0.grid(row=13)
		
def checkacc3():
	global eq2
	eq2=enteraccppp.get()
	global EQ
	EQ2=enterpassppp.get()
	import sqlite3
	global con   
	con=sqlite3.connect('globalbank.db')
	global c
	c=con.cursor()           
	c.execute("SELECT name FROM sqlite_master WHERE type='table';")
	global a
	ola=c.fetchall()
	global MH	
	MH=(''.join(map(str,ola)))
	
	
	if eq2 in MH:
		
		con=sqlite3.connect('globalbank.db')
		c=con.cursor()  
		c.execute("SELECT * FROM "+"\'"+eq2+"\'"+"WHERE Account_number="+"\'"+eq2+"\'")
		records=c.fetchall()
		for row in records:
			jjjjj=(row[1])
			

		
		if EQ2 ==jjjjj:
			transferwindow1()
		else:
			messagebox.showwarning("ERROR", "YOUR ACCOUNT NUMBER\n           AND\nPASSWORD DON'T MATCH") 
			
	else:
		messagebox.showwarning("ERROR", "PLEASE ENTER \nCORRECT ACCOUNT NUMBER") 
		

	
	con.commit()

 
	con.close() 
	
	
def transferwindow1():
	transferwindow1= Toplevel(root)
	transferwindow1.resizable(0,0)
	transferwindow1.title('ENTER DETAILS')
	transferwindow1.geometry("1190x520")

	space31=Label(transferwindow1,text="")
	space31.grid(row=0)
	space32=Label(transferwindow1,text="")
	space32.grid(row=1)
	space33=Label(transferwindow1,text="")
	space33.grid(row=2)
	space34=Label(transferwindow1,text="")
	space34.grid(row=12)
	
	entaccd=Label(transferwindow1,text="TRANSFER TO ACCOUNT\nNUMBER:",font='Futura 16 bold underline',relief="ridge",borderwidth=6)
	
	entaccd.grid(row=7,column=0,sticky='nsew')
	
	entercon=Label(transferwindow1,text="AMOUNT TO BE TRANSFERED",font='Futura 16 bold underline',relief="ridge",borderwidth=6)
	
	space39=Label(transferwindow1,text="")
	space39.grid(row=9)
	space40=Label(transferwindow1,text="")
	space40.grid(row=10)
	
	entercon.grid(row=11,column=0,sticky='nsew')
	
	global enteraccdd
	enteraccdd= Entry(transferwindow1, width=68,bd=4)
	enteraccdd.grid(row=7, column=1,sticky='nsew')
	
	global entercondd
	
	entercondd= Entry(transferwindow1,width=68,bd=4)
	entercondd.grid(row=11,column=1,sticky='nsew')
	
	Nxt4=Button(transferwindow1,command=transfer_func,text='NEXT',borderwidth = 6,width =48,relief="raised",font='Futura 16 bold underline',justify=CENTER)
	Nxt4.grid(row=14,column=0,columnspan=20,sticky='nsew')
	spc0=Label(transferwindow1,text="")
	spc0.grid(row=13)

import sqlite3  	
def transfer_func():
	global con   
	con=sqlite3.connect('globalbank.db')
	global c
	c=con.cursor()           
	c.execute("SELECT name FROM sqlite_master WHERE type='table';")
	global ama
	ama=c.fetchall()
	global jk5	
	jk5=(''.join(map(str,ama)))
	mbb=enteraccdd.get()
		
			
	global ap
	ap=enteraccdd.get()
	
	global AP
	AP=entercondd.get()		
	
	if mbb in jk5:		
		c.execute("SELECT * FROM "+"\'"+mbb+"\'"+"WHERE Account_number="+"\'"+mbb+"\'")
		records=c.fetchall()
		for row in records:
			global mmmmmm
			mmmmmm=(row[2])
			con=sqlite3.connect('globalbank.db')
			c=con.cursor()  
			c.execute("SELECT * FROM "+"\'"+eq2+"\'"+"WHERE Account_number="+"\'"+eq2+"\'")
		records=c.fetchall()
		for row in records:
			global mmmmm
			mmmmm=(row[14])
			global nameoftrans
			nameoftrans=str(row[2])
		if mmmmm=='ACTIVATED':
			if int(AP)<=50000:
				con=sqlite3.connect('globalbank.db')	
				c=con.cursor()  
				c.execute("SELECT * FROM "+"\'"+eq2+"\'")
				records=c.fetchall()
				for row in records:
					global klmno
					klmno=(row[17])
				if klmno>=int(AP):					
					c.execute("SELECT * FROM "+"\'"+eq2+"\'")
					records=c.fetchall()
					for row in records:
						global jjjjjj
						jjjjjj=(row[17])
					global ikiii
					ikiii=(int(jjjjjj)-int(AP))
					jpg=str(AP)
					global transfrmoney
					transfrmoney=("TRANSFERED Rs."+" "+jpg+" "+"TO"+" "+mmmmmm)
					c.execute("INSERT INTO" +"\'"+eq2+"\'"+"(Date_of_transaction,last_transaction,Balance)VALUES(date('now'),?,?)",(transfrmoney,ikiii))



					c.execute("SELECT * FROM "+"\'"+mbb+"\'")
					records1=c.fetchall()
					for row1 in records1:
						global jjjjjjb
						jjjjjjb=(row1[17])
						print(jjjjjjb)
					global ikiiii
					ikiiii=(int(jjjjjjb)+int(AP))
					jpg=str(AP)
					transfermoney11=(nameoftrans+" "+"TRANSFERED Rs."+" "+jpg+" "+"TO YOUR ACCOUNT")
					c.execute ("INSERT INTO" +"\'"+mbb+"\'"+"(Date_of_transaction,last_transaction,Balance)VALUES(date('now'),?,?)",(transfermoney11,ikiiii))

					con.commit()
					con.close() 
					transferwindowl()
				else:
					messagebox.showwarning("ERROR", "YOU DON'T HAVE ENOUGH BALANCE")  
#______________
				
			else:
				messagebox.showwarning("ERROR", "YOU CAN TRANSFER\n RS.50000 in one time.")  
		else:
			messagebox.showwarning("ERROR", "YOUR ACCCOUNT IS DEACTIVE\nTO START TRANSACTIONS \nPLEASE ACTIVATE YOUR ACCOUNT.") 
	else:
		messagebox.showwarning("ERROR", "PLEASE ENTER \nCORRECT ACCOUNT NUMBER") 
				

def transferwindowl():
	transferwindowl=Toplevel(root)
	transferwindowl.resizable(0,0)
	transferwindowl.title('THANK YOU FOR USING OUR SERVICES')
	transferwindowl.geometry("965x360")
	
	spcclose=Label(transferwindowl,text="")
	spcclose.grid(row=0,column=0)
	
	
	
	spcclose7=Label(transferwindowl,text="")
	spcclose7.grid(row=3,column=0)
	
	youtrans=("YOU TRANSFERED Rs."+" "+str(AP)+" "+"TO"+" "+"\n"+mmmmmm)
	
	tanscomplete1=Label(transferwindowl,font='Futura 15 bold underline',text=youtrans,relief="ridge",borderwidth=6,width=48)
	tanscomplete1.grid(row=5,column=0,columnspan=14,sticky='nsew')
	
	transbal=("YOUR REMAINING BALANCE IS RS."+" "+str(ikiii))
	tanscomplete2=Label(transferwindowl,font='Futura 15 bold underline',text=transbal,relief="ridge",borderwidth=6,width=48)
	tanscomplete2.grid(row=6,column=0,columnspan=14,sticky='nsew')
	
	spcclose3=Label(transferwindowl,text="")
	spcclose3.grid(row=4,column=0)
	
	
	clicktocut=Button(transferwindowl,font='Futura 15 bold underline',text="CLICK TO QUIT",relief="raised",width=48,borderwidth=6,command=root.destroy)
	clicktocut.grid(row=8,column=0,columnspan=14,sticky='nsew')
	
	spcclose6=Label(transferwindowl,text="")
	spcclose7.grid(row=7,column=0)

#________________________________________#
#--------------------------END-------------------------------#
#---------------TRANSFER MONEY-------------------------#
#________________________________________#
		
	
		
			





#________________________________________#
#----------------------WITHDRAW---------------------#
#------------------------MONEY--------------------------#
#________________________________________#


def withdrawwindow():
	withdrawwindow=Toplevel(root)
	withdrawwindow.resizable(0,0)
	withdrawwindow.title('ENTER ACCOUNT DETAILS')
	withdrawwindow.geometry("1190x460")
	
	space31=Label(text="")
	space31.grid(row=0)
	space32=Label(withdrawwindow,text="")
	space32.grid(row=1)
	space33=Label(withdrawwindow,text="")
	space33.grid(row=2)
	space34=Label(withdrawwindow,text="")
	space34.grid(row=12)
	
	wentacc=Label(withdrawwindow,text="ENTER ACCOUNT NUMBER",font='Futura 16 bold underline',relief="ridge",borderwidth=6,width=22)
	
	wentacc.grid(row=7,column=0,sticky='nsew')
	
	wentpass=Label(withdrawwindow,text="ENTER PASSWORD",font='Futura 16 bold underline',relief="ridge",borderwidth=6)
	
	space39=Label(withdrawwindow,text="")
	space39.grid(row=9)
	space40=Label(withdrawwindow,text="")
	space40.grid(row=10)
	
	wentpass.grid(row=11,column=0,sticky='nsew')
	
	global wenteracc
	wenteracc= Entry(withdrawwindow, width=69,bd=4)
	wenteracc.grid(row=7, column=1,sticky='nsew')
	
	global wenterpass
	
	wenterpass= Entry(withdrawwindow,width=69,bd=4,show="*")
	wenterpass.grid(row=11,column=1,sticky='nsew')
	
	Nxt4=Button(withdrawwindow,command=checkaccnumber11,text='NEXT',borderwidth = 6,width =49,relief="raised",font='Futura 16 bold underline',justify=CENTER)
	Nxt4.grid(row=14,column=0,columnspan=20,sticky='nsew')
	spc0=Label(withdrawwindow,text="")
	spc0.grid(row=13)
	
def checkaccnumber11():
	import sqlite3
	global con   
	con=sqlite3.connect('globalbank.db')
	global c
	c=con.cursor()           
	c.execute("SELECT name FROM sqlite_master WHERE type='table';")
	global pla
	pla=c.fetchall()
	global jnk	
	jnk=(''.join(map(str,pla)))
	
	global op111
	op111=wenteracc.get()
	global OP111
	OP111=wenterpass.get()
	
	if op111 in jnk:
		con=sqlite3.connect('globalbank.db')
		c=con.cursor()  
		c.execute("SELECT * FROM "+"\'"+op111+"\'"+"WHERE Account_number="+"\'"+op111+"\'")
		records=c.fetchall()
		print(records)
		for row in records:
			global jjjj
			jjjj=(row[1])
			global mmmm
			mmmm=(row[14])
			print(jjjj)			
		if OP111==jjjj:
			withdrawwindow1()
			
		else:
			messagebox.showwarning("ERROR", "YOUR ACCOUNT NUMBER\n           AND\nPASSWORD DON'T MATCH") 
			
	else:
		messagebox.showwarning("ERROR", "PLEASE ENTER \nCORRECT ACCOUNT NUMBER") 
		

	
	con.commit()

 
	con.close() 
	
	
def withdrawwindow1():
	withdrawwindow1=Toplevel(root)
	withdrawwindow1.resizable(0,0)
	withdrawwindow1.title('WITHDRAW MONEY')
	withdrawwindow1.geometry("1185x460")
	
	
	space31=Label(text="")
	space31.grid(row=0)
	space32=Label(withdrawwindow1,text="")
	space32.grid(row=1)
	space33=Label(withdrawwindow1,text="")
	space33.grid(row=2)
	space34=Label(withdrawwindow1,text="")
	space34.grid(row=12)
	
	wentacc=Label(withdrawwindow1,text="AMOUNT OF MONEY TO\nWITHDRAW(IN RUPEES)",font='Futura 15 bold underline',relief="ridge",borderwidth=6,width=24)
	
	wentacc.grid(row=7,column=0,sticky='nsew')
	
	global var6
	var6= StringVar()
	
	global wchkmoney
	wchkmoney=Checkbutton(withdrawwindow1,text="CLICK HERE TO PROCEED ",borderwidth = 8,width =51,relief="sunken",font='Futura 11 bold',variable=var6, onvalue="on", offvalue="off")
	wchkmoney.deselect()
	
	
	space39=Label(withdrawwindow1,text="")
	space39.grid(row=9)
	space40=Label(withdrawwindow1,text="")
	space40.grid(row=10)
	
	wchkmoney.grid(row=11,sticky='nsew',columnspan=14)
	
	global wentermone
	wentermone= Entry(withdrawwindow1, width=70,bd=4)
	wentermone.grid(row=7, column=1,sticky='nsew')
		
	Nxt4=Button(withdrawwindow1,command=withdrawfunc,text='WITHDRAW MONEY',borderwidth = 6,width =49,relief="raised",font='Futura 16 bold underline',justify=CENTER)
	Nxt4.grid(row=14,column=0,columnspan=20,sticky='nsew')
	spc0=Label(withdrawwindow1,text="")
	spc0.grid(row=13)
	
	
def withdrawfunc():
	if var6.get()=="on":
		global wgotmoney
		wgotmoney=wentermone.get()
		global withdrawmoney
		withdrawmoney=("DEBITED RUPEES "+wgotmoney)
		print(withdrawmoney)
		
		if int(wentermone.get())<=50000:
			if mmmm=="ACTIVATED":
				con=sqlite3.connect('globalbank.db')	
				c=con.cursor()  
				c.execute("SELECT * FROM "+"\'"+op111+"\'")
				records=c.fetchall()
				for row in records:
					global klmn
					klmn=(row[17])
				if klmn>=int(wentermone.get()):
					
					con=sqlite3.connect('globalbank.db')	
					c=con.cursor()  
					c.execute("SELECT * FROM "+"\'"+op111+"\'")
					records=c.fetchall()
					for row in records:
						jjjj=(row[17])
						print(jjjj)
						global iki
						iki=(int(jjjj)-int(wentermone.get()))
				else:
					
					messagebox.showwarning("ERROR", "YOU DON'T HAVR ENOUGH\nBALANCE!.") 

						
				c=con.cursor()
				c.execute ("INSERT INTO" +"\'"+op111+"\'"+"(Date_of_transaction,last_transaction,Balance)VALUES(date('now'),?,?)",(withdrawmoney,iki))

				con.commit()
				con.close() 
				
				closewithdrawwindow()
			else:
					
				messagebox.showwarning("ERROR", "YOUR ACCCOUNT IS DEACTIVE\nTO START TRANSACTIONS \nPLEASE ACTIVATE YOUR ACCOUNT.") 
		
		else:
			messagebox.showwarning("ERROR", "YOU CAN WITHDRAW\n Rs.50,000 ONCE!") 
	else:
		messagebox.showwarning("ERROR", "PLEASE COLLECT THE CAPTCHA\n(CLICK TO PROCEED)")
		
def closewithdrawwindow():
	closewithdrawwindow=Toplevel(root)
	closewithdrawwindow.resizable(0,0)
	closewithdrawwindow.title('THANK YOU FOR USING OUR SERVICES')
	closewithdrawwindow.geometry("960x360")
	
	spcclose=Label(closewithdrawwindow,text="")
	spcclose.grid(row=0,column=0)
	
	prodone=Label(closewithdrawwindow,font='Futura 15 bold underline',text="TRANSACTION SUCCESSFUL!",relief="ridge",borderwidth=6,width=47)
	prodone.grid(row=1,column=0,columnspan=14,sticky='nsew')
	
	spcclose7=Label(closewithdrawwindow,text="")
	spcclose7.grid(row=3,column=0)
	
	prodone1=Label(closewithdrawwindow,font='Futura 15 bold underline',text="YOU WITHDRAWED:(RUPEES)",relief="ridge",borderwidth=6,width=28)
	prodone1.grid(row=5,column=0)
	
	prodone2=Label(closewithdrawwindow,font='Futura 15 bold underline',text=wgotmoney,relief="ridge",borderwidth=6,width=21)
	prodone2.grid(row=5,column=1)
	
	spcclose3=Label(closewithdrawwindow,text="")
	spcclose3.grid(row=4,column=0)
	
	prodone3=Label(closewithdrawwindow,font='Futura 15 bold underline',text="YOUR BALANCE IS",relief="ridge",borderwidth=6,width=28)
	prodone3.grid(row=6,column=0)
	
	prodone4=Label(closewithdrawwindow,font='Futura 15 bold underline',text=iki,relief="ridge",borderwidth=6,width=21)
	prodone4.grid(row=6,column=1)
	
	clicktocut=Button(closewithdrawwindow,font='Futura 15 bold underline',text="CLICK TO QUIT",relief="raised",width=47,borderwidth=6,command=root.destroy)
	clicktocut.grid(row=8,column=0,columnspan=14,sticky='nsew')
	
	spcclose6=Label(closewithdrawwindow,text="")
	spcclose7.grid(row=7,column=0)
	
	#_______________END_____________________#
#----------------------WITHDRAW---------------------#
#------------------------MONEY--------------------------#
#________________________________________#
	
	



#________________________________________#
#-----------------------DEPOSIT-------------------------#
#------------------------MONEY--------------------------#
#________________________________________#


def depositwindow():
	depositwindow=Toplevel(root)
	depositwindow.resizable(0,0)
	depositwindow.title('ENTER ACCOUNT DETAILS')
	depositwindow.geometry("1190x460")
	
	space31=Label(text="")
	space31.grid(row=0)
	space32=Label(depositwindow,text="")
	space32.grid(row=1)
	space33=Label(depositwindow,text="")
	space33.grid(row=2)
	space34=Label(depositwindow,text="")
	space34.grid(row=12)
	
	entacc=Label(depositwindow,text="ENTER ACCOUNT NUMBER",font='Futura 16 bold underline',relief="ridge",borderwidth=6,width=22)
	
	entacc.grid(row=7,column=0,sticky='nsew')
	
	entpass=Label(depositwindow,text="ENTER PASSWORD",font='Futura 16 bold underline',relief="ridge",borderwidth=6)
	
	space39=Label(depositwindow,text="")
	space39.grid(row=9)
	space40=Label(depositwindow,text="")
	space40.grid(row=10)
	
	entpass.grid(row=11,column=0,sticky='nsew')
	
	global enteracc
	enteracc= Entry(depositwindow, width=69,bd=4)
	enteracc.grid(row=7, column=1,sticky='nsew')
	
	global enterpass
	
	enterpass= Entry(depositwindow,width=69,bd=4,show="*")
	enterpass.grid(row=11,column=1,sticky='nsew')
	
	Nxt4=Button(depositwindow,command=checkaccnumber1,text='NEXT',borderwidth = 6,width =49,relief="raised",font='Futura 16 bold underline',justify=CENTER)
	Nxt4.grid(row=14,column=0,columnspan=20,sticky='nsew')
	spc0=Label(depositwindow,text="")
	spc0.grid(row=13)
	
def checkaccnumber1():
	import sqlite3
	global con   
	con=sqlite3.connect('globalbank.db')
	global c
	c=con.cursor()           
	c.execute("SELECT name FROM sqlite_master WHERE type='table';")
	global a
	a=c.fetchall()
	global jk	
	jk=(''.join(map(str,a)))
	
	global op11
	op11=enteracc.get()
	global OP11
	OP11=enterpass.get()
	
	if op11 in jk:
		con=sqlite3.connect('globalbank.db')
		c=con.cursor()  
		c.execute("SELECT * FROM "+"\'"+op11+"\'"+"WHERE Account_number="+"\'"+op11+"\'")
		records=c.fetchall()
		print(records)
		for row in records:
			global jjj
			jjj=(row[1])
			global mmm
			mmm=(row[14])
			print(jjj)			
		if OP11==jjj:
			depositwindow1()
			
		else:
			messagebox.showwarning("ERROR", "YOUR ACCOUNT NUMBER\n              AND\nPASSWORD DON'T MATCH") 
			
	else:
		messagebox.showwarning("ERROR", "PLEASE ENTER \nCORRECT ACCOUNT NUMBER") 
		

	
	con.commit()

 
	con.close() 
	
	
def depositwindow1():
	depositwindow1=Toplevel(root)
	depositwindow1.resizable(0,0)
	depositwindow1.title('DEPOSIT MONEY')
	depositwindow1.geometry("1185x460")
	
	
	space31=Label(text="")
	space31.grid(row=0)
	space32=Label(depositwindow1,text="")
	space32.grid(row=1)
	space33=Label(depositwindow1,text="")
	space33.grid(row=2)
	space34=Label(depositwindow1,text="")
	space34.grid(row=12)
	
	entacc=Label(depositwindow1,text="AMOUNT OF MONEY TO\nBE DEPOSITED(IN RUPEES)",font='Futura 15 bold underline',relief="ridge",borderwidth=6,width=24)
	
	entacc.grid(row=7,column=0,sticky='nsew')
	
	global var5
	var5= StringVar()
	
	global chkmoney
	chkmoney=Checkbutton(depositwindow1,text="MONEY DEPOSITED TO RESPECTIVE COUNTER/ATM",borderwidth = 8,width =51,relief="sunken",font='Futura 11 bold',variable=var5, onvalue="on", offvalue="off")
	chkmoney.deselect()
	
	
	space39=Label(depositwindow1,text="")
	space39.grid(row=9)
	space40=Label(depositwindow1,text="")
	space40.grid(row=10)
	
	chkmoney.grid(row=11,sticky='nsew',columnspan=14)
	
	global entermone
	entermone= Entry(depositwindow1, width=70,bd=4)
	entermone.grid(row=7, column=1,sticky='nsew')
		
	Nxt4=Button(depositwindow1,command=depositfunc,text='DEPOSIT MONEY',borderwidth = 6,width =49,relief="raised",font='Futura 16 bold underline',justify=CENTER)
	Nxt4.grid(row=14,column=0,columnspan=20,sticky='nsew')
	spc0=Label(depositwindow1,text="")
	spc0.grid(row=13)
	
	
def depositfunc():
	if var5.get()=="on":
		global gotmoney
		gotmoney=entermone.get()
		global depmoney
		depmoney=("CREDITED RS. "+gotmoney)
		print(depmoney)
		
		if int(entermone.get())<=50000:
			if mmm=="ACTIVATED":
				con=sqlite3.connect('globalbank.db')	
				c=con.cursor()  
				c.execute("SELECT * FROM "+"\'"+op11+"\'")
				records=c.fetchall()
				for row in records:
					jjj=(row[17])
					print(jjj)
					global kik
					kik=int(entermone.get())+int(jjj)
				c=con.cursor()
				c.execute ("INSERT INTO" +"\'"+op11+"\'"+"(Date_of_transaction,last_transaction,Balance)VALUES(date('now'),?,?)",(depmoney,kik))

				con.commit()
				con.close() 
				
				closedepositwindow()
			else:
					
				messagebox.showwarning("ERROR", "YOUR ACCCOUNT IS DEACTIVE\nTO START TRANSACTIONS \nPLEASE ACTIVATE YOUR ACCOUNT.") 
		
		else:
			messagebox.showwarning("ERROR", "YOU CAN DEPOSIT\n Rs.50,000 ONCE!") 
	else:
		messagebox.showwarning("ERROR", "PLEASE DEPOSIT MONEY TO\n RESPECTIVE COUNTER/ATM")
		
def closedepositwindow():
	closedepositwindow=Toplevel(root)
	closedepositwindow.resizable(0,0)
	closedepositwindow.title('THANK YOU FOR USING OUR SERVICES')
	closedepositwindow.geometry("960x360")
	
	spcclose=Label(closedepositwindow,text="")
	spcclose.grid(row=0,column=0)
	
	prodone=Label(closedepositwindow,font='Futura 15 bold underline',text="TRANSACTION SUCCESSFUL!",relief="ridge",borderwidth=6,width=47)
	prodone.grid(row=1,column=0,columnspan=14,sticky='nsew')
	
	spcclose7=Label(closedepositwindow,text="")
	spcclose7.grid(row=3,column=0)
	
	prodone1=Label(closedepositwindow,font='Futura 15 bold underline',text="YOU DEPOSITED:(RUPEES)",relief="ridge",borderwidth=6,width=28)
	prodone1.grid(row=5,column=0)
	
	prodone2=Label(closedepositwindow,font='Futura 15 bold underline',text=gotmoney,relief="ridge",borderwidth=6,width=21)
	prodone2.grid(row=5,column=1)
	
	spcclose3=Label(closedepositwindow,text="")
	spcclose3.grid(row=4,column=0)
	
	prodone3=Label(closedepositwindow,font='Futura 15 bold underline',text="YOUR BALANCE IS",relief="ridge",borderwidth=6,width=28)
	prodone3.grid(row=6,column=0)
	
	prodone4=Label(closedepositwindow,font='Futura 15 bold underline',text=kik,relief="ridge",borderwidth=6,width=21)
	prodone4.grid(row=6,column=1)
	
	clicktocut=Button(closedepositwindow,font='Futura 15 bold underline',text="CLICK TO QUIT",relief="raised",width=47,borderwidth=6,command=root.destroy)
	clicktocut.grid(row=8,column=0,columnspan=14,sticky='nsew')
	
	spcclose6=Label(closedepositwindow,text="")
	spcclose7.grid(row=7,column=0)
	
	
	
	
	
	
	
	
	
	
			
#••••••••••••••••••••••END••••••••••••••••••••••#
#______________________________________#
	
	
	
	
	
	










#--------------------------------------------------------------#

#---------------------LAST STAFF --------------------#
#-----ACCESS(ACCOUNT ACTIVATION)----#





#--------------------------------------------------------------#
	
def Entrywindowp():
	Entrywindowp= Toplevel(root)
	Entrywindowp.resizable(0,0)
	Entrywindowp.title('Note:-THIS FUNCTION IS ONLY FOR BANK STAFF')
	Entrywindowp.geometry("1175x520")

	space31=Label(Entrywindowp,text="")
	space31.grid(row=0)
	space32=Label(Entrywindowp,text="")
	space32.grid(row=1)
	space33=Label(Entrywindowp,text="")
	space33.grid(row=2)
	space34=Label(Entrywindowp,text="")
	space34.grid(row=12)
	
	entaccp=Label(Entrywindowp,text="ENTER STAFF ID",font='Futura 16 bold underline',relief="ridge",borderwidth=6,width=21)
	
	entaccp.grid(row=7,column=0,sticky='nsew')
	
	entpassp=Label(Entrywindowp,text="ENTER PASSWORD",font='Futura 16 bold underline',relief="ridge",borderwidth=6)
	
	space39=Label(Entrywindowp,text="")
	space39.grid(row=9)
	space40=Label(Entrywindowp,text="")
	space40.grid(row=10)
	
	entpassp.grid(row=11,column=0,sticky='nsew')
	
	global enteraccp
	enteraccp= Entry(Entrywindowp, width=70,bd=4)
	enteraccp.grid(row=7, column=1,sticky='nsew')
	
	global enterpassp
	
	enterpassp= Entry(Entrywindowp,width=70,bd=4,show="*")
	enterpassp.grid(row=11,column=1,sticky='nsew')
	
	Nxt4=Button(Entrywindowp,command=checkstaff,text='NEXT',borderwidth = 6,width =49,relief="raised",font='Futura 16 bold underline',justify=CENTER)
	Nxt4.grid(row=14,column=0,columnspan=20,sticky='nsew')
	spc0=Label(Entrywindowp,text="")
	spc0.grid(row=13)
		
def checkstaff():
	global eq
	eq=enteraccp.get()
	global EQ
	EQ=enterpassp.get()
	
	staffid="123456789"
	staffpass="987654321"
	
	if eq==staffid and EQ==staffpass:
		Entrywindow()
	else:
		messagebox.showwarning("ERROR", "Please Enter Correct STAFF ID or PASSWORD") 
	
		
	
def Entrywindow():
	Entrywindow= Toplevel(root)
	Entrywindow.resizable(0,0)
	Entrywindow.title('ENTER DETAILS')
	Entrywindow.geometry("1175x520")

	space31=Label(Entrywindow,text="")
	space31.grid(row=0)
	space32=Label(Entrywindow,text="")
	space32.grid(row=1)
	space33=Label(Entrywindow,text="")
	space33.grid(row=2)
	space34=Label(Entrywindow,text="")
	space34.grid(row=12)
	
	entacc=Label(Entrywindow,text="ENTER ACCOUNT NUMBER",font='Futura 16 bold underline',relief="ridge",borderwidth=6)
	
	entacc.grid(row=7,column=0,sticky='nsew')
	
	entpass=Label(Entrywindow,text="ENTER PASSWORD",font='Futura 16 bold underline',relief="ridge",borderwidth=6)
	
	space39=Label(Entrywindow,text="")
	space39.grid(row=9)
	space40=Label(Entrywindow,text="")
	space40.grid(row=10)
	
	entpass.grid(row=11,column=0,sticky='nsew')
	
	global enteracc
	enteracc= Entry(Entrywindow, width=70,bd=4)
	enteracc.grid(row=7, column=1,sticky='nsew')
	
	global enterpass
	
	enterpass= Entry(Entrywindow,width=70,bd=4,show="*")
	enterpass.grid(row=11,column=1,sticky='nsew')
	
	Nxt4=Button(Entrywindow,command=check_acc_number,text='NEXT',borderwidth = 6,width =49,relief="raised",font='Futura 16 bold underline',justify=CENTER)
	Nxt4.grid(row=14,column=0,columnspan=20,sticky='nsew')
	spc0=Label(Entrywindow,text="")
	spc0.grid(row=13)

import sqlite3  	
def check_acc_number():
	global con   
	con=sqlite3.connect('globalbank.db')
	global c
	c=con.cursor()           
	c.execute("SELECT name FROM sqlite_master WHERE type='table';")
	global a
	a=c.fetchall()
	global jk	
	jk=(''.join(map(str,a)))
	


		
			
	global op
	op=enteracc.get()
	
	global OP
	OP=enterpass.get()
	
	if op in jk:
		
		con=sqlite3.connect('globalbank.db')
		c=con.cursor()  
		c.execute("SELECT * FROM "+"\'"+op+"\'"+"WHERE Account_number="+"\'"+op+"\'")
		records=c.fetchall()
		for row in records:
			jjj=(row[1])
			

		
		if OP ==jjj:
			Entrywindow1()
		else:
			messagebox.showwarning("ERROR", "YOUR ACCOUNT NUMBER\n           AND\nPASSWORD DON'T MATCH") 
			
	else:
		messagebox.showwarning("ERROR", "PLEASE ENTER \nCORRECT ACCOUNT NUMBER") 
		

	
	con.commit()

 
	con.close() 
	
	
		
				
def Entrywindow1():
	Entrywindow1=Toplevel(root)
	Entrywindow1.resizable(0,0)
	Entrywindow1.title('ACTIVATING ACCOUNT')
	Entrywindow1.geometry("1280x720")
	
	Cong=Label(Entrywindow1,width =50,pady="10",font='Futura 20 bold underline',text="")
	
	Cong1=Label(Entrywindow1,width =50,font='Futura 14 bold',text="")
	spc4=Label(Entrywindow1,text="")
	spc4.grid(row=0)
	Cong.grid(row="1",column="0",columnspan="3",sticky='nsew')
	Cong1.grid(row="3",rowspan="1",columnspan="3",sticky='nsew')
	act= Label(Entrywindow1,width =50,borderwidth = 8,relief="sunken",font='Futura 11 bold underline',text="PLEASE CHECK WHETHER ALL THE DOCUMENTS\nARE PRESENT AND ATTACH THEM TO RESPECTIVE FILES")
	act.grid(row="2",column="1",rowspan="1",pady=10,sticky='nsew')
	global var4
	var4= StringVar()
	global var1
	var1= StringVar()
	global var2
	var2= StringVar()
	global var3
	var3= StringVar()
	global aadhar55
	aadhar55=Checkbutton(Entrywindow1,text="AADHAR CARD(XEROX)     ",anchor=W,borderwidth = 8,width =49,relief="sunken",font='Futura 11 bold',variable=var4, onvalue="on", offvalue="off")
	aadhar55.deselect()
	global pan55
	pan55=Checkbutton(Entrywindow1,text="PAN CARD(XEROX)",anchor=W,borderwidth = 8,width =49,relief="sunken",font='Futura 11 bold',variable=var1, onvalue="on", offvalue="off")
	pan55.deselect()
	global ebill55
	ebill55=Checkbutton(Entrywindow1,text="ELECTRICITY BILL",anchor=W,borderwidth = 8,width =49,relief="sunken",font='Futura 11 bold',variable=var2, onvalue="on", offvalue="off")	
	ebill55.deselect()
	global photo55
	photo55=Checkbutton(Entrywindow1,text="APPLICANT'S PHOTOGRAPHS",borderwidth = 8,anchor=W,width =49,relief="sunken",font='Futura 11 bold',variable=var3, onvalue="on", offvalue="off")
	photo55.deselect()
	aadhar55.grid(row="4",column="1",sticky='nsew')
	pan55.grid(row="5",column='1',sticky='nsew')
	ebill55.grid(row=6,column=1,sticky='nsew')
	photo55.grid(row=7,column=1,sticky='nsew')
	
	spc1=Label(Entrywindow1,text="")
	spc1.grid(row=8)
	quit=Button(Entrywindow1,text='CLICK TO ACTIVATE ACCOUNT',width=51,borderwidth=9,relief="raised",font='futura 14 bold',command=action)
	quit.grid(row="9",column="1",sticky='nsew')
	
	

def action():
	if var4.get()=="on" and var1.get()=="on" and var2.get()=="on" and var3.get()=="on":
		Entrywindow2()
		con=sqlite3.connect('globalbank.db')
		global c
		c=con.cursor()           
		c.execute("UPDATE "+"\'"+op+"\'"+" SET Status='ACTIVATED' WHERE Account_number="+"\'"+op+"\'")
		con.commit()
		con.close()		
	else:
		messagebox.showwarning("ERROR", "Please Submit All the documents")

def Entrywindow2():
	Entrywindow2=Toplevel(root)
	Entrywindow2.resizable(0,0)
	Entrywindow2.title('ACCOUNT ACTIVATED')
	Entrywindow2.geometry("1280x720")
	Congno=Label(Entrywindow2,borderwidth =14,width =50,pady="10",relief="ridge",bg="#FFF1A5",font='Futura 20 bold underline',text="CONGRATULATIONS!!")
	
	Congno1=Label(Entrywindow2,borderwidth =10,width =50,relief="ridge",bg="#BFE6FF",font='Futura 14 bold',text=" YOUR ACCOUNT HAS BEEN ACTIVATED")
	spc4=Label(Entrywindow2,text="")
	spc4.grid(row=0)
	Congno.grid(row="1",column="0",columnspan="3",sticky='nsew')
	Congno1.grid(row="2",rowspan="1",columnspan="3",sticky='nsew')
	act11= Label(Entrywindow2,borderwidth = 8,width =49,font='Futura 11 bold underline',relief="sunken",text="NOW YOU CAN START YOUR TRANSACTIONS")
	act11.grid(row="4",column="1",rowspan="1",pady=10,sticky='nsew')
	
	spacedude=Label(Entrywindow2,text="",width =49,font='Futura 11 bold underline')
	spacedude1=Label(Entrywindow2,text="THANKS FOR USING\n OUR FACILITIES.!",borderwidth = 8,width =49,font='Futura 11 bold underline',relief="sunken")
	thank=Label(Entrywindow2,text="NOW YOU CAN ALSO\nUSE OTHER OPTIONS",borderwidth = 8,width =49,relief="sunken",font='Futura 11 bold underline')
	spaceman=Label(Entrywindow2,text="WE ARE GLAD TO HELP YOU.!",borderwidth = 8,width =49,relief="sunken",font='Futura 11 bold underline')
	spacedude.grid(row="3",column="1",sticky='nsew')
	spacedude1.grid(row="5",column='1',sticky='nsew')
	thank.grid(row=6,column=1,sticky='nsew')
	spaceman.grid(row=7,column=1,sticky='nsew')
	
	spc1=Label(Entrywindow2,text="")
	spc1.grid(row=8)
	quit=Button(Entrywindow2,text='CLICK TO QUIT',width=51,borderwidth=9,relief="raised",font='futura 14 bold',command=root.destroy)
	quit.grid(row="9",column="1",sticky='nsew')
	
	
#--------------------------END-----------------------------#
#---------------------LAST STAFF --------------------#
#-----ACCESS(ACCOUNT ACTIVATION)----#
#••••••••••••••••••••••••••••••••••••••••••••••••••
#-----------------------------------------------------------#	#--------------------------END-----------------------------#







#--------------------------------------------------------------#

#-----BUTTON 1 CREATING ACCOUNT-----#

#--------------------------------------------------------------#
           



#C = Canvas(root, bg="blue",height=9,width=16)
#filename = PhotoImage(file ="/storage/emulated/0/toolwizPhoto/ToolWiz_Photos/the-dark-hedges-4094148_1920_1599191896415.png")
#background_label = Label(root,image=filename)
#background_label.place(x=0,y=0,relwidth=1,relheight=1)

#C.grid(sticky='nsew')



		#Defining Functions & Windows		



root.geometry("1280x720")
root.resizable(0,0)
			



def newwindow3():
	newwindow3=Toplevel(root)
	newwindow3.resizable(0,0)
	newwindow3.title('GET ASSOCIATED WITH US')
	newwindow3.geometry("1280x720")
	
	import sqlite3

                     #Cursor
                     
	global con
	con=sqlite3.connect('globalbank.db')
	global c
	c=con.cursor()
        
        			#For Account number
                  
	c.execute("SELECT name FROM sqlite_master WHERE type='table';")

	a=c.fetchall()
	d=(a[-1])
	res=int(''.join(map(str,d)))
	Accnumber=res+1
	print(Accnumber)
#accnumb=str(res)
#accnumb=('\"'+ accnumb+'\"')
	Accountnumber=str(Accnumber)
	global Accountnumb
	Accountnumb=('\"'+ Accountnumber+'\"')
	

	con.commit()

 
	con.close() 
	
	
	space20=Label(newwindow3,text="")
	space20.grid(row=0)
	space21=Label(newwindow3,text="")
	space21.grid(row=1)
	space22=Label(newwindow3,text="")
	space22.grid(row=2)
	space23=Label(newwindow3,text="")
	space23.grid(row=3)
	
	accnumis1=Label(newwindow3,text="YOUR ACCOUNT NUMBER IS : ",font='Futura 18 bold underline',relief="ridge",borderwidth=6)
	accnumis1.grid(row=4,column=0,sticky='nsew')
	
	space24=Label(newwindow3,text="")
	space24.grid(row=5)
	space25=Label(newwindow3,text="")
	space25.grid(row=6)
	
	accnumis=Label(newwindow3,text=Accnumber,font='Futura 16 bold underline',relief="ridge",borderwidth=6)
	
	accnumis.grid(row=4,column=1,sticky='nsew')	
	
	space26=Label(newwindow3,text="")
	space26.grid(row=5)
	space27=Label(newwindow3,text="")
	space27.grid(row=6)
	
	crpasswo1=Label(newwindow3,text="CREATE PASSWORD",font='Futura 16 bold underline',relief="ridge",borderwidth=6)
	
	crpasswo1.grid(row=7,column=0,sticky='nsew')
	
	crpasswo=Label(newwindow3,text="CONFIRM PASSWORD",font='Futura 16 bold underline',relief="ridge",borderwidth=6)
	
	space29=Label(newwindow3,text="")
	space29.grid(row=9)
	space30=Label(newwindow3,text="")
	space30.grid(row=10)
	
	crpasswo.grid(row=11,column=0,sticky='nsew')
	
	global Passwo1
	Passwo1= Entry(newwindow3, width=70,bd=4,show="*")
	Passwo1.grid(row=7, column=1,sticky='nsew')
	
	global Passwo
	
	Passwo= Entry(newwindow3,width=70,bd=4,show="*")
	Passwo.grid(row=11,column=1,sticky='nsew')
	
	Nxt4=Button(newwindow3,command=check_and_open,text='SUBMIT',borderwidth = 6,width =49,relief="raised",font='Futura 16 bold underline',justify=CENTER)
	Nxt4.grid(row=14,column=0,columnspan=20,sticky='nsew')
	spc=Label(newwindow3,text="")
	spc.grid(row=13)
	

def check_and_open():
	global passwo1
	passwo1=Passwo1.get()
	global passwo
	passwo=Passwo.get()		
	if passwo1==passwo:
		get()
		submit()
		newwindow4()
	else:
		messagebox.showwarning("ERROR", "PASSWORD DON'T MATCH") 		
		

	
	
	
	
	
def newwindow4():
	newwindow4=Toplevel(root)
	newwindow4.resizable(0,0)
	newwindow4.title('THANKS FOR CREATING ACCOUNT')
	newwindow4.geometry("1280x720")
	
	Cong=Label(newwindow4,borderwidth =14,width =50,pady="10",relief="ridge",bg="#FFF1A5",font='Futura 20 bold underline',text="CONGRATULATIONS!!")
	
	Cong1=Label(newwindow4,borderwidth =10,width =50,relief="ridge",bg="#BFE6FF",font='Futura 14 bold',text=" YOUR ACCOUNT HAS BEEN CREATED")
	spc4=Label(newwindow4,text="")
	spc4.grid(row=0)
	Cong.grid(row="1",column="0",columnspan="3",sticky='nsew')
	Cong1.grid(row="2",rowspan="1",columnspan="3",sticky='nsew')
	act= Label(newwindow4,borderwidth = 8,width =50,font='Futura 14',text="TO ACTIVATE YOUR ACCOUNT & START TRANSACTIONS\n PLEASE SUBMIT THE FOLLOWING DOCUMENTS TO THE NEAREST BRANCH")
	act.grid(row="3",column="0",rowspan="1",columnspan="14",pady=10,sticky='nsew')
	
	aadhar=Label(newwindow4,text="AADHAR CARD",borderwidth = 8,width =49,relief="sunken",font='Futura 11 bold underline')
	pan=Label(newwindow4,text="PAN CARD",borderwidth = 8,width =49,relief="sunken",font='Futura 11 bold underline')
	ebill=Label(newwindow4,text="ELECTRICITY BILL",borderwidth = 8,width =49,relief="sunken",font='Futura 11 bold underline')
	photo=Label(newwindow4,text="APPLICANT'S PHOTOGRAPHS",borderwidth = 8,width =49,relief="sunken",font='Futura 11 bold underline')
	aadhar.grid(row="4",column="1",sticky='nsew')
	pan.grid(row="5",column='1',sticky='nsew')
	ebill.grid(row=6,column=1,sticky='nsew')
	photo.grid(row=7,column=1,sticky='nsew')
	
	spc1=Label(newwindow4,text="")
	spc1.grid(row=8)
	quit=Button(newwindow4,text='CLICK TO QUIT',width=51,borderwidth=9,relief="raised",font='futura 14 bold',command=root.destroy)
	quit.grid(row="9",column="1",sticky='nsew')

						
												
																								
												
def newwindow2():
	newwindow2=Toplevel(root)
	newwindow2.resizable(0,0)
	newwindow2.title('READ CAREFULLY')
	newwindow2.geometry("1190x760")
	
	
	
	def checkterm():
		if var.get()=="on":
			newwindow3()
		else:
			messagebox.showwarning("ERROR", "Please Agree Terms & Conditions")
	
	tc=Label(newwindow2,text="Accuracy of Information : \nThe Customer is responsible for the correctness of information supplied to THE GLOBAL BANK for use\nof the Services.THE GLOBAL BANK accepts no liability for the consequences arising out of erroneous\ninformation supplied by the Customer.\nIf the Customer notices an  error in the Instructions supplied to THE GLOBAL BANK, the Customer\nshall immediately advise THE GLOBAL BANK which will endeavour to correct the error wherever\npossible on a reasonable best effort basis.\n \nLiability for Officials/DSAs:\nTHE GLOBAL BANK shall be responsible for the acts of omission andor commission of the Officials/DSAs\nappointed by THE GLOBAL BANK for the purpose of providing the Services to the Customers.\nOperation of Services:\n \n1) The Customer acknowledges and agrees that the Instructions for the services shall be processed by\nTHE GLOBAL BANKonly if the same are received by THE GLOBAL BANK in the prescribed time and manner. \n \n2)The Customer agrees and acknowledges that the Services shall be provided by THE GLOBAL BANK\nin his own account only and at the registered communication address of the Customer available with\nTHE GLOBAL BANK at the time of the Customer applying for the Services through the Application.In case\nof any request provided by the Customer for getting the registered communication address changed in the\n records of THE GLOBAL BANK in a manner as may be prescribed by THE GLOBAL BANK, such changed\ncommunication address shall be used by THE GLOBAL BANK for providing the Services to the Customers.",justify=LEFT,font='futura 11')
	tc.grid()	
	var= StringVar()

	chk=Checkbutton(newwindow2, text="I AGREE ALL THE TERMS & CONDITION OF THE GLOBAL BANK",font='futura 10',variable=var, onvalue="on", offvalue="off")
	chk.deselect()
	chk.grid(row=3,sticky='n')		
	Nxt3=Button(newwindow2,command=checkterm,text='NEXT',borderwidth = 6,width =49,relief="raised",font='Futura 11 bold underline',justify=CENTER)
	Nxt3.grid(row=5,column=0,columnspan=20,sticky='nsew')
	spc=Label(newwindow2,text="")
	spc.grid(row=4)

	



def newwindow1():	
	newwindow1=Toplevel(root)
	newwindow1.resizable(0,0)
	newwindow1.title('                                                                                                                    PLEASE FILL THE FORM TO PROCEED')
	newwindow1.geometry("1275x675")
	
	Heading1=Label(newwindow1,borderwidth =10,width =20,relief="ridge",bg="#BFE6FF",font='Futura 16 bold',text="COMMUNICATION ADRESS")
	Heading1.grid(row=0,column=1,columnspan=10,sticky='nsew')
	
	global Address1
	Address1= Entry(newwindow1, width=82)
	Address1.grid(row=1,column=3,sticky='ns')
	
	
	global Permanent_add	
	Permanent_add= Entry(newwindow1, width=82)
	Permanent_add.grid(row=2, column=3,sticky='ns')

	
	global Pincode
	
	Pincode=Entry(newwindow1,width=82)
	Pincode.grid(row=3,column=3,sticky='ns')

	
	global Mnum
	Mnum=Entry(newwindow1,width=82)
	Mnum.grid(row=4,column=3,sticky='ns')
	Mnum.insert(0,"+91")
	
	
	global Mnum1
	Mnum1=Entry(newwindow1,width=82)
	Mnum1.grid(row=5,column=3,sticky='ns')
	Mnum1.insert(0,"+91")
	
	
	global Lannum
	Lannum=Entry(newwindow1,width=82)
	Lannum.grid(row=6,column=3,sticky='ns')
	
	
	def check_inputs():
		dd=Address1.get()
		ee=Permanent_add.get()
		ff=Pincode.get()
		gg=Mnum.get()
		hh=Mnum1.get()
		ii=Lannum.get()
		if dd !="":
			pass
		else:
			messagebox.showwarning("ERROR", "Please Enter Current Address") 

		if ee !="":
			pass
		else:
			messagebox.showwarning("ERROR", "Please Enter Permanent Address") 
			
		if ff !="":
			pass
		else:
			messagebox.showwarning("ERROR", "Please Enter Pincode") 															
		if gg !="+91":
			pass
		else:
			messagebox.showwarning("ERROR", "Please Enter Mobile number") 	
			
		if hh !="+91":
			pass
		else:
			messagebox.showwarning("ERROR", "Please Enter Mobile number") 

			
		if dd!="" and ee!="" and ff!="" and gg!="+91" and hh!="+91":
			newwindow2()		
		else:
			pass
					
			
		
			

	
	
					#Labels	
	Adressq= Label(newwindow1, text="Current Adress",borderwidth =3,width =26,relief="sunken",font='Futura 12')
	Adressq.grid(row=1,column=1)
	
	Permanentadd= Label(newwindow1, text="Your permanent Address",borderwidth =3,width =26,relief="sunken",font='Futura 12')
	Permanentadd.grid(row=2,column=1)
	
	Pincode1=Label(newwindow1,text="Pincode",borderwidth =3,width =26,relief="sunken",font='Futura 12')
	Pincode1.grid(row=3,column=1)
	
	Phonenum= Label(newwindow1, text="Phone number",borderwidth =3,width =26,relief="sunken",font='Futura 12')
	Phonenum.grid(row=4,column=1)
	Mobilenum=Label(newwindow1,text="Mobile number",borderwidth =3,width =26,relief="sunken",font='Futura 12')
	Mobilenum.grid(row=5,column=1)
	Landnum=Label(newwindow1,text="Landline Number",borderwidth =3,width =26,relief="sunken",font='Futura 12')
	Landnum.grid(row=6,column=1)

	
				#Colon Labels	
	colon7=Label(newwindow1,text=":")
	colon8=Label(newwindow1,text=":")
	colon9=Label(newwindow1,text=":")
	colon10=Label(newwindow1,text=":")
	colon11=Label(newwindow1,text=":")
	colon12=Label(newwindow1,text=":")
	
	colon7.grid(row=1,column=2)
	colon8.grid(row=2,column=2)
	colon9.grid(row=3,column=2)
	colon10.grid(row=4,column=2)
	colon11.grid(row=5,column=2)
	colon12.grid(row=6,column=2)	
	space6=Label(newwindow1,text="")
	space6.grid(row=9)
	
	
	Next1=Button(newwindow1,command=check_inputs,text='SUBMIT',borderwidth = 6,width =49,relief="raised",font='Futura 11 bold underline')
	Next1.grid(row=10,column=1,columnspan=20,sticky='nsew')
	
	
	
	
	
	
	
	
	
def newWindow():
             
                 #SQLite CONNECTION
	import sqlite3

                     #Cursor
                     
	global con
	con=sqlite3.connect('globalbank.db')
	global c
	c=con.cursor()
	defaulttable=("'12190'")
        
        			#For Account number
	c.execute("create table if not exists "+defaulttable+ " (Account_number integer,Password text, Account_Holders_name text, Mothers_name text, Fathers_name text, Birthdate text, Temporary_address text, Permanent_address text, Pincode integer, Email_id text, Occupation text, Phone_number integer, Mobile_number integer, Landline_number integer, Status text default DEACTIVE, Date_of_transaction text default NO_TRANSACTIONS, last_transaction text default '0',Balance integer default 0);")
	c.execute("SELECT name FROM sqlite_master WHERE type='table';")
	a=c.fetchall()
	d=(a[-1])
	res=int(''.join(map(str,d)))
	global Accnumber
	Accnumber=res+1
	print(Accnumber)
#accnumb=str(res)
#accnumb=('\"'+ accnumb+'\"')
	Accountnumber=str(Accnumber)
	global Accountnumb
	Accountnumb=('\"'+ Accountnumber+'\"')
	

	con.commit()	


	newWindow= Toplevel(root)
	newWindow.resizable(0,0)
	newWindow.title('PLEASE FILL THE FORM TO PROCEED')
	newWindow.geometry("1275x675")
	
	global name
	name=Entry(newWindow,width=27,bd=3,justify=CENTER)
	name.grid(row=1,column=3,sticky='nsw')
	name.insert(0,"FIRST NAME")
	global namem
	namem= Entry(newWindow, width=27,bd=3,justify=CENTER)
	namem.grid(row=1, column=3,rowspan=1,columnspan=10,sticky='ns')
	namem.insert(0,"MIDDLE NAME")
	global names
	names= Entry(newWindow, width=27,bd=3,justify=CENTER)
	names.grid(row=1, column=3,rowspan=1,sticky='nse')
	names.insert(0,"SURNAME")
	
	
	
	global Birthdated
	Birthdated=Entry(newWindow, width=27,bd=3,justify=CENTER)
	Birthdated.grid(row=2, column=3,rowspan=1,sticky='nsw')
	Birthdated.insert(0,"DD")
	global Birth_datem
	Birth_datem= Entry(newWindow, width=27,bd=3,justify=CENTER)
	Birth_datem.grid(row=2, column=3,rowspan=1,columnspan=10,sticky='ns')
	Birth_datem.insert(0,"MM")
	
	global Birth_datey
	Birth_datey= Entry(newWindow, width=27,bd=3,justify=CENTER)
	Birth_datey.grid(row=2, column=3,rowspan=1,sticky='nse')
	Birth_datey.insert(0,"YYYY")
	
	global Occupation1
	Occupation1= Entry(newWindow, width=82,bd=3)
	Occupation1.grid(row=3,column=3,sticky='nsew')
	
	global Fname1
	Fname1=Entry(newWindow,width=27,bd=3,justify=CENTER)
	Fname1.grid(row=4,column=3,sticky='nsw')
	Fname1.insert(0,"FIRST NAME")
	global Fnamem
	Fnamem= Entry(newWindow, width=27,bd=3,justify=CENTER)
	Fnamem.grid(row=4, column=3,rowspan=1,columnspan=10,sticky='ns')
	Fnamem.insert(0,"MIDDLE NAME")
	global Fnames
	Fnames= Entry(newWindow, width=27,bd=3,justify=CENTER)
	Fnames.grid(row=4, column=3,rowspan=1,sticky='nse')
	Fnames.insert(0,"SURNAME")
	
	
	
	global Mname1
	Mname1=Entry(newWindow,width=27,bd=3,justify=CENTER)
	Mname1.grid(row=5,column=3,sticky='nsw')
	Mname1.insert(0,"FIRST NAME")
	global Mnamem
	Mnamem= Entry(newWindow, width=27,bd=3,justify=CENTER)
	Mnamem.grid(row=5, column=3,rowspan=1,columnspan=10,sticky='ns')
	Mnamem.insert(0,"MIDDLE NAME")
	global Mnames
	Mnames= Entry(newWindow, width=27,bd=3,justify=CENTER)
	Mnames.grid(row=5, column=3,rowspan=1,sticky='nse')
	Mnames.insert(0,"SURNAME")
	

	
	
	global mail
	mail=Entry(newWindow,width=82,bd=3)
	mail.grid(row=6,column=3,sticky='nsew')

	
	
	
			# Create Text Box Labels
	Heading=Label(newWindow,borderwidth =10,width =20,relief="ridge",bg="#BFE6FF",font='Futura 16 bold',text="PERSONAL DETAILS")
	Heading.grid(row=0,column=1,columnspan=10,sticky='nsew')
	
	Name= Label(newWindow, text="Name of Applicant",borderwidth =3,width =26,relief="sunken",font='Futura 12')
	Name.grid(row=1, column=1)
	Birthdate= Label(newWindow, text="Date of Birth",borderwidth =3,width =26,relief="sunken",font='Futura 12')
	Birthdate.grid(row=2, column=1)
	
	
			#Checking date & names
	
	
	def check_date():
		global i
		i=int(Birthdated.get())
		global j
		j=int(Birth_datem.get())
		global k
		k=int(Birth_datey.get())
		
		if i in range(1,32):
			pass
		else:
			messagebox.showwarning("ERROR", "Please Enter a valid numeric Birth date" ) 
		if j in range(1,13):
			pass
		else:
			messagebox.showwarning("ERROR", "Please Enter a valid numeric Birth date" ) 
		if k in range(1910,2003):
			pass
		else:
			messagebox.showwarning("ERROR", "Please Enter a valid numeric Birth date \n                                 OR \n Your age don\'t meet Our elgibilty Criteria")
				
		n=name.get()
		middlen=namem.get()
		surnamen=names.get()
		bb=Mname1.get()
		bbb=Mnamem.get()
		bbbb=Mnames.get()
		cc=Fname1.get()
		ccc=Fnamem.get()
		cccc=Fnames.get()
		oo=Occupation1.get()
		mm=mail.get()
		if n!="FIRST NAME":
			pass
		else:
			messagebox.showwarning("ERROR", "ENTER FIRST NAME")
		if middlen!="MIDDLE NAME":
			pass
		else:
			messagebox.showwarning("ERROR", "ENTER MIDDLE NAME")
		if surnamen!="SURNAME":
				pass
		else:
				messagebox.showwarning("ERROR", "ENTER SURNAME")
		
		if bb!="FIRST NAME":
			pass
		else:
			messagebox.showwarning("ERROR", "ENTER MOTHER\'S FIRST NAME")
		if bbb!="MIDDLE NAME":
			pass
		else:
			messagebox.showwarning("ERROR", "ENTER MOTHER\'S MIDDLE NAME")
		if bbbb!="SURNAME":
				pass
		else:
				messagebox.showwarning("ERROR", "ENTER MOTHER\'S SURNAME NAME")
				
		if cc!="FIRST NAME":
			pass
		else:
			messagebox.showwarning("ERROR", "ENTER FATHER\'S FIRST NAME")
		if ccc!="MIDDLE NAME":
			pass
		else:
			messagebox.showwarning("ERROR", "ENTER FATHER\'S MIDDLE NAME")
		if cccc!="SURNAME":
				pass
		else:
				messagebox.showwarning("ERROR", "ENTER FATHER\'S SURNAME NAME")
			
		
		if oo!="":
		 	pass
		else:
		 	messagebox.showwarning("ERROR", "ENTER OCCUPATION")
		if mm!="":
			
		 	pass
		else:
		 	messagebox.showwarning("ERROR", "ENTER EMAIL")		 
		 
			
				
		if j in range(1,13) and i in range(1,31) and k in range(1910,2003) and surnamen !="SURNAME" and middlen !="MIDDLE NAME" and n!="FIRST NAME" and bbbb !="SURNAME" and bbb !="MIDDLE NAME" and bb!="FIRST NAME" and cccc !="SURNAME" and ccc !="MIDDLE NAME" and cc!="FIRST NAME" and oo !="" and mm !="":
				

			newwindow1()
		else:
			pass
			
		
		
	
			
              #--------------------------------#
	
	
	Occupation= Label(newWindow,text="Enter Your Occupation",borderwidth =3,width =26,relief="sunken",font='Futura 12')
	Occupation.grid(row=3,column=1)

	Fname= Label(newWindow, text="Father\'s Name",borderwidth =3,width =26,relief="sunken",font='Futura 12')
	Fname.grid(row=4,column=1)
	
	
	Mname=Label(newWindow,text="Mother\'s Name",borderwidth =3,width =26,relief="sunken",font='Futura 12')
	Mname.grid(row=5,column=1)

	
	email=Label(newWindow,text="Email id",borderwidth =3,width =26,relief="sunken",font='Futura 12')
	email.grid(row=6,column=1)
	
	
	
	
	Next=Button(newWindow,text='NEXT',command=check_date,borderwidth = 6,width =49,relief="raised",font='Futura 11 bold underline')
	Next.grid(row=9,column=1,columnspan=20,sticky='nsew')

	space3=Label(newWindow,text="")
	space3.grid(row=0)
	space4=Label(newWindow,text="")
	space4.grid(row=8)
	space5=Label(newWindow,text="")
	space5.grid(row=9)
	
	#colon labels
	
	colon1=Label(newWindow,text=":")
	colon2=Label(newWindow,text=":")
	colon3=Label(newWindow,text=":")
	colon4=Label(newWindow,text=":")
	colon5=Label(newWindow,text=":")
	colon6=Label(newWindow,text=":")
	
	colon1.grid(row=1,column=2)
	colon2.grid(row=2,column=2)
	colon3.grid(row=3,column=2)
	colon4.grid(row=4,column=2)
	colon5.grid(row=5,column=2)
	colon6.grid(row=6,column=2)
	
def get():
		
	p=name.get()
	q=namem.get()
	r=names.get()
	global full_name
	full_name=p+" "+q+" "+r
	
	global occ
	occ=Occupation1.get()
		
	t=Fname1.get()
	u=Fnamem.get()
	v=Fnames.get()
	global FATHER_FULL
	FATHER_FULL=t+" "+u+" "+v
	
	w=Mname1.get()
	x=Mnamem.get()
	y=Mnames.get()	
	global MOTHER_FULL
	MOTHER_FULL=w+" "+x+" "+y		
	global email1
	email1=mail.get()
	
	global add
	add=Address1.get()
	
	global Padd
	Padd=Permanent_add.get()	
		
	global pinco
	pinco=Pincode.get()
	
	global mobnum
	mobnum=Mnum.get()	
	
	global mobnum1
	mobnum1=Mnum1.get()	
	
	global landnum
	landnum=Lannum.get()
	
				
	global l
	l=(str(i)+"/"+str(j)+"/"+str(k))	
	
	global ppp
	ppp=Passwo1.get()
	global pppp
	pppp=Passwo.get()
	

def submit():
	con = sqlite3.connect('globalbank.db')
	c=con.cursor()
	b=("create table if not exists "+Accountnumb+ " (Account_number integer,Password text, Account_Holders_name text, Mothers_name text, Fathers_name text, Birthdate text, Temporary_address text, Permanent_address text, Pincode integer, Email_id text, Occupation text, Phone_number integer, Mobile_number integer, Landline_number integer, Status text default DEACTIVE, Date_of_transaction text default NO_TRANSACTIONS, last_transaction text default '0',Balance integer default 0)")

	
	c.execute(b)
	
	c.execute ("INSERT INTO" +Accountnumb +"(Account_number,Password,Account_Holders_name,Mothers_name,Fathers_name,Birthdate,Temporary_address,Permanent_address,Pincode,Email_id,Occupation,Phone_number,Mobile_number,Landline_number)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(Accnumber,str(ppp),full_name,MOTHER_FULL,FATHER_FULL,l,add,Padd,pinco,email1,occ,mobnum,mobnum1,landnum))



	con.commit()

 
	con.close() 
	
#•••••••••••••••END 1ST BUTTON••••••••••••#


#--------------------------------------------------------------#

#---------------------MAIN WINDOW-----------------#

#--------------------------------------------------------------#


wlcm= Label(root,borderwidth = 20,width =47,pady="10",relief="ridge",bg="#FFF1A5",font='Futura 32 bold underline',text="WELCOME TO THE BANK")

stmt1=Label(root,borderwidth =10,width =40,relief="ridge",bg="#BFE6FF",font='Futura 14 bold',text=" HOW CAN WE HELP YOU?")

stmt2= Label(root,borderwidth = 8,width =54,relief="sunken",font='Futura 14 bold underline',text="SELECT WHAT DO YOU WANT TO PERFORM:")

but1=Button(root,borderwidth = 8,width =49,relief="raised",font='Futura 11 bold underline',text='REQUEST FOR OPENING \n NEW ACCOUNT',command=newWindow)

but2=Button(root,borderwidth = 8,width =49,relief="raised",font='Futura 11 bold underline',text='WITHDRAW MONEY',command=withdrawwindow)
but3=Button(root,borderwidth = 8,width =49,relief="raised",font='Futura 11 bold underline',text='DEPOSIT MONEY',command=depositwindow)
but7=Button(root,borderwidth = 8,width =49,relief="raised",font='Futura 11 bold underline',text='UPDATE YOUR INFORMATION',command=updatewindow)
but5=Button(root,borderwidth = 8,width =49,relief="raised",font='Futura 11 bold underline',text='DIGITAL PASSBOOK \n (see latest transactions)',command=passbookwindow)
but6=Button(root,borderwidth = 8,width =49,relief="raised",font='Futura 11 bold underline',text='TRANSFER MONEY',command=transferwindowp)
but4=Button(root,borderwidth = 8,width =49,relief="raised",font='Futura 11 bold underline',text='REQUEST FOR ISSUING\n CHEQUE BOOK',command=chequebookwindow)
but8=Button(root,borderwidth = 8,width =49,relief="raised",font='Futura 11 bold underline',text='REQUEST FOR CLOSING \n YOUR ACCOUNT',command=deletewindow)

staff=Label(root,borderwidth =10,width =40,relief="ridge",bg="#BFE6FF",font='Futura 14 bold',text=" ONLY STAFF ACESS")

staff.grid(row="14",column="6",rowspan="1",columnspan="8",sticky='nsew')

activate=Button(root,borderwidth = 8,command=Entrywindowp,width =49,relief="raised",font='Futura 11 bold underline',text='ACTIVATE ACCOUNT')
activate.grid(row="15",column="6",rowspan="1",columnspan="8",sticky='nsew')


space=Label(root,text="")

space1=Label(root,text="")

space6=Label(root,text="")

wlcm.grid(row="0",column="0",columnspan="21",sticky='nsew')
stmt1.grid(row="2",column="6",rowspan="1",columnspan="8",sticky='nsew')
stmt2.grid(row="4",column="3",rowspan="3",columnspan="14",pady=10,sticky='nsew')
space.grid(row="1")
space1.grid(row="3")
space6.grid(row="13")
but1.grid(row="8",column="3",columnspan="7",sticky=' nsew')
but2.grid(row="10",column="3",columnspan="7",sticky='w')
but3.grid(row="11",column="3",columnspan="7",sticky='w')
but4.grid(row="12",column="3",columnspan="7",sticky='w')
but5.grid(row="8",column="10",columnspan="7")
but6.grid(row="10",column="10",columnspan="7")
but7.grid(row="11",column="10",columnspan="7")
but8.grid(row="12",column="10",columnspan="7")


root.mainloop()

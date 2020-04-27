#tkinter tourism app: barcelona --- 2017/12/09
# by: rohun baxi

#imports and initialization
#optimised for full hd screen
from tkinter import *
import webbrowser

root = Tk()
root.title('Barcelona Tourism App')


root.grid_rowconfigure(0, minsize = 50)
root.grid_rowconfigure(1, minsize = 0)
root.grid_rowconfigure(2, minsize = 0)
root.grid_rowconfigure(3, minsize = 0)

for n in range(18):
               root.grid_columnconfigure(n, minsize = 20)

root.grid_columnconfigure(12, minsize = 20)


root.minsize(width=1080, height=600)

#title
Label(root,text='Visit Barcelona!', bg = "yellow", fg = "red", font=("Times New Roman bold", 30)).place(relx=0.48, rely=0.04, anchor=CENTER)#place



#functions for each of the 6 widgets 
def CurrencyConv():
    class CurrencyConversion:#converts CAD to EUR
        def __init__(self):
            
            Label(root,text = "Euro Currency Conversion", font = "Times 12 bold", bg = 'yellow', fg = "black").grid(row=2,column=1, sticky =W)
            

            X = Label(root, text = "Canadian Dollars ($):", bg = "pink", fg = "maroon").grid(row = 3, column = 1, sticky = W)
            Y = Label(root, text = "Euros (Currency of Spain):").grid(row = 4, column = 1, sticky = W)

            self.cdn = StringVar()
            Entry(root, textvariable = self.cdn, justify = RIGHT).grid(row =3, column = 3)

            self.euro = StringVar()
            lblTotalPayment = Label(root, textvariable = self.euro).grid(row = 4, column = 3, sticky = E)

            Z = btComputePayment = Button(root, text = "Convert to Euros  ", bg = "red", fg = "white", command = self.eurocostcalcs).grid(row = 5, column = 3, sticky = E)

            root.mainloop()

        def eurocostcalcs(self):
            eurosss = float(self.cdn.get()) * 0.66
            eurosss = format(eurosss, '.2f')
            eurosss = str(eurosss)
            self.euro.set(format('>>>>>>>> ' + eurosss))                 
        def finaleuros(self, cdn, euro):
            return finaleuros;

    CurrencyConversion()


def Weather():
    class WeatherConversion:#otuputs weather depending on month
        def __init__(self):
            
            Label(root,text = "Barca Weather Convertor", font = "Times 12 bold", bg = 'yellow', fg = "black").grid(row=2,column=1, sticky =W)
            X = Label(root, text = "MONTH of the Year:", bg = "pink", fg = "maroon").grid(row = 3, column = 1, sticky = W)
            Y = Label(root, text = "Temperature (High/Low):").grid(row = 4, column = 1, sticky = W)

            self.monthh = StringVar()
            Entry(root, textvariable = self.monthh, justify = RIGHT).grid(row = 3, column = 3)

            self.temperature = StringVar()
            lblTotalPayment = Label(root, textvariable = self.temperature).grid(row = 4, column = 3, sticky = E)

            Z = btComputePayment = Button(root, text = "Find Temperature", bg = "red", fg = "white", command = self.conversion).grid(row = 5, column = 3, sticky = E)

            root.mainloop()

        def conversion(self):
            month = str(self.monthh.get())
            
            if month == ("January"):
                month = ("High: 15, Low: 9")
            elif month == ('February'):
                month = ("High: 16, Low: 9")
            elif month == ('March'):
                month = ("High: 17, Low: 11")
            elif month == ('April'):
                month = ("High: 19, Low: 13")
            elif month == ('May'):
                month = ("High: 23, Low: 16")
            elif month == ('June'):
                month = ("High: 26, Low: 20")
            elif month == ('July'):
                month = ("High: 29, Low: 23")
            elif month == ('August'):
                month = ("High: 29, Low: 23")
            elif month == ('September'):
                month = ("High: 26, Low: 20")
            elif month == ('October'):
                month = ("High: 23, Low: 17")
            elif month == ('November'):
                month = ("High: 18, Low: 12")
            elif month == ('December'):
                month = ("High: 15, Low: 10")


            self.temperature.set(format(month))

                         
        def month(self, monthh, temperature):
            return month;

        x = Label(root,text='... With This App, You Can Better Plan Your Dream Vacation!!!', bg = '#6bf0ff', font=("Courier New bold italic", 16)).grid(row=14, column=4, columnspan = 5)


    WeatherConversion()




def Demo():#informs user on barcelona's demographics
    Label(root,text='Demographics:', bg = "light blue", font=("Courier New bold italic", 16)).grid(row= 6, column=1, sticky = W)
    Label(root,fg = '#021be0', text='Population Density: 5065 people/ km squared.\nEthnicities: 59% Catalonian - 18% Other Spanish - 23% Foreigners\nReligion: 50% Catholic - 6% Muslim - 44% Atheist/ Other\nPopulation: 1 608 746', font=("Courier New",12)).grid(row=8, column=1, sticky = E)

def POI():#lists 5 major places of intrest user should visit
    Label(root,text='Points of Intrest:', bg = "hot pink", font=("Courier New bold italic", 16)).grid(row= 14, column=1, sticky = W)
    Label(root,fg = '#db00c8', text='1. Sagrada Familia\n2. Casa Mila\n3. Gothic Quarter\n4. Camp Nou (FC Barcelona)\n5. Museu Picasso', font=("Courier New",12)).grid(row=16, column=1)
    
def Politics():#talks about politics and the situation in barcelona
    Label(root,text='Politics:', bg = "#25ff00", font=("Courier New bold italic", 16)).grid(row= 3, column=8, sticky = W)
    Label(root,fg = '#006811', text="The current mayor of Barcelona is Ada Collau Ballona,\n and the city as a whole is the capital of the Spanish community of Catalonia,\n the wealthiest of region of the country.\nThe regional government is headquartered in the city's main park: Parc de la Ciutadella.\nCurrently, the Catalonian community wishes to gain independance from Spain\n and the headquarters of said movement is the city of Barcelona.\nThe movement is mostly due to the economic superiority of the region\n and the distinct sense of Catalonian heritage\n with the movement as a whole proving Barcelona's importance as a political center.", justify = LEFT, font=("Courier New",11)).grid(row=5, column=8)

def Web():
    url = 'http://www.barcelonaturisme.com/wv3/en/'
    webbrowser.open(url,2)

    
def Quit():#exits program upon command
    quit()



#inserts menubar from which user can call all widget functions
menubar = Menu(root)
menubar.add_command(label="Currency Conversion!", command=CurrencyConv)
menubar.add_command(label='Local Weather', command= Weather)
menubar.add_command(label='Demographics', command =Demo)
menubar.add_command(label='Points of Intrest', command =POI)
menubar.add_command(label='Politics', command =Politics)
menubar.add_command(label='Official Website',command=Web)
menubar.add_command(label="Quit!", command=Quit)


# display the menu
root.config(menu=menubar)



#conclusory text
Label(root,text='Thank You For Using This Program! Hope you come and visit us.', underline = 0, fg = '#ff8c00', font=("Times New Roman bold italic", 14)).grid(row=12, column=4, columnspan = 5)
root.mainloop()

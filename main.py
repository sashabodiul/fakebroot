from tkinter import *
from async_tkinter_loop import async_handler, async_mainloop
import asyncio
from PIL import ImageTk, Image
import random
import os

class Broot(Tk):
    def __init__(self):
        super().__init__()
        # set window size
        self.geometry("500x800")
        self.title("Broot")
        self.resizable(False,False)
        # Add image file
        # self.bg = PhotoImage(file = "./source/img/fakebroot.png")

        # # Show image using label
        # self.label1 = Label(self, image = self.bg)
        # self.label1.place(x = 0, y = 0)

        self.lbl_check = Label(self, text = "Checked")
        self.lbl_check.place(x=560/2/2/2, y=20, width=160,height=60)
        with open("list.txt") as m:
            self.m = m.readlines() 
        self.tb = Text(
            self,
            height=9,
            width=40,
            background='black',
            fg='white'
        )
        self.tb.place(x=560/2/2/2, y=80,)

        self.lbl_found = Label(self, text = "Founde:")
        self.lbl_found.place(x=560/2/2/2, y=250, width=140,height=60)
        self.tbf = Text(
            self,
            height=9,
            width=40,
            background='white',
            fg='green'
        )
        self.tbf.place(x=560/2/2/2, y=300,)
        img = ImageTk.PhotoImage(Image.open('./source/img/1.png')) # the one-liner I used in my app
        label = Label(self, image=img)
        label.image = img # this feels redundant but the image didn't show up without it in my app
        label.place(x=560/2/2/2-10, y=530)

        img1 = ImageTk.PhotoImage(Image.open('./source/img/2.png')) # the one-liner I used in my app
        label1 = Label(self, image=img1)
        label1.image = img1 # this feels redundant but the image didn't show up without it in my app
        label1.place(x=560/2/2/2-10+145, y=530)

        img2 = ImageTk.PhotoImage(Image.open('./source/img/3.png')) # the one-liner I used in my app
        label2 = Label(self, image=img2)
        label2.image2 = img2 # this feels redundant but the image didn't show up without it in my app
        label2.place(x=560/2/2/2-10+290, y=530)

        self.btc = StringVar()
        self.ltc = StringVar()
        self.eth = StringVar()
        Checkbutton(self,
                variable=self.btc,
                onvalue='btc',
                offvalue='disagree',).place(x=560/2/2/2+40, y=670,)
        Checkbutton(self,
                variable=self.ltc,
                onvalue='ltc',
                offvalue='disagree').place(x=560/2/2+115, y=670,)
        Checkbutton(self,
                variable=self.eth,
                onvalue='eth',
                offvalue='disagree').place(x=560/2+120, y=670,)
        btn_start = Button(self, text="Start", bg='green', fg='white', command = self.broot, width=20,height=3, cursor='hand2')
        btn_start.place(x=560/2/2/2, y=700,)
        btn_start = Button(self, text="Stop",  bg='red', fg='white', command = self.stopcheck, width=20,height=3, cursor='hand2')
        btn_start.place(x=560/2, y=700,)

    @async_handler
    async def broot(self):
        self.check = True
        c=0
        checker = 0
        found = 0
        while self.check == True:
            if c == len(self.m):
                c = 0
            self.tb.insert('1.0',f'Wallet check:{self.m[c]}')
            checker+=1
            self.lbl_check.configure(text=f'Checked: {checker} wallets')
            c+=1
            r = random.randint(1,10000)
            btc_r = random.randint(1,10000)
            ltc_r = random.randint(1,10000)
            eth_r = random.randint(1,10000)
            if self.btc.get() == 'btc' and btc_r == r:
                self.tbf.configure(fg='green')
                found+=1
                self.tbf.insert('1.0', f'BTC:{random.randint(0,4000)}$ found\n')
            if self.ltc.get() == 'ltc' and ltc_r == r:
                self.tbf.configure(fg='green')
                self.tbf.insert('1.0', f'LTC:{random.randint(0,400)}$ found\n')
                found+=1
            if self.eth.get() == 'eth' and eth_r == r:
                self.tbf.configure(fg='green')
                found+=1
                self.tbf.insert('1.0', f'ETH:{random.randint(0,1000)}$ found\n')
            self.lbl_found.configure(text=f'Find: {found} results')
            await asyncio.sleep(0.001)

    def stopcheck(self):
        self.check = False


app = Broot()
async_mainloop(app)
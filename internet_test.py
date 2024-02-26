from tkinter import * #type: ignore
import speedtest
if __name__ == "__main__":
    def speed_Checker():
        sp = speedtest.Speedtest() # Here speedtest is module and .Speedtest() is a class so sp
        upload = str(round(sp.upload()/(10**6),3)) + "Mbps"
        down = str(round(sp.download()/(10**6),3)) + "Mbps"
        text2.config(text=down)
        text4.config(text=upload)
        quit()

    root = Tk()
    root.geometry("600x600")
    root.config(bg="black")

    text = Label(root,text="Internet Speed Test",bg="Black",fg="red",font=("New Roman Times",30,"bold","underline"))
    text.place(x=120,y=0)


    button1 = Button(root, text = "Check Your internet speed",font =("New Roman Times",25,"bold"),fg="white",padx= 5, pady = 1,bg="cyan",command= speed_Checker)
    button1.place(x=75,y=100)


    text1 = Label(root,text="Download Speed",bg="Black",fg="red",font=("New Roman Times",30,"bold","underline"))
    text1.place(x=150,y=200)


    text2 = Label(root,text="00",bg="white",fg="red",font=("New Roman Times",30,"bold"))
    text2.place(x=100,y=280,width=400,height = 50)

    text3 = Label(root,text="Upload speed",bg="Black",fg="red",font=("New Roman Times",30,"bold","underline"))
    text3.place(x=150,y=350)


    text4 = Label(root,text="00",bg="white",fg="red",font=("New Roman Times",30,"bold"))
    text4.place(x=100,y=430,width=400,height = 50)

    root.mainloop()
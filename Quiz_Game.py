from tkinter import *
import tkinter.messagebox
class quiz:
    def __init__(self,window):
        self.window=window
        self.ans = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        topframe=Frame(self.window,width=500,height=350,bg="lightyellow")
        topframe.place(x=450,y=160)
        label_1=Label(topframe,text="WELCOME TO PYTHON QUIZ",bg="lightyellow")
        label_1.place(x=50,y=10)
        self.name=StringVar()
        self.reg=StringVar()
        self.sec=StringVar()
        label_2=Label(topframe,text="Name",bg="lightyellow")
        label_3=Label(topframe,text="Registration No.",bg="lightyellow")
        label_4=Label(topframe,text="Section",bg="lightyellow")
        label_5=Label(topframe,text="Level",bg="lightyellow")
        label_2.place(x=0,y=35)
        label_3.place(x=0,y=55)
        label_4.place(x=0,y=75)
        label_5.place(x=0,y=95)
        entry_1=Entry(topframe,textvariable=self.name)
        entry_2=Entry(topframe,textvariable=self.reg)
        entry_3=Entry(topframe,textvariable=self.sec)
        entry_1.place(x=100,y=35)
        entry_2.place(x=100,y=55)
        entry_3.place(x=100,y=75)
        self.level=IntVar()
        button_1=Radiobutton(topframe,variable=self.level,value=1,bg="lightyellow")
        button_2=Radiobutton(topframe,variable=self.level,value=2,bg="lightyellow")
        button_3=Radiobutton(topframe,variable=self.level,value=3,bg="lightyellow")
        label_6=Label(topframe,text="Easy",bg="lightyellow")
        label_7=Label(topframe,text="Medium",bg="lightyellow")
        label_8=Label(topframe,text="Tough",bg="lightyellow")
        button_1.place(x=100,y=95)
        button_2.place(x=100,y=115)
        button_3.place(x=100,y=135)
        label_6.place(x=130,y=95)
        label_7.place(x=130,y=115)
        label_8.place(x=130,y=135)
        button_4=Button(topframe,text="Submit",width=10,command=self.levelcheck,bg="green",activebackground="red")
        button_4.place(x=120,y=170)
    def levelcheck(self):
        if len(self.name.get())==0:
            tkinter.messagebox.showinfo("Warning","Enter name")
        elif len(self.reg.get())==0:
            tkinter.messagebox.showinfo("Warning","Enter registration number")
        elif len(self.sec.get())==0:
            tkinter.messagebox.showinfo("Warning","Enter section")
        else:
            if self.level.get()==1:
                self.easy()
            elif self.level.get()==2:
                self.medium()
            else:
                self.tough()
    def result(self):
        answer=tkinter.messagebox.askyesno('quiz','Do you want to submit')
        if answer == True:
            topframe=Frame(self.window,width=400,height=300,bg="lightyellow")
            topframe.place(x=450,y=160)
            score=0
            j=0
            while j<10:
                if self.ans[j]==self.answer[j]:
                    score=score+1
                j=j+1
        str(score)
        labeln=Label(topframe,text="Results of:-",font="Verdana 15 bold",bg="lightyellow")
        labeln.place(x=130,y=130)
        labelName=Label(topframe,text=self.name.get(),font="Verdana 10 bold",bg="lightyellow",fg="Blue")
        labelName.place(x=270,y=135)
        labelScore=Label(topframe,text=score,font="Verdana 10 bold",bg="lightyellow")
        labelScore.place(x=150,y=200)
        labeltotalscore=Label(topframe,text="<--   Out of 10",font="Verdana 10 bold",bg="lightyellow")
        labeltotalscore.place(x=180,y=200)


    def increment(self,question,option):
        self.ans[self.i]=self.ans1.get()
        self.i = self.i + 1
        if(self.i<10 and self.i>=0):
            self.create(question,option)
        else:
            self.i=self.i-1
            self.create(question,option)
    def decrement(self,question,option):
        self.i = self.i - 1
        if(self.i<0):
            self.i=0
            self.create(question,option)
        else:
            self.create(question,option)

    def create(self,question,option):
        topframe=Frame(self.window,width=400,height=160,bg="lightyellow")
        topframe.place(x=450,y=160)
        labelQuest=Label(topframe,text=question[self.i],bg="lightyellow")
        labelQuest.place(x=10,y=50)
        selectOpt1=Radiobutton(topframe,text=option[self.i][0],variable=self.ans1,value=0,bg="lightyellow")
        selectOpt2=Radiobutton(topframe,text=option[self.i][1],variable=self.ans1,value=1,bg="lightyellow")
        selectOpt3=Radiobutton(topframe,text=option[self.i][2],variable=self.ans1,value=2,bg="lightyellow")
        selectOpt4=Radiobutton(topframe,text=option[self.i][3],variable=self.ans1,value=3,bg="lightyellow")
        selectOpt1.place(x=15,y=80)
        selectOpt2.place(x=15,y=100)
        selectOpt3.place(x=15,y=120)
        selectOpt4.place(x=15,y=140)

    def medium(self):
        question=["Q1. Q1.For tuples and list which is correct?",
                  "Q2. Which is invalid in python for z = 5",
                  "Q3. Which among them is used to create an object?",
                  "Q4. Which of the following statements is true?",
                  "Q5. What is used to define a block of code (body of loop, function etc.) in Python?",
                  "Q6. In the following code n='5', n is a/an _______?",
                  "Q7. What is used to take input from the user in Python?",
                  "Q8. What is the output of this code? print(3>=3)",
                  "Q9. The statement using and operator results true if _______",
                  "Q10. Constructor of a class is called when?"]

        option=[["List and tuple both are mutable","List is mutable whereas tuples are immutable","List and tuples both are immutable.","List is immutable whereas tuples are mutable"],
                ["z = z++","z = ++z","z += 1","z -= 1"],
                ["A class","A function","A method","A constructor"],
                ["Python is a high level programming language.","Python is an interpreted language.","Python is an object-oriented language.","All of the above."],
                ["Curly braces","Parenthesis","Indentation","Quotation"],
                ["string","tuple","Integer","operator"],
                ["cin","scanf()","input()","<>"],
                ["3>=3","True","false","None"],
                ["both operands are true","both operands are false","either of the operands is true","first operand is true"],
                ["class is formed","object is formed","instance of a class is formed","2 and 3 both"],
                ]
        self.answer=[1, 0, 3, 3, 2, 0, 2, 1, 0, 3]

        topframe=Frame(self.window,width=400,height=300,bg="lightyellow")
        topframe.place(x=450,y=160)
        labelName=Label(topframe,text="Welcome "+self.name.get(),bg="lightyellow",fg="blue")
        labelName.place(x=10,y=10)
        self.i = 0
        self.ans1=IntVar()
        self.create(question,option)
        butB=Button(topframe,text="<- Back",width=7,command=lambda: self.decrement(question,option),bg="red",fg="black")
        butN=Button(topframe,text="Next ->",width=7,command=lambda: self.increment(question,option),bg="yellow",fg="black")
        butS=Button(topframe,text="Submit",width=7,command=self.result,bg="green",fg="black")
        butB.place(x=50,y=220)
        butN.place(x=250,y=220)
        butS.place(x=140,y=220)

    def easy(self):
        question=["Q1. Which is the correct operator for power(x)??",
                  "Q2. Which one of these is floor division?",
                  "Q3. What is answer of this expression, 22 % 3 is?",
                  "Q4. Operators with the same precedence are evaluated in which manner??",
                  "Q5. Which of these in not a core data type?",
                  "Q6. What is the return type of function id ?",
                  "Q7. What error occurs when you execute?  apple=mango",
                  "Q8.  In order to store values in terms of key and value we use what core data type.",
                  "Q9.  What is the return value of trunc() ?",
                  "Q10. What is the maximum possible length of an identifier?"]

        option=[["x^y","x**y","x^^y","None of the mentioned."],
                ["/","//","%","None of the mentioned."],
                ["1","7","0","3"],
                ["Left to Right","Right to left","can't say.","None of the mentioned."],
                ["Lists","Dictionary","Tuples","Class"],
                ["int","float","bool","dict"],
                ["syntax error","name error","value error","Type error"],
                ["List","Tuple","Dictionary","class"],
                ["int","bool","float","None"],
                ["31 characters","63 characters","92 characters","None of the mentioned"],
                ]
        self.answer=[1, 1, 0, 0, 3, 0, 1, 2, 0, 0]

        topframe=Frame(self.window,width=400,height=300,bg="lightyellow")
        topframe.place(x=450,y=160)
        labelName=Label(topframe,text="Welcome "+self.name.get(),bg="lightyellow",fg="blue")
        labelName.place(x=10,y=10)
        self.i = 0
        self.ans1=IntVar()
        self.create(question,option)
        butB=Button(topframe,text="<- Back",width=7,command=lambda: self.decrement(question,option),bg="red",fg="black")
        butN=Button(topframe,text="Next ->",width=7,command=lambda: self.increment(question,option),bg="yellow",fg="black")
        butS=Button(topframe,text="Submit",width=7,command=self.result,bg="green",fg="black")
        butB.place(x=50,y=220)
        butN.place(x=250,y=220)
        butS.place(x=140,y=220)

    def tough(self):
        question=["Q1. Is Python case sensitive when dealing with identifiers??",
                  "Q2. Why are local variable names beginning with an underscore discouraged?",
                  "Q3. Which of the following is not a keyword?",
                  "Q4. All keywords in Python are in",
                  "Q5. Which of the following cannot be a variable?",
                  "Q6. What is the result of math.trunc(3.1)? ?",
                  "Q7. Which of the following is the same as math.exp(p)?",
                  "Q8. What is the default base used when math.log(x) is found?",
                  "Q9. Which of these is false about recursion?",
                  "Q10. What is tail recursion?"]

        option=[["yes","no","machine dependent","None of the mentioned."],
                ["they are used to indicate a private variables of a class"," they confuse the interpreter"," they are used to indicate global variables","they slow down execution."],
                ["eval","assert","nonlocal","pass"],
                ["lower case","UPPER CASE","capitalized.","None of the mentioned."],
                ["__init__","in","it","on"],
                ["3.0","3","0.1","1"],
                ["e**p","math.e ** p","p ** e"," p ** math.e"],
                ["e","10","2","None"],
                ["Recursive function can be replaced by a non-recursive function","Recursive functions usually take more memory space than non-recursive function","Recursive functions run faster than non-recursive function","Recursion makes programs easier to understand"],
                ["A recursive function that has two base cases","A function where the recursive functions leads to an infinite loop","A recursive function where the function doesn’t return anything and just prints the values"," A function where the recursive call is the last thing executed by the function"],
                ]
        self.answer=[0, 0, 0, 3, 0, 1, 1, 0, 2, 3]

        topframe=Frame(self.window,width=400,height=300,bg="lightyellow")
        topframe.place(x=450,y=160)
        labelName=Label(topframe,text="Welcome "+self.name.get(),bg="lightyellow",fg="blue")
        labelName.place(x=10,y=10)
        self.i = 0
        self.ans1=IntVar()
        self.create(question,option)
        butB=Button(topframe,text="<-Back",width=7,command=lambda: self.decrement(question,option),bg="red",fg="black")
        butN=Button(topframe,text="Next->",width=7,command=lambda: self.increment(question,option),bg="yellow",fg="black")
        butS=Button(topframe,text="Submit",width=7,command=self.result,bg="green",fg="black")
        butB.place(x=50,y=220)
        butN.place(x=250,y=220)
        butS.place(x=140,y=220)









        

root = Tk()
root.configure(bg="pink")
root.geometry("1200x900")
app = quiz(root)
root.mainloop()

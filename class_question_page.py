from tkinter import *
import tkinter.font as font
import random
import sqlite3

conn = sqlite3.connect('questions.db')
 
c = conn.cursor()

class question_page(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, width=750, height=400, bg="#1c1b1c")
        self.font = font.Font(family='Helvetica', size=25)
        self.button_font = font.Font(family='Helvetica', size=15)

        self.question_number = 0
        print(self.question_number)

        self.rq_int = random.sample(range(1,6), 5)
        print(self.rq_int)

        self.question_func()
        self.A_func()
        self.B_func()
        self.C_func()
        self.D_func()

        
    
    def question_func(self):
        if self.question_number == 5:
            print("game over")
        else:
            for row in c.execute('SELECT question FROM questions WHERE rowid = ?', (self.rq_int[self.question_number],)):
                if self.rq_int[self.question_number] == 1:
                    self.question1 = Label(self, text=row, font=self.font, bg="#1c1b1c", fg="#ffffff")
                    self.question1.place(relx=0.5, rely=0.05, anchor=CENTER)
                if self.rq_int[self.question_number] == 2:
                    self.question2 = Label(self, text=row, font=self.font, bg="#1c1b1c", fg="#ffffff")
                    self.question2.place(relx=0.5, rely=0.05, anchor=CENTER)
                if self.rq_int[self.question_number] == 3:
                    self.question3 = Label(self, text=row, font=self.font, bg="#1c1b1c", fg="#ffffff")
                    self.question3.place(relx=0.5, rely=0.05, anchor=CENTER)
                if self.rq_int[self.question_number] == 4:
                    self.question4 = Label(self, text=row, font=self.font, bg="#1c1b1c", fg="#ffffff")
                    self.question4.place(relx=0.5, rely=0.05, anchor=CENTER)
                if self.rq_int[self.question_number] == 5:
                    self.question5 = Label(self, text=row, font=self.font, bg="#1c1b1c", fg="#ffffff")
                    self.question5.place(relx=0.5, rely=0.05, anchor=CENTER)

        
    
    def A_func(self):
        if self.question_number == 5:
            pass
        else:
            for row in c.execute('SELECT answers1 FROM questions WHERE rowid = ?', (self.rq_int[self.question_number],)):
                if self.rq_int[self.question_number] == 1:
                    self.A1 = Button(self, text=row, bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff", command=self.incorrect)
                    self.A1.place(relx=0.2, rely=0.25, anchor=CENTER)
                if self.rq_int[self.question_number] == 2:
                    self.A2 = Button(self, text=row, bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff", command=self.incorrect)
                    self.A2.place(relx=0.2, rely=0.25, anchor=CENTER)
                if self.rq_int[self.question_number] == 3:
                    self.A3 = Button(self, text=row, bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff", command=self.question3_correct)
                    self.A3.place(relx=0.2, rely=0.25, anchor=CENTER)
                if self.rq_int[self.question_number] == 4:
                    self.A4 = Button(self, text=row, bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff", command=self.incorrect)
                    self.A4.place(relx=0.2, rely=0.25, anchor=CENTER)
                if self.rq_int[self.question_number] == 5:
                    self.A5 = Button(self, text=row, bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff", command=self.question5_correct)
                    self.A5.place(relx=0.2, rely=0.25, anchor=CENTER)
    
    def B_func(self):
        if self.question_number == 5:
            pass
        else:
            for row in c.execute('SELECT answers2 FROM questions WHERE rowid = ?', (self.rq_int[self.question_number],)):
                if self.rq_int[self.question_number] == 1:
                    self.B1 = Button(self, text=row,bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff", command=self.question1_correct)
                    self.B1.place(relx=0.2, rely=0.45, anchor=CENTER)
                if self.rq_int[self.question_number] == 2:
                    self.B2 = Button(self, text=row,bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff", command=self.incorrect)
                    self.B2.place(relx=0.2, rely=0.45, anchor=CENTER)
                if self.rq_int[self.question_number] == 3:
                    self.B3 = Button(self, text=row,bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff", command=self.incorrect)
                    self.B3.place(relx=0.2, rely=0.45, anchor=CENTER)
                if self.rq_int[self.question_number] == 4:
                    self.B4 = Button(self, text=row,bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff", command=self.incorrect)
                    self.B4.place(relx=0.2, rely=0.45, anchor=CENTER)
                if self.rq_int[self.question_number] == 5:
                    self.B5 = Button(self, text=row,bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff", command=self.incorrect)
                    self.B5.place(relx=0.2, rely=0.45, anchor=CENTER)
    
    def C_func(self):
        if self.question_number == 5:
            pass
        else:
            for row in c.execute('SELECT answers3 FROM questions WHERE rowid = ?', (self.rq_int[self.question_number],)):
                if self.rq_int[self.question_number] == 1:
                    self.C1 = Button(self, text=row,bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff", command=self.incorrect)
                    self.C1.place(relx=0.2, rely=0.65, anchor=CENTER)
                if self.rq_int[self.question_number] == 2:
                    self.C2 = Button(self, text=row,bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff", command=self.question2_correct)
                    self.C2.place(relx=0.2, rely=0.65, anchor=CENTER)
                if self.rq_int[self.question_number] == 3:
                    self.C3 = Button(self, text=row,bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff", command=self.incorrect)
                    self.C3.place(relx=0.2, rely=0.65, anchor=CENTER)
                if self.rq_int[self.question_number] == 4:
                    self.C4 = Button(self, text=row,bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff", command=self.incorrect)
                    self.C4.place(relx=0.2, rely=0.65, anchor=CENTER)
                if self.rq_int[self.question_number] == 5:
                    self.C5 = Button(self, text=row,bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff", command=self.incorrect)
                    self.C5.place(relx=0.2, rely=0.65, anchor=CENTER)

    def D_func(self):
        if self.question_number == 5:
            pass
        else:
            for row in c.execute('SELECT answers4 FROM questions WHERE rowid = ?', (self.rq_int[self.question_number],)):
                if self.rq_int[self.question_number] == 1:
                    self.D1 = Button(self, text=row,bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff", command=self.incorrect)
                    self.D1.place(relx=0.2, rely=0.85, anchor=CENTER)
                if self.rq_int[self.question_number] == 2:
                    self.D2 = Button(self, text=row,bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff", command=self.incorrect)
                    self.D2.place(relx=0.2, rely=0.85, anchor=CENTER)
                if self.rq_int[self.question_number] == 3:
                    self.D3 = Button(self, text=row,bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff", command=self.incorrect)
                    self.D3.place(relx=0.2, rely=0.85, anchor=CENTER)
                if self.rq_int[self.question_number] == 4:
                    self.D4 = Button(self, text=row,bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff", command=self.question4_correct)
                    self.D4.place(relx=0.2, rely=0.85, anchor=CENTER)
                if self.rq_int[self.question_number] == 5:
                    self.D5 = Button(self, text=row,bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff", command=self.incorrect)
                    self.D5.place(relx=0.2, rely=0.85, anchor=CENTER)

    def question1_correct(self):
        self.question1.destroy()
        self.A1.destroy()
        self.B1.destroy()
        self.C1.destroy()
        self.D1.destroy()
        self.question_number = self.question_number + 1
        print(self.question_number)
            
        self.question_func()
        self.A_func()
        self.B_func()
        self.C_func()
        self.D_func()

    def question2_correct(self):
        self.question2.destroy()
        self.A2.destroy()
        self.B2.destroy()
        self.C2.destroy()
        self.D2.destroy()
        self.question_number = self.question_number + 1
        print(self.question_number)

        self.question_func()
        self.A_func()
        self.B_func()
        self.C_func()
        self.D_func()

    def question3_correct(self):
        self.question3.destroy()
        self.A3.destroy()
        self.B3.destroy()
        self.C3.destroy()
        self.D3.destroy()
        self.question_number = self.question_number + 1
        print(self.question_number)

        self.question_func()
        self.A_func()
        self.B_func()
        self.C_func()
        self.D_func()

    def question4_correct(self):
        self.question4.destroy()
        self.A4.destroy()
        self.B4.destroy()
        self.C4.destroy()
        self.D4.destroy()
        self.question_number = self.question_number + 1
        print(self.question_number)

        self.question_func()
        self.A_func()
        self.B_func()
        self.C_func()
        self.D_func()

    def question5_correct(self):
        self.question5.destroy()
        self.A5.destroy()
        self.B5.destroy()
        self.C5.destroy()
        self.D5.destroy()
        self.question_number = self.question_number + 1
        print(self.question_number)

        self.question_func()
        self.A_func()
        self.B_func()
        self.C_func()
        self.D_func()

    def incorrect(self):
        print("Incorrect")

    def choose_question(self):
        question = self.rq_int[1]

        for row in c.execute('SELECT question FROM questions WHERE rowid = ?', (rq_int[1],)):
            print(row)

if __name__ == "__main__":
    conn.commit()
    conn.close()
from tkinter import *
import tkinter.font as font
import random
import sqlite3

conn = sqlite3.connect('questions.db')
 
c = conn.cursor()

class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, width=750, height=400)
        self.font = font.Font(family='Helvetica', size=30)

        self.top_score = str(0)
        self.top_score_string = "Your Top Score: " + self.top_score
        print(self.top_score_string)
        top_score_label = Label(self, text=self.top_score_string, font=self.font)
        top_score_label.place(relx=0.5, rely=0.4, anchor=CENTER)

        title = Label(self, text="Computer Science Quiz!", font=self.font)
        title.place(relx=0.5, rely=0.05, anchor=CENTER)

        start_quiz_button = Button(self, text="Start Quiz", font=self.font, bg="#324ca8", fg="#ffffff", command=lambda: master.switch_frame(question_page))
        start_quiz_button.place(relx=0.5, rely=0.65, anchor=CENTER)


class question_page(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, width=750, height=400, bg="#1c1b1c")
        self.font = font.Font(family='Helvetica', size=25)
        self.button_font = font.Font(family='Helvetica', size=15)



        self.rq_int = random.sample(range(1,5), 1)

        for row in c.execute('SELECT question FROM questions WHERE rowid = ?', (self.rq_int[0],)):
            question = Label(self, text=row, font=self.font, bg="#1c1b1c", fg="#ffffff")
            question.place(relx=0.5, rely=0.05, anchor=CENTER)

        for row in c.execute('SELECT answers1 FROM questions WHERE rowid = ?', (self.rq_int[0],)):
            A = Button(self, text=row, bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff")
            A.place(relx=0.2, rely=0.25, anchor=CENTER)

        for row in c.execute('SELECT answers2 FROM questions WHERE rowid = ?', (self.rq_int[0],)):
            B = Button(self, text=row,bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff")
            B.place(relx=0.2, rely=0.45, anchor=CENTER)

        for row in c.execute('SELECT answers3 FROM questions WHERE rowid = ?', (self.rq_int[0],)):
            C = Button(self, text=row,bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff")
            C.place(relx=0.2, rely=0.65, anchor=CENTER)

        for row in c.execute('SELECT answers4 FROM questions WHERE rowid = ?', (self.rq_int[0],)):
            D = Button(self, text=row,bg="#1c1b1c", fg="#ffffff", font=self.button_font, activebackground="#4a4e54", activeforeground="#ffffff")
            D.place(relx=0.2, rely=0.85, anchor=CENTER)

        

    def choose_question(self):
        question = self.rq_int[1]

        for row in c.execute('SELECT question FROM questions WHERE rowid = ?', (rq_int[1],)):
            print(row)





        


if __name__ == "__main__":
    conn.commit()
    app = SampleApp()
    app.mainloop()
    conn.close()
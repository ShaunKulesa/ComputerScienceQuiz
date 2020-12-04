from tkinter import *
import tkinter.font as font
from class_question_page import question_page 

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
        

if __name__ == "__main__":
    
    app = SampleApp()
    app.mainloop()

    

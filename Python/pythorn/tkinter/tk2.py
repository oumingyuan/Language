import tkinter as tk


class APP:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.hi_here = tk.Button(frame, text='call', bg='black', fg='white', command=self.say_hi)

        self.hi_here.pack()

    def say_hi(self):
        print('lala')


root = tk.Tk()
app = APP(root)
root.mainloop()

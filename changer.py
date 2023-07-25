import customtkinter as ctk
import pywinstyles

class Changer(ctk.CTk):
    def __init__(self):
        super().__init__()  
        self.gui()
        
    def gui(self):
        '''Set windows title and geometry'''
        self.title("Changer Test")
        self.geometry(f"{200}x{120}") 
        '''Creating Main Frame for all gui elements'''
        self.main_frame = ctk.CTkFrame(self, width=510,height=290)
        self.main_frame.grid(row=0, column=10,columnspan=10, rowspan=10, ipadx=5, ipady=0, padx=0, pady=0, sticky="nw")
        self.main_frame.grid_rowconfigure(3, weight=1)
        '''All for integration pywinstyles'''
        styles = ["Choose Style", "dark", 
                    "mica", "aero", "transparent", 
                    "acrylic", "win7", "inverse", 
                    "popup", "native", "optimised",
                    "light"]
        self.switch_var2 = ctk.StringVar()
        self.switch_mode2 = ctk.CTkSwitch(self.main_frame,text="◆",font=("Arial", 25), variable=self.switch_var2,onvalue="on", offvalue="off",command=self.changer,progress_color=("#7d7de8","#6666FF"))
        self.switch_mode2.grid(row=5, column=3,columnspan=1, padx=5, pady=10, rowspan=1,sticky="nsew")

    '''Change style to transparent "aero" of pywinstyles'''    
    def changer(self):
        if self.switch_var2.get() == "on":
            pywinstyles.apply_style(self, "aero") 
            self.switch_var2.set("on")
            self.switch_mode2.configure(text="◇")
        elif self.switch_var2.get() == "off":   
            pywinstyles.apply_style(self, "dark")
            self.switch_mode2.configure(text="◆")

if __name__ == "__main__":
    app = Changer()  
    app.resizable(width=False, height=False)
    app.mainloop()
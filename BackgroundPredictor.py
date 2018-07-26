from tkinter import Tk, Canvas, Frame, BOTH
from random import randint
from sklearn import tree

class BackgroundPredictor(Frame):
    def __init__(self):
        super().__init__()   
        self.ui()
        
    def ui(self):
        self.master.title("Background Predictor")        
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        canvas.configure(background='#383838')
                         
        rc = (randint(0,255),randint(0,255),randint(0,255))                
        mycolor = '#%02x%02x%02x' % (rc)   
        colours = [[255,255,255],[0,0,0],[0,153,0],[51,0,0],[51,25,0],[52,52,0],[25,51,0],[0,51,0],[0,51,25],[0,51,51],[0,0,51],[51,0,51],[102,0,0],[102,51,0],[102,102,0],[51,102,0],[0,102,0],[176,23,31],[220,20,60],[230, 25, 75],[60, 180, 75],[0, 130, 200],[245, 130, 48],[145, 30, 180],[0, 128, 128],[170, 110, 40],[128, 0, 0],[128, 128, 0],[0, 0, 128],[255, 225, 25],[70, 240, 240],[210, 245, 60],[250, 190, 190],[230, 190, 255],[255, 250, 200],[170, 255, 195],[255, 215, 180],[128, 128, 128],[102,255,178],[153,255,255],[153,153,255],[255,153,204],[204,255,229],[255,204,204],[51,255,255],[255,51,255],[255,51,51],[102,102,255],[102,255,102],[192,192,192]]
        labels = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(colours,labels)
        p=clf.predict([rc])
        if p==[0]:
            canvas.create_oval(125, 50, 175, 100, fill="white", outline="white", width=2)
        else:
            canvas.create_oval(375, 50, 425, 100, fill="white", outline="white", width=2)
                         
        canvas.create_oval(50, 150, 250, 350, fill=mycolor, outline="#383838", width=2)
        canvas.create_text(150, 250,font=("Purisa", 30, 'bold'), text="BLACK", fill = "black")
        canvas.create_oval(300, 150, 500, 350, fill=mycolor, outline="#383838", width=2)
        canvas.create_text(400, 250,font=("Purisa", 30, 'bold'), text="WHITE", fill = "white")
        canvas.pack(fill=BOTH, expand=1)
            
def main():
    root = Tk()
    BackgroundPredictor()
    root.geometry("550x500+200+200")
    root.mainloop() 
    
if __name__ == '__main__':
    main()  
    
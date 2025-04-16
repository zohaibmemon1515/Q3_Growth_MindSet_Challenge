import tkinter as tk  # Tkinter library import kar rahe hain GUI (Graphics) banane ke liye

Cell_Size = 20  # Har ek box (cell) ka size 20x20 pixels hoga
Erase_Size = 20  # Eraser ka size bhi 20x20 pixels hoga
Rows = 10  # Grid ke total rows (upar se neeche)
column = 10  # Grid ke total columns (daayen se baayen)


class erase_canvas: # Ek class bana rahe hain jo canvas (drawing area) handle karegi
    def __init__(self, root):
      
        self.canvas = tk.Canvas(root, width=Cell_Size * column, height=Cell_Size * Rows, bg="white")   # Ek canvas bana rahe hain jisme grid draw hogi
        self.canvas.pack()  # Canvas ko window pe show kar rahe hain
        self.cells = {}  # Dictionary jisme har box (cell) ka position store hoga

        # Loop chala rahe hain grid (jaali) banane ke liye
        for i in range(Rows):  # Rows ke liye loop
            for j in range(column):  # Columns ke liye loop
                x1 = j * Cell_Size  # Har column ka x1 position
                x2 = x1 + Cell_Size  # Har column ka x2 position
                y1 = i * Cell_Size  # Har row ka y1 position
                y2 = y1 + Cell_Size  # Har row ka y2 position
               
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="white")  # Ek blue color ka block draw kar rahe hain
                self.cells[rect] = [x1, y1, x2, y2] # Har block ka position dictionary me save kar rahe hain

        
        self.eraser = self.canvas.create_rectangle(0, 0, Erase_Size, Erase_Size, outline="Red", fill="black") # Eraser banaya (yeh black color ka rectangle hoga)
        self.canvas.bind("<B1-Motion>", self.erase) # Mouse drag karne pe erase function chalega

    
    def erase(self, event): # Yeh function blocks erase karega jab mouse drag karoge
        x = event.x  # Mouse ka X position
        y = event.y  # Mouse ka Y position
        x1 = x - Erase_Size // 2  # Eraser ka start position
        x2 = x1 + Erase_Size  # Eraser ka end position
        y1 = y - Erase_Size // 2  # Eraser ka start position
        y2 = y1 + Erase_Size  # Eraser ka end position

       
        self.canvas.coords(self.eraser, x1, y1, x2, y2)  # Eraser ko move karwa rahe hain

        
        for rect, [rx1, ry1, rx2, ry2] in self.cells.items(): # Check kar rahe hain kon se blocks eraser ke andar aa rahe hain
            if not (rx2 < x1 or rx1 > x2 or ry2 < y1 or ry1 > y2):  # Agar eraser kisi block ke andar hai
                self.canvas.itemconfig(rect, fill="white")  # Us block ko white kar do (erase kar do)


root = tk.Tk() # Window (root) create kar rahe hain
root.title("Erase Canvas") # Window ka title set kar rahe hain
erase_canvas(root) # erase_canvas class ko initialize kar rahe hain (jo grid aur eraser handle karegi)
root.mainloop() # Tkinter ka main loop chala rahe hain takay window band na ho

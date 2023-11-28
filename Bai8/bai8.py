import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class ImageEdgeDetectionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Ứng dụng Tách biên ảnh")

        self.image_label = tk.Label(self.master)
        self.image_label.pack(padx=10, pady=10)

        self.load_button = tk.Button(self.master, text="Chọn ảnh", command=self.load_image)
        self.load_button.pack(pady=10)

        self.detect_edge_button = tk.Button(self.master, text="Tách biên ảnh", command=self.detect_edge)
        self.detect_edge_button.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            image = cv2.imread(file_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image = ImageTk.PhotoImage(image)
            self.image_label.config(image=image)
            self.image_label.image = image

            self.loaded_image = cv2.imread(file_path)

    def detect_edge(self):
        if hasattr(self, 'loaded_image'):
            gray_image = cv2.cvtColor(self.loaded_image, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray_image, 50, 150)
            cv2.imshow("Ảnh đã tách biên", edges)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            tk.messagebox.showinfo("Thông báo", "Hãy chọn ảnh trước khi thực hiện tách biên.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEdgeDetectionApp(root)
    root.mainloop()

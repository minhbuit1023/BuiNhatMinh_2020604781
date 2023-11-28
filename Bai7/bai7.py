import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class ImageFilterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Ứng dụng Lọc làm mịn ảnh")

        self.image_label = tk.Label(self.master)
        self.image_label.pack(padx=10, pady=10)

        self.load_button = tk.Button(self.master, text="Chọn ảnh", command=self.load_image)
        self.load_button.pack(pady=10)

        self.smooth_button = tk.Button(self.master, text="Lọc làm mịn", command=self.smooth_image)
        self.smooth_button.pack(pady=10)

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

    def smooth_image(self):
        if hasattr(self, 'loaded_image'):
            smoothed_image = cv2.GaussianBlur(self.loaded_image, (15, 15), 0)
            cv2.imshow("Lọc làm mịn ảnh", smoothed_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            tk.messagebox.showinfo("Thông báo", "Hãy chọn ảnh trước khi thực hiện lọc làm mịn.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageFilterApp(root)
    root.mainloop()

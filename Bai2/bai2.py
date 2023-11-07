import tkinter as tk
from sympy import symbols, diff, integrate, solve, sympify
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def tinh_dao_ham():
    try:
        bieu_thuc = sympify(nhap_bieu_thuc.get())
        bien = bien_dao_ham.get()
        x = symbols(bien)
        dao_ham = diff(bieu_thuc, x)
        ket_qua.set(f"Đạo hàm của {bieu_thuc} theo {bien} là {dao_ham}")
    except Exception as e:
        ket_qua.set(f"Lỗi: {e}")

def tinh_nguyen_ham():
    try:
        bieu_thuc = sympify(nhap_bieu_thuc.get())
        bien = bien_nguyen_ham.get()
        x = symbols(bien)
        nguyen_ham = integrate(bieu_thuc, x)
        ket_qua.set(f"Nguyên hàm của {bieu_thuc} theo {bien} là {nguyen_ham}")
    except Exception as e:
        ket_qua.set(f"Lỗi: {e}")

def ve_do_thi():
    try:
        bieu_thuc = sympify(nhap_bieu_thuc.get())
        bien = bien_do_thi.get()
        x = symbols(bien)
        a = float(gia_tri_a.get())
        b = float(gia_tri_b.get())
        x_values = np.linspace(a, b, 400)
        y_values = [bieu_thuc.subs(x, val) for val in x_values]
        plt.plot(x_values, y_values)
        plt.xlabel(bien)
        plt.ylabel("Giá trị của biểu thức")
        plt.title("Đồ thị của hàm số")
        canvas = FigureCanvasTkAgg(plt.gcf(), master=frame)
        canvas.get_tk_widget().pack()

    except Exception as e:
        ket_qua.set(f"Lỗi: {e}")

app = tk.Tk()
app.title("Ứng dụng hỗ trợ môn giải tích")

nhap_bieu_thuc = tk.Entry(app, width=40)
bien_dao_ham = tk.Entry(app, width=5)
bien_nguyen_ham = tk.Entry(app, width=5)
bien_do_thi = tk.Entry(app, width=5)
gia_tri_a = tk.Entry(app, width=5)
gia_tri_b = tk.Entry(app, width=5)
ket_qua = tk.StringVar()
ket_qua.set("Kết quả sẽ được hiển thị ở đây")

frame = tk.Frame(app)
frame.pack()

tk.Label(app, text="Nhập biểu thức hàm số:").pack()
nhap_bieu_thuc.pack()

tk.Label(app, text="Nhập biến (đạo hàm):").pack()
bien_dao_ham.pack()

tk.Label(app, text="Nhập biến (nguyên hàm):").pack()
bien_nguyen_ham.pack()

tk.Label(app, text="Nhập biến (đồ thị):").pack()
bien_do_thi.pack()

tk.Label(app, text="Nhập giá trị a:").pack()
gia_tri_a.pack()

tk.Label(app, text="Nhập giá trị b:").pack()
gia_tri_b.pack()

tk.Button(app, text="Tính đạo hàm", command=tinh_dao_ham).pack()
tk.Button(app, text="Tính nguyên hàm", command=tinh_nguyen_ham).pack()
tk.Button(app, text="Vẽ đồ thị", command=ve_do_thi).pack()

tk.Label(app, textvariable=ket_qua).pack()

app.mainloop()

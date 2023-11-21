import tkinter as tk
from math import sin, pi

def calculate_triangle_window(m_value):
    wt_values = []
    for s in range(m_value):
        if 0 <= s <= (m_value - 1) / 2:
            wt_s_m = 2 * s / (m_value - 1)
        elif (m_value - 1) / 2 <= s <= (m_value - 1):
            wt_s_m = 2 - (2 * s / (m_value - 1))
        else:
            wt_s_m = 0
        wt_values.append(wt_s_m)
    return wt_values

def calculate_hd(wt_values, wc_value, m_value):
    h_values = [
        ((wc_value / pi) * (sin(wc_value * (n - (m_value - 1) / 2)) / (wc_value * (n - (m_value - 1) / 2))))
        if wc_value != 0 and wc_value * (n - (m_value - 1) / 2) != 0
        else 0
        for n in range(m_value)
    ]
    hd_values = [wt * h for wt, h in zip(wt_values, h_values)]
    return hd_values

def find_fir_filter():
    # Lấy giá trị từ ô nhập
    m_value = int(entry_m.get())
    k_value = float(entry_k.get())

    # Tính giá trị của Wc
    wc_value = k_value * pi

    # Tính giá trị của WT(s, m)
    wt_values = calculate_triangle_window(m_value)

    # Tính giá trị của hd(n)
    hd_values = calculate_hd(wt_values, wc_value, m_value)

    # Hiển thị kết quả
    print(hd_values)

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Phần Mềm Hỗ Trợ Tìm Bộ Lọc FIR")

# Tạo các thành phần trong giao diện
label = tk.Label(window, text="Chào mừng bạn đến với Phần Mềm Hỗ Trợ Tìm Bộ Lọc FIR")
label_m = tk.Label(window, text="Nhập giá trị của m (số nguyên lẻ):")
entry_m = tk.Entry(window)
label_k = tk.Label(window, text="Nhập giá trị của k:")
entry_k = tk.Entry(window)
button = tk.Button(window, text="Tìm Bộ Lọc FIR", command=find_fir_filter)

# Đặt các thành phần lên cửa sổ chính
label.pack(padx=10, pady=10)
label_m.pack(pady=5)
entry_m.pack(pady=5)
label_k.pack(pady=5)
entry_k.pack(pady=5)
button.pack(pady=10)

# Chạy vòng lặp chính
window.mainloop()

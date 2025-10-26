import os
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont

# === 加水印函式 ===
def add_watermark_to_images(folder, font_path, text):
    if not folder or not os.path.exists(folder):
        messagebox.showerror("錯誤", "請選擇有效的圖片資料夾")
        return

    output_folder = os.path.join(folder, "output")
    os.makedirs(output_folder, exist_ok=True)

    # 掃描資料夾內圖片
    images = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if not images:
        messagebox.showwarning("提示", "該資料夾中沒有圖片！")
        return

    for img_name in images:
        img_path = os.path.join(folder, img_name)
        img = Image.open(img_path).convert("RGBA")

        # 建立文字圖層
        txt_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt_layer)

        # 設定字體
        try:
            font = ImageFont.truetype(font_path, int(img.width / 20))  # 自動字體大小
        except Exception:
            messagebox.showerror("錯誤", "字體檔載入失敗！請重新選擇字體。")
            return

        text_w, text_h = draw.textsize(text, font=font)
        pos = (img.width - text_w - 20, img.height - text_h - 20)

        # 畫上水印
        draw.text(pos, text, fill=(255, 255, 255, 128), font=font)  # 半透明白色文字

        watermarked = Image.alpha_composite(img, txt_layer)
        watermarked = watermarked.convert("RGB")  # 去除透明通道以存JPG

        out_path = os.path.join(output_folder, img_name)
        watermarked.save(out_path)

    messagebox.showinfo("完成", f"已生成水印圖片！輸出於：\n{output_folder}")

# === 瀏覽資料夾 ===
def choose_folder():
    folder = filedialog.askdirectory(title="選擇圖片資料夾")
    folder_entry.delete(0, END)
    folder_entry.insert(0, folder)

# === 瀏覽字體檔 ===
def choose_font():
    font_file = filedialog.askopenfilename(
        title="選擇字體檔案 (.ttf)",
        filetypes=[("TrueType 字體", "*.ttf")]
    )
    font_entry.delete(0, END)
    font_entry.insert(0, font_file)

# === 點擊生成 ===
def generate():
    folder = folder_entry.get().strip()
    font_path = font_entry.get().strip()
    text = text_entry.get().strip()

    if not folder or not font_path or not text:
        messagebox.showwarning("提示", "請先選擇資料夾、字體並輸入水印內容！")
        return

    add_watermark_to_images(folder, font_path, text)

# === Tkinter 主介面 ===
root = Tk()
root.title("批量水印生成工具")
root.geometry("480x300")
root.resizable(False, False)

Label(root, text="圖片資料夾：").grid(row=0, column=0, padx=10, pady=10, sticky="e")
folder_entry = Entry(root, width=40)
folder_entry.grid(row=0, column=1)
Button(root, text="選擇...", command=choose_folder).grid(row=0, column=2, padx=5)

Label(root, text="字體檔案：").grid(row=1, column=0, padx=10, pady=10, sticky="e")
font_entry = Entry(root, width=40)
font_entry.grid(row=1, column=1)
Button(root, text="選擇...", command=choose_font).grid(row=1, column=2, padx=5)

Label(root, text="水印內容：").grid(row=2, column=0, padx=10, pady=10, sticky="e")
text_entry = Entry(root, width=40)
text_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=10)

Button(root, text="生成水印", width=20, bg="#4CAF50", fg="white", command=generate).grid(row=3, column=1, pady=20)

root.mainloop()

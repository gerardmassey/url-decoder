import urllib.parse
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk

def decode_url():
    url = url_entry.get()
    decoded_url = urllib.parse.unquote(url)
    result_label.config(text=decoded_url)
    
    # Resize the window to fit the decoded URL
    root.geometry(f"{root.winfo_reqwidth()}x{result_label.winfo_reqheight()+120}")

def copy_to_clipboard():
    result = result_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(result)
    messagebox.showinfo("Info", "The decoded URL has been copied to the clipboard")

# Create the root window
root = tk.Tk()
root.title("URL Decoder")

# Center the window on the screen
window_width = 500
window_height = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create the widgets
url_label = tk.Label(root, text="Enter URL to decode:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

decode_button = tk.Button(root, text="Decode", command=decode_url)
decode_button.pack()

result_label = tk.Label(root, text="", wraplength=600)
result_label.pack()

copy_button = ttk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.pack()

# Set initial window size
root.geometry("500x150")

root.mainloop()

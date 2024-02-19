import tkinter as tk
from tkinter import messagebox
import subprocess

def run_nmap(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error executing command: {e}")

def button_click(scan_type):
    target = target_entry.get().strip()

    if not target:
        messagebox.showerror("Error", "Please enter the IP address or target name", font=("Arial", 15, "bold"))
        return

    if scan_type == "SYN":
        command = f"nmap {target} -sS"
    elif scan_type == "TCP":
        command = f"nmap {target} -sT"
    elif scan_type == "UDP":
        command = f"nmap {target} -sU"
    elif scan_type == "ACK":
        command = f"nmap {target} -sA"
    elif scan_type == "HOST":
        command = f"nmap {target} -sn"
    elif scan_type == "PORT":
        command = f"nmap {target} -p 1-1000"
    elif scan_type == "OS":
        command = f"nmap {target} -O"
    elif scan_type == "Version":
        command = f"nmap {target} -sV"
    elif scan_type == "WOLF SCRIPT":
        command = f"nmap {target} -sC"
    elif scan_type == "WINDOWS":
        command = f"nmap {target} -sW"
    elif scan_type == "HELP":
        command = f"nmap {target} -h"
    else:
        messagebox.showerror("Error", "Invalid scan type. Please enter -sS, -sT, -sU, -sA , -sn . -p -1000 , OS , Version")
        return

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Running command: {command}\n")
    try:
        completed_process = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        result_text.insert(tk.END, completed_process.stdout)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error executing command: {e}")
        result_text.insert(tk.END, f"Error executing command: {e}\n")

root = tk.Tk()
root.title("YASHWOLF V 1.0.1...!")

target_label = tk.Label(root, text="Enter the IP address or target name:")
target_label.grid(row=0, column=0, columnspan=4)
target_entry = tk.Entry(root)
target_entry.grid(row=1, column=0, columnspan=4)

scan_types = ["SYN", "TCP", "UDP", "ACK", "HOST", "PORT", "OS", "Version", "WOLF SCRIPT", "WINDOWS", "HELP"]

for i, scan_type in enumerate(scan_types):
    button = tk.Button(root, text=scan_type, command=lambda st=scan_type: button_click(st), font=("Arial", 10, "bold"), bg="black", fg="white")
    button.grid(row=2 + i // 4, column=i % 4)

result_label = tk.Label(root, text="Scan Result:")
result_label.grid(row=3 + len(scan_types) // 4, column=0, columnspan=4, pady=5)
result_text = tk.Text(root, height=27, width=120, fg="green", bg="black")
result_text.grid(row=4 + len(scan_types) // 4, column=0, columnspan=4)

root.mainloop()

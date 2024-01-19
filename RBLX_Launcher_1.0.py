import subprocess
import tkinter as tk

def check_process_running():
    adb_command = 'adb shell "ps | grep com.roblox.client"'
    process = subprocess.Popen(adb_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    return 'com.roblox.client' in output.decode('utf-8')

def launch_roblox():
    game_id = server_entry.get()
    adb_command = f'adb shell am start -a android.intent.action.VIEW -d "roblox://placeId={game_id}"'
    subprocess.run(adb_command, shell=True)

def check_and_relaunch():
    if not check_process_running():
        status_label.config(text="Roblox Launched")
        launch_roblox()
    status_label.after(5000, check_and_relaunch)

def launch_button_click():
    status_label.config(text="Roblox Launched")
    launch_roblox()
    check_and_relaunch()

# Create the main window
window = tk.Tk()
window.title("Roblox Monitor")
window.geometry("400x200")  # Set window size

# Create UI components
status_label = tk.Label(window, text="RBLX LAUNCHER")
status_label.config(font=("Arial", 14))  # Increase font size
status_label.pack()

server_label = tk.Label(window, text="Enter Game ID:")
server_label.config(font=("Arial", 12))  # Increase font size
server_label.pack()

server_entry = tk.Entry(window)
server_entry.config(font=("Arial", 12))  # Increase font size
server_entry.pack()

launch_button = tk.Button(window, text="Launch", command=launch_button_click)
launch_button.config(font=("Arial", 12))  # Increase font size
launch_button.pack()

# Start the main event loop
window.mainloop()

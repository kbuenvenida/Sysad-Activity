import tkinter as tk
from tkinter import messagebox

def save_user_details():
    username = entry_username.get()
    primary_group = entry_primary_group.get()
    secondary_group = entry_secondary_group.get()
    comment = entry_comment.get()
    home_directory = entry_home_directory.get()
    password_expiration = entry_password_expiration.get()

    # Create the file path for saving user details
    file_path = r"C:\Users\wafsm\OneDrive\Documents\user_details.txt"

    # Save the user details to a file
    with open(file_path, "a") as file:
        file.write("Username: {}\n".format(username))
        file.write("Primary Group: {}\n".format(primary_group))
        file.write("Secondary Group: {}\n".format(secondary_group))
        file.write("Comment: {}\n".format(comment))
        file.write("Home Directory: {}\n".format(home_directory))
        file.write("Password Expiration: {}\n".format(password_expiration))
        file.write("\n")

    # Clear the entry fields after saving
    entry_username.delete(0, tk.END)
    entry_primary_group.delete(0, tk.END)
    entry_secondary_group.delete(0, tk.END)
    entry_comment.delete(0, tk.END)
    entry_home_directory.delete(0, tk.END)
    entry_password_expiration.delete(0, tk.END)

    # Display a message box to indicate successful saving
    messagebox.showinfo("User Details", "User details saved successfully!")

def delete_user_details():
    username = entry_username.get()

    # Create the file path for deleting user details
    file_path = r"C:\Users\wafsm\OneDrive\Documents\user_details.txt"

    # Read the contents of the file
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Remove the user details from the lines list
    new_lines = []
    found_user = False
    for line in lines:
        if line.strip() == "Username: {}".format(username):
            found_user = True
            continue
        if found_user:
            if line.strip() == "":
                found_user = False
            continue
        new_lines.append(line)

    # Write the modified lines back to the file
    with open(file_path, "w") as file:
        file.writelines(new_lines)

    # Clear the entry field after deleting
    entry_username.delete(0, tk.END)

    # Display a message box to indicate successful deleting
    messagebox.showinfo("User Details", "User details deleted successfully!")

# Create the main window
window = tk.Tk()
window.title("User Details")
window.geometry("360x360")

# Create labels and entry fields for each user detail
label_username = tk.Label(window, text="Username:")
label_username.pack()
entry_username = tk.Entry(window)
entry_username.pack()

label_primary_group = tk.Label(window, text="Primary Group:")
label_primary_group.pack()
entry_primary_group = tk.Entry(window)
entry_primary_group.pack()

label_secondary_group = tk.Label(window, text="Secondary Group:")
label_secondary_group.pack()
entry_secondary_group = tk.Entry(window)
entry_secondary_group.pack()

label_comment = tk.Label(window, text="Comment:")
label_comment.pack()
entry_comment = tk.Entry(window)
entry_comment.pack()

label_home_directory = tk.Label(window, text="Home Directory:")
label_home_directory.pack()
entry_home_directory = tk.Entry(window)
entry_home_directory.pack()

label_password_expiration = tk.Label(window, text="Password Expiration:")
label_password_expiration.pack()
entry_password_expiration = tk.Entry(window)
entry_password_expiration.pack()

# Create a button to save the user details
button_save = tk.Button(window, text="Save", command=save_user_details)
button_save.pack()

# Create a button to save the user details
button_delete = tk.Button(window, text="Delete", command=delete_user_details)
button_delete.pack()

# Run the main event loop
window.mainloop()
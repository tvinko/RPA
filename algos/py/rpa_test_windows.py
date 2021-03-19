from RPA.Desktop.Windows import Windows

win = Windows()

def open_notepad():
    win.open_from_search("notepad.exe", "Untitled - Notepad")
    elements = win.get_window_elements()
    result = win.get_element_rich_text('id:15')

    win.send_keys("Hello World!")

if __name__ == "__main__":
    open_notepad()
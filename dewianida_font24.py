import PySimpleGUI as sg
sg.theme("DarkGreen4") #penentuan tema
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("FTI UNISKA ", font=("Helvetica",24))],
                           [sg.Text("Fakultas Teknologi Informasi ", font=("Courier",18,"italic","bold","underline"))],
                           [sg.Text("Uniska MAB Banjarmasin", text_color="#FFCC00")]],
                           size=(430,200),
                           font=("Times", 18))
window()
window.close()
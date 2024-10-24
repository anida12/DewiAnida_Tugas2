import PySimpleGUI as sg
sg.theme("DarkGreen4") #penentuan tema
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("Teknologi Informasi ", size=(25,1), justification="center")],
                           [sg.Text("Teknologi Informasi ", size=(25,1), justification="left")],
                           [sg.Text("Teknologi Informasi ", size=(25,1), justification="right")],
                           [sg.Text(("Teknologi Informasi "+" ")* 2, size=(25,2), justification="center")],
                           
                           [sg.Text("Uniska MAB Banjarmasin ", text_color="#FFCC00")]],
                           size=(400,250),
                           font=("Times", 18))
window()
window.close()
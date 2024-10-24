import PySimpleGUI as sg
susunan=[[sg.Text("Uniska MAB",font=("Helvetica", 24))],
        [sg.Text("Banjarmasin",font=("Courier", 18) )]]
window = sg.Window(title="Elemen Text",
                        layout=susunan,
                        element_justification = "center",
                        size=(430,200))
window()
window.close()
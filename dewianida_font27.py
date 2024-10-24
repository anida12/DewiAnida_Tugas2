import PySimpleGUI as sg
susunan=[[sg.Push(),
        sg.Text("Uniska MAB",font=("Helvetica", 24)),
        sg.Push()],
        [sg.Push(),
         sg.Text("Banjarmasin", font=("Courier", 18)),
         sg.Push()],
         [sg.VPush()]
         ]
window = sg.Window(title="Elemen Text",
                        layout=susunan,
                        size=(430,200))
window()
window.close()
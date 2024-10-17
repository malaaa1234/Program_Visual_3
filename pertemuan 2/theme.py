import PySimpleGUI as sg
sg.theme("DarkGreen4")
window = sg.Window(title="Profile",
                    layout=[[sg.Text("NPM      : 2210010392")],
                            [sg.Text("Nama     : NURMALA SARI")],
                            [sg.Text("Kelas    : 5M Regular Banjarmasin")],
                            [sg.Text("Matkul   : Pemrograman Visual 3")]
                            ],
                            size=(400,200))
window()
window.close()
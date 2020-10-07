import PySimpleGUI as sg
import wolframalpha
import wikipedia
import pyttsx3
engine = pyttsx3.init()


client = wolframalpha.Client("6PUV4Y-U49PRP5K3R")

sg.theme('DarkAmber')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Enter a Command'), sg.InputText()], [sg.Button('Ok'), sg.Button('Cancel')] ]
window = sg.Window('PyDa', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    res = client.query(values[0]) 
    try: 
        wolfram_res = next(res.results).text
    except StopIteration:
        wolfram_res = values[0]
    wiki_res = wikipedia.summary(values[0], sentences=2)
    combined_results = "Wolfram Result: " + wolfram_res, "\nWikipedia Result: " + wiki_res
    sg.PopupNonBlocking("Wolfram Result: " + wolfram_res, "\nWikipedia Result: " + wiki_res)
    strung_results = str(combined_results)
    engine.say(strung_results)
    engine.runAndWait()
    print(values[0])

window.close()

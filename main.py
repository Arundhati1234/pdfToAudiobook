import pyttsx3
import PyPDF2
book = open('HP_book.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"
   
speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    voices = speaker.getProperty('voices')
    for voice in voices:
        print(voice)
    
    speaker.say(text)
    speaker.setProperty('voice', voice_id)
    speaker.setProperty('rate', 150)
    speaker.runAndWait()

import pyttsx3
import PyPDF2

pdfreader = PyPDF2.PdfReader(open('story.pdf', 'rb'))
speaker = pyttsx3.init()

clean_text = ""
print(f"pages {pdfreader.pages}")
for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    print(text)
    clean_text += text.strip().replace('/n', '')

print(clean_text)

speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()

speaker.stop()

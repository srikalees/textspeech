from gtts import gTTS
import os

def text_to_speech(text, lang='en'):
    # Initialize gTTS (Google Text-to-Speech) with the text to be converted
    tts = gTTS(text=text, lang=lang, slow=False)  # 'slow=False' means the speaking speed is normal

    # Save the audio to a file
    tts.save("output.mp3")

    # Play the converted audio
    os.system("start output.mp3")  # Opens the file with the default audio player on Windows

if __name__ == "__main__":
    # Example usage:
    input_text = "Hello sri , how are you today?"
    text_to_speech(input_text)

import streamlit as st
import whisper

# assume you have an uploaded file named `uploaded_file`

# read the audio data from the uploaded file into a NumPy array


# App Title Name
st.title("Speech to Text")

# uploading an audio file
audio_file = st.file_uploader("Upload Audio", type=["wav","mp3","m4a"])
# audio_file = audio_recorder()
# if audio_file:
#     st.audio(audio_file, format="audio/wav")


model = whisper.load_model("base")
st.text("Whisper Model Loaded")

if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing Audio")
        transcription = model.transcribe(audio_file.name)
        st.sidebar.success("Transcription Complete")
        st.text(transcription["text"])
    else:
        st.sidebar.error("Please Upload an Audio File")

import streamlit as st
import matchering as mg
from datetime import datetime

# Define a basic text output function that will also output the current datetime
def my_print(text):
    print(f"{datetime.now()}: {text}")

# The information output will be marked with a prefix
def info(text):
    my_print(f"INFO: {text}")

# The warning output will be highlighted with exclamation marks on both sides
def warning(text):
    my_print("!" * 20)
    my_print(f"! WARNING: {text}")
    my_print("!" * 20)

# Set new handlers
mg.log(warning_handler=warning, info_handler=info, debug_handler=my_print)

# Function to process audio files
def process_audio(target, reference, results):
    mg.process(target=target, reference=reference, results=results)

# Streamlit UI
def main():
    st.title("Audio Matching App")
    st.write("This app matches target audio to mastered audio and produces a new mastered audio file as output.")

    # File uploader for target audio
    target_file = st.file_uploader("Upload target audio (mp3 format)", type=["mp3"])

    # File uploader for reference audio
    reference_file = st.file_uploader("Upload reference audio (mp3 format)", type=["mp3"])

    # File uploader for results
    result_files = []
    for i in range(2):  # Assuming only 2 result files as in the original code
        result_files.append(st.file_uploader(f"Upload result audio {i+1} (wav format)", type=["wav"]))

    if st.button("Process Audio"):
        if target_file and reference_file and all(result_files):
            # Process audio files
            process_audio(target=target_file.name, reference=reference_file.name, results=[file.name for file in result_files])
            st.success("Audio processing completed successfully.")
        else:
            st.error("Please upload all required audio files.")

if __name__ == "__main__":
    main()
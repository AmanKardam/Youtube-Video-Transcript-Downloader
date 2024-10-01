from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st

def fetch_youtube_transcript(video_link):
    try:
        video_id = video_link.split("=")[1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        print(transcript)

        transcript_text = ''

        for i in transcript:
            print(i)
            print(i["text"])
            transcript_text +=' '+ i["text"]

        print(transcript_text)

        return transcript_text
    

    except Exception as e:
        raise e 
    

st.title("Youtube Video Transcript Downloader")
link = st.text_input("Enter Youtube Link:")

if link:
    video_id = link.split("=")[1]
    print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    
if st.button("Get Transcript"):
    transcript=fetch_youtube_transcript(link)
    
    with open("./Transcript.txt",'w') as my_file:
        my_file.write(transcript)

    st.success("Transcript.txt saved.")


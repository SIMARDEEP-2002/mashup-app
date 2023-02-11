import streamlit as st
import pandas as pd
import os
import mashupcode
from SendEmail import send_email
import shutil
           
           
           
# if (os.path.exists('audios')):
#      shutil.rmtree('audios')
# if (os.path.exists('videos')):
#      shutil.rmtree('videos')
             
# if (os.path.exists('media')):
#      shutil.rmtree('media')
    
             
flag=0
# flag2=1
st.title('Mashup Web App')

form = st.form("my_form", clear_on_submit=False)
with form:

    singer = st.text_input(
        "Singer Name",
        key="singer",
    )
    # singer should be required

    videos = st.text_input(
        "No. of Videos (Please enter more than 10 videos)",
        key="videos",
    )
    # videos should be required and should be greater than 10

    if len(videos) > 0:
       if int(videos)<=10:
           st.error("enter more than 10 videos")
           flag=1
    

    duration = st.text_input(
        "Enter Duration of each video in seconds (Please enter more than or equal to 20 seconds)",
        key="duration",
    )
    if len(duration) > 0:
       if int(duration)<20:
            st.error("enter more than or equal to 20 seconds")
            flag=1

    Email = st.text_input(
        "Enter Email to send zip file",
        key="email",
        
    )
    #mail check
    if len(Email) > 0:
        if '@' in Email:
            pass
        else:
            st.error("enter valid email")
            flag=1

    submitted=st.form_submit_button("Submit")

    if singer and videos and duration and Email and flag==0:
        
        
        if submitted and flag==0:
            st.write("Submitted Successfully.")
            st.write("Wait till email sent message before closing the app!")
            if not (os.path.exists('audios')):
                os.mkdir('audios')

            if not (os.path.exists('videos')):
                os.mkdir('videos')

            if not (os.path.exists('media')):
                os.mkdir('media')
            mashupcode.main(singer,int(videos),int(duration))
            SENDER_ADDRESS=st.secrets["aq"]
            # encrypted password
            SENDER_PASSWORD=st.secrets["qib"]
            SMTP_SERVER_ADDRESS='smtp.gmail.com'

            send_email(SENDER_ADDRESS, SENDER_PASSWORD, Email, SMTP_SERVER_ADDRESS, 587, 'Here is your zip file', 'Mashup', 'media/mashup.zip')
            
            st.write("Email sent successfully.")
            

#remove all files from audios, videos and media folder
            import shutil
            shutil.rmtree('audios')
            shutil.rmtree('videos')
            shutil.rmtree('media')
            # flag2=0
            
    else:
        st.write("All fields are required.")
       
        
    # if flag2==1:
    #     import shutil
    #     shutil.rmtree('audios')
    #     shutil.rmtree('videos')
    #     shutil.rmtree('media')
   

    # submitted = st.form_submit_button("Submit")

#send email of zip file

# SENDER_ADDRESS='simarprojects26@gmail.com'
# SENDER_PASSWORD='rewlmswcjnqnfxia'
# SMTP_SERVER_ADDRESS='smtp.gmail.com'

# send_email(SENDER_ADDRESS, SENDER_PASSWORD, Email, SMTP_SERVER_ADDRESS, 587, 'Here is your zip file', 'Mashup', 'media/mashup.zip')

# #remove all files from audios, videos and media folder
# import shutil
# shutil.rmtree('audios')
# shutil.rmtree('videos')
# shutil.rmtree('media')


import pandas as pd
import numpy as np
import concurrent.futures

from youtubesearchpython import *
import json
import math
from youtubesearchpython import *
import os
from pytube import YouTube
import moviepy.editor as mp
from pydub import AudioSegment
import sys

import logging
import threading
import time
# create audios 

class ParameterError(Exception):
    pass

class videoinputerror(Exception):
    pass




def download(l,j):
    yt = YouTube(l)
    yt = yt.streams.get_by_itag(18)
    yt.download('videos/',filename='song'+f'{j}'+'.mp4')


import concurrent.futures
import os
import moviepy.editor as mp

def convert(index):
    video_file = 'videos/song{}.mp4'.format(index)
    audio_file = 'audios/song{}.mp3'.format(index)
    
    clip = mp.VideoFileClip(video_file)
    audio = clip.audio
    audio.write_audiofile(audio_file)

def convert_thread(n):
    with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        futures = [executor.submit(convert, index) for index in range(n)]
        
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
            except Exception as e:
                print(e)



def cut_merge(z,m,output):
        file='audios/song'+str(m)+'.mp3'
        sound = AudioSegment.from_mp3(file)
    #Selecting Portion we want to cut
        StrtMin = 0
        StrtSec = 0
        EndMin = 0
        EndSec = min(z,sound.duration_seconds)
    # Time to milliseconds conversion
        StrtTime = StrtMin*60*1000+StrtSec*1000
        EndTime = EndMin*60*1000+EndSec*1000
    # Opening file and extracting portion of it
        extract = sound[StrtTime:EndTime]
        output.append(extract)  


     
     

def target(singer_name,n,dur):
    
    z=dur
    s=math.ceil(n/19)
    string=singer_name


    videosSearch = CustomSearch(string+' songs', VideoDurationFilter.short)

    list=[]
    while len(list)<n:
        # print(videosSearch.result()['result'][i]['link'])
        for i in range(19):
            # do not append live youtube videos and append the required number of links that are n
            if len(list) <= n:
                if videosSearch.result()['result'][i]['duration'] != 'Live':
                    list.append(videosSearch.result()['result'][i]['link'])
            if len(list)== n:
                break
        videosSearch.next()


            #     if videosSearch.result()['result'][i]['duration'] != 'Live':
            #        list.append(videosSearch.result()['result'][i]['link'])
            # videosSearch.next()



    # print(list)
    l1 = []
    
    # taking an counter
    count = 0
    
    # traversing the array
    for item in list:
        if item not in l1:
            count += 1
            l1.append(item)
    

    # print("No of unique items are:", count)
    # print(len(list))
    data = [(element,index) for index,element in enumerate(list[:n])]
    with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        executor.map(lambda x: download(*x), data)
 
    # from pytube import get
    # for i in range(n):
    #     download(list[i],i)
    convert_thread(n)
        

    # data1 = [(index) for index in range(n)]
    # with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor1:
    #     executor1.map(lambda x: convert(*x), data1)
 
    # for j in range(n):
    #      convert(j)
        
    #importing file from location by giving its path
    merged=AudioSegment.empty()
    output=[]
    data2 = [(z, index, output) for index in range(n)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor2:
        executor2.map(lambda x: cut_merge(*x), data2)

    # for i in range(n):
    #      cut_merge(z,i,output)
    for i in output:
         merged=merged+i
    #exporting file to folder named media
    merged.export('media/mashup.mp3', format='mp3')
    #zip file and store in media folder
    import zipfile
    zipObj = zipfile.ZipFile('media/mashup.zip', 'w')
    zipObj.write('media/mashup.mp3')
    zipObj.close()


    


def main(singer_name,n,dur):
      try:
        
        # if(n<10):
        #     raise videoinputerror
       

          
        target(singer_name,n,dur)
      except ParameterError:
          print('enter correct number of parameters')
      except videoinputerror:
          print('enter number of videos equal to or greater then 10')







          





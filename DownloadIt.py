import json
import os, pyautogui

#使用前须知：
#1. pyautogui非必须，只是提供一个输入框，没有的话就把comment里的替换出来，效果相同(大概)
#2. 该系统基于youtube-dl提供command line download, 因此必须安装youtube-dl并设为path。
#youtube-dl的网站：https://www.youtube-dl.org/ 
#3. 有很多小限制，但是我也没写很久，不要在意（

#用法：先打开要下载的avenue视频，点击F12打开网页控制，找到Network并打开
#播放视频，在name一栏找到"seg-2-v1-a1.ts"这样的title,打开后看到
#Request URL: https://cfvod.kaltura.com/hls/p/2152421/sp/215242100/serveFlavor/entryId/1_8652hotq/v/1/ev/5/flavorId/1_vo7fjzv9/name/a.mp4/seg-2-v1-a1.ts
#将http ~ a.mp4/复制并填入takingSource, takingRange为最后一个视频的编号，可以溢出，但短了的话视频会不全，长了的话会浪费时间
#命名，他会下载到D盘，可以下面找地方改location
'''
takingSource = pyautogui.prompt("sourceLocation")
takingRange = int(pyautogui.prompt("length"))
getAName = pyautogui.prompt("name")

'''
"""
takingSource = input("sourceLocation")
takingRange = int(input("length"))
getAName = input("name")
"""

booking = open("c:\\Essential Components\\AveuneDownload\\downloadBook.json","r")
jsonInstructions = booking.read(99999999)
instructions = json.loads(jsonInstructions)
booking.close()
for i in range(len(instructions) - 1):
    takingSource = instructions[i][0][0:instructions[i][0].find("a.mp4/")] + "a.mp4/"
    takingRange = int(instructions[i][1])
    getAName = instructions[i][2]
    if takingSource == "SourceLocatioa.mp4/":
        continue
#改这个来改下载地址
    path = 'D:\YoutubeVideos\AvenueDownload\A' + getAName
    print(takingSource)
    print(takingRange)
    for i in range(1,takingRange + 1):
        if i < 10:
            num = "00" + str(i)
        elif i < 100:
            num = "0" + str(i)
        else:
            num = str(i)
        #改这个来改下载地址
        presets = 'youtube-dl -o"D:\YoutubeVideos\AvenueDownload\A' + getAName + '\A' + num + '.%(ext)s" '
        name = "seg-" + str(i) + "-v1-a1.ts"
        setting = presets + takingSource +name
        print(setting)
        os.system(setting)
#如果是C盘，把D改成C
    os.system("D:&cd " + path + "&copy /b *.ts " + getAName + ".mp4")
    os.system("D:&cd " + path + "&erase *.ts")
    
os.startfile('D:\YoutubeVideos\AvenueDownload')
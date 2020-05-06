import os,shutil
audio_ex=('.mp3','.wav','.flac','.m4a')
video_ex=('.mp4','.mkv','.MKV','.flv','.mpeg')
document_ex=('.pdf','.ppt','.xls','.txt')
all_ex=('.mp3','.wav','.flac','.m4a','.mp4','.mkv','.MKV','.flv','.mpeg','.pdf','.ppt','.xls','.txt')
path=input("Enter Path Where You Want to Find")
def file_finder(file_path,file_extension):
    files=[]
    for file in os.listdir(file_path):
        for extension in file_extension:
            if file.endswith(extension):
                os.mkdir('G:\Study\Mix Daa\Videos1')
                files.append(file)
                shutil.move('files','G:\Study\Mix Daa\Videos1')
    return files
print(file_finder(path,video_ex))


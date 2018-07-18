# to convert .au files to .wav files

genres = 0
genre_names = ['blues','classical','country','disco','hiphop','jazz','metal','pop','reggae','rock']

cur_time = time.time()
while genres<10:
    folder_name = genre_names[genres]
    songs = os.listdir('data/' + folder_name)
    print('processing folder: ', folder_name)
    song_number = 0
    while song_number<100:
        filename = songs[song_number]
        path = 'data/'+folder_name+'/'+filename
        song = AudioSegment.from_file(path,'au')
        path_export = 'data_wav/'+folder_name+'/'+str(song_number)+'.wav'
        song.export(path_export,format='wav')
        song_number += 1
    genres +=1
final_time = time.time()
time_taken = final_time - cur_time
print('time taken : ', time_taken/60)

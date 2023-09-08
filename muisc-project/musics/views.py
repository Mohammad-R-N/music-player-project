from django.shortcuts import render

app_name="musics"
def playlist_detail(request):
    return render(request,'musics/allplaylists/playlist-detail.html')

app_name="musics"
def song_detail(request):
    return render(request,'musics/songdetail/songdetail.html')
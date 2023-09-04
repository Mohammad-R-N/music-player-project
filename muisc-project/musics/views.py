from django.shortcuts import render

def playlist_detail(request):
    return render(request,'musics/allplaylists/playlist-detail.html')

def song_detail(request):
    return render(request,'musics/songdetail/songdetail.html')
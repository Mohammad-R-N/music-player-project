from django.shortcuts import render

def playlist_detail(request):
    return render(request,'musics/allplaylists/playlist-detail.html')
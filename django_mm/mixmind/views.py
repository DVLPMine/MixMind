from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import UserEmotion, MusicInfo, MusicEmotion
import numpy as np
from .serializers import MusicInfoSerializer
from .serializers import GenreSerializer
from .serializers import TitleSerializer


class MusicRecommendViewSet(viewsets.ViewSet):
    def create(self, request):
        # serializer = MusicRecommendSerializer(data=request.data)
        # serializer.is_valid() # raise_exception=True
        emotion_values = request.data.get('emotions')
        
        user_emotion = UserEmotion.objects.create(
            love=emotion_values[0],
            joy=emotion_values[2],
            passion=emotion_values[4],
            happiness=emotion_values[6],
            sadness=emotion_values[1],
            anger=emotion_values[3],
            loneliness=emotion_values[5],
            longing=emotion_values[7],
            fear=emotion_values[9],
            surprise=emotion_values[8]
        )

        music_emotions = MusicEmotion.objects.all()
        music_emotions_similarity = []
        user_emotion_values = np.array([
            user_emotion.love,
            user_emotion.joy,
            user_emotion.passion,
            user_emotion.happiness,
            user_emotion.sadness,
            user_emotion.anger,
            user_emotion.loneliness,
            user_emotion.longing,
            user_emotion.fear,
            user_emotion.surprise
        ])
        for music_emotion in music_emotions:
            music_emotion_values = np.array([
                music_emotion.love,
                music_emotion.joy,
                music_emotion.passion,
                music_emotion.happiness,
                music_emotion.sadness,
                music_emotion.anger,
                music_emotion.loneliness,
                music_emotion.longing,
                music_emotion.fear,
                music_emotion.surprise
            ])
            cosine_similarity = np.dot(user_emotion_values, music_emotion_values) / (
                    np.linalg.norm(user_emotion_values) * np.linalg.norm(music_emotion_values))
            music_emotions_similarity.append((music_emotion, cosine_similarity))
        music_emotions_similarity.sort(key=lambda x: x[1], reverse=True)
        music_info_list = []
        for i in range(min(len(music_emotions_similarity), 10)):
            music_emotion = music_emotions_similarity[i][0]
            music_info = MusicInfo.objects.filter(id=music_emotion.musicId_id).first()
            if music_info:
                music_info_list.append(music_info)
        serializer = MusicInfoSerializer(music_info_list, many=True)
        return Response(serializer.data)


class MusicPalyViewSet(viewsets.ViewSet):
    # 
    pass

class MusicListViewSet(viewsets.ViewSet):
    def list(self, request):
        musiclist_info = MusicInfo.objects.all()
        serializer = MusicInfoSerializer(musiclist_info, many=True)
        return Response(serializer.data)

class GenreListViewSet(viewsets.ViewSet):
    def list(self, request):
        genreList = MusicInfo.objects.filter(genre = '발라드')
        serializer = MusicInfoSerializer(genreList, many=True)
        return Response(serializer.data)

class GenreSelectViewSet(viewsets.ViewSet):
    def list(self, request):
        genreSelect = MusicInfo.objects.values('genre').distinct()
        serializer = GenreSerializer(genreSelect, many=True)
        return Response(serializer.data)


# class GenreSelectInfoViewSet(viewsets.ViewSet): 
#     @action(detail=True, methods=['get'])
#     def genreSelectInfo(self, request, genre=None):
#         # genreSelectInfo = MusicInfo.objects.filter(genre = request.data.get(''))  appservice -> body : genre(value) -> genre: 1 
#         genre = request.query_params.get('genre')
#         genreSelectInfo = MusicInfo.objects.filter(genre = genre)
#         serializer = MusicInfoSerializer(genreSelectInfo, many=True)
#         return Response(serializer.data)

class GenreSelectInfoViewSet(viewsets.ViewSet): 
    @action(detail=False, methods=['get'])
    def search(self, request):
        # genreSelectInfo = MusicInfo.objects.filter(genre = request.data.get(''))  appservice -> body : genre(value) -> genre: 1 
        genre = request.query_params.get('genre')
        genreSelectInfo = MusicInfo.objects.filter(genre = genre)
        serializer = MusicInfoSerializer(genreSelectInfo, many=True)
        return Response(serializer.data)

class CollectTitleViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def search(self, request):
        # genreSelectInfo = MusicInfo.objects.filter(genre = request.data.get(''))  appservice -> body : genre(value) -> genre: 1 
        title = request.query_params.get('title')
        titleInfo = MusicInfo.objects.filter(title = title)
        serializer = MusicInfoSerializer(titleInfo, many=True)
        return Response(serializer.data)

    def list(self, request):
        # entireTitle = MusicInfo.objects.values('title').distinct()
        entireTitle = MusicInfo.objects.values('title')
        alltitles = []
        for titles in entireTitle:
            alltitles.append(titles['title'])
        # serializer = TitleSerializer(entireTitle, many=True)
        return Response(alltitles)
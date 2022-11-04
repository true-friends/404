from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LikeSerializer
from .models import Like
from Post.models import Post
from Follow.models import Follow
from rest_framework.response import Response
from rest_framework import viewsets, status


class PostLikeView(viewsets.ModelViewSet):
    serializer_class = LikeSerializer

    def get_queryset(self):
        liked_post_id = self.kwargs['post_id'] if 'post_id' in self.kwargs else None
        liked_comment_id = self.kwargs['comment_id'] if 'comment_id' in self.kwargs else None
        if liked_comment_id:
            return Like.objects.filter(comment_id=liked_comment_id)
        if liked_post_id:
            return Like.objects.filter(post_id=liked_post_id)
        return Like.objects.all()

    def create(self, request, *args, **kwargs):
        liked_post_id = self.kwargs['post_id'] if 'post_id' in self.kwargs else None
        serializer = self.serializer_class(data=request.data)

        post_obj = Post.objects.get(id=liked_post_id)
        if post_obj.visibility == 'FRIENDS':
            liker = request.user
            post_owner = post_obj.author
            follow_obj = Follow.objects.filter(follower=liker, followee=post_owner)
            if not post_owner == liker:
                if not follow_obj.exists():
                    return Response({"error": "must be a follower to like a private post"},
                                    status.HTTP_403_FORBIDDEN)
        
        if serializer.is_valid():
            existing_like = Like.objects.filter(post_id = liked_post_id).filter(author=request.user)
            if existing_like:
                existing_like.delete()
                return Response("Existing like deleted", status=status.HTTP_202_ACCEPTED)
            serializer.save(post_id=liked_post_id)
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = LikeSerializer(instance=instance)
        serializer.data['summary'] = instance.summary
        return Response(serializer.data)

class AuthorLikeView(viewsets.ModelViewSet):

    serializer_class = LikeSerializer

    def get_queryset(self):
        user_id = self.kwargs['author_id'] if 'author_id' in self.kwargs else None
        if user_id:
            return Like.objects.filter(author_id=user_id)
        return Like.objects.all()
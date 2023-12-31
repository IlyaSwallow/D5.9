from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    user_author = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rating = models.IntegerField(default=0)

    def update_rating(self):
        rating_posts_author = Post.objects.filter(author_post=self).aggregate(Sum('rating_news')).get('rating_news__sum') * 3
        rating_comments_author = Comment.objects.filter(user_comment=self.user_author).aggregate(Sum('rating_comment')).get('rating_comment__sum')
        rating_comments_posts = Comment.objects.filter(post_comment__author_post=self.id).aggregate(Sum('rating_comment')).get('rating_comment__sum')

        self.user_rating = rating_posts_author + rating_comments_author + rating_comments_posts
        print(self.user_rating)
        self.save()

tehnica = 'TH'
nauka = 'НА'
sport = 'СП'
politica = 'ПО'

TEMATIC = [
    (tehnica, 'ТЕХНИКА'),
    (nauka, 'НАУКА'),
    (sport, 'СПОРТ'),
    (politica, 'ПОЛИТИКА')
]


class Category(models.Model):
    tematic = models.CharField(max_length=2, choices=TEMATIC, unique=True)

post = 'PO'
news = 'NE'
POST = [
    (post, 'ПОСТ'),
    (news, 'НОВОСТЬ')
]


class Post(models.Model):
    author_post = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_news = models.CharField(max_length=2, choices=POST)
    date_in = models.DateTimeField(auto_now_add=True)
    Category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=50)
    text = models.TextField()
    rating_news = models.IntegerField(default=0)

    def like(self):
        self.rating_news += 1
        self.save()
    def dislike(self):
        self.rating_news -=1
        self.save()

    def preview(self):
        return self.text[0:124]+'...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    text_comment = models.TextField()
    data_time_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating_comment += 1
        self.save()
    def dislike(self):
        self.rating_comment -= 1
        self.save()




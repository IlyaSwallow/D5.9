'''python3 manage.py shell
from news.models import *

1. Создать двух пользователей с помощью метода User.objects.create_user:

user1 = User.objects.create_user('пользователь1')
user2 = User.objects.create_user('пользователь2')


2. Создать два объекта модели Author, связанные с пользователями:

author1 = Author.objects.create(user_author=user1)
author2 = Author.objects.create(user_author=user2)


3. Добавить 4 категории в модель Category:

cat1 = Category.objects.create(tematic='Экономика')
cat2 = Category.objects.create(tematic='Ботаника')
cat3 = Category.objects.create(tematic='Космос')
cat4 = Category.objects.create(tematic='Животные')



4. Добавить 2 статьи и 1 новость:

p1 = Post.objects.create(author_post=author1, post_news='PO', title='Статья1', text='текст статьи 1')
p2 = Post.objects.create(author_post=author1, post_news='NE', title='Новость1', text='текс новости 1')
p3 = Post.objects.create(author_post=author2, post_news='NE', title='Новость2', text='текс новости 2')
p4 = Post.objects.create(author_post=author2, post_news='PO', title='Статья2', text='текст статьи 2')


5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий):

p1.Category.add(cat1)
p2.Category.add(cat2)
p3.Category.add(cat3)
p4.Category.add(cat4)

6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий):

comm1 = Comment.objects.create(post_comment=p1, user_comment=user1,text_comment='комментарий 1')
comm2 = Comment.objects.create(post_comment=p1, user_comment=user1,text_comment='комментарий 2')
comm3 = Comment.objects.create(post_comment=p2, user_comment=user2,text_comment='комментарий 3')
comm4 = Comment.objects.create(post_comment=p2, user_comment=user2,text_comment='комментарий 4')
comm5 = Comment.objects.create(post_comment=p3, user_comment=user2,text_comment='комментарий 5')

7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов:


comm1.like()
comm1.dislike()
comm1.like()

comm2.like()
comm2.dislike()
comm2.dislike()

comm3.like()
comm3.like()
comm3.dislike()

comm4.like()
comm4.dislike()
comm4.like()

comm5.like()
comm5.dislike()
comm5.like()
comm5.like()

p1.like()
p1.dislike)

p2.like()
p2.dislike()
p2.like()

p3.like()
p3.dislike()
p3.like()
p3.like()

p4.like()
p4.dislike()
p4.dislike()
p4.dislike()

8. Обновить рейтинги пользователей:

author1.update_rating()
author2.update_rating()



9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта):

Author.objects.all().order_by('-user_rating').values('user_author__username', 'user_rating').first()

10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи,
основываясь на лайках/дислайках к этой статье:

Post.objects.order_by('-rating_news').values('date_in', 'author_post_id__user_author__username', 'rating_news', 'title').first()
Post.objects.order_by('-rating_news').first().preview()

11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье:

best_post = Post.objects.order_by('-rating_news').first()
best_post.comment_set.all().values('data_time_comment', 'user_comment__username', 'rating_comment', 'text_comment')

'''
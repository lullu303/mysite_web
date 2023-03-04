from django.db import models

# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

#댓글
class Comment(models.Model): 
    # board에 있는 글이 없어지면, 댓글도 같이 삭제
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    # 내용 => 두개의 테이블 구성만 해놓음
    content = models.TextField()
    create_date = models.DateTimeField()



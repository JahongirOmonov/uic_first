from django.db import models



# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="author/")
    description = models.TextField()
    content = models.TextField()

    facebook_url = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    instagram_url = models.CharField(max_length=255)
    pinterest_url = models.CharField(max_length=255)

    is_top = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


    


class Tag(BaseModel):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tag'

    def __str__(self):
        return self.title

class Post(BaseModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="post/")
    short_content = models.CharField(max_length=255)
    content = models.TextField()

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="posts"
    )
    tag = models.ManyToManyField(Tag, related_name="posts")

    published_date = models.DateField(auto_now_add=True)

    read_min = models.CharField(max_length=255)

    is_featured = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Post'

    def __str__(self):
        return self.title


class ContactUsRequest(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    text = models.TextField()

    class Meta:
        verbose_name = 'ContactUsRequest'
        verbose_name_plural = 'ContactUsRequest'

    def __str__(self):
        return self.name


class ContactUs(BaseModel):
    content = models.TextField()

    facebook_url = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    instagram_url = models.CharField(max_length=255)
    pinterest_url = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'ContactUs'
        verbose_name_plural = 'ContactUs'


class FAQ(BaseModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'


class Category(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="category/")
    count = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.title



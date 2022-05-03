
class Source:
    def __init__(self, id, name):
        self.id = id
        self.name = name





class Article:

    article_list = []

    def __init__(self,article_id, author, title, description, image, date):
        self.article_id = article_id
        self.author = author
        self.title = title
        self.description = description
        self.image = image
        self.date = date 

    def save_article(self):
        Article.article_list.append(self)

    @classmethod
    def clear_article(cls):
        Article.article_list.clear()

    @classmethod
    def get_articles(cls,id):
        response = []

        for article in cls.article_list:
            if article.article_id == id:
                response.append(article)

                return response



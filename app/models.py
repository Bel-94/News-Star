
class Source:
    def __init__(self, id, url, name):
        self.id = id
        self.name = name
        self.url = url





class Article:

    article_list = []

    def __init__(self,source_name, author, title, description,url, image, date):
        self.source_name = source_name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
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



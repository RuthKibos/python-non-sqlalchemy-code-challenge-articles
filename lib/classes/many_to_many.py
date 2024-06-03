class Article:
    all_articles = []  

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise TypeError("Title must be a string between 5 and 50 characters")
        
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all_articles.append(self)  

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise TypeError("Name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all_articles if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set(magazine.category for magazine in self.magazines()))

class Magazine:
    all_magazines = []  # Class variable to store all magazines

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise TypeError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise TypeError("Category must be a non-empty string")
        
        self._name = name
        self._category = category
        Magazine.all_magazines.append(self)  # Add the new magazine to the list of all magazines

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise TypeError("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise TypeError("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return [article for article in Article.all_articles if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        return list(set(author for author in authors if authors.count(author) > 2))
        
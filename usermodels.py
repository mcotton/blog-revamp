from google.appengine.ext import db

  
class Blog(db.Model):
  date = db.DateTimeProperty(auto_now_add=True)
  title = db.StringProperty()
  tag = db.StringProperty()
  author = db.StringProperty()
  content_img = db.TextProperty() # Image above preview post
  content = db.TextProperty()  # Generated HTML from showdown.js
  markdown = db.TextProperty() # Markdown kept allow editting later
  teaser = db.TextProperty() # Teaser that is shown on front page
  show_teaser = db.BooleanProperty() # Should we show the whole post or just the teaser?
  
class SideBar(db.Model):
  title = db.StringProperty()
  path = db.StringProperty()
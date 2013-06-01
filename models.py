from google.appengine.ext import db

class sources(db.Model):
    # for versioning
    date = db.DateTimeProperty(required=False)
    date_added = db.DateTimeProperty(required=False)
    last_updated = db.DateTimeProperty(required=False)
    recnum = db.IntegerProperty(required=False)
    feed_url = db.StringProperty(required=False)
    
    #Weekly Read Stuff
    source = db.StringProperty(required=False) # AKA Office
    title = db.StringProperty(required=False)
    link = db.StringProperty(required=True)
    tags = db.CategoryProperty(required=False)
    tags_list = db.ListProperty(str)
    description = db.TextProperty(required=False)
    relevance = db.TextProperty (required=False)
    
    #ESIL Stuff
    esil = db.ListProperty(str)
    
    #Alchemy Stuff
    content = db.TextProperty (required=False)
    alchemy_keywords = db.CategoryProperty(required=False)
    concepts = db.CategoryProperty(required=False) # Still need to generate this field
    keywords_list = db.ListProperty(str)
    concepts_list = db.ListProperty(str)
    
    #PAS Stuff
    issue = db.CategoryProperty(required=False)
    policy = db.CategoryProperty(required=False)
    format = db.CategoryProperty (required=False)
    origin = db.CategoryProperty(required=False)
    
    posted_by = db.StringProperty(required=False) # AKA Feed Owner
    
    #Only for Legislation
    bill = db.StringProperty(required=False) 
    congress = db.IntegerProperty(required=False) 
    
    # Report Selectors
    report = db.CategoryProperty(required=False)
    report_list = db.ListProperty(str)
    wr = db.BooleanProperty(required=False)
    repository = db.BooleanProperty(required=False)
    processed = db.BooleanProperty(required=False)
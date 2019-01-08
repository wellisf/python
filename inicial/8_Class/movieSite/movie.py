import webbrowser
     
class Movie():
     ''' This class provides a way to store movie related information ''' 
    
    title = None
    storyline = None
    poster_image_url = None
    trailer_youtube_url = None
    
    def __init__(self, title, storyline, post_image, trailer_youtube):
        
        self.title = title
        self.storyline = storyline
        self.poster_image_url = post_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)
        
    def show_post(self):
        webbrowser.open(self.post_image)         

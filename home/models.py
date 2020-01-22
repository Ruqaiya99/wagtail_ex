from django.db import models
from django.db.models import CharField
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
# from wagtail.core.fields import RichTextField
from wagtail.core.fields import StreamField
from streams import blocks
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList


class HomePage(Page):
    """Home page class""" 
    template = "home/home_page.html"

    background = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link'],null=True,blank=False)
    history = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link'],null=True,blank=False)
    
    participate = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link'],null=True,blank=False)
    participate_points = StreamField(
		[
			("text",blocks.participate_pointsBlock())
		],
		null=True,
		blank=True
	)
	
    content_panels = Page.content_panels + [
         FieldPanel("background"),
         FieldPanel("history"),
         StreamFieldPanel("participate_points"),
         FieldPanel("participate"),
        
      ]

    class Meta:
         verbose_name = "About Us Page"
#  *************


    


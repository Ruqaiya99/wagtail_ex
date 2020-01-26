from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.documents.blocks import DocumentChooserBlock
# from wagtailimages.blocks import ImageChooserBlock
from streams import blocks

class FlexPage(Page):
    template = "flex/flex_page.html"
    content = StreamField(
		[
			("doc_upload",blocks.FlexBlock())
		],
		null=True,
		blank=True,
	) 
    content_panels = Page.content_panels + [
         
         StreamFieldPanel("content"),
        
        
      ]

    class Meta:
         verbose_name = "Presentation and Document Page" 
    
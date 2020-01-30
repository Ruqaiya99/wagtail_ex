from django.db import models
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, PageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
# from wagtailimages.blocks import ImageChooserBlock
from streams import blocks
# Create your models here.
# from wagtail.core.blocks import DateTimeBlock
# from datetime import datetime
class WorkshopListingPage(Page):
    """Listing page lists all the Blog Detail Pages."""

    template = "workshop/workshop_listing_page.html"

    custom_heading = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_heading"),
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = WorkshopDetailPage.objects.live().public()
        return context


class WorkshopDetailPage(Page):
    """Workshop detail page."""
    template = "workshop/workshop_detail_page.html"
    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )
    description = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link'],null=True,blank=False)
    # objectives= RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link'],null=True,blank=True)
    # datetime = blocks.DateTimeBlock(default=date.today)
    # models.DateTimeBlock("required=True")
     
    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    content = StreamField(
        [    
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
           
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        ImageChooserPanel("blog_image"),
        StreamFieldPanel("content"),
        FieldPanel("description"),
        # FieldPanel("objectives"), 
    ]
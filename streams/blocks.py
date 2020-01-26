"""Streamfield live n here"""

from wagtail.core import blocks
from wagtail.core.blocks import RichTextBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.documents.blocks import DocumentChooserBlock

class TitleAndTextBlock(blocks.StructBlock):
    heading = blocks.CharBlock(classname="full title")
    paragraph = blocks.RichTextBlock(features=['h2', 'h3', 'bold', 'italic', 'link'])
    # body = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link'])

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"
from wagtail.core import blocks

# class RichtextBlock(blocks.RichTextBlock):
    
    #  class Meta:
        #  template = "streams/richtext_block.html"
        #  icon="doc-full"
        #  label = "Full RichText"
#   class SimpleRichtextBlock(blocks.RichTextBlock):
    
    #  def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        #  super().__init__(**kwargs)
        #  self.features = [
            #  "bold",
            #  "italic",
             
        #  ]
        
    #  class Meta:
        #  template = "streams/richtext_block.html"
        #  icon="edit"
        #  label = "Simple RichText"


class participate_pointsBlock(blocks.StructBlock):
   
    text = blocks.CharBlock(required=True,max_length=255,null=True,blank=False)
    # body = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link'])

    class Meta:
        template = "streams/participate_points.html"
        icon = "edit"
        label = "text"

# class DocumentChooserBlock():

    # class Meta:
    #     template = "streams/documents.html"
    #     icon = "edit"
    #     label = "text"        
class FlexBlock(blocks.StructBlock):
    """document block"""

    title = blocks.CharBlock(required=True)

    points = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("point", blocks.CharBlock(required=True, max_length=200)),
                ("doc_upload",DocumentChooserBlock(required=True)),
            ]
        )
    )

    class Meta:  #noqa
        template = "streams/flex_document.html"
        icon="edit"
        label="Presentation & Documents"
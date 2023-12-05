from django.contrib.auth.models import User
from django.db import models

from item.models import Item

class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)
    
class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)

# Many-to-Many Relationship:
# Conversation and User: Many users can be part of multiple conversations, and each conversation can involve multiple users. 
# This forms a many-to-many relationship between the Conversation and User models.

# One-to-Many Relationship:
# Item and Conversation: Each item can be associated with multiple conversations, but each conversation is linked to only one item. 
# This creates a one-to-many relationship between the Item and Conversation models.

# One-to-Many Relationship:
# Conversation and ConversationMessage: Each conversation can have multiple messages associated with it, but each message is linked 
# to only one conversation. This forms a one-to-many relationship between the Conversation and ConversationMessage models.

# One-to-Many Relationship:
# User and ConversationMessage: Each user can create multiple conversation messages, but each message is associated with only one user. 
# This establishes a one-to-many relationship between the User and ConversationMessage models.

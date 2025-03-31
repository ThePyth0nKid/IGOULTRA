from django.db import models
from django.conf import settings  # Use settings.AUTH_USER_MODEL instead of direct User import

# UserProfile extends the core user model with game-related fields
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # Link to custom user model
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)  # Optional profile image
    bio = models.TextField(blank=True)  # Short bio text
    location = models.CharField(max_length=100, blank=True)  # Optional location

    xp = models.IntegerField(default=0)     # Total XP for this user
    level = models.IntegerField(default=1)  # Current level
    rank = models.CharField(max_length=50, default='Unranked')  # Display rank title

    def __str__(self):
        return self.user.username  # Show username in admin/output


# XPEntry logs XP earned from real-life activities (pushups, running, etc.)
class XPEntry(models.Model):
    CATEGORY_CHOICES = [
        ('Pushups', 'Pushups'),
        ('Running', 'Running'),
        ('Meditation', 'Meditation'),
        ('Breathwork', 'Breathwork'),
        ('Custom', 'Custom'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Link to custom user model
        on_delete=models.CASCADE,
        related_name='xp_entries'  # Enables user.xp_entries.all()
    )
    amount = models.IntegerField()  # XP amount earned
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  # Type of activity
    timestamp = models.DateTimeField(auto_now_add=True)  # When the entry was created

    def __str__(self):
        return f"{self.user.username} - {self.amount} XP - {self.category}"

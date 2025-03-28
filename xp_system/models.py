from django.db import models
from django.contrib.auth.models import User


# UserProfile extends the default User with game-related fields
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    
    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    rank = models.CharField(max_length=50, default='Unranked')

    def __str__(self):
        return self.user.username


# XPEntry tracks individual XP actions (like pushups, running, etc.)
class XPEntry(models.Model):
    CATEGORY_CHOICES = [
        ('Pushups', 'Pushups'),
        ('Running', 'Running'),
        ('Meditation', 'Meditation'),
        ('Breathwork', 'Breathwork'),
        ('Custom', 'Custom'),
    ]
    
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='xp_entries'
    )
    amount = models.IntegerField()  # e.g. 200 XP
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} XP - {self.category}"

from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, verbose_name="Użytkownik")
    email = models.EmailField(verbose_name="E-mail")
    publication_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Data i czas rejestracji")
    update_datetime = models.DateTimeField(auto_now=True, verbose_name="Data i czas ostatniej aktualizacji")
    first_name = models.CharField(max_length=64, verbose_name="Imię", blank=True, default='')
    last_name = models.CharField(max_length=64, verbose_name="Nazwisko", blank=True, default='')

    def __str__(self):
        return f'({self.publication_datetime.date()}) {self.first_name} {self.last_name}'
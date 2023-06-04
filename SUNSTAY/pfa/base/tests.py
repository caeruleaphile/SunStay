from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import annonce

class AnnonceTestCase(TestCase):
    def setUp(self):
        # Créer un utilisateur de test
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Créer un objet annonce de test
        self.annonce = annonce.objects.create(title='Test House', description='This is a test house', price=100.0, location='Test Location')

    def test_annonce_creation(self):
        self.assertEqual(self.annonce.title, 'Test House')
        self.assertEqual(self.annonce.description, 'This is a test house')
        self.assertEqual(self.annonce.price, 100.0)
        self.assertEqual(self.annonce.location, 'Test Location')

    def test_annonce_list_view(self):
        # Vérifier si la vue de liste renvoie le code de statut 200 (OK)
        response = self.client.get(reverse('listing'))
        self.assertEqual(response.status_code, 200)

        # Vérifier si le titre de l'annonce de test est présent dans la réponse
        self.assertContains(response, 'Test House')

    def test_authenticated_annonce_list_view(self):
        # Connecter l'utilisateur de test
        self.client.login(username='testuser', password='testpassword')

        # Vérifier si la vue de liste renvoie le code de statut 200 (OK)
        response = self.client.get(reverse('listing'))
        self.assertEqual(response.status_code, 200)

        # Vérifier si le titre de l'annonce de test est présent dans la réponse
        self.assertContains(response, 'Test House')

    def test_unauthenticated_annonce_list_view(self):
        # Déconnecter l'utilisateur de test
        self.client.logout()

        # Vérifier si la vue de liste redirige vers la page de connexion (code de statut 302)
        response = self.client.get(reverse('listing'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/listing/')

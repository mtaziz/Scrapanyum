# from django.test import TestCase
# from Scraper.models import Mention
# from Core.models import Client
# from django.utils import timezone
#
#
# # models test
# class MentionTest(TestCase):
#     def create_client(self):
#         return Client.objects.create(
#             first_name="Scarlett",
#             last_name="Johansson",
#             brand="GITS",
#             tripadvisor="an url",
#             twitter="a twitter",
#             facebook="a FB"
#         )
#
#     def create_mention(self, c):
#         return Mention.objects.create(
#             social_network='twitter',
#             sentiment='positive',
#             date='2-5-2016',
#             title='Buen yantar',
#             content='Esta comida me ha hecho sentir cosas que solo senti en aquella orgia gay nazi con pirotecenia',
#             user='Donald Trump',
#             user_pic='a user pic url',
#             user_tag='Pepe le frog',
#             web_url='an url',
#             tags='category1, category2',
#             client=c
#                                       )
#
#     def test_mention_creation(self):
#         c = self.create_client()
#         self.assertTrue(isinstance(c, Client))
#         m = self.create_mention(c)
#         self.assertTrue(isinstance(m, Mention))
#         self.assertEqual(m.__unicode__(), m.social_network)
#         self.assertEqual(m.__unicode__(), m.sentiment)
#         self.assertEqual(m.__unicode__(), m.date)
#         self.assertEqual(m.__unicode__(), m.title)
#         self.assertEqual(m.__unicode__(), m.content)
#         self.assertEqual(m.__unicode__(), m.user)
#         self.assertEqual(m.__unicode__(), m.user_pic)
#         self.assertEqual(m.__unicode__(), m.user_tag)
#         self.assertEqual(m.__unicode__(), m.web_url)
#         self.assertEqual(m.__unicode__(), m.tags)

from django.test import RequestFactory, TestCase, Client
from django.contrib.auth.models import AnonymousUser

import mock


_views = __import__("MVC Structure.Controller.views")
_views = _views.Controller.views

# from Model.models import User, Profile, BillingAddress
_models = __import__("MVC Structure.Model.models")
_models = _models.Model.models

# cursor_wrapper = mock.Mock()
# cursor_wrapper.side_effect = RuntimeError("No touching the database!")
#
#
# @mock.patch(
#     "django.db.backends.util.CursorWraper",
#     cursor_wrapper
# )

class ViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = _models.User.objects._create_user(email="test@gmail.com",password="top_secret")
        self.category = _models.Category()
        self.category.title = "mix"
        self.category.save()
        self.product = _models.Product()
        self.product.name = "Iphone 12 pro max"
        self.product.category = self.category
        self.product.preview_text = "Iphone 12 pro max for sell"
        self.product.detail_text = "Iphone 12 pro max with 12 gb ram"
        self.product.old_price = 120000
        self.product.price = 100000
        self.product.save()
    def testLogin(self):
        request = self.factory.get('/account/login')
        request.user = self.user
        response = _views.login_user(request)
        # print(response.content)
        # print(help(response))
        # print(help(response))
        # response = MyView.as_View()(request)
        self.assertEqual(response.status_code, 200)
    # def test_login_post(self):
    #     pass
        # request = self.factory.post('/account/login',{'username':"test@gmail.com", "password":"top_secret"})
        # expected_string = "You Are Logged in Successfully"
        # self.assertContains(response.content, expected_string, "Should have logged in with correct credential")
        # self.assertEqual(response.status_code, 200)

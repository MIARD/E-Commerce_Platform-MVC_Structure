from django.test import RequestFactory, TestCase
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
        self.user = _models.User.objects._create_user(email="abcd@gmail.com",password="top_secret")
    def test_login(self):
        request = self.factory.get('/account/login')
        request.user = self.user
        print("hello world")
        response = _views.login_user(request)
        print(response.context)
        # print(help(response))
        # response = MyView.as_View()(request)
        self.assertEqual(response.status_code, 200)

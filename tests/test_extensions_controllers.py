import unittest
import jwt

try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import Mock, patch
from importlib import import_module

module = import_module('auth.controllers')
credentials = import_module('auth.credentials')


class ExtensionsTestCase(unittest.TestCase):

    def setUp(self):

        # Cleanup
        self.addCleanup(patch.stopall)

        # Mock response from models (to make sure it's new user)
        module.create_or_get_user = Mock(
            return_value={'new': True, 'id': 'test'}
        )
        self.private_key = credentials.private_key

    # Tests

    def test___check___on_new_user_is_called(self):
        profile = dict(id='test', name='name', email='test@mail.com')
        token = module._get_token_from_profile('test_provider', profile, self.private_key)
        user_profile = jwt.decode(token, self.private_key)
        self.assertEquals(user_profile.get('userid'), 'new-user')

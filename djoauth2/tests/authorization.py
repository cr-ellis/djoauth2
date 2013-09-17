# coding: utf-8
from django.conf.urls.defaults import patterns
from django.http import HttpResponse

from djoauth2.authorization import AuthorizationCodeGenerator
from djoauth2.authorization import AuthorizationException
from djoauth2.tests import test_urls
from djoauth2.tests.abstractions import DJOAuth2TestCase

class TestAuthorizationCodeEndpoint(DJOAuth2TestCase):
  # Method types
  def test_get_requests_succeed(self):
    self.initialize(scope_names=['verify'])

    authenticator = AuthorizationCodeGenerator('/oauth2/missing_redirect_uri/')

    def dummy_view(request):
      try:
        authenticator.validate(request)
      except AuthorizationException as e:
        self.fail(e)

      return HttpResponse('OK')

    test_urls.urlpatterns += patterns('',
        (r'^oauth2/authorization/', dummy_view),
    )

    self.user.set_password('password')
    self.user.save()

    self.oauth_client.login(username=self.user.username, password='password')

    response = self.oauth_client.make_authorization_request(
        client_id=self.client.key,
        scope_string=self.oauth_client.scope_string,
        endpoint='/oauth2/authorization/',
        use_ssl=True)

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.content, 'OK')



  #def test_post_requests_succeed(self):
  #  raise NotImplementedError()

  ## SSL
  #def test_ssl_required_secure_request_succeeds(self):
  #  raise NotImplementedError()
  #def test_ssl_required_insecure_request_fails(self):
  #  raise NotImplementedError()
  #def test_no_ssl_required_secure_request_succeeds(self):
  #  raise NotImplementedError()
  #def test_no_ssl_required_insecure_request_succeeds(self):
  #  raise NotImplementedError()

  ## Authentication
  #def test_user_not_authenticated_fails(self):
  #  raise NotImplementedError()
  #def test_response_type_not_code_fails(self):
  #  raise NotImplementedError()

  ## State
  #def test_state_required_and_no_state_included_fails(self):
  #  raise NotImplementedError()
  #def test_state_required_and_state_included_fails(self):
  #  raise NotImplementedError()
  #def test_state_not_requred_and_state_included_succeeds(self):
  #  raise NotImplementedError()
  #def test_state_not_requred_and_no_state_included_succeeds(self):
  #  raise NotImplementedError()

  ## Scope
  #def test_no_scope_included_fails(self):
  #  raise NotImplementedError()
  #def test_nonexistent_scope_included_fails(self):
  #  raise NotImplementedError()
  #def test_single_scope_included_succeeds(self):
  #  raise NotImplementedError()
  #def test_multiple_scopes_included_succeeds(self):
  #  raise NotImplementedError()

  ## Client ID
  #def test_no_client_id_included_fails(self):
  #  raise NotImplementedError()
  #def test_nonexistent_client_id_fails(self):
  #  raise NotImplementedError()

  ## Redirect URI
  #def test_included_redirect_matches_registered_succeeds(self):
  #  raise NotImplementedError()
  #def test_included_redirect_does_not_match_registered_fails(self):
  #  raise NotImplementedError()
  #def test_non_absolute_redirect_uri_fails(self):
  #  raise NotImplementedError()
  #def test_redirect_uri_query_parameters_preserved_on_success(self):
  #  raise NotImplementedError()
  #def test_redirect_uri_query_parameters_preserved_on_error(self):
  #  raise NotImplementedError()

  ## User interaction
  #def test_error_response_redirects_to_valid_uri(self):
  #  raise NotImplementedError()
  #def test_error_response_does_not_redirect_to_invalid_uri(self):
  #  raise NotImplementedError()



class TestMakeAuthorizationEndpointHelper(DJOAuth2TestCase):
  pass
  #def test_make_authorization_endpoint_returns_a_function(self):
  #  raise NotImplementedError()
  #def test_created_endpoint_redirects_to_passed_uri(self):
  #  raise NotImplementedError()
  #def test_created_endpoint_renders_passed_template(self):
  #  raise NotImplementedError()
  #def test_created_endpoint_redirects_to_missing_uri(self):
  #  raise NotImplementedError()




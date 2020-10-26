from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type
class AppTokenGenerador(PasswordResetTokenGenerator):

    def _make_hash_value(self, usuarioRegistrado, timestamp):
        return (text_type(usuarioRegistrado.is_active)+text_type(usuarioRegistrado.pk)+text_type(timestamp))

token_generador=AppTokenGenerador()
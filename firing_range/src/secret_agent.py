class SecretAgent:
    _codeword = ""

    def __init__(self, codename):
        self.codename = codename
        self._secrets = []

    def remember(self, secret):
        self._secrets.append(secret)

    @property
    def secret(self):
        return self._secrets[-1] if self._secrets else None

    @secret.setter
    def secret(self, value):
        self._secrets.append(self._encrypt(value))

    @secret.deleter
    def secret(self):
        self._secrets = []

    @classmethod
    def inform(cls, codeword):
        cls._codeword = codeword

    @classmethod
    def _encrypt(cls, message, *, decrypt=False):
        code = sum(ord(c) for c in cls._codeword)
        if decrypt:
            code = -code
        return ''.join(chr(ord(m) + code) for m in message)

    @staticmethod
    def inquiry(question):
        print("I know nothing")

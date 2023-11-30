from djoser.serializers import UserCreateSerializer as BaseUserCreate , UserSerializer as BaseUserSerializer

class UserCreateSerializer(BaseUserCreate):
    class Meta(BaseUserCreate.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
        
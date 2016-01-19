from rest_framework import serializers
from api.models import Nse, NseArgv

class NseArgvSerializer(serializers.ModelSerializer):
    """
    models.NseArgvのシリアライザ
    """
    class Meta:
        model = NseArgv
        fileds = ('argv', 'argv_discription', 'argv_discription_ja')

class NseSerializer(serializers.ModelSerializer):
    """
    models.Nseのシリアライザ
    """
    argvs = NseArgvSerializer(many=True, read_only=True)

    class Meta:
        model = Nse
        fields = ('name', 'category', 'summary', 'summary_ja', 'argvs', 'example_usage', 'example_output', 'author', 'download_link')

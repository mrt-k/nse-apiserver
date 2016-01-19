from django.db import models
from multiselectfield import MultiSelectField

class NseArgv(models.Model):
    """
    argv : NSEの引数
    argv_description : NSEの引数の説明
    argv_description_ja : NSEの引数の説明(日本語)
    """

    argv = models.CharField(max_length=128, blank=True)
    argv_description = models.TextField(blank=True)
    argv_description_ja = models.TextField(blank=True)

    def __str__(self):
        return "%s" % (self.argv)


class Nse(models.Model):
    """
    CATEGORIES : カテゴリの定義
    name : スクリプト名
    category : カテゴリ
    summary : スクリプトの説明
    summary_ja : スクリプトの説明(日本語)
    argvs : 引数. NseArgvとリレーション
    example_usage : 使い方の例
    example_output : 出力例
    author : 作者
    download_link : スクリプトへのリンク
    """

    CATEGORIES = (
            ("auth", "auth"),
            ("broadcast", "broadcast"),
            ("brute", "brute"),
            ("default", "default"),
            ("discovery", "discovery"),
            ("dos", "dos"),
            ("exploit", "exploit"),
            ("external", "external"),
            ("fuzzer", "fuzzer"),
            ("intrusive", "intrusive"),
            ("malware", "malware"),
            ("safe", "safe"),
            ("version", "version"),
            ("vuln", "vuln"),
    )

    name = models.CharField(max_length=128)
    category = MultiSelectField(max_length=128, choices=CATEGORIES)
    summary = models.TextField(blank=True)
    summary_ja = models.TextField(blank=True)
    argvs = models.ManyToManyField(NseArgv, blank=True)
    example_usage = models.TextField(blank=True)
    example_output = models.TextField(blank=True)
    author = models.CharField(max_length=128)
    download_link = models.URLField()

    def __str__(self):
        return "%s" % (self.name)

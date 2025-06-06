# Generated by Django 5.2.1 on 2025-05-28 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='servicos/', verbose_name='Imagem ilustrativa'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome do serviço'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Preço (R$)'),
        ),
    ]

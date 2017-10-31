# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='board_detail_test',
            fields=[
                ('id', models.CharField(db_column=b'id', max_length=20, primary_key=True, serialize=False)),
                ('zbxp', models.CharField(blank=True, db_column=b'\xe4\xb8\xbb\xe6\x9d\xbf\xe8\x8a\xaf\xe7\x89\x87', max_length=255)),
                ('jcxp', models.CharField(blank=True, db_column=b'\xe9\x9b\x86\xe6\x88\x90\xe8\x8a\xaf\xe7\x89\x87', max_length=255)),
                ('zxpz', models.CharField(blank=True, db_column=b'\xe4\xb8\xbb\xe8\x8a\xaf\xe7\x89\x87\xe7\xbb\x84', max_length=255)),
                ('xpzms', models.CharField(blank=True, db_column=b'\xe8\x8a\xaf\xe7\x89\x87\xe7\xbb\x84\xe6\x8f\x8f\xe8\xbf\xb0', max_length=255)),
                ('xsxp', models.CharField(blank=True, db_column=b'\xe6\x98\xbe\xe7\xa4\xba\xe8\x8a\xaf\xe7\x89\x87', max_length=255)),
                ('ypxp', models.CharField(blank=True, db_column=b'\xe9\x9f\xb3\xe9\xa2\x91\xe8\x8a\xaf\xe7\x89\x87', max_length=255)),
                ('wkxp', models.CharField(blank=True, db_column=b'\xe7\xbd\x91\xe5\x8d\xa1\xe8\x8a\xaf\xe7\x89\x87', max_length=255)),
                ('clqgg', models.CharField(blank=True, db_column=b'\xe5\xa4\x84\xe7\x90\x86\xe5\x99\xa8\xe8\xa7\x84\xe6\xa0\xbc', max_length=255)),
                ('cpulx', models.CharField(blank=True, db_column=b'CPU\xe7\xb1\xbb\xe5\x9e\x8b', max_length=255)),
                ('cpucc', models.CharField(blank=True, db_column=b'CPU\xe6\x8f\x92\xe6\xa7\xbd', max_length=255)),
                ('cpums', models.CharField(blank=True, db_column=b'CPU\xe6\x8f\x8f\xe8\xbf\xb0', max_length=255)),
                ('ncgg', models.CharField(blank=True, db_column=b'\xe5\x86\x85\xe5\xad\x98\xe8\xa7\x84\xe6\xa0\xbc', max_length=255)),
                ('nclx', models.CharField(blank=True, db_column=b'\xe5\x86\x85\xe5\xad\x98\xe7\xb1\xbb\xe5\x9e\x8b', max_length=255)),
                ('nccc', models.CharField(blank=True, db_column=b'\xe5\x86\x85\xe5\xad\x98\xe6\x8f\x92\xe6\xa7\xbd', max_length=255)),
                ('zdncrl', models.CharField(blank=True, db_column=b'\xe6\x9c\x80\xe5\xa4\xa7\xe5\x86\x85\xe5\xad\x98\xe5\xae\xb9\xe9\x87\x8f', max_length=255)),
                ('ncms', models.CharField(blank=True, db_column=b'\xe5\x86\x85\xe5\xad\x98\xe6\x8f\x8f\xe8\xbf\xb0', max_length=255)),
                ('kzcc', models.CharField(blank=True, db_column=b'\xe6\x89\xa9\xe5\xb1\x95\xe6\x8f\x92\xe6\xa7\xbd', max_length=255)),
                ('pciebz', models.CharField(blank=True, db_column=b'PCI_E\xe6\xa0\x87\xe5\x87\x86', max_length=255)),
                ('pciecc', models.CharField(blank=True, db_column=b'PCI_E\xe6\x8f\x92\xe6\xa7\xbd', max_length=255)),
                ('pcicc', models.CharField(blank=True, db_column=b'PCI\xe6\x8f\x92\xe6\xa7\xbd', max_length=255)),
                ('ccjk', models.CharField(blank=True, db_column=b'\xe5\xad\x98\xe5\x82\xa8\xe6\x8e\xa5\xe5\x8f\xa3', max_length=255)),
                ('iojk', models.CharField(blank=True, db_column=b'I_O\xe6\x8e\xa5\xe5\x8f\xa3', max_length=255)),
                ('usbjk', models.CharField(blank=True, db_column=b'USB\xe6\x8e\xa5\xe5\x8f\xa3', max_length=255)),
                ('hdmijk', models.CharField(blank=True, db_column=b'HDMI\xe6\x8e\xa5\xe5\x8f\xa3', max_length=255)),
                ('wdjk', models.CharField(blank=True, db_column=b'\xe5\xa4\x96\xe6\x8e\xa5\xe7\xab\xaf\xe5\x8f\xa3', max_length=255)),
                ('ps2jk', models.CharField(blank=True, db_column=b'PS_2\xe6\x8e\xa5\xe5\x8f\xa3', max_length=255)),
                ('dyck', models.CharField(blank=True, db_column=b'\xe7\x94\xb5\xe6\xba\x90\xe6\x8f\x92\xe5\x8f\xa3', max_length=255)),
                ('qtjk', models.CharField(blank=True, db_column=b'\xe5\x85\xb6\xe5\xae\x83\xe6\x8e\xa5\xe5\x8f\xa3', max_length=255)),
                ('bx', models.CharField(blank=True, db_column=b'\xe6\x9d\xbf\xe5\x9e\x8b', max_length=255)),
                ('zbbx', models.CharField(blank=True, db_column=b'\xe4\xb8\xbb\xe6\x9d\xbf\xe6\x9d\xbf\xe5\x9e\x8b', max_length=255)),
                ('wxcc', models.CharField(blank=True, db_column=b'\xe5\xa4\x96\xe5\xbd\xa2\xe5\xb0\xba\xe5\xaf\xb8', max_length=255)),
                ('rjgl', models.CharField(blank=True, db_column=b'\xe8\xbd\xaf\xe4\xbb\xb6\xe7\xae\xa1\xe7\x90\x86', max_length=255)),
                ('biosxn', models.CharField(blank=True, db_column=b'BIOS\xe6\x80\xa7\xe8\x83\xbd', max_length=255)),
                ('qtcs', models.CharField(blank=True, db_column=b'\xe5\x85\xb6\xe5\xae\x83\xe5\x8f\x82\xe6\x95\xb0', max_length=255)),
                ('dxkjs', models.CharField(blank=True, db_column=b'\xe5\xa4\x9a\xe6\x98\xbe\xe5\x8d\xa1\xe6\x8a\x80\xe6\x9c\xaf', max_length=255)),
                ('gdms', models.CharField(blank=True, db_column=b'\xe4\xbe\x9b\xe7\x94\xb5\xe6\xa8\xa1\xe5\xbc\x8f', max_length=255)),
                ('raidgn', models.CharField(blank=True, db_column=b'RAID\xe5\x8a\x9f\xe8\x83\xbd', max_length=255)),
                ('qtxn', models.CharField(blank=True, db_column=b'\xe5\x85\xb6\xe5\xae\x83\xe6\x80\xa7\xe8\x83\xbd', max_length=255)),
                ('ssrq', models.CharField(blank=True, db_column=b'\xe4\xb8\x8a\xe5\xb8\x82\xe6\x97\xa5\xe6\x9c\x9f', max_length=255)),
                ('zbfj', models.CharField(blank=True, db_column=b'\xe4\xb8\xbb\xe6\x9d\xbf\xe9\x99\x84\xe4\xbb\xb6', max_length=255)),
                ('bzqd', models.CharField(blank=True, db_column=b'\xe5\x8c\x85\xe8\xa3\x85\xe6\xb8\x85\xe5\x8d\x95', max_length=255)),
                ('bxxx', models.CharField(blank=True, db_column=b'\xe4\xbf\x9d\xe4\xbf\xae\xe4\xbf\xa1\xe6\x81\xaf', max_length=255)),
                ('bxzc', models.CharField(blank=True, db_column=b'\xe4\xbf\x9d\xe4\xbf\xae\xe6\x94\xbf\xe7\xad\x96', max_length=255)),
                ('zbsj', models.CharField(blank=True, db_column=b'\xe8\xb4\xa8\xe4\xbf\x9d\xe6\x97\xb6\xe9\x97\xb4', max_length=255)),
                ('zbbz', models.CharField(blank=True, db_column=b'\xe8\xb4\xa8\xe4\xbf\x9d\xe5\xa4\x87\xe6\xb3\xa8', max_length=255)),
                ('dhbz', models.CharField(blank=True, db_column=b'\xe7\x94\xb5\xe8\xaf\x9d\xe5\xa4\x87\xe6\xb3\xa8', max_length=255)),
                ('xxnr', models.CharField(blank=True, db_column=b'\xe8\xaf\xa6\xe7\xbb\x86\xe5\x86\x85\xe5\xae\xb9', max_length=2550)),
            ],
            options={
                'db_table': 'board_detail_test',
            },
        ),
        migrations.CreateModel(
            name='board_list_test',
            fields=[
                ('id', models.CharField(db_column=b'id', max_length=20, primary_key=True, serialize=False)),
                ('attr', models.CharField(db_column=b'attr', max_length=20)),
                ('name', models.CharField(db_column=b'name', max_length=255)),
                ('price', models.FloatField(db_column=b'price', max_length=255)),
                ('sales', models.IntegerField(db_column=b'sales', max_length=255)),
                ('provider', models.CharField(db_column=b'provider', max_length=255)),
                ('supportstaff_tel', models.CharField(blank=True, db_column=b'supportstaff_tel', max_length=255)),
                ('supportstaff_qq', models.CharField(blank=True, db_column=b'supportstaff_qq', max_length=255)),
                ('image1', models.CharField(db_column=b'image1', max_length=255)),
                ('image2', models.CharField(blank=True, db_column=b'image2', max_length=255)),
                ('image3', models.CharField(blank=True, db_column=b'image3', max_length=255)),
                ('image4', models.CharField(blank=True, db_column=b'image4', max_length=255)),
                ('image5', models.CharField(blank=True, db_column=b'image5', max_length=255)),
            ],
            options={
                'db_table': 'board_list_test',
            },
        ),
        migrations.CreateModel(
            name='cpu_detail_test',
            fields=[
                ('id', models.CharField(db_column=b'id', max_length=20, primary_key=True, serialize=False)),
                ('jbcs', models.CharField(blank=True, db_column=b'\xe5\x9f\xba\xe6\x9c\xac\xe5\x8f\x82\xe6\x95\xb0', max_length=255)),
                ('sylx', models.CharField(blank=True, db_column=b'\xe9\x80\x82\xe7\x94\xa8\xe7\xb1\xbb\xe5\x9e\x8b', max_length=255)),
                ('cpuxl', models.CharField(blank=True, db_column=b'cpu\xe7\xb3\xbb\xe5\x88\x97', max_length=255)),
                ('zzgy', models.CharField(blank=True, db_column=b'\xe5\x88\xb6\xe4\xbd\x9c\xe5\xb7\xa5\xe8\x89\xba', max_length=255)),
                ('hxdh', models.CharField(blank=True, db_column=b'\xe6\xa0\xb8\xe5\xbf\x83\xe4\xbb\xa3\xe5\x8f\xb7', max_length=255)),
                ('cpujg', models.CharField(blank=True, db_column=b'cpu\xe6\x9e\xb6\xe6\x9e\x84', max_length=255)),
                ('cclx', models.CharField(blank=True, db_column=b'\xe6\x8f\x92\xe6\xa7\xbd\xe7\xb1\xbb\xe5\x9e\x8b', max_length=255)),
                ('fzdx', models.CharField(blank=True, db_column=b'\xe5\xb0\x81\xe8\xa3\x85\xe5\xa4\xa7\xe5\xb0\x8f', max_length=255)),
                ('bzxs', models.CharField(blank=True, db_column=b'\xe5\x8c\x85\xe8\xa3\x85\xe5\xbd\xa2\xe5\xbc\x8f', max_length=255)),
                ('xncs', models.CharField(blank=True, db_column=b'\xe6\x80\xa7\xe8\x83\xbd\xe5\x8f\x82\xe6\x95\xb0', max_length=255)),
                ('cpuzp', models.CharField(blank=True, db_column=b'cpu\xe4\xb8\xbb\xe9\xa2\x91', max_length=255)),
                ('dtjspl', models.CharField(blank=True, db_column=b'\xe5\x8a\xa8\xe6\x80\x81\xe5\x8a\xa0\xe9\x80\x9f\xe9\xa2\x91\xe7\x8e\x87', max_length=255)),
                ('hxsl', models.CharField(blank=True, db_column=b'\xe6\xa0\xb8\xe5\xbf\x83\xe6\x95\xb0\xe9\x87\x8f', max_length=255)),
                ('xcsl', models.CharField(blank=True, db_column=b'\xe7\xba\xbf\xe7\xa8\x8b\xe6\x95\xb0\xe9\x87\x8f', max_length=255)),
                ('sjhc', models.CharField(blank=True, db_column=b'\xe4\xb8\x89\xe7\xba\xa7\xe7\xbc\x93\xe5\xad\x98', max_length=255)),
                ('zxgg', models.CharField(blank=True, db_column=b'\xe6\x80\xbb\xe7\xba\xbf\xe8\xa7\x84\xe6\xa0\xbc', max_length=255)),
                ('rsjgh', models.CharField(blank=True, db_column=b'\xe7\x83\xad\xe8\xae\xbe\xe8\xae\xa1\xe5\x8a\x9f\xe8\x80\x97', max_length=255)),
                ('nccs', models.CharField(blank=True, db_column=b'\xe5\x86\x85\xe5\xad\x98\xe5\x8f\x82\xe6\x95\xb0', max_length=255)),
                ('zczdnc', models.CharField(blank=True, db_column=b'\xe6\x94\xaf\xe6\x8c\x81\xe6\x9c\x80\xe5\xa4\xa7\xe5\x86\x85\xe5\xad\x98', max_length=255)),
                ('nclx', models.CharField(blank=True, db_column=b'\xe5\x86\x85\xe5\xad\x98\xe7\xb1\xbb\xe5\x9e\x8b', max_length=255)),
                ('ncms', models.CharField(blank=True, db_column=b'\xe5\x86\x85\xe5\xad\x98\xe6\x8f\x8f\xe8\xbf\xb0', max_length=255)),
                ('xkcs', models.CharField(blank=True, db_column=b'\xe6\x98\xbe\xe5\x8d\xa1\xe5\x8f\x82\xe6\x95\xb0', max_length=255)),
                ('jcxk', models.CharField(blank=True, db_column=b'\xe9\x9b\x86\xe6\x88\x90\xe6\x98\xbe\xe5\x8d\xa1', max_length=255)),
                ('xkjbpl', models.CharField(blank=True, db_column=b'\xe6\x98\xbe\xe5\x8d\xa1\xe5\x9f\xba\xe6\x9c\xac\xe9\xa2\x91\xe7\x8e\x87', max_length=255)),
                ('xkdtpl', models.CharField(blank=True, db_column=b'\xe6\x98\xbe\xe5\x8d\xa1\xe5\x8a\xa8\xe6\x80\x81\xe9\xa2\x91\xe7\x8e\x87', max_length=255)),
                ('xkqttx', models.CharField(blank=True, db_column=b'\xe6\x98\xbe\xe5\x8d\xa1\xe5\x85\xb6\xe5\xae\x83\xe7\x89\xb9\xe6\x80\xa7', max_length=255)),
                ('jscs', models.CharField(blank=True, db_column=b'\xe6\x8a\x80\xe6\x9c\xaf\xe5\x8f\x82\xe6\x95\xb0', max_length=255)),
                ('rpjsjs', models.CharField(blank=True, db_column=b'\xe7\x9d\xbf\xe9\xa2\x91\xe5\x8a\xa0\xe9\x80\x9f\xe6\x8a\x80\xe6\x9c\xaf', max_length=255)),
                ('cxcjs', models.CharField(blank=True, db_column=b'\xe8\xb6\x85\xe7\xba\xbf\xe7\xa8\x8b\xe6\x8a\x80\xe6\x9c\xaf', max_length=255)),
                ('xnhjs', models.CharField(blank=True, db_column=b'\xe8\x99\x9a\xe6\x8b\x9f\xe5\x8c\x96\xe6\x8a\x80\xe6\x9c\xaf', max_length=255)),
                ('zlj', models.CharField(blank=True, db_column=b'\xe6\x8c\x87\xe4\xbb\xa4\xe9\x9b\x86', max_length=255)),
                ('clq_64', models.CharField(blank=True, db_column=b'64\xe4\xbd\x8d\xe5\xa4\x84\xe7\x90\x86\xe5\x99\xa8', max_length=255)),
                ('qtjs', models.CharField(blank=True, db_column=b'\xe5\x85\xb6\xe5\xae\x83\xe6\x8a\x80\xe6\x9c\xaf', max_length=255)),
            ],
            options={
                'db_table': 'cpu_detail_test',
            },
        ),
        migrations.CreateModel(
            name='cpu_list_test',
            fields=[
                ('id', models.CharField(db_column=b'id', max_length=20, primary_key=True, serialize=False)),
                ('attr', models.CharField(db_column=b'attr', max_length=20)),
                ('name', models.CharField(db_column=b'name', max_length=255)),
                ('price', models.FloatField(db_column=b'price', max_length=255)),
                ('sales', models.IntegerField(db_column=b'sales', max_length=255)),
                ('provider', models.CharField(db_column=b'provider', max_length=255)),
                ('supportstaff_tel', models.CharField(blank=True, db_column=b'supportstaff_tel', max_length=255)),
                ('supportstaff_qq', models.CharField(blank=True, db_column=b'supportstaff_qq', max_length=255)),
                ('image1', models.CharField(db_column=b'image1', max_length=255)),
                ('image2', models.CharField(blank=True, db_column=b'image2', max_length=255)),
                ('image3', models.CharField(blank=True, db_column=b'image3', max_length=255)),
                ('image4', models.CharField(blank=True, db_column=b'image4', max_length=255)),
                ('image5', models.CharField(blank=True, db_column=b'image5', max_length=255)),
            ],
            options={
                'db_table': 'cpu_list_test',
            },
        ),
        migrations.CreateModel(
            name='graphic_detail_test',
            fields=[
                ('id', models.CharField(db_column=b'id', max_length=20, primary_key=True, serialize=False)),
                ('xkhx', models.CharField(blank=True, db_column=b'\xe6\x98\xbe\xe5\x8d\xa1\xe6\xa0\xb8\xe5\xbf\x83', max_length=255)),
                ('xpcs', models.CharField(blank=True, db_column=b'\xe8\x8a\xaf\xe7\x89\x87\xe5\x8e\x82\xe5\x95\x86', max_length=255)),
                ('xkxp', models.CharField(blank=True, db_column=b'\xe6\x98\xbe\xe5\x8d\xa1\xe8\x8a\xaf\xe7\x89\x87', max_length=255)),
                ('xkxpxl', models.CharField(blank=True, db_column=b'\xe6\x98\xbe\xe7\xa4\xba\xe8\x8a\xaf\xe7\x89\x87\xe7\xb3\xbb\xe5\x88\x97', max_length=255)),
                ('zzgy', models.CharField(blank=True, db_column=b'\xe5\x88\xb6\xe4\xbd\x9c\xe5\xb7\xa5\xe8\x89\xba', max_length=255)),
                ('hxdh', models.CharField(blank=True, db_column=b'\xe6\xa0\xb8\xe5\xbf\x83\xe4\xbb\xa3\xe5\x8f\xb7', max_length=255)),
                ('hxpl', models.CharField(blank=True, db_column=b'\xe6\xa0\xb8\xe5\xbf\x83\xe9\xa2\x91\xe7\x8e\x87', max_length=255)),
                ('cudahx', models.CharField(blank=True, db_column=b'CUDA\xe6\xa0\xb8\xe5\xbf\x83', max_length=255)),
                ('xcgg', models.CharField(blank=True, db_column=b'\xe6\x98\xbe\xe5\xad\x98\xe8\xa7\x84\xe6\xa0\xbc', max_length=255)),
                ('xcpl', models.CharField(blank=True, db_column=b'\xe6\x98\xbe\xe5\xad\x98\xe9\xa2\x91\xe7\x8e\x87', max_length=255)),
                ('xclx', models.CharField(blank=True, db_column=b'\xe6\x98\xbe\xe5\xad\x98\xe7\xb1\xbb\xe5\x9e\x8b', max_length=255)),
                ('xcrl', models.CharField(blank=True, db_column=b'\xe6\x98\xbe\xe5\xad\x98\xe5\xae\xb9\xe9\x87\x8f', max_length=255)),
                ('xcwk', models.CharField(blank=True, db_column=b'\xe6\x98\xbe\xe5\xad\x98\xe4\xbd\x8d\xe5\xae\xbd', max_length=255)),
                ('zdfbl', models.CharField(blank=True, db_column=b'\xe6\x9c\x80\xe5\xa4\xa7\xe5\x88\x86\xe8\xbe\xa8\xe7\x8e\x87', max_length=255)),
                ('xkjk', models.CharField(blank=True, db_column=b'\xe6\x98\xbe\xe5\x8d\xa1\xe6\x8e\xa5\xe5\x8f\xa3', max_length=255)),
                ('jklx', models.CharField(blank=True, db_column=b'\xe6\x8e\xa5\xe5\x8f\xa3\xe7\xb1\xbb\xe5\x9e\x8b', max_length=255)),
                ('iojk', models.CharField(blank=True, db_column=b'I_O\xe6\x8e\xa5\xe5\x8f\xa3', max_length=255)),
                ('dyjk', models.CharField(blank=True, db_column=b'\xe7\x94\xb5\xe6\xba\x90\xe6\x8e\xa5\xe5\x8f\xa3', max_length=255)),
                ('qtcs', models.CharField(blank=True, db_column=b'\xe5\x85\xb6\xe5\xae\x83\xe5\x8f\x82\xe6\x95\xb0', max_length=255)),
                ('xslx', models.CharField(blank=True, db_column=b'\xe6\x98\xbe\xe7\xa4\xba\xe7\xb1\xbb\xe5\x9e\x8b', max_length=255)),
                ('srfs', models.CharField(blank=True, db_column=b'\xe6\x95\xa3\xe7\x83\xad\xe6\x96\xb9\xe5\xbc\x8f', max_length=255)),
                ('api_3d', models.CharField(blank=True, db_column=b'API_3D', max_length=255)),
                ('gdms', models.CharField(blank=True, db_column=b'\xe4\xbe\x9b\xe7\x94\xb5\xe6\xa8\xa1\xe5\xbc\x8f', max_length=255)),
                ('zchdcp', models.CharField(blank=True, db_column=b'\xe6\x94\xaf\xe6\x8c\x81HDCP', max_length=255)),
                ('zdgh', models.CharField(blank=True, db_column=b'\xe6\x9c\x80\xe5\xa4\xa7\xe5\x8a\x9f\xe8\x80\x97', max_length=2550)),
                ('jydy', models.CharField(blank=True, db_column=b'\xe5\xbb\xba\xe8\xae\xae\xe7\x94\xb5\xe6\xba\x90', max_length=255)),
                ('qttd', models.CharField(blank=True, db_column=b'\xe5\x85\xb6\xe5\xae\x83\xe7\x89\xb9\xe7\x82\xb9', max_length=255)),
                ('sssj', models.CharField(blank=True, db_column=b'\xe4\xb8\x8a\xe5\xb8\x82\xe6\x97\xb6\xe9\x97\xb4', max_length=255)),
                ('bxxx', models.CharField(blank=True, db_column=b'\xe4\xbf\x9d\xe4\xbf\xae\xe4\xbf\xa1\xe6\x81\xaf', max_length=255)),
                ('bxzc', models.CharField(blank=True, db_column=b'\xe4\xbf\x9d\xe4\xbf\xae\xe6\x94\xbf\xe7\xad\x96', max_length=255)),
                ('zbsj', models.CharField(blank=True, db_column=b'\xe8\xb4\xa8\xe4\xbf\x9d\xe6\x97\xb6\xe9\x97\xb4', max_length=255)),
                ('zbbz', models.CharField(blank=True, db_column=b'\xe8\xb4\xa8\xe4\xbf\x9d\xe5\xa4\x87\xe6\xb3\xa8', max_length=255)),
                ('xxnr', models.CharField(blank=True, db_column=b'\xe8\xaf\xa6\xe7\xbb\x86\xe5\x86\x85\xe5\xae\xb9', max_length=2550)),
            ],
            options={
                'db_table': 'graphic_detail_test',
            },
        ),
        migrations.CreateModel(
            name='graphic_list_test',
            fields=[
                ('id', models.CharField(db_column=b'id', max_length=20, primary_key=True, serialize=False)),
                ('attr', models.CharField(db_column=b'attr', max_length=20)),
                ('name', models.CharField(db_column=b'name', max_length=255)),
                ('price', models.FloatField(db_column=b'price', max_length=255)),
                ('sales', models.IntegerField(db_column=b'sales', max_length=255)),
                ('provider', models.CharField(db_column=b'provider', max_length=255)),
                ('supportstaff_tel', models.CharField(blank=True, db_column=b'supportstaff_tel', max_length=255)),
                ('supportstaff_qq', models.CharField(blank=True, db_column=b'supportstaff_qq', max_length=255)),
                ('image1', models.CharField(db_column=b'image1', max_length=255)),
                ('image2', models.CharField(blank=True, db_column=b'image2', max_length=255)),
                ('image3', models.CharField(blank=True, db_column=b'image3', max_length=255)),
                ('image4', models.CharField(blank=True, db_column=b'image4', max_length=255)),
                ('image5', models.CharField(blank=True, db_column=b'image5', max_length=255)),
            ],
            options={
                'db_table': 'graphic_list_test',
            },
        ),
        migrations.CreateModel(
            name='mem_detail_test',
            fields=[
                ('id', models.CharField(db_column=b'id', max_length=20, primary_key=True, serialize=False)),
                ('jbcs', models.CharField(blank=True, db_column=b'\xe5\x9f\xba\xe6\x9c\xac\xe5\x8f\x82\xe6\x95\xb0', max_length=255)),
                ('sylx', models.CharField(blank=True, db_column=b'\xe9\x80\x82\xe7\x94\xa8\xe7\xb1\xbb\xe5\x9e\x8b', max_length=255)),
                ('ncrl', models.CharField(blank=True, db_column=b'\xe5\x86\x85\xe5\xad\x98\xe5\xae\xb9\xe9\x87\x8f', max_length=255)),
                ('rlms', models.CharField(blank=True, db_column=b'\xe5\xae\xb9\xe9\x87\x8f\xe6\x8f\x8f\xe8\xbf\xb0', max_length=255)),
                ('nclx', models.CharField(blank=True, db_column=b'\xe5\x86\x85\xe5\xad\x98\xe7\xb1\xbb\xe5\x9e\x8b', max_length=255)),
                ('nczp', models.CharField(blank=True, db_column=b'\xe5\x86\x85\xe5\xad\x98\xe4\xb8\xbb\xe9\xa2\x91', max_length=255)),
                ('csbz', models.CharField(blank=True, db_column=b'\xe4\xbc\xa0\xe8\xbe\x93\xe6\xa0\x87\xe5\x87\x86', max_length=255)),
                ('zjs', models.CharField(blank=True, db_column=b'\xe9\x92\x88\xe8\x84\x9a\xe6\x95\xb0', max_length=255)),
                ('cclx', models.CharField(blank=True, db_column=b'\xe6\x8f\x92\xe6\xa7\xbd\xe7\xb1\xbb\xe5\x9e\x8b', max_length=255)),
                ('jscs', models.CharField(blank=True, db_column=b'\xe6\x8a\x80\xe6\x9c\xaf\xe5\x8f\x82\xe6\x95\xb0', max_length=255)),
                ('klpz', models.CharField(blank=True, db_column=b'\xe9\xa2\x97\xe7\xb2\x92\xe9\x85\x8d\xe7\xbd\xae', max_length=255)),
                ('clyc', models.CharField(blank=True, db_column=b'CL\xe5\xbb\xb6\xe8\xbf\x9f', max_length=255)),
                ('zzgy', models.CharField(blank=True, db_column=b'\xe5\x88\xb6\xe4\xbd\x9c\xe5\xb7\xa5\xe8\x89\xba', max_length=255)),
                ('qtcs', models.CharField(blank=True, db_column=b'\xe5\x85\xb6\xe5\xae\x83\xe5\x8f\x82\xe6\x95\xb0', max_length=255)),
                ('srp', models.CharField(blank=True, db_column=b'\xe6\x95\xa3\xe7\x83\xad\xe7\x89\x87', max_length=255)),
                ('gzdy', models.CharField(blank=True, db_column=b'\xe5\xb7\xa5\xe4\xbd\x9c\xe7\x94\xb5\xe5\x8e\x8b', max_length=255)),
                ('qtxn', models.CharField(blank=True, db_column=b'\xe5\x85\xb6\xe5\xae\x83\xe6\x80\xa7\xe8\x83\xbd', max_length=255)),
                ('qttd', models.CharField(blank=True, db_column=b'\xe5\x85\xb6\xe5\xae\x83\xe7\x89\xb9\xe7\x82\xb9', max_length=255)),
                ('bxxx', models.CharField(blank=True, db_column=b'\xe4\xbf\x9d\xe4\xbf\xae\xe4\xbf\xa1\xe6\x81\xaf', max_length=255)),
                ('bxzc', models.CharField(blank=True, db_column=b'\xe4\xbf\x9d\xe4\xbf\xae\xe6\x94\xbf\xe7\xad\x96', max_length=255)),
                ('zbsj', models.CharField(blank=True, db_column=b'\xe8\xb4\xa8\xe4\xbf\x9d\xe6\x97\xb6\xe9\x97\xb4', max_length=255)),
                ('zbbz', models.CharField(blank=True, db_column=b'\xe8\xb4\xa8\xe4\xbf\x9d\xe5\xa4\x87\xe6\xb3\xa8', max_length=255)),
                ('dhbz', models.CharField(blank=True, db_column=b'\xe7\x94\xb5\xe8\xaf\x9d\xe5\xa4\x87\xe6\xb3\xa8', max_length=255)),
                ('xxnr', models.CharField(blank=True, db_column=b'\xe8\xaf\xa6\xe7\xbb\x86\xe5\x86\x85\xe5\xae\xb9', max_length=2550)),
            ],
            options={
                'db_table': 'mem_detail_test',
            },
        ),
        migrations.CreateModel(
            name='mem_list_test',
            fields=[
                ('id', models.CharField(db_column=b'id', max_length=20, primary_key=True, serialize=False)),
                ('attr', models.CharField(db_column=b'attr', max_length=20)),
                ('name', models.CharField(db_column=b'name', max_length=255)),
                ('price', models.FloatField(db_column=b'price', max_length=255)),
                ('sales', models.IntegerField(db_column=b'sales', max_length=255)),
                ('provider', models.CharField(db_column=b'provider', max_length=255)),
                ('supportstaff_tel', models.CharField(blank=True, db_column=b'supportstaff_tel', max_length=255)),
                ('supportstaff_qq', models.CharField(blank=True, db_column=b'supportstaff_qq', max_length=255)),
                ('image1', models.CharField(db_column=b'image1', max_length=255)),
                ('image2', models.CharField(blank=True, db_column=b'image2', max_length=255)),
                ('image3', models.CharField(blank=True, db_column=b'image3', max_length=255)),
                ('image4', models.CharField(blank=True, db_column=b'image4', max_length=255)),
                ('image5', models.CharField(blank=True, db_column=b'image5', max_length=255)),
            ],
            options={
                'db_table': 'mem_list_test',
            },
        ),
        migrations.CreateModel(
            name='power_detail_test',
            fields=[
                ('id', models.CharField(db_column=b'id', max_length=20, primary_key=True, serialize=False)),
                ('jbcs', models.CharField(blank=True, db_column=b'\xe5\x9f\xba\xe6\x9c\xac\xe5\x8f\x82\xe6\x95\xb0', max_length=255)),
                ('dylx', models.CharField(blank=True, db_column=b'\xe7\x94\xb5\xe6\xba\x90\xe7\xb1\xbb\xe5\x9e\x8b', max_length=255)),
                ('syfw', models.CharField(blank=True, db_column=b'\xe9\x80\x82\xe7\x94\xa8\xe8\x8c\x83\xe5\x9b\xb4', max_length=255)),
                ('dybb', models.CharField(blank=True, db_column=b'\xe7\x94\xb5\xe6\xba\x90\xe7\x89\x88\xe6\x9c\xac', max_length=255)),
                ('cxlx', models.CharField(blank=True, db_column=b'\xe5\x87\xba\xe7\xba\xbf\xe7\xb1\xbb\xe5\x9e\x8b', max_length=255)),
                ('edgl', models.CharField(blank=True, db_column=b'\xe9\xa2\x9d\xe5\xae\x9a\xe5\x8a\x9f\xe7\x8e\x87', max_length=255)),
                ('fsms', models.CharField(blank=True, db_column=b'\xe9\xa3\x8e\xe6\x89\x87\xe6\x8f\x8f\xe8\xbf\xb0', max_length=255)),
                ('dycc', models.CharField(blank=True, db_column=b'\xe7\x94\xb5\xe6\xba\x90\xe5\xb0\xba\xe5\xaf\xb8', max_length=255)),
                ('dyjk', models.CharField(blank=True, db_column=b'\xe7\x94\xb5\xe6\xba\x90\xe6\x8e\xa5\xe5\x8f\xa3', max_length=255)),
                ('zbjk', models.CharField(blank=True, db_column=b'\xe4\xb8\xbb\xe6\x9d\xbf\xe6\x8e\xa5\xe5\x8f\xa3', max_length=255)),
                ('cpujk44', models.CharField(blank=True, db_column=b'cpu\xe6\x8e\xa5\xe5\x8f\xa344', max_length=255)),
                ('cpujkf', models.CharField(blank=True, db_column=b'cpu\xe6\x8e\xa5\xe5\x8f\xa3\xe6\x96\xb9', max_length=255)),
                ('xkjk62', models.CharField(blank=True, db_column=b'\xe6\x98\xbe\xe5\x8d\xa1\xe6\x8e\xa5\xe5\x8f\xa362', max_length=255)),
                ('xkjk6', models.CharField(blank=True, db_column=b'\xe6\x98\xbe\xe5\x8d\xa1\xe6\x8e\xa5\xe5\x8f\xa36', max_length=255)),
                ('ypjk', models.CharField(blank=True, db_column=b'\xe7\xa1\xac\xe7\x9b\x98\xe6\x8e\xa5\xe5\x8f\xa3', max_length=255)),
                ('rqjk', models.CharField(blank=True, db_column=b'\xe8\xbd\xaf\xe9\xa9\xb1\xe6\x8e\xa5\xe5\x8f\xa3', max_length=255)),
                ('gdjk', models.CharField(blank=True, db_column=b'\xe4\xbe\x9b\xe7\x94\xb5\xe6\x8e\xa5\xe5\x8f\xa3', max_length=255)),
                ('xncs', models.CharField(blank=True, db_column=b'\xe6\x80\xa7\xe8\x83\xbd\xe5\x8f\x82\xe6\x95\xb0', max_length=255)),
                ('jlsc', models.CharField(blank=True, db_column=b'\xe4\xba\xa4\xe6\xb5\x81\xe8\xbe\x93\xe5\x85\xa5', max_length=255)),
                ('scdl3_3V', models.CharField(blank=True, db_column=b'\xe8\xbe\x93\xe5\x87\xba\xe7\x94\xb5\xe6\xb5\x813_3V', max_length=255)),
                ('scdl5V', models.CharField(blank=True, db_column=b'\xe8\xbe\x93\xe5\x87\xba\xe7\x94\xb5\xe6\xb5\x815V', max_length=255)),
                ('scdl5Vsb', models.CharField(blank=True, db_column=b'\xe8\xbe\x93\xe5\x87\xba\xe7\x94\xb5\xe6\xb5\x815Vsb', max_length=255)),
                ('scdl12V', models.CharField(blank=True, db_column=b'\xe8\xbe\x93\xe5\x87\xba\xe7\x94\xb5\xe6\xb5\x8112V', max_length=255)),
                ('scdl_12V', models.CharField(blank=True, db_column=b'\xe8\xbe\x93\xe5\x87\xba\xe7\x94\xb5\xe6\xb5\x81_12V', max_length=255)),
                ('qtcs', models.CharField(blank=True, db_column=b'\xe5\x85\xb6\xe4\xbb\x96\xe5\x8f\x82\xe6\x95\xb0', max_length=255)),
                ('rfclx', models.CharField(blank=True, db_column=b'PFC\xe7\xb1\xbb\xe5\x9e\x8b', max_length=255)),
                ('bhgn', models.CharField(blank=True, db_column=b'\xe4\xbf\x9d\xe6\x8a\xa4\xe5\x8a\x9f\xe8\x83\xbd', max_length=255)),
                ('zhxl', models.CharField(blank=True, db_column=b'\xe8\xbd\xac\xe6\x8d\xa2\xe6\x95\x88\xe7\x8e\x87', max_length=255)),
                ('plusrz', models.CharField(blank=True, db_column=b'PLUS\xe8\xae\xa4\xe8\xaf\x81_80', max_length=255)),
                ('agrz', models.CharField(blank=True, db_column=b'\xe5\xae\x89\xe8\xa7\x84\xe8\xae\xa4\xe8\xaf\x81', max_length=255)),
                ('dyfj', models.CharField(blank=True, db_column=b'\xe7\x94\xb5\xe6\xba\x90\xe9\x99\x84\xe4\xbb\xb6', max_length=255)),
                ('dyqd', models.CharField(blank=True, db_column=b'\xe5\x8c\x85\xe8\xa3\x85\xe6\xb8\x85\xe5\x8d\x95', max_length=255)),
                ('bxxx', models.CharField(blank=True, db_column=b'\xe4\xbf\x9d\xe4\xbf\xae\xe4\xbf\xa1\xe6\x81\xaf', max_length=255)),
                ('bxzc', models.CharField(blank=True, db_column=b'\xe4\xbf\x9d\xe4\xbf\xae\xe6\x94\xbf\xe7\xad\x96', max_length=255)),
                ('zbsj', models.CharField(blank=True, db_column=b'\xe8\xb4\xa8\xe4\xbf\x9d\xe6\x97\xb6\xe9\x97\xb4', max_length=255)),
                ('zbbz', models.CharField(blank=True, db_column=b'\xe8\xb4\xa8\xe4\xbf\x9d\xe5\xa4\x87\xe6\xb3\xa8', max_length=255)),
                ('dhbz', models.CharField(blank=True, db_column=b'\xe7\x94\xb5\xe8\xaf\x9d\xe5\xa4\x87\xe6\xb3\xa8', max_length=255)),
                ('xxnr', models.CharField(blank=True, db_column=b'\xe8\xaf\xa6\xe7\xbb\x86\xe5\x86\x85\xe5\xae\xb9', max_length=2550)),
            ],
            options={
                'db_table': 'power_detail_test',
            },
        ),
        migrations.CreateModel(
            name='power_list_test',
            fields=[
                ('id', models.CharField(db_column=b'id', max_length=20, primary_key=True, serialize=False)),
                ('attr', models.CharField(db_column=b'attr', max_length=20)),
                ('name', models.CharField(db_column=b'name', max_length=255)),
                ('price', models.FloatField(db_column=b'price', max_length=255)),
                ('sales', models.IntegerField(db_column=b'sales', max_length=255)),
                ('provider', models.CharField(db_column=b'provider', max_length=255)),
                ('supportstaff_tel', models.CharField(blank=True, db_column=b'supportstaff_tel', max_length=255)),
                ('supportstaff_qq', models.CharField(blank=True, db_column=b'supportstaff_qq', max_length=255)),
                ('image1', models.CharField(db_column=b'image1', max_length=255)),
                ('image2', models.CharField(blank=True, db_column=b'image2', max_length=255)),
                ('image3', models.CharField(blank=True, db_column=b'image3', max_length=255)),
                ('image4', models.CharField(blank=True, db_column=b'image4', max_length=255)),
                ('image5', models.CharField(blank=True, db_column=b'image5', max_length=255)),
            ],
            options={
                'db_table': 'power_list_test',
            },
        ),
        migrations.CreateModel(
            name='radiator_detail_test',
            fields=[
                ('id', models.CharField(db_column=b'id', max_length=20, primary_key=True, serialize=False)),
                ('jbcs', models.CharField(blank=True, db_column=b'\xe5\x9f\xba\xe6\x9c\xac\xe5\x8f\x82\xe6\x95\xb0', max_length=255)),
                ('srqlx', models.CharField(blank=True, db_column=b'\xe6\x95\xa3\xe7\x83\xad\xe5\x99\xa8\xe7\xb1\xbb\xe5\x9e\x8b', max_length=255)),
                ('srfs', models.CharField(blank=True, db_column=b'\xe6\x95\xa3\xe7\x83\xad\xe6\x96\xb9\xe5\xbc\x8f', max_length=255)),
                ('flcs', models.CharField(blank=True, db_column=b'\xe9\xa3\x8e\xe5\x86\xb7\xe5\x8f\x82\xe6\x95\xb0', max_length=255)),
                ('fscc', models.CharField(blank=True, db_column=b'\xe9\xa3\x8e\xe6\x89\x87\xe5\xb0\xba\xe5\xaf\xb8', max_length=255)),
                ('zclx', models.CharField(blank=True, db_column=b'\xe8\xbd\xb4\xe6\x89\xbf\xe7\xb1\xbb\xe5\x9e\x8b', max_length=255)),
                ('zsms', models.CharField(blank=True, db_column=b'\xe8\xbd\xac\xe6\x95\xb0\xe6\x8f\x8f\xe8\xbf\xb0', max_length=255)),
                ('zdfl', models.CharField(blank=True, db_column=b'\xe6\x9c\x80\xe5\xa4\xa7\xe9\xa3\x8e\xe9\x87\x8f', max_length=255)),
                ('fy', models.CharField(blank=True, db_column=b'\xe9\xa3\x8e\xe5\x8e\x8b', max_length=255)),
                ('zy', models.CharField(blank=True, db_column=b'\xe5\x99\xaa\xe9\x9f\xb3', max_length=255)),
                ('srqfj', models.CharField(blank=True, db_column=b'\xe6\x95\xa3\xe7\x83\xad\xe5\x99\xa8\xe9\x99\x84\xe4\xbb\xb6', max_length=255)),
                ('bzqd', models.CharField(blank=True, db_column=b'\xe5\x8c\x85\xe8\xa3\x85\xe6\xb8\x85\xe5\x8d\x95', max_length=255)),
                ('bxxx', models.CharField(blank=True, db_column=b'\xe4\xbf\x9d\xe4\xbf\xae\xe4\xbf\xa1\xe6\x81\xaf', max_length=255)),
                ('bxzc', models.CharField(blank=True, db_column=b'\xe4\xbf\x9d\xe4\xbf\xae\xe6\x94\xbf\xe7\xad\x96', max_length=255)),
                ('zbsj', models.CharField(blank=True, db_column=b'\xe8\xb4\xa8\xe4\xbf\x9d\xe6\x97\xb6\xe9\x97\xb4', max_length=255)),
                ('zbbz', models.CharField(blank=True, db_column=b'\xe8\xb4\xa8\xe4\xbf\x9d\xe5\xa4\x87\xe6\xb3\xa8', max_length=255)),
                ('dhbz', models.CharField(blank=True, db_column=b'\xe7\x94\xb5\xe8\xaf\x9d\xe5\xa4\x87\xe6\xb3\xa8', max_length=255)),
                ('xxnr', models.CharField(blank=True, db_column=b'\xe8\xaf\xa6\xe7\xbb\x86\xe5\x86\x85\xe5\xae\xb9', max_length=2550)),
            ],
            options={
                'db_table': 'radiator_detail_test',
            },
        ),
        migrations.CreateModel(
            name='radiator_list_test',
            fields=[
                ('id', models.CharField(db_column=b'id', max_length=20, primary_key=True, serialize=False)),
                ('attr', models.CharField(db_column=b'attr', max_length=20)),
                ('name', models.CharField(db_column=b'name', max_length=255)),
                ('price', models.FloatField(db_column=b'price', max_length=255)),
                ('sales', models.IntegerField(db_column=b'sales', max_length=255)),
                ('provider', models.CharField(db_column=b'provider', max_length=255)),
                ('supportstaff_tel', models.CharField(blank=True, db_column=b'supportstaff_tel', max_length=255)),
                ('supportstaff_qq', models.CharField(blank=True, db_column=b'supportstaff_qq', max_length=255)),
                ('image1', models.CharField(db_column=b'image1', max_length=255)),
                ('image2', models.CharField(blank=True, db_column=b'image2', max_length=255)),
                ('image3', models.CharField(blank=True, db_column=b'image3', max_length=255)),
                ('image4', models.CharField(blank=True, db_column=b'image4', max_length=255)),
                ('image5', models.CharField(blank=True, db_column=b'image5', max_length=255)),
            ],
            options={
                'db_table': 'radiator_list_test',
            },
        ),
        migrations.CreateModel(
            name='scrapy_date',
            fields=[
                ('id', models.CharField(db_column=b'id', max_length=20, primary_key=True, serialize=False)),
                ('date', models.CharField(db_column=b'date', max_length=20)),
            ],
            options={
                'db_table': 'scapy_date',
            },
        ),
    ]

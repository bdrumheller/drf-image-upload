import tempfile
from os import walk
import os

from django.contrib.auth.models import User, Group
from quickstart.models import Image, ImageContainer
from rest_framework import serializers
from django.core.files import File
import urllib.request
from versatileimagefield.serializers import VersatileImageFieldSerializer
import zipfile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image')

    image = VersatileImageFieldSerializer(sizes='image_sizes', required=False)


class ImageContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageContainer
        fields = ('id', 'description', 'url', 'images', 'some_test')

    images = ImageSerializer(many=True, read_only=True)
    some_test = serializers.CharField(source='get_absolute_url', read_only=True)

    def create(self, validated_data):
        new_image_container = ImageContainer.objects.create(**validated_data)
        url = validated_data['url']  # zip file url

        with tempfile.TemporaryDirectory() as tmp_dir:
            with tempfile.TemporaryFile() as zip_tmp:
                with urllib.request.urlopen(url) as image_zip:
                    zip_tmp.write(image_zip.read())

                with zipfile.ZipFile(zip_tmp, 'r') as zip_ref:
                    zip_ref.extractall(tmp_dir)


            for (dir_path, dir_names, file_names) in walk(tmp_dir):
                for file_name in file_names:
                    print(os.sep.join((dir_path, file_name)))
                    with open(os.sep.join((dir_path, file_name)), 'rb') as file_contents:
                        new_image = Image.objects.create(image_container=new_image_container)
                        new_image.image.save(file_name, File(file_contents))
                        new_image.save()

        #image_filename = url[url.rindex('/')+1:]
        #with urllib.request.urlopen(url) as image:
        #    new_image.images.save(image_filename, File(image))

        # create each of the images
        # same the new images

        return new_image_container

    #def to_representation(self, instance):
    #    rep = super(ImageContainerSerializer, self).to_representation(instance)
        #rep.pop('url') # remove the url from the get request
    #    return rep

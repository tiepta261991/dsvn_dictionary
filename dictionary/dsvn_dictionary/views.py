from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from dsvn_dictionary.models import DsvnDictionary, Vi_Dictionary, Ja_Dictionary
from dsvn_dictionary.serializers import DsvnDictionarySerializer
from dsvn_dictionary.serializers import Vi_DictionarySerializer
from dsvn_dictionary.serializers import Ja_DictionarySerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def vidictionary_list(request):

    # function get all list of vi-dictionary
    if request.method == 'GET':
        tutorials = Vi_Dictionary.objects.all()
        
        vi_text = request.GET.get('vi_text', None)
        if vi_text is not None:
            tutorials = tutorials.filter(title__icontains=vi_text)
        
        tutorials_serializer = Vi_DictionarySerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    # function add to vi-dictionary
    elif request.method == 'POST':
        vidic_data = JSONParser().parse(request)
        vidic_serializer = Vi_DictionarySerializer(data=vidic_data)
        if vidic_serializer.is_valid():
            vidic_serializer.save()
            return JsonResponse(vidic_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(vidic_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # function delete all list of vi-dictionary
    elif request.method == 'DELETE':
        count = Vi_Dictionary.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# function search by vi to ja
@api_view(['GET', 'POST', 'DELETE'])
def vidictionary_search(request):
    if request.method == 'GET':
        title_name=request.GET['vi_text']
        # if title_name is not None:
        #     return JsonResponse(Error("please enter key search"), status=status.HTTP_400_BAD_REQUEST)

        tutorials = Vi_Dictionary.objects.raw("SELECT id, vi_text FROM dsvn_dictionary_vi_dictionary WHERE vi_text=%s",[title_name])
        tutorials_serializer = Vi_DictionarySerializer(tutorials, many=True)
        
        return JsonResponse(tutorials_serializer.data, safe=False)

# function update vi-dic by id
@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def vidictionary_update(request, pk):

    try: 
        tutorial = Vi_Dictionary.objects.get(id=pk) 
    except Vi_Dictionary.DoesNotExist: 
        return JsonResponse({'message': 'The vi dictionary does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = Vi_DictionarySerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

# function delete vi-dic by id
@api_view(['GET', 'POST', 'DELETE'])
def vidictionary_delete(request, pk):

    try: 
        vi_dic = Vi_Dictionary.objects.get(pk=pk) 
    except Vi_Dictionary.DoesNotExist: 
        return JsonResponse({'message': 'The vi dictionary does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'DELETE': 
        vi_dic.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)    

    # if request.method == 'DELETE':
    #     title_name = request.GET['vi_text']
    #     Vi_Dictionary.objects.filter(vi_text = title_name).delete()
    #     return JsonResponse({'message': 'Tutorials were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def jadictionary_list(request):

    # function get all list of ja-dictionary
    if request.method == 'GET':
        ja_dic = Ja_Dictionary.objects.all()
        
        hiragana_text = request.GET.get('hiragana_text', None)
        if hiragana_text is not None:
            ja_dic = ja_dic.filter(title__icontains=hiragana_text)
        
        ja_serializer = Ja_DictionarySerializer(ja_dic, many=True)
        return JsonResponse(ja_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    # function add to ja-dictionary
    elif request.method == 'POST':
        jadic_data = JSONParser().parse(request)
        jadic_serializer = Ja_DictionarySerializer(data=jadic_data)
        if jadic_serializer.is_valid():
            jadic_serializer.save()
            return JsonResponse(jadic_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(jadic_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # function delete all list of ja-dictionary
    elif request.method == 'DELETE':
        count = Ja_Dictionary.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# function search by ja to vi
@api_view(['GET', 'POST', 'DELETE'])
def jadictionary_search(request):
    if request.method == 'GET':
        title_name=request.GET['ja_text']
        # if title_name is not None:
        #     return JsonResponse(Error("please enter key search"), status=status.HTTP_400_BAD_REQUEST)

        jadictionarys = Ja_Dictionary.objects.raw("SELECT id, hiragana_text, vi_text FROM dsvn_dictionary_ja_dictionary WHERE (hiragana_text=%s OR kanji_text=%s OR katakana_text=%s)",[title_name, title_name, title_name])
        ja_serializer = Ja_DictionarySerializer(jadictionarys, many=True)
        
        return JsonResponse(ja_serializer.data, safe=False)

# function update ja-dic by id
@api_view(['GET', 'PUT'])
def jadictionary_update(request, pk):

    try: 
        jadic_data = Ja_Dictionary.objects.get(id=pk) 
    except Ja_Dictionary.DoesNotExist: 
        return JsonResponse({'message': 'The ja dictionary does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'PUT': 
        ja_data = JSONParser().parse(request) 
        jadic_serializer = Ja_DictionarySerializer(jadic_data, data=ja_data) 
        if jadic_serializer.is_valid(): 
            jadic_serializer.save() 
            return JsonResponse(jadic_serializer.data) 
        return JsonResponse(jadic_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

# function delete ja-dic by id
@api_view(['GET', 'POST', 'DELETE'])
def jadictionary_delete(request, pk):

    try: 
        ja_dic = Ja_Dictionary.objects.get(pk=pk) 
    except Ja_Dictionary.DoesNotExist: 
        return JsonResponse({'message': 'The ja dictionary does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'DELETE': 
        ja_dic.delete() 
        return JsonResponse({'message': 'The row ja dictionary was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)  

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = DsvnDictionary.objects.all()
        
        title = request.GET.get('title', None)
        
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = DsvnDictionarySerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = DsvnDictionarySerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = DsvnDictionary.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try: 
        tutorial = DsvnDictionary.objects.get(pk=pk) 
    except DsvnDictionary.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = DsvnDictionarySerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = DsvnDictionarySerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = DsvnDictionary.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutorials_serializer = DsvnDictionarySerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)  
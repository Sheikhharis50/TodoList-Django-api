from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, status, renderers
from django.core.paginator import Paginator


class todoView(APIView):
    def get(self, request):
        """
        List all Todo.
        """
        data = {}

        try:
            todos = todo.objects.all().order_by('id')
            result = todoSerializer(todos, many=True).data
            data['status'] = 1  # Means success
            data['message'] = 'Successful.'
            page_number = request.GET.get('page')
            page_size = request.GET.get('size')
            if page_number or page_size:
                paginator = Paginator(result, page_size)
                page_obj = paginator.get_page(page_number)
                data['data'] = list(page_obj)
                data['has_next'] = page_obj.has_next()
            else:
                data['data'] = result
        except Exception as e:
            print(e)
            del data
            data = {}
            data['status'] = 0  # Means error
            data['message'] = 'Invalid Request!'

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        '''
        Create a new todo
        '''

        title = request.data.get("title")

        try:
            if not title:
                raise Exception("title is not given")
        except Exception as e:
            print(e)
            return Response({
                'status': 0,
                'message': 'Invalid data!',
            }, status=status.HTTP_200_OK)

        data = {}

        try:
            data['status'] = 1  # Means success
            data['message'] = 'Created Successfully.'
            obj = todo.objects.create(
                title=title
            )
            data['data'] = todoSerializer(obj).data
        except Exception as e:
            print(e)
            del data
            data = {}
            data['status'] = 0  # Means error
            data['message'] = 'Invalid Request!'

        return Response(data=data, status=status.HTTP_200_OK)


class todoDetailView(APIView):
    def get(self, request, id):
        """
        Retrieve a todo.
        """
        data = {}
        try:
            td = todo.objects.get(id=id)
            result = todoSerializer(td).data
            data['status'] = 1  # Means success
            data['message'] = 'Successful.'
            data['data'] = result
        except Exception as e:
            print(e)
            del data
            data = {}
            data['status'] = 0  # Means error
            data['message'] = 'Record Not Found!'

        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, id):
        '''
        Update a todo
        '''

        title = request.data.get("title")
        completed = request.data.get("completed")

        try:
            td = todo.objects.get(id=id)
            if not completed:
                completed = False
        except Exception as e:
            print(e)
            return Response({
                'status': 0,
                'message': 'Record Not Found!',
            }, status=status.HTTP_200_OK)

        data = {}
        try:
            data['status'] = 1  # Means success
            data['message'] = 'Updated Successfully.'
            td.title = title
            td.completed = completed
            td.save()
            data['data'] = todoSerializer(td).data
        except Exception as e:
            print(e)
            del data
            data = {}
            data['status'] = 0  # Means error
            data['message'] = 'Failed!'

        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        """
        Delete a todo.
        """
        data = {}

        try:
            todo.objects.get(id=id).delete()
            data['status'] = 1  # Means success
            data['message'] = 'Deleted Successfully.'
        except Exception as e:
            print(e)
            del data
            data = {}
            data['status'] = 0  # Means error
            data['message'] = 'Record Not Found!'

        return Response(data, status=status.HTTP_200_OK)

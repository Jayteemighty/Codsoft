# calc/views.py
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'calc/home.html')

def calculate(request, operation):
    try:
        num1 = float(request.GET.get('num1', 0))
        num2 = float(request.GET.get('num2', 0))

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
        elif operation == 'percentage':
            result = num1 * (num2 / 100)
        else:
            raise ValueError("Invalid operation")

        return JsonResponse({'result': result})
    except Exception as e:
        return JsonResponse({'error': str(e)})

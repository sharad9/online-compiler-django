from django.shortcuts import render
from django.http import HttpResponse
from .fileGenerator import generateFile;
from django.views.decorators.csrf import csrf_exempt
from .executor import compile
from compiler.models import Payload;
import json
# Create your views here.

#create index function

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def runcode(request):

    output = "";
    code = "";
    if request.method == "GET":
        
       
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        code = data['code'];
        language = data['language'];
        userName = data['userName'];


        try:
           
            print(generateFile(code = code, language = language , userName = "CodeFiles/"+userName));
            output = compile(language = language, fileName = userName, inputs = inputs);
            payload = Payload(userName = userName,language = language, code = code, inputs = inputs, output = output);
            payload.save();

        except Exception as e:
            
            output = e        

        return HttpResponse(json.dumps(output))
        
    if request.method == "POST":
        
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        print(data)
        code = data['code'];
        language = data['language'];
        userName = data['userName'];
        inputs = data['inputs'];
        
        try:
           
            print(generateFile(code = code, language = language , userName = userName));
            output = compile(language = language, fileName = userName, inputs = inputs);
            payload = Payload(userName = userName,language = language, code = code, inputs = inputs, output = output);
            payload.save();

        except Exception as e:
            
            output = e        


        return HttpResponse(json.dumps(output))

    result = {"code": code, "output":output};
    return HttpResponse(json.dumps(result))    

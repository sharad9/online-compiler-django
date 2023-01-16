from subprocess import Popen, PIPE, STDOUT


def execute(command,inputArgument):
    stdout, stderr = Popen(command, stdout=PIPE, stdin=PIPE, stderr=STDOUT, encoding='utf-8').communicate(inputArgument);
    stdout = stdout is not None and stdout.splitlines() or [];
    stderr = stderr is not None and stderr.splitlines() or [];
    return dict(output = stdout, stderr = stderr);
    
def compile(language, fileName, inputs):

    fileName = "CodeFiles/"+fileName;

    match (language):
        
        case "JavaScript":
            return None;

        case "Python":
            inputArgument = '\n'.join(inputs)
            command = ['python', fileName+".py"];
            return execute(command,inputArgument);

        case "Java":
            inputArgument = '\n'.join(inputs)
            command = ['java', fileName+".java"];
            return execute(command,inputArgument);
        
        case default:
            return None;
        
# print(compile("Python", "UserName",["45"]))        
# print(compile("Java", "UserName",["45"]))





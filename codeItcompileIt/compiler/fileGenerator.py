def writeContent(content, fileName, extention):
    try:
        file = open(fileName+extention, "w")
        file.writelines(content)
        file.close()
        return "Created/Overwritten {fileName}{extention}".format(fileName=fileName, extention=extention)
    except Exception as e:
        return e


def generateFile(language, userName, code):

    userName ="CodeFiles/"+userName;
    
    match(language):

        case "Python":
            return writeContent(code, userName, ".py")

        case "Java":
            return writeContent(code, userName, ".java")

        case "CPP":
            return writeContent(code, userName, ".c++")

        case default:
            return ("Verify Language!!")


#print(generateFile("Python", "UserName", "print('UserName')"))
JavaCode = '''
import java.util.*;
import java.util.concurrent.TimeUnit;
class Hii {
    public static void main(String args[]) {
        long startTime = System.nanoTime();
        long stopTime = System.nanoTime();
        long elapsedTime = (stopTime - startTime);
        System.out.println("Execution Time :"+(TimeUnit.MILLISECONDS.convert(elapsedTime, TimeUnit.NANOSECONDS) / 1000.0)+"s");
    }

}
'''
#print(generateFile("Java", "CodeFiles/UserName", JavaCode))

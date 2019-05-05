import os,sys
import filecmp


class Compilar:

    codes = {
        200: 'success',
        404: 'file not found',
        400: 'error',
        408: 'timeout'
    }


    languages = {
        "py": 'python',
        "cpp": 'c++',
        "c": 'c',
        "java": 'Java'
    }

    def __init__(self, source_code, lang):
        PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
        os.chdir(PROJECT_PATH + '/sandbox')

        self.language = self.languages[lang]
        self.file_name = "program.{}".format(lang)
        with open(self.file_name,"w") as f:
            f.write(source_code)

        if self.file_name == 'java':
            self.class_file = self.file_name[:6]+".class"
        elif self.file_name == 'c':
            self.class_file = self.file_name[:-2]
        elif self.file_name == 'cpp':
            self.class_file = self.file_name[:-4]


        self.input_file = "input.txt"
        self.output_file = "output.txt"
        self.program_output = "program_output.txt"


    def compile(self,source_code):

        if (os.path.isfile(self.file_name)):
            if self.language == 'java':
                cmd = 'javac '+ self.file_name
                os.system()
            elif self.language == 'c' or self.language == 'c++':
                cmd = 'gcc -o '+ self.class_file + ' ' + self.file_name

            os.system(cmd)
            
            if (os.path.isfile(self.class_file)):
                return 200
            else:
                return 400
        else:
            return 404


    def run(self,input_data, timeout):

        with open(self.input_file,"w") as f:
            f.write(input_data)

        if self.language == 'java':
            cmd = 'java '+ self.class_file
        elif self.language == 'c' or self.language == 'cpp':
            cmd = './'+ self.class_file
        elif self.language == 'python':
            cmd = 'python ' +  self.file_name

        command = 'timeout '+ str(timeout) +' '+cmd+' < ' + self.input_file + ' > ' + self.program_output
        r = os.system(command)

        if self.language != 'python':
            os.remove(self.class_file)

        if r == 0:
            return 200
        elif r == 31744:
            os.remove('out.txt')
            return 408
        else:
            os.remove('out.txt')
            return 400


    def match(self, output):
        with open(self.output_file,"w") as f:
            f.write(output)

        if os.path.isfile(self.program_output) and os.path.isfile(self.output_file):
            b = filecmp.cmp(self.program_output, self.output_file)
            return b
        else:
            return 404


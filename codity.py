# -*- coding: UTF-8 -*-




import inspect
from functools import wraps



def trace_entry_and_exit(decorated_function):
    @wraps(decorated_function)
    def wrapper(*dec_fn_args, **dec_fn_kwargs):
        func_name = decorated_function.__name__
        CodityRunner.trace("Run : " + func_name)
        arg_names = decorated_function.__code__.co_varnames
        params = dict(args=dict(zip(arg_names, dec_fn_args)))
        print("\t" + ', '.join(['{}={}'.format(str(k), repr(v)) for k, v in params.items()]))
        out = decorated_function(*dec_fn_args)
        print "\t" + 'ret = %s' % repr(out)
        return out
    return wrapper



class CodityRunner(object):
    
    FUNCTION_NAME = "solution"
    
    def __init__(self, solution_func=None):
        self.vector = []
        if solution_func is None:
            self.solution = self.find_solution()
        else:
            self.solution = solution_func
            

    @staticmethod
    def trace(info):
        print info
    
    @classmethod
    def find_solution(cls):
        module = __import__("__main__")
        return module.__dict__.get(cls.FUNCTION_NAME)
    

    def inspect_traceback(self, exception):
        CALL_DEPTH = 1
        DEFAULT = dict.fromkeys(["path", "line", "function", "code"], "no info")
        traceback = inspect.trace()
        stack = []
        try :
            for index in range(CALL_DEPTH, len(traceback)):
                stack.append(dict(DEFAULT))
                stack[-1]["path"]      = traceback[index][1]
                stack[-1]["line"]      = traceback[index][2]
                stack[-1]["function"]  = traceback[index][3]
                stack[-1]["code"]      = str(traceback[index][4][0]).strip("\n\r")
        except Exception:
            pass
        des = {}
        des["stack"]            = stack
        des["exception_info"]   = str(exception)
        des["exception_class"]  = exception.__class__.__name__
        return des


    def trace_traceback(self, des):
        dis = "Exception \n"
        for sline in des["stack"] :
            dis += "    File \"%s\", line %d, in %s\n" % (sline["path"], sline["line"], sline["function"])
            dis += "        %s\n" % (sline["code"])
        dis += "    %s\n" % (des["exception_class"])
        dis += "    %s\n" % (des["exception_info"])
        self.trace(dis)
            

    def add_vector(self, result, *params):
        self.vector.append((result, params))
    
    def run(self, *param):
        try:
            ret = self.solution(*param)
        except Exception, ex :
            des = self.inspect_traceback(ex)
            self.trace_traceback(des)            
            ret = None
        return ret

    def run_test(self):
        res_pass = 0
        for index, vec in enumerate(self.vector):
            params = vec[1]

            res = vec[0]
            self.trace("######### %d/%s #########" % (index, len(self.vector)))
            ret = self.run(*params)
            if ret == res:
                self.trace("Pass => %s == %s" % (repr(ret), repr(res)))
                res_pass += 1
            else:
                self.trace("Fail => %s != %s" % (repr(ret), repr(res)))
            self.trace("")
        self.trace("Total pass : %d/%s" % (res_pass, len(self.vector)))
        self.trace("")

















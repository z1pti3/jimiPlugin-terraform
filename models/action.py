from pathlib import Path
import uuid
from python_terraform import *

import jimi

class _terraformInit(jimi.action._action):
    terraform_dir = str()

    def doAction(self,data):
        terraform_dir = jimi.helpers.evalString(self.terraform_dir,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        if not jimi.helpers.safeFilepath(str(Path(terraform_dir)),"data/temp"):
            return { "result" : False, "rc" : 403, "msg" : "Invalid terraform directory." }
        t = Terraform(working_dir=str(Path(terraform_dir)))
        return_code, stdout, stderr = t.init()
        return { "result" : True, "rc" : return_code, "data" : stdout, "error": stderr }

class _terraformPlan(jimi.action._action):
    terraform_dir = str()
    terraform_vars = dict()

    def doAction(self,data):
        terraform_dir = jimi.helpers.evalString(self.terraform_dir,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        terraform_vars = jimi.helpers.evalDict(self.terraform_vars,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        if not jimi.helpers.safeFilepath(str(Path(terraform_dir)),"data/temp"):
            return { "result" : False, "rc" : 403, "msg" : "Invalid terraform directory." }
        t = Terraform(working_dir=str(Path(terraform_dir)))
        out = str(uuid.uuid4())
        return_code, stdout, stderr = t.plan(var=terraform_vars,out=out)
        return { "result" : True, "rc" : return_code, "data" : stdout, "error": stderr, "plan_out" : out }

class _terraformApply(jimi.action._action):
    terraform_dir = str()
    terraform_vars = dict()
    terraform_plan = str()

    def doAction(self,data):
        terraform_dir = jimi.helpers.evalString(self.terraform_dir,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        terraform_plan = jimi.helpers.evalDict(self.terraform_plan,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        terraform_vars = jimi.helpers.evalString(self.terraform_vars,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        if not jimi.helpers.safeFilepath(str(Path(terraform_dir)),"data/temp"):
            return { "result" : False, "rc" : 403, "msg" : "Invalid terraform directory." }
        t = Terraform(working_dir=str(Path(terraform_dir)))
        if terraform_plan:
            return_code, stdout, stderr = t.apply(terraform_plan,var=terraform_vars)
        else:
            return_code, stdout, stderr = t.apply(var=terraform_vars)
        return { "result" : True, "rc" : return_code, "data" : stdout, "error": stderr }

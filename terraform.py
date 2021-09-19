import jimi

class _terraform(jimi.plugin._plugin):
    version = 0.11

    def install(self):
        # Register models
        jimi.model.registerModel("terraformInit","_terraformInit","_action","plugins.terraform.models.action")
        jimi.model.registerModel("terraformPlan","_terraformPlan","_action","plugins.terraform.models.action")
        jimi.model.registerModel("terraformApply","_terraformApply","_action","plugins.terraform.models.action")
        return True

    def uninstall(self):
        # deregister models
        jimi.model.deregisterModel("terraformInit","_terraformInit","_action","plugins.terraform.models.action")
        jimi.model.deregisterModel("terraformPlan","_terraformPlan","_action","plugins.terraform.models.action")
        jimi.model.deregisterModel("terraformApply","_terraformApply","_action","plugins.terraform.models.action")
        return True

    def upgrade(self,LatestPluginVersion):
        if self.version < 0.11:
            jimi.model.registerModel("terraformPlan","_terraformPlan","_action","plugins.terraform.models.action")
            jimi.model.registerModel("terraformApply","_terraformApply","_action","plugins.terraform.models.action")
        return True

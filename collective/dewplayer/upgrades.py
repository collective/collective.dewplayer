PROFILE = 'profile-collective.gallery:default'

def upgrade_1_to_10(context):
    """Install new configurable view
    """
    #apply types.xml
    context.runImportStepFromProfile(PROFILE, 'typeinfo')
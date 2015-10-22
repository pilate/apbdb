from django.db import models


class Apbpawnconstant(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)  # Field name made lowercase.
    eapbpawnconstant = models.IntegerField(db_column='eAPBPawnConstant', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APBPawnConstant'


class Apbsupportpages(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sbaseurl = models.TextField(db_column='sBaseURL', blank=True, null=True)  # Field name made lowercase.
    sinternalbrowsertitle = models.TextField(db_column='sInternalBrowserTitle', blank=True, null=True)  # Field name made lowercase.
    sparameters = models.TextField(db_column='sParameters', blank=True, null=True)  # Field name made lowercase.
    sregiondependanturl_inikey = models.TextField(db_column='sRegionDependantURL_INIKey', blank=True, null=True)  # Field name made lowercase.
    eapbsupportpages = models.IntegerField(db_column='eAPBSupportPages', blank=True, null=True)  # Field name made lowercase.
    eurlwippage = models.IntegerField(db_column='eURLWipPage', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APBSupportPages'


class Apbviewporttypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    eapbviewporttype = models.IntegerField(db_column='eAPBViewportType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APBViewportTypes'


class Activitymessageparametertypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    slocalisationtoken = models.TextField(db_column='sLocalisationToken', blank=True, null=True)  # Field name made lowercase.
    eactivitymessageparametertype = models.IntegerField(db_column='eActivityMessageParameterType', blank=True, null=True)  # Field name made lowercase.
    ndebugparam = models.IntegerField(db_column='nDebugParam', blank=True, null=True)  # Field name made lowercase.
    econversion = models.IntegerField(db_column='eConversion', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActivityMessageParameterTypes'


class Activitymessagepriorities(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eactivitymessagepriority = models.IntegerField(db_column='eActivityMessagePriority', blank=True, null=True)  # Field name made lowercase.
    fdelaymax = models.FloatField(db_column='fDelayMax', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActivityMessagePriorities'


class Activitymessages(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eactivitymessage = models.IntegerField(db_column='eActivityMessage', blank=True, null=True)  # Field name made lowercase.
    ehudmessage = models.IntegerField(db_column='eHUDMessage', blank=True, null=True)  # Field name made lowercase.
    eparamtype_0 = models.IntegerField(db_column='eParamType_0', blank=True, null=True)  # Field name made lowercase.
    eparamtype_1 = models.IntegerField(db_column='eParamType_1', blank=True, null=True)  # Field name made lowercase.
    eparamtype_2 = models.IntegerField(db_column='eParamType_2', blank=True, null=True)  # Field name made lowercase.
    eparamtype_3 = models.IntegerField(db_column='eParamType_3', blank=True, null=True)  # Field name made lowercase.
    eparamtype_4 = models.IntegerField(db_column='eParamType_4', blank=True, null=True)  # Field name made lowercase.
    epriority = models.IntegerField(db_column='ePriority', blank=True, null=True)  # Field name made lowercase.
    eexcludelist = models.IntegerField(db_column='eExcludeList', blank=True, null=True)  # Field name made lowercase.
    eincludelist = models.IntegerField(db_column='eIncludeList', blank=True, null=True)  # Field name made lowercase.
    elocation = models.IntegerField(db_column='eLocation', blank=True, null=True)  # Field name made lowercase.
    evalidfaction = models.IntegerField(db_column='eValidFaction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActivityMessages'


class Ammocategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    sname = models.TextField(db_column='sName', blank=True, null=True)  # Field name made lowercase.
    snameabbreviated = models.TextField(db_column='sNameAbbreviated', blank=True, null=True)  # Field name made lowercase.
    squantitytext = models.TextField(db_column='sQuantityText', blank=True, null=True)  # Field name made lowercase.
    eammocategory = models.IntegerField(db_column='eAmmoCategory', blank=True, null=True)  # Field name made lowercase.
    erequiresweaponunlocked = models.IntegerField(db_column='eRequiresWeaponUnlocked', blank=True, null=True)  # Field name made lowercase.
    nboxcost = models.IntegerField(db_column='nBoxCost', blank=True, null=True)  # Field name made lowercase.
    nboxsize = models.IntegerField(db_column='nBoxSize', blank=True, null=True)  # Field name made lowercase.
    ncapacity = models.IntegerField(db_column='nCapacity', blank=True, null=True)  # Field name made lowercase.
    ngiftedamount = models.IntegerField(db_column='nGiftedAmount', blank=True, null=True)  # Field name made lowercase.
    npresetboxquantity_0 = models.IntegerField(db_column='nPresetBoxQuantity_0', blank=True, null=True)  # Field name made lowercase.
    npresetboxquantity_1 = models.IntegerField(db_column='nPresetBoxQuantity_1', blank=True, null=True)  # Field name made lowercase.
    npresetboxquantity_2 = models.IntegerField(db_column='nPresetBoxQuantity_2', blank=True, null=True)  # Field name made lowercase.
    npresetboxquantity_3 = models.IntegerField(db_column='nPresetBoxQuantity_3', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    shudimage_bullet = models.IntegerField(db_column='sHUDImage_Bullet', blank=True, null=True)  # Field name made lowercase.
    bthrowngrenade = models.IntegerField(db_column='bThrownGrenade', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AmmoCategories'


class AnimtreedecisionEquippeditem(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eanimtreedecision_equippeditem = models.IntegerField(db_column='eAnimTreeDecision_EquippedItem', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AnimTreeDecision_EquippedItem'


class AnimtreedecisionVehicle(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eanimtreedecision_vehicle = models.IntegerField(db_column='eAnimTreeDecision_Vehicle', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AnimTreeDecision_Vehicle'


class Animationdescriptors(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eanimationdescriptor = models.IntegerField(db_column='eAnimationDescriptor', blank=True, null=True)  # Field name made lowercase.
    fstaminadrain = models.FloatField(db_column='fStaminaDrain', blank=True, null=True)  # Field name made lowercase.
    ercetype = models.IntegerField(db_column='eRCEType', blank=True, null=True)  # Field name made lowercase.
    bfreezecameraloc = models.IntegerField(db_column='bFreezeCameraLoc', blank=True, null=True)  # Field name made lowercase.
    bresetlocomotion = models.IntegerField(db_column='bResetLocomotion', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AnimationDescriptors'


class Audioamp(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    saudioswitchname = models.TextField(db_column='sAudioSwitchName', blank=True, null=True)  # Field name made lowercase.
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)  # Field name made lowercase.
    fvolume = models.FloatField(db_column='fVolume', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AudioAmp'


class Audiodumpvalve(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    saudioeventname = models.TextField(db_column='sAudioEventName', blank=True, null=True)  # Field name made lowercase.
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AudioDumpValve'


class Audioengine(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    saudioeventname = models.TextField(db_column='sAudioEventName', blank=True, null=True)  # Field name made lowercase.
    ssimulationdataset = models.TextField(db_column='sSimulationDataSet', blank=True, null=True)  # Field name made lowercase.
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AudioEngine'


class Audioexhaust(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    saudioeventname = models.TextField(db_column='sAudioEventName', blank=True, null=True)  # Field name made lowercase.
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AudioExhaust'


class Audioexhaustpops(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    saudioeventname = models.TextField(db_column='sAudioEventName', blank=True, null=True)  # Field name made lowercase.
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AudioExhaustPops'


class Audiogearchange(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    saudioeventname = models.TextField(db_column='sAudioEventName', blank=True, null=True)  # Field name made lowercase.
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AudioGearChange'


class Audiohorn(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    saudiotype = models.TextField(db_column='sAudioType', blank=True, null=True)  # Field name made lowercase.
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)  # Field name made lowercase.
    fpitchmodifier = models.FloatField(db_column='fPitchModifier', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AudioHorn'


class Audiosiren(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    saudiotype = models.TextField(db_column='sAudioType', blank=True, null=True)  # Field name made lowercase.
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AudioSiren'


class Audiospeaker(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)  # Field name made lowercase.
    feqparameter1 = models.FloatField(db_column='fEQParameter1', blank=True, null=True)  # Field name made lowercase.
    feqparameter2 = models.FloatField(db_column='fEQParameter2', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AudioSpeaker'


class Audiotransmission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    saudioeventname = models.TextField(db_column='sAudioEventName', blank=True, null=True)  # Field name made lowercase.
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)  # Field name made lowercase.
    fpitchmodifier = models.FloatField(db_column='fPitchModifier', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AudioTransmission'


class Audioturbo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    smainaudioeventname = models.TextField(db_column='sMainAudioEventName', blank=True, null=True)  # Field name made lowercase.
    ssecondaudioeventname = models.TextField(db_column='sSecondAudioEventName', blank=True, null=True)  # Field name made lowercase.
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)  # Field name made lowercase.
    fmainpitchmodifier = models.FloatField(db_column='fMainPitchModifier', blank=True, null=True)  # Field name made lowercase.
    fmainvolumefullrpm = models.FloatField(db_column='fMainVolumeFullRPM', blank=True, null=True)  # Field name made lowercase.
    fmainvolumestartrpm = models.FloatField(db_column='fMainVolumeStartRPM', blank=True, null=True)  # Field name made lowercase.
    fsecondpitchmodifier = models.FloatField(db_column='fSecondPitchModifier', blank=True, null=True)  # Field name made lowercase.
    fsecondvolumefullrpm = models.FloatField(db_column='fSecondVolumeFullRPM', blank=True, null=True)  # Field name made lowercase.
    fsecondvolumestartrpm = models.FloatField(db_column='fSecondVolumeStartRPM', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AudioTurbo'


class Awesomeplayerdetectionrules(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eawesomeplayerdetectionrules = models.IntegerField(db_column='eAwesomePlayerDetectionRules', blank=True, null=True)  # Field name made lowercase.
    ndistancesamplinginterval = models.IntegerField(db_column='nDistanceSamplingInterval', blank=True, null=True)  # Field name made lowercase.
    ndistancesamplingintervalthreshold = models.IntegerField(db_column='nDistanceSamplingIntervalThreshold', blank=True, null=True)  # Field name made lowercase.
    ndistancesamplingtotalthreshold = models.IntegerField(db_column='nDistanceSamplingTotalThreshold', blank=True, null=True)  # Field name made lowercase.
    ndistrictmapallowedtime = models.IntegerField(db_column='nDistrictMapAllowedTime', blank=True, null=True)  # Field name made lowercase.
    ntime = models.IntegerField(db_column='nTime', blank=True, null=True)  # Field name made lowercase.
    ntimebetweenwarnings = models.IntegerField(db_column='nTimeBetweenWarnings', blank=True, null=True)  # Field name made lowercase.
    nwarningdistrictmaptimetokick = models.IntegerField(db_column='nWarningDistrictMapTimeToKick', blank=True, null=True)  # Field name made lowercase.
    nwarningtimetokick = models.IntegerField(db_column='nWarningTimeToKick', blank=True, null=True)  # Field name made lowercase.
    ballcsa = models.IntegerField(db_column='bAllCSA', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AwesomePlayerDetectionRules'


class Awesomeplayerdetectionrulesevents(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eawesomeplayerdetectionrules = models.IntegerField(db_column='eAwesomePlayerDetectionRules', blank=True, null=True)  # Field name made lowercase.
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AwesomePlayerDetectionRulesEvents'


class Bombequipmenttypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ebomblevel = models.IntegerField(db_column='eBombLevel', blank=True, null=True)  # Field name made lowercase.
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BombEquipmentTypes'


class Bomblevels(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ebomblevel = models.IntegerField(db_column='eBombLevel', blank=True, null=True)  # Field name made lowercase.
    eexplosiontype = models.IntegerField(db_column='eExplosionType', blank=True, null=True)  # Field name made lowercase.
    nlevel = models.IntegerField(db_column='nLevel', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BombLevels'


class Budgettrackervalues(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sbudgetcategories = models.TextField(db_column='sBudgetCategories', blank=True, null=True)  # Field name made lowercase.
    fbudgetvalue = models.FloatField(db_column='fBudgetValue', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BudgetTrackerValues'


class CcArraypurchaseelements(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sattributearray = models.TextField(db_column='sAttributeArray', blank=True, null=True)  # Field name made lowercase.
    ecc_purchaseelement = models.IntegerField(db_column='eCC_PurchaseElement', blank=True, null=True)  # Field name made lowercase.
    naddcost = models.IntegerField(db_column='nAddCost', blank=True, null=True)  # Field name made lowercase.
    ndeletecost = models.IntegerField(db_column='nDeleteCost', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CC_ArrayPurchaseElements'


class CcPurchaseelement(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sattributes = models.TextField(db_column='sAttributes', blank=True, null=True)  # Field name made lowercase.
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    ecc_purchaseelement = models.IntegerField(db_column='eCC_PurchaseElement', blank=True, null=True)  # Field name made lowercase.
    ncost = models.IntegerField(db_column='nCost', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CC_PurchaseElement'


class Ccameramodes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    f16_9backadjust = models.FloatField(db_column='f16_9BackAdjust', blank=True, null=True)  # Field name made lowercase.
    f16_9crouchbackadjust = models.FloatField(db_column='f16_9CrouchBackAdjust', blank=True, null=True)  # Field name made lowercase.
    f16_9crouchheightadjust = models.FloatField(db_column='f16_9CrouchHeightAdjust', blank=True, null=True)  # Field name made lowercase.
    f16_9crouchrightadjust = models.FloatField(db_column='f16_9CrouchRightAdjust', blank=True, null=True)  # Field name made lowercase.
    f16_9crouchrightadjustpitchscalar = models.FloatField(db_column='f16_9CrouchRightAdjustPitchScalar', blank=True, null=True)  # Field name made lowercase.
    f16_9fov = models.FloatField(db_column='f16_9FOV', blank=True, null=True)  # Field name made lowercase.
    f16_9heightadjust = models.FloatField(db_column='f16_9HeightAdjust', blank=True, null=True)  # Field name made lowercase.
    f16_9rightadjust = models.FloatField(db_column='f16_9RightAdjust', blank=True, null=True)  # Field name made lowercase.
    f16_9rightadjustpitchscalar = models.FloatField(db_column='f16_9RightAdjustPitchScalar', blank=True, null=True)  # Field name made lowercase.
    f4_3backadjust = models.FloatField(db_column='f4_3BackAdjust', blank=True, null=True)  # Field name made lowercase.
    f4_3crouchbackadjust = models.FloatField(db_column='f4_3CrouchBackAdjust', blank=True, null=True)  # Field name made lowercase.
    f4_3crouchheightadjust = models.FloatField(db_column='f4_3CrouchHeightAdjust', blank=True, null=True)  # Field name made lowercase.
    f4_3crouchrightadjust = models.FloatField(db_column='f4_3CrouchRightAdjust', blank=True, null=True)  # Field name made lowercase.
    f4_3crouchrightadjustpitchscalar = models.FloatField(db_column='f4_3CrouchRightAdjustPitchScalar', blank=True, null=True)  # Field name made lowercase.
    f4_3fov = models.FloatField(db_column='f4_3FOV', blank=True, null=True)  # Field name made lowercase.
    f4_3heightadjust = models.FloatField(db_column='f4_3HeightAdjust', blank=True, null=True)  # Field name made lowercase.
    f4_3rightadjust = models.FloatField(db_column='f4_3RightAdjust', blank=True, null=True)  # Field name made lowercase.
    f4_3rightadjustpitchscalar = models.FloatField(db_column='f4_3RightAdjustPitchScalar', blank=True, null=True)  # Field name made lowercase.
    fadjustblendspeed = models.FloatField(db_column='fAdjustBlendSpeed', blank=True, null=True)  # Field name made lowercase.
    fcameraoriginlagspeed = models.FloatField(db_column='fCameraOriginLagSpeed', blank=True, null=True)  # Field name made lowercase.
    fcamerarollblendspeed = models.FloatField(db_column='fCameraRollBlendSpeed', blank=True, null=True)  # Field name made lowercase.
    fcamerarolldegrees = models.FloatField(db_column='fCameraRollDegrees', blank=True, null=True)  # Field name made lowercase.
    fcrouchsafelocx = models.FloatField(db_column='fCrouchSafeLocX', blank=True, null=True)  # Field name made lowercase.
    fcrouchsafelocy = models.FloatField(db_column='fCrouchSafeLocY', blank=True, null=True)  # Field name made lowercase.
    fcrouchsafelocz = models.FloatField(db_column='fCrouchSafeLocZ', blank=True, null=True)  # Field name made lowercase.
    ffovblendspeed = models.FloatField(db_column='fFOVBlendSpeed', blank=True, null=True)  # Field name made lowercase.
    fsafelocx = models.FloatField(db_column='fSafeLocX', blank=True, null=True)  # Field name made lowercase.
    fsafelocy = models.FloatField(db_column='fSafeLocY', blank=True, null=True)  # Field name made lowercase.
    fsafelocz = models.FloatField(db_column='fSafeLocZ', blank=True, null=True)  # Field name made lowercase.
    ecameramode = models.IntegerField(db_column='eCameraMode', blank=True, null=True)  # Field name made lowercase.
    bcandolookbehindcam = models.IntegerField(db_column='bCanDoLookBehindCam', blank=True, null=True)  # Field name made lowercase.
    bcrouchenabled = models.IntegerField(db_column='bCrouchEnabled', blank=True, null=True)  # Field name made lowercase.
    busedefaultcameraadjustments = models.IntegerField(db_column='bUseDefaultCameraAdjustments', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CCameraModes'


class CsaAutoroutedata(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ssocketname_0 = models.TextField(db_column='sSocketName_0', blank=True, null=True)  # Field name made lowercase.
    ssocketname_1 = models.TextField(db_column='sSocketName_1', blank=True, null=True)  # Field name made lowercase.
    ssocketname_2 = models.TextField(db_column='sSocketName_2', blank=True, null=True)  # Field name made lowercase.
    ssocketname_3 = models.TextField(db_column='sSocketName_3', blank=True, null=True)  # Field name made lowercase.
    ssocketname_4 = models.TextField(db_column='sSocketName_4', blank=True, null=True)  # Field name made lowercase.
    ecsa_autoroutedata = models.IntegerField(db_column='eCSA_AutoRouteData', blank=True, null=True)  # Field name made lowercase.
    foffsetforward = models.FloatField(db_column='fOffsetForward', blank=True, null=True)  # Field name made lowercase.
    foffsetright = models.FloatField(db_column='fOffsetRight', blank=True, null=True)  # Field name made lowercase.
    ealignmenttype = models.IntegerField(db_column='eAlignmentType', blank=True, null=True)  # Field name made lowercase.
    eautoroutetype = models.IntegerField(db_column='eAutoRouteType', blank=True, null=True)  # Field name made lowercase.
    broutealongnormal = models.IntegerField(db_column='bRouteAlongNormal', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CSA_AutoRouteData'


class CsaEatpropassociation(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eautoroutedata = models.IntegerField(db_column='eAutoRouteData', blank=True, null=True)  # Field name made lowercase.
    ecsa_eatpropassociation = models.IntegerField(db_column='eCSA_EATPropAssociation', blank=True, null=True)  # Field name made lowercase.
    eequipmentanimation = models.IntegerField(db_column='eEquipmentAnimation', blank=True, null=True)  # Field name made lowercase.
    eitemassociation = models.IntegerField(db_column='eItemAssociation', blank=True, null=True)  # Field name made lowercase.
    epropcategory = models.IntegerField(db_column='ePropCategory', blank=True, null=True)  # Field name made lowercase.
    bchecksuseautoroutelocation = models.IntegerField(db_column='bChecksUseAutoRouteLocation', blank=True, null=True)  # Field name made lowercase.
    busesmallcollisionvolume = models.IntegerField(db_column='bUseSmallCollisionVolume', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CSA_EATPropAssociation'


class CsaEatvehicleassociation(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eequipmentanimation = models.IntegerField(db_column='eEquipmentAnimation', blank=True, null=True)  # Field name made lowercase.
    eitemassociation = models.IntegerField(db_column='eItemAssociation', blank=True, null=True)  # Field name made lowercase.
    evehicleanimationtype = models.IntegerField(db_column='eVehicleAnimationType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CSA_EATVehicleAssociation'


class CsaEquipmentanimationtype(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sintroanim = models.TextField(db_column='sIntroAnim', blank=True, null=True)  # Field name made lowercase.
    smainanim1 = models.TextField(db_column='sMainAnim1', blank=True, null=True)  # Field name made lowercase.
    smainanim2 = models.TextField(db_column='sMainAnim2', blank=True, null=True)  # Field name made lowercase.
    smainanim3 = models.TextField(db_column='sMainAnim3', blank=True, null=True)  # Field name made lowercase.
    soutroanim = models.TextField(db_column='sOutroAnim', blank=True, null=True)  # Field name made lowercase.
    svfxclass = models.TextField(db_column='sVFXClass', blank=True, null=True)  # Field name made lowercase.
    ecsa_equipmentanimationtype = models.IntegerField(db_column='eCSA_EquipmentAnimationType', blank=True, null=True)  # Field name made lowercase.
    foutroduration = models.FloatField(db_column='fOutroDuration', blank=True, null=True)  # Field name made lowercase.
    eoutroendpoint = models.IntegerField(db_column='eOutroEndPoint', blank=True, null=True)  # Field name made lowercase.
    bcanmirror = models.IntegerField(db_column='bCanMirror', blank=True, null=True)  # Field name made lowercase.
    buserootmotion = models.IntegerField(db_column='bUseRootMotion', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CSA_EquipmentAnimationType'


class CsaIatstate(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nmaxconcurrentusersperactor = models.IntegerField(db_column='nMaxConcurrentUsersPerActor', blank=True, null=True)  # Field name made lowercase.
    nmaxconcurrentusersperip = models.IntegerField(db_column='nMaxConcurrentUsersPerIP', blank=True, null=True)  # Field name made lowercase.
    ecsa_iatstate = models.IntegerField(db_column='eCSA_IATState', blank=True, null=True)  # Field name made lowercase.
    einteractiveactortype = models.IntegerField(db_column='eInteractiveActorType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CSA_IATState'


class CsaIatstateassociation(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ecsa_iatstateassociation = models.IntegerField(db_column='eCSA_IATStateAssociation', blank=True, null=True)  # Field name made lowercase.
    einputmapping = models.IntegerField(db_column='eInputMapping', blank=True, null=True)  # Field name made lowercase.
    fduration = models.FloatField(db_column='fDuration', blank=True, null=True)  # Field name made lowercase.
    nprioritylayer = models.IntegerField(db_column='nPriorityLayer', blank=True, null=True)  # Field name made lowercase.
    econtextsensitiveaction = models.IntegerField(db_column='eContextSensitiveAction', blank=True, null=True)  # Field name made lowercase.
    ecsa_iatstate = models.IntegerField(db_column='eCSA_IATState', blank=True, null=True)  # Field name made lowercase.
    boverridepriority = models.IntegerField(db_column='bOverridePriority', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CSA_IATStateAssociation'


class CsaInputmapping(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    skeybinding = models.TextField(db_column='sKeyBinding', blank=True, null=True)  # Field name made lowercase.
    ecsa_inputmapping = models.IntegerField(db_column='eCSA_InputMapping', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CSA_InputMapping'


class CsaItemassociation(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ecsa_itemassociation = models.IntegerField(db_column='eCSA_ItemAssociation', blank=True, null=True)  # Field name made lowercase.
    edefaultequipmentanimationtype = models.IntegerField(db_column='eDefaultEquipmentAnimationType', blank=True, null=True)  # Field name made lowercase.
    eequipmenttype = models.IntegerField(db_column='eEquipmentType', blank=True, null=True)  # Field name made lowercase.
    eitemassociationcategory = models.IntegerField(db_column='eItemAssociationCategory', blank=True, null=True)  # Field name made lowercase.
    feffectivenessmodifier = models.FloatField(db_column='fEffectivenessModifier', blank=True, null=True)  # Field name made lowercase.
    econtextsensitiveaction = models.IntegerField(db_column='eContextSensitiveAction', blank=True, null=True)  # Field name made lowercase.
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CSA_ItemAssociation'


class CsaItemassociationcategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    seffect = models.TextField(db_column='sEffect', blank=True, null=True)  # Field name made lowercase.
    ecsa_itemassociationcategory = models.IntegerField(db_column='eCSA_ItemAssociationCategory', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CSA_ItemAssociationCategories'


class CsaTaskitemanimationset(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sanimname = models.TextField(db_column='sAnimName', blank=True, null=True)  # Field name made lowercase.
    ecsa_taskitemanimationset = models.IntegerField(db_column='eCSA_TaskItemAnimationSet', blank=True, null=True)  # Field name made lowercase.
    ecsa = models.IntegerField(db_column='eCSA', blank=True, null=True)  # Field name made lowercase.
    etaskitemsize = models.IntegerField(db_column='eTaskItemSize', blank=True, null=True)  # Field name made lowercase.
    blogical = models.IntegerField(db_column='bLogical', blank=True, null=True)  # Field name made lowercase.
    buseanimduration = models.IntegerField(db_column='bUseAnimDuration', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CSA_TaskItemAnimationSet'


class Cameraconstants(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)  # Field name made lowercase.
    ecameraconstant = models.IntegerField(db_column='eCameraConstant', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CameraConstants'


class Camerahandycampresetexported(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ecamerahandycampreset = models.IntegerField(db_column='eCameraHandyCamPreset', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CameraHandyCamPresetExported'


class Camerahandycampresets(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ecamerahandycampreset = models.IntegerField(db_column='eCameraHandyCamPreset', blank=True, null=True)  # Field name made lowercase.
    einterpolateto = models.IntegerField(db_column='eInterpolateTo', blank=True, null=True)  # Field name made lowercase.
    fchangeinmovementspeed = models.FloatField(db_column='fChangeInMovementSpeed', blank=True, null=True)  # Field name made lowercase.
    fdelaymax = models.FloatField(db_column='fDelayMax', blank=True, null=True)  # Field name made lowercase.
    fdelaymin = models.FloatField(db_column='fDelayMin', blank=True, null=True)  # Field name made lowercase.
    fduration = models.FloatField(db_column='fDuration', blank=True, null=True)  # Field name made lowercase.
    finterpolationspeedmax = models.FloatField(db_column='fInterpolationSpeedMax', blank=True, null=True)  # Field name made lowercase.
    finterpolationspeedmin = models.FloatField(db_column='fInterpolationSpeedMin', blank=True, null=True)  # Field name made lowercase.
    finterptodelay = models.FloatField(db_column='fInterpToDelay', blank=True, null=True)  # Field name made lowercase.
    fmovementspeedmax = models.FloatField(db_column='fMovementSpeedMax', blank=True, null=True)  # Field name made lowercase.
    fmovementspeedmin = models.FloatField(db_column='fMovementSpeedMin', blank=True, null=True)  # Field name made lowercase.
    nmaxdeviationpitch = models.IntegerField(db_column='nMaxDeviationPitch', blank=True, null=True)  # Field name made lowercase.
    nmaxdeviationroll = models.IntegerField(db_column='nMaxDeviationRoll', blank=True, null=True)  # Field name made lowercase.
    nmaxdeviationyaw = models.IntegerField(db_column='nMaxDeviationYaw', blank=True, null=True)  # Field name made lowercase.
    ballowactivation = models.IntegerField(db_column='bAllowActivation', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CameraHandyCamPresets'


class Cameraseatsetups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ecameraseatsetup = models.IntegerField(db_column='eCameraSeatSetup', blank=True, null=True)  # Field name made lowercase.
    ffov = models.FloatField(db_column='fFOV', blank=True, null=True)  # Field name made lowercase.
    fideallocoffset_x = models.FloatField(db_column='fIdealLocOffset_X', blank=True, null=True)  # Field name made lowercase.
    fideallocoffset_y = models.FloatField(db_column='fIdealLocOffset_Y', blank=True, null=True)  # Field name made lowercase.
    fideallocoffset_z = models.FloatField(db_column='fIdealLocOffset_Z', blank=True, null=True)  # Field name made lowercase.
    fworstlocoffset_x = models.FloatField(db_column='fWorstLocOffset_X', blank=True, null=True)  # Field name made lowercase.
    fworstlocoffset_y = models.FloatField(db_column='fWorstLocOffset_Y', blank=True, null=True)  # Field name made lowercase.
    fworstlocoffset_z = models.FloatField(db_column='fWorstLocOffset_Z', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CameraSeatSetups'


class Camerashakepresetexported(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ecamerashakepreset = models.IntegerField(db_column='eCameraShakePreset', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CameraShakePresetExported'


class Camerashakepresets(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ecamerashakepreset = models.IntegerField(db_column='eCameraShakePreset', blank=True, null=True)  # Field name made lowercase.
    fduration = models.FloatField(db_column='fDuration', blank=True, null=True)  # Field name made lowercase.
    ffovamplitude = models.FloatField(db_column='fFOVAmplitude', blank=True, null=True)  # Field name made lowercase.
    ffovfrequency = models.FloatField(db_column='fFOVFrequency', blank=True, null=True)  # Field name made lowercase.
    flocationamplitudex = models.FloatField(db_column='fLocationAmplitudeX', blank=True, null=True)  # Field name made lowercase.
    flocationamplitudey = models.FloatField(db_column='fLocationAmplitudeY', blank=True, null=True)  # Field name made lowercase.
    flocationamplitudez = models.FloatField(db_column='fLocationAmplitudeZ', blank=True, null=True)  # Field name made lowercase.
    flocationfrequencyx = models.FloatField(db_column='fLocationFrequencyX', blank=True, null=True)  # Field name made lowercase.
    flocationfrequencyy = models.FloatField(db_column='fLocationFrequencyY', blank=True, null=True)  # Field name made lowercase.
    flocationfrequencyz = models.FloatField(db_column='fLocationFrequencyZ', blank=True, null=True)  # Field name made lowercase.
    frotationamplitudex = models.FloatField(db_column='fRotationAmplitudeX', blank=True, null=True)  # Field name made lowercase.
    frotationamplitudey = models.FloatField(db_column='fRotationAmplitudeY', blank=True, null=True)  # Field name made lowercase.
    frotationamplitudez = models.FloatField(db_column='fRotationAmplitudeZ', blank=True, null=True)  # Field name made lowercase.
    frotationfrequencyx = models.FloatField(db_column='fRotationFrequencyX', blank=True, null=True)  # Field name made lowercase.
    frotationfrequencyy = models.FloatField(db_column='fRotationFrequencyY', blank=True, null=True)  # Field name made lowercase.
    frotationfrequencyz = models.FloatField(db_column='fRotationFrequencyZ', blank=True, null=True)  # Field name made lowercase.
    brandomstartingfov = models.IntegerField(db_column='bRandomStartingFOV', blank=True, null=True)  # Field name made lowercase.
    brandomstartinglocationx = models.IntegerField(db_column='bRandomStartingLocationX', blank=True, null=True)  # Field name made lowercase.
    brandomstartinglocationy = models.IntegerField(db_column='bRandomStartingLocationY', blank=True, null=True)  # Field name made lowercase.
    brandomstartinglocationz = models.IntegerField(db_column='bRandomStartingLocationZ', blank=True, null=True)  # Field name made lowercase.
    brandomstartingrotationx = models.IntegerField(db_column='bRandomStartingRotationX', blank=True, null=True)  # Field name made lowercase.
    brandomstartingrotationy = models.IntegerField(db_column='bRandomStartingRotationY', blank=True, null=True)  # Field name made lowercase.
    brandomstartingrotationz = models.IntegerField(db_column='bRandomStartingRotationZ', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CameraShakePresets'


class Capacityitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    namount = models.IntegerField(db_column='nAmount', blank=True, null=True)  # Field name made lowercase.
    einventoryitemcategory = models.IntegerField(db_column='eInventoryItemCategory', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CapacityItemTypes'


class Charactercustomisationoverrides(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sfullbodymeshoverridefemale = models.TextField(db_column='sFullBodyMeshOverrideFemale', blank=True, null=True)  # Field name made lowercase.
    sfullbodymeshoverridemale = models.TextField(db_column='sFullBodyMeshOverrideMale', blank=True, null=True)  # Field name made lowercase.
    svfxtemplatefemale = models.TextField(db_column='sVFXTemplateFemale', blank=True, null=True)  # Field name made lowercase.
    svfxtemplatemale = models.TextField(db_column='sVFXTemplateMale', blank=True, null=True)  # Field name made lowercase.
    echaractercustomisationoverride = models.IntegerField(db_column='eCharacterCustomisationOverride', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CharacterCustomisationOverrides'


class Characterinteractionmenu(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sicon = models.TextField(db_column='sIcon', blank=True, null=True)  # Field name made lowercase.
    sid = models.TextField(db_column='sID', blank=True, null=True)  # Field name made lowercase.
    nposition = models.IntegerField(db_column='nPosition', blank=True, null=True)  # Field name made lowercase.
    bsamedistrict = models.IntegerField(db_column='bSameDistrict', blank=True, null=True)  # Field name made lowercase.
    bsamefaction = models.IntegerField(db_column='bSameFaction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CharacterInteractionMenu'


class Charactermodifieritemtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CharacterModifierItemTypes'


class Characterstatuses(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    estatusiconcombo = models.IntegerField(db_column='eStatusIconCombo', blank=True, null=True)  # Field name made lowercase.
    echaracterstatus = models.IntegerField(db_column='eCharacterStatus', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CharacterStatuses'


class Charactervoipstatus(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    evoipiconcombo = models.IntegerField(db_column='eVOIPIconCombo', blank=True, null=True)  # Field name made lowercase.
    echaractervoipstatus = models.IntegerField(db_column='eCharacterVOIPStatus', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CharacterVOIPStatus'


class Chatconstants(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)  # Field name made lowercase.
    echatconstant = models.IntegerField(db_column='eChatConstant', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChatConstants'


class Chatmessagecategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    sfunctionname = models.TextField(db_column='sFunctionName', blank=True, null=True)  # Field name made lowercase.
    ssecondaryslashcommand = models.TextField(db_column='sSecondarySlashCommand', blank=True, null=True)  # Field name made lowercase.
    sslashcommand = models.TextField(db_column='sSlashCommand', blank=True, null=True)  # Field name made lowercase.
    ssyntaxexample = models.TextField(db_column='sSyntaxExample', blank=True, null=True)  # Field name made lowercase.
    stag = models.TextField(db_column='sTag', blank=True, null=True)  # Field name made lowercase.
    efiltercolour = models.IntegerField(db_column='eFilterColour', blank=True, null=True)  # Field name made lowercase.
    echatmessagecategory = models.IntegerField(db_column='eChatMessageCategory', blank=True, null=True)  # Field name made lowercase.
    eworksfromstate = models.IntegerField(db_column='eWorksFromState', blank=True, null=True)  # Field name made lowercase.
    bdisplaynotification = models.IntegerField(db_column='bDisplayNotification', blank=True, null=True)  # Field name made lowercase.
    bhasaudionotification = models.IntegerField(db_column='bHasAudioNotification', blank=True, null=True)  # Field name made lowercase.
    bmodepersists = models.IntegerField(db_column='bModePersists', blank=True, null=True)  # Field name made lowercase.
    bvalidcommand = models.IntegerField(db_column='bValidCommand', blank=True, null=True)  # Field name made lowercase.
    bvalidfilter = models.IntegerField(db_column='bValidFilter', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChatMessageCategories'


class Chattags(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    stagtext = models.TextField(db_column='sTagText', blank=True, null=True)  # Field name made lowercase.
    etagcolour = models.IntegerField(db_column='eTagColour', blank=True, null=True)  # Field name made lowercase.
    npriority = models.IntegerField(db_column='nPriority', blank=True, null=True)  # Field name made lowercase.
    echattag = models.IntegerField(db_column='eChatTag', blank=True, null=True)  # Field name made lowercase.
    erequiredpermission = models.IntegerField(db_column='eRequiredPermission', blank=True, null=True)  # Field name made lowercase.
    bhiddenbydefault = models.IntegerField(db_column='bHiddenByDefault', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChatTags'


class Clanranks(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sname = models.TextField(db_column='sName', blank=True, null=True)  # Field name made lowercase.
    eicon = models.IntegerField(db_column='eIcon', blank=True, null=True)  # Field name made lowercase.
    eclanrank = models.IntegerField(db_column='eClanRank', blank=True, null=True)  # Field name made lowercase.
    bassignrank = models.IntegerField(db_column='bAssignRank', blank=True, null=True)  # Field name made lowercase.
    bclanchatlisten = models.IntegerField(db_column='bClanChatListen', blank=True, null=True)  # Field name made lowercase.
    bclanchatspeak = models.IntegerField(db_column='bClanChatSpeak', blank=True, null=True)  # Field name made lowercase.
    bcontact = models.IntegerField(db_column='bContact', blank=True, null=True)  # Field name made lowercase.
    beditclanbio = models.IntegerField(db_column='bEditClanBio', blank=True, null=True)  # Field name made lowercase.
    beditclaninformation = models.IntegerField(db_column='bEditClanInformation', blank=True, null=True)  # Field name made lowercase.
    beditclansymbol = models.IntegerField(db_column='bEditClanSymbol', blank=True, null=True)  # Field name made lowercase.
    beditclantheme = models.IntegerField(db_column='bEditClanTheme', blank=True, null=True)  # Field name made lowercase.
    beditmotd = models.IntegerField(db_column='bEditMotd', blank=True, null=True)  # Field name made lowercase.
    beditprivatenote = models.IntegerField(db_column='bEditPrivateNote', blank=True, null=True)  # Field name made lowercase.
    beditpublicnote = models.IntegerField(db_column='bEditPublicNote', blank=True, null=True)  # Field name made lowercase.
    binvitemember = models.IntegerField(db_column='bInviteMember', blank=True, null=True)  # Field name made lowercase.
    bofficerchatlisten = models.IntegerField(db_column='bOfficerChatListen', blank=True, null=True)  # Field name made lowercase.
    bofficerchatspeak = models.IntegerField(db_column='bOfficerChatSpeak', blank=True, null=True)  # Field name made lowercase.
    bremovemember = models.IntegerField(db_column='bRemoveMember', blank=True, null=True)  # Field name made lowercase.
    breuseme = models.IntegerField(db_column='bReuseMe', blank=True, null=True)  # Field name made lowercase.
    bviewprivatenote = models.IntegerField(db_column='bViewPrivateNote', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClanRanks'


class Clothingitemcategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eclothingitemcategory = models.IntegerField(db_column='eClothingItemCategory', blank=True, null=True)  # Field name made lowercase.
    einventoryiteminfracategory = models.IntegerField(db_column='eInventoryItemInfraCategory', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClothingItemCategories'


class Clothingitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    sresource = models.TextField(db_column='sResource', blank=True, null=True)  # Field name made lowercase.
    egolempart = models.IntegerField(db_column='eGolemPart', blank=True, null=True)  # Field name made lowercase.
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    nreeditfee = models.IntegerField(db_column='nReeditFee', blank=True, null=True)  # Field name made lowercase.
    bfemale = models.IntegerField(db_column='bFemale', blank=True, null=True)  # Field name made lowercase.
    bmale = models.IntegerField(db_column='bMale', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClothingItemTypes'


class Consolecommands(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    sfunctionname = models.TextField(db_column='sFunctionName', blank=True, null=True)  # Field name made lowercase.
    sslashcommand = models.TextField(db_column='sSlashCommand', blank=True, null=True)  # Field name made lowercase.
    ssyntaxexample = models.TextField(db_column='sSyntaxExample', blank=True, null=True)  # Field name made lowercase.
    econsolecommand = models.IntegerField(db_column='eConsoleCommand', blank=True, null=True)  # Field name made lowercase.
    nmaxargcount = models.IntegerField(db_column='nMaxArgCount', blank=True, null=True)  # Field name made lowercase.
    nminargcount = models.IntegerField(db_column='nMinArgCount', blank=True, null=True)  # Field name made lowercase.
    ecommandtype = models.IntegerField(db_column='eCommandType', blank=True, null=True)  # Field name made lowercase.
    epermissionrequired = models.IntegerField(db_column='ePermissionRequired', blank=True, null=True)  # Field name made lowercase.
    eworksfromstate = models.IntegerField(db_column='eWorksFromState', blank=True, null=True)  # Field name made lowercase.
    benabled = models.IntegerField(db_column='bEnabled', blank=True, null=True)  # Field name made lowercase.
    bworksineditors = models.IntegerField(db_column='bWorksInEditors', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConsoleCommands'


class Contactlevels(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    srewardmailbody = models.TextField(db_column='sRewardMailBody', blank=True, null=True)  # Field name made lowercase.
    srewardmailsubject = models.TextField(db_column='sRewardMailSubject', blank=True, null=True)  # Field name made lowercase.
    econtact = models.IntegerField(db_column='eContact', blank=True, null=True)  # Field name made lowercase.
    econtactlevel = models.IntegerField(db_column='eContactLevel', blank=True, null=True)  # Field name made lowercase.
    erewardpackage = models.IntegerField(db_column='eRewardPackage', blank=True, null=True)  # Field name made lowercase.
    forganisationrewardmultiplier = models.FloatField(db_column='fOrganisationRewardMultiplier', blank=True, null=True)  # Field name made lowercase.
    ncontactscore = models.IntegerField(db_column='nContactScore', blank=True, null=True)  # Field name made lowercase.
    nlevel = models.IntegerField(db_column='nLevel', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    nstandingthreshold = models.IntegerField(db_column='nStandingThreshold', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactLevels'


class Contactreferrals(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    econtactlevel = models.IntegerField(db_column='eContactLevel', blank=True, null=True)  # Field name made lowercase.
    eunlockedcontact = models.IntegerField(db_column='eUnlockedContact', blank=True, null=True)  # Field name made lowercase.
    npartialunlockindex = models.IntegerField(db_column='nPartialUnlockIndex', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactReferrals'


class Contactrotationanims(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sleftrotationanim = models.TextField(db_column='sLeftRotationAnim', blank=True, null=True)  # Field name made lowercase.
    srightrotationanim = models.TextField(db_column='sRightRotationAnim', blank=True, null=True)  # Field name made lowercase.
    econtactrotationanim = models.IntegerField(db_column='eContactRotationAnim', blank=True, null=True)  # Field name made lowercase.
    nangle = models.IntegerField(db_column='nAngle', blank=True, null=True)  # Field name made lowercase.
    nanglecutoff = models.IntegerField(db_column='nAngleCutoff', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactRotationAnims'


class Contacts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nsecondarykey = models.TextField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    saudiotype = models.TextField(db_column='sAudioType', blank=True, null=True)  # Field name made lowercase.
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    stitle = models.TextField(db_column='sTitle', blank=True, null=True)  # Field name made lowercase.
    econtact = models.IntegerField(db_column='eContact', blank=True, null=True)  # Field name made lowercase.
    econtacticon = models.IntegerField(db_column='eContactIcon', blank=True, null=True)  # Field name made lowercase.
    edistrict = models.IntegerField(db_column='eDistrict', blank=True, null=True)  # Field name made lowercase.
    emissionpurpose = models.IntegerField(db_column='eMissionPurpose', blank=True, null=True)  # Field name made lowercase.
    epurchaseshoptype = models.IntegerField(db_column='ePurchaseShopType', blank=True, null=True)  # Field name made lowercase.
    npartialunlocks = models.IntegerField(db_column='nPartialUnlocks', blank=True, null=True)  # Field name made lowercase.
    econtacttype = models.IntegerField(db_column='eContactType', blank=True, null=True)  # Field name made lowercase.
    edealsinrewardtokenitems = models.IntegerField(db_column='eDealsInRewardTokenItems', blank=True, null=True)  # Field name made lowercase.
    eorganisation = models.IntegerField(db_column='eOrganisation', blank=True, null=True)  # Field name made lowercase.
    bbuyscrossorganisation = models.IntegerField(db_column='bBuysCrossOrganisation', blank=True, null=True)  # Field name made lowercase.
    bdealsincommonitems = models.IntegerField(db_column='bDealsInCommonItems', blank=True, null=True)  # Field name made lowercase.
    bdefaultassets = models.IntegerField(db_column='bDefaultAssets', blank=True, null=True)  # Field name made lowercase.
    bexcludefromtrackedactivities = models.IntegerField(db_column='bExcludeFromTrackedActivities', blank=True, null=True)  # Field name made lowercase.
    bfemale = models.IntegerField(db_column='bFemale', blank=True, null=True)  # Field name made lowercase.
    bhidden = models.IntegerField(db_column='bHidden', blank=True, null=True)  # Field name made lowercase.
    binitiallyunlocked = models.IntegerField(db_column='bInitiallyUnlocked', blank=True, null=True)  # Field name made lowercase.
    bleftalignname = models.IntegerField(db_column='bLeftAlignName', blank=True, null=True)  # Field name made lowercase.
    btest = models.IntegerField(db_column='bTest', blank=True, null=True)  # Field name made lowercase.
    btutor = models.IntegerField(db_column='bTutor', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contacts'


class Contextsensitiveaction(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    edefaultautoroutedata = models.IntegerField(db_column='eDefaultAutoRouteData', blank=True, null=True)  # Field name made lowercase.
    faimdot = models.FloatField(db_column='fAimDot', blank=True, null=True)  # Field name made lowercase.
    fcameradirectionaimdotweightingscalar = models.FloatField(db_column='fCameraDirectionAimDotWeightingScalar', blank=True, null=True)  # Field name made lowercase.
    fdistanceweightingscalar = models.FloatField(db_column='fDistanceWeightingScalar', blank=True, null=True)  # Field name made lowercase.
    fhorizontalserverdistanceerrormargin = models.FloatField(db_column='fHorizontalServerDistanceErrorMargin', blank=True, null=True)  # Field name made lowercase.
    fhudhintdistance = models.FloatField(db_column='fHUDHintDistance', blank=True, null=True)  # Field name made lowercase.
    finteractiondistance = models.FloatField(db_column='fInteractionDistance', blank=True, null=True)  # Field name made lowercase.
    fpawndirectionaimdotweightingscalar = models.FloatField(db_column='fPawnDirectionAimDotWeightingScalar', blank=True, null=True)  # Field name made lowercase.
    fverticalinteractiondistance = models.FloatField(db_column='fVerticalInteractionDistance', blank=True, null=True)  # Field name made lowercase.
    fverticalserverdistanceerrormargin = models.FloatField(db_column='fVerticalServerDistanceErrorMargin', blank=True, null=True)  # Field name made lowercase.
    nprioritylayer = models.IntegerField(db_column='nPriorityLayer', blank=True, null=True)  # Field name made lowercase.
    econtextsensitiveaction = models.IntegerField(db_column='eContextSensitiveAction', blank=True, null=True)  # Field name made lowercase.
    edefaultalignmenttype = models.IntegerField(db_column='eDefaultAlignmentType', blank=True, null=True)  # Field name made lowercase.
    elinechecktype = models.IntegerField(db_column='eLineCheckType', blank=True, null=True)  # Field name made lowercase.
    baimcheck = models.IntegerField(db_column='bAimCheck', blank=True, null=True)  # Field name made lowercase.
    ballowwhilefalling = models.IntegerField(db_column='bAllowWhileFalling', blank=True, null=True)  # Field name made lowercase.
    bchecksuseautoroutedata = models.IntegerField(db_column='bChecksUseAutoRouteData', blank=True, null=True)  # Field name made lowercase.
    bdefaultlinecheck = models.IntegerField(db_column='bDefaultLineCheck', blank=True, null=True)  # Field name made lowercase.
    bdistancecheck = models.IntegerField(db_column='bDistanceCheck', blank=True, null=True)  # Field name made lowercase.
    bisanimationdrivenaction = models.IntegerField(db_column='bIsAnimationDrivenAction', blank=True, null=True)  # Field name made lowercase.
    bistargetedcsa = models.IntegerField(db_column='bIsTargetedCSA', blank=True, null=True)  # Field name made lowercase.
    blargetaskitem = models.IntegerField(db_column='bLargeTaskItem', blank=True, null=True)  # Field name made lowercase.
    bmediumtaskitem = models.IntegerField(db_column='bMediumTaskItem', blank=True, null=True)  # Field name made lowercase.
    bsingleinteractionpoint = models.IntegerField(db_column='bSingleInteractionPoint', blank=True, null=True)  # Field name made lowercase.
    bsingleprogressbar = models.IntegerField(db_column='bSingleProgressBar', blank=True, null=True)  # Field name made lowercase.
    bsmalltaskitem = models.IntegerField(db_column='bSmallTaskItem', blank=True, null=True)  # Field name made lowercase.
    bsprintpriority = models.IntegerField(db_column='bSprintPriority', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContextSensitiveAction'


class Contextsensitiveactionbase(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    ebegincsatutorialtrigger = models.IntegerField(db_column='eBeginCSATutorialTrigger', blank=True, null=True)  # Field name made lowercase.
    eendcsatutorialtrigger = models.IntegerField(db_column='eEndCSATutorialTrigger', blank=True, null=True)  # Field name made lowercase.
    eanimtype = models.IntegerField(db_column='eAnimType', blank=True, null=True)  # Field name made lowercase.
    econtextsensitiveactionbase = models.IntegerField(db_column='eContextSensitiveActionBase', blank=True, null=True)  # Field name made lowercase.
    einputtype = models.IntegerField(db_column='eInputType', blank=True, null=True)  # Field name made lowercase.
    eopposingcsa = models.IntegerField(db_column='eOpposingCSA', blank=True, null=True)  # Field name made lowercase.
    bcancelscrouch = models.IntegerField(db_column='bCancelsCrouch', blank=True, null=True)  # Field name made lowercase.
    bcanresume = models.IntegerField(db_column='bCanResume', blank=True, null=True)  # Field name made lowercase.
    bconsideractive = models.IntegerField(db_column='bConsiderActive', blank=True, null=True)  # Field name made lowercase.
    bindefiniteduration = models.IntegerField(db_column='bIndefiniteDuration', blank=True, null=True)  # Field name made lowercase.
    binterruptinventory = models.IntegerField(db_column='bInterruptInventory', blank=True, null=True)  # Field name made lowercase.
    binvoked = models.IntegerField(db_column='bInvoked', blank=True, null=True)  # Field name made lowercase.
    bmissioncsa = models.IntegerField(db_column='bMissionCSA', blank=True, null=True)  # Field name made lowercase.
    bnohideweapon = models.IntegerField(db_column='bNoHideWeapon', blank=True, null=True)  # Field name made lowercase.
    bprogressbar = models.IntegerField(db_column='bProgressBar', blank=True, null=True)  # Field name made lowercase.
    bsmalltargetvolume = models.IntegerField(db_column='bSmallTargetVolume', blank=True, null=True)  # Field name made lowercase.
    btimedduration = models.IntegerField(db_column='bTimedDuration', blank=True, null=True)  # Field name made lowercase.
    bvolumecsa = models.IntegerField(db_column='bVolumeCSA', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContextSensitiveActionBase'


class Coopcheckpointmultipliers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fmultiplier = models.FloatField(db_column='fMultiplier', blank=True, null=True)  # Field name made lowercase.
    ncoopcheckpointmultipliers = models.IntegerField(db_column='nCoopCheckpointMultipliers', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CoopCheckpointMultipliers'


class Customisedassetpriorities(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fpriority = models.FloatField(db_column='fPriority', blank=True, null=True)  # Field name made lowercase.
    ecustomisedassetpriority = models.IntegerField(db_column='eCustomisedAssetPriority', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomisedAssetPriorities'


class Dailyactivities(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    edailyactivity = models.IntegerField(db_column='eDailyActivity', blank=True, null=True)  # Field name made lowercase.
    eprobability = models.IntegerField(db_column='eProbability', blank=True, null=True)  # Field name made lowercase.
    eredeemablereward = models.IntegerField(db_column='eRedeemableReward', blank=True, null=True)  # Field name made lowercase.
    etrackedactivity = models.IntegerField(db_column='eTrackedActivity', blank=True, null=True)  # Field name made lowercase.
    nrefreshtime = models.IntegerField(db_column='nRefreshTime', blank=True, null=True)  # Field name made lowercase.
    nrequirement = models.IntegerField(db_column='nRequirement', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DailyActivities'


class Dailyactivitycontacts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    shuddescription = models.TextField(db_column='sHUDDescription', blank=True, null=True)  # Field name made lowercase.
    slongdescription = models.TextField(db_column='sLongDescription', blank=True, null=True)  # Field name made lowercase.
    stitle = models.TextField(db_column='sTitle', blank=True, null=True)  # Field name made lowercase.
    econtactlevel = models.IntegerField(db_column='eContactLevel', blank=True, null=True)  # Field name made lowercase.
    edailyactivity = models.IntegerField(db_column='eDailyActivity', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DailyActivityContacts'


class Damageableattachmentvisuals(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eitemattachmentvisual = models.IntegerField(db_column='eItemAttachmentVisual', blank=True, null=True)  # Field name made lowercase.
    fcollisionarc = models.FloatField(db_column='fCollisionArc', blank=True, null=True)  # Field name made lowercase.
    fcollisioncrouchheightoffset = models.FloatField(db_column='fCollisionCrouchHeightOffset', blank=True, null=True)  # Field name made lowercase.
    fcollisionheightbottom = models.FloatField(db_column='fCollisionHeightBottom', blank=True, null=True)  # Field name made lowercase.
    fcollisionheighttop = models.FloatField(db_column='fCollisionHeightTop', blank=True, null=True)  # Field name made lowercase.
    bisrightsidecarry = models.IntegerField(db_column='bIsRightSideCarry', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DamageableAttachmentVisuals'


class Defaultcustomcolours(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    edefaultcustomcolour = models.IntegerField(db_column='eDefaultCustomColour', blank=True, null=True)  # Field name made lowercase.
    nhue = models.IntegerField(db_column='nHue', blank=True, null=True)  # Field name made lowercase.
    nlum = models.IntegerField(db_column='nLum', blank=True, null=True)  # Field name made lowercase.
    nsat = models.IntegerField(db_column='nSat', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DefaultCustomColours'


class Defaultoutfititems(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eclothingitemtype = models.IntegerField(db_column='eClothingItemType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DefaultOutfitItems'


class DefaultTodBehaviours(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etod_event = models.IntegerField(db_column='eTOD_Event', blank=True, null=True)  # Field name made lowercase.
    flikelihood = models.FloatField(db_column='fLikelihood', blank=True, null=True)  # Field name made lowercase.
    ereaction = models.IntegerField(db_column='eReaction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Default_TOD_Behaviours'


class Designerconstants(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DesignerConstants'


class Designerconstants2(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    scomment = models.TextField(db_column='sComment', blank=True, null=True)  # Field name made lowercase.
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)  # Field name made lowercase.
    edesignerconstant2 = models.IntegerField(db_column='eDesignerConstant2', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DesignerConstants2'


class Displaypoint(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nsecondarykey = models.TextField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    sobtainedby = models.TextField(db_column='sObtainedBy', blank=True, null=True)  # Field name made lowercase.
    sscreenshot = models.TextField(db_column='sScreenShot', blank=True, null=True)  # Field name made lowercase.
    sshorttitle = models.TextField(db_column='sShortTitle', blank=True, null=True)  # Field name made lowercase.
    stitle = models.TextField(db_column='sTitle', blank=True, null=True)  # Field name made lowercase.
    edisplaypoint = models.IntegerField(db_column='eDisplayPoint', blank=True, null=True)  # Field name made lowercase.
    edistrict = models.IntegerField(db_column='eDistrict', blank=True, null=True)  # Field name made lowercase.
    eactivationtype = models.IntegerField(db_column='eActivationType', blank=True, null=True)  # Field name made lowercase.
    etype = models.IntegerField(db_column='eType', blank=True, null=True)  # Field name made lowercase.
    bcriminal = models.IntegerField(db_column='bCriminal', blank=True, null=True)  # Field name made lowercase.
    benforcer = models.IntegerField(db_column='bEnforcer', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DisplayPoint'


class Districtblocks(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    edistrict = models.IntegerField(db_column='eDistrict', blank=True, null=True)  # Field name made lowercase.
    edistrictblock = models.IntegerField(db_column='eDistrictBlock', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    themes_0 = models.IntegerField(db_column='Themes_0', blank=True, null=True)  # Field name made lowercase.
    themes_1 = models.IntegerField(db_column='Themes_1', blank=True, null=True)  # Field name made lowercase.
    themes_2 = models.IntegerField(db_column='Themes_2', blank=True, null=True)  # Field name made lowercase.
    themes_3 = models.IntegerField(db_column='Themes_3', blank=True, null=True)  # Field name made lowercase.
    themes_4 = models.IntegerField(db_column='Themes_4', blank=True, null=True)  # Field name made lowercase.
    themes_5 = models.IntegerField(db_column='Themes_5', blank=True, null=True)  # Field name made lowercase.
    themes_6 = models.IntegerField(db_column='Themes_6', blank=True, null=True)  # Field name made lowercase.
    themes_7 = models.IntegerField(db_column='Themes_7', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DistrictBlocks'


class Districtinstancetype(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    edistrict = models.IntegerField(db_column='eDistrict', blank=True, null=True)  # Field name made lowercase.
    edistrictinstancetype = models.IntegerField(db_column='eDistrictInstanceType', blank=True, null=True)  # Field name made lowercase.
    edistrictlanguage = models.IntegerField(db_column='eDistrictLanguage', blank=True, null=True)  # Field name made lowercase.
    edistrictrating = models.IntegerField(db_column='eDistrictRating', blank=True, null=True)  # Field name made lowercase.
    edistrictruleset = models.IntegerField(db_column='eDistrictRuleSet', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DistrictInstanceType'


class Districtlanguage(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    slanguageshortname = models.TextField(db_column='sLanguageShortName', blank=True, null=True)  # Field name made lowercase.
    slocalisationini = models.TextField(db_column='sLocalisationINI', blank=True, null=True)  # Field name made lowercase.
    edistrictlanguage = models.IntegerField(db_column='eDistrictLanguage', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DistrictLanguage'


class Districtrating(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    edistrictrating = models.IntegerField(db_column='eDistrictRating', blank=True, null=True)  # Field name made lowercase.
    nmaxrating = models.IntegerField(db_column='nMaxRating', blank=True, null=True)  # Field name made lowercase.
    nminrating = models.IntegerField(db_column='nMinRating', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DistrictRating'


class Districtrulesets(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    edistrictruleset = models.IntegerField(db_column='eDistrictRuleSet', blank=True, null=True)  # Field name made lowercase.
    emissiontypefilter_0 = models.IntegerField(db_column='eMissionTypeFilter_0', blank=True, null=True)  # Field name made lowercase.
    emissiontypefilter_1 = models.IntegerField(db_column='eMissionTypeFilter_1', blank=True, null=True)  # Field name made lowercase.
    fmaximumtoohightime = models.FloatField(db_column='fMaximumTooHighTime', blank=True, null=True)  # Field name made lowercase.
    freticuletargetingdistance = models.FloatField(db_column='fReticuleTargetingDistance', blank=True, null=True)  # Field name made lowercase.
    fscoreunopposedmultiplier = models.FloatField(db_column='fScoreUnopposedMultiplier', blank=True, null=True)  # Field name made lowercase.
    fwscharinfodistance = models.FloatField(db_column='fWSCharInfoDistance', blank=True, null=True)  # Field name made lowercase.
    nmissiondelay = models.IntegerField(db_column='nMissionDelay', blank=True, null=True)  # Field name made lowercase.
    nnewmissioncooldowntimer = models.IntegerField(db_column='nNewMissionCooldownTimer', blank=True, null=True)  # Field name made lowercase.
    echaractercollideswithcharacter = models.IntegerField(db_column='eCharacterCollidesWithCharacter', blank=True, null=True)  # Field name made lowercase.
    edistricttypeinfo = models.IntegerField(db_column='eDistrictTypeInfo', blank=True, null=True)  # Field name made lowercase.
    eheatfunctionality = models.IntegerField(db_column='eHeatFunctionality', blank=True, null=True)  # Field name made lowercase.
    epvpdamage = models.IntegerField(db_column='ePvPDamage', blank=True, null=True)  # Field name made lowercase.
    etutorialbypassbehaviour = models.IntegerField(db_column='eTutorialBypassBehaviour', blank=True, null=True)  # Field name made lowercase.
    eweapontypeset = models.IntegerField(db_column='eWeaponTypeSet', blank=True, null=True)  # Field name made lowercase.
    ewitnessingfunctionality = models.IntegerField(db_column='eWitnessingFunctionality', blank=True, null=True)  # Field name made lowercase.
    ewitnessingmissionsystem = models.IntegerField(db_column='eWitnessingMissionSystem', blank=True, null=True)  # Field name made lowercase.
    ballowbackupcall = models.IntegerField(db_column='bAllowBackupCall', blank=True, null=True)  # Field name made lowercase.
    ballowfnmods = models.IntegerField(db_column='bAllowFnMods', blank=True, null=True)  # Field name made lowercase.
    balwaysaccessinventory = models.IntegerField(db_column='bAlwaysAccessInventory', blank=True, null=True)  # Field name made lowercase.
    bbountiesavailable = models.IntegerField(db_column='bBountiesAvailable', blank=True, null=True)  # Field name made lowercase.
    bcontactreferralson = models.IntegerField(db_column='bContactReferralsOn', blank=True, null=True)  # Field name made lowercase.
    bcustomisationlimiter = models.IntegerField(db_column='bCustomisationLimiter', blank=True, null=True)  # Field name made lowercase.
    bdistinguishfactionnamecolours = models.IntegerField(db_column='bDistinguishFactionNameColours', blank=True, null=True)  # Field name made lowercase.
    bdobuildingchecks = models.IntegerField(db_column='bDoBuildingChecks', blank=True, null=True)  # Field name made lowercase.
    bdropweapons = models.IntegerField(db_column='bDropWeapons', blank=True, null=True)  # Field name made lowercase.
    bhudshowradarpings = models.IntegerField(db_column='bHUDShowRadarPings', blank=True, null=True)  # Field name made lowercase.
    bincompletetutorialavailable = models.IntegerField(db_column='bIncompleteTutorialAvailable', blank=True, null=True)  # Field name made lowercase.
    bminigamesavailable = models.IntegerField(db_column='bMinigamesAvailable', blank=True, null=True)  # Field name made lowercase.
    bmissionoffers = models.IntegerField(db_column='bMissionOffers', blank=True, null=True)  # Field name made lowercase.
    bnoskillrating = models.IntegerField(db_column='bNoSkillRating', blank=True, null=True)  # Field name made lowercase.
    bofferautogroup = models.IntegerField(db_column='bOfferAutoGroup', blank=True, null=True)  # Field name made lowercase.
    brelease = models.IntegerField(db_column='bRelease', blank=True, null=True)  # Field name made lowercase.
    bshowthreatandrank = models.IntegerField(db_column='bShowThreatAndRank', blank=True, null=True)  # Field name made lowercase.
    busemasterspawnzoneonly = models.IntegerField(db_column='bUseMasterSpawnZoneOnly', blank=True, null=True)  # Field name made lowercase.
    bwscharinfousesradarpings = models.IntegerField(db_column='bWSCharInfoUsesRadarPings', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DistrictRuleSets'


class Districttypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    edistricttype = models.IntegerField(db_column='eDistrictType', blank=True, null=True)  # Field name made lowercase.
    efactionallowed = models.IntegerField(db_column='eFactionAllowed', blank=True, null=True)  # Field name made lowercase.
    bissocial = models.IntegerField(db_column='bIsSocial', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DistrictTypes'


class Districts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    saudiobanks = models.TextField(db_column='sAudioBanks', blank=True, null=True)  # Field name made lowercase.
    saudioreflectiondata = models.TextField(db_column='sAudioReflectionData', blank=True, null=True)  # Field name made lowercase.
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    sdiffusetexture = models.TextField(db_column='sDiffuseTexture', blank=True, null=True)  # Field name made lowercase.
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    sdistancefieldtexture = models.TextField(db_column='sDistanceFieldTexture', blank=True, null=True)  # Field name made lowercase.
    sdistrictmap = models.TextField(db_column='sDistrictMap', blank=True, null=True)  # Field name made lowercase.
    eawesomeplayerdetectionrules = models.IntegerField(db_column='eAwesomePlayerDetectionRules', blank=True, null=True)  # Field name made lowercase.
    ecriminalorganisationcontact = models.IntegerField(db_column='eCriminalOrganisationContact', blank=True, null=True)  # Field name made lowercase.
    edefaultdistrictinstancetype = models.IntegerField(db_column='eDefaultDistrictInstanceType', blank=True, null=True)  # Field name made lowercase.
    edistrict = models.IntegerField(db_column='eDistrict', blank=True, null=True)  # Field name made lowercase.
    eenforcerorganisationcontact = models.IntegerField(db_column='eEnforcerOrganisationContact', blank=True, null=True)  # Field name made lowercase.
    etutorialdistrictinstancetype = models.IntegerField(db_column='eTutorialDistrictInstanceType', blank=True, null=True)  # Field name made lowercase.
    fmaxsafeheight = models.FloatField(db_column='fMaxSafeHeight', blank=True, null=True)  # Field name made lowercase.
    fnmaxdistancetopedestriandestroynode = models.FloatField(db_column='fnMaxDistanceToPedestrianDestroyNode', blank=True, null=True)  # Field name made lowercase.
    fuiinactivitytimeout = models.FloatField(db_column='fUIInactivityTimeout', blank=True, null=True)  # Field name made lowercase.
    ncentrex = models.IntegerField(db_column='nCentreX', blank=True, null=True)  # Field name made lowercase.
    ncentrey = models.IntegerField(db_column='nCentreY', blank=True, null=True)  # Field name made lowercase.
    ndiameter = models.IntegerField(db_column='nDiameter', blank=True, null=True)  # Field name made lowercase.
    nnumcollectables = models.IntegerField(db_column='nNumCollectables', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    edistricttype = models.IntegerField(db_column='eDistrictType', blank=True, null=True)  # Field name made lowercase.
    espawnvariable = models.IntegerField(db_column='eSpawnVariable', blank=True, null=True)  # Field name made lowercase.
    breleasedistrict = models.IntegerField(db_column='bReleaseDistrict', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Districts'


class Dynamicmenuentries(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplaypicture = models.TextField(db_column='sDisplayPicture', blank=True, null=True)  # Field name made lowercase.
    sdisplaytext = models.TextField(db_column='sDisplayText', blank=True, null=True)  # Field name made lowercase.
    slistid = models.TextField(db_column='sListID', blank=True, null=True)  # Field name made lowercase.
    sremoteevent = models.TextField(db_column='sRemoteEvent', blank=True, null=True)  # Field name made lowercase.
    swwiseswitch = models.TextField(db_column='sWwiseSwitch', blank=True, null=True)  # Field name made lowercase.
    edynamicmenuentry = models.IntegerField(db_column='eDynamicMenuEntry', blank=True, null=True)  # Field name made lowercase.
    ecustomisationmode = models.IntegerField(db_column='eCustomisationMode', blank=True, null=True)  # Field name made lowercase.
    egender = models.IntegerField(db_column='eGender', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DynamicMenuEntries'


class Emotecommands(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    spackageref = models.TextField(db_column='sPackageRef', blank=True, null=True)  # Field name made lowercase.
    sslashcommand = models.TextField(db_column='sSlashCommand', blank=True, null=True)  # Field name made lowercase.
    eemotecommand = models.IntegerField(db_column='eEmoteCommand', blank=True, null=True)  # Field name made lowercase.
    bkickcheckenabled = models.IntegerField(db_column='bKickCheckEnabled', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmoteCommands'


class Encumbrances(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nuiencumbrancelevel = models.IntegerField(db_column='nUIEncumbranceLevel', blank=True, null=True)  # Field name made lowercase.
    eencumbrance = models.IntegerField(db_column='eEncumbrance', blank=True, null=True)  # Field name made lowercase.
    bcancrouchmove = models.IntegerField(db_column='bCanCrouchMove', blank=True, null=True)  # Field name made lowercase.
    bcanjump = models.IntegerField(db_column='bCanJump', blank=True, null=True)  # Field name made lowercase.
    bcanrun = models.IntegerField(db_column='bCanRun', blank=True, null=True)  # Field name made lowercase.
    bcansprint = models.IntegerField(db_column='bCanSprint', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Encumbrances'


class Equipmentcategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    eequipmentcategory = models.IntegerField(db_column='eEquipmentCategory', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EquipmentCategories'


class Equipmenttypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    eequipmentcategory = models.IntegerField(db_column='eEquipmentCategory', blank=True, null=True)  # Field name made lowercase.
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    eitemattachment = models.IntegerField(db_column='eItemAttachment', blank=True, null=True)  # Field name made lowercase.
    fdurationofuse = models.IntegerField(db_column='fDurationOfUse', blank=True, null=True)  # Field name made lowercase.
    ngradeordinal = models.IntegerField(db_column='nGradeOrdinal', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EquipmentTypes'


class Errorcode(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ndummy = models.IntegerField(db_column='nDummy', blank=True, null=True)  # Field name made lowercase.
    eerrorcode = models.IntegerField(db_column='eErrorCode', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ErrorCode'


class Explosions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    saudiotype = models.TextField(db_column='sAudioType', blank=True, null=True)  # Field name made lowercase.
    svfxasset = models.TextField(db_column='sVFXAsset', blank=True, null=True)  # Field name made lowercase.
    svfxasset_airburst = models.TextField(db_column='sVFXAsset_Airburst', blank=True, null=True)  # Field name made lowercase.
    ecamerashake = models.IntegerField(db_column='eCameraShake', blank=True, null=True)  # Field name made lowercase.
    eexplosion = models.IntegerField(db_column='eExplosion', blank=True, null=True)  # Field name made lowercase.
    fexplosionradius = models.FloatField(db_column='fExplosionRadius', blank=True, null=True)  # Field name made lowercase.
    fgroundzeroradius = models.FloatField(db_column='fGroundZeroRadius', blank=True, null=True)  # Field name made lowercase.
    fharddamagemodifier = models.FloatField(db_column='fHardDamageModifier', blank=True, null=True)  # Field name made lowercase.
    fimpulsezmax = models.FloatField(db_column='fImpulseZMax', blank=True, null=True)  # Field name made lowercase.
    fimpulsezmin = models.FloatField(db_column='fImpulseZMin', blank=True, null=True)  # Field name made lowercase.
    flifetimemaxdamagetime = models.FloatField(db_column='fLifetimeMaxDamageTime', blank=True, null=True)  # Field name made lowercase.
    flifetimemindamagepercentage = models.FloatField(db_column='fLifetimeMinDamagePercentage', blank=True, null=True)  # Field name made lowercase.
    fminimumdamagepercentage = models.FloatField(db_column='fMinimumDamagePercentage', blank=True, null=True)  # Field name made lowercase.
    fragdollradialimpulse = models.FloatField(db_column='fRagdollRadialImpulse', blank=True, null=True)  # Field name made lowercase.
    fsoftdamagemodifier = models.FloatField(db_column='fSoftDamageModifier', blank=True, null=True)  # Field name made lowercase.
    ndamage = models.IntegerField(db_column='nDamage', blank=True, null=True)  # Field name made lowercase.
    nstundamage = models.IntegerField(db_column='nStunDamage', blank=True, null=True)  # Field name made lowercase.
    enpcworldevent = models.IntegerField(db_column='eNPCWorldEvent', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Explosions'


class Fxmaterialimpacts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sexplosiveimpactvfx = models.TextField(db_column='sExplosiveImpactVFX', blank=True, null=True)  # Field name made lowercase.
    sheavyexitvfx = models.TextField(db_column='sHeavyExitVFX', blank=True, null=True)  # Field name made lowercase.
    sheavyfootfallvfx = models.TextField(db_column='sHeavyFootfallVFX', blank=True, null=True)  # Field name made lowercase.
    sheavyimpactvfx = models.TextField(db_column='sHeavyImpactVFX', blank=True, null=True)  # Field name made lowercase.
    slightfootfallvfx = models.TextField(db_column='sLightFootfallVFX', blank=True, null=True)  # Field name made lowercase.
    smaterialdescription = models.TextField(db_column='sMaterialDescription', blank=True, null=True)  # Field name made lowercase.
    smediumexitvfx = models.TextField(db_column='sMediumExitVFX', blank=True, null=True)  # Field name made lowercase.
    smediumfootfallvfx = models.TextField(db_column='sMediumFootfallVFX', blank=True, null=True)  # Field name made lowercase.
    smediumimpactvfx = models.TextField(db_column='sMediumImpactVFX', blank=True, null=True)  # Field name made lowercase.
    smeleeimpactvfx = models.TextField(db_column='sMeleeImpactVFX', blank=True, null=True)  # Field name made lowercase.
    snonlethalimpactvfx = models.TextField(db_column='sNonLethalImpactVFX', blank=True, null=True)  # Field name made lowercase.
    srbcollisionlargevfx = models.TextField(db_column='sRBCollisionLargeVFX', blank=True, null=True)  # Field name made lowercase.
    srbcollisionsmallvfx = models.TextField(db_column='sRBCollisionSmallVFX', blank=True, null=True)  # Field name made lowercase.
    srbcollisionvfx = models.TextField(db_column='sRBCollisionVFX', blank=True, null=True)  # Field name made lowercase.
    srbscrapevfx = models.TextField(db_column='sRBScrapeVFX', blank=True, null=True)  # Field name made lowercase.
    sshotimpactvfx = models.TextField(db_column='sShotImpactVFX', blank=True, null=True)  # Field name made lowercase.
    ssmallexitvfx = models.TextField(db_column='sSmallExitVFX', blank=True, null=True)  # Field name made lowercase.
    ssmallimpactvfx = models.TextField(db_column='sSmallImpactVFX', blank=True, null=True)  # Field name made lowercase.
    swheelsmokevfx = models.TextField(db_column='sWheelSmokeVFX', blank=True, null=True)  # Field name made lowercase.
    fhardnesslower = models.FloatField(db_column='fHardnessLower', blank=True, null=True)  # Field name made lowercase.
    fhardnessupper = models.FloatField(db_column='fHardnessUpper', blank=True, null=True)  # Field name made lowercase.
    efxmaterialimpact = models.IntegerField(db_column='eFXMaterialImpact', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FXMaterialImpacts'


class Facialhairrandomgeneration(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fprobability = models.FloatField(db_column='fProbability', blank=True, null=True)  # Field name made lowercase.
    efacialhairrandomgeneration = models.IntegerField(db_column='eFacialHairRandomGeneration', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FacialHairRandomGeneration'


class Factionrestrictedlocations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    efactionrestrictedlocation = models.IntegerField(db_column='eFactionRestrictedLocation', blank=True, null=True)  # Field name made lowercase.
    npadding_ignore_me = models.IntegerField(db_column='nPadding_Ignore_Me', blank=True, null=True)  # Field name made lowercase.
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FactionRestrictedLocations'


class Factions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    sfactioninfodescription = models.TextField(db_column='sFactionInfoDescription', blank=True, null=True)  # Field name made lowercase.
    sfactioninfodisplayname = models.TextField(db_column='sFactionInfoDisplayName', blank=True, null=True)  # Field name made lowercase.
    sskinname = models.TextField(db_column='sSkinName', blank=True, null=True)  # Field name made lowercase.
    espawnzonemarker = models.IntegerField(db_column='eSpawnZoneMarker', blank=True, null=True)  # Field name made lowercase.
    evolumecolour = models.IntegerField(db_column='eVolumeColour', blank=True, null=True)  # Field name made lowercase.
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Factions'


class Feedbackmessages(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sfeedbackmessage = models.TextField(db_column='sFeedbackMessage', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    efeedbackmessage = models.IntegerField(db_column='eFeedbackMessage', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FeedbackMessages'


class Fireoffsets(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fforwards = models.FloatField(db_column='fForwards', blank=True, null=True)  # Field name made lowercase.
    fright = models.FloatField(db_column='fRight', blank=True, null=True)  # Field name made lowercase.
    fup = models.FloatField(db_column='fUp', blank=True, null=True)  # Field name made lowercase.
    efireoffset = models.IntegerField(db_column='eFireOffset', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FireOffsets'


class Gameflowdialogs(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sbutton1label = models.TextField(db_column='sButton1Label', blank=True, null=True)  # Field name made lowercase.
    sbutton2label = models.TextField(db_column='sButton2Label', blank=True, null=True)  # Field name made lowercase.
    sbutton3label = models.TextField(db_column='sButton3Label', blank=True, null=True)  # Field name made lowercase.
    splayerclass = models.TextField(db_column='sPlayerClass', blank=True, null=True)  # Field name made lowercase.
    stitle = models.TextField(db_column='sTitle', blank=True, null=True)  # Field name made lowercase.
    ebutton1result = models.IntegerField(db_column='eButton1Result', blank=True, null=True)  # Field name made lowercase.
    ebutton2result = models.IntegerField(db_column='eButton2Result', blank=True, null=True)  # Field name made lowercase.
    ebutton3result = models.IntegerField(db_column='eButton3Result', blank=True, null=True)  # Field name made lowercase.
    ecancelresult = models.IntegerField(db_column='eCancelResult', blank=True, null=True)  # Field name made lowercase.
    edefaultbutton = models.IntegerField(db_column='eDefaultButton', blank=True, null=True)  # Field name made lowercase.
    escaleforminterface = models.IntegerField(db_column='eScaleformInterface', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GameFlowDialogs'


class Gameplayeventcategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sactivitymessageparameter4comment = models.TextField(db_column='sActivityMessageParameter4Comment', blank=True, null=True)  # Field name made lowercase.
    ndummy = models.IntegerField(db_column='nDummy', blank=True, null=True)  # Field name made lowercase.
    egameplayeventcategory = models.IntegerField(db_column='eGameplayEventCategory', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GameplayEventCategories'


class Gameplayeventcategories2(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sactivitymessageparameter4comment = models.TextField(db_column='sActivityMessageParameter4Comment', blank=True, null=True)  # Field name made lowercase.
    ndummy = models.IntegerField(db_column='nDummy', blank=True, null=True)  # Field name made lowercase.
    egameplayeventcategory2 = models.IntegerField(db_column='eGameplayEventCategory2', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GameplayEventCategories2'


class GameplayeventInventoryoperation(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)  # Field name made lowercase.
    echildrule = models.IntegerField(db_column='eChildRule', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GameplayEvent_InventoryOperation'


class GameplayeventMissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    echildrule = models.IntegerField(db_column='eChildRule', blank=True, null=True)  # Field name made lowercase.
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GameplayEvent_Missions'


class GameplayeventTasktargets(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)  # Field name made lowercase.
    echildrule = models.IntegerField(db_column='eChildRule', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GameplayEvent_TaskTargets'


class GameplayeventVehiclehealth(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)  # Field name made lowercase.
    echildrule = models.IntegerField(db_column='eChildRule', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GameplayEvent_VehicleHealth'


class Gameplayevents(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eactivitymessage_0 = models.IntegerField(db_column='eActivityMessage_0', blank=True, null=True)  # Field name made lowercase.
    eactivitymessage_1 = models.IntegerField(db_column='eActivityMessage_1', blank=True, null=True)  # Field name made lowercase.
    eactivitymessage_2 = models.IntegerField(db_column='eActivityMessage_2', blank=True, null=True)  # Field name made lowercase.
    eactivitymessageonreward = models.IntegerField(db_column='eActivityMessageOnReward', blank=True, null=True)  # Field name made lowercase.
    edisabledrulesets = models.IntegerField(db_column='eDisabledRuleSets', blank=True, null=True)  # Field name made lowercase.
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)  # Field name made lowercase.
    ehelppopup = models.IntegerField(db_column='eHelpPopup', blank=True, null=True)  # Field name made lowercase.
    emissionsystems = models.IntegerField(db_column='eMissionSystems', blank=True, null=True)  # Field name made lowercase.
    eobject = models.IntegerField(db_column='eObject', blank=True, null=True)  # Field name made lowercase.
    eobjectset = models.IntegerField(db_column='eObjectSet', blank=True, null=True)  # Field name made lowercase.
    eobjectstateset = models.IntegerField(db_column='eObjectStateSet', blank=True, null=True)  # Field name made lowercase.
    eresultantheatchange = models.IntegerField(db_column='eResultantHeatChange', blank=True, null=True)  # Field name made lowercase.
    eresultantwitnessablecrime = models.IntegerField(db_column='eResultantWitnessableCrime', blank=True, null=True)  # Field name made lowercase.
    eresultantwitnessablecrimeend = models.IntegerField(db_column='eResultantWitnessableCrimeEnd', blank=True, null=True)  # Field name made lowercase.
    etrackedactivity = models.IntegerField(db_column='eTrackedActivity', blank=True, null=True)  # Field name made lowercase.
    fexpiryperiod = models.FloatField(db_column='fExpiryPeriod', blank=True, null=True)  # Field name made lowercase.
    na = models.IntegerField(db_column='nA', blank=True, null=True)  # Field name made lowercase.
    nb = models.IntegerField(db_column='nB', blank=True, null=True)  # Field name made lowercase.
    nprecedence = models.IntegerField(db_column='nPrecedence', blank=True, null=True)  # Field name made lowercase.
    ecsa = models.IntegerField(db_column='eCSA', blank=True, null=True)  # Field name made lowercase.
    eexcludelist = models.IntegerField(db_column='eExcludeList', blank=True, null=True)  # Field name made lowercase.
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)  # Field name made lowercase.
    egameplayeventcategory = models.IntegerField(db_column='eGameplayEventCategory', blank=True, null=True)  # Field name made lowercase.
    egameplayeventcategory2 = models.IntegerField(db_column='eGameplayEventCategory2', blank=True, null=True)  # Field name made lowercase.
    eincludelist = models.IntegerField(db_column='eIncludeList', blank=True, null=True)  # Field name made lowercase.
    emutuallyexclusive = models.IntegerField(db_column='eMutuallyExclusive', blank=True, null=True)  # Field name made lowercase.
    epvp = models.IntegerField(db_column='ePvP', blank=True, null=True)  # Field name made lowercase.
    eresultantreward = models.IntegerField(db_column='eResultantReward', blank=True, null=True)  # Field name made lowercase.
    brequirea = models.IntegerField(db_column='bRequireA', blank=True, null=True)  # Field name made lowercase.
    brequireb = models.IntegerField(db_column='bRequireB', blank=True, null=True)  # Field name made lowercase.
    bresettrackedactivity = models.IntegerField(db_column='bResetTrackedActivity', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GameplayEvents'


class GameplayeventsModetimer(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    echildrule = models.IntegerField(db_column='eChildRule', blank=True, null=True)  # Field name made lowercase.
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GameplayEvents_ModeTimer'


class Gameplaymodetimertypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    edistrictruleset = models.IntegerField(db_column='eDistrictRuleSet', blank=True, null=True)  # Field name made lowercase.
    egameplaymodetimertype = models.IntegerField(db_column='eGameplayModeTimerType', blank=True, null=True)  # Field name made lowercase.
    balive = models.IntegerField(db_column='bAlive', blank=True, null=True)  # Field name made lowercase.
    bcharactereditor = models.IntegerField(db_column='bCharacterEditor', blank=True, null=True)  # Field name made lowercase.
    bclothingeditor = models.IntegerField(db_column='bClothingEditor', blank=True, null=True)  # Field name made lowercase.
    bdirectedmission = models.IntegerField(db_column='bDirectedMission', blank=True, null=True)  # Field name made lowercase.
    bmaxheat = models.IntegerField(db_column='bMaxHeat', blank=True, null=True)  # Field name made lowercase.
    bmusiceditor = models.IntegerField(db_column='bMusicEditor', blank=True, null=True)  # Field name made lowercase.
    bnotineditor = models.IntegerField(db_column='bNotInEditor', blank=True, null=True)  # Field name made lowercase.
    botherpvp = models.IntegerField(db_column='bOtherPvP', blank=True, null=True)  # Field name made lowercase.
    bsymboleditor = models.IntegerField(db_column='bSymbolEditor', blank=True, null=True)  # Field name made lowercase.
    btotal = models.IntegerField(db_column='bTotal', blank=True, null=True)  # Field name made lowercase.
    bvehicleeditor = models.IntegerField(db_column='bVehicleEditor', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GameplayModeTimerTypes'


class Gameplayobjectsets(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    egameplayobjectset = models.IntegerField(db_column='eGameplayObjectSet', blank=True, null=True)  # Field name made lowercase.
    ndummy = models.IntegerField(blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GameplayObjectSets'


class Gameplayobjects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    egameplayobject = models.IntegerField(db_column='eGameplayObject', blank=True, null=True)  # Field name made lowercase.
    ememberof_0 = models.IntegerField(db_column='eMemberOf_0', blank=True, null=True)  # Field name made lowercase.
    ememberof_1 = models.IntegerField(db_column='eMemberOf_1', blank=True, null=True)  # Field name made lowercase.
    ememberof_2 = models.IntegerField(db_column='eMemberOf_2', blank=True, null=True)  # Field name made lowercase.
    ememberof_3 = models.IntegerField(db_column='eMemberOf_3', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GameplayObjects'


class Gameplayobjectsfixed(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    egameplayobject = models.IntegerField(db_column='eGameplayObject', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GameplayObjectsFixed'


class Gameplaystatesets(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    egameplaystateset = models.IntegerField(db_column='eGameplayStateSet', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GameplayStateSets'


class Gameplaystates(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ememberof_0 = models.IntegerField(db_column='eMemberOf_0', blank=True, null=True)  # Field name made lowercase.
    ememberof_1 = models.IntegerField(db_column='eMemberOf_1', blank=True, null=True)  # Field name made lowercase.
    ememberof_2 = models.IntegerField(db_column='eMemberOf_2', blank=True, null=True)  # Field name made lowercase.
    ememberof_3 = models.IntegerField(db_column='eMemberOf_3', blank=True, null=True)  # Field name made lowercase.
    egameplaystate = models.IntegerField(db_column='eGameplayState', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GameplayStates'


class Gameplayvehiclehealthranges(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nhealthmax = models.IntegerField(db_column='nHealthMax', blank=True, null=True)  # Field name made lowercase.
    nhealthmin = models.IntegerField(db_column='nHealthMin', blank=True, null=True)  # Field name made lowercase.
    egameplayvehiclehealthrange = models.IntegerField(db_column='eGameplayVehicleHealthRange', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GameplayVehicleHealthRanges'


class Golempartclasses(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    egolempartclass = models.IntegerField(db_column='eGolemPartClass', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    bcoversbreasts = models.IntegerField(db_column='bCoversBreasts', blank=True, null=True)  # Field name made lowercase.
    bcoversgenitalia = models.IntegerField(db_column='bCoversGenitalia', blank=True, null=True)  # Field name made lowercase.
    buseinclothingpreview = models.IntegerField(db_column='bUseInClothingPreview', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GolemPartClasses'


class Golemparts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sgolempart = models.TextField(db_column='sGolemPart', blank=True, null=True)  # Field name made lowercase.
    susername = models.TextField(db_column='sUsername', blank=True, null=True)  # Field name made lowercase.
    eclass = models.IntegerField(db_column='eClass', blank=True, null=True)  # Field name made lowercase.
    eclothingitemcategory = models.IntegerField(db_column='eClothingItemCategory', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    nversatility = models.IntegerField(db_column='nVersatility', blank=True, null=True)  # Field name made lowercase.
    bstartup = models.IntegerField(db_column='bStartup', blank=True, null=True)  # Field name made lowercase.
    btestasset = models.IntegerField(db_column='bTestAsset', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GolemParts'


class Graffitidisplaypoint(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    edisplaypoint = models.IntegerField(db_column='eDisplayPoint', blank=True, null=True)  # Field name made lowercase.
    fspraydurationoverride = models.FloatField(db_column='fSprayDurationOverride', blank=True, null=True)  # Field name made lowercase.
    einteractiontype = models.IntegerField(db_column='eInteractionType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GraffitiDisplayPoint'


class Grenadeweapontype(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    erecoil = models.IntegerField(db_column='eRecoil', blank=True, null=True)  # Field name made lowercase.
    eweaponprojectile = models.IntegerField(db_column='eWeaponProjectile', blank=True, null=True)  # Field name made lowercase.
    eweapontype = models.IntegerField(db_column='eWeaponType', blank=True, null=True)  # Field name made lowercase.
    ffiringspeed = models.FloatField(db_column='fFiringSpeed', blank=True, null=True)  # Field name made lowercase.
    fmaxangleadded = models.FloatField(db_column='fMaxAngleAdded', blank=True, null=True)  # Field name made lowercase.
    fpinpulltime = models.FloatField(db_column='fPinPullTime', blank=True, null=True)  # Field name made lowercase.
    fthrowtime = models.FloatField(db_column='fThrowTime', blank=True, null=True)  # Field name made lowercase.
    baffectedbygravity = models.IntegerField(db_column='bAffectedByGravity', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GrenadeWeaponType'


class Hudceremonymsg(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    stitle = models.TextField(db_column='sTitle', blank=True, null=True)  # Field name made lowercase.
    ehudmessage = models.IntegerField(db_column='eHUDMessage', blank=True, null=True)  # Field name made lowercase.
    eiconfallback = models.IntegerField(db_column='eIconFallback', blank=True, null=True)  # Field name made lowercase.
    etitlebgcolour = models.IntegerField(db_column='eTitleBGColour', blank=True, null=True)  # Field name made lowercase.
    etype = models.IntegerField(db_column='eType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDCeremonyMsg'


class Hudcolour(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ehudcolour = models.IntegerField(db_column='eHUDColour', blank=True, null=True)  # Field name made lowercase.
    eoverridecolour = models.IntegerField(db_column='eOverrideColour', blank=True, null=True)  # Field name made lowercase.
    na = models.IntegerField(db_column='nA', blank=True, null=True)  # Field name made lowercase.
    nb = models.IntegerField(db_column='nB', blank=True, null=True)  # Field name made lowercase.
    ng = models.IntegerField(db_column='nG', blank=True, null=True)  # Field name made lowercase.
    nr = models.IntegerField(db_column='nR', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDColour'


class Hudcolourprofiles(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ehudcolourprofile = models.IntegerField(db_column='eHUDColourProfile', blank=True, null=True)  # Field name made lowercase.
    eprimarycolour = models.IntegerField(db_column='ePrimaryColour', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDColourProfiles'


class Hudcombatmessages(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sline0 = models.TextField(db_column='sLine0', blank=True, null=True)  # Field name made lowercase.
    sline1 = models.TextField(db_column='sLine1', blank=True, null=True)  # Field name made lowercase.
    sline2 = models.TextField(db_column='sLine2', blank=True, null=True)  # Field name made lowercase.
    ehudmessage = models.IntegerField(db_column='eHUDMessage', blank=True, null=True)  # Field name made lowercase.
    eicon = models.IntegerField(db_column='eIcon', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDCombatMessages'


class Hudconstantbools(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    scomment = models.TextField(db_column='sComment', blank=True, null=True)  # Field name made lowercase.
    ehudconstantbool = models.IntegerField(db_column='eHUDConstantBool', blank=True, null=True)  # Field name made lowercase.
    bvalue = models.IntegerField(db_column='bValue', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDConstantBools'


class Hudconstantstring(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    scomment = models.TextField(db_column='sComment', blank=True, null=True)  # Field name made lowercase.
    stext = models.TextField(db_column='sText', blank=True, null=True)  # Field name made lowercase.
    ehudconstantstring = models.IntegerField(db_column='eHUDConstantString', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDConstantString'


class Hudconstants(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    scomment = models.TextField(db_column='sComment', blank=True, null=True)  # Field name made lowercase.
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)  # Field name made lowercase.
    ehudconstant = models.IntegerField(db_column='eHUDConstant', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDConstants'


class Huddistrictmapmarker(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    slegendname = models.TextField(db_column='sLegendName', blank=True, null=True)  # Field name made lowercase.
    ehuddistrictmapmarker = models.IntegerField(db_column='eHUDDistrictMapMarker', blank=True, null=True)  # Field name made lowercase.
    eiconcombo = models.IntegerField(db_column='eIconCombo', blank=True, null=True)  # Field name made lowercase.
    fmaxvisibledistance = models.FloatField(db_column='fMaxVisibleDistance', blank=True, null=True)  # Field name made lowercase.
    ndraworder = models.IntegerField(db_column='nDrawOrder', blank=True, null=True)  # Field name made lowercase.
    nsize = models.IntegerField(db_column='nSize', blank=True, null=True)  # Field name made lowercase.
    bdisablewaypoints = models.IntegerField(db_column='bDisableWaypoints', blank=True, null=True)  # Field name made lowercase.
    binlegend = models.IntegerField(db_column='bInLegend', blank=True, null=True)  # Field name made lowercase.
    binteractonmap = models.IntegerField(db_column='bInteractOnMap', blank=True, null=True)  # Field name made lowercase.
    bisaesthetic = models.IntegerField(db_column='bIsAesthetic', blank=True, null=True)  # Field name made lowercase.
    bshowonelectivespawnmap = models.IntegerField(db_column='bShowOnElectiveSpawnMap', blank=True, null=True)  # Field name made lowercase.
    bshowonspawnmap = models.IntegerField(db_column='bShowOnSpawnMap', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDDistrictMapMarker'


class Hudeffects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    smaterialref = models.TextField(db_column='sMaterialRef', blank=True, null=True)  # Field name made lowercase.
    ehudeffect = models.IntegerField(db_column='eHUDEffect', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDEffects'


class Hudiconcombos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ehudiconcombo = models.IntegerField(db_column='eHUDIconCombo', blank=True, null=True)  # Field name made lowercase.
    elayer1 = models.IntegerField(db_column='eLayer1', blank=True, null=True)  # Field name made lowercase.
    elayer2 = models.IntegerField(db_column='eLayer2', blank=True, null=True)  # Field name made lowercase.
    elayer3 = models.IntegerField(db_column='eLayer3', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDIconCombos'


class Hudicons(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ehudicon = models.IntegerField(db_column='eHUDIcon', blank=True, null=True)  # Field name made lowercase.
    niconcolumn = models.IntegerField(db_column='nIconColumn', blank=True, null=True)  # Field name made lowercase.
    niconrow = models.IntegerField(db_column='nIconRow', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDIcons'


class Hudinfobrowsers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    spackageref = models.TextField(db_column='sPackageRef', blank=True, null=True)  # Field name made lowercase.
    ehudinfobrowser = models.IntegerField(db_column='eHUDInfoBrowser', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDInfoBrowsers'


class Hudmarkeroffset(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ehudmarkeroffset = models.IntegerField(db_column='eHUDMarkerOffset', blank=True, null=True)  # Field name made lowercase.
    foffset_x = models.FloatField(db_column='fOffset_X', blank=True, null=True)  # Field name made lowercase.
    foffset_y = models.FloatField(db_column='fOffset_Y', blank=True, null=True)  # Field name made lowercase.
    foffset_z = models.FloatField(db_column='fOffset_Z', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDMarkerOffset'


class Hudmarkerstatecolours(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    edefault = models.IntegerField(db_column='eDefault', blank=True, null=True)  # Field name made lowercase.
    ehudmarkerstatecolour = models.IntegerField(db_column='eHUDMarkerStateColour', blank=True, null=True)  # Field name made lowercase.
    etask_neutral = models.IntegerField(db_column='eTask_Neutral', blank=True, null=True)  # Field name made lowercase.
    etask_oppositionattack = models.IntegerField(db_column='eTask_OppositionAttack', blank=True, null=True)  # Field name made lowercase.
    etask_oppositiondefend = models.IntegerField(db_column='eTask_OppositionDefend', blank=True, null=True)  # Field name made lowercase.
    etask_ownerattack = models.IntegerField(db_column='eTask_OwnerAttack', blank=True, null=True)  # Field name made lowercase.
    etask_ownerdefend = models.IntegerField(db_column='eTask_OwnerDefend', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDMarkerStateColours'


class Hudmarkerstates(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fupdatedelay = models.FloatField(db_column='fUpdateDelay', blank=True, null=True)  # Field name made lowercase.
    ehudmarkerstate = models.IntegerField(db_column='eHUDMarkerState', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDMarkerStates'


class Hudmarkervisual(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ecolourprofile = models.IntegerField(db_column='eColourProfile', blank=True, null=True)  # Field name made lowercase.
    edistrictmapmarker = models.IntegerField(db_column='eDistrictMapMarker', blank=True, null=True)  # Field name made lowercase.
    ehudmarkeroffset = models.IntegerField(db_column='eHUDMarkerOffset', blank=True, null=True)  # Field name made lowercase.
    ehudmarkervisual = models.IntegerField(db_column='eHUDMarkerVisual', blank=True, null=True)  # Field name made lowercase.
    eradarmarker = models.IntegerField(db_column='eRadarMarker', blank=True, null=True)  # Field name made lowercase.
    etaskmarker = models.IntegerField(db_column='eTaskMarker', blank=True, null=True)  # Field name made lowercase.
    ecategory = models.IntegerField(db_column='eCategory', blank=True, null=True)  # Field name made lowercase.
    bcontainsplayerdata = models.IntegerField(db_column='bContainsPlayerData', blank=True, null=True)  # Field name made lowercase.
    bpreventpawnvisibilitychecks = models.IntegerField(db_column='bPreventPawnVisibilityChecks', blank=True, null=True)  # Field name made lowercase.
    buseindividualstate = models.IntegerField(db_column='bUseIndividualState', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDMarkerVisual'


class Hudmarkervisualtext(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sneutral = models.TextField(db_column='sNeutral', blank=True, null=True)  # Field name made lowercase.
    soppositionattack = models.TextField(db_column='sOppositionAttack', blank=True, null=True)  # Field name made lowercase.
    soppositiondefend = models.TextField(db_column='sOppositionDefend', blank=True, null=True)  # Field name made lowercase.
    sownerattack = models.TextField(db_column='sOwnerAttack', blank=True, null=True)  # Field name made lowercase.
    sownerdefend = models.TextField(db_column='sOwnerDefend', blank=True, null=True)  # Field name made lowercase.
    ehudmarkervisual = models.IntegerField(db_column='eHUDMarkerVisual', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDMarkerVisualText'


class Hudmessagecategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplaytext = models.TextField(db_column='sDisplayText', blank=True, null=True)  # Field name made lowercase.
    ehudmessagecategory = models.IntegerField(db_column='eHUDMessageCategory', blank=True, null=True)  # Field name made lowercase.
    eicon = models.IntegerField(db_column='eIcon', blank=True, null=True)  # Field name made lowercase.
    echatcategory = models.IntegerField(db_column='eChatCategory', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDMessageCategories'


class Hudmessageposition(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ehudmessageposition = models.IntegerField(db_column='eHUDMessagePosition', blank=True, null=True)  # Field name made lowercase.
    fypercent = models.FloatField(db_column='fYPercent', blank=True, null=True)  # Field name made lowercase.
    nyoffset = models.IntegerField(db_column='nYOffset', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDMessagePosition'


class Hudmessagescenes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    spackageref = models.TextField(db_column='sPackageRef', blank=True, null=True)  # Field name made lowercase.
    ehudmessagescene = models.IntegerField(db_column='eHUDMessageScene', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDMessageScenes'


class Hudmessages(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    saudiocue = models.TextField(db_column='sAudioCue', blank=True, null=True)  # Field name made lowercase.
    schattext = models.TextField(db_column='sChatText', blank=True, null=True)  # Field name made lowercase.
    sdisplaytext = models.TextField(db_column='sDisplayText', blank=True, null=True)  # Field name made lowercase.
    sfemaletext = models.TextField(db_column='sFemaleText', blank=True, null=True)  # Field name made lowercase.
    ecategory = models.IntegerField(db_column='eCategory', blank=True, null=True)  # Field name made lowercase.
    ehudmessage = models.IntegerField(db_column='eHUDMessage', blank=True, null=True)  # Field name made lowercase.
    enextmessage = models.IntegerField(db_column='eNextMessage', blank=True, null=True)  # Field name made lowercase.
    epopupdialogoverride = models.IntegerField(db_column='ePopupDialogOverride', blank=True, null=True)  # Field name made lowercase.
    eposition = models.IntegerField(db_column='ePosition', blank=True, null=True)  # Field name made lowercase.
    escene = models.IntegerField(db_column='eScene', blank=True, null=True)  # Field name made lowercase.
    euistyle = models.IntegerField(db_column='eUIStyle', blank=True, null=True)  # Field name made lowercase.
    fdisplaytime = models.FloatField(db_column='fDisplayTime', blank=True, null=True)  # Field name made lowercase.
    fqueuetimeout = models.FloatField(db_column='fQueueTimeout', blank=True, null=True)  # Field name made lowercase.
    epriority = models.IntegerField(db_column='ePriority', blank=True, null=True)  # Field name made lowercase.
    ballowmultiples = models.IntegerField(db_column='bAllowMultiples', blank=True, null=True)  # Field name made lowercase.
    bforaction = models.IntegerField(db_column='bForAction', blank=True, null=True)  # Field name made lowercase.
    bforceremony = models.IntegerField(db_column='bForCeremony', blank=True, null=True)  # Field name made lowercase.
    bforchat = models.IntegerField(db_column='bForChat', blank=True, null=True)  # Field name made lowercase.
    bforcombat = models.IntegerField(db_column='bForCombat', blank=True, null=True)  # Field name made lowercase.
    bfordistrictmap = models.IntegerField(db_column='bForDistrictMap', blank=True, null=True)  # Field name made lowercase.
    bsuppressmain = models.IntegerField(db_column='bSuppressMain', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDMessages'


class Hudpopupmenuitems(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sconsolecommand = models.TextField(db_column='sConsoleCommand', blank=True, null=True)  # Field name made lowercase.
    skeypress = models.TextField(db_column='sKeyPress', blank=True, null=True)  # Field name made lowercase.
    slocalisationtext = models.TextField(db_column='sLocalisationText', blank=True, null=True)  # Field name made lowercase.
    ehudpopupmenuitem = models.IntegerField(db_column='eHUDPopUpMenuItem', blank=True, null=True)  # Field name made lowercase.
    eimage = models.IntegerField(db_column='eImage', blank=True, null=True)  # Field name made lowercase.
    eenabledrule = models.IntegerField(db_column='eEnabledRule', blank=True, null=True)  # Field name made lowercase.
    bdisplaykeybinding = models.IntegerField(db_column='bDisplayKeyBinding', blank=True, null=True)  # Field name made lowercase.
    benablewhendead = models.IntegerField(db_column='bEnableWhenDead', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDPopUpMenuItems'


class Hudradarmarkers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ehudradarmarker = models.IntegerField(db_column='eHUDRadarMarker', blank=True, null=True)  # Field name made lowercase.
    eicon = models.IntegerField(db_column='eIcon', blank=True, null=True)  # Field name made lowercase.
    eiconsurround = models.IntegerField(db_column='eIconSurround', blank=True, null=True)  # Field name made lowercase.
    niconsize = models.IntegerField(db_column='nIconSize', blank=True, null=True)  # Field name made lowercase.
    niconsurroundsize = models.IntegerField(db_column='nIconSurroundSize', blank=True, null=True)  # Field name made lowercase.
    bshowonelectivespawnmap = models.IntegerField(db_column='bShowOnElectiveSpawnMap', blank=True, null=True)  # Field name made lowercase.
    bvalidinmission = models.IntegerField(db_column='bValidInMission', blank=True, null=True)  # Field name made lowercase.
    bvalidoutofmission = models.IntegerField(db_column='bValidOutOfMission', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDRadarMarkers'


class Hudreticulehinticons(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplaytext = models.TextField(db_column='sDisplayText', blank=True, null=True)  # Field name made lowercase.
    ecolour = models.IntegerField(db_column='eColour', blank=True, null=True)  # Field name made lowercase.
    ehudreticulehinticon = models.IntegerField(db_column='eHUDReticuleHintIcon', blank=True, null=True)  # Field name made lowercase.
    eicon = models.IntegerField(db_column='eIcon', blank=True, null=True)  # Field name made lowercase.
    fmaxdistance = models.FloatField(db_column='fMaxDistance', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDReticuleHintIcons'


class Hudreticules(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    spackageref = models.TextField(db_column='sPackageRef', blank=True, null=True)  # Field name made lowercase.
    ecolourdefault = models.IntegerField(db_column='eColourDefault', blank=True, null=True)  # Field name made lowercase.
    ecolourenemy = models.IntegerField(db_column='eColourEnemy', blank=True, null=True)  # Field name made lowercase.
    ecolourfriend = models.IntegerField(db_column='eColourFriend', blank=True, null=True)  # Field name made lowercase.
    ehudreticule = models.IntegerField(db_column='eHUDReticule', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDReticules'


class Hudscenes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdatastoretag = models.TextField(db_column='sDataStoreTag', blank=True, null=True)  # Field name made lowercase.
    spackageref = models.TextField(db_column='sPackageRef', blank=True, null=True)  # Field name made lowercase.
    ehudscenes = models.IntegerField(db_column='eHUDScenes', blank=True, null=True)  # Field name made lowercase.
    bopeninloginlevel = models.IntegerField(db_column='bOpenInLoginLevel', blank=True, null=True)  # Field name made lowercase.
    bstarthidden = models.IntegerField(db_column='bStartHidden', blank=True, null=True)  # Field name made lowercase.
    bupdatewhiledead = models.IntegerField(db_column='bUpdateWhileDead', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDScenes'


class Hudtaskmarkerscenes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    spackageref = models.TextField(db_column='sPackageRef', blank=True, null=True)  # Field name made lowercase.
    ehudtaskmarkerscene = models.IntegerField(db_column='eHUDTaskMarkerScene', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDTaskMarkerScenes'


class Hudtaskmarkers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    earrowicon = models.IntegerField(db_column='eArrowIcon', blank=True, null=True)  # Field name made lowercase.
    earrowiconellipse = models.IntegerField(db_column='eArrowIconEllipse', blank=True, null=True)  # Field name made lowercase.
    earrowiconocc = models.IntegerField(db_column='eArrowIconOcc', blank=True, null=True)  # Field name made lowercase.
    eellipseicon = models.IntegerField(db_column='eEllipseIcon', blank=True, null=True)  # Field name made lowercase.
    ehudtaskmarker = models.IntegerField(db_column='eHUDTaskMarker', blank=True, null=True)  # Field name made lowercase.
    eoccludedicon = models.IntegerField(db_column='eOccludedIcon', blank=True, null=True)  # Field name made lowercase.
    escene = models.IntegerField(db_column='eScene', blank=True, null=True)  # Field name made lowercase.
    evisibleicon = models.IntegerField(db_column='eVisibleIcon', blank=True, null=True)  # Field name made lowercase.
    fmaxvisibledistance = models.FloatField(db_column='fMaxVisibleDistance', blank=True, null=True)  # Field name made lowercase.
    npriority = models.IntegerField(db_column='nPriority', blank=True, null=True)  # Field name made lowercase.
    bhidedistance = models.IntegerField(db_column='bHideDistance', blank=True, null=True)  # Field name made lowercase.
    bhidewhenoccluded = models.IntegerField(db_column='bHideWhenOccluded', blank=True, null=True)  # Field name made lowercase.
    binteractondistrictmap = models.IntegerField(db_column='bInteractOnDistrictMap', blank=True, null=True)  # Field name made lowercase.
    bshowbydefault = models.IntegerField(db_column='bShowByDefault', blank=True, null=True)  # Field name made lowercase.
    bshowinworld = models.IntegerField(db_column='bShowInWorld', blank=True, null=True)  # Field name made lowercase.
    bshowonedge = models.IntegerField(db_column='bShowOnEdge', blank=True, null=True)  # Field name made lowercase.
    bshowonself = models.IntegerField(db_column='bShowOnSelf', blank=True, null=True)  # Field name made lowercase.
    bvalidinmission = models.IntegerField(db_column='bValidInMission', blank=True, null=True)  # Field name made lowercase.
    bvalidoutofmission = models.IntegerField(db_column='bValidOutOfMission', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDTaskMarkers'


class Hudtextureicons(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    siconsetname = models.TextField(db_column='sIconSetName', blank=True, null=True)  # Field name made lowercase.
    smoviename = models.TextField(db_column='sMovieName', blank=True, null=True)  # Field name made lowercase.
    spackageref = models.TextField(db_column='sPackageRef', blank=True, null=True)  # Field name made lowercase.
    ehudtextureicon = models.IntegerField(db_column='eHUDTextureIcon', blank=True, null=True)  # Field name made lowercase.
    etexturepageicon = models.IntegerField(db_column='eTexturePageIcon', blank=True, null=True)  # Field name made lowercase.
    nframenumber = models.IntegerField(db_column='nFrameNumber', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDTextureIcons'


class Hudtexturepage(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    spackagename = models.TextField(db_column='sPackageName', blank=True, null=True)  # Field name made lowercase.
    ehudtexturepage = models.IntegerField(db_column='eHUDTexturePage', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDTexturePage'


class Hudtexturepageicon(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ehudtexturepageicon = models.IntegerField(db_column='eHUDTexturePageIcon', blank=True, null=True)  # Field name made lowercase.
    etexturepage = models.IntegerField(db_column='eTexturePage', blank=True, null=True)  # Field name made lowercase.
    nu = models.IntegerField(db_column='nU', blank=True, null=True)  # Field name made lowercase.
    nul = models.IntegerField(db_column='nUL', blank=True, null=True)  # Field name made lowercase.
    nv = models.IntegerField(db_column='nV', blank=True, null=True)  # Field name made lowercase.
    nvl = models.IntegerField(db_column='nVL', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDTexturePageIcon'


class HudusablesDisplaysettings(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eiconcolour = models.IntegerField(db_column='eIconColour', blank=True, null=True)  # Field name made lowercase.
    fbackgroundopacity = models.FloatField(db_column='fBackgroundOpacity', blank=True, null=True)  # Field name made lowercase.
    ftextbackgroundopacity = models.FloatField(db_column='fTextBackgroundOpacity', blank=True, null=True)  # Field name made lowercase.
    ehudusables_displaysetting = models.IntegerField(db_column='eHUDUsables_DisplaySetting', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDUsables_DisplaySettings'


class Hudwscharinfos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ecolourprofile = models.IntegerField(db_column='eColourProfile', blank=True, null=True)  # Field name made lowercase.
    ehudwscharinfo = models.IntegerField(db_column='eHUDWSCharInfo', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDWSCharInfos'


class Hudzonenotifier(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eicon = models.IntegerField(db_column='eIcon', blank=True, null=True)  # Field name made lowercase.
    ehudzonenotifier = models.IntegerField(db_column='eHUDZoneNotifier', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HUDZoneNotifier'


class Heatactionaffects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eheatactionaffect = models.IntegerField(db_column='eHeatActionAffect', blank=True, null=True)  # Field name made lowercase.
    enotorietyeffect = models.IntegerField(db_column='eNotorietyEffect', blank=True, null=True)  # Field name made lowercase.
    eprestigeeffect = models.IntegerField(db_column='ePrestigeEffect', blank=True, null=True)  # Field name made lowercase.
    fescapepenaltytimer = models.FloatField(db_column='fEscapePenaltyTimer', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HeatActionAffects'


class Heatconstants(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    scomment = models.TextField(db_column='sComment', blank=True, null=True)  # Field name made lowercase.
    fcriminalvalue = models.FloatField(db_column='fCriminalValue', blank=True, null=True)  # Field name made lowercase.
    fenforcervalue = models.FloatField(db_column='fEnforcerValue', blank=True, null=True)  # Field name made lowercase.
    eheatconstant = models.IntegerField(db_column='eHeatConstant', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HeatConstants'


class Heatlevels(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    eheatlevel = models.IntegerField(db_column='eHeatLevel', blank=True, null=True)  # Field name made lowercase.
    ehudtexture = models.IntegerField(db_column='eHUDTexture', blank=True, null=True)  # Field name made lowercase.
    frewardmultiplier = models.FloatField(db_column='fRewardMultiplier', blank=True, null=True)  # Field name made lowercase.
    fthreshold = models.FloatField(db_column='fThreshold', blank=True, null=True)  # Field name made lowercase.
    nlevel = models.IntegerField(db_column='nLevel', blank=True, null=True)  # Field name made lowercase.
    bbreakscontactpledges = models.IntegerField(db_column='bBreaksContactPledges', blank=True, null=True)  # Field name made lowercase.
    bdispatchbounty = models.IntegerField(db_column='bDispatchBounty', blank=True, null=True)  # Field name made lowercase.
    bdispatchmission = models.IntegerField(db_column='bDispatchMission', blank=True, null=True)  # Field name made lowercase.
    bpvpunlockedtoallopposingfaction = models.IntegerField(db_column='bPVPUnlockedToAllOpposingFaction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HeatLevels'


class Hostingconfigfiles(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sfilename = models.TextField(db_column='sFilename', blank=True, null=True)  # Field name made lowercase.
    npersistentid = models.IntegerField(db_column='nPersistentId', blank=True, null=True)  # Field name made lowercase.
    ehostingconfigfile = models.IntegerField(db_column='eHostingConfigFile', blank=True, null=True)  # Field name made lowercase.
    etype = models.IntegerField(db_column='eType', blank=True, null=True)  # Field name made lowercase.
    bpersistent = models.IntegerField(db_column='bPersistent', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HostingConfigFiles'


class Hudgroupstates(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sheadertext = models.TextField(db_column='sHeaderText', blank=True, null=True)  # Field name made lowercase.
    eheadercolour = models.IntegerField(db_column='eHeaderColour', blank=True, null=True)  # Field name made lowercase.
    eheadericon = models.IntegerField(db_column='eHeaderIcon', blank=True, null=True)  # Field name made lowercase.
    ehudgroupstate = models.IntegerField(db_column='eHudGroupState', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HudGroupStates'


class Instrumentitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sresource = models.TextField(db_column='sResource', blank=True, null=True)  # Field name made lowercase.
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InstrumentItemTypes'


class Interactiveactortype(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    dummy = models.FloatField(db_column='Dummy', blank=True, null=True)  # Field name made lowercase.
    einteractiveactorcategory = models.IntegerField(db_column='eInteractiveActorCategory', blank=True, null=True)  # Field name made lowercase.
    einteractiveactortype = models.IntegerField(db_column='eInteractiveActorType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InteractiveActorType'


class Intraactivityrewards(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fpercentagelosspercapture = models.FloatField(db_column='fPercentageLossPerCapture', blank=True, null=True)  # Field name made lowercase.
    ncash_0 = models.IntegerField(db_column='nCash_0', blank=True, null=True)  # Field name made lowercase.
    ncash_1 = models.IntegerField(db_column='nCash_1', blank=True, null=True)  # Field name made lowercase.
    ncontactstanding_0 = models.IntegerField(db_column='nContactStanding_0', blank=True, null=True)  # Field name made lowercase.
    ncontactstanding_1 = models.IntegerField(db_column='nContactStanding_1', blank=True, null=True)  # Field name made lowercase.
    nminimumpointsvalue = models.IntegerField(db_column='nMinimumPointsValue', blank=True, null=True)  # Field name made lowercase.
    nscore = models.IntegerField(db_column='nScore', blank=True, null=True)  # Field name made lowercase.
    eintraactivityreward = models.IntegerField(db_column='eIntraActivityReward', blank=True, null=True)  # Field name made lowercase.
    escorecategory = models.IntegerField(db_column='eScoreCategory', blank=True, null=True)  # Field name made lowercase.
    baddtoopenworldcashpool = models.IntegerField(db_column='bAddToOpenWorldCashPool', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IntraActivityRewards'


class Inventoryitemcategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    stablename = models.TextField(db_column='sTableName', blank=True, null=True)  # Field name made lowercase.
    nbytesize = models.IntegerField(db_column='nByteSize', blank=True, null=True)  # Field name made lowercase.
    nbytesizeui = models.IntegerField(db_column='nByteSizeUI', blank=True, null=True)  # Field name made lowercase.
    ninitialstoragespace = models.IntegerField(db_column='nInitialStorageSpace', blank=True, null=True)  # Field name made lowercase.
    nmaxstoragespace = models.IntegerField(db_column='nMaxStorageSpace', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    einventoryitemcategory = models.IntegerField(db_column='eInventoryItemCategory', blank=True, null=True)  # Field name made lowercase.
    bcopyable = models.IntegerField(db_column='bCopyable', blank=True, null=True)  # Field name made lowercase.
    bcreatorwaivesrating = models.IntegerField(db_column='bCreatorWaivesRating', blank=True, null=True)  # Field name made lowercase.
    bmarketplacesearch = models.IntegerField(db_column='bMarketplaceSearch', blank=True, null=True)  # Field name made lowercase.
    brenamable = models.IntegerField(db_column='bRenamable', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryItemCategories'


class Inventoryitemcategorylimited(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fcustomisationreplenishperiod = models.FloatField(db_column='fCustomisationReplenishPeriod', blank=True, null=True)  # Field name made lowercase.
    ncustomisationinitialavailability = models.IntegerField(db_column='nCustomisationInitialAvailability', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    einventoryitemcategory = models.IntegerField(db_column='eInventoryItemCategory', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryItemCategoryLimited'


class Inventoryiteminfracategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    sidentifier = models.TextField(db_column='sIdentifier', blank=True, null=True)  # Field name made lowercase.
    ssingularname = models.TextField(db_column='sSingularName', blank=True, null=True)  # Field name made lowercase.
    einventoryiteminfracategory = models.IntegerField(db_column='eInventoryItemInfraCategory', blank=True, null=True)  # Field name made lowercase.
    ninitialavail = models.IntegerField(db_column='nInitialAvail', blank=True, null=True)  # Field name made lowercase.
    ninitialrate = models.IntegerField(db_column='nInitialRate', blank=True, null=True)  # Field name made lowercase.
    nmaxavail = models.IntegerField(db_column='nMaxAvail', blank=True, null=True)  # Field name made lowercase.
    nmaxrate = models.IntegerField(db_column='nMaxRate', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    esubcategory = models.IntegerField(db_column='eSubCategory', blank=True, null=True)  # Field name made lowercase.
    bispublished = models.IntegerField(db_column='bIsPublished', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryItemInfraCategories'


class Inventoryitemleases(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    einventoryitemlease = models.IntegerField(db_column='eInventoryItemLease', blank=True, null=True)  # Field name made lowercase.
    fcostapbcashmultiplier = models.FloatField(db_column='fCostAPBCashMultiplier', blank=True, null=True)  # Field name made lowercase.
    fexpirytime = models.FloatField(db_column='fExpiryTime', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryItemLeases'


class Inventoryitemsubcategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    ecategory = models.IntegerField(db_column='eCategory', blank=True, null=True)  # Field name made lowercase.
    einventoryitemsubcategory = models.IntegerField(db_column='eInventoryItemSubCategory', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryItemSubCategories'


class Inventoryitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    screatorname = models.TextField(db_column='sCreatorName', blank=True, null=True)  # Field name made lowercase.
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    ehudimage = models.IntegerField(db_column='eHUDImage', blank=True, null=True)  # Field name made lowercase.
    einfracategory = models.IntegerField(db_column='eInfraCategory', blank=True, null=True)  # Field name made lowercase.
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    elease = models.IntegerField(db_column='eLease', blank=True, null=True)  # Field name made lowercase.
    eunlock = models.IntegerField(db_column='eUnlock', blank=True, null=True)  # Field name made lowercase.
    narmascategoryid = models.IntegerField(db_column='nArmasCategoryID', blank=True, null=True)  # Field name made lowercase.
    narmasproductid = models.IntegerField(db_column='nArmasProductID', blank=True, null=True)  # Field name made lowercase.
    narmassubcategoryid = models.IntegerField(db_column='nArmasSubcategoryID', blank=True, null=True)  # Field name made lowercase.
    ncostapbcash = models.IntegerField(db_column='nCostAPBCash', blank=True, null=True)  # Field name made lowercase.
    ncostrewardtokens = models.IntegerField(db_column='nCostRewardTokens', blank=True, null=True)  # Field name made lowercase.
    nminrating = models.IntegerField(db_column='nMinRating', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    eorganisation = models.IntegerField(db_column='eOrganisation', blank=True, null=True)  # Field name made lowercase.
    etrade = models.IntegerField(db_column='eTrade', blank=True, null=True)  # Field name made lowercase.
    bcansellback = models.IntegerField(db_column='bCanSellback', blank=True, null=True)  # Field name made lowercase.
    bcriminal = models.IntegerField(db_column='bCriminal', blank=True, null=True)  # Field name made lowercase.
    benforcer = models.IntegerField(db_column='bEnforcer', blank=True, null=True)  # Field name made lowercase.
    bgifted = models.IntegerField(db_column='bGifted', blank=True, null=True)  # Field name made lowercase.
    bignoresddvalidation = models.IntegerField(db_column='bIgnoreSddValidation', blank=True, null=True)  # Field name made lowercase.
    bisarmas = models.IntegerField(db_column='bIsArmas', blank=True, null=True)  # Field name made lowercase.
    bispublished = models.IntegerField(db_column='bIsPublished', blank=True, null=True)  # Field name made lowercase.
    bnodelete = models.IntegerField(db_column='bNoDelete', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryItemTypes'


class Invokedcontextsensitiveaction(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fduration = models.FloatField(db_column='fDuration', blank=True, null=True)  # Field name made lowercase.
    econtextsensitiveaction = models.IntegerField(db_column='eContextSensitiveAction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvokedContextSensitiveAction'


class Itemattachmentvisual(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sanimsetasset = models.TextField(db_column='sAnimSetAsset', blank=True, null=True)  # Field name made lowercase.
    sanimtreeasset = models.TextField(db_column='sAnimTreeAsset', blank=True, null=True)  # Field name made lowercase.
    sattachmentasset = models.TextField(db_column='sAttachmentAsset', blank=True, null=True)  # Field name made lowercase.
    sattachmentclass = models.TextField(db_column='sAttachmentClass', blank=True, null=True)  # Field name made lowercase.
    saudiotype = models.TextField(db_column='sAudioType', blank=True, null=True)  # Field name made lowercase.
    sphysicsasset = models.TextField(db_column='sPhysicsAsset', blank=True, null=True)  # Field name made lowercase.
    eanimtreedecision = models.IntegerField(db_column='eAnimTreeDecision', blank=True, null=True)  # Field name made lowercase.
    eitemattachmentvisual = models.IntegerField(db_column='eItemAttachmentVisual', blank=True, null=True)  # Field name made lowercase.
    euimeshviewersetup = models.IntegerField(db_column='eUIMeshViewerSetup', blank=True, null=True)  # Field name made lowercase.
    euimeshviewersetup_inventory = models.IntegerField(db_column='eUIMeshViewerSetup_Inventory', blank=True, null=True)  # Field name made lowercase.
    etaskitemanimationtype = models.IntegerField(db_column='eTaskItemAnimationType', blank=True, null=True)  # Field name made lowercase.
    blefthandikbydefault = models.IntegerField(db_column='bLeftHandIKByDefault', blank=True, null=True)  # Field name made lowercase.
    blefthandikwhileaiming = models.IntegerField(db_column='bLeftHandIKWhileAiming', blank=True, null=True)  # Field name made lowercase.
    bsuppressrunanimation = models.IntegerField(db_column='bSuppressRunAnimation', blank=True, null=True)  # Field name made lowercase.
    bsuppresssprintanimation = models.IntegerField(db_column='bSuppressSprintAnimation', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ItemAttachmentVisual'


class Itemattachmentvisualdamagestates(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sassetname = models.TextField(db_column='sAssetName', blank=True, null=True)  # Field name made lowercase.
    sdamagesfx = models.TextField(db_column='sDamageSFX', blank=True, null=True)  # Field name made lowercase.
    sdamagevfx = models.TextField(db_column='sDamageVFX', blank=True, null=True)  # Field name made lowercase.
    srecoversfx = models.TextField(db_column='sRecoverSFX', blank=True, null=True)  # Field name made lowercase.
    srecovervfx = models.TextField(db_column='sRecoverVFX', blank=True, null=True)  # Field name made lowercase.
    edamageableattachmentvisual = models.IntegerField(db_column='eDamageableAttachmentVisual', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ItemAttachmentVisualDamageStates'


class Loadingmovieaudiobanks(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nbankend = models.IntegerField(db_column='nBankEnd', blank=True, null=True)  # Field name made lowercase.
    nbankstart = models.IntegerField(db_column='nBankStart', blank=True, null=True)  # Field name made lowercase.
    eloadingmovieaudiobanks = models.IntegerField(db_column='eLoadingMovieAudioBanks', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoadingMovieAudioBanks'


class Loadingmovieconfigs(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sloadingmovie = models.TextField(db_column='sLoadingMovie', blank=True, null=True)  # Field name made lowercase.
    suiscene = models.TextField(db_column='sUIScene', blank=True, null=True)  # Field name made lowercase.
    edistrict = models.IntegerField(db_column='eDistrict', blank=True, null=True)  # Field name made lowercase.
    eloadingmovieconfig = models.IntegerField(db_column='eLoadingMovieConfig', blank=True, null=True)  # Field name made lowercase.
    nnumaudiotracks = models.IntegerField(db_column='nNumAudioTracks', blank=True, null=True)  # Field name made lowercase.
    nnumberofpages = models.IntegerField(db_column='nNumberOfPages', blank=True, null=True)  # Field name made lowercase.
    npagelength = models.IntegerField(db_column='nPageLength', blank=True, null=True)  # Field name made lowercase.
    etransitiontype = models.IntegerField(db_column='eTransitionType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoadingMovieConfigs'


class Loadingmovietips(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    smessage = models.TextField(db_column='sMessage', blank=True, null=True)  # Field name made lowercase.
    eloadingmovietip = models.IntegerField(db_column='eLoadingMovieTip', blank=True, null=True)  # Field name made lowercase.
    nmaximumrating = models.IntegerField(db_column='nMaximumRating', blank=True, null=True)  # Field name made lowercase.
    nminimumrating = models.IntegerField(db_column='nMinimumRating', blank=True, null=True)  # Field name made lowercase.
    edistrictrestriction = models.IntegerField(db_column='eDistrictRestriction', blank=True, null=True)  # Field name made lowercase.
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoadingMovieTips'


class Localetypepriorities(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    npriority = models.IntegerField(db_column='nPriority', blank=True, null=True)  # Field name made lowercase.
    elocaletypepriority = models.IntegerField(db_column='eLocaleTypePriority', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LocaleTypePriorities'


class Locationbeaconinstances(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    slocalisedname = models.TextField(db_column='sLocalisedName', blank=True, null=True)  # Field name made lowercase.
    edistrict = models.IntegerField(db_column='eDistrict', blank=True, null=True)  # Field name made lowercase.
    elocationbeaconinstance = models.IntegerField(db_column='eLocationBeaconInstance', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LocationBeaconInstances'


class Locationbeacons(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    elocationbeacon = models.IntegerField(db_column='eLocationBeacon', blank=True, null=True)  # Field name made lowercase.
    fradius = models.FloatField(db_column='fRadius', blank=True, null=True)  # Field name made lowercase.
    nheight = models.IntegerField(db_column='nHeight', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LocationBeacons'


class Mailconstants(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nvalue = models.IntegerField(db_column='nValue', blank=True, null=True)  # Field name made lowercase.
    emailconstant = models.IntegerField(db_column='eMailConstant', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MailConstants'


class Maildurations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nminutes = models.IntegerField(db_column='nMinutes', blank=True, null=True)  # Field name made lowercase.
    emailduration = models.IntegerField(db_column='eMailDuration', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MailDurations'


class Marketplacecashtype(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sresource = models.TextField(db_column='sResource', blank=True, null=True)  # Field name made lowercase.
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MarketplaceCashType'


class Marketplaceconstants(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)  # Field name made lowercase.
    emarketplaceconstant = models.IntegerField(db_column='eMarketplaceConstant', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MarketplaceConstants'


class Marketplacedurations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplaystring = models.TextField(db_column='sDisplayString', blank=True, null=True)  # Field name made lowercase.
    nminutes = models.IntegerField(db_column='nMinutes', blank=True, null=True)  # Field name made lowercase.
    emarketplaceduration = models.IntegerField(db_column='eMarketplaceDuration', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MarketplaceDurations'


class Marketplacetimeleft(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplaystring = models.TextField(db_column='sDisplayString', blank=True, null=True)  # Field name made lowercase.
    nminutes = models.IntegerField(db_column='nMinutes', blank=True, null=True)  # Field name made lowercase.
    emarketplacetimeleft = models.IntegerField(db_column='eMarketplaceTimeLeft', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MarketplaceTimeLeft'


class Medalcategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    emedalcategory = models.IntegerField(db_column='eMedalCategory', blank=True, null=True)  # Field name made lowercase.
    bexclusivemedal = models.IntegerField(db_column='bExclusiveMedal', blank=True, null=True)  # Field name made lowercase.
    bimmediateaward = models.IntegerField(db_column='bImmediateAward', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MedalCategories'


class Medals(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    stitle = models.TextField(db_column='sTitle', blank=True, null=True)  # Field name made lowercase.
    elargemedalicon = models.IntegerField(db_column='eLargeMedalIcon', blank=True, null=True)  # Field name made lowercase.
    emedal = models.IntegerField(db_column='eMedal', blank=True, null=True)  # Field name made lowercase.
    emedalicon = models.IntegerField(db_column='eMedalIcon', blank=True, null=True)  # Field name made lowercase.
    eshowcasetrackedactivity = models.IntegerField(db_column='eShowcaseTrackedActivity', blank=True, null=True)  # Field name made lowercase.
    nclassificationordinal = models.IntegerField(db_column='nClassificationOrdinal', blank=True, null=True)  # Field name made lowercase.
    nparamx = models.IntegerField(db_column='nParamX', blank=True, null=True)  # Field name made lowercase.
    nparamy = models.IntegerField(db_column='nParamY', blank=True, null=True)  # Field name made lowercase.
    nscore = models.IntegerField(db_column='nScore', blank=True, null=True)  # Field name made lowercase.
    nshowcaseorder = models.IntegerField(db_column='nShowcaseOrder', blank=True, null=True)  # Field name made lowercase.
    emedalcategory = models.IntegerField(db_column='eMedalCategory', blank=True, null=True)  # Field name made lowercase.
    escorecategory = models.IntegerField(db_column='eScoreCategory', blank=True, null=True)  # Field name made lowercase.
    eshowcasefaction = models.IntegerField(db_column='eShowcaseFaction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Medals'


class Minigameconstants(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)  # Field name made lowercase.
    eminigameconstant = models.IntegerField(db_column='eMinigameConstant', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MinigameConstants'


class Minigameeffects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sparticlesystem = models.TextField(db_column='sParticleSystem', blank=True, null=True)  # Field name made lowercase.
    ssoundeffect = models.TextField(db_column='sSoundEffect', blank=True, null=True)  # Field name made lowercase.
    eminigameeffect = models.IntegerField(db_column='eMinigameEffect', blank=True, null=True)  # Field name made lowercase.
    fmaxplaydistance = models.FloatField(db_column='fMaxPlayDistance', blank=True, null=True)  # Field name made lowercase.
    fsfxoffsetx = models.FloatField(db_column='fSFXOffsetX', blank=True, null=True)  # Field name made lowercase.
    fsfxoffsety = models.FloatField(db_column='fSFXOffsetY', blank=True, null=True)  # Field name made lowercase.
    fsfxoffsetz = models.FloatField(db_column='fSFXOffsetZ', blank=True, null=True)  # Field name made lowercase.
    fvfxoffsetx = models.FloatField(db_column='fVFXOffsetX', blank=True, null=True)  # Field name made lowercase.
    fvfxoffsety = models.FloatField(db_column='fVFXOffsetY', blank=True, null=True)  # Field name made lowercase.
    fvfxoffsetz = models.FloatField(db_column='fVFXOffsetZ', blank=True, null=True)  # Field name made lowercase.
    bplayfordeadplayers = models.IntegerField(db_column='bPlayForDeadPlayers', blank=True, null=True)  # Field name made lowercase.
    buse3dsound = models.IntegerField(db_column='bUse3DSound', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MinigameEffects'


class MinigamegungameWeaponsetupentries(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    echaractercustomisationoverride = models.IntegerField(db_column='eCharacterCustomisationOverride', blank=True, null=True)  # Field name made lowercase.
    eminigamegungame_weaponsetup = models.IntegerField(db_column='eMinigameGunGame_WeaponSetup', blank=True, null=True)  # Field name made lowercase.
    eweaponloadout = models.IntegerField(db_column='eWeaponLoadout', blank=True, null=True)  # Field name made lowercase.
    fscoremodifier = models.FloatField(db_column='fScoreModifier', blank=True, null=True)  # Field name made lowercase.
    nlevel = models.IntegerField(db_column='nLevel', blank=True, null=True)  # Field name made lowercase.
    nnextlevelrequiredkills = models.IntegerField(db_column='nNextLevelRequiredKills', blank=True, null=True)  # Field name made lowercase.
    nnextlevelrequiredscore = models.IntegerField(db_column='nNextLevelRequiredScore', blank=True, null=True)  # Field name made lowercase.
    bnextlevelrequiredscoreisabsolute = models.IntegerField(db_column='bNextLevelRequiredScoreIsAbsolute', blank=True, null=True)  # Field name made lowercase.
    bnextlevelrequiregamescorelimit = models.IntegerField(db_column='bNextLevelRequireGameScoreLimit', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MinigameGunGame_WeaponSetupEntries'


class MinigamegungameWeaponsetups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eminigamegungame_weaponsetup = models.IntegerField(db_column='eMinigameGunGame_WeaponSetup', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MinigameGunGame_WeaponSetups'


class Minigamelocations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    edistrictblock = models.IntegerField(db_column='eDistrictBlock', blank=True, null=True)  # Field name made lowercase.
    edistrictruleset = models.IntegerField(db_column='eDistrictRuleSet', blank=True, null=True)  # Field name made lowercase.
    eminigame = models.IntegerField(db_column='eMinigame', blank=True, null=True)  # Field name made lowercase.
    eminigamelocation = models.IntegerField(db_column='eMinigameLocation', blank=True, null=True)  # Field name made lowercase.
    nweight = models.IntegerField(db_column='nWeight', blank=True, null=True)  # Field name made lowercase.
    erarity = models.IntegerField(db_column='eRarity', blank=True, null=True)  # Field name made lowercase.
    espawnvariableoverride = models.IntegerField(db_column='eSpawnVariableOverride', blank=True, null=True)  # Field name made lowercase.
    ballowlocationreuse = models.IntegerField(db_column='bAllowLocationReuse', blank=True, null=True)  # Field name made lowercase.
    bentiredistrict = models.IntegerField(db_column='bEntireDistrict', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MinigameLocations'


class Minigamerewards(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eminigame = models.IntegerField(db_column='eMinigame', blank=True, null=True)  # Field name made lowercase.
    eminigamereward = models.IntegerField(db_column='eMinigameReward', blank=True, null=True)  # Field name made lowercase.
    ereward = models.IntegerField(db_column='eReward', blank=True, null=True)  # Field name made lowercase.
    ncashreward_0 = models.IntegerField(db_column='nCashReward_0', blank=True, null=True)  # Field name made lowercase.
    ncashreward_1 = models.IntegerField(db_column='nCashReward_1', blank=True, null=True)  # Field name made lowercase.
    nrewardlevel = models.IntegerField(db_column='nRewardLevel', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MinigameRewards'


class Minigamespawnerthemes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eminigamespawnertheme = models.IntegerField(db_column='eMinigameSpawnerTheme', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MinigameSpawnerThemes'


class Minigames(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    steamheaders_0 = models.TextField(db_column='sTeamHeaders_0', blank=True, null=True)  # Field name made lowercase.
    steamheaders_1 = models.TextField(db_column='sTeamHeaders_1', blank=True, null=True)  # Field name made lowercase.
    steamnames_0 = models.TextField(db_column='sTeamNames_0', blank=True, null=True)  # Field name made lowercase.
    steamnames_1 = models.TextField(db_column='sTeamNames_1', blank=True, null=True)  # Field name made lowercase.
    echaractermodifiers_0 = models.IntegerField(db_column='eCharacterModifiers_0', blank=True, null=True)  # Field name made lowercase.
    echaractermodifiers_1 = models.IntegerField(db_column='eCharacterModifiers_1', blank=True, null=True)  # Field name made lowercase.
    echaractermodifiers_2 = models.IntegerField(db_column='eCharacterModifiers_2', blank=True, null=True)  # Field name made lowercase.
    echaracteroverrides_0 = models.IntegerField(db_column='eCharacterOverrides_0', blank=True, null=True)  # Field name made lowercase.
    echaracteroverrides_1 = models.IntegerField(db_column='eCharacterOverrides_1', blank=True, null=True)  # Field name made lowercase.
    echaracteroverrides_2 = models.IntegerField(db_column='eCharacterOverrides_2', blank=True, null=True)  # Field name made lowercase.
    eendeffect = models.IntegerField(db_column='eEndEffect', blank=True, null=True)  # Field name made lowercase.
    eminigame = models.IntegerField(db_column='eMinigame', blank=True, null=True)  # Field name made lowercase.
    eonmissionhudmarkervisual = models.IntegerField(db_column='eOnMissionHUDMarkerVisual', blank=True, null=True)  # Field name made lowercase.
    eoutofmissionhudmarkervisual = models.IntegerField(db_column='eOutOfMissionHUDMarkerVisual', blank=True, null=True)  # Field name made lowercase.
    espawnertheme = models.IntegerField(db_column='eSpawnerTheme', blank=True, null=True)  # Field name made lowercase.
    estarteffect = models.IntegerField(db_column='eStartEffect', blank=True, null=True)  # Field name made lowercase.
    etimeouteffect = models.IntegerField(db_column='eTimeoutEffect', blank=True, null=True)  # Field name made lowercase.
    evehicleoverrides_0 = models.IntegerField(db_column='eVehicleOverrides_0', blank=True, null=True)  # Field name made lowercase.
    evehicleoverrides_1 = models.IntegerField(db_column='eVehicleOverrides_1', blank=True, null=True)  # Field name made lowercase.
    evehicleoverrides_2 = models.IntegerField(db_column='eVehicleOverrides_2', blank=True, null=True)  # Field name made lowercase.
    eweaponloadouts_0 = models.IntegerField(db_column='eWeaponLoadouts_0', blank=True, null=True)  # Field name made lowercase.
    eweaponloadouts_1 = models.IntegerField(db_column='eWeaponLoadouts_1', blank=True, null=True)  # Field name made lowercase.
    eweaponloadouts_2 = models.IntegerField(db_column='eWeaponLoadouts_2', blank=True, null=True)  # Field name made lowercase.
    fabandontimeout = models.FloatField(db_column='fAbandonTimeout', blank=True, null=True)  # Field name made lowercase.
    fintroductiontime = models.FloatField(db_column='fIntroductionTime', blank=True, null=True)  # Field name made lowercase.
    ftimeoutnotifyinterval = models.FloatField(db_column='fTimeoutNotifyInterval', blank=True, null=True)  # Field name made lowercase.
    ftimeoutnotifystart = models.FloatField(db_column='fTimeoutNotifyStart', blank=True, null=True)  # Field name made lowercase.
    ftimetoclearplayers = models.FloatField(db_column='fTimeToClearPlayers', blank=True, null=True)  # Field name made lowercase.
    nmaxbonuscash = models.IntegerField(db_column='nMaxBonusCash', blank=True, null=True)  # Field name made lowercase.
    nminimumplayercount_0 = models.IntegerField(db_column='nMinimumPlayerCount_0', blank=True, null=True)  # Field name made lowercase.
    nminimumplayercount_1 = models.IntegerField(db_column='nMinimumPlayerCount_1', blank=True, null=True)  # Field name made lowercase.
    nscoreeventsforparticipation = models.IntegerField(db_column='nScoreEventsForParticipation', blank=True, null=True)  # Field name made lowercase.
    nscoreminimumforparticipation = models.IntegerField(db_column='nScoreMinimumForParticipation', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    espawnvariable = models.IntegerField(db_column='eSpawnVariable', blank=True, null=True)  # Field name made lowercase.
    etype = models.IntegerField(db_column='eType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Minigames'


class MinigamesBlockfdm(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eminigame = models.IntegerField(db_column='eMinigame', blank=True, null=True)  # Field name made lowercase.
    fdeadparticipationtimer = models.FloatField(db_column='fDeadParticipationTimer', blank=True, null=True)  # Field name made lowercase.
    flowteamcountscale = models.FloatField(db_column='fLowTeamCountScale', blank=True, null=True)  # Field name made lowercase.
    flowteaminitialstartuptimer = models.FloatField(db_column='fLowTeamInitialStartupTimer', blank=True, null=True)  # Field name made lowercase.
    flowteaminitialtimer = models.FloatField(db_column='fLowTeamInitialTimer', blank=True, null=True)  # Field name made lowercase.
    flowteamlivesremovallinearportion = models.FloatField(db_column='fLowTeamLivesRemovalLinearPortion', blank=True, null=True)  # Field name made lowercase.
    flowteamlivesremovalquadraticportion = models.FloatField(db_column='fLowTeamLivesRemovalQuadraticPortion', blank=True, null=True)  # Field name made lowercase.
    foobparticipationtimer = models.FloatField(db_column='fOOBParticipationTimer', blank=True, null=True)  # Field name made lowercase.
    foutofboundstime = models.FloatField(db_column='fOutOfBoundsTime', blank=True, null=True)  # Field name made lowercase.
    nminnumlives = models.IntegerField(db_column='nMinNumLives', blank=True, null=True)  # Field name made lowercase.
    nnumberoflivesperplayer = models.IntegerField(db_column='nNumberOfLivesPerPlayer', blank=True, null=True)  # Field name made lowercase.
    bcountarrests = models.IntegerField(db_column='bCountArrests', blank=True, null=True)  # Field name made lowercase.
    bignoreallsuicides = models.IntegerField(db_column='bIgnoreAllSuicides', blank=True, null=True)  # Field name made lowercase.
    bignorefriendlykills = models.IntegerField(db_column='bIgnoreFriendlyKills', blank=True, null=True)  # Field name made lowercase.
    bignoregmsuicides = models.IntegerField(db_column='bIgnoreGMSuicides', blank=True, null=True)  # Field name made lowercase.
    bignorekillsbothoob = models.IntegerField(db_column='bIgnoreKillsBothOOB', blank=True, null=True)  # Field name made lowercase.
    bignorekillsbyweaponsotherthanloadout = models.IntegerField(db_column='bIgnoreKillsByWeaponsOtherThanLoadout', blank=True, null=True)  # Field name made lowercase.
    bignorekillskilledoob = models.IntegerField(db_column='bIgnoreKillsKilledOOB', blank=True, null=True)  # Field name made lowercase.
    bignorekillskillernotinminigame = models.IntegerField(db_column='bIgnoreKillsKillerNotInMinigame', blank=True, null=True)  # Field name made lowercase.
    bignorekillskilleroob = models.IntegerField(db_column='bIgnoreKillsKillerOOB', blank=True, null=True)  # Field name made lowercase.
    bignorenonweaponexplosions = models.IntegerField(db_column='bIgnoreNonWeaponExplosions', blank=True, null=True)  # Field name made lowercase.
    bignoreroadkills = models.IntegerField(db_column='bIgnoreRoadKills', blank=True, null=True)  # Field name made lowercase.
    bignoresuicideoob = models.IntegerField(db_column='bIgnoreSuicideOOB', blank=True, null=True)  # Field name made lowercase.
    bignoresuicidewithoutassist = models.IntegerField(db_column='bIgnoreSuicideWithoutAssist', blank=True, null=True)  # Field name made lowercase.
    bignoresuicidewithoutenemyassist = models.IntegerField(db_column='bIgnoreSuicideWithoutEnemyAssist', blank=True, null=True)  # Field name made lowercase.
    bignoresuicidewithoutfriendlyassist = models.IntegerField(db_column='bIgnoreSuicideWithoutFriendlyAssist', blank=True, null=True)  # Field name made lowercase.
    bsetdeathmatchtarget = models.IntegerField(db_column='bSetDeathMatchTarget', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Minigames_BlockFDM'


class MinigamesGoldengun(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    spickupasset = models.TextField(db_column='sPickupAsset', blank=True, null=True)  # Field name made lowercase.
    spickupsfx = models.TextField(db_column='sPickupSFX', blank=True, null=True)  # Field name made lowercase.
    spickupvfx = models.TextField(db_column='sPickupVFX', blank=True, null=True)  # Field name made lowercase.
    eminigame = models.IntegerField(db_column='eMinigame', blank=True, null=True)  # Field name made lowercase.
    eonmissionprotagonisthudmarker = models.IntegerField(db_column='eOnMissionProtagonistHUDMarker', blank=True, null=True)  # Field name made lowercase.
    eoutofmissionprotagonisthudmarker = models.IntegerField(db_column='eOutOfMissionProtagonistHUDMarker', blank=True, null=True)  # Field name made lowercase.
    fmaxpickuptime = models.FloatField(db_column='fMaxPickupTime', blank=True, null=True)  # Field name made lowercase.
    fremovealivetime = models.FloatField(db_column='fRemoveAliveTime', blank=True, null=True)  # Field name made lowercase.
    fremovedeadtime = models.FloatField(db_column='fRemoveDeadTime', blank=True, null=True)  # Field name made lowercase.
    fremovedistance = models.FloatField(db_column='fRemoveDistance', blank=True, null=True)  # Field name made lowercase.
    ftotalminigametimeouttime = models.FloatField(db_column='fTotalMinigameTimeoutTime', blank=True, null=True)  # Field name made lowercase.
    nkilltarget = models.IntegerField(db_column='nKillTarget', blank=True, null=True)  # Field name made lowercase.
    busesingleteam = models.IntegerField(db_column='bUseSingleTeam', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Minigames_GoldenGun'


class MinigamesGungame(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eminigame = models.IntegerField(db_column='eMinigame', blank=True, null=True)  # Field name made lowercase.
    eweaponsetup = models.IntegerField(db_column='eWeaponSetup', blank=True, null=True)  # Field name made lowercase.
    fdeadparticipationtimer = models.FloatField(db_column='fDeadParticipationTimer', blank=True, null=True)  # Field name made lowercase.
    fminrespawndistance = models.FloatField(db_column='fMinRespawnDistance', blank=True, null=True)  # Field name made lowercase.
    foobparticipationtimer = models.FloatField(db_column='fOOBParticipationTimer', blank=True, null=True)  # Field name made lowercase.
    foutofboundstime = models.FloatField(db_column='fOutOfBoundsTime', blank=True, null=True)  # Field name made lowercase.
    ftotalgametimeout = models.FloatField(db_column='fTotalGameTimeout', blank=True, null=True)  # Field name made lowercase.
    nacckillchangeonarrest = models.IntegerField(db_column='nAccKillChangeOnArrest', blank=True, null=True)  # Field name made lowercase.
    nacckillchangeondeath = models.IntegerField(db_column='nAccKillChangeOnDeath', blank=True, null=True)  # Field name made lowercase.
    nacckillchangeonnonweapondeath = models.IntegerField(db_column='nAccKillChangeOnNonWeaponDeath', blank=True, null=True)  # Field name made lowercase.
    nacckillchangeonsuicide = models.IntegerField(db_column='nAccKillChangeOnSuicide', blank=True, null=True)  # Field name made lowercase.
    naccscorechangeonarrest = models.IntegerField(db_column='nAccScoreChangeOnArrest', blank=True, null=True)  # Field name made lowercase.
    naccscorechangeondeath = models.IntegerField(db_column='nAccScoreChangeOnDeath', blank=True, null=True)  # Field name made lowercase.
    naccscorechangeonnonweapondeath = models.IntegerField(db_column='nAccScoreChangeOnNonWeaponDeath', blank=True, null=True)  # Field name made lowercase.
    naccscorechangeonsuicide = models.IntegerField(db_column='nAccScoreChangeOnSuicide', blank=True, null=True)  # Field name made lowercase.
    nlevelchangeonarrest = models.IntegerField(db_column='nLevelChangeOnArrest', blank=True, null=True)  # Field name made lowercase.
    nlevelchangeondeath = models.IntegerField(db_column='nLevelChangeOnDeath', blank=True, null=True)  # Field name made lowercase.
    nlevelchangeonnonweapondeath = models.IntegerField(db_column='nLevelChangeOnNonWeaponDeath', blank=True, null=True)  # Field name made lowercase.
    nlevelchangeonsuicide = models.IntegerField(db_column='nLevelChangeOnSuicide', blank=True, null=True)  # Field name made lowercase.
    nscorelimit = models.IntegerField(db_column='nScoreLimit', blank=True, null=True)  # Field name made lowercase.
    ballowscorelevelup = models.IntegerField(db_column='bAllowScoreLevelUp', blank=True, null=True)  # Field name made lowercase.
    bcountarrests = models.IntegerField(db_column='bCountArrests', blank=True, null=True)  # Field name made lowercase.
    bcountassignedsuicides = models.IntegerField(db_column='bCountAssignedSuicides', blank=True, null=True)  # Field name made lowercase.
    bcountnonweaponkills = models.IntegerField(db_column='bCountNonWeaponKills', blank=True, null=True)  # Field name made lowercase.
    bdisablepostitivemedalscore = models.IntegerField(db_column='bDisablePostitiveMedalScore', blank=True, null=True)  # Field name made lowercase.
    bforcelastweapononscorelimit = models.IntegerField(db_column='bForceLastWeaponOnScoreLimit', blank=True, null=True)  # Field name made lowercase.
    blockoutofarea = models.IntegerField(db_column='bLockOutOfArea', blank=True, null=True)  # Field name made lowercase.
    bmultiplyaccscorechanges = models.IntegerField(db_column='bMultiplyAccScoreChanges', blank=True, null=True)  # Field name made lowercase.
    breducelevelonnegativeacckills = models.IntegerField(db_column='bReduceLevelOnNegativeAccKills', blank=True, null=True)  # Field name made lowercase.
    breducelevelonnegativeaccscore = models.IntegerField(db_column='bReduceLevelOnNegativeAccScore', blank=True, null=True)  # Field name made lowercase.
    brequirekillwithfinalweapon = models.IntegerField(db_column='bRequireKillWithFinalWeapon', blank=True, null=True)  # Field name made lowercase.
    bscorenonweaponkills = models.IntegerField(db_column='bScoreNonWeaponKills', blank=True, null=True)  # Field name made lowercase.
    bspawncompletelyrandom = models.IntegerField(db_column='bSpawnCompletelyRandom', blank=True, null=True)  # Field name made lowercase.
    busesingleteam = models.IntegerField(db_column='bUseSingleTeam', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Minigames_GunGame'


class MinigamesInfection(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eendblockidentifier = models.IntegerField(db_column='eEndBlockIdentifier', blank=True, null=True)  # Field name made lowercase.
    eminigame = models.IntegerField(db_column='eMinigame', blank=True, null=True)  # Field name made lowercase.
    eprotagonistonmissionhudmarker = models.IntegerField(db_column='eProtagonistOnMissionHUDMarker', blank=True, null=True)  # Field name made lowercase.
    esurvivorpinghudmarker = models.IntegerField(db_column='eSurvivorPingHUDMarker', blank=True, null=True)  # Field name made lowercase.
    finfectedmajoritytimer = models.FloatField(db_column='fInfectedMajorityTimer', blank=True, null=True)  # Field name made lowercase.
    finfectedscoremultipliermax = models.FloatField(db_column='fInfectedScoreMultiplierMax', blank=True, null=True)  # Field name made lowercase.
    finfectedscoremultipliermin = models.FloatField(db_column='fInfectedScoreMultiplierMin', blank=True, null=True)  # Field name made lowercase.
    fminimumsurvivoraddtime = models.FloatField(db_column='fMinimumSurvivorAddTime', blank=True, null=True)  # Field name made lowercase.
    fnosurvivorslefttimer = models.FloatField(db_column='fNoSurvivorsLeftTimer', blank=True, null=True)  # Field name made lowercase.
    fprotagonistkillscoremultiplier = models.FloatField(db_column='fProtagonistKillScoreMultiplier', blank=True, null=True)  # Field name made lowercase.
    fprotagonistscoremultipliermax = models.FloatField(db_column='fProtagonistScoreMultiplierMax', blank=True, null=True)  # Field name made lowercase.
    fprotagonistscoremultipliermin = models.FloatField(db_column='fProtagonistScoreMultiplierMin', blank=True, null=True)  # Field name made lowercase.
    fsurvivormajorityratio = models.FloatField(db_column='fSurvivorMajorityRatio', blank=True, null=True)  # Field name made lowercase.
    fsurvivorpingduration = models.FloatField(db_column='fSurvivorPingDuration', blank=True, null=True)  # Field name made lowercase.
    fsurvivorpinginterval = models.FloatField(db_column='fSurvivorPingInterval', blank=True, null=True)  # Field name made lowercase.
    fsurvivorscoremultipliermax = models.FloatField(db_column='fSurvivorScoreMultiplierMax', blank=True, null=True)  # Field name made lowercase.
    fsurvivorscoremultipliermin = models.FloatField(db_column='fSurvivorScoreMultiplierMin', blank=True, null=True)  # Field name made lowercase.
    ftotalgametimeout = models.FloatField(db_column='fTotalGameTimeout', blank=True, null=True)  # Field name made lowercase.
    badjustassistscore = models.IntegerField(db_column='bAdjustAssistScore', blank=True, null=True)  # Field name made lowercase.
    badjustmedalscore = models.IntegerField(db_column='bAdjustMedalScore', blank=True, null=True)  # Field name made lowercase.
    badjustnegativescore = models.IntegerField(db_column='bAdjustNegativeScore', blank=True, null=True)  # Field name made lowercase.
    badjustnonplayerkillinfrarewards = models.IntegerField(db_column='bAdjustNonPlayerKillInfraRewards', blank=True, null=True)  # Field name made lowercase.
    badjustplayerconvertedleaderscore = models.IntegerField(db_column='bAdjustPlayerConvertedLeaderScore', blank=True, null=True)  # Field name made lowercase.
    badjustplayerconvertedscore = models.IntegerField(db_column='bAdjustPlayerConvertedScore', blank=True, null=True)  # Field name made lowercase.
    bendminigameinblock = models.IntegerField(db_column='bEndMinigameInBlock', blank=True, null=True)  # Field name made lowercase.
    bkillallinfectedatstop = models.IntegerField(db_column='bKillAllInfectedAtStop', blank=True, null=True)  # Field name made lowercase.
    bkillallplayersatstop = models.IntegerField(db_column='bKillAllPlayersAtStop', blank=True, null=True)  # Field name made lowercase.
    bkillplayerbecomingprotagonist = models.IntegerField(db_column='bKillPlayerBecomingProtagonist', blank=True, null=True)  # Field name made lowercase.
    bleaderbecomessurvivorwhenkilled = models.IntegerField(db_column='bLeaderBecomesSurvivorWhenKilled', blank=True, null=True)  # Field name made lowercase.
    bprotagonistpingswithsurvivors = models.IntegerField(db_column='bProtagonistPingsWithSurvivors', blank=True, null=True)  # Field name made lowercase.
    bprotagonistvisibleduringsurvivormajority = models.IntegerField(db_column='bProtagonistVisibleDuringSurvivorMajority', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Minigames_Infection'


class MinigamesInfectionItemcollection(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eitemtype = models.IntegerField(db_column='eItemType', blank=True, null=True)  # Field name made lowercase.
    eminigame_infection = models.IntegerField(db_column='eMinigame_Infection', blank=True, null=True)  # Field name made lowercase.
    etaskitemoperation = models.IntegerField(db_column='eTaskItemOperation', blank=True, null=True)  # Field name made lowercase.
    ffailedspawnretrytimer = models.FloatField(db_column='fFailedSpawnRetryTimer', blank=True, null=True)  # Field name made lowercase.
    fitemcollectiontimeout = models.FloatField(db_column='fItemCollectionTimeout', blank=True, null=True)  # Field name made lowercase.
    navailabletaskitems = models.IntegerField(db_column='nAvailableTaskItems', blank=True, null=True)  # Field name made lowercase.
    nminimumitemstaken = models.IntegerField(db_column='nMinimumItemsTaken', blank=True, null=True)  # Field name made lowercase.
    nrequiredtaskitemcounts = models.IntegerField(db_column='nRequiredTaskItemCounts', blank=True, null=True)  # Field name made lowercase.
    nspawnercount = models.IntegerField(db_column='nSpawnerCount', blank=True, null=True)  # Field name made lowercase.
    ntargetitemstaken = models.IntegerField(db_column='nTargetItemsTaken', blank=True, null=True)  # Field name made lowercase.
    bblockpickups = models.IntegerField(db_column='bBlockPickups', blank=True, null=True)  # Field name made lowercase.
    bcandeliveritems = models.IntegerField(db_column='bCanDeliverItems', blank=True, null=True)  # Field name made lowercase.
    bcandropsmallitems = models.IntegerField(db_column='bCanDropSmallItems', blank=True, null=True)  # Field name made lowercase.
    bcountdelivereditems = models.IntegerField(db_column='bCountDeliveredItems', blank=True, null=True)  # Field name made lowercase.
    bcountdestroyeditems = models.IntegerField(db_column='bCountDestroyedItems', blank=True, null=True)  # Field name made lowercase.
    bcountpickedupitems = models.IntegerField(db_column='bCountPickedUpItems', blank=True, null=True)  # Field name made lowercase.
    bitemsinsingleblock = models.IntegerField(db_column='bItemsInSingleBlock', blank=True, null=True)  # Field name made lowercase.
    bleaderassignedbyscore = models.IntegerField(db_column='bLeaderAssignedByScore', blank=True, null=True)  # Field name made lowercase.
    blimitspawnerstoselectedblock = models.IntegerField(db_column='bLimitSpawnersToSelectedBlock', blank=True, null=True)  # Field name made lowercase.
    brespawndelivereditems = models.IntegerField(db_column='bRespawnDeliveredItems', blank=True, null=True)  # Field name made lowercase.
    brespawndestroyeditems = models.IntegerField(db_column='bRespawnDestroyedItems', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Minigames_Infection_ItemCollection'


class MinigamesInfectionRichfx(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sendstagemusic_start = models.TextField(db_column='sEndStageMusic_Start', blank=True, null=True)  # Field name made lowercase.
    sendstagemusic_stop = models.TextField(db_column='sEndStageMusic_Stop', blank=True, null=True)  # Field name made lowercase.
    soverrideweather = models.TextField(db_column='sOverrideWeather', blank=True, null=True)  # Field name made lowercase.
    einfectedspawnfx_female = models.IntegerField(db_column='eInfectedSpawnFX_Female', blank=True, null=True)  # Field name made lowercase.
    einfectedspawnfx_male = models.IntegerField(db_column='eInfectedSpawnFX_Male', blank=True, null=True)  # Field name made lowercase.
    eminigame_infection = models.IntegerField(db_column='eMinigame_Infection', blank=True, null=True)  # Field name made lowercase.
    eplayerpingfx = models.IntegerField(db_column='ePlayerPingFX', blank=True, null=True)  # Field name made lowercase.
    eprotagonistassignedfx = models.IntegerField(db_column='eProtagonistAssignedFX', blank=True, null=True)  # Field name made lowercase.
    eprotagonistkillfx = models.IntegerField(db_column='eProtagonistKillFX', blank=True, null=True)  # Field name made lowercase.
    eprotagonistspawnfx_female = models.IntegerField(db_column='eProtagonistSpawnFX_Female', blank=True, null=True)  # Field name made lowercase.
    eprotagonistspawnfx_male = models.IntegerField(db_column='eProtagonistSpawnFX_Male', blank=True, null=True)  # Field name made lowercase.
    nendtodhours = models.IntegerField(db_column='nEndToDHours', blank=True, null=True)  # Field name made lowercase.
    nendtodminutes = models.IntegerField(db_column='nEndToDMinutes', blank=True, null=True)  # Field name made lowercase.
    npausetodhours = models.IntegerField(db_column='nPauseToDHours', blank=True, null=True)  # Field name made lowercase.
    npausetodminutes = models.IntegerField(db_column='nPauseToDMinutes', blank=True, null=True)  # Field name made lowercase.
    bendtodstartswithinfectedmajority = models.IntegerField(db_column='bEndToDStartsWithInfectedMajority', blank=True, null=True)  # Field name made lowercase.
    bforcerestoreweather = models.IntegerField(db_column='bForceRestoreWeather', blank=True, null=True)  # Field name made lowercase.
    bpausetod = models.IntegerField(db_column='bPauseToD', blank=True, null=True)  # Field name made lowercase.
    bplayprotagonistkillfromkilledlocation = models.IntegerField(db_column='bPlayProtagonistKillFromKilledLocation', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Minigames_Infection_RichFX'


class MinigamesInfectionVip(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eminigame_infection = models.IntegerField(db_column='eMinigame_Infection', blank=True, null=True)  # Field name made lowercase.
    nlowheatgroupchance = models.IntegerField(db_column='nLowHeatGroupChance', blank=True, null=True)  # Field name made lowercase.
    nmaxheatgroupchance = models.IntegerField(db_column='nMaxHeatGroupChance', blank=True, null=True)  # Field name made lowercase.
    nmaxheatungroupedchance = models.IntegerField(db_column='nMaxHeatUngroupedChance', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Minigames_Infection_VIP'


class MinigamesMug(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    splayerinmugrangeaudio = models.TextField(db_column='sPlayerInMugRangeAudio', blank=True, null=True)  # Field name made lowercase.
    ecarrierhudmarker_0 = models.IntegerField(db_column='eCarrierHUDMarker_0', blank=True, null=True)  # Field name made lowercase.
    ecarrierhudmarker_1 = models.IntegerField(db_column='eCarrierHUDMarker_1', blank=True, null=True)  # Field name made lowercase.
    ecarrierhudmarker_2 = models.IntegerField(db_column='eCarrierHUDMarker_2', blank=True, null=True)  # Field name made lowercase.
    ecarrierhudmarker_3 = models.IntegerField(db_column='eCarrierHUDMarker_3', blank=True, null=True)  # Field name made lowercase.
    ecarrierhudmarker_4 = models.IntegerField(db_column='eCarrierHUDMarker_4', blank=True, null=True)  # Field name made lowercase.
    edeliveryeffect_0 = models.IntegerField(db_column='eDeliveryEffect_0', blank=True, null=True)  # Field name made lowercase.
    edeliveryeffect_1 = models.IntegerField(db_column='eDeliveryEffect_1', blank=True, null=True)  # Field name made lowercase.
    edeliveryeffect_2 = models.IntegerField(db_column='eDeliveryEffect_2', blank=True, null=True)  # Field name made lowercase.
    edeliveryeffect_3 = models.IntegerField(db_column='eDeliveryEffect_3', blank=True, null=True)  # Field name made lowercase.
    einvulerableeffect = models.IntegerField(db_column='eInvulerableEffect', blank=True, null=True)  # Field name made lowercase.
    eitemspawnrule_0 = models.IntegerField(db_column='eItemSpawnRule_0', blank=True, null=True)  # Field name made lowercase.
    eitemspawnrule_1 = models.IntegerField(db_column='eItemSpawnRule_1', blank=True, null=True)  # Field name made lowercase.
    ekillcarriereffect = models.IntegerField(db_column='eKillCarrierEffect', blank=True, null=True)  # Field name made lowercase.
    eminigame = models.IntegerField(db_column='eMinigame', blank=True, null=True)  # Field name made lowercase.
    emugcompleteeffect = models.IntegerField(db_column='eMugCompleteEffect', blank=True, null=True)  # Field name made lowercase.
    enpchudmarker_0 = models.IntegerField(db_column='eNPCHudMarker_0', blank=True, null=True)  # Field name made lowercase.
    enpchudmarker_1 = models.IntegerField(db_column='eNPCHudMarker_1', blank=True, null=True)  # Field name made lowercase.
    enpckillitemspawnrule_0 = models.IntegerField(db_column='eNPCKillItemSpawnRule_0', blank=True, null=True)  # Field name made lowercase.
    enpckillitemspawnrule_1 = models.IntegerField(db_column='eNPCKillItemSpawnRule_1', blank=True, null=True)  # Field name made lowercase.
    enpcoperation_0 = models.IntegerField(db_column='eNPCOperation_0', blank=True, null=True)  # Field name made lowercase.
    enpcoperation_1 = models.IntegerField(db_column='eNPCOperation_1', blank=True, null=True)  # Field name made lowercase.
    enpctype_0 = models.IntegerField(db_column='eNPCType_0', blank=True, null=True)  # Field name made lowercase.
    enpctype_1 = models.IntegerField(db_column='eNPCType_1', blank=True, null=True)  # Field name made lowercase.
    eoomcarrierhudmarker_0 = models.IntegerField(db_column='eOOMCarrierHUDMarker_0', blank=True, null=True)  # Field name made lowercase.
    eoomcarrierhudmarker_1 = models.IntegerField(db_column='eOOMCarrierHUDMarker_1', blank=True, null=True)  # Field name made lowercase.
    eoomcarrierhudmarker_2 = models.IntegerField(db_column='eOOMCarrierHUDMarker_2', blank=True, null=True)  # Field name made lowercase.
    eoomcarrierhudmarker_3 = models.IntegerField(db_column='eOOMCarrierHUDMarker_3', blank=True, null=True)  # Field name made lowercase.
    eoomcarrierhudmarker_4 = models.IntegerField(db_column='eOOMCarrierHUDMarker_4', blank=True, null=True)  # Field name made lowercase.
    eoomprotagonisthudmarker = models.IntegerField(db_column='eOOMProtagonistHUDMarker', blank=True, null=True)  # Field name made lowercase.
    eprotagonisthudmarker = models.IntegerField(db_column='eProtagonistHUDMarker', blank=True, null=True)  # Field name made lowercase.
    etaskitemhudmarker = models.IntegerField(db_column='eTaskItemHudMarker', blank=True, null=True)  # Field name made lowercase.
    etaskitemoperation = models.IntegerField(db_column='eTaskItemOperation', blank=True, null=True)  # Field name made lowercase.
    fdeliverymultiplier_0 = models.FloatField(db_column='fDeliveryMultiplier_0', blank=True, null=True)  # Field name made lowercase.
    fdeliverymultiplier_1 = models.FloatField(db_column='fDeliveryMultiplier_1', blank=True, null=True)  # Field name made lowercase.
    fdeliverymultiplier_2 = models.FloatField(db_column='fDeliveryMultiplier_2', blank=True, null=True)  # Field name made lowercase.
    fdeliverymultiplier_3 = models.FloatField(db_column='fDeliveryMultiplier_3', blank=True, null=True)  # Field name made lowercase.
    fimmunityaudiotime = models.FloatField(db_column='fImmunityAudioTime', blank=True, null=True)  # Field name made lowercase.
    fimmunitytimeout = models.FloatField(db_column='fImmunityTimeout', blank=True, null=True)  # Field name made lowercase.
    finactivitytimeouttime = models.FloatField(db_column='fInactivityTimeoutTime', blank=True, null=True)  # Field name made lowercase.
    fmaxnpctime = models.FloatField(db_column='fMaxNPCTime', blank=True, null=True)  # Field name made lowercase.
    fnodropkilltransfer = models.FloatField(db_column='fNoDropKillTransfer', blank=True, null=True)  # Field name made lowercase.
    fnodropmugtransfer = models.FloatField(db_column='fNoDropMugTransfer', blank=True, null=True)  # Field name made lowercase.
    fnodropsuicidepenalty = models.FloatField(db_column='fNoDropSuicidePenalty', blank=True, null=True)  # Field name made lowercase.
    fnpcchance_0 = models.FloatField(db_column='fNPCChance_0', blank=True, null=True)  # Field name made lowercase.
    fnpcchance_1 = models.FloatField(db_column='fNPCChance_1', blank=True, null=True)  # Field name made lowercase.
    fnpccountperplayer = models.FloatField(db_column='fNPCCountPerPlayer', blank=True, null=True)  # Field name made lowercase.
    fnpcmugimmunityduration = models.FloatField(db_column='fNPCMugImmunityDuration', blank=True, null=True)  # Field name made lowercase.
    fplayermugimmunityduration = models.FloatField(db_column='fPlayerMugImmunityDuration', blank=True, null=True)  # Field name made lowercase.
    fpostimmunitymugtimeout = models.FloatField(db_column='fPostImmunityMugTimeout', blank=True, null=True)  # Field name made lowercase.
    fprotagonistkillmultiplier = models.FloatField(db_column='fProtagonistKillMultiplier', blank=True, null=True)  # Field name made lowercase.
    fremovedistance = models.FloatField(db_column='fRemoveDistance', blank=True, null=True)  # Field name made lowercase.
    fremovetimealive = models.FloatField(db_column='fRemoveTimeAlive', blank=True, null=True)  # Field name made lowercase.
    fremovetimedead = models.FloatField(db_column='fRemoveTimeDead', blank=True, null=True)  # Field name made lowercase.
    frespawnwithitemsimmunity = models.FloatField(db_column='fRespawnWithItemsImmunity', blank=True, null=True)  # Field name made lowercase.
    ftaskitemcleanuptime = models.FloatField(db_column='fTaskItemCleanupTime', blank=True, null=True)  # Field name made lowercase.
    ftotalminigametimeouttime = models.FloatField(db_column='fTotalMinigameTimeoutTime', blank=True, null=True)  # Field name made lowercase.
    ndeliverlimit = models.IntegerField(db_column='nDeliverLimit', blank=True, null=True)  # Field name made lowercase.
    nnpccount = models.IntegerField(db_column='nNPCCount', blank=True, null=True)  # Field name made lowercase.
    nnpccountlimit = models.IntegerField(db_column='nNPCCountLimit', blank=True, null=True)  # Field name made lowercase.
    noverridekillscore = models.IntegerField(db_column='nOverrideKillScore', blank=True, null=True)  # Field name made lowercase.
    bcandropoffitems = models.IntegerField(db_column='bCanDropOffItems', blank=True, null=True)  # Field name made lowercase.
    bcanmugplayers = models.IntegerField(db_column='bCanMugPlayers', blank=True, null=True)  # Field name made lowercase.
    bdisableprimaryscore = models.IntegerField(db_column='bDisablePrimaryScore', blank=True, null=True)  # Field name made lowercase.
    bhideplayerradarmarkers = models.IntegerField(db_column='bHidePlayerRadarMarkers', blank=True, null=True)  # Field name made lowercase.
    bkillmuggedplayers = models.IntegerField(db_column='bKillMuggedPlayers', blank=True, null=True)  # Field name made lowercase.
    bkillnpcwhendone = models.IntegerField(db_column='bKillNPCWhenDone', blank=True, null=True)  # Field name made lowercase.
    bkillnpcwhendonemugging = models.IntegerField(db_column='bKillNPCWhenDoneMugging', blank=True, null=True)  # Field name made lowercase.
    bmultimug = models.IntegerField(db_column='bMultiMug', blank=True, null=True)  # Field name made lowercase.
    bmultiplydelivereditemnumbers = models.IntegerField(db_column='bMultiplyDeliveredItemNumbers', blank=True, null=True)  # Field name made lowercase.
    bnodrops = models.IntegerField(db_column='bNoDrops', blank=True, null=True)  # Field name made lowercase.
    bnodroptransfergainonly = models.IntegerField(db_column='bNoDropTransferGainOnly', blank=True, null=True)  # Field name made lowercase.
    bnpcmarkersafterfirstmug = models.IntegerField(db_column='bNPCMarkersAfterFirstMug', blank=True, null=True)  # Field name made lowercase.
    bnpcmugusesimmunitytimeout = models.IntegerField(db_column='bNPCMugUsesImmunityTimeout', blank=True, null=True)  # Field name made lowercase.
    bopposeallcarriers = models.IntegerField(db_column='bOpposeAllCarriers', blank=True, null=True)  # Field name made lowercase.
    boverridetitle = models.IntegerField(db_column='bOverrideTitle', blank=True, null=True)  # Field name made lowercase.
    bpvpunlockallcarriers = models.IntegerField(db_column='bPvPUnlockAllCarriers', blank=True, null=True)  # Field name made lowercase.
    bpvpunlockprotagonist = models.IntegerField(db_column='bPVPUnlockProtagonist', blank=True, null=True)  # Field name made lowercase.
    bshowcarrierstoall = models.IntegerField(db_column='bShowCarriersToAll', blank=True, null=True)  # Field name made lowercase.
    busedeliverymultipliers = models.IntegerField(db_column='bUseDeliveryMultipliers', blank=True, null=True)  # Field name made lowercase.
    busesingleteam = models.IntegerField(db_column='bUseSingleTeam', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Minigames_Mug'


class MinigamesVip(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eminigame = models.IntegerField(db_column='eMinigame', blank=True, null=True)  # Field name made lowercase.
    fvipwintime = models.FloatField(db_column='fVIPWinTime', blank=True, null=True)  # Field name made lowercase.
    nlowheatgroupchance = models.IntegerField(db_column='nLowHeatGroupChance', blank=True, null=True)  # Field name made lowercase.
    nmaxheatgroupchance = models.IntegerField(db_column='nMaxHeatGroupChance', blank=True, null=True)  # Field name made lowercase.
    nmaxheatungroupedchance = models.IntegerField(db_column='nMaxHeatUngroupedChance', blank=True, null=True)  # Field name made lowercase.
    nvipwinkills = models.IntegerField(db_column='nVIPWinKills', blank=True, null=True)  # Field name made lowercase.
    bbulklog = models.IntegerField(db_column='bBulkLog', blank=True, null=True)  # Field name made lowercase.
    bkillbodyguardsatstart = models.IntegerField(db_column='bKillBodyGuardsAtStart', blank=True, null=True)  # Field name made lowercase.
    bkillvipatstart = models.IntegerField(db_column='bKillVIPAtStart', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Minigames_VIP'


class Missionofcriminalcontacts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    econtact = models.IntegerField(db_column='eContact', blank=True, null=True)  # Field name made lowercase.
    emission = models.IntegerField(db_column='eMission', blank=True, null=True)  # Field name made lowercase.
    emissionofcriminalcontact = models.IntegerField(db_column='eMissionOfCriminalContact', blank=True, null=True)  # Field name made lowercase.
    nmaxlevel = models.IntegerField(db_column='nMaxLevel', blank=True, null=True)  # Field name made lowercase.
    nminlevel = models.IntegerField(db_column='nMinLevel', blank=True, null=True)  # Field name made lowercase.
    bdisabled = models.IntegerField(db_column='bDisabled', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MissionOfCriminalContacts'


class Missionofenforcercontacts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    econtact = models.IntegerField(db_column='eContact', blank=True, null=True)  # Field name made lowercase.
    emission = models.IntegerField(db_column='eMission', blank=True, null=True)  # Field name made lowercase.
    emissionofenforcercontact = models.IntegerField(db_column='eMissionOfEnforcerContact', blank=True, null=True)  # Field name made lowercase.
    nmaxlevel = models.IntegerField(db_column='nMaxLevel', blank=True, null=True)  # Field name made lowercase.
    nminlevel = models.IntegerField(db_column='nMinLevel', blank=True, null=True)  # Field name made lowercase.
    bdisabled = models.IntegerField(db_column='bDisabled', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MissionOfEnforcerContacts'


class Missionresultreasons(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdrawmessage = models.TextField(db_column='sDrawMessage', blank=True, null=True)  # Field name made lowercase.
    slosemessage = models.TextField(db_column='sLoseMessage', blank=True, null=True)  # Field name made lowercase.
    swinmessage = models.TextField(db_column='sWinMessage', blank=True, null=True)  # Field name made lowercase.
    emissionresultreason = models.IntegerField(db_column='eMissionResultReason', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MissionResultReasons'


class Missionrewardpackages(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    emissionrewardpackage = models.IntegerField(db_column='eMissionRewardPackage', blank=True, null=True)  # Field name made lowercase.
    nbasecash_0 = models.IntegerField(db_column='nBaseCash_0', blank=True, null=True)  # Field name made lowercase.
    nbasecash_1 = models.IntegerField(db_column='nBaseCash_1', blank=True, null=True)  # Field name made lowercase.
    nbasecontactstanding_0 = models.IntegerField(db_column='nBaseContactStanding_0', blank=True, null=True)  # Field name made lowercase.
    nbasecontactstanding_1 = models.IntegerField(db_column='nBaseContactStanding_1', blank=True, null=True)  # Field name made lowercase.
    nscore = models.IntegerField(db_column='nScore', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MissionRewardPackages'


class Missionsystemfilterentries(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    emissionsystemfilter = models.IntegerField(db_column='eMissionSystemFilter', blank=True, null=True)  # Field name made lowercase.
    emissionsystem = models.IntegerField(db_column='eMissionSystem', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MissionSystemFilterEntries'


class Missionsystemfilters(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    emissionsystemfilter = models.IntegerField(db_column='eMissionSystemFilter', blank=True, null=True)  # Field name made lowercase.
    bexclusive = models.IntegerField(db_column='bExclusive', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MissionSystemFilters'


class Missiontakeoutlookup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nmissiontakeoutlookup = models.IntegerField(db_column='nMissionTakeoutLookUp', blank=True, null=True)  # Field name made lowercase.
    ntakeoutlimit = models.IntegerField(db_column='nTakeoutLimit', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MissionTakeoutLookUp'


class Missiontemplateuiprofiles(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    strackedvaluedescription_0 = models.TextField(db_column='sTrackedValueDescription_0', blank=True, null=True)  # Field name made lowercase.
    strackedvaluedescription_1 = models.TextField(db_column='sTrackedValueDescription_1', blank=True, null=True)  # Field name made lowercase.
    strackedvaluedescription_2 = models.TextField(db_column='sTrackedValueDescription_2', blank=True, null=True)  # Field name made lowercase.
    strackedvaluedescription_3 = models.TextField(db_column='sTrackedValueDescription_3', blank=True, null=True)  # Field name made lowercase.
    strackedvalueimage_0 = models.TextField(db_column='sTrackedValueImage_0', blank=True, null=True)  # Field name made lowercase.
    strackedvalueimage_1 = models.TextField(db_column='sTrackedValueImage_1', blank=True, null=True)  # Field name made lowercase.
    strackedvalueimage_2 = models.TextField(db_column='sTrackedValueImage_2', blank=True, null=True)  # Field name made lowercase.
    strackedvalueimage_3 = models.TextField(db_column='sTrackedValueImage_3', blank=True, null=True)  # Field name made lowercase.
    emissiontemplateuiprofile = models.IntegerField(db_column='eMissionTemplateUIProfile', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluebarfgdisabled_0 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_0', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluebarfgdisabled_1 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_1', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluebarfgdisabled_2 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_2', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluebarfgdisabled_3 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_3', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluebg_0 = models.IntegerField(db_column='eTrackedValueBg_0', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluebg_1 = models.IntegerField(db_column='eTrackedValueBg_1', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluebg_2 = models.IntegerField(db_column='eTrackedValueBg_2', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluebg_3 = models.IntegerField(db_column='eTrackedValueBg_3', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluefg_0 = models.IntegerField(db_column='eTrackedValueFg_0', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluefg_1 = models.IntegerField(db_column='eTrackedValueFg_1', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluefg_2 = models.IntegerField(db_column='eTrackedValueFg_2', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluefg_3 = models.IntegerField(db_column='eTrackedValueFg_3', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluesocket_0 = models.IntegerField(db_column='eTrackedValueSocket_0', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluesocket_1 = models.IntegerField(db_column='eTrackedValueSocket_1', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluesocket_2 = models.IntegerField(db_column='eTrackedValueSocket_2', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluesocket_3 = models.IntegerField(db_column='eTrackedValueSocket_3', blank=True, null=True)  # Field name made lowercase.
    etrackedvalue_0 = models.IntegerField(db_column='eTrackedValue_0', blank=True, null=True)  # Field name made lowercase.
    etrackedvalue_1 = models.IntegerField(db_column='eTrackedValue_1', blank=True, null=True)  # Field name made lowercase.
    etrackedvalue_2 = models.IntegerField(db_column='eTrackedValue_2', blank=True, null=True)  # Field name made lowercase.
    etrackedvalue_3 = models.IntegerField(db_column='eTrackedValue_3', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluedisplay_0 = models.IntegerField(db_column='eTrackedValueDisplay_0', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluedisplay_1 = models.IntegerField(db_column='eTrackedValueDisplay_1', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluedisplay_2 = models.IntegerField(db_column='eTrackedValueDisplay_2', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluedisplay_3 = models.IntegerField(db_column='eTrackedValueDisplay_3', blank=True, null=True)  # Field name made lowercase.
    bflashwhenchanged_0 = models.IntegerField(db_column='bFlashWhenChanged_0', blank=True, null=True)  # Field name made lowercase.
    bflashwhenchanged_1 = models.IntegerField(db_column='bFlashWhenChanged_1', blank=True, null=True)  # Field name made lowercase.
    bflashwhenchanged_2 = models.IntegerField(db_column='bFlashWhenChanged_2', blank=True, null=True)  # Field name made lowercase.
    bflashwhenchanged_3 = models.IntegerField(db_column='bFlashWhenChanged_3', blank=True, null=True)  # Field name made lowercase.
    bhideatmax_0 = models.IntegerField(db_column='bHideAtMax_0', blank=True, null=True)  # Field name made lowercase.
    bhideatmax_1 = models.IntegerField(db_column='bHideAtMax_1', blank=True, null=True)  # Field name made lowercase.
    bhideatmax_2 = models.IntegerField(db_column='bHideAtMax_2', blank=True, null=True)  # Field name made lowercase.
    bhideatmax_3 = models.IntegerField(db_column='bHideAtMax_3', blank=True, null=True)  # Field name made lowercase.
    bhidewhenone_0 = models.IntegerField(db_column='bHideWhenOne_0', blank=True, null=True)  # Field name made lowercase.
    bhidewhenone_1 = models.IntegerField(db_column='bHideWhenOne_1', blank=True, null=True)  # Field name made lowercase.
    bhidewhenone_2 = models.IntegerField(db_column='bHideWhenOne_2', blank=True, null=True)  # Field name made lowercase.
    bhidewhenone_3 = models.IntegerField(db_column='bHideWhenOne_3', blank=True, null=True)  # Field name made lowercase.
    bhidewhenoppositionviptakeoutsdisabled_0 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_0', blank=True, null=True)  # Field name made lowercase.
    bhidewhenoppositionviptakeoutsdisabled_1 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_1', blank=True, null=True)  # Field name made lowercase.
    bhidewhenoppositionviptakeoutsdisabled_2 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_2', blank=True, null=True)  # Field name made lowercase.
    bhidewhenoppositionviptakeoutsdisabled_3 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_3', blank=True, null=True)  # Field name made lowercase.
    bhidewhenownerviptakeoutsdisabled_0 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_0', blank=True, null=True)  # Field name made lowercase.
    bhidewhenownerviptakeoutsdisabled_1 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_1', blank=True, null=True)  # Field name made lowercase.
    bhidewhenownerviptakeoutsdisabled_2 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_2', blank=True, null=True)  # Field name made lowercase.
    bhidewhenownerviptakeoutsdisabled_3 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_3', blank=True, null=True)  # Field name made lowercase.
    bhidewhenpointsdisabled_0 = models.IntegerField(db_column='bHideWhenPointsDisabled_0', blank=True, null=True)  # Field name made lowercase.
    bhidewhenpointsdisabled_1 = models.IntegerField(db_column='bHideWhenPointsDisabled_1', blank=True, null=True)  # Field name made lowercase.
    bhidewhenpointsdisabled_2 = models.IntegerField(db_column='bHideWhenPointsDisabled_2', blank=True, null=True)  # Field name made lowercase.
    bhidewhenpointsdisabled_3 = models.IntegerField(db_column='bHideWhenPointsDisabled_3', blank=True, null=True)  # Field name made lowercase.
    bhidewhentakeoutsdisabled_0 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_0', blank=True, null=True)  # Field name made lowercase.
    bhidewhentakeoutsdisabled_1 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_1', blank=True, null=True)  # Field name made lowercase.
    bhidewhentakeoutsdisabled_2 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_2', blank=True, null=True)  # Field name made lowercase.
    bhidewhentakeoutsdisabled_3 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_3', blank=True, null=True)  # Field name made lowercase.
    bhidewhenunopposed_0 = models.IntegerField(db_column='bHideWhenUnopposed_0', blank=True, null=True)  # Field name made lowercase.
    bhidewhenunopposed_1 = models.IntegerField(db_column='bHideWhenUnopposed_1', blank=True, null=True)  # Field name made lowercase.
    bhidewhenunopposed_2 = models.IntegerField(db_column='bHideWhenUnopposed_2', blank=True, null=True)  # Field name made lowercase.
    bhidewhenunopposed_3 = models.IntegerField(db_column='bHideWhenUnopposed_3', blank=True, null=True)  # Field name made lowercase.
    btrackedvalueinlocaloverview_0 = models.IntegerField(db_column='bTrackedValueInLocalOverview_0', blank=True, null=True)  # Field name made lowercase.
    btrackedvalueinlocaloverview_1 = models.IntegerField(db_column='bTrackedValueInLocalOverview_1', blank=True, null=True)  # Field name made lowercase.
    btrackedvalueinlocaloverview_2 = models.IntegerField(db_column='bTrackedValueInLocalOverview_2', blank=True, null=True)  # Field name made lowercase.
    btrackedvalueinlocaloverview_3 = models.IntegerField(db_column='bTrackedValueInLocalOverview_3', blank=True, null=True)  # Field name made lowercase.
    btrackedvalueinremoteoverview_0 = models.IntegerField(db_column='bTrackedValueInRemoteOverview_0', blank=True, null=True)  # Field name made lowercase.
    btrackedvalueinremoteoverview_1 = models.IntegerField(db_column='bTrackedValueInRemoteOverview_1', blank=True, null=True)  # Field name made lowercase.
    btrackedvalueinremoteoverview_2 = models.IntegerField(db_column='bTrackedValueInRemoteOverview_2', blank=True, null=True)  # Field name made lowercase.
    btrackedvalueinremoteoverview_3 = models.IntegerField(db_column='bTrackedValueInRemoteOverview_3', blank=True, null=True)  # Field name made lowercase.
    btrackedvalueonhud_0 = models.IntegerField(db_column='bTrackedValueOnHUD_0', blank=True, null=True)  # Field name made lowercase.
    btrackedvalueonhud_1 = models.IntegerField(db_column='bTrackedValueOnHUD_1', blank=True, null=True)  # Field name made lowercase.
    btrackedvalueonhud_2 = models.IntegerField(db_column='bTrackedValueOnHUD_2', blank=True, null=True)  # Field name made lowercase.
    btrackedvalueonhud_3 = models.IntegerField(db_column='bTrackedValueOnHUD_3', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MissionTemplateUIProfiles'


class Missiontemplates(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    smissiontitle = models.TextField(db_column='sMissionTitle', blank=True, null=True)  # Field name made lowercase.
    emissiontemplate = models.IntegerField(db_column='eMissionTemplate', blank=True, null=True)  # Field name made lowercase.
    emissiontypefilter = models.IntegerField(db_column='eMissionTypeFilter', blank=True, null=True)  # Field name made lowercase.
    emissionuioppositionprofile = models.IntegerField(db_column='eMissionUIOppositionProfile', blank=True, null=True)  # Field name made lowercase.
    emissionuiownerprofile = models.IntegerField(db_column='eMissionUIOwnerProfile', blank=True, null=True)  # Field name made lowercase.
    epurpose = models.IntegerField(db_column='ePurpose', blank=True, null=True)  # Field name made lowercase.
    erarity = models.IntegerField(db_column='eRarity', blank=True, null=True)  # Field name made lowercase.
    erewardpackage = models.IntegerField(db_column='eRewardPackage', blank=True, null=True)  # Field name made lowercase.
    fowningsidebias = models.FloatField(db_column='fOwningSideBias', blank=True, null=True)  # Field name made lowercase.
    ncomplexity = models.IntegerField(db_column='nComplexity', blank=True, null=True)  # Field name made lowercase.
    ngroupsizemax = models.IntegerField(db_column='nGroupSizeMax', blank=True, null=True)  # Field name made lowercase.
    ngroupsizemin = models.IntegerField(db_column='nGroupSizeMin', blank=True, null=True)  # Field name made lowercase.
    nopposingsideviplives = models.IntegerField(db_column='nOpposingSideVIPLives', blank=True, null=True)  # Field name made lowercase.
    nowningsideviplives = models.IntegerField(db_column='nOwningSideVIPLives', blank=True, null=True)  # Field name made lowercase.
    nrespawntime = models.IntegerField(db_column='nRespawnTime', blank=True, null=True)  # Field name made lowercase.
    nrespawntimeincrement = models.IntegerField(db_column='nRespawnTimeIncrement', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    nsimultaneouscap = models.IntegerField(db_column='nSimultaneousCap', blank=True, null=True)  # Field name made lowercase.
    ntakeoutcount = models.IntegerField(db_column='nTakeoutCount', blank=True, null=True)  # Field name made lowercase.
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)  # Field name made lowercase.
    etimeofdayavailability = models.IntegerField(db_column='eTimeOfDayAvailability', blank=True, null=True)  # Field name made lowercase.
    bbountyhunter = models.IntegerField(db_column='bBountyHunter', blank=True, null=True)  # Field name made lowercase.
    bcountarrestsastakeouts = models.IntegerField(db_column='bCountArrestsAsTakeouts', blank=True, null=True)  # Field name made lowercase.
    bcountarrestsasviptakeouts = models.IntegerField(db_column='bCountArrestsAsVIPTakeouts', blank=True, null=True)  # Field name made lowercase.
    bcountkillsastakeouts = models.IntegerField(db_column='bCountKillsAsTakeouts', blank=True, null=True)  # Field name made lowercase.
    bcountkillsasviptakeouts = models.IntegerField(db_column='bCountKillsAsVIPTakeouts', blank=True, null=True)  # Field name made lowercase.
    bdisabled = models.IntegerField(db_column='bDisabled', blank=True, null=True)  # Field name made lowercase.
    bnocriminalopposition = models.IntegerField(db_column='bNoCriminalOpposition', blank=True, null=True)  # Field name made lowercase.
    boppositionwinonmaxtakeouts = models.IntegerField(db_column='bOppositionWinOnMaxTakeouts', blank=True, null=True)  # Field name made lowercase.
    bownerwinonmaxtakeouts = models.IntegerField(db_column='bOwnerWinOnMaxTakeouts', blank=True, null=True)  # Field name made lowercase.
    btest = models.IntegerField(db_column='bTest', blank=True, null=True)  # Field name made lowercase.
    busetakeoutbar = models.IntegerField(db_column='bUseTakeoutBar', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MissionTemplates'


class Missionuisockets(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    emissionuisocket = models.IntegerField(db_column='eMissionUISocket', blank=True, null=True)  # Field name made lowercase.
    nrow = models.IntegerField(db_column='nRow', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MissionUISockets'


class Missionuitrackedstateprofile(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sarmedicon = models.TextField(db_column='sArmedIcon', blank=True, null=True)  # Field name made lowercase.
    sneutralicon = models.TextField(db_column='sNeutralIcon', blank=True, null=True)  # Field name made lowercase.
    soppositionclaimed = models.TextField(db_column='sOppositionClaimed', blank=True, null=True)  # Field name made lowercase.
    sownerclaimed = models.TextField(db_column='sOwnerClaimed', blank=True, null=True)  # Field name made lowercase.
    sunarmedicon = models.TextField(db_column='sUnarmedIcon', blank=True, null=True)  # Field name made lowercase.
    emissionuitrackedstateprofile = models.IntegerField(db_column='eMissionUITrackedStateProfile', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MissionUITrackedStateProfile'


class Modifiercategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    emodifiercategory = models.IntegerField(db_column='eModifierCategory', blank=True, null=True)  # Field name made lowercase.
    nselectableslot = models.IntegerField(db_column='nSelectableSlot', blank=True, null=True)  # Field name made lowercase.
    emodifierclass = models.IntegerField(db_column='eModifierClass', blank=True, null=True)  # Field name made lowercase.
    emodifiertype = models.IntegerField(db_column='eModifierType', blank=True, null=True)  # Field name made lowercase.
    estackingslot = models.IntegerField(db_column='eStackingSlot', blank=True, null=True)  # Field name made lowercase.
    bavailableaspassenger = models.IntegerField(db_column='bAvailableAsPassenger', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ModifierCategories'


class Modifierdeployableeffects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    emodifieritem = models.IntegerField(db_column='eModifierItem', blank=True, null=True)  # Field name made lowercase.
    etaskitem = models.IntegerField(db_column='eTaskItem', blank=True, null=True)  # Field name made lowercase.
    bdeployatmodifierend = models.IntegerField(db_column='bDeployAtModifierEnd', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ModifierDeployableEffects'


class Modifiereffects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    emodifieritem = models.IntegerField(db_column='eModifierItem', blank=True, null=True)  # Field name made lowercase.
    faddtoresult = models.FloatField(db_column='fAddToResult', blank=True, null=True)  # Field name made lowercase.
    feffectmultiplier = models.FloatField(db_column='fEffectMultiplier', blank=True, null=True)  # Field name made lowercase.
    eeffecttype = models.IntegerField(db_column='eEffectType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ModifierEffects'


class Modifieritemeffects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    eitem = models.IntegerField(db_column='eItem', blank=True, null=True)  # Field name made lowercase.
    emodifieritem = models.IntegerField(db_column='eModifierItem', blank=True, null=True)  # Field name made lowercase.
    eeffect = models.IntegerField(db_column='eEffect', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ModifierItemEffects'


class Modifieritemtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    emodifieritem = models.IntegerField(db_column='eModifierItem', blank=True, null=True)  # Field name made lowercase.
    napplicationcost = models.IntegerField(db_column='nApplicationCost', blank=True, null=True)  # Field name made lowercase.
    nremovalcost = models.IntegerField(db_column='nRemovalCost', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ModifierItemTypes'


class Modifieritems(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    striggersfx = models.TextField(db_column='sTriggerSFX', blank=True, null=True)  # Field name made lowercase.
    striggervfx = models.TextField(db_column='sTriggerVFX', blank=True, null=True)  # Field name made lowercase.
    emodifiercategory = models.IntegerField(db_column='eModifierCategory', blank=True, null=True)  # Field name made lowercase.
    emodifieritem = models.IntegerField(db_column='eModifierItem', blank=True, null=True)  # Field name made lowercase.
    erulesetexclusion = models.IntegerField(db_column='eRulesetExclusion', blank=True, null=True)  # Field name made lowercase.
    fcooldowntimeatpremiumlevel_0 = models.FloatField(db_column='fCooldownTimeAtPremiumLevel_0', blank=True, null=True)  # Field name made lowercase.
    fcooldowntimeatpremiumlevel_1 = models.FloatField(db_column='fCooldownTimeAtPremiumLevel_1', blank=True, null=True)  # Field name made lowercase.
    fdurationatpremiumlevel_0 = models.FloatField(db_column='fDurationAtPremiumLevel_0', blank=True, null=True)  # Field name made lowercase.
    fdurationatpremiumlevel_1 = models.FloatField(db_column='fDurationAtPremiumLevel_1', blank=True, null=True)  # Field name made lowercase.
    fintervaltimeatpremiumlevel_0 = models.FloatField(db_column='fIntervalTimeAtPremiumLevel_0', blank=True, null=True)  # Field name made lowercase.
    fintervaltimeatpremiumlevel_1 = models.FloatField(db_column='fIntervalTimeAtPremiumLevel_1', blank=True, null=True)  # Field name made lowercase.
    nmodifierlevel = models.IntegerField(db_column='nModifierLevel', blank=True, null=True)  # Field name made lowercase.
    egiftboxtheme = models.IntegerField(db_column='eGiftBoxTheme', blank=True, null=True)  # Field name made lowercase.
    bactivationendsimmunity = models.IntegerField(db_column='bActivationEndsImmunity', blank=True, null=True)  # Field name made lowercase.
    bbroadcastsfx = models.IntegerField(db_column='bBroadcastSFX', blank=True, null=True)  # Field name made lowercase.
    buncancelable = models.IntegerField(db_column='bUnCancelable', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ModifierItems'


class Npcanimationcategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    enpcanimationcategory = models.IntegerField(db_column='eNPCAnimationCategory', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NPCAnimationCategories'


class Npcaudiotype(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sclothingaccessoriesswitchvalue = models.TextField(db_column='sClothingAccessoriesSwitchValue', blank=True, null=True)  # Field name made lowercase.
    sclothingarmsswitchvalue = models.TextField(db_column='sClothingArmsSwitchValue', blank=True, null=True)  # Field name made lowercase.
    sclothingfootwearswitchvalue = models.TextField(db_column='sClothingFootwearSwitchValue', blank=True, null=True)  # Field name made lowercase.
    sclothinglegsswitchvalue = models.TextField(db_column='sClothingLegsSwitchValue', blank=True, null=True)  # Field name made lowercase.
    svoiceswitchvalue = models.TextField(db_column='sVoiceSwitchValue', blank=True, null=True)  # Field name made lowercase.
    enpcaudiotype = models.IntegerField(db_column='eNPCAudioType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NPCAudioType'


class Npcdrivertypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    enpcdrivertype = models.IntegerField(db_column='eNPCDriverType', blank=True, null=True)  # Field name made lowercase.
    enpctypefemale = models.IntegerField(db_column='eNPCTypeFemale', blank=True, null=True)  # Field name made lowercase.
    enpctypemale = models.IntegerField(db_column='eNPCTypeMale', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NPCDriverTypes'


class NpceventAllowedtooverrides(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nignoreme = models.IntegerField(db_column='nIgnoreMe', blank=True, null=True)  # Field name made lowercase.
    enpcevent = models.IntegerField(db_column='eNPCEvent', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NPCEvent_AllowedToOverrides'


class Npcevents(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nignoreme = models.IntegerField(db_column='nIgnoreMe', blank=True, null=True)  # Field name made lowercase.
    enpcevent = models.IntegerField(db_column='eNPCEvent', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NPCEvents'


class Npcpedestriananimations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    snpcpedestriananimation = models.TextField(db_column='sNPCPedestrianAnimation', blank=True, null=True)  # Field name made lowercase.
    eanimationcategory = models.IntegerField(db_column='eAnimationCategory', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NPCPedestrianAnimations'


class NpcreactionAllowedtooverrides(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    npriority = models.IntegerField(db_column='nPriority', blank=True, null=True)  # Field name made lowercase.
    enpcreaction = models.IntegerField(db_column='eNPCReaction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NPCReaction_AllowedToOverrides'


class Npcreactions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    npriority = models.IntegerField(db_column='nPriority', blank=True, null=True)  # Field name made lowercase.
    enpcreaction = models.IntegerField(db_column='eNPCReaction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NPCReactions'


class NpctypeTodDistricts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    edistrict = models.IntegerField(db_column='eDistrict', blank=True, null=True)  # Field name made lowercase.
    enpctype_tod = models.IntegerField(db_column='eNPCType_TOD', blank=True, null=True)  # Field name made lowercase.
    enpctype_tod_district = models.IntegerField(db_column='eNPCType_TOD_District', blank=True, null=True)  # Field name made lowercase.
    fpopulationpercentage = models.FloatField(db_column='fPopulationPercentage', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NPCType_TOD_Districts'


class NpctypeTodInfo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    enpctype = models.IntegerField(db_column='eNPCType', blank=True, null=True)  # Field name made lowercase.
    enpctype_tod = models.IntegerField(db_column='eNPCType_TOD', blank=True, null=True)  # Field name made lowercase.
    etod = models.IntegerField(db_column='eTOD', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NPCType_TOD_Info'


class Npctypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    enpctype = models.IntegerField(db_column='eNPCType', blank=True, null=True)  # Field name made lowercase.
    fdebugcolour_b = models.FloatField(db_column='fDebugColour_B', blank=True, null=True)  # Field name made lowercase.
    fdebugcolour_g = models.FloatField(db_column='fDebugColour_G', blank=True, null=True)  # Field name made lowercase.
    fdebugcolour_r = models.FloatField(db_column='fDebugColour_R', blank=True, null=True)  # Field name made lowercase.
    egender = models.IntegerField(db_column='eGender', blank=True, null=True)  # Field name made lowercase.
    enpccategory = models.IntegerField(db_column='eNPCCategory', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NPCTypes'


class Npcvehicleanimations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    snpcvehicleanimation = models.TextField(db_column='sNPCVehicleAnimation', blank=True, null=True)  # Field name made lowercase.
    eanimationcategory = models.IntegerField(db_column='eAnimationCategory', blank=True, null=True)  # Field name made lowercase.
    evehiclenpcinsideanimationset = models.IntegerField(db_column='eVehicleNPCInsideAnimationSet', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NPCVehicleAnimations'


class Npcvehiclespeeds(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    enpcvehiclecategory = models.IntegerField(db_column='eNPCVehicleCategory', blank=True, null=True)  # Field name made lowercase.
    fmaxacceleration = models.FloatField(db_column='fMaxAcceleration', blank=True, null=True)  # Field name made lowercase.
    fmaxdeceleration = models.FloatField(db_column='fMaxDeceleration', blank=True, null=True)  # Field name made lowercase.
    fmaxtopspeedratio = models.FloatField(db_column='fMaxTopSpeedRatio', blank=True, null=True)  # Field name made lowercase.
    fminacceleration = models.FloatField(db_column='fMinAcceleration', blank=True, null=True)  # Field name made lowercase.
    fmindeceleration = models.FloatField(db_column='fMinDeceleration', blank=True, null=True)  # Field name made lowercase.
    fmintopspeedratio = models.FloatField(db_column='fMinTopSpeedRatio', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NPCVehicleSpeeds'


class Npcworldevents(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    spedestrianaudioreason = models.TextField(db_column='sPedestrianAudioReason', blank=True, null=True)  # Field name made lowercase.
    epedestrianblastevent = models.IntegerField(db_column='ePedestrianBlastEvent', blank=True, null=True)  # Field name made lowercase.
    epedestriandangerevent = models.IntegerField(db_column='ePedestrianDangerEvent', blank=True, null=True)  # Field name made lowercase.
    epedestrianwitnessevent = models.IntegerField(db_column='ePedestrianWitnessEvent', blank=True, null=True)  # Field name made lowercase.
    evehicleblastevent = models.IntegerField(db_column='eVehicleBlastEvent', blank=True, null=True)  # Field name made lowercase.
    evehicledangerevent = models.IntegerField(db_column='eVehicleDangerEvent', blank=True, null=True)  # Field name made lowercase.
    evehiclewitnessevent = models.IntegerField(db_column='eVehicleWitnessEvent', blank=True, null=True)  # Field name made lowercase.
    faudibilitydistance = models.FloatField(db_column='fAudibilityDistance', blank=True, null=True)  # Field name made lowercase.
    fblastdistance = models.FloatField(db_column='fBlastDistance', blank=True, null=True)  # Field name made lowercase.
    fdangerdistance = models.FloatField(db_column='fDangerDistance', blank=True, null=True)  # Field name made lowercase.
    fvisibilitydistance = models.FloatField(db_column='fVisibilityDistance', blank=True, null=True)  # Field name made lowercase.
    enpcworldevent = models.IntegerField(db_column='eNPCWorldEvent', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NPCWorldEvents'


class NpcTodBehaviours(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    enpc_tod_event = models.IntegerField(db_column='eNPC_TOD_Event', blank=True, null=True)  # Field name made lowercase.
    ereaction = models.IntegerField(db_column='eReaction', blank=True, null=True)  # Field name made lowercase.
    flikelihood = models.FloatField(db_column='fLikelihood', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NPC_TOD_Behaviours'


class NpcTodEvent(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    enpc_tod_event = models.IntegerField(db_column='eNPC_TOD_Event', blank=True, null=True)  # Field name made lowercase.
    enpctype = models.IntegerField(db_column='eNPCType', blank=True, null=True)  # Field name made lowercase.
    etod_event = models.IntegerField(db_column='eTOD_Event', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NPC_TOD_Event'


class Notorietyeffects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eforcemaxlevel = models.IntegerField(db_column='eForceMaxLevel', blank=True, null=True)  # Field name made lowercase.
    eforceminlevel = models.IntegerField(db_column='eForceMinLevel', blank=True, null=True)  # Field name made lowercase.
    enotorietyeffect = models.IntegerField(db_column='eNotorietyEffect', blank=True, null=True)  # Field name made lowercase.
    enotorietylevellimit = models.IntegerField(db_column='eNotorietyLevelLimit', blank=True, null=True)  # Field name made lowercase.
    fquantity = models.FloatField(db_column='fQuantity', blank=True, null=True)  # Field name made lowercase.
    nenforcerwitnesserscap = models.IntegerField(db_column='nEnforcerWitnessersCap', blank=True, null=True)  # Field name made lowercase.
    nnpcwitnesserscap = models.IntegerField(db_column='nNPCWitnessersCap', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NotorietyEffects'


class Notorietylevels(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eheatlevel = models.IntegerField(db_column='eHeatLevel', blank=True, null=True)  # Field name made lowercase.
    enotorietylevel = models.IntegerField(db_column='eNotorietyLevel', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NotorietyLevels'


class Owaitemspawnrules(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eitemmetatag_0 = models.IntegerField(db_column='eItemMetaTag_0', blank=True, null=True)  # Field name made lowercase.
    eitemmetatag_1 = models.IntegerField(db_column='eItemMetaTag_1', blank=True, null=True)  # Field name made lowercase.
    eitemmetatag_2 = models.IntegerField(db_column='eItemMetaTag_2', blank=True, null=True)  # Field name made lowercase.
    eitemmetatag_3 = models.IntegerField(db_column='eItemMetaTag_3', blank=True, null=True)  # Field name made lowercase.
    eitemmetatag_4 = models.IntegerField(db_column='eItemMetaTag_4', blank=True, null=True)  # Field name made lowercase.
    eowaitemspawnrule = models.IntegerField(db_column='eOWAItemSpawnRule', blank=True, null=True)  # Field name made lowercase.
    nlargeitemweighting = models.IntegerField(db_column='nLargeItemWeighting', blank=True, null=True)  # Field name made lowercase.
    nlowermidrange = models.IntegerField(db_column='nLowerMidRange', blank=True, null=True)  # Field name made lowercase.
    nlowerrange = models.IntegerField(db_column='nLowerRange', blank=True, null=True)  # Field name made lowercase.
    nmediumitemweighting = models.IntegerField(db_column='nMediumItemWeighting', blank=True, null=True)  # Field name made lowercase.
    npercentagechancezeroitems = models.IntegerField(db_column='nPercentageChanceZeroItems', blank=True, null=True)  # Field name made lowercase.
    nsmallitemweighting = models.IntegerField(db_column='nSmallItemWeighting', blank=True, null=True)  # Field name made lowercase.
    nuppermidrange = models.IntegerField(db_column='nUpperMidRange', blank=True, null=True)  # Field name made lowercase.
    nupperrange = models.IntegerField(db_column='nUpperRange', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OWAItemSpawnRules'


class Onfootdeathanimations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sanimname = models.TextField(db_column='sAnimName', blank=True, null=True)  # Field name made lowercase.
    eonfootdeathanimation = models.IntegerField(db_column='eOnFootDeathAnimation', blank=True, null=True)  # Field name made lowercase.
    bretainmomentum = models.IntegerField(db_column='bRetainMomentum', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnFootDeathAnimations'


class Openworldconstant(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)  # Field name made lowercase.
    eopenworldconstant = models.IntegerField(db_column='eOpenWorldConstant', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OpenWorldConstant'


class Openworlddropoffs(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ehudmarkertype = models.IntegerField(db_column='eHUDMarkerType', blank=True, null=True)  # Field name made lowercase.
    eopenworlddropoff = models.IntegerField(db_column='eOpenWorldDropOff', blank=True, null=True)  # Field name made lowercase.
    fcycledurationseconds = models.FloatField(db_column='fCycleDurationSeconds', blank=True, null=True)  # Field name made lowercase.
    fpointreplenishmentpercycle = models.FloatField(db_column='fPointReplenishmentPerCycle', blank=True, null=True)  # Field name made lowercase.
    ndeliverypoints = models.IntegerField(db_column='nDeliveryPoints', blank=True, null=True)  # Field name made lowercase.
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)  # Field name made lowercase.
    efactionhudmarkerfilter = models.IntegerField(db_column='eFactionHUDMarkerFilter', blank=True, null=True)  # Field name made lowercase.
    etaskitemsize_0 = models.IntegerField(db_column='eTaskItemSize_0', blank=True, null=True)  # Field name made lowercase.
    etaskitemsize_1 = models.IntegerField(db_column='eTaskItemSize_1', blank=True, null=True)  # Field name made lowercase.
    etaskitemsize_2 = models.IntegerField(db_column='eTaskItemSize_2', blank=True, null=True)  # Field name made lowercase.
    etaskitemsize_3 = models.IntegerField(db_column='eTaskItemSize_3', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OpenWorldDropOffs'


class Openworldoperations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    suidescription = models.TextField(db_column='sUIDescription', blank=True, null=True)  # Field name made lowercase.
    suititle = models.TextField(db_column='sUITitle', blank=True, null=True)  # Field name made lowercase.
    eopenworldoperation = models.IntegerField(db_column='eOpenWorldOperation', blank=True, null=True)  # Field name made lowercase.
    euiicon = models.IntegerField(db_column='eUIIcon', blank=True, null=True)  # Field name made lowercase.
    ncsaduration = models.IntegerField(db_column='nCSADuration', blank=True, null=True)  # Field name made lowercase.
    enpcworldevent = models.IntegerField(db_column='eNPCWorldEvent', blank=True, null=True)  # Field name made lowercase.
    eopenworldcsa = models.IntegerField(db_column='eOpenWorldCSA', blank=True, null=True)  # Field name made lowercase.
    etaskoperationcategory = models.IntegerField(db_column='eTaskOperationCategory', blank=True, null=True)  # Field name made lowercase.
    ballowedonmission = models.IntegerField(db_column='bAllowedOnMission', blank=True, null=True)  # Field name made lowercase.
    buireticulehighlight = models.IntegerField(db_column='bUIReticuleHighlight', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OpenWorldOperations'


class Openworldtargetactivities(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eopenworldoperationcriminal = models.IntegerField(db_column='eOpenWorldOperationCriminal', blank=True, null=True)  # Field name made lowercase.
    eopenworldoperationenforcer = models.IntegerField(db_column='eOpenWorldOperationEnforcer', blank=True, null=True)  # Field name made lowercase.
    eopenworldtargetactivity = models.IntegerField(db_column='eOpenWorldTargetActivity', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OpenWorldTargetActivities'


class Optioncategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sname = models.TextField(db_column='sName', blank=True, null=True)  # Field name made lowercase.
    eaccessrestrictions = models.IntegerField(db_column='eAccessRestrictions', blank=True, null=True)  # Field name made lowercase.
    eoptioncategory = models.IntegerField(db_column='eOptionCategory', blank=True, null=True)  # Field name made lowercase.
    eparent = models.IntegerField(db_column='eParent', blank=True, null=True)  # Field name made lowercase.
    binclude = models.IntegerField(db_column='bInclude', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OptionCategories'


class Organisations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sname = models.TextField(db_column='sName', blank=True, null=True)  # Field name made lowercase.
    spicture = models.TextField(db_column='sPicture', blank=True, null=True)  # Field name made lowercase.
    ehudicon = models.IntegerField(db_column='eHUDIcon', blank=True, null=True)  # Field name made lowercase.
    eorganisationcontact = models.IntegerField(db_column='eOrganisationContact', blank=True, null=True)  # Field name made lowercase.
    eorganisationicon = models.IntegerField(db_column='eOrganisationIcon', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)  # Field name made lowercase.
    eorganisation = models.IntegerField(db_column='eOrganisation', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Organisations'


class Outfititemtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sresource = models.TextField(db_column='sResource', blank=True, null=True)  # Field name made lowercase.
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OutfitItemTypes'


class PawnhitreactionBonelists(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    svalue_0 = models.TextField(db_column='sValue_0', blank=True, null=True)  # Field name made lowercase.
    svalue_1 = models.TextField(db_column='sValue_1', blank=True, null=True)  # Field name made lowercase.
    svalue_2 = models.TextField(db_column='sValue_2', blank=True, null=True)  # Field name made lowercase.
    svalue_3 = models.TextField(db_column='sValue_3', blank=True, null=True)  # Field name made lowercase.
    svalue_4 = models.TextField(db_column='sValue_4', blank=True, null=True)  # Field name made lowercase.
    svalue_5 = models.TextField(db_column='sValue_5', blank=True, null=True)  # Field name made lowercase.
    svalue_6 = models.TextField(db_column='sValue_6', blank=True, null=True)  # Field name made lowercase.
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_BoneLists'


class PawnhitreactionBoneremaptables(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sbonefrom = models.TextField(db_column='sBoneFrom', blank=True, null=True)  # Field name made lowercase.
    sboneto = models.TextField(db_column='sBoneTo', blank=True, null=True)  # Field name made lowercase.
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_BoneRemapTables'


class PawnhitreactionBools(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction', blank=True, null=True)  # Field name made lowercase.
    bvalue = models.IntegerField(db_column='bValue', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_Bools'


class PawnhitreactionConstrainedbonelists(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    svalue_0 = models.TextField(db_column='sValue_0', blank=True, null=True)  # Field name made lowercase.
    svalue_1 = models.TextField(db_column='sValue_1', blank=True, null=True)  # Field name made lowercase.
    svalue_2 = models.TextField(db_column='sValue_2', blank=True, null=True)  # Field name made lowercase.
    svalue_3 = models.TextField(db_column='sValue_3', blank=True, null=True)  # Field name made lowercase.
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_ConstrainedBoneLists'


class PawnhitreactionFloats(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction', blank=True, null=True)  # Field name made lowercase.
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_Floats'


class PawnhitreactionSpringlists(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    svalue_0 = models.TextField(db_column='sValue_0', blank=True, null=True)  # Field name made lowercase.
    svalue_1 = models.TextField(db_column='sValue_1', blank=True, null=True)  # Field name made lowercase.
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_SpringLists'


class PawnhitreactionVector2Ds(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction', blank=True, null=True)  # Field name made lowercase.
    fx = models.FloatField(db_column='fX', blank=True, null=True)  # Field name made lowercase.
    fy = models.FloatField(db_column='fY', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_Vector2Ds'


class Pawnhitreactions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction', blank=True, null=True)  # Field name made lowercase.
    etype = models.IntegerField(db_column='eType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PawnHitReactions'


class Pedavoidanimation(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    savoidanimationleft = models.TextField(db_column='sAvoidAnimationLeft', blank=True, null=True)  # Field name made lowercase.
    savoidanimationright = models.TextField(db_column='sAvoidAnimationRight', blank=True, null=True)  # Field name made lowercase.
    eavoidanimationcategory = models.IntegerField(db_column='eAvoidAnimationCategory', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedAvoidAnimation'


class Pedavoidanimationcategory(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    epedavoidanimationcategory = models.IntegerField(db_column='ePedAvoidAnimationCategory', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedAvoidAnimationCategory'


class Pedwalkandrunvariations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sanimation = models.TextField(db_column='sAnimation', blank=True, null=True)  # Field name made lowercase.
    epedavoidanimationcategory = models.IntegerField(db_column='ePedAvoidAnimationCategory', blank=True, null=True)  # Field name made lowercase.
    epedwalkandrunvariation = models.IntegerField(db_column='ePedWalkAndRunVariation', blank=True, null=True)  # Field name made lowercase.
    fbasespeed = models.FloatField(db_column='fBaseSpeed', blank=True, null=True)  # Field name made lowercase.
    egender = models.IntegerField(db_column='eGender', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedWalkAndRunVariations'


class Pedestrianassets(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sasset = models.TextField(db_column='sAsset', blank=True, null=True)  # Field name made lowercase.
    eaudiotype = models.IntegerField(db_column='eAudioType', blank=True, null=True)  # Field name made lowercase.
    enpctype = models.IntegerField(db_column='eNPCType', blank=True, null=True)  # Field name made lowercase.
    epedestrianasset = models.IntegerField(db_column='ePedestrianAsset', blank=True, null=True)  # Field name made lowercase.
    eracetype = models.IntegerField(db_column='eRaceType', blank=True, null=True)  # Field name made lowercase.
    ewalkstyle = models.IntegerField(db_column='eWalkStyle', blank=True, null=True)  # Field name made lowercase.
    epedestrianpalettetype = models.IntegerField(db_column='ePedestrianPaletteType', blank=True, null=True)  # Field name made lowercase.
    bhighheels = models.IntegerField(db_column='bHighHeels', blank=True, null=True)  # Field name made lowercase.
    bshoelaces = models.IntegerField(db_column='bShoeLaces', blank=True, null=True)  # Field name made lowercase.
    bwristwatch = models.IntegerField(db_column='bWristWatch', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedestrianAssets'


class Pedestrianevents(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nignoreme = models.IntegerField(db_column='nIgnoreMe', blank=True, null=True)  # Field name made lowercase.
    enpcevent = models.IntegerField(db_column='eNPCEvent', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedestrianEvents'


class Pedestrianpalettecolours(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fblue = models.FloatField(db_column='fBlue', blank=True, null=True)  # Field name made lowercase.
    fgreen = models.FloatField(db_column='fGreen', blank=True, null=True)  # Field name made lowercase.
    fred = models.FloatField(db_column='fRed', blank=True, null=True)  # Field name made lowercase.
    ncolourindex = models.IntegerField(db_column='nColourIndex', blank=True, null=True)  # Field name made lowercase.
    epedestrianpalettetype = models.IntegerField(db_column='ePedestrianPaletteType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedestrianPaletteColours'


class Pedestrianttianimationoverrides(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    snpcanimation = models.TextField(db_column='sNPCAnimation', blank=True, null=True)  # Field name made lowercase.
    enpctype = models.IntegerField(db_column='eNPCType', blank=True, null=True)  # Field name made lowercase.
    epedestrianttireaction = models.IntegerField(db_column='ePedestrianTTIReaction', blank=True, null=True)  # Field name made lowercase.
    eplayeranimtype = models.IntegerField(db_column='ePlayerAnimType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedestrianTTIAnimationOverrides'


class Pedestrianttianimations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    snpcanimation = models.TextField(db_column='sNPCAnimation', blank=True, null=True)  # Field name made lowercase.
    epedestrianttireaction = models.IntegerField(db_column='ePedestrianTTIReaction', blank=True, null=True)  # Field name made lowercase.
    eplayeranimtype = models.IntegerField(db_column='ePlayerAnimType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedestrianTTIAnimations'


class Pedestrianttireactionoverrides(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    scancelaudioevent = models.TextField(db_column='sCancelAudioEvent', blank=True, null=True)  # Field name made lowercase.
    scompleteaudioevent = models.TextField(db_column='sCompleteAudioEvent', blank=True, null=True)  # Field name made lowercase.
    sstartaudioevent = models.TextField(db_column='sStartAudioEvent', blank=True, null=True)  # Field name made lowercase.
    enpctype = models.IntegerField(db_column='eNPCType', blank=True, null=True)  # Field name made lowercase.
    epedestrianttireaction = models.IntegerField(db_column='ePedestrianTTIReaction', blank=True, null=True)  # Field name made lowercase.
    ewhencancelled = models.IntegerField(db_column='eWhenCancelled', blank=True, null=True)  # Field name made lowercase.
    ewhencompleted = models.IntegerField(db_column='eWhenCompleted', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedestrianTTIReactionOverrides'


class Pedestrianttireactions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    scancelaudioevent = models.TextField(db_column='sCancelAudioEvent', blank=True, null=True)  # Field name made lowercase.
    scompleteaudioevent = models.TextField(db_column='sCompleteAudioEvent', blank=True, null=True)  # Field name made lowercase.
    sstartaudioevent = models.TextField(db_column='sStartAudioEvent', blank=True, null=True)  # Field name made lowercase.
    epedestrianttireaction = models.IntegerField(db_column='ePedestrianTTIReaction', blank=True, null=True)  # Field name made lowercase.
    ewhencancelled = models.IntegerField(db_column='eWhenCancelled', blank=True, null=True)  # Field name made lowercase.
    ewhencompleted = models.IntegerField(db_column='eWhenCompleted', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedestrianTTIReactions'


class Pedestriantempsetups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    stempsetupinfo = models.TextField(db_column='sTempSetupInfo', blank=True, null=True)  # Field name made lowercase.
    epedestriantempsetup = models.IntegerField(db_column='ePedestrianTempSetup', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedestrianTempSetups'


class Pedestriantyperestrictions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    enpctype = models.IntegerField(db_column='eNPCType', blank=True, null=True)  # Field name made lowercase.
    nnumconcurrentsetuptypes = models.IntegerField(db_column='nNumConcurrentSetupTypes', blank=True, null=True)  # Field name made lowercase.
    npedestriantyperestriction = models.IntegerField(db_column='nPedestrianTypeRestriction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedestrianTypeRestrictions'


class Playerroles(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    eactivities_0 = models.IntegerField(db_column='eActivities_0', blank=True, null=True)  # Field name made lowercase.
    eactivities_1 = models.IntegerField(db_column='eActivities_1', blank=True, null=True)  # Field name made lowercase.
    eactivities_2 = models.IntegerField(db_column='eActivities_2', blank=True, null=True)  # Field name made lowercase.
    efirstmilestone = models.IntegerField(db_column='eFirstMilestone', blank=True, null=True)  # Field name made lowercase.
    eplayerrole = models.IntegerField(db_column='ePlayerRole', blank=True, null=True)  # Field name made lowercase.
    fdisplayformulavalue = models.FloatField(db_column='fDisplayFormulaValue', blank=True, null=True)  # Field name made lowercase.
    nnummilestones = models.IntegerField(db_column='nNumMilestones', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    edisplayformulaoperation = models.IntegerField(db_column='eDisplayFormulaOperation', blank=True, null=True)  # Field name made lowercase.
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)  # Field name made lowercase.
    bachievement = models.IntegerField(db_column='bAchievement', blank=True, null=True)  # Field name made lowercase.
    bachievementhidden = models.IntegerField(db_column='bAchievementHidden', blank=True, null=True)  # Field name made lowercase.
    bshowtotalvalues = models.IntegerField(db_column='bShowTotalValues', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    def name(self):
        return self.sdisplayname

    class Meta:
        managed = False
        db_table = 'PlayerRoles'


class Populationtotals(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    edistricttype = models.IntegerField(db_column='eDistrictType', blank=True, null=True)  # Field name made lowercase.
    npopulationtotal = models.IntegerField(db_column='nPopulationTotal', blank=True, null=True)  # Field name made lowercase.
    ntotalpedestrians = models.IntegerField(db_column='nTotalPedestrians', blank=True, null=True)  # Field name made lowercase.
    ntotalvehicles = models.IntegerField(db_column='nTotalVehicles', blank=True, null=True)  # Field name made lowercase.
    etod = models.IntegerField(db_column='eTOD', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PopulationTotals'


class Popupdialogcategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ehighlightcolour = models.IntegerField(db_column='eHighlightColour', blank=True, null=True)  # Field name made lowercase.
    epopupdialogcategory = models.IntegerField(db_column='ePopupDialogCategory', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PopupDialogCategories'


class Popupdialogtriggersceneopen(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    seventname = models.TextField(db_column='sEventName', blank=True, null=True)  # Field name made lowercase.
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PopupDialogTriggerSceneOpen'


class PopupdialogtriggerCsaBegin(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    seventname = models.TextField(db_column='sEventName', blank=True, null=True)  # Field name made lowercase.
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_CSA_Begin'


class PopupdialogtriggerCsaEnd(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    seventname = models.TextField(db_column='sEventName', blank=True, null=True)  # Field name made lowercase.
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_CSA_End'


class PopupdialogtriggerGameplayevents(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    seventname = models.TextField(db_column='sEventName', blank=True, null=True)  # Field name made lowercase.
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_GamePlayEvents'


class PopupdialogtriggerGeneric(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    seventname = models.TextField(db_column='sEventName', blank=True, null=True)  # Field name made lowercase.
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_Generic'


class PopupdialogtriggerReticuleover(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    seventname = models.TextField(db_column='sEventName', blank=True, null=True)  # Field name made lowercase.
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_ReticuleOver'


class PopupdialogtriggerSceneclose(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    seventname = models.TextField(db_column='sEventName', blank=True, null=True)  # Field name made lowercase.
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_SceneClose'


class PopupdialogtriggerUieventPostonclick(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    seventname = models.TextField(db_column='sEventName', blank=True, null=True)  # Field name made lowercase.
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_UIEvent_PostOnClick'


class PopupdialogtriggerWorldspacezone(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    seventname = models.TextField(db_column='sEventName', blank=True, null=True)  # Field name made lowercase.
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_WorldSpaceZone'


class Popupdialogtriggers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    edialogshown = models.IntegerField(db_column='eDialogShown', blank=True, null=True)  # Field name made lowercase.
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PopupDialogTriggers'


class Popupdialoguihighlightaggregation(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    swidget1 = models.TextField(db_column='sWidget1', blank=True, null=True)  # Field name made lowercase.
    swidget2 = models.TextField(db_column='sWidget2', blank=True, null=True)  # Field name made lowercase.
    swidget3 = models.TextField(db_column='sWidget3', blank=True, null=True)  # Field name made lowercase.
    swidget4 = models.TextField(db_column='sWidget4', blank=True, null=True)  # Field name made lowercase.
    swidget5 = models.TextField(db_column='sWidget5', blank=True, null=True)  # Field name made lowercase.
    epopupdialoguihighlightaggregation = models.IntegerField(db_column='ePopupDialogUIHighlightAggregation', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PopupDialogUIHighlightAggregation'


class Popupdialogs(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    spopupbody = models.TextField(db_column='sPopupBody', blank=True, null=True)  # Field name made lowercase.
    echainedpopup = models.IntegerField(db_column='eChainedPopup', blank=True, null=True)  # Field name made lowercase.
    eknowledgebaseurl = models.IntegerField(db_column='eKnowledgeBaseURL', blank=True, null=True)  # Field name made lowercase.
    eoptionalwaypoint = models.IntegerField(db_column='eOptionalWaypoint', blank=True, null=True)  # Field name made lowercase.
    epopupdialog = models.IntegerField(db_column='ePopupDialog', blank=True, null=True)  # Field name made lowercase.
    eposition = models.IntegerField(db_column='ePosition', blank=True, null=True)  # Field name made lowercase.
    euiwidgethightlight_aggregation = models.IntegerField(db_column='eUIWidgetHightlight_Aggregation', blank=True, null=True)  # Field name made lowercase.
    fdisplaytime = models.FloatField(db_column='fDisplayTime', blank=True, null=True)  # Field name made lowercase.
    ntimestoshow = models.IntegerField(db_column='nTimesToShow', blank=True, null=True)  # Field name made lowercase.
    epopupcategory = models.IntegerField(db_column='ePopupCategory', blank=True, null=True)  # Field name made lowercase.
    bdonotqueue = models.IntegerField(db_column='bDoNotQueue', blank=True, null=True)  # Field name made lowercase.
    bflushqueue = models.IntegerField(db_column='bFlushQueue', blank=True, null=True)  # Field name made lowercase.
    bforceknowledgebase = models.IntegerField(db_column='bForceKnowledgebase', blank=True, null=True)  # Field name made lowercase.
    bforchat = models.IntegerField(db_column='bForChat', blank=True, null=True)  # Field name made lowercase.
    bsuppresscriminal = models.IntegerField(db_column='bSuppressCriminal', blank=True, null=True)  # Field name made lowercase.
    bsuppressenforcer = models.IntegerField(db_column='bSuppressEnforcer', blank=True, null=True)  # Field name made lowercase.
    bsuppressmain = models.IntegerField(db_column='bSuppressMain', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PopupDialogs'


class Preloadaction(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    spreloadaction = models.TextField(db_column='sPreloadAction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PreloadAction'


class Preloadcommon(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    spreloadcommon = models.TextField(db_column='sPreloadCommon', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PreloadCommon'


class Preloadcustomisations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    spackage = models.TextField(db_column='sPackage', blank=True, null=True)  # Field name made lowercase.
    spreloadcustomisation = models.TextField(db_column='sPreloadCustomisation', blank=True, null=True)  # Field name made lowercase.
    bcoversbreasts = models.IntegerField(db_column='bCoversBreasts', blank=True, null=True)  # Field name made lowercase.
    bcoversgenitalia = models.IntegerField(db_column='bCoversGenitalia', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PreloadCustomisations'


class Preloadsocial(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    spreloadsocial = models.TextField(db_column='sPreloadSocial', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PreloadSocial'


class Prestigeeffects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eforcemaxlevel = models.IntegerField(db_column='eForceMaxLevel', blank=True, null=True)  # Field name made lowercase.
    eforceminlevel = models.IntegerField(db_column='eForceMinLevel', blank=True, null=True)  # Field name made lowercase.
    eprestigeeffect = models.IntegerField(db_column='ePrestigeEffect', blank=True, null=True)  # Field name made lowercase.
    eprestigelevellimit = models.IntegerField(db_column='ePrestigeLevelLimit', blank=True, null=True)  # Field name made lowercase.
    fquantity = models.FloatField(db_column='fQuantity', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrestigeEffects'


class Prestigelevels(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eheatlevel = models.IntegerField(db_column='eHeatLevel', blank=True, null=True)  # Field name made lowercase.
    eprestigelevel = models.IntegerField(db_column='ePrestigeLevel', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrestigeLevels'


class Primitiveentries(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    epage = models.IntegerField(db_column='ePage', blank=True, null=True)  # Field name made lowercase.
    eprimitiveentry = models.IntegerField(db_column='ePrimitiveEntry', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrimitiveEntries'


class Primitivepages(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    eprimitivepage = models.IntegerField(db_column='ePrimitivePage', blank=True, null=True)  # Field name made lowercase.
    etype = models.IntegerField(db_column='eType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrimitivePages'


class Primitiveunlockitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sresource = models.TextField(db_column='sResource', blank=True, null=True)  # Field name made lowercase.
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    nlegacydata = models.IntegerField(db_column='nLegacyData', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    etype = models.IntegerField(db_column='eType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrimitiveUnlockItemTypes'


class Probabilities(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eprobability = models.IntegerField(db_column='eProbability', blank=True, null=True)  # Field name made lowercase.
    fcoefficient = models.FloatField(db_column='fCoefficient', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Probabilities'


class Profanityfilterentries(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sprofanityfilterentry = models.TextField(db_column='sProfanityFilterEntry', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProfanityFilterEntries'


class Progressionfixups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    nlatestversion = models.IntegerField(db_column='nLatestVersion', blank=True, null=True)  # Field name made lowercase.
    eprogressionfixup = models.IntegerField(db_column='eProgressionFixup', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProgressionFixups'


class Provinggroundschallengemissionactivity(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    eexclude = models.IntegerField(db_column='eExclude', blank=True, null=True)  # Field name made lowercase.
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)  # Field name made lowercase.
    eprovinggroundschallengemissionactivity = models.IntegerField(db_column='eProvingGroundsChallengeMissionActivity', blank=True, null=True)  # Field name made lowercase.
    erarity = models.IntegerField(db_column='eRarity', blank=True, null=True)  # Field name made lowercase.
    nrequirement_0 = models.IntegerField(db_column='nRequirement_0', blank=True, null=True)  # Field name made lowercase.
    nrequirement_1 = models.IntegerField(db_column='nRequirement_1', blank=True, null=True)  # Field name made lowercase.
    nrequirement_2 = models.IntegerField(db_column='nRequirement_2', blank=True, null=True)  # Field name made lowercase.
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProvingGroundsChallengeMissionActivity'


class Provinggroundschallengemissiontype(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    emissiontypefilter = models.IntegerField(db_column='eMissionTypeFilter', blank=True, null=True)  # Field name made lowercase.
    eprovinggroundschallengemissiontype = models.IntegerField(db_column='eProvingGroundsChallengeMissionType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProvingGroundsChallengeMissionType'


class Provinggroundschallengestats(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdatabasecolumn = models.TextField(db_column='sDatabaseColumn', blank=True, null=True)  # Field name made lowercase.
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    sdisplaynamepercentage = models.TextField(db_column='sDisplayNamePercentage', blank=True, null=True)  # Field name made lowercase.
    sdisplayscoreboard = models.TextField(db_column='sDisplayScoreboard', blank=True, null=True)  # Field name made lowercase.
    shudprogress = models.TextField(db_column='sHUDProgress', blank=True, null=True)  # Field name made lowercase.
    stitle = models.TextField(db_column='sTitle', blank=True, null=True)  # Field name made lowercase.
    eprovinggroundschallengestat = models.IntegerField(db_column='eProvingGroundsChallengeStat', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProvingGroundsChallengeStats'


class Raceinfos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eraceinfo = models.IntegerField(db_column='eRaceInfo', blank=True, null=True)  # Field name made lowercase.
    eracetype = models.IntegerField(db_column='eRaceType', blank=True, null=True)  # Field name made lowercase.
    fb = models.FloatField(db_column='fB', blank=True, null=True)  # Field name made lowercase.
    fg = models.FloatField(db_column='fG', blank=True, null=True)  # Field name made lowercase.
    fr = models.FloatField(db_column='fR', blank=True, null=True)  # Field name made lowercase.
    ncolourindex = models.IntegerField(db_column='nColourIndex', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RaceInfos'


class Racetyes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sname = models.TextField(db_column='sName', blank=True, null=True)  # Field name made lowercase.
    eracetype = models.IntegerField(db_column='eRaceType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RaceTyes'


class Randomrewards(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    efirstweightedreward = models.IntegerField(db_column='eFirstWeightedReward', blank=True, null=True)  # Field name made lowercase.
    epurpose = models.IntegerField(db_column='ePurpose', blank=True, null=True)  # Field name made lowercase.
    erandomreward = models.IntegerField(db_column='eRandomReward', blank=True, null=True)  # Field name made lowercase.
    especificcontact = models.IntegerField(db_column='eSpecificContact', blank=True, null=True)  # Field name made lowercase.
    fchancepercentage_0 = models.FloatField(db_column='fChancePercentage_0', blank=True, null=True)  # Field name made lowercase.
    fchancepercentage_1 = models.FloatField(db_column='fChancePercentage_1', blank=True, null=True)  # Field name made lowercase.
    nnumweightedrewards = models.IntegerField(db_column='nNumWeightedRewards', blank=True, null=True)  # Field name made lowercase.
    especificorganisation = models.IntegerField(db_column='eSpecificOrganisation', blank=True, null=True)  # Field name made lowercase.
    bspecificuseonly = models.IntegerField(db_column='bSpecificUseOnly', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RandomRewards'


class Randomtimelimitedrewards(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    edisabledrulesets = models.IntegerField(db_column='eDisabledRulesets', blank=True, null=True)  # Field name made lowercase.
    emissionsystemfilter = models.IntegerField(db_column='eMissionSystemFilter', blank=True, null=True)  # Field name made lowercase.
    erandomreward = models.IntegerField(db_column='eRandomReward', blank=True, null=True)  # Field name made lowercase.
    fdefaultmaxskillratingdifference = models.FloatField(db_column='fDefaultMaxSkillRatingDifference', blank=True, null=True)  # Field name made lowercase.
    ffailedmaximumtime = models.FloatField(db_column='fFailedMaximumTime', blank=True, null=True)  # Field name made lowercase.
    ffailedminimumtime = models.FloatField(db_column='fFailedMinimumTime', blank=True, null=True)  # Field name made lowercase.
    fminskillratingweight = models.FloatField(db_column='fMinSkillRatingWeight', blank=True, null=True)  # Field name made lowercase.
    fstandardmaximumtime = models.FloatField(db_column='fStandardMaximumTime', blank=True, null=True)  # Field name made lowercase.
    fstandardminimumtime = models.FloatField(db_column='fStandardMinimumTime', blank=True, null=True)  # Field name made lowercase.
    nmindistrictpop = models.IntegerField(db_column='nMinDistrictPop', blank=True, null=True)  # Field name made lowercase.
    bawardonloss = models.IntegerField(db_column='bAwardOnLoss', blank=True, null=True)  # Field name made lowercase.
    bawardonwin = models.IntegerField(db_column='bAwardOnWin', blank=True, null=True)  # Field name made lowercase.
    bonworldlevel = models.IntegerField(db_column='bOnWorldLevel', blank=True, null=True)  # Field name made lowercase.
    bresetatentry = models.IntegerField(db_column='bResetAtEntry', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RandomTimeLimitedRewards'


class Rangedweapontype(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eexplosiontype = models.IntegerField(db_column='eExplosionType', blank=True, null=True)  # Field name made lowercase.
    erecoil = models.IntegerField(db_column='eRecoil', blank=True, null=True)  # Field name made lowercase.
    eweapontype = models.IntegerField(db_column='eWeaponType', blank=True, null=True)  # Field name made lowercase.
    faccuracycooldown = models.FloatField(db_column='fAccuracyCooldown', blank=True, null=True)  # Field name made lowercase.
    faccuracypower = models.FloatField(db_column='fAccuracyPower', blank=True, null=True)  # Field name made lowercase.
    fcrouchmodifier = models.FloatField(db_column='fCrouchModifier', blank=True, null=True)  # Field name made lowercase.
    finvehiclemodifier = models.FloatField(db_column='fInVehicleModifier', blank=True, null=True)  # Field name made lowercase.
    fjumpmodifier = models.FloatField(db_column='fJumpModifier', blank=True, null=True)  # Field name made lowercase.
    fleanmodifier = models.FloatField(db_column='fLeanModifier', blank=True, null=True)  # Field name made lowercase.
    fmarksmanshipfov16_9 = models.FloatField(db_column='fMarksmanshipFOV16_9', blank=True, null=True)  # Field name made lowercase.
    fmarksmanshipfov4_3 = models.FloatField(db_column='fMarksmanshipFOV4_3', blank=True, null=True)  # Field name made lowercase.
    fmarksmanshipmodifier = models.FloatField(db_column='fMarksmanshipModifier', blank=True, null=True)  # Field name made lowercase.
    fmaxrange = models.FloatField(db_column='fMaxRange', blank=True, null=True)  # Field name made lowercase.
    fmaxtimebetweenshots = models.FloatField(db_column='fMaxTimeBetweenShots', blank=True, null=True)  # Field name made lowercase.
    fmindamagerange = models.FloatField(db_column='fMinDamageRange', blank=True, null=True)  # Field name made lowercase.
    fminimumcrosshairwidth = models.FloatField(db_column='fMinimumCrosshairWidth', blank=True, null=True)  # Field name made lowercase.
    fminimumdamagepercentage = models.FloatField(db_column='fMinimumDamagePercentage', blank=True, null=True)  # Field name made lowercase.
    foverallshotmodifiercap = models.FloatField(db_column='fOverallShotModifierCap', blank=True, null=True)  # Field name made lowercase.
    fpershotmodifier = models.FloatField(db_column='fPerShotModifier', blank=True, null=True)  # Field name made lowercase.
    fpiercedamagereduction = models.FloatField(db_column='fPierceDamageReduction', blank=True, null=True)  # Field name made lowercase.
    fpiercedamagescale = models.FloatField(db_column='fPierceDamageScale', blank=True, null=True)  # Field name made lowercase.
    fradiusattenmetres = models.FloatField(db_column='fRadiusAtTenMetres', blank=True, null=True)  # Field name made lowercase.
    frampdistance = models.FloatField(db_column='fRampDistance', blank=True, null=True)  # Field name made lowercase.
    frayspreadattenmetres = models.FloatField(db_column='fRaySpreadAtTenMetres', blank=True, null=True)  # Field name made lowercase.
    frecoverydelay = models.FloatField(db_column='fRecoveryDelay', blank=True, null=True)  # Field name made lowercase.
    frecoverypersecond = models.FloatField(db_column='fRecoveryPerSecond', blank=True, null=True)  # Field name made lowercase.
    frunmodifier = models.FloatField(db_column='fRunModifier', blank=True, null=True)  # Field name made lowercase.
    fsprintmodifier = models.FloatField(db_column='fSprintModifier', blank=True, null=True)  # Field name made lowercase.
    fwalkmodifier = models.FloatField(db_column='fWalkModifier', blank=True, null=True)  # Field name made lowercase.
    fweaponswitchminaccuracy = models.FloatField(db_column='fWeaponSwitchMinAccuracy', blank=True, null=True)  # Field name made lowercase.
    nfreeammo = models.IntegerField(db_column='nFreeAmmo', blank=True, null=True)  # Field name made lowercase.
    nmaxpiercecount = models.IntegerField(db_column='nMaxPierceCount', blank=True, null=True)  # Field name made lowercase.
    nminnumshots = models.IntegerField(db_column='nMinNumShots', blank=True, null=True)  # Field name made lowercase.
    nrayspershot = models.IntegerField(db_column='nRaysPerShot', blank=True, null=True)  # Field name made lowercase.
    ntracerfrequency = models.IntegerField(db_column='nTracerFrequency', blank=True, null=True)  # Field name made lowercase.
    bcanhitownvehicle = models.IntegerField(db_column='bCanHitOwnVehicle', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RangedWeaponType'


class Ratingbands(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fthreatincrement = models.FloatField(db_column='fThreatIncrement', blank=True, null=True)  # Field name made lowercase.
    nbegins = models.IntegerField(db_column='nBegins', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RatingBands'


class Ratingtextures(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplaynamecrim = models.TextField(db_column='sDisplayNameCrim', blank=True, null=True)  # Field name made lowercase.
    sdisplaynameenf = models.TextField(db_column='sDisplayNameEnf', blank=True, null=True)  # Field name made lowercase.
    ehudiconcombocriminal_0 = models.IntegerField(db_column='eHUDIconComboCriminal_0', blank=True, null=True)  # Field name made lowercase.
    ehudiconcombocriminal_1 = models.IntegerField(db_column='eHUDIconComboCriminal_1', blank=True, null=True)  # Field name made lowercase.
    ehudiconcombocriminal_2 = models.IntegerField(db_column='eHUDIconComboCriminal_2', blank=True, null=True)  # Field name made lowercase.
    ehudiconcombocriminal_3 = models.IntegerField(db_column='eHUDIconComboCriminal_3', blank=True, null=True)  # Field name made lowercase.
    ehudiconcombocriminal_4 = models.IntegerField(db_column='eHUDIconComboCriminal_4', blank=True, null=True)  # Field name made lowercase.
    ehudiconcomboenforcer_0 = models.IntegerField(db_column='eHUDIconComboEnforcer_0', blank=True, null=True)  # Field name made lowercase.
    ehudiconcomboenforcer_1 = models.IntegerField(db_column='eHUDIconComboEnforcer_1', blank=True, null=True)  # Field name made lowercase.
    ehudiconcomboenforcer_2 = models.IntegerField(db_column='eHUDIconComboEnforcer_2', blank=True, null=True)  # Field name made lowercase.
    ehudiconcomboenforcer_3 = models.IntegerField(db_column='eHUDIconComboEnforcer_3', blank=True, null=True)  # Field name made lowercase.
    ehudiconcomboenforcer_4 = models.IntegerField(db_column='eHUDIconComboEnforcer_4', blank=True, null=True)  # Field name made lowercase.
    ehudtextureiconcriminal_0 = models.IntegerField(db_column='eHUDTextureIconCriminal_0', blank=True, null=True)  # Field name made lowercase.
    ehudtextureiconcriminal_1 = models.IntegerField(db_column='eHUDTextureIconCriminal_1', blank=True, null=True)  # Field name made lowercase.
    ehudtextureiconcriminal_2 = models.IntegerField(db_column='eHUDTextureIconCriminal_2', blank=True, null=True)  # Field name made lowercase.
    ehudtextureiconcriminal_3 = models.IntegerField(db_column='eHUDTextureIconCriminal_3', blank=True, null=True)  # Field name made lowercase.
    ehudtextureiconcriminal_4 = models.IntegerField(db_column='eHUDTextureIconCriminal_4', blank=True, null=True)  # Field name made lowercase.
    ehudtextureiconenforcer_0 = models.IntegerField(db_column='eHUDTextureIconEnforcer_0', blank=True, null=True)  # Field name made lowercase.
    ehudtextureiconenforcer_1 = models.IntegerField(db_column='eHUDTextureIconEnforcer_1', blank=True, null=True)  # Field name made lowercase.
    ehudtextureiconenforcer_2 = models.IntegerField(db_column='eHUDTextureIconEnforcer_2', blank=True, null=True)  # Field name made lowercase.
    ehudtextureiconenforcer_3 = models.IntegerField(db_column='eHUDTextureIconEnforcer_3', blank=True, null=True)  # Field name made lowercase.
    ehudtextureiconenforcer_4 = models.IntegerField(db_column='eHUDTextureIconEnforcer_4', blank=True, null=True)  # Field name made lowercase.
    eratingtexture = models.IntegerField(db_column='eRatingTexture', blank=True, null=True)  # Field name made lowercase.
    escaleformiconcriminal_0 = models.IntegerField(db_column='eScaleformIconCriminal_0', blank=True, null=True)  # Field name made lowercase.
    escaleformiconcriminal_1 = models.IntegerField(db_column='eScaleformIconCriminal_1', blank=True, null=True)  # Field name made lowercase.
    escaleformiconcriminal_2 = models.IntegerField(db_column='eScaleformIconCriminal_2', blank=True, null=True)  # Field name made lowercase.
    escaleformiconcriminal_3 = models.IntegerField(db_column='eScaleformIconCriminal_3', blank=True, null=True)  # Field name made lowercase.
    escaleformiconcriminal_4 = models.IntegerField(db_column='eScaleformIconCriminal_4', blank=True, null=True)  # Field name made lowercase.
    escaleformiconenforcer_0 = models.IntegerField(db_column='eScaleformIconEnforcer_0', blank=True, null=True)  # Field name made lowercase.
    escaleformiconenforcer_1 = models.IntegerField(db_column='eScaleformIconEnforcer_1', blank=True, null=True)  # Field name made lowercase.
    escaleformiconenforcer_2 = models.IntegerField(db_column='eScaleformIconEnforcer_2', blank=True, null=True)  # Field name made lowercase.
    escaleformiconenforcer_3 = models.IntegerField(db_column='eScaleformIconEnforcer_3', blank=True, null=True)  # Field name made lowercase.
    escaleformiconenforcer_4 = models.IntegerField(db_column='eScaleformIconEnforcer_4', blank=True, null=True)  # Field name made lowercase.
    nrating = models.IntegerField(db_column='nRating', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RatingTextures'


class Redeemablerewards(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    smailbody = models.TextField(db_column='sMailBody', blank=True, null=True)  # Field name made lowercase.
    smailsubject = models.TextField(db_column='sMailSubject', blank=True, null=True)  # Field name made lowercase.
    ehudicon = models.IntegerField(db_column='eHUDIcon', blank=True, null=True)  # Field name made lowercase.
    eredeemablereward = models.IntegerField(db_column='eRedeemableReward', blank=True, null=True)  # Field name made lowercase.
    ereward = models.IntegerField(db_column='eReward', blank=True, null=True)  # Field name made lowercase.
    nkey = models.IntegerField(db_column='nKey', blank=True, null=True)  # Field name made lowercase.
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)  # Field name made lowercase.
    bignoresddvalidation = models.IntegerField(db_column='bIgnoreSddValidation', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RedeemableRewards'


class Referafriendevents(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    ereferafriendevent = models.IntegerField(db_column='eReferAFriendEvent', blank=True, null=True)  # Field name made lowercase.
    bunique = models.IntegerField(db_column='bUnique', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReferAFriendEvents'


class Rewardpackagechildren(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    eitems_0 = models.IntegerField(db_column='eItems_0', blank=True, null=True)  # Field name made lowercase.
    eitems_1 = models.IntegerField(db_column='eItems_1', blank=True, null=True)  # Field name made lowercase.
    eitems_10 = models.IntegerField(db_column='eItems_10', blank=True, null=True)  # Field name made lowercase.
    eitems_11 = models.IntegerField(db_column='eItems_11', blank=True, null=True)  # Field name made lowercase.
    eitems_12 = models.IntegerField(db_column='eItems_12', blank=True, null=True)  # Field name made lowercase.
    eitems_13 = models.IntegerField(db_column='eItems_13', blank=True, null=True)  # Field name made lowercase.
    eitems_14 = models.IntegerField(db_column='eItems_14', blank=True, null=True)  # Field name made lowercase.
    eitems_15 = models.IntegerField(db_column='eItems_15', blank=True, null=True)  # Field name made lowercase.
    eitems_16 = models.IntegerField(db_column='eItems_16', blank=True, null=True)  # Field name made lowercase.
    eitems_17 = models.IntegerField(db_column='eItems_17', blank=True, null=True)  # Field name made lowercase.
    eitems_18 = models.IntegerField(db_column='eItems_18', blank=True, null=True)  # Field name made lowercase.
    eitems_19 = models.IntegerField(db_column='eItems_19', blank=True, null=True)  # Field name made lowercase.
    eitems_2 = models.IntegerField(db_column='eItems_2', blank=True, null=True)  # Field name made lowercase.
    eitems_20 = models.IntegerField(db_column='eItems_20', blank=True, null=True)  # Field name made lowercase.
    eitems_21 = models.IntegerField(db_column='eItems_21', blank=True, null=True)  # Field name made lowercase.
    eitems_22 = models.IntegerField(db_column='eItems_22', blank=True, null=True)  # Field name made lowercase.
    eitems_23 = models.IntegerField(db_column='eItems_23', blank=True, null=True)  # Field name made lowercase.
    eitems_24 = models.IntegerField(db_column='eItems_24', blank=True, null=True)  # Field name made lowercase.
    eitems_25 = models.IntegerField(db_column='eItems_25', blank=True, null=True)  # Field name made lowercase.
    eitems_26 = models.IntegerField(db_column='eItems_26', blank=True, null=True)  # Field name made lowercase.
    eitems_27 = models.IntegerField(db_column='eItems_27', blank=True, null=True)  # Field name made lowercase.
    eitems_28 = models.IntegerField(db_column='eItems_28', blank=True, null=True)  # Field name made lowercase.
    eitems_29 = models.IntegerField(db_column='eItems_29', blank=True, null=True)  # Field name made lowercase.
    eitems_3 = models.IntegerField(db_column='eItems_3', blank=True, null=True)  # Field name made lowercase.
    eitems_30 = models.IntegerField(db_column='eItems_30', blank=True, null=True)  # Field name made lowercase.
    eitems_31 = models.IntegerField(db_column='eItems_31', blank=True, null=True)  # Field name made lowercase.
    eitems_32 = models.IntegerField(db_column='eItems_32', blank=True, null=True)  # Field name made lowercase.
    eitems_33 = models.IntegerField(db_column='eItems_33', blank=True, null=True)  # Field name made lowercase.
    eitems_34 = models.IntegerField(db_column='eItems_34', blank=True, null=True)  # Field name made lowercase.
    eitems_35 = models.IntegerField(db_column='eItems_35', blank=True, null=True)  # Field name made lowercase.
    eitems_36 = models.IntegerField(db_column='eItems_36', blank=True, null=True)  # Field name made lowercase.
    eitems_37 = models.IntegerField(db_column='eItems_37', blank=True, null=True)  # Field name made lowercase.
    eitems_38 = models.IntegerField(db_column='eItems_38', blank=True, null=True)  # Field name made lowercase.
    eitems_39 = models.IntegerField(db_column='eItems_39', blank=True, null=True)  # Field name made lowercase.
    eitems_4 = models.IntegerField(db_column='eItems_4', blank=True, null=True)  # Field name made lowercase.
    eitems_5 = models.IntegerField(db_column='eItems_5', blank=True, null=True)  # Field name made lowercase.
    eitems_6 = models.IntegerField(db_column='eItems_6', blank=True, null=True)  # Field name made lowercase.
    eitems_7 = models.IntegerField(db_column='eItems_7', blank=True, null=True)  # Field name made lowercase.
    eitems_8 = models.IntegerField(db_column='eItems_8', blank=True, null=True)  # Field name made lowercase.
    eitems_9 = models.IntegerField(db_column='eItems_9', blank=True, null=True)  # Field name made lowercase.
    erewardpackagechild = models.IntegerField(db_column='eRewardPackageChild', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    bselectable = models.IntegerField(db_column='bSelectable', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RewardPackageChildren'


class Rewardpackageitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    smailbody = models.TextField(db_column='sMailBody', blank=True, null=True)  # Field name made lowercase.
    smailsubject = models.TextField(db_column='sMailSubject', blank=True, null=True)  # Field name made lowercase.
    echeckunlock = models.IntegerField(db_column='eCheckUnlock', blank=True, null=True)  # Field name made lowercase.
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    erewardpackage = models.IntegerField(db_column='eRewardPackage', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    egenderrestriction = models.IntegerField(db_column='eGenderRestriction', blank=True, null=True)  # Field name made lowercase.
    bdescriptionshowsitems = models.IntegerField(db_column='bDescriptionShowsItems', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RewardPackageItemTypes'


class Rewardpackages(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    echildpackage = models.IntegerField(db_column='eChildPackage', blank=True, null=True)  # Field name made lowercase.
    eitems_0 = models.IntegerField(db_column='eItems_0', blank=True, null=True)  # Field name made lowercase.
    eitems_1 = models.IntegerField(db_column='eItems_1', blank=True, null=True)  # Field name made lowercase.
    eitems_2 = models.IntegerField(db_column='eItems_2', blank=True, null=True)  # Field name made lowercase.
    eitems_3 = models.IntegerField(db_column='eItems_3', blank=True, null=True)  # Field name made lowercase.
    eitems_4 = models.IntegerField(db_column='eItems_4', blank=True, null=True)  # Field name made lowercase.
    eitems_5 = models.IntegerField(db_column='eItems_5', blank=True, null=True)  # Field name made lowercase.
    eitems_6 = models.IntegerField(db_column='eItems_6', blank=True, null=True)  # Field name made lowercase.
    eitems_7 = models.IntegerField(db_column='eItems_7', blank=True, null=True)  # Field name made lowercase.
    eitems_8 = models.IntegerField(db_column='eItems_8', blank=True, null=True)  # Field name made lowercase.
    eitems_9 = models.IntegerField(db_column='eItems_9', blank=True, null=True)  # Field name made lowercase.
    erewardpackage = models.IntegerField(db_column='eRewardPackage', blank=True, null=True)  # Field name made lowercase.
    ncash = models.IntegerField(db_column='nCash', blank=True, null=True)  # Field name made lowercase.
    ncharges_0 = models.IntegerField(db_column='nCharges_0', blank=True, null=True)  # Field name made lowercase.
    ncharges_1 = models.IntegerField(db_column='nCharges_1', blank=True, null=True)  # Field name made lowercase.
    nrewardtokens_0 = models.IntegerField(db_column='nRewardTokens_0', blank=True, null=True)  # Field name made lowercase.
    nrewardtokens_1 = models.IntegerField(db_column='nRewardTokens_1', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    bsendmail = models.IntegerField(db_column='bSendMail', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RewardPackages'


class Rolemilestoneformulae(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    erolemilestoneformula = models.IntegerField(db_column='eRoleMilestoneFormula', blank=True, null=True)  # Field name made lowercase.
    ba_optional = models.IntegerField(db_column='bA_Optional', blank=True, null=True)  # Field name made lowercase.
    ba_required = models.IntegerField(db_column='bA_Required', blank=True, null=True)  # Field name made lowercase.
    bb_optional = models.IntegerField(db_column='bB_Optional', blank=True, null=True)  # Field name made lowercase.
    bb_required = models.IntegerField(db_column='bB_Required', blank=True, null=True)  # Field name made lowercase.
    bc_optional = models.IntegerField(db_column='bC_Optional', blank=True, null=True)  # Field name made lowercase.
    bc_required = models.IntegerField(db_column='bC_Required', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoleMilestoneFormulae'


class Rolemilestones(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    siconoverlaytext = models.TextField(db_column='sIconOverlayText', blank=True, null=True)  # Field name made lowercase.
    srewardmailbody = models.TextField(db_column='sRewardMailBody', blank=True, null=True)  # Field name made lowercase.
    srewardmailsubject = models.TextField(db_column='sRewardMailSubject', blank=True, null=True)  # Field name made lowercase.
    stitle = models.TextField(db_column='sTitle', blank=True, null=True)  # Field name made lowercase.
    eformula = models.IntegerField(db_column='eFormula', blank=True, null=True)  # Field name made lowercase.
    ereward = models.IntegerField(db_column='eReward', blank=True, null=True)  # Field name made lowercase.
    eroleicon = models.IntegerField(db_column='eRoleIcon', blank=True, null=True)  # Field name made lowercase.
    erolemilestone = models.IntegerField(db_column='eRoleMilestone', blank=True, null=True)  # Field name made lowercase.
    fpassmark_0 = models.FloatField(db_column='fPassMark_0', blank=True, null=True)  # Field name made lowercase.
    fpassmark_1 = models.FloatField(db_column='fPassMark_1', blank=True, null=True)  # Field name made lowercase.
    fpassmark_2 = models.FloatField(db_column='fPassMark_2', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoleMilestones'


class Rulesetexclusions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eruleset_0 = models.IntegerField(db_column='eRuleSet_0', blank=True, null=True)  # Field name made lowercase.
    eruleset_1 = models.IntegerField(db_column='eRuleSet_1', blank=True, null=True)  # Field name made lowercase.
    eruleset_2 = models.IntegerField(db_column='eRuleSet_2', blank=True, null=True)  # Field name made lowercase.
    eruleset_3 = models.IntegerField(db_column='eRuleSet_3', blank=True, null=True)  # Field name made lowercase.
    eruleset_4 = models.IntegerField(db_column='eRuleSet_4', blank=True, null=True)  # Field name made lowercase.
    eruleset_5 = models.IntegerField(db_column='eRuleSet_5', blank=True, null=True)  # Field name made lowercase.
    eruleset_6 = models.IntegerField(db_column='eRuleSet_6', blank=True, null=True)  # Field name made lowercase.
    eruleset_7 = models.IntegerField(db_column='eRuleSet_7', blank=True, null=True)  # Field name made lowercase.
    eruleset_8 = models.IntegerField(db_column='eRuleSet_8', blank=True, null=True)  # Field name made lowercase.
    eruleset_9 = models.IntegerField(db_column='eRuleSet_9', blank=True, null=True)  # Field name made lowercase.
    erulesetexclusion = models.IntegerField(db_column='eRuleSetExclusion', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RuleSetExclusions'


class Scaleformcriticaltimers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sicon = models.TextField(db_column='sIcon', blank=True, null=True)  # Field name made lowercase.
    stext = models.TextField(db_column='sText', blank=True, null=True)  # Field name made lowercase.
    npriority = models.IntegerField(db_column='nPriority', blank=True, null=True)  # Field name made lowercase.
    escaleformcriticaltimer = models.IntegerField(db_column='eScaleformCriticalTimer', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ScaleformCriticalTimers'


class Scaleformicons(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    siconsetname = models.TextField(db_column='sIconSetName', blank=True, null=True)  # Field name made lowercase.
    smoviename = models.TextField(db_column='sMovieName', blank=True, null=True)  # Field name made lowercase.
    escaleformicon = models.IntegerField(db_column='eScaleformIcon', blank=True, null=True)  # Field name made lowercase.
    nframenumber = models.IntegerField(db_column='nFrameNumber', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ScaleformIcons'


class Scaleforminterfaces(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sscene = models.TextField(db_column='sScene', blank=True, null=True)  # Field name made lowercase.
    elayer = models.IntegerField(db_column='eLayer', blank=True, null=True)  # Field name made lowercase.
    npriority = models.IntegerField(db_column='nPriority', blank=True, null=True)  # Field name made lowercase.
    elayoutmode = models.IntegerField(db_column='eLayoutMode', blank=True, null=True)  # Field name made lowercase.
    escaleforminterface = models.IntegerField(db_column='eScaleformInterface', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ScaleformInterfaces'


class Scaleformlayers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    slayerbackground = models.TextField(db_column='sLayerBackground', blank=True, null=True)  # Field name made lowercase.
    escaleformlayer = models.IntegerField(db_column='eScaleformLayer', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    bblurwhenactive = models.IntegerField(db_column='bBlurWhenActive', blank=True, null=True)  # Field name made lowercase.
    bcaptureinput = models.IntegerField(db_column='bCaptureInput', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ScaleformLayers'


class Scenelayers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    escenelayer = models.IntegerField(db_column='eSceneLayer', blank=True, null=True)  # Field name made lowercase.
    blimitopenfrequency = models.IntegerField(db_column='bLimitOpenFrequency', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SceneLayers'


class Scorecategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    escorecategory = models.IntegerField(db_column='eScoreCategory', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ScoreCategories'


class Scoreboarddescriptions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplaytext = models.TextField(db_column='sDisplayText', blank=True, null=True)  # Field name made lowercase.
    escoreboarddescription = models.IntegerField(db_column='eScoreboardDescription', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ScoreboardDescriptions'


class Securityviolations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    scategory = models.TextField(db_column='sCategory', blank=True, null=True)  # Field name made lowercase.
    skickmessage = models.TextField(db_column='sKickMessage', blank=True, null=True)  # Field name made lowercase.
    nbandurationdays = models.IntegerField(db_column='nBanDurationDays', blank=True, null=True)  # Field name made lowercase.
    esecurityviolation = models.IntegerField(db_column='eSecurityViolation', blank=True, null=True)  # Field name made lowercase.
    bban = models.IntegerField(db_column='bBan', blank=True, null=True)  # Field name made lowercase.
    bkick = models.IntegerField(db_column='bKick', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SecurityViolations'


class Shopuifilterrestrictions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eiteminfracategory = models.IntegerField(db_column='eItemInfraCategory', blank=True, null=True)  # Field name made lowercase.
    eshopuifilterrestriction = models.IntegerField(db_column='eShopUIFilterRestriction', blank=True, null=True)  # Field name made lowercase.
    eunlockvehiclecomponentcategory = models.IntegerField(db_column='eUnlockVehicleComponentCategory', blank=True, null=True)  # Field name made lowercase.
    eunlockweapontype = models.IntegerField(db_column='eUnlockWeaponType', blank=True, null=True)  # Field name made lowercase.
    eweapontype = models.IntegerField(db_column='eWeaponType', blank=True, null=True)  # Field name made lowercase.
    ecustomisable = models.IntegerField(db_column='eCustomisable', blank=True, null=True)  # Field name made lowercase.
    eitemcategory = models.IntegerField(db_column='eItemCategory', blank=True, null=True)  # Field name made lowercase.
    eitemsubcategory = models.IntegerField(db_column='eItemSubCategory', blank=True, null=True)  # Field name made lowercase.
    emodifierclass = models.IntegerField(db_column='eModifierClass', blank=True, null=True)  # Field name made lowercase.
    emodifiertype = models.IntegerField(db_column='eModifierType', blank=True, null=True)  # Field name made lowercase.
    eunlockitemcategory = models.IntegerField(db_column='eUnlockItemCategory', blank=True, null=True)  # Field name made lowercase.
    eunlockitemsubcategory = models.IntegerField(db_column='eUnlockItemSubCategory', blank=True, null=True)  # Field name made lowercase.
    eunlockmodifierclass = models.IntegerField(db_column='eUnlockModifierClass', blank=True, null=True)  # Field name made lowercase.
    eunlockmodifiertype = models.IntegerField(db_column='eUnlockModifierType', blank=True, null=True)  # Field name made lowercase.
    bembeddeditem = models.IntegerField(db_column='bEmbeddedItem', blank=True, null=True)  # Field name made lowercase.
    bequipable = models.IntegerField(db_column='bEquipable', blank=True, null=True)  # Field name made lowercase.
    bnotdeployed = models.IntegerField(db_column='bNotDeployed', blank=True, null=True)  # Field name made lowercase.
    btrade = models.IntegerField(db_column='bTrade', blank=True, null=True)  # Field name made lowercase.
    bunlockcapacity = models.IntegerField(db_column='bUnlockCapacity', blank=True, null=True)  # Field name made lowercase.
    bunlockemote = models.IntegerField(db_column='bUnlockEmote', blank=True, null=True)  # Field name made lowercase.
    bunlocksymbolprimitive = models.IntegerField(db_column='bUnlockSymbolPrimitive', blank=True, null=True)  # Field name made lowercase.
    bunlockvehiclecomponent = models.IntegerField(db_column='bUnlockVehicleComponent', blank=True, null=True)  # Field name made lowercase.
    bunused = models.IntegerField(db_column='bUnused', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShopUIFilterRestrictions'


class Shopuifilters(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sname = models.TextField(db_column='sName', blank=True, null=True)  # Field name made lowercase.
    eenable_0 = models.IntegerField(db_column='eEnable_0', blank=True, null=True)  # Field name made lowercase.
    eenable_1 = models.IntegerField(db_column='eEnable_1', blank=True, null=True)  # Field name made lowercase.
    eenable_2 = models.IntegerField(db_column='eEnable_2', blank=True, null=True)  # Field name made lowercase.
    eoption_0 = models.IntegerField(db_column='eOption_0', blank=True, null=True)  # Field name made lowercase.
    eoption_1 = models.IntegerField(db_column='eOption_1', blank=True, null=True)  # Field name made lowercase.
    eoption_2 = models.IntegerField(db_column='eOption_2', blank=True, null=True)  # Field name made lowercase.
    eoption_3 = models.IntegerField(db_column='eOption_3', blank=True, null=True)  # Field name made lowercase.
    eparent = models.IntegerField(db_column='eParent', blank=True, null=True)  # Field name made lowercase.
    eshop_0 = models.IntegerField(db_column='eShop_0', blank=True, null=True)  # Field name made lowercase.
    eshop_1 = models.IntegerField(db_column='eShop_1', blank=True, null=True)  # Field name made lowercase.
    eshop_2 = models.IntegerField(db_column='eShop_2', blank=True, null=True)  # Field name made lowercase.
    eshop_3 = models.IntegerField(db_column='eShop_3', blank=True, null=True)  # Field name made lowercase.
    eshop_4 = models.IntegerField(db_column='eShop_4', blank=True, null=True)  # Field name made lowercase.
    eshopuifilter = models.IntegerField(db_column='eShopUIFilter', blank=True, null=True)  # Field name made lowercase.
    ndefaultweighting = models.IntegerField(db_column='nDefaultWeighting', blank=True, null=True)  # Field name made lowercase.
    bdevonly = models.IntegerField(db_column='bDevOnly', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShopUIFilters'


class Shopuishops(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eshopuishop = models.IntegerField(db_column='eShopUIShop', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShopUIShops'


class Skillratingconstants(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)  # Field name made lowercase.
    eskillratingconstant = models.IntegerField(db_column='eSkillRatingConstant', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SkillRatingConstants'


class Songitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sresource = models.TextField(db_column='sResource', blank=True, null=True)  # Field name made lowercase.
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SongItemTypes'


class Spawnconstant(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)  # Field name made lowercase.
    espawnconstant = models.IntegerField(db_column='eSpawnConstant', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SpawnConstant'


class Spawnvariables(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fspawndistanceafk = models.FloatField(db_column='fSpawnDistanceAFK', blank=True, null=True)  # Field name made lowercase.
    fspawndistanceobjectivemaximum = models.FloatField(db_column='fSpawnDistanceObjectiveMaximum', blank=True, null=True)  # Field name made lowercase.
    fspawndistanceobjectiveminimum = models.FloatField(db_column='fSpawnDistanceObjectiveMinimum', blank=True, null=True)  # Field name made lowercase.
    fspawndistanceopponentignored = models.FloatField(db_column='fSpawnDistanceOpponentIgnored', blank=True, null=True)  # Field name made lowercase.
    fspawndistanceopponentinvalid = models.FloatField(db_column='fSpawnDistanceOpponentInvalid', blank=True, null=True)  # Field name made lowercase.
    fspawndistanceoppositionspawnzone = models.FloatField(db_column='fSpawnDistanceOppositionSpawnZone', blank=True, null=True)  # Field name made lowercase.
    fspawndistanceotherspawnzone = models.FloatField(db_column='fSpawnDistanceOtherSpawnZone', blank=True, null=True)  # Field name made lowercase.
    fspawndistanceplayer = models.FloatField(db_column='fSpawnDistancePlayer', blank=True, null=True)  # Field name made lowercase.
    fspawndistanceteammateliving = models.FloatField(db_column='fSpawnDistanceTeamMateLiving', blank=True, null=True)  # Field name made lowercase.
    fspawnvehicledistanceopponent = models.FloatField(db_column='fSpawnVehicleDistanceOpponent', blank=True, null=True)  # Field name made lowercase.
    fspawnvehicledistanceplayermaximum = models.FloatField(db_column='fSpawnVehicleDistancePlayerMaximum', blank=True, null=True)  # Field name made lowercase.
    fspawnvehicledistanceplayerminimum = models.FloatField(db_column='fSpawnVehicleDistancePlayerMinimum', blank=True, null=True)  # Field name made lowercase.
    fspawnvehicleheightmaximum = models.FloatField(db_column='fSpawnVehicleHeightMaximum', blank=True, null=True)  # Field name made lowercase.
    fspawnwo = models.FloatField(db_column='fSpawnWo', blank=True, null=True)  # Field name made lowercase.
    fspawnwp = models.FloatField(db_column='fSpawnWp', blank=True, null=True)  # Field name made lowercase.
    erelaxationrule = models.IntegerField(db_column='eRelaxationRule', blank=True, null=True)  # Field name made lowercase.
    espawnvariable = models.IntegerField(db_column='eSpawnVariable', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SpawnVariables'


class Streetname(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplayedstreetname = models.TextField(db_column='sDisplayedStreetName', blank=True, null=True)  # Field name made lowercase.
    edistrict = models.IntegerField(db_column='eDistrict', blank=True, null=True)  # Field name made lowercase.
    estreetnameid = models.IntegerField(db_column='eStreetNameID', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StreetName'


class Symboleditormenuentries(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplayimage = models.TextField(db_column='sDisplayImage', blank=True, null=True)  # Field name made lowercase.
    sdisplaytext = models.TextField(db_column='sDisplayText', blank=True, null=True)  # Field name made lowercase.
    smenulevel = models.TextField(db_column='sMenuLevel', blank=True, null=True)  # Field name made lowercase.
    smenutag = models.TextField(db_column='sMenuTag', blank=True, null=True)  # Field name made lowercase.
    soptionalscene = models.TextField(db_column='sOptionalScene', blank=True, null=True)  # Field name made lowercase.
    esymboleditormenuentry = models.IntegerField(db_column='eSymbolEditorMenuEntry', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SymbolEditorMenuEntries'


class Symbolitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sresource = models.TextField(db_column='sResource', blank=True, null=True)  # Field name made lowercase.
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SymbolItemTypes'


class Tesprojectioninfos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fmaxvalueatpremiumlevel_0 = models.FloatField(db_column='fMaxValueAtPremiumLevel_0', blank=True, null=True)  # Field name made lowercase.
    fmaxvalueatpremiumlevel_1 = models.FloatField(db_column='fMaxValueAtPremiumLevel_1', blank=True, null=True)  # Field name made lowercase.
    etesprojectioninfo = models.IntegerField(db_column='eTESProjectionInfo', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TESProjectionInfos'


class TodEventAllowedtooverrides(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eevent_allowedtooverride = models.IntegerField(db_column='eEvent_AllowedToOverride', blank=True, null=True)  # Field name made lowercase.
    etod_event = models.IntegerField(db_column='eTOD_Event', blank=True, null=True)  # Field name made lowercase.
    etod = models.IntegerField(db_column='eTOD', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TOD_Event_AllowedToOverrides'


class TodEvents(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etod_event = models.IntegerField(db_column='eTOD_Event', blank=True, null=True)  # Field name made lowercase.
    eevent = models.IntegerField(db_column='eEvent', blank=True, null=True)  # Field name made lowercase.
    etod = models.IntegerField(db_column='eTOD', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TOD_Events'


class Taskitemboomboxes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    samptype = models.TextField(db_column='sAmpType', blank=True, null=True)  # Field name made lowercase.
    efriendlyhudmarker = models.IntegerField(db_column='eFriendlyHUDMarker', blank=True, null=True)  # Field name made lowercase.
    eoppositionhudmarker = models.IntegerField(db_column='eOppositionHUDMarker', blank=True, null=True)  # Field name made lowercase.
    etaskitemboombox = models.IntegerField(db_column='eTaskItemBoomBox', blank=True, null=True)  # Field name made lowercase.
    fampattenuationscale = models.FloatField(db_column='fAmpAttenuationScale', blank=True, null=True)  # Field name made lowercase.
    fampvolume = models.FloatField(db_column='fAmpVolume', blank=True, null=True)  # Field name made lowercase.
    ffriendlyradius = models.FloatField(db_column='fFriendlyRadius', blank=True, null=True)  # Field name made lowercase.
    foppositionradius = models.FloatField(db_column='fOppositionRadius', blank=True, null=True)  # Field name made lowercase.
    fspeakereq1 = models.FloatField(db_column='fSpeakerEQ1', blank=True, null=True)  # Field name made lowercase.
    fspeakereq2 = models.FloatField(db_column='fSpeakerEQ2', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskItemBoomBoxes'


class Taskitemcategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    etaskitemcategory = models.IntegerField(db_column='eTaskItemCategory', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskItemCategories'


class Taskitemdamagedpickups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sassetname = models.TextField(db_column='sAssetName', blank=True, null=True)  # Field name made lowercase.
    sdamagesfx = models.TextField(db_column='sDamageSFX', blank=True, null=True)  # Field name made lowercase.
    sdamagevfx = models.TextField(db_column='sDamageVFX', blank=True, null=True)  # Field name made lowercase.
    srecoversfx = models.TextField(db_column='sRecoverSFX', blank=True, null=True)  # Field name made lowercase.
    srecovervfx = models.TextField(db_column='sRecoverVFX', blank=True, null=True)  # Field name made lowercase.
    etaskitemvisual = models.IntegerField(db_column='eTaskItemVisual', blank=True, null=True)  # Field name made lowercase.
    bdetroyeddamagestate = models.IntegerField(db_column='bDetroyedDamageState', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskItemDamagedPickups'


class Taskitemeffects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    stimedexplosivesfxend = models.TextField(db_column='sTimedExplosiveSFXEnd', blank=True, null=True)  # Field name made lowercase.
    stimedexplosivesfxstart = models.TextField(db_column='sTimedExplosiveSFXStart', blank=True, null=True)  # Field name made lowercase.
    eboombox = models.IntegerField(db_column='eBoomBox', blank=True, null=True)  # Field name made lowercase.
    eexplosion = models.IntegerField(db_column='eExplosion', blank=True, null=True)  # Field name made lowercase.
    etaskitemeffect = models.IntegerField(db_column='eTaskItemEffect', blank=True, null=True)  # Field name made lowercase.
    ffieldsupplierradius = models.FloatField(db_column='fFieldSupplierRadius', blank=True, null=True)  # Field name made lowercase.
    fjumpzmodifier = models.FloatField(db_column='fJumpZModifier', blank=True, null=True)  # Field name made lowercase.
    frepairmultiplier = models.FloatField(db_column='fRepairMultiplier', blank=True, null=True)  # Field name made lowercase.
    ftimedexplosionduration = models.FloatField(db_column='fTimedExplosionDuration', blank=True, null=True)  # Field name made lowercase.
    nfieldsupplieramount = models.IntegerField(db_column='nFieldSupplierAmount', blank=True, null=True)  # Field name made lowercase.
    nhealth = models.IntegerField(db_column='nHealth', blank=True, null=True)  # Field name made lowercase.
    nsymbolmaterialindex = models.IntegerField(db_column='nSymbolMaterialIndex', blank=True, null=True)  # Field name made lowercase.
    bdontbounce = models.IntegerField(db_column='bDontBounce', blank=True, null=True)  # Field name made lowercase.
    bhasgrip = models.IntegerField(db_column='bHasGrip', blank=True, null=True)  # Field name made lowercase.
    bhostssymbol = models.IntegerField(db_column='bHostsSymbol', blank=True, null=True)  # Field name made lowercase.
    bragdollondeath = models.IntegerField(db_column='bRagdollOnDeath', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskItemEffects'


class Taskitemgiftboxcontents(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    edefaultweaponskin = models.IntegerField(db_column='eDefaultWeaponSkin', blank=True, null=True)  # Field name made lowercase.
    efnmods_0 = models.IntegerField(db_column='eFnMods_0', blank=True, null=True)  # Field name made lowercase.
    efnmods_1 = models.IntegerField(db_column='eFnMods_1', blank=True, null=True)  # Field name made lowercase.
    efnmods_2 = models.IntegerField(db_column='eFnMods_2', blank=True, null=True)  # Field name made lowercase.
    eitemtype = models.IntegerField(db_column='eItemType', blank=True, null=True)  # Field name made lowercase.
    etaskitemgiftbox = models.IntegerField(db_column='eTaskItemGiftBox', blank=True, null=True)  # Field name made lowercase.
    nmaxextraitems = models.IntegerField(db_column='nMaxExtraItems', blank=True, null=True)  # Field name made lowercase.
    nminextraitems = models.IntegerField(db_column='nMinExtraItems', blank=True, null=True)  # Field name made lowercase.
    nweight = models.IntegerField(db_column='nWeight', blank=True, null=True)  # Field name made lowercase.
    bselectrandomskin = models.IntegerField(db_column='bSelectRandomSkin', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskItemGiftBoxContents'


class Taskitemgiftboxmodifierentries(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ecategory = models.IntegerField(db_column='eCategory', blank=True, null=True)  # Field name made lowercase.
    eitem = models.IntegerField(db_column='eItem', blank=True, null=True)  # Field name made lowercase.
    etaskitemgiftboxmodifier = models.IntegerField(db_column='eTaskItemGiftBoxModifier', blank=True, null=True)  # Field name made lowercase.
    fweight = models.FloatField(db_column='fWeight', blank=True, null=True)  # Field name made lowercase.
    etheme = models.IntegerField(db_column='eTheme', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskItemGiftBoxModifierEntries'


class Taskitemgiftboxmodifiers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskitemgiftboxmodifier = models.IntegerField(db_column='eTaskItemGiftBoxModifier', blank=True, null=True)  # Field name made lowercase.
    fchancenomod = models.FloatField(db_column='fChanceNoMod', blank=True, null=True)  # Field name made lowercase.
    fweightperlevel_0 = models.FloatField(db_column='fWeightPerLevel_0', blank=True, null=True)  # Field name made lowercase.
    fweightperlevel_1 = models.FloatField(db_column='fWeightPerLevel_1', blank=True, null=True)  # Field name made lowercase.
    fweightperlevel_2 = models.FloatField(db_column='fWeightPerLevel_2', blank=True, null=True)  # Field name made lowercase.
    fweightperlevel_3 = models.FloatField(db_column='fWeightPerLevel_3', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskItemGiftBoxModifiers'


class Taskitemgiftboxes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sactivevfx = models.TextField(db_column='sActiveVFX', blank=True, null=True)  # Field name made lowercase.
    sinactivevfx = models.TextField(db_column='sInactiveVFX', blank=True, null=True)  # Field name made lowercase.
    sstartactivesfx = models.TextField(db_column='sStartActiveSFX', blank=True, null=True)  # Field name made lowercase.
    sstopactivesfx = models.TextField(db_column='sStopActiveSFX', blank=True, null=True)  # Field name made lowercase.
    etaskitemgiftbox = models.IntegerField(db_column='eTaskItemGiftBox', blank=True, null=True)  # Field name made lowercase.
    factivationspintime = models.FloatField(db_column='fActivationSpinTime', blank=True, null=True)  # Field name made lowercase.
    faddeddropdirectionalvelocitymax = models.FloatField(db_column='fAddedDropDirectionalVelocityMax', blank=True, null=True)  # Field name made lowercase.
    faddeddropdirectionalvelocitymin = models.FloatField(db_column='fAddedDropDirectionalVelocityMin', blank=True, null=True)  # Field name made lowercase.
    faddeddropupvelocitymax = models.FloatField(db_column='fAddedDropUpVelocityMax', blank=True, null=True)  # Field name made lowercase.
    faddeddropupvelocitymin = models.FloatField(db_column='fAddedDropUpVelocityMin', blank=True, null=True)  # Field name made lowercase.
    fmaximumrotationspeed = models.FloatField(db_column='fMaximumRotationSpeed', blank=True, null=True)  # Field name made lowercase.
    frotationacceleration = models.FloatField(db_column='fRotationAcceleration', blank=True, null=True)  # Field name made lowercase.
    frotationspeed = models.FloatField(db_column='fRotationSpeed', blank=True, null=True)  # Field name made lowercase.
    fvfxoffsetx = models.FloatField(db_column='fVFXOffsetX', blank=True, null=True)  # Field name made lowercase.
    fvfxoffsety = models.FloatField(db_column='fVFXOffsetY', blank=True, null=True)  # Field name made lowercase.
    fvfxoffsetz = models.FloatField(db_column='fVFXOffsetZ', blank=True, null=True)  # Field name made lowercase.
    eavailability = models.IntegerField(db_column='eAvailability', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskItemGiftBoxes'


class Taskitemsizes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    ncargopips = models.IntegerField(db_column='nCargoPips', blank=True, null=True)  # Field name made lowercase.
    eencumbrance = models.IntegerField(db_column='eEncumbrance', blank=True, null=True)  # Field name made lowercase.
    etaskitemsize = models.IntegerField(db_column='eTaskItemSize', blank=True, null=True)  # Field name made lowercase.
    bcancarry = models.IntegerField(db_column='bCanCarry', blank=True, null=True)  # Field name made lowercase.
    bslowpickup = models.IntegerField(db_column='bSlowPickup', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskItemSizes'


class Taskitemsubcategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    egameplayobject = models.IntegerField(db_column='eGameplayObject', blank=True, null=True)  # Field name made lowercase.
    etaskitemsubcategory = models.IntegerField(db_column='eTaskItemSubCategory', blank=True, null=True)  # Field name made lowercase.
    etaskitemcategory = models.IntegerField(db_column='eTaskItemCategory', blank=True, null=True)  # Field name made lowercase.
    etaskitemsize = models.IntegerField(db_column='eTaskItemSize', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskItemSubCategories'


class Taskitemtags(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskitemtag = models.IntegerField(db_column='eTaskItemTag', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskItemTags'


class Taskitemvarieties(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    eeffect = models.IntegerField(db_column='eEffect', blank=True, null=True)  # Field name made lowercase.
    egiftbox = models.IntegerField(db_column='eGiftBox', blank=True, null=True)  # Field name made lowercase.
    ehudiconcombo = models.IntegerField(db_column='eHUDIconCombo', blank=True, null=True)  # Field name made lowercase.
    ehudmarkervisual = models.IntegerField(db_column='eHUDMarkerVisual', blank=True, null=True)  # Field name made lowercase.
    emetatag_0 = models.IntegerField(db_column='eMetaTag_0', blank=True, null=True)  # Field name made lowercase.
    emetatag_1 = models.IntegerField(db_column='eMetaTag_1', blank=True, null=True)  # Field name made lowercase.
    emetatag_2 = models.IntegerField(db_column='eMetaTag_2', blank=True, null=True)  # Field name made lowercase.
    etaskitemsubcategory = models.IntegerField(db_column='eTaskItemSubCategory', blank=True, null=True)  # Field name made lowercase.
    etaskitemvariety = models.IntegerField(db_column='eTaskItemVariety', blank=True, null=True)  # Field name made lowercase.
    etaskitemvisual = models.IntegerField(db_column='eTaskItemVisual', blank=True, null=True)  # Field name made lowercase.
    fgiftboxoffsetx = models.FloatField(db_column='fGiftBoxOffsetX', blank=True, null=True)  # Field name made lowercase.
    fgiftboxoffsety = models.FloatField(db_column='fGiftBoxOffsetY', blank=True, null=True)  # Field name made lowercase.
    fgiftboxoffsetz = models.FloatField(db_column='fGiftBoxOffsetZ', blank=True, null=True)  # Field name made lowercase.
    fvehicleheightreductionamount = models.FloatField(db_column='fVehicleHeightReductionAmount', blank=True, null=True)  # Field name made lowercase.
    fvehicletorquereductionfactor = models.FloatField(db_column='fVehicleTorqueReductionFactor', blank=True, null=True)  # Field name made lowercase.
    nexpensetariff = models.IntegerField(db_column='nExpenseTariff', blank=True, null=True)  # Field name made lowercase.
    bhidehudmarkerwhilecarried = models.IntegerField(db_column='bHideHUDMarkerWhileCarried', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskItemVarieties'


class Taskitemvisuals(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    spickupanimsetasset = models.TextField(db_column='sPickupAnimSetAsset', blank=True, null=True)  # Field name made lowercase.
    spickupanimtreeasset = models.TextField(db_column='sPickupAnimTreeAsset', blank=True, null=True)  # Field name made lowercase.
    spickupassetname = models.TextField(db_column='sPickupAssetName', blank=True, null=True)  # Field name made lowercase.
    spickupphysicsasset = models.TextField(db_column='sPickupPhysicsAsset', blank=True, null=True)  # Field name made lowercase.
    eitemattachmentvisual = models.IntegerField(db_column='eItemAttachmentVisual', blank=True, null=True)  # Field name made lowercase.
    etaskitemvisual = models.IntegerField(db_column='eTaskItemVisual', blank=True, null=True)  # Field name made lowercase.
    fcollisionheight = models.FloatField(db_column='fCollisionHeight', blank=True, null=True)  # Field name made lowercase.
    fpickupoffsetx = models.FloatField(db_column='fPickupOffsetX', blank=True, null=True)  # Field name made lowercase.
    fpickupoffsety = models.FloatField(db_column='fPickupOffsetY', blank=True, null=True)  # Field name made lowercase.
    fpickupoffsetz = models.FloatField(db_column='fPickupOffsetZ', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskItemVisuals'


class Taskobjectives(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdispatchbrief = models.TextField(db_column='sDispatchBrief', blank=True, null=True)  # Field name made lowercase.
    sownerbrief = models.TextField(db_column='sOwnerBrief', blank=True, null=True)  # Field name made lowercase.
    emissiontemplate = models.IntegerField(db_column='eMissionTemplate', blank=True, null=True)  # Field name made lowercase.
    eoperation = models.IntegerField(db_column='eOperation', blank=True, null=True)  # Field name made lowercase.
    etargetallocation = models.IntegerField(db_column='eTargetAllocation', blank=True, null=True)  # Field name made lowercase.
    etaskitemvariety = models.IntegerField(db_column='eTaskItemVariety', blank=True, null=True)  # Field name made lowercase.
    etaskobjective = models.IntegerField(db_column='eTaskObjective', blank=True, null=True)  # Field name made lowercase.
    evehiclecategory = models.IntegerField(db_column='eVehicleCategory', blank=True, null=True)  # Field name made lowercase.
    ntargetsrequired = models.IntegerField(db_column='nTargetsRequired', blank=True, null=True)  # Field name made lowercase.
    ntaskitemsavailable = models.IntegerField(db_column='nTaskItemsAvailable', blank=True, null=True)  # Field name made lowercase.
    ntaskitemsrequired = models.IntegerField(db_column='nTaskItemsRequired', blank=True, null=True)  # Field name made lowercase.
    ntimelimit = models.IntegerField(db_column='nTimeLimit', blank=True, null=True)  # Field name made lowercase.
    nvehiclesrequired = models.IntegerField(db_column='nVehiclesRequired', blank=True, null=True)  # Field name made lowercase.
    eitembatch = models.IntegerField(db_column='eItemBatch', blank=True, null=True)  # Field name made lowercase.
    eopposingsidevipassignment = models.IntegerField(db_column='eOpposingSideVIPAssignment', blank=True, null=True)  # Field name made lowercase.
    eowningsidevipassignment = models.IntegerField(db_column='eOwningSideVIPAssignment', blank=True, null=True)  # Field name made lowercase.
    estage = models.IntegerField(db_column='eStage', blank=True, null=True)  # Field name made lowercase.
    etaskitemspecificationmethod = models.IntegerField(db_column='eTaskItemSpecificationMethod', blank=True, null=True)  # Field name made lowercase.
    evehiclebatch = models.IntegerField(db_column='eVehicleBatch', blank=True, null=True)  # Field name made lowercase.
    bbonustime = models.IntegerField(db_column='bBonusTime', blank=True, null=True)  # Field name made lowercase.
    bclearopposingsideviptakeoutsonstart = models.IntegerField(db_column='bClearOpposingSideVIPTakeoutsOnStart', blank=True, null=True)  # Field name made lowercase.
    bclearowningsideviptakeoutsonstart = models.IntegerField(db_column='bClearOwningSideVIPTakeoutsOnStart', blank=True, null=True)  # Field name made lowercase.
    bcleartakeoutsonstart = models.IntegerField(db_column='bClearTakeoutsOnStart', blank=True, null=True)  # Field name made lowercase.
    bcompletesconcurrentpair = models.IntegerField(db_column='bCompletesConcurrentPair', blank=True, null=True)  # Field name made lowercase.
    bdisabletakeouts = models.IntegerField(db_column='bDisableTakeouts', blank=True, null=True)  # Field name made lowercase.
    bdrawontimeout = models.IntegerField(db_column='bDrawOnTimeOut', blank=True, null=True)  # Field name made lowercase.
    benabledpvp = models.IntegerField(db_column='bEnabledPvP', blank=True, null=True)  # Field name made lowercase.
    benableopposingsideviptakeouts = models.IntegerField(db_column='bEnableOpposingSideVIPTakeouts', blank=True, null=True)  # Field name made lowercase.
    benableowningsideviptakeouts = models.IntegerField(db_column='bEnableOwningSideVIPTakeouts', blank=True, null=True)  # Field name made lowercase.
    bendonlyontimeout = models.IntegerField(db_column='bEndOnlyOnTimeOut', blank=True, null=True)  # Field name made lowercase.
    bisconcurrent = models.IntegerField(db_column='bIsConcurrent', blank=True, null=True)  # Field name made lowercase.
    bisopposition = models.IntegerField(db_column='bIsOpposition', blank=True, null=True)  # Field name made lowercase.
    bleaveremainingtaskitems = models.IntegerField(db_column='bLeaveRemainingTaskItems', blank=True, null=True)  # Field name made lowercase.
    bopenworldcashpoolitem = models.IntegerField(db_column='bOpenWorldCashPoolItem', blank=True, null=True)  # Field name made lowercase.
    boppositionwinontargetdestroyedbyowners = models.IntegerField(db_column='bOppositionWinOnTargetDestroyedByOwners', blank=True, null=True)  # Field name made lowercase.
    bownerswinontargetdestroyedbyopponent = models.IntegerField(db_column='bOwnersWinOnTargetDestroyedByOpponent', blank=True, null=True)  # Field name made lowercase.
    bscorepointonwin = models.IntegerField(db_column='bScorePointOnWin', blank=True, null=True)  # Field name made lowercase.
    bspawnininventory = models.IntegerField(db_column='bSpawnInInventory', blank=True, null=True)  # Field name made lowercase.
    bwinoncompletion = models.IntegerField(db_column='bWinOnCompletion', blank=True, null=True)  # Field name made lowercase.
    bwinonunopposedcompletion = models.IntegerField(db_column='bWinOnUnopposedCompletion', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskObjectives'


class Taskoperationarmedguard(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    funused = models.FloatField(db_column='fUnused', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationArmedGuard'


class Taskoperationbusts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    nhealthpool = models.IntegerField(db_column='nHealthPool', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationBusts'


class Taskoperationcsis(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    fcsaduration = models.FloatField(db_column='fCSADuration', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationCSIs'


class Taskoperationcategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ereticulehint = models.IntegerField(db_column='eReticuleHint', blank=True, null=True)  # Field name made lowercase.
    fmintakeoutmultiplier = models.FloatField(db_column='fMinTakeoutMultiplier', blank=True, null=True)  # Field name made lowercase.
    etaskoperationcategory = models.IntegerField(db_column='eTaskOperationCategory', blank=True, null=True)  # Field name made lowercase.
    bautoinstigateopposition = models.IntegerField(db_column='bAutoInstigateOpposition', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationCategories'


class Taskoperationdeathmatches(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    npadding = models.IntegerField(db_column='nPadding', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationDeathmatches'


class Taskoperationescape(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    farrestedpenaltyseconds = models.FloatField(db_column='fArrestedPenaltySeconds', blank=True, null=True)  # Field name made lowercase.
    farrestopponentpenaltyseconds = models.FloatField(db_column='fArrestOpponentPenaltySeconds', blank=True, null=True)  # Field name made lowercase.
    fescapebarlimit = models.FloatField(db_column='fEscapeBarLimit', blank=True, null=True)  # Field name made lowercase.
    fkilledpenaltyseconds = models.FloatField(db_column='fKilledPenaltySeconds', blank=True, null=True)  # Field name made lowercase.
    fkillopponentpenaltyseconds = models.FloatField(db_column='fKillOpponentPenaltySeconds', blank=True, null=True)  # Field name made lowercase.
    ftakedamagepenaltyseconds = models.FloatField(db_column='fTakeDamagePenaltySeconds', blank=True, null=True)  # Field name made lowercase.
    fweaponfirepenaltyseconds = models.FloatField(db_column='fWeaponFirePenaltySeconds', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationEscape'


class Taskoperationescort(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    ftriggertime = models.FloatField(db_column='fTriggerTime', blank=True, null=True)  # Field name made lowercase.
    bvipopponentcancapture = models.IntegerField(db_column='bVIPOpponentCanCapture', blank=True, null=True)  # Field name made lowercase.
    bwinontimeout = models.IntegerField(db_column='bWinOnTimeout', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationEscort'


class Taskoperationhacking(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    fcsaduration = models.FloatField(db_column='fCSADuration', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationHacking'


class Taskoperationmovingtarget(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    npadding = models.IntegerField(db_column='nPadding', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationMovingTarget'


class Taskoperationpickups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    npadding = models.IntegerField(db_column='nPadding', blank=True, null=True)  # Field name made lowercase.
    bisvehicledeliverable = models.IntegerField(db_column='bIsVehicleDeliverable', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationPickups'


class Taskoperationsabotages(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    fcsaduration = models.FloatField(db_column='fCSADuration', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationSabotages'


class Taskoperationsurvival(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    npadding = models.IntegerField(db_column='nPadding', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationSurvival'


class Taskoperationterritorycontrols(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    fcapturetime = models.FloatField(db_column='fCaptureTime', blank=True, null=True)  # Field name made lowercase.
    fresettime = models.FloatField(db_column='fResetTime', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationTerritoryControls'


class Taskoperationuiprofile(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    scriminalbrief = models.TextField(db_column='sCriminalBrief', blank=True, null=True)  # Field name made lowercase.
    senforcerbrief = models.TextField(db_column='sEnforcerBrief', blank=True, null=True)  # Field name made lowercase.
    sshortbrief = models.TextField(db_column='sShortBrief', blank=True, null=True)  # Field name made lowercase.
    strackedvaluedescription_0 = models.TextField(db_column='sTrackedValueDescription_0', blank=True, null=True)  # Field name made lowercase.
    strackedvaluedescription_1 = models.TextField(db_column='sTrackedValueDescription_1', blank=True, null=True)  # Field name made lowercase.
    strackedvaluedescription_2 = models.TextField(db_column='sTrackedValueDescription_2', blank=True, null=True)  # Field name made lowercase.
    strackedvaluedescription_3 = models.TextField(db_column='sTrackedValueDescription_3', blank=True, null=True)  # Field name made lowercase.
    strackedvalueimage_0 = models.TextField(db_column='sTrackedValueImage_0', blank=True, null=True)  # Field name made lowercase.
    strackedvalueimage_1 = models.TextField(db_column='sTrackedValueImage_1', blank=True, null=True)  # Field name made lowercase.
    strackedvalueimage_2 = models.TextField(db_column='sTrackedValueImage_2', blank=True, null=True)  # Field name made lowercase.
    strackedvalueimage_3 = models.TextField(db_column='sTrackedValueImage_3', blank=True, null=True)  # Field name made lowercase.
    etaskoperationuiprofile = models.IntegerField(db_column='eTaskOperationUIProfile', blank=True, null=True)  # Field name made lowercase.
    etrackedstateprofile_0 = models.IntegerField(db_column='eTrackedStateProfile_0', blank=True, null=True)  # Field name made lowercase.
    etrackedstateprofile_1 = models.IntegerField(db_column='eTrackedStateProfile_1', blank=True, null=True)  # Field name made lowercase.
    etrackedstateprofile_2 = models.IntegerField(db_column='eTrackedStateProfile_2', blank=True, null=True)  # Field name made lowercase.
    etrackedstateprofile_3 = models.IntegerField(db_column='eTrackedStateProfile_3', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluebarfgdisabled_0 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_0', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluebarfgdisabled_1 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_1', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluebarfgdisabled_2 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_2', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluebarfgdisabled_3 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_3', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluebg_0 = models.IntegerField(db_column='eTrackedValueBg_0', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluebg_1 = models.IntegerField(db_column='eTrackedValueBg_1', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluebg_2 = models.IntegerField(db_column='eTrackedValueBg_2', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluebg_3 = models.IntegerField(db_column='eTrackedValueBg_3', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluefg_0 = models.IntegerField(db_column='eTrackedValueFg_0', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluefg_1 = models.IntegerField(db_column='eTrackedValueFg_1', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluefg_2 = models.IntegerField(db_column='eTrackedValueFg_2', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluefg_3 = models.IntegerField(db_column='eTrackedValueFg_3', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluesocket_0 = models.IntegerField(db_column='eTrackedValueSocket_0', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluesocket_1 = models.IntegerField(db_column='eTrackedValueSocket_1', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluesocket_2 = models.IntegerField(db_column='eTrackedValueSocket_2', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluesocket_3 = models.IntegerField(db_column='eTrackedValueSocket_3', blank=True, null=True)  # Field name made lowercase.
    ntrackedvaluestageoffset_0 = models.IntegerField(db_column='nTrackedValueStageOffset_0', blank=True, null=True)  # Field name made lowercase.
    ntrackedvaluestageoffset_1 = models.IntegerField(db_column='nTrackedValueStageOffset_1', blank=True, null=True)  # Field name made lowercase.
    ntrackedvaluestageoffset_2 = models.IntegerField(db_column='nTrackedValueStageOffset_2', blank=True, null=True)  # Field name made lowercase.
    ntrackedvaluestageoffset_3 = models.IntegerField(db_column='nTrackedValueStageOffset_3', blank=True, null=True)  # Field name made lowercase.
    etrackedvalue_0 = models.IntegerField(db_column='eTrackedValue_0', blank=True, null=True)  # Field name made lowercase.
    etrackedvalue_1 = models.IntegerField(db_column='eTrackedValue_1', blank=True, null=True)  # Field name made lowercase.
    etrackedvalue_2 = models.IntegerField(db_column='eTrackedValue_2', blank=True, null=True)  # Field name made lowercase.
    etrackedvalue_3 = models.IntegerField(db_column='eTrackedValue_3', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluedisplay_0 = models.IntegerField(db_column='eTrackedValueDisplay_0', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluedisplay_1 = models.IntegerField(db_column='eTrackedValueDisplay_1', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluedisplay_2 = models.IntegerField(db_column='eTrackedValueDisplay_2', blank=True, null=True)  # Field name made lowercase.
    etrackedvaluedisplay_3 = models.IntegerField(db_column='eTrackedValueDisplay_3', blank=True, null=True)  # Field name made lowercase.
    bflashwhenchanged_0 = models.IntegerField(db_column='bFlashWhenChanged_0', blank=True, null=True)  # Field name made lowercase.
    bflashwhenchanged_1 = models.IntegerField(db_column='bFlashWhenChanged_1', blank=True, null=True)  # Field name made lowercase.
    bflashwhenchanged_2 = models.IntegerField(db_column='bFlashWhenChanged_2', blank=True, null=True)  # Field name made lowercase.
    bflashwhenchanged_3 = models.IntegerField(db_column='bFlashWhenChanged_3', blank=True, null=True)  # Field name made lowercase.
    bhideatmax_0 = models.IntegerField(db_column='bHideAtMax_0', blank=True, null=True)  # Field name made lowercase.
    bhideatmax_1 = models.IntegerField(db_column='bHideAtMax_1', blank=True, null=True)  # Field name made lowercase.
    bhideatmax_2 = models.IntegerField(db_column='bHideAtMax_2', blank=True, null=True)  # Field name made lowercase.
    bhideatmax_3 = models.IntegerField(db_column='bHideAtMax_3', blank=True, null=True)  # Field name made lowercase.
    bhidenamewhendisabled_0 = models.IntegerField(db_column='bHideNameWhenDisabled_0', blank=True, null=True)  # Field name made lowercase.
    bhidenamewhendisabled_1 = models.IntegerField(db_column='bHideNameWhenDisabled_1', blank=True, null=True)  # Field name made lowercase.
    bhidenamewhendisabled_2 = models.IntegerField(db_column='bHideNameWhenDisabled_2', blank=True, null=True)  # Field name made lowercase.
    bhidenamewhendisabled_3 = models.IntegerField(db_column='bHideNameWhenDisabled_3', blank=True, null=True)  # Field name made lowercase.
    bhidewhenone_0 = models.IntegerField(db_column='bHideWhenOne_0', blank=True, null=True)  # Field name made lowercase.
    bhidewhenone_1 = models.IntegerField(db_column='bHideWhenOne_1', blank=True, null=True)  # Field name made lowercase.
    bhidewhenone_2 = models.IntegerField(db_column='bHideWhenOne_2', blank=True, null=True)  # Field name made lowercase.
    bhidewhenone_3 = models.IntegerField(db_column='bHideWhenOne_3', blank=True, null=True)  # Field name made lowercase.
    bhidewhenoppositionviptakeoutsdisabled_0 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_0', blank=True, null=True)  # Field name made lowercase.
    bhidewhenoppositionviptakeoutsdisabled_1 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_1', blank=True, null=True)  # Field name made lowercase.
    bhidewhenoppositionviptakeoutsdisabled_2 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_2', blank=True, null=True)  # Field name made lowercase.
    bhidewhenoppositionviptakeoutsdisabled_3 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_3', blank=True, null=True)  # Field name made lowercase.
    bhidewhenownerviptakeoutsdisabled_0 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_0', blank=True, null=True)  # Field name made lowercase.
    bhidewhenownerviptakeoutsdisabled_1 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_1', blank=True, null=True)  # Field name made lowercase.
    bhidewhenownerviptakeoutsdisabled_2 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_2', blank=True, null=True)  # Field name made lowercase.
    bhidewhenownerviptakeoutsdisabled_3 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_3', blank=True, null=True)  # Field name made lowercase.
    bhidewhenpointsdisabled_0 = models.IntegerField(db_column='bHideWhenPointsDisabled_0', blank=True, null=True)  # Field name made lowercase.
    bhidewhenpointsdisabled_1 = models.IntegerField(db_column='bHideWhenPointsDisabled_1', blank=True, null=True)  # Field name made lowercase.
    bhidewhenpointsdisabled_2 = models.IntegerField(db_column='bHideWhenPointsDisabled_2', blank=True, null=True)  # Field name made lowercase.
    bhidewhenpointsdisabled_3 = models.IntegerField(db_column='bHideWhenPointsDisabled_3', blank=True, null=True)  # Field name made lowercase.
    bhidewhentakeoutsdisabled_0 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_0', blank=True, null=True)  # Field name made lowercase.
    bhidewhentakeoutsdisabled_1 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_1', blank=True, null=True)  # Field name made lowercase.
    bhidewhentakeoutsdisabled_2 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_2', blank=True, null=True)  # Field name made lowercase.
    bhidewhentakeoutsdisabled_3 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_3', blank=True, null=True)  # Field name made lowercase.
    bhidewhenunopposed_0 = models.IntegerField(db_column='bHideWhenUnopposed_0', blank=True, null=True)  # Field name made lowercase.
    bhidewhenunopposed_1 = models.IntegerField(db_column='bHideWhenUnopposed_1', blank=True, null=True)  # Field name made lowercase.
    bhidewhenunopposed_2 = models.IntegerField(db_column='bHideWhenUnopposed_2', blank=True, null=True)  # Field name made lowercase.
    bhidewhenunopposed_3 = models.IntegerField(db_column='bHideWhenUnopposed_3', blank=True, null=True)  # Field name made lowercase.
    btrackedvalueinoverview_0 = models.IntegerField(db_column='bTrackedValueInOverview_0', blank=True, null=True)  # Field name made lowercase.
    btrackedvalueinoverview_1 = models.IntegerField(db_column='bTrackedValueInOverview_1', blank=True, null=True)  # Field name made lowercase.
    btrackedvalueinoverview_2 = models.IntegerField(db_column='bTrackedValueInOverview_2', blank=True, null=True)  # Field name made lowercase.
    btrackedvalueinoverview_3 = models.IntegerField(db_column='bTrackedValueInOverview_3', blank=True, null=True)  # Field name made lowercase.
    btrackedvalueonhud_0 = models.IntegerField(db_column='bTrackedValueOnHUD_0', blank=True, null=True)  # Field name made lowercase.
    btrackedvalueonhud_1 = models.IntegerField(db_column='bTrackedValueOnHUD_1', blank=True, null=True)  # Field name made lowercase.
    btrackedvalueonhud_2 = models.IntegerField(db_column='bTrackedValueOnHUD_2', blank=True, null=True)  # Field name made lowercase.
    btrackedvalueonhud_3 = models.IntegerField(db_column='bTrackedValueOnHUD_3', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationUIProfile'


class Taskoperationvehiclecargos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    fcsaduration = models.FloatField(db_column='fCSADuration', blank=True, null=True)  # Field name made lowercase.
    bisvehicledeliverable = models.IntegerField(db_column='bIsVehicleDeliverable', blank=True, null=True)  # Field name made lowercase.
    bvehiclelocked = models.IntegerField(db_column='bVehicleLocked', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationVehicleCargos'


class Taskoperations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    scriminalbrief = models.TextField(db_column='sCriminalBrief', blank=True, null=True)  # Field name made lowercase.
    senforcerbrief = models.TextField(db_column='sEnforcerBrief', blank=True, null=True)  # Field name made lowercase.
    suidescription = models.TextField(db_column='sUIDescription', blank=True, null=True)  # Field name made lowercase.
    emissionuiprofile = models.IntegerField(db_column='eMissionUIProfile', blank=True, null=True)  # Field name made lowercase.
    emissionuiprofileopposition = models.IntegerField(db_column='eMissionUIProfileOpposition', blank=True, null=True)  # Field name made lowercase.
    eoppositiontargethudmarker = models.IntegerField(db_column='eOppositionTargetHUDMarker', blank=True, null=True)  # Field name made lowercase.
    eoutofmissiontargethudmarker = models.IntegerField(db_column='eOutOfMissionTargetHUDMarker', blank=True, null=True)  # Field name made lowercase.
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    etasktargethudmarker = models.IntegerField(db_column='eTaskTargetHUDMarker', blank=True, null=True)  # Field name made lowercase.
    nobjectiveholdpointstarget = models.IntegerField(db_column='nObjectiveHoldPointsTarget', blank=True, null=True)  # Field name made lowercase.
    enpcworldevent = models.IntegerField(db_column='eNPCWorldEvent', blank=True, null=True)  # Field name made lowercase.
    eoppositionitemvisibility = models.IntegerField(db_column='eOppositionItemVisibility', blank=True, null=True)  # Field name made lowercase.
    eoutofmissionitemvisibility = models.IntegerField(db_column='eOutOfMissionItemVisibility', blank=True, null=True)  # Field name made lowercase.
    eowneritemvisibility = models.IntegerField(db_column='eOwnerItemVisibility', blank=True, null=True)  # Field name made lowercase.
    etaskoperationcategory = models.IntegerField(db_column='eTaskOperationCategory', blank=True, null=True)  # Field name made lowercase.
    etasktargetclass = models.IntegerField(db_column='eTaskTargetClass', blank=True, null=True)  # Field name made lowercase.
    banysidecaninitiate = models.IntegerField(db_column='bAnySideCanInitiate', blank=True, null=True)  # Field name made lowercase.
    bhidealldeliverablesfromopposition = models.IntegerField(db_column='bHideAllDeliverablesFromOpposition', blank=True, null=True)  # Field name made lowercase.
    bhidealldeliverablesfromowners = models.IntegerField(db_column='bHideAllDeliverablesFromOwners', blank=True, null=True)  # Field name made lowercase.
    boppositioncancarrytaskitems = models.IntegerField(db_column='bOppositionCanCarryTaskItems', blank=True, null=True)  # Field name made lowercase.
    boppositioncaninteractwithvehicles = models.IntegerField(db_column='bOppositionCanInteractWithVehicles', blank=True, null=True)  # Field name made lowercase.
    boutofmissioncaninteract = models.IntegerField(db_column='bOutOfMissionCanInteract', blank=True, null=True)  # Field name made lowercase.
    bownerscancarrytaskitems = models.IntegerField(db_column='bOwnersCanCarryTaskItems', blank=True, null=True)  # Field name made lowercase.
    bownerscaninteractwithvehicles = models.IntegerField(db_column='bOwnersCanInteractWithVehicles', blank=True, null=True)  # Field name made lowercase.
    bshowoppositiontotaskgroup = models.IntegerField(db_column='bShowOppositionToTaskGroup', blank=True, null=True)  # Field name made lowercase.
    bshowtaskgrouptoopposition = models.IntegerField(db_column='bShowTaskGroupToOpposition', blank=True, null=True)  # Field name made lowercase.
    buseobjectiveholdpoints = models.IntegerField(db_column='bUseObjectiveHoldPoints', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperations'


class Taskoperationsarson(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    fcsaduration = models.FloatField(db_column='fCSADuration', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationsArson'


class Taskoperationsbombing(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ebomblevel = models.IntegerField(db_column='eBombLevel', blank=True, null=True)  # Field name made lowercase.
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    fbombdisposalguardtime = models.FloatField(db_column='fBombDisposalGuardTime', blank=True, null=True)  # Field name made lowercase.
    fcsaduration = models.FloatField(db_column='fCSADuration', blank=True, null=True)  # Field name made lowercase.
    ffusetimer = models.FloatField(db_column='fFuseTimer', blank=True, null=True)  # Field name made lowercase.
    bisbombdefusable = models.IntegerField(db_column='bIsBombDefusable', blank=True, null=True)  # Field name made lowercase.
    bisbombrearmable = models.IntegerField(db_column='bIsBombRearmable', blank=True, null=True)  # Field name made lowercase.
    btriggeronallbombsdefused = models.IntegerField(db_column='bTriggerOnAllBombsDefused', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationsBombing'


class Taskoperationsbuildingbreakin(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    suseactionname = models.TextField(db_column='sUseActionName', blank=True, null=True)  # Field name made lowercase.
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    fcsaduration = models.FloatField(db_column='fCSADuration', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationsBuildingBreakIn'


class Taskoperationsgraffiti(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    nsprayduration = models.IntegerField(db_column='nSprayDuration', blank=True, null=True)  # Field name made lowercase.
    bisresprayable = models.IntegerField(db_column='bIsResprayable', blank=True, null=True)  # Field name made lowercase.
    bstartsneutral = models.IntegerField(db_column='bStartsNeutral', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationsGraffiti'


class Taskoperationsitemdelivery(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    ftriggertime = models.FloatField(db_column='fTriggerTime', blank=True, null=True)  # Field name made lowercase.
    bdelivertoalltargets = models.IntegerField(db_column='bDeliverToAllTargets', blank=True, null=True)  # Field name made lowercase.
    bdelivervehicle = models.IntegerField(db_column='bDeliverVehicle', blank=True, null=True)  # Field name made lowercase.
    bdelivervehiclecargo = models.IntegerField(db_column='bDeliverVehicleCargo', blank=True, null=True)  # Field name made lowercase.
    bremovedeliverables = models.IntegerField(db_column='bRemoveDeliverables', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationsItemDelivery'


class Taskoperationsnpc(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    fcsaduration = models.FloatField(db_column='fCSADuration', blank=True, null=True)  # Field name made lowercase.
    ecsastate = models.IntegerField(db_column='eCSAState', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationsNPC'


class Taskoperationsramraid(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    nhealthpool = models.IntegerField(db_column='nHealthPool', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationsRamRaid'


class Taskoperationsrendezvous(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    ftriggertime = models.FloatField(db_column='fTriggerTime', blank=True, null=True)  # Field name made lowercase.
    ballsidemembers = models.IntegerField(db_column='bAllSideMembers', blank=True, null=True)  # Field name made lowercase.
    ballsimultaneously = models.IntegerField(db_column='bAllSimultaneously', blank=True, null=True)  # Field name made lowercase.
    biscoopcheckpoint = models.IntegerField(db_column='bIsCoopCheckpoint', blank=True, null=True)  # Field name made lowercase.
    bvehiclerequired = models.IntegerField(db_column='bVehicleRequired', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationsRendezvous'


class Taskoperationsvandalism(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    nhealthpool = models.IntegerField(db_column='nHealthPool', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationsVandalism'


class Taskoperationsvehiclelooting(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    fcsaduration = models.FloatField(db_column='fCSADuration', blank=True, null=True)  # Field name made lowercase.
    bisvehicledeliverable = models.IntegerField(db_column='bIsVehicleDeliverable', blank=True, null=True)  # Field name made lowercase.
    bvehiclelocked = models.IntegerField(db_column='bVehicleLocked', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationsVehicleLooting'


class Taskoperationsvehicletheft(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)  # Field name made lowercase.
    fcsaduration = models.FloatField(db_column='fCSADuration', blank=True, null=True)  # Field name made lowercase.
    npointlessextrapadding = models.IntegerField(db_column='nPointlessExtraPadding', blank=True, null=True)  # Field name made lowercase.
    bisvehicledeliverable = models.IntegerField(db_column='bIsVehicleDeliverable', blank=True, null=True)  # Field name made lowercase.
    bvehiclelocked = models.IntegerField(db_column='bVehicleLocked', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskOperationsVehicleTheft'


class Tasktargetallocations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    elocationconstraint = models.IntegerField(db_column='eLocationConstraint', blank=True, null=True)  # Field name made lowercase.
    emissiontemplate = models.IntegerField(db_column='eMissionTemplate', blank=True, null=True)  # Field name made lowercase.
    etasktargetallocation = models.IntegerField(db_column='eTaskTargetAllocation', blank=True, null=True)  # Field name made lowercase.
    etasktargettype = models.IntegerField(db_column='eTaskTargetType', blank=True, null=True)  # Field name made lowercase.
    etheme_0 = models.IntegerField(db_column='eTheme_0', blank=True, null=True)  # Field name made lowercase.
    etheme_1 = models.IntegerField(db_column='eTheme_1', blank=True, null=True)  # Field name made lowercase.
    etheme_2 = models.IntegerField(db_column='eTheme_2', blank=True, null=True)  # Field name made lowercase.
    etheme_3 = models.IntegerField(db_column='eTheme_3', blank=True, null=True)  # Field name made lowercase.
    evehiclecategory = models.IntegerField(db_column='eVehicleCategory', blank=True, null=True)  # Field name made lowercase.
    flocationdistancemax = models.FloatField(db_column='fLocationDistanceMax', blank=True, null=True)  # Field name made lowercase.
    flocationdistancemin = models.FloatField(db_column='fLocationDistanceMin', blank=True, null=True)  # Field name made lowercase.
    nmaxtargetsperblock = models.IntegerField(db_column='nMaxTargetsPerBlock', blank=True, null=True)  # Field name made lowercase.
    ntargetcount = models.IntegerField(db_column='nTargetCount', blank=True, null=True)  # Field name made lowercase.
    etasktargetspecificationmethod = models.IntegerField(db_column='eTaskTargetSpecificationMethod', blank=True, null=True)  # Field name made lowercase.
    ballowdifferentblock = models.IntegerField(db_column='bAllowDifferentBlock', blank=True, null=True)  # Field name made lowercase.
    ballowsameblock = models.IntegerField(db_column='bAllowSameBlock', blank=True, null=True)  # Field name made lowercase.
    buniqueblock = models.IntegerField(db_column='bUniqueBlock', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskTargetAllocations'


class Tasktargetcheckpoints(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etasktargettype = models.IntegerField(db_column='eTaskTargetType', blank=True, null=True)  # Field name made lowercase.
    nmaxplayerspaces = models.IntegerField(db_column='nMaxPlayerSpaces', blank=True, null=True)  # Field name made lowercase.
    nmaxvehiclespaces = models.IntegerField(db_column='nMaxVehicleSpaces', blank=True, null=True)  # Field name made lowercase.
    ballowdropoffs = models.IntegerField(db_column='bAllowDropOffs', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskTargetCheckpoints'


class Tasktargetclasses(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etasktargetclass = models.IntegerField(db_column='eTaskTargetClass', blank=True, null=True)  # Field name made lowercase.
    bcanbeusedindirectedmissions = models.IntegerField(db_column='bCanBeUsedInDirectedMissions', blank=True, null=True)  # Field name made lowercase.
    blivingcity = models.IntegerField(db_column='bLivingCity', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskTargetClasses'


class Tasktargetgraffiti(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etasktargettype = models.IntegerField(db_column='eTaskTargetType', blank=True, null=True)  # Field name made lowercase.
    ndummy = models.IntegerField(db_column='nDummy', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskTargetGraffiti'


class Tasktargetnpcs(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    enpctype = models.IntegerField(db_column='eNPCType', blank=True, null=True)  # Field name made lowercase.
    etasktargettype = models.IntegerField(db_column='eTaskTargetType', blank=True, null=True)  # Field name made lowercase.
    ntemplctype = models.IntegerField(db_column='nTempLCType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskTargetNPCs'


class Tasktargetprops(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    spropassetname = models.TextField(db_column='sPropAssetName', blank=True, null=True)  # Field name made lowercase.
    epropcategory = models.IntegerField(db_column='ePropCategory', blank=True, null=True)  # Field name made lowercase.
    etasktargettype = models.IntegerField(db_column='eTaskTargetType', blank=True, null=True)  # Field name made lowercase.
    farsondamagedelayseconds = models.FloatField(db_column='fArsonDamageDelaySeconds', blank=True, null=True)  # Field name made lowercase.
    barson = models.IntegerField(db_column='bArson', blank=True, null=True)  # Field name made lowercase.
    bbombdisposal = models.IntegerField(db_column='bBombDisposal', blank=True, null=True)  # Field name made lowercase.
    bbombing = models.IntegerField(db_column='bBombing', blank=True, null=True)  # Field name made lowercase.
    bburglary = models.IntegerField(db_column='bBurglary', blank=True, null=True)  # Field name made lowercase.
    bbust = models.IntegerField(db_column='bBust', blank=True, null=True)  # Field name made lowercase.
    bcsi = models.IntegerField(db_column='bCSI', blank=True, null=True)  # Field name made lowercase.
    bforcedentry = models.IntegerField(db_column='bForcedEntry', blank=True, null=True)  # Field name made lowercase.
    bhacking = models.IntegerField(db_column='bHacking', blank=True, null=True)  # Field name made lowercase.
    bisbuildingfeature = models.IntegerField(db_column='bIsBuildingFeature', blank=True, null=True)  # Field name made lowercase.
    bramraid = models.IntegerField(db_column='bRamRaid', blank=True, null=True)  # Field name made lowercase.
    bsabotage = models.IntegerField(db_column='bSabotage', blank=True, null=True)  # Field name made lowercase.
    bvandalism = models.IntegerField(db_column='bVandalism', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskTargetProps'


class Tasktargettypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    egameplayobject = models.IntegerField(db_column='eGameplayObject', blank=True, null=True)  # Field name made lowercase.
    ehudmarkeroffsetoverride = models.IntegerField(db_column='eHUDMarkerOffsetOverride', blank=True, null=True)  # Field name made lowercase.
    eopenworldtargetactivity = models.IntegerField(db_column='eOpenWorldTargetActivity', blank=True, null=True)  # Field name made lowercase.
    eowaitemspawnrule = models.IntegerField(db_column='eOWAItemSpawnRule', blank=True, null=True)  # Field name made lowercase.
    etasktargettype = models.IntegerField(db_column='eTaskTargetType', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    etasktargetclass = models.IntegerField(db_column='eTaskTargetClass', blank=True, null=True)  # Field name made lowercase.
    etimeofdayavailability = models.IntegerField(db_column='eTimeOfDayAvailability', blank=True, null=True)  # Field name made lowercase.
    ballowsimultaneousallocations = models.IntegerField(db_column='bAllowSimultaneousAllocations', blank=True, null=True)  # Field name made lowercase.
    bopenworldonly = models.IntegerField(db_column='bOpenWorldOnly', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskTargetTypes'


class Themeitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sresource = models.TextField(db_column='sResource', blank=True, null=True)  # Field name made lowercase.
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ThemeItemTypes'


class Threatlevels(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    salloweddistrictthreats = models.TextField(db_column='sAllowedDistrictThreats', blank=True, null=True)  # Field name made lowercase.
    sdisplayedname = models.TextField(db_column='sDisplayedName', blank=True, null=True)  # Field name made lowercase.
    ehudtextureicon = models.IntegerField(db_column='eHUDTextureIcon', blank=True, null=True)  # Field name made lowercase.
    ethreatlevel = models.IntegerField(db_column='eThreatLevel', blank=True, null=True)  # Field name made lowercase.
    fmedianthreat = models.FloatField(db_column='fMedianThreat', blank=True, null=True)  # Field name made lowercase.
    fthreshold = models.FloatField(db_column='fThreshold', blank=True, null=True)  # Field name made lowercase.
    nratingtexturearrayindex = models.IntegerField(db_column='nRatingTextureArrayIndex', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ThreatLevels'


class Timeofdayavailabilities(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etimeofdayavailability = models.IntegerField(db_column='eTimeOfDayAvailability', blank=True, null=True)  # Field name made lowercase.
    bafternoon = models.IntegerField(db_column='bAfternoon', blank=True, null=True)  # Field name made lowercase.
    bevening = models.IntegerField(db_column='bEvening', blank=True, null=True)  # Field name made lowercase.
    bmorning = models.IntegerField(db_column='bMorning', blank=True, null=True)  # Field name made lowercase.
    bnight = models.IntegerField(db_column='bNight', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TimeOfDayAvailabilities'


class Timeofdayperiod(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nendtimehours = models.IntegerField(db_column='nEndTimeHours', blank=True, null=True)  # Field name made lowercase.
    nendtimemins = models.IntegerField(db_column='nEndTimeMins', blank=True, null=True)  # Field name made lowercase.
    nstarttimehours = models.IntegerField(db_column='nStartTimeHours', blank=True, null=True)  # Field name made lowercase.
    nstarttimemins = models.IntegerField(db_column='nStartTimeMins', blank=True, null=True)  # Field name made lowercase.
    etimeofdayperiod = models.IntegerField(db_column='eTimeofDayPeriod', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TimeofDayPeriod'


class Titleunlockitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    bfemale = models.IntegerField(db_column='bFemale', blank=True, null=True)  # Field name made lowercase.
    bhideuntilunlocked = models.IntegerField(db_column='bHideUntilUnlocked', blank=True, null=True)  # Field name made lowercase.
    bmale = models.IntegerField(db_column='bMale', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TitleUnlockItemTypes'


class Trackedactivities(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etrackedactivity = models.IntegerField(db_column='eTrackedActivity', blank=True, null=True)  # Field name made lowercase.
    eunit = models.IntegerField(db_column='eUnit', blank=True, null=True)  # Field name made lowercase.
    nmaxincrementperzone = models.IntegerField(db_column='nMaxIncrementPerZone', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)  # Field name made lowercase.
    epersistencetype = models.IntegerField(db_column='ePersistenceType', blank=True, null=True)  # Field name made lowercase.
    bupdateduringwitnessingmission = models.IntegerField(db_column='bUpdateDuringWitnessingMission', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TrackedActivities'


class Trackedactivitiesderived(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    emaster_0 = models.IntegerField(db_column='eMaster_0', blank=True, null=True)  # Field name made lowercase.
    emaster_1 = models.IntegerField(db_column='eMaster_1', blank=True, null=True)  # Field name made lowercase.
    emaster_2 = models.IntegerField(db_column='eMaster_2', blank=True, null=True)  # Field name made lowercase.
    emaster_3 = models.IntegerField(db_column='eMaster_3', blank=True, null=True)  # Field name made lowercase.
    emaster_4 = models.IntegerField(db_column='eMaster_4', blank=True, null=True)  # Field name made lowercase.
    emaster_5 = models.IntegerField(db_column='eMaster_5', blank=True, null=True)  # Field name made lowercase.
    emaster_6 = models.IntegerField(db_column='eMaster_6', blank=True, null=True)  # Field name made lowercase.
    emaster_7 = models.IntegerField(db_column='eMaster_7', blank=True, null=True)  # Field name made lowercase.
    emaster_8 = models.IntegerField(db_column='eMaster_8', blank=True, null=True)  # Field name made lowercase.
    emaster_9 = models.IntegerField(db_column='eMaster_9', blank=True, null=True)  # Field name made lowercase.
    etrackedactivity = models.IntegerField(db_column='eTrackedActivity', blank=True, null=True)  # Field name made lowercase.
    eoperation = models.IntegerField(db_column='eOperation', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TrackedActivitiesDerived'


class Trackedactivitiesfixed(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etrackedactivity = models.IntegerField(db_column='eTrackedActivity', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TrackedActivitiesFixed'


class Trackedactivityunits(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sformatting = models.TextField(db_column='sFormatting', blank=True, null=True)  # Field name made lowercase.
    etrackedactivityunit = models.IntegerField(db_column='eTrackedActivityUnit', blank=True, null=True)  # Field name made lowercase.
    econversion = models.IntegerField(db_column='eConversion', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TrackedActivityUnits'


class Trafficlightdurations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    edistrict = models.IntegerField(db_column='eDistrict', blank=True, null=True)  # Field name made lowercase.
    etrafficlightduration = models.IntegerField(db_column='eTrafficLightDuration', blank=True, null=True)  # Field name made lowercase.
    fped_fourlanemax = models.FloatField(db_column='fPed_FourLaneMax', blank=True, null=True)  # Field name made lowercase.
    fped_fourlanemin = models.FloatField(db_column='fPed_FourLaneMin', blank=True, null=True)  # Field name made lowercase.
    fped_onelanemax = models.FloatField(db_column='fPed_OneLaneMax', blank=True, null=True)  # Field name made lowercase.
    fped_onelanemin = models.FloatField(db_column='fPed_OneLaneMin', blank=True, null=True)  # Field name made lowercase.
    fped_threelanemax = models.FloatField(db_column='fPed_ThreeLaneMax', blank=True, null=True)  # Field name made lowercase.
    fped_threelanemin = models.FloatField(db_column='fPed_ThreeLaneMin', blank=True, null=True)  # Field name made lowercase.
    fped_twolanemax = models.FloatField(db_column='fPed_TwoLaneMax', blank=True, null=True)  # Field name made lowercase.
    fped_twolanemin = models.FloatField(db_column='fPed_TwoLaneMin', blank=True, null=True)  # Field name made lowercase.
    fvehicle_fourlanemax = models.FloatField(db_column='fVehicle_FourLaneMax', blank=True, null=True)  # Field name made lowercase.
    fvehicle_fourlanemin = models.FloatField(db_column='fVehicle_FourLaneMin', blank=True, null=True)  # Field name made lowercase.
    fvehicle_onelanemax = models.FloatField(db_column='fVehicle_OneLaneMax', blank=True, null=True)  # Field name made lowercase.
    fvehicle_onelanemin = models.FloatField(db_column='fVehicle_OneLaneMin', blank=True, null=True)  # Field name made lowercase.
    fvehicle_threelanemax = models.FloatField(db_column='fVehicle_ThreeLaneMax', blank=True, null=True)  # Field name made lowercase.
    fvehicle_threelanemin = models.FloatField(db_column='fVehicle_ThreeLaneMin', blank=True, null=True)  # Field name made lowercase.
    fvehicle_twolanemax = models.FloatField(db_column='fVehicle_TwoLaneMax', blank=True, null=True)  # Field name made lowercase.
    fvehicle_twolanemin = models.FloatField(db_column='fVehicle_TwoLaneMin', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TrafficLightDurations'


class Tutorialcategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    srewardmailbody = models.TextField(db_column='sRewardMailBody', blank=True, null=True)  # Field name made lowercase.
    srewardmailsubject = models.TextField(db_column='sRewardMailSubject', blank=True, null=True)  # Field name made lowercase.
    erewardpackage = models.IntegerField(db_column='eRewardPackage', blank=True, null=True)  # Field name made lowercase.
    etutorial = models.IntegerField(db_column='eTutorial', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TutorialCategories'


class Tutorialevents(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    shudtext = models.TextField(db_column='sHUDText', blank=True, null=True)  # Field name made lowercase.
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)  # Field name made lowercase.
    ehudmarker = models.IntegerField(db_column='eHUDMarker', blank=True, null=True)  # Field name made lowercase.
    etutorial = models.IntegerField(db_column='eTutorial', blank=True, null=True)  # Field name made lowercase.
    euihighlight = models.IntegerField(db_column='eUIHighlight', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TutorialEvents'


class Tutorials(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sbody = models.TextField(db_column='sBody', blank=True, null=True)  # Field name made lowercase.
    sscreenshot = models.TextField(db_column='sScreenshot', blank=True, null=True)  # Field name made lowercase.
    ssubtitle = models.TextField(db_column='sSubTitle', blank=True, null=True)  # Field name made lowercase.
    stitle = models.TextField(db_column='sTitle', blank=True, null=True)  # Field name made lowercase.
    eparent = models.IntegerField(db_column='eParent', blank=True, null=True)  # Field name made lowercase.
    etutorial = models.IntegerField(db_column='eTutorial', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tutorials'


class Uiinteractionpoints(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sinfobrowsertext = models.TextField(db_column='sInfoBrowserText', blank=True, null=True)  # Field name made lowercase.
    ehudmarker = models.IntegerField(db_column='eHUDMarker', blank=True, null=True)  # Field name made lowercase.
    einfobrowsericon = models.IntegerField(db_column='eInfoBrowserIcon', blank=True, null=True)  # Field name made lowercase.
    euiinteractionpoint = models.IntegerField(db_column='eUIInteractionPoint', blank=True, null=True)  # Field name made lowercase.
    ecsa = models.IntegerField(db_column='eCSA', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UIInteractionPoints'


class Uimeshviewersetup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nuimeshviewersetup = models.TextField(db_column='nUIMeshViewerSetup', blank=True, null=True)  # Field name made lowercase.
    fcamerafov = models.FloatField(db_column='fCameraFOV', blank=True, null=True)  # Field name made lowercase.
    fcameraposx = models.FloatField(db_column='fCameraPosX', blank=True, null=True)  # Field name made lowercase.
    fcameraposy = models.FloatField(db_column='fCameraPosY', blank=True, null=True)  # Field name made lowercase.
    fcameraposz = models.FloatField(db_column='fCameraPosZ', blank=True, null=True)  # Field name made lowercase.
    fmeshcentrex = models.FloatField(db_column='fMeshCentreX', blank=True, null=True)  # Field name made lowercase.
    fmeshcentrey = models.FloatField(db_column='fMeshCentreY', blank=True, null=True)  # Field name made lowercase.
    fmeshcentrez = models.FloatField(db_column='fMeshCentreZ', blank=True, null=True)  # Field name made lowercase.
    fmeshorientationx = models.FloatField(db_column='fMeshOrientationX', blank=True, null=True)  # Field name made lowercase.
    fmeshorientationy = models.FloatField(db_column='fMeshOrientationY', blank=True, null=True)  # Field name made lowercase.
    fmeshorientationz = models.FloatField(db_column='fMeshOrientationZ', blank=True, null=True)  # Field name made lowercase.
    fmeshscale = models.FloatField(db_column='fMeshScale', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UIMeshViewerSetup'


class Uuistyles(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sname = models.TextField(db_column='sName', blank=True, null=True)  # Field name made lowercase.
    euistyle = models.IntegerField(db_column='eUIStyle', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UUIStyles'


class Unlockiteminfracategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)  # Field name made lowercase.
    einventoryiteminfracategory = models.IntegerField(db_column='eInventoryItemInfraCategory', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UnlockItemInfraCategories'


class Unlockitemsubcategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)  # Field name made lowercase.
    einventoryitemsubcategory = models.IntegerField(db_column='eInventoryItemSubCategory', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UnlockItemSubCategories'


class Unlockitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    eunlockitem = models.IntegerField(db_column='eUnlockItem', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UnlockItemTypes'


class Usabletokentypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    emodifieritem = models.IntegerField(db_column='eModifierItem', blank=True, null=True)  # Field name made lowercase.
    ncharges = models.IntegerField(db_column='nCharges', blank=True, null=True)  # Field name made lowercase.
    nmaxcharges = models.IntegerField(db_column='nMaxCharges', blank=True, null=True)  # Field name made lowercase.
    nmaxstacks = models.IntegerField(db_column='nMaxStacks', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsableTokenTypes'


class Vfxassociations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    svfxprefabname = models.TextField(db_column='sVFXPrefabName', blank=True, null=True)  # Field name made lowercase.
    svfxreplacedactor = models.TextField(db_column='sVFXReplacedActor', blank=True, null=True)  # Field name made lowercase.
    evfxassociation = models.IntegerField(db_column='eVFXAssociation', blank=True, null=True)  # Field name made lowercase.
    evfxtype = models.IntegerField(db_column='eVFXType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VFXAssociations'


class Vfxtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    evfxtype = models.IntegerField(db_column='eVFXType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VFXTypes'


class Vehicleaudiopart(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleAudioPart'


class Vehicleaudiopartdefaults(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdamagetype = models.TextField(db_column='sDamageType', blank=True, null=True)  # Field name made lowercase.
    sdooreventclosefront = models.TextField(db_column='sDoorEventCloseFront', blank=True, null=True)  # Field name made lowercase.
    sdooreventcloserearback = models.TextField(db_column='sDoorEventCloseRearBack', blank=True, null=True)  # Field name made lowercase.
    sdooreventcloserearside = models.TextField(db_column='sDoorEventCloseRearSide', blank=True, null=True)  # Field name made lowercase.
    sdooreventopenfront = models.TextField(db_column='sDoorEventOpenFront', blank=True, null=True)  # Field name made lowercase.
    sdooreventopenrearback = models.TextField(db_column='sDoorEventOpenRearBack', blank=True, null=True)  # Field name made lowercase.
    sdooreventopenrearside = models.TextField(db_column='sDoorEventOpenRearSide', blank=True, null=True)  # Field name made lowercase.
    slc_vehicletype = models.TextField(db_column='sLC_VehicleType', blank=True, null=True)  # Field name made lowercase.
    ssuspensiontype = models.TextField(db_column='sSuspensionType', blank=True, null=True)  # Field name made lowercase.
    edefaultamp = models.IntegerField(db_column='eDefaultAmp', blank=True, null=True)  # Field name made lowercase.
    edefaultengine = models.IntegerField(db_column='eDefaultEngine', blank=True, null=True)  # Field name made lowercase.
    edefaultexhaust = models.IntegerField(db_column='eDefaultExhaust', blank=True, null=True)  # Field name made lowercase.
    edefaulthorn = models.IntegerField(db_column='eDefaultHorn', blank=True, null=True)  # Field name made lowercase.
    edefaultsiren = models.IntegerField(db_column='eDefaultSiren', blank=True, null=True)  # Field name made lowercase.
    edefaultspeaker = models.IntegerField(db_column='eDefaultSpeaker', blank=True, null=True)  # Field name made lowercase.
    evehicleaudiopartdefaults = models.IntegerField(db_column='eVehicleAudioPartDefaults', blank=True, null=True)  # Field name made lowercase.
    fmaxenclosedness = models.FloatField(db_column='fMaxEnclosedness', blank=True, null=True)  # Field name made lowercase.
    fwheelforceeventthreshold = models.FloatField(db_column='fWheelForceEventThreshold', blank=True, null=True)  # Field name made lowercase.
    fwheelforcemax = models.FloatField(db_column='fWheelForceMax', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleAudioPartDefaults'


class Vehiclecategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    evehiclecategory = models.IntegerField(db_column='eVehicleCategory', blank=True, null=True)  # Field name made lowercase.
    fhairsquash = models.FloatField(db_column='fHairSquash', blank=True, null=True)  # Field name made lowercase.
    fmaxheight = models.FloatField(db_column='fMaxHeight', blank=True, null=True)  # Field name made lowercase.
    fmaxlength = models.FloatField(db_column='fMaxLength', blank=True, null=True)  # Field name made lowercase.
    fmaxwidth = models.FloatField(db_column='fMaxWidth', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleCategories'


class Vehiclecategoryrestrictions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    evehiclecategory = models.IntegerField(db_column='eVehicleCategory', blank=True, null=True)  # Field name made lowercase.
    nnumconcurrentsetuptypes = models.IntegerField(db_column='nNumConcurrentSetupTypes', blank=True, null=True)  # Field name made lowercase.
    nvehiclecategoryrestriction = models.IntegerField(db_column='nVehicleCategoryRestriction', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleCategoryRestrictions'


class Vehiclecolours(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fprobability = models.FloatField(db_column='fProbability', blank=True, null=True)  # Field name made lowercase.
    nbluecomponent = models.IntegerField(db_column='nBlueComponent', blank=True, null=True)  # Field name made lowercase.
    ngreencomponent = models.IntegerField(db_column='nGreenComponent', blank=True, null=True)  # Field name made lowercase.
    nredcomponent = models.IntegerField(db_column='nRedComponent', blank=True, null=True)  # Field name made lowercase.
    evehiclecolour = models.IntegerField(db_column='eVehicleColour', blank=True, null=True)  # Field name made lowercase.
    bismetallic = models.IntegerField(db_column='bIsMetallic', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleColours'


class Vehiclecomponentunlockitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    salternateresource = models.TextField(db_column='sAlternateResource', blank=True, null=True)  # Field name made lowercase.
    sresource = models.TextField(db_column='sResource', blank=True, null=True)  # Field name made lowercase.
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    euicomponent = models.IntegerField(db_column='eUIComponent', blank=True, null=True)  # Field name made lowercase.
    napplicationcost = models.IntegerField(db_column='nApplicationCost', blank=True, null=True)  # Field name made lowercase.
    napplicationrating = models.IntegerField(db_column='nApplicationRating', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleComponentUnlockItemTypes'


class Vehiclecomponents(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    evehiclecomponent = models.IntegerField(db_column='eVehicleComponent', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleComponents'


class Vehiclecritical(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ehudmessage = models.IntegerField(db_column='eHUDMessage', blank=True, null=True)  # Field name made lowercase.
    evehiclecritical = models.IntegerField(db_column='eVehicleCritical', blank=True, null=True)  # Field name made lowercase.
    fweight = models.FloatField(db_column='fWeight', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleCritical'


class Vehicledamagehandlingeffects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    evehicledamagehandlingeffect = models.IntegerField(db_column='eVehicleDamageHandlingEffect', blank=True, null=True)  # Field name made lowercase.
    fbrakeeffectiveness = models.FloatField(db_column='fBrakeEffectiveness', blank=True, null=True)  # Field name made lowercase.
    fenginetorquescale = models.FloatField(db_column='fEngineTorqueScale', blank=True, null=True)  # Field name made lowercase.
    ffrontlatgrip = models.FloatField(db_column='fFrontLatGrip', blank=True, null=True)  # Field name made lowercase.
    ffrontlonggrip = models.FloatField(db_column='fFrontLongGrip', blank=True, null=True)  # Field name made lowercase.
    fmaxspeedscale = models.FloatField(db_column='fMaxSpeedScale', blank=True, null=True)  # Field name made lowercase.
    frearlatgrip = models.FloatField(db_column='fRearLatGrip', blank=True, null=True)  # Field name made lowercase.
    frearlonggrip = models.FloatField(db_column='fRearLongGrip', blank=True, null=True)  # Field name made lowercase.
    fsteeringspeed = models.FloatField(db_column='fSteeringSpeed', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleDamageHandlingEffects'


class Vehicledamagelevels(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ehandlingeffect = models.IntegerField(db_column='eHandlingEffect', blank=True, null=True)  # Field name made lowercase.
    evehiclecritical = models.IntegerField(db_column='eVehicleCritical', blank=True, null=True)  # Field name made lowercase.
    evehicledamagelevel = models.IntegerField(db_column='eVehicleDamageLevel', blank=True, null=True)  # Field name made lowercase.
    fhealththreshold = models.FloatField(db_column='fHealthThreshold', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleDamageLevels'


class Vehicledamagevfx(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdamagestatebegin = models.TextField(db_column='sDamageStateBegin', blank=True, null=True)  # Field name made lowercase.
    sdamagestateend = models.TextField(db_column='sDamageStateEnd', blank=True, null=True)  # Field name made lowercase.
    sexplosionaudio = models.TextField(db_column='sExplosionAudio', blank=True, null=True)  # Field name made lowercase.
    sexplosionevent = models.TextField(db_column='sExplosionEvent', blank=True, null=True)  # Field name made lowercase.
    evehicledamagevfx = models.IntegerField(db_column='eVehicleDamageVFX', blank=True, null=True)  # Field name made lowercase.
    fhealththreshold = models.FloatField(db_column='fHealthThreshold', blank=True, null=True)  # Field name made lowercase.
    nstatenumber = models.IntegerField(db_column='nStateNumber', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleDamageVFX'


class Vehicledistrict(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sheightfield = models.TextField(db_column='sHeightfield', blank=True, null=True)  # Field name made lowercase.
    fworldoffsetx = models.FloatField(db_column='fWorldOffsetX', blank=True, null=True)  # Field name made lowercase.
    fworldoffsety = models.FloatField(db_column='fWorldOffsetY', blank=True, null=True)  # Field name made lowercase.
    fworldoffsetz = models.FloatField(db_column='fWorldOffsetZ', blank=True, null=True)  # Field name made lowercase.
    fworldtotexturescalexy = models.FloatField(db_column='fWorldToTextureScaleXY', blank=True, null=True)  # Field name made lowercase.
    fworldtotexturescalez = models.FloatField(db_column='fWorldToTextureScaleZ', blank=True, null=True)  # Field name made lowercase.
    evehicledistricts = models.IntegerField(db_column='eVehicleDistricts', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleDistrict'


class Vehicledooranimationsets(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sclosedframe = models.TextField(db_column='sClosedFrame', blank=True, null=True)  # Field name made lowercase.
    sclosefrominside = models.TextField(db_column='sCloseFromInside', blank=True, null=True)  # Field name made lowercase.
    sclosefromoutside = models.TextField(db_column='sCloseFromOutside', blank=True, null=True)  # Field name made lowercase.
    sclosegetin = models.TextField(db_column='sCloseGetIn', blank=True, null=True)  # Field name made lowercase.
    sopenbailout = models.TextField(db_column='sOpenBailOut', blank=True, null=True)  # Field name made lowercase.
    sopenframe = models.TextField(db_column='sOpenFrame', blank=True, null=True)  # Field name made lowercase.
    sopenfromoutside = models.TextField(db_column='sOpenFromOutside', blank=True, null=True)  # Field name made lowercase.
    sopengetout = models.TextField(db_column='sOpenGetOut', blank=True, null=True)  # Field name made lowercase.
    sopenseatslideejectcriminal = models.TextField(db_column='sOpenSeatSlideEjectCriminal', blank=True, null=True)  # Field name made lowercase.
    sopenseatslideejectenforcer = models.TextField(db_column='sOpenSeatSlideEjectEnforcer', blank=True, null=True)  # Field name made lowercase.
    evehicledooranimationset = models.IntegerField(db_column='eVehicleDoorAnimationSet', blank=True, null=True)  # Field name made lowercase.
    bdooropenwhileinside = models.IntegerField(db_column='bDoorOpenWhileInside', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleDoorAnimationSets'


class Vehicleevents(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nignoreme = models.IntegerField(db_column='nIgnoreMe', blank=True, null=True)  # Field name made lowercase.
    enpcevent = models.IntegerField(db_column='eNPCEvent', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleEvents'


class Vehiclegear(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    spackageimageref = models.TextField(db_column='sPackageImageRef', blank=True, null=True)  # Field name made lowercase.
    evehiclegear = models.IntegerField(db_column='eVehicleGear', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleGear'


class Vehicleinteractionanimations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fblendintime = models.FloatField(db_column='fBlendInTime', blank=True, null=True)  # Field name made lowercase.
    fblendouttime = models.FloatField(db_column='fBlendOutTime', blank=True, null=True)  # Field name made lowercase.
    evehicleinteractionanimation = models.IntegerField(db_column='eVehicleInteractionAnimation', blank=True, null=True)  # Field name made lowercase.
    bmirror = models.IntegerField(db_column='bMirror', blank=True, null=True)  # Field name made lowercase.
    bpauseatend = models.IntegerField(db_column='bPauseAtEnd', blank=True, null=True)  # Field name made lowercase.
    bscaleroot = models.IntegerField(db_column='bScaleRoot', blank=True, null=True)  # Field name made lowercase.
    bstartatorigin = models.IntegerField(db_column='bStartAtOrigin', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleInteractionAnimations'


class Vehicleinteractionsequences(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ssequencename = models.TextField(db_column='sSequenceName', blank=True, null=True)  # Field name made lowercase.
    evehicleplayeranimationset = models.IntegerField(db_column='eVehiclePlayerAnimationSet', blank=True, null=True)  # Field name made lowercase.
    evehicleinteractionanimation = models.IntegerField(db_column='eVehicleInteractionAnimation', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleInteractionSequences'


class Vehicleitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    sresource = models.TextField(db_column='sResource', blank=True, null=True)  # Field name made lowercase.
    efnmod_0 = models.IntegerField(db_column='eFnMod_0', blank=True, null=True)  # Field name made lowercase.
    efnmod_1 = models.IntegerField(db_column='eFnMod_1', blank=True, null=True)  # Field name made lowercase.
    efnmod_2 = models.IntegerField(db_column='eFnMod_2', blank=True, null=True)  # Field name made lowercase.
    efnmod_3 = models.IntegerField(db_column='eFnMod_3', blank=True, null=True)  # Field name made lowercase.
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    nreeditfee = models.IntegerField(db_column='nReeditFee', blank=True, null=True)  # Field name made lowercase.
    evehicle = models.IntegerField(db_column='eVehicle', blank=True, null=True)  # Field name made lowercase.
    bpreset = models.IntegerField(db_column='bPreset', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleItemTypes'


class Vehiclemenuentries(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplaypicture = models.TextField(db_column='sDisplayPicture', blank=True, null=True)  # Field name made lowercase.
    sdisplaytext = models.TextField(db_column='sDisplayText', blank=True, null=True)  # Field name made lowercase.
    smenulevel = models.TextField(db_column='sMenuLevel', blank=True, null=True)  # Field name made lowercase.
    smenutag = models.TextField(db_column='sMenuTag', blank=True, null=True)  # Field name made lowercase.
    soptionalscene = models.TextField(db_column='sOptionalScene', blank=True, null=True)  # Field name made lowercase.
    ecameraangle = models.IntegerField(db_column='eCameraAngle', blank=True, null=True)  # Field name made lowercase.
    evehiclemenuentry = models.IntegerField(db_column='eVehicleMenuEntry', blank=True, null=True)  # Field name made lowercase.
    benabled = models.IntegerField(db_column='bEnabled', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleMenuEntries'


class Vehiclemodifieritemtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleModifierItemTypes'


class Vehiclenpcinsideanimationsets(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sejectinitialcriminal = models.TextField(db_column='sEjectInitialCriminal', blank=True, null=True)  # Field name made lowercase.
    sejectinitialenforcer = models.TextField(db_column='sEjectInitialEnforcer', blank=True, null=True)  # Field name made lowercase.
    sejectinitialfrompassengersidecriminal = models.TextField(db_column='sEjectInitialFromPassengerSideCriminal', blank=True, null=True)  # Field name made lowercase.
    sejectinitialfrompassengersideenforcer = models.TextField(db_column='sEjectInitialFromPassengerSideEnforcer', blank=True, null=True)  # Field name made lowercase.
    sejectlatercriminal = models.TextField(db_column='sEjectLaterCriminal', blank=True, null=True)  # Field name made lowercase.
    sejectlaterenforcer = models.TextField(db_column='sEjectLaterEnforcer', blank=True, null=True)  # Field name made lowercase.
    sejectlaterfrompassengersidecriminal = models.TextField(db_column='sEjectLaterFromPassengerSideCriminal', blank=True, null=True)  # Field name made lowercase.
    sejectlaterfrompassengersideenforcer = models.TextField(db_column='sEjectLaterFromPassengerSideEnforcer', blank=True, null=True)  # Field name made lowercase.
    evehiclenpcinsideanimationset = models.IntegerField(db_column='eVehicleNPCInsideAnimationSet', blank=True, null=True)  # Field name made lowercase.
    fejectdistancedriversidecriminal = models.FloatField(db_column='fEjectDistanceDriverSideCriminal', blank=True, null=True)  # Field name made lowercase.
    fejectdistancedriversideenforcer = models.FloatField(db_column='fEjectDistanceDriverSideEnforcer', blank=True, null=True)  # Field name made lowercase.
    fejectdistancepassengersidecriminal = models.FloatField(db_column='fEjectDistancePassengerSideCriminal', blank=True, null=True)  # Field name made lowercase.
    fejectdistancepassengersideenforcer = models.FloatField(db_column='fEjectDistancePassengerSideEnforcer', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleNPCInsideAnimationSets'


class Vehicleplayeranimationsets(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdrivesteer = models.TextField(db_column='sDriveSteer', blank=True, null=True)  # Field name made lowercase.
    spassengeridle = models.TextField(db_column='sPassengerIdle', blank=True, null=True)  # Field name made lowercase.
    eanimtreedecision = models.IntegerField(db_column='eAnimTreeDecision', blank=True, null=True)  # Field name made lowercase.
    evehicleplayeranimationset = models.IntegerField(db_column='eVehiclePlayerAnimationSet', blank=True, null=True)  # Field name made lowercase.
    fleaninduration = models.FloatField(db_column='fLeanInDuration', blank=True, null=True)  # Field name made lowercase.
    fleanoutduration = models.FloatField(db_column='fLeanOutDuration', blank=True, null=True)  # Field name made lowercase.
    bmirroranimations = models.IntegerField(db_column='bMirrorAnimations', blank=True, null=True)  # Field name made lowercase.
    breverseaim = models.IntegerField(db_column='bReverseAim', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehiclePlayerAnimationSets'


class Vehiclepositioninfo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    evehicleanimationcategory = models.IntegerField(db_column='eVehicleAnimationCategory', blank=True, null=True)  # Field name made lowercase.
    evehicledooranimationset = models.IntegerField(db_column='eVehicleDoorAnimationSet', blank=True, null=True)  # Field name made lowercase.
    evehiclenpcinsideanimationset = models.IntegerField(db_column='eVehicleNPCInsideAnimationSet', blank=True, null=True)  # Field name made lowercase.
    evehicleplayeranimationset = models.IntegerField(db_column='eVehiclePlayerAnimationSet', blank=True, null=True)  # Field name made lowercase.
    nvcpangle = models.IntegerField(db_column='nVCPAngle', blank=True, null=True)  # Field name made lowercase.
    nvcpdirection = models.IntegerField(db_column='nVCPDirection', blank=True, null=True)  # Field name made lowercase.
    evehiclepositionindex = models.IntegerField(db_column='eVehiclePositionIndex', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehiclePositionInfo'


class Vehicleseatcameras(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eleanoutcamera = models.IntegerField(db_column='eLeanOutCamera', blank=True, null=True)  # Field name made lowercase.
    esittingcamera = models.IntegerField(db_column='eSittingCamera', blank=True, null=True)  # Field name made lowercase.
    evehiclepositionindex = models.IntegerField(db_column='eVehiclePositionIndex', blank=True, null=True)  # Field name made lowercase.
    evehiclesetuptype = models.IntegerField(db_column='eVehicleSetupType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleSeatCameras'


class Vehiclesetuptypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    sgolemobilebase = models.TextField(db_column='sGolemobileBase', blank=True, null=True)  # Field name made lowercase.
    sphysicsasset = models.TextField(db_column='sPhysicsAsset', blank=True, null=True)  # Field name made lowercase.
    sshareddataobject = models.TextField(db_column='sSharedDataObject', blank=True, null=True)  # Field name made lowercase.
    svehiclename = models.TextField(db_column='sVehicleName', blank=True, null=True)  # Field name made lowercase.
    svehiclesetupasset = models.TextField(db_column='sVehicleSetupAsset', blank=True, null=True)  # Field name made lowercase.
    svfxprefab = models.TextField(db_column='sVFXPrefab', blank=True, null=True)  # Field name made lowercase.
    eaudiotype = models.IntegerField(db_column='eAudioType', blank=True, null=True)  # Field name made lowercase.
    eexplosiontype = models.IntegerField(db_column='eExplosionType', blank=True, null=True)  # Field name made lowercase.
    egameplayobject = models.IntegerField(db_column='eGameplayObject', blank=True, null=True)  # Field name made lowercase.
    epedestriandriver = models.IntegerField(db_column='ePedestrianDriver', blank=True, null=True)  # Field name made lowercase.
    euimeshviewersetup = models.IntegerField(db_column='eUIMeshViewerSetup', blank=True, null=True)  # Field name made lowercase.
    evehicleanimationcategory = models.IntegerField(db_column='eVehicleAnimationCategory', blank=True, null=True)  # Field name made lowercase.
    evehiclecategory = models.IntegerField(db_column='eVehicleCategory', blank=True, null=True)  # Field name made lowercase.
    f0mssteerangle = models.FloatField(db_column='f0msSteerAngle', blank=True, null=True)  # Field name made lowercase.
    f12mssteerangle = models.FloatField(db_column='f12msSteerAngle', blank=True, null=True)  # Field name made lowercase.
    f22mssteerangle = models.FloatField(db_column='f22msSteerAngle', blank=True, null=True)  # Field name made lowercase.
    f2500rpmtorque = models.FloatField(db_column='f2500RpmTorque', blank=True, null=True)  # Field name made lowercase.
    f2ndgearspeed = models.FloatField(db_column='f2ndGearSpeed', blank=True, null=True)  # Field name made lowercase.
    f3rdgearspeed = models.FloatField(db_column='f3rdGearSpeed', blank=True, null=True)  # Field name made lowercase.
    f4500rpmtorque = models.FloatField(db_column='f4500RpmTorque', blank=True, null=True)  # Field name made lowercase.
    f4thgearspeed = models.FloatField(db_column='f4thGearSpeed', blank=True, null=True)  # Field name made lowercase.
    f500rpmtorque = models.FloatField(db_column='f500RpmTorque', blank=True, null=True)  # Field name made lowercase.
    f5thgearspeed = models.FloatField(db_column='f5thGearSpeed', blank=True, null=True)  # Field name made lowercase.
    f7000rpmtorque = models.FloatField(db_column='f7000RpmTorque', blank=True, null=True)  # Field name made lowercase.
    fblobshadowscale_0 = models.FloatField(db_column='fBlobShadowScale_0', blank=True, null=True)  # Field name made lowercase.
    fblobshadowscale_1 = models.FloatField(db_column='fBlobShadowScale_1', blank=True, null=True)  # Field name made lowercase.
    fblobshadowscale_2 = models.FloatField(db_column='fBlobShadowScale_2', blank=True, null=True)  # Field name made lowercase.
    fblobshadowtranslate_0 = models.FloatField(db_column='fBlobShadowTranslate_0', blank=True, null=True)  # Field name made lowercase.
    fblobshadowtranslate_1 = models.FloatField(db_column='fBlobShadowTranslate_1', blank=True, null=True)  # Field name made lowercase.
    fblobshadowtranslate_2 = models.FloatField(db_column='fBlobShadowTranslate_2', blank=True, null=True)  # Field name made lowercase.
    fbreakincsaduration = models.FloatField(db_column='fBreakInCSADuration', blank=True, null=True)  # Field name made lowercase.
    fcambasezfar = models.FloatField(db_column='fCamBaseZFar', blank=True, null=True)  # Field name made lowercase.
    fcambaseznear = models.FloatField(db_column='fCamBaseZNear', blank=True, null=True)  # Field name made lowercase.
    fcargoheightreductionfactor = models.FloatField(db_column='fCargoHeightReductionFactor', blank=True, null=True)  # Field name made lowercase.
    fcargotorquereductionfactor = models.FloatField(db_column='fCargoTorqueReductionFactor', blank=True, null=True)  # Field name made lowercase.
    fchassistorquefactor = models.FloatField(db_column='fChassisTorqueFactor', blank=True, null=True)  # Field name made lowercase.
    fcollisiondamage = models.FloatField(db_column='fCollisionDamage', blank=True, null=True)  # Field name made lowercase.
    fcomoffsetx = models.FloatField(db_column='fCOMOffsetX', blank=True, null=True)  # Field name made lowercase.
    fcomoffsetz = models.FloatField(db_column='fCOMOffsetZ', blank=True, null=True)  # Field name made lowercase.
    fdrivercamfar = models.FloatField(db_column='fDriverCamFar', blank=True, null=True)  # Field name made lowercase.
    fdrivercamnear = models.FloatField(db_column='fDriverCamNear', blank=True, null=True)  # Field name made lowercase.
    fenginebrakingfactor = models.FloatField(db_column='fEngineBrakingFactor', blank=True, null=True)  # Field name made lowercase.
    ffinaldriveratio = models.FloatField(db_column='fFinalDriveRatio', blank=True, null=True)  # Field name made lowercase.
    ffrontlatfactor = models.FloatField(db_column='fFrontLatFactor', blank=True, null=True)  # Field name made lowercase.
    ffrontlongfactor = models.FloatField(db_column='fFrontLongFactor', blank=True, null=True)  # Field name made lowercase.
    ffrontsuspensionspeed = models.FloatField(db_column='fFrontSuspensionSpeed', blank=True, null=True)  # Field name made lowercase.
    ffrontsuspensiontravel = models.FloatField(db_column='fFrontSuspensionTravel', blank=True, null=True)  # Field name made lowercase.
    ffrontwheelboneoffset_0 = models.FloatField(db_column='fFrontWheelBoneOffset_0', blank=True, null=True)  # Field name made lowercase.
    ffrontwheelboneoffset_1 = models.FloatField(db_column='fFrontWheelBoneOffset_1', blank=True, null=True)  # Field name made lowercase.
    ffrontwheelboneoffset_2 = models.FloatField(db_column='fFrontWheelBoneOffset_2', blank=True, null=True)  # Field name made lowercase.
    ffrontwheelmeshoffset_0 = models.FloatField(db_column='fFrontWheelMeshOffset_0', blank=True, null=True)  # Field name made lowercase.
    ffrontwheelmeshoffset_1 = models.FloatField(db_column='fFrontWheelMeshOffset_1', blank=True, null=True)  # Field name made lowercase.
    ffrontwheelmeshoffset_2 = models.FloatField(db_column='fFrontWheelMeshOffset_2', blank=True, null=True)  # Field name made lowercase.
    ffrontwheelradius = models.FloatField(db_column='fFrontWheelRadius', blank=True, null=True)  # Field name made lowercase.
    fgearratios_0 = models.FloatField(db_column='fGearRatios_0', blank=True, null=True)  # Field name made lowercase.
    fgearratios_1 = models.FloatField(db_column='fGearRatios_1', blank=True, null=True)  # Field name made lowercase.
    fgearratios_2 = models.FloatField(db_column='fGearRatios_2', blank=True, null=True)  # Field name made lowercase.
    fgearratios_3 = models.FloatField(db_column='fGearRatios_3', blank=True, null=True)  # Field name made lowercase.
    fgearratios_4 = models.FloatField(db_column='fGearRatios_4', blank=True, null=True)  # Field name made lowercase.
    fgearratios_5 = models.FloatField(db_column='fGearRatios_5', blank=True, null=True)  # Field name made lowercase.
    fidlerpm = models.FloatField(db_column='fIdleRPM', blank=True, null=True)  # Field name made lowercase.
    flsdfactor = models.FloatField(db_column='fLSDFactor', blank=True, null=True)  # Field name made lowercase.
    fmaxbraketorque = models.FloatField(db_column='fMaxBrakeTorque', blank=True, null=True)  # Field name made lowercase.
    fmaxcargoheightreduction = models.FloatField(db_column='fMaxCargoHeightReduction', blank=True, null=True)  # Field name made lowercase.
    fmaxcargotorquereduction = models.FloatField(db_column='fMaxCargoTorqueReduction', blank=True, null=True)  # Field name made lowercase.
    fmaxdirt = models.FloatField(db_column='fMaxDirt', blank=True, null=True)  # Field name made lowercase.
    fmaxdust = models.FloatField(db_column='fMaxDust', blank=True, null=True)  # Field name made lowercase.
    fmaxrepairtimesecs = models.FloatField(db_column='fMaxRepairTimeSecs', blank=True, null=True)  # Field name made lowercase.
    fmaxreversespeed = models.FloatField(db_column='fMaxReverseSpeed', blank=True, null=True)  # Field name made lowercase.
    fmaxspeed = models.FloatField(db_column='fMaxSpeed', blank=True, null=True)  # Field name made lowercase.
    fmindirt = models.FloatField(db_column='fMinDirt', blank=True, null=True)  # Field name made lowercase.
    fmindust = models.FloatField(db_column='fMinDust', blank=True, null=True)  # Field name made lowercase.
    fpercentdirty = models.FloatField(db_column='fPercentDirty', blank=True, null=True)  # Field name made lowercase.
    fpercentperfectlyclean = models.FloatField(db_column='fPercentPerfectlyClean', blank=True, null=True)  # Field name made lowercase.
    framraiddamagemultiplier = models.FloatField(db_column='fRamraidDamageMultiplier', blank=True, null=True)  # Field name made lowercase.
    frearhandbrakelat = models.FloatField(db_column='fRearHandbrakeLat', blank=True, null=True)  # Field name made lowercase.
    frearhandbrakelong = models.FloatField(db_column='fRearHandbrakeLong', blank=True, null=True)  # Field name made lowercase.
    frearlatfactor = models.FloatField(db_column='fRearLatFactor', blank=True, null=True)  # Field name made lowercase.
    frearlongfactor = models.FloatField(db_column='fRearLongFactor', blank=True, null=True)  # Field name made lowercase.
    frearsuspensionspeed = models.FloatField(db_column='fRearSuspensionSpeed', blank=True, null=True)  # Field name made lowercase.
    frearsuspensiontravel = models.FloatField(db_column='fRearSuspensionTravel', blank=True, null=True)  # Field name made lowercase.
    frearwheelboneoffset_0 = models.FloatField(db_column='fRearWheelBoneOffset_0', blank=True, null=True)  # Field name made lowercase.
    frearwheelboneoffset_1 = models.FloatField(db_column='fRearWheelBoneOffset_1', blank=True, null=True)  # Field name made lowercase.
    frearwheelboneoffset_2 = models.FloatField(db_column='fRearWheelBoneOffset_2', blank=True, null=True)  # Field name made lowercase.
    frearwheelmeshoffset_0 = models.FloatField(db_column='fRearWheelMeshOffset_0', blank=True, null=True)  # Field name made lowercase.
    frearwheelmeshoffset_1 = models.FloatField(db_column='fRearWheelMeshOffset_1', blank=True, null=True)  # Field name made lowercase.
    frearwheelmeshoffset_2 = models.FloatField(db_column='fRearWheelMeshOffset_2', blank=True, null=True)  # Field name made lowercase.
    frearwheelradius = models.FloatField(db_column='fRearWheelRadius', blank=True, null=True)  # Field name made lowercase.
    fredlinerpm = models.FloatField(db_column='fRedlineRPM', blank=True, null=True)  # Field name made lowercase.
    freversethrottle = models.FloatField(db_column='fReverseThrottle', blank=True, null=True)  # Field name made lowercase.
    fsteeraccel = models.FloatField(db_column='fSteerAccel', blank=True, null=True)  # Field name made lowercase.
    fsteerspeed = models.FloatField(db_column='fSteerSpeed', blank=True, null=True)  # Field name made lowercase.
    fsuspensiondamping = models.FloatField(db_column='fSuspensionDamping', blank=True, null=True)  # Field name made lowercase.
    fsuspensionstiffness = models.FloatField(db_column='fSuspensionStiffness', blank=True, null=True)  # Field name made lowercase.
    fwheellatasymptoteslip = models.FloatField(db_column='fWheelLatAsymptoteSlip', blank=True, null=True)  # Field name made lowercase.
    fwheellatasymptotevalue = models.FloatField(db_column='fWheelLatAsymptoteValue', blank=True, null=True)  # Field name made lowercase.
    fwheellatextremumslip = models.FloatField(db_column='fWheelLatExtremumSlip', blank=True, null=True)  # Field name made lowercase.
    fwheellatextremumvalue = models.FloatField(db_column='fWheelLatExtremumValue', blank=True, null=True)  # Field name made lowercase.
    fwheellongasymptoteslip = models.FloatField(db_column='fWheelLongAsymptoteSlip', blank=True, null=True)  # Field name made lowercase.
    fwheellongasymptotevalue = models.FloatField(db_column='fWheelLongAsymptoteValue', blank=True, null=True)  # Field name made lowercase.
    fwheellongextremumslip = models.FloatField(db_column='fWheelLongExtremumSlip', blank=True, null=True)  # Field name made lowercase.
    fwheellongextremumvalue = models.FloatField(db_column='fWheelLongExtremumValue', blank=True, null=True)  # Field name made lowercase.
    ncabincargopipcapacity = models.IntegerField(db_column='nCabinCargoPipCapacity', blank=True, null=True)  # Field name made lowercase.
    ncamerapitchmax = models.IntegerField(db_column='nCameraPitchMax', blank=True, null=True)  # Field name made lowercase.
    ncamerapitchmin = models.IntegerField(db_column='nCameraPitchMin', blank=True, null=True)  # Field name made lowercase.
    ncargoareaseatpositions = models.IntegerField(db_column='nCargoAreaSeatPositions', blank=True, null=True)  # Field name made lowercase.
    ninitialcampitch = models.IntegerField(db_column='nInitialCamPitch', blank=True, null=True)  # Field name made lowercase.
    nmaincargopipcapacity = models.IntegerField(db_column='nMainCargoPipCapacity', blank=True, null=True)  # Field name made lowercase.
    nmaxhealth = models.IntegerField(db_column='nMaxHealth', blank=True, null=True)  # Field name made lowercase.
    nmaxrepaircost = models.IntegerField(db_column='nMaxRepairCost', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    nspawncost = models.IntegerField(db_column='nSpawnCost', blank=True, null=True)  # Field name made lowercase.
    edrivetype = models.IntegerField(db_column='eDriveType', blank=True, null=True)  # Field name made lowercase.
    etempassets = models.IntegerField(db_column='eTempAssets', blank=True, null=True)  # Field name made lowercase.
    euicategory = models.IntegerField(db_column='eUICategory', blank=True, null=True)  # Field name made lowercase.
    evehiclemodelclass = models.IntegerField(db_column='eVehicleModelClass', blank=True, null=True)  # Field name made lowercase.
    evehiclesetuptype = models.IntegerField(db_column='eVehicleSetupType', blank=True, null=True)  # Field name made lowercase.
    bhasalarm = models.IntegerField(db_column='bHasAlarm', blank=True, null=True)  # Field name made lowercase.
    bhasrearseats = models.IntegerField(db_column='bHasRearSeats', blank=True, null=True)  # Field name made lowercase.
    bhastaillights = models.IntegerField(db_column='bHasTailLights', blank=True, null=True)  # Field name made lowercase.
    bisplayeronlyvehicle = models.IntegerField(db_column='bIsPlayerOnlyVehicle', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleSetupTypes'


class Vehicletempsetups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    stempsetupinfo = models.TextField(db_column='sTempSetupInfo', blank=True, null=True)  # Field name made lowercase.
    evehicletempsetup = models.IntegerField(db_column='eVehicleTempSetup', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleTempSetups'


class Vehicleuicameraangles(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    evehicleuicameraangle = models.IntegerField(db_column='eVehicleUICameraAngle', blank=True, null=True)  # Field name made lowercase.
    factorrotation = models.FloatField(db_column='fActorRotation', blank=True, null=True)  # Field name made lowercase.
    fcameraposition = models.FloatField(db_column='fCameraPosition', blank=True, null=True)  # Field name made lowercase.
    ffov = models.FloatField(db_column='fFOV', blank=True, null=True)  # Field name made lowercase.
    bopendoors = models.IntegerField(db_column='bOpenDoors', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleUICameraAngles'


class Vehicleuicategory(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    evehicleuicategory = models.IntegerField(db_column='eVehicleUICategory', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleUICategory'


class Vehicleuicomponentcategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    evehicleuicomponentcategory = models.IntegerField(db_column='eVehicleUIComponentCategory', blank=True, null=True)  # Field name made lowercase.
    nsortingpriority = models.IntegerField(db_column='nSortingPriority', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleUIComponentCategories'


class Vehicleuicomponentinfos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ecameraangle = models.IntegerField(db_column='eCameraAngle', blank=True, null=True)  # Field name made lowercase.
    ecategory = models.IntegerField(db_column='eCategory', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleUIComponentInfos'


class Vehicleuisetups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    facceleration = models.FloatField(db_column='fAcceleration', blank=True, null=True)  # Field name made lowercase.
    fcollisiondamage = models.FloatField(db_column='fCollisionDamage', blank=True, null=True)  # Field name made lowercase.
    fhandling = models.FloatField(db_column='fHandling', blank=True, null=True)  # Field name made lowercase.
    fhealth = models.FloatField(db_column='fHealth', blank=True, null=True)  # Field name made lowercase.
    fsuspensionoffsethack = models.FloatField(db_column='fSuspensionOffsetHack', blank=True, null=True)  # Field name made lowercase.
    ftopspeed = models.FloatField(db_column='fTopSpeed', blank=True, null=True)  # Field name made lowercase.
    evehiclesetuptype = models.IntegerField(db_column='eVehicleSetupType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleUISetups'


class Videoreplayuientries(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)  # Field name made lowercase.
    svideofilename = models.TextField(db_column='sVideoFileName', blank=True, null=True)  # Field name made lowercase.
    evideoreplayuientry = models.IntegerField(db_column='eVideoReplayUIEntry', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VideoReplayUIEntries'


class Vignettetypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    spackage = models.TextField(db_column='sPackage', blank=True, null=True)  # Field name made lowercase.
    evignettedescriptor = models.IntegerField(db_column='eVignetteDescriptor', blank=True, null=True)  # Field name made lowercase.
    fmaxcanceldistancefromvnode = models.FloatField(db_column='fMaxCancelDistanceFromVNode', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VignetteTypes'


class Wardrobemenuentries(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdisplayimage = models.TextField(db_column='sDisplayImage', blank=True, null=True)  # Field name made lowercase.
    sdisplaytext = models.TextField(db_column='sDisplayText', blank=True, null=True)  # Field name made lowercase.
    smenulevel = models.TextField(db_column='sMenuLevel', blank=True, null=True)  # Field name made lowercase.
    smenutag = models.TextField(db_column='sMenuTag', blank=True, null=True)  # Field name made lowercase.
    smouseovertext = models.TextField(db_column='sMouseOverText', blank=True, null=True)  # Field name made lowercase.
    soptionalscene = models.TextField(db_column='sOptionalScene', blank=True, null=True)  # Field name made lowercase.
    ewardrobemenuentry = models.IntegerField(db_column='eWardrobeMenuEntry', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WardrobeMenuEntries'


class Warningpromptgroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    swarningpromptgroupname = models.TextField(db_column='sWarningPromptGroupName', blank=True, null=True)  # Field name made lowercase.
    ewarningpromptgroup = models.IntegerField(db_column='eWarningPromptGroup', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WarningPromptGroups'


class Weaponattachmentvisuals(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    simpactvfx = models.TextField(db_column='sImpactVFX', blank=True, null=True)  # Field name made lowercase.
    smuzzleflashvfx = models.TextField(db_column='sMuzzleFlashVFX', blank=True, null=True)  # Field name made lowercase.
    snontracershotvfx = models.TextField(db_column='sNonTracerShotVFX', blank=True, null=True)  # Field name made lowercase.
    stracervfx = models.TextField(db_column='sTracerVFX', blank=True, null=True)  # Field name made lowercase.
    swindupaudiotype = models.TextField(db_column='sWindupAudioType', blank=True, null=True)  # Field name made lowercase.
    eitemattachmentvisual = models.IntegerField(db_column='eItemAttachmentVisual', blank=True, null=True)  # Field name made lowercase.
    eimpactclass = models.IntegerField(db_column='eImpactClass', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaponAttachmentVisuals'


class Weaponclasses(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sunrealclassname = models.TextField(db_column='sUnrealClassName', blank=True, null=True)  # Field name made lowercase.
    eweaponclass = models.IntegerField(db_column='eWeaponClass', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaponClasses'


class Weaponcurves(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    saccuracyrecovery = models.TextField(db_column='sAccuracyRecovery', blank=True, null=True)  # Field name made lowercase.
    sburstshots = models.TextField(db_column='sBurstShots', blank=True, null=True)  # Field name made lowercase.
    seffectiverange = models.TextField(db_column='sEffectiveRange', blank=True, null=True)  # Field name made lowercase.
    spershotmodifier = models.TextField(db_column='sPerShotModifier', blank=True, null=True)  # Field name made lowercase.
    spingdistance = models.TextField(db_column='sPingDistance', blank=True, null=True)  # Field name made lowercase.
    spitch = models.TextField(db_column='sPitch', blank=True, null=True)  # Field name made lowercase.
    sradiusattenmetres = models.TextField(db_column='sRadiusAtTenMetres', blank=True, null=True)  # Field name made lowercase.
    srecoverypersecond = models.TextField(db_column='sRecoveryPerSecond', blank=True, null=True)  # Field name made lowercase.
    sreloadtime = models.TextField(db_column='sReloadTime', blank=True, null=True)  # Field name made lowercase.
    syawnegative = models.TextField(db_column='sYawNegative', blank=True, null=True)  # Field name made lowercase.
    syawpositive = models.TextField(db_column='sYawPositive', blank=True, null=True)  # Field name made lowercase.
    eweaponcurve = models.IntegerField(db_column='eWeaponCurve', blank=True, null=True)  # Field name made lowercase.
    fburstshotsinc = models.FloatField(db_column='fBurstShotsInc', blank=True, null=True)  # Field name made lowercase.
    fgeneralrecoverydelay = models.FloatField(db_column='fGeneralRecoveryDelay', blank=True, null=True)  # Field name made lowercase.
    fgeneralrecoveryscale = models.FloatField(db_column='fGeneralRecoveryScale', blank=True, null=True)  # Field name made lowercase.
    fpershotmodifierinc = models.FloatField(db_column='fPerShotModifierInc', blank=True, null=True)  # Field name made lowercase.
    fpingdistanceinc = models.FloatField(db_column='fPingDistanceInc', blank=True, null=True)  # Field name made lowercase.
    fpitchinc = models.FloatField(db_column='fPitchInc', blank=True, null=True)  # Field name made lowercase.
    fradiusattenmetresinc = models.FloatField(db_column='fRadiusAtTenMetresInc', blank=True, null=True)  # Field name made lowercase.
    freloadtimeinc = models.FloatField(db_column='fReloadTimeInc', blank=True, null=True)  # Field name made lowercase.
    fyawnegativeinc = models.FloatField(db_column='fYawNegativeInc', blank=True, null=True)  # Field name made lowercase.
    fyawpositiveinc = models.FloatField(db_column='fYawPositiveInc', blank=True, null=True)  # Field name made lowercase.
    bburstshotsrecover = models.IntegerField(db_column='bBurstShotsRecover', blank=True, null=True)  # Field name made lowercase.
    bpershotmodifierrecover = models.IntegerField(db_column='bPerShotModifierRecover', blank=True, null=True)  # Field name made lowercase.
    bpingdistancerecovers = models.IntegerField(db_column='bPingDistanceRecovers', blank=True, null=True)  # Field name made lowercase.
    bpitchrecover = models.IntegerField(db_column='bPitchRecover', blank=True, null=True)  # Field name made lowercase.
    bradiusattenmetresrecover = models.IntegerField(db_column='bRadiusAtTenMetresRecover', blank=True, null=True)  # Field name made lowercase.
    byawnegativerecover = models.IntegerField(db_column='bYawNegativeRecover', blank=True, null=True)  # Field name made lowercase.
    byawpositiverecover = models.IntegerField(db_column='bYawPositiveRecover', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaponCurves'


class Weaponitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)  # Field name made lowercase.
    eactivitymessageicon = models.IntegerField(db_column='eActivityMessageIcon', blank=True, null=True)  # Field name made lowercase.
    efnmod_0 = models.IntegerField(db_column='eFnMod_0', blank=True, null=True)  # Field name made lowercase.
    efnmod_1 = models.IntegerField(db_column='eFnMod_1', blank=True, null=True)  # Field name made lowercase.
    efnmod_2 = models.IntegerField(db_column='eFnMod_2', blank=True, null=True)  # Field name made lowercase.
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    eitemattachment = models.IntegerField(db_column='eItemAttachment', blank=True, null=True)  # Field name made lowercase.
    eweapontypelink = models.IntegerField(db_column='eWeaponTypeLink', blank=True, null=True)  # Field name made lowercase.
    bcausescontagion = models.IntegerField(db_column='bCausesContagion', blank=True, null=True)  # Field name made lowercase.
    bisskinnable = models.IntegerField(db_column='bIsSkinnable', blank=True, null=True)  # Field name made lowercase.
    bpreset = models.IntegerField(db_column='bPreset', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaponItemTypes'


class Weaponloadouts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eweaponloadout = models.IntegerField(db_column='eWeaponLoadout', blank=True, null=True)  # Field name made lowercase.
    eweapontocreate_0 = models.IntegerField(db_column='eWeaponToCreate_0', blank=True, null=True)  # Field name made lowercase.
    eweapontocreate_1 = models.IntegerField(db_column='eWeaponToCreate_1', blank=True, null=True)  # Field name made lowercase.
    eweapontocreate_2 = models.IntegerField(db_column='eWeaponToCreate_2', blank=True, null=True)  # Field name made lowercase.
    eweapontocreate_3 = models.IntegerField(db_column='eWeaponToCreate_3', blank=True, null=True)  # Field name made lowercase.
    eweapontypetofind_0 = models.IntegerField(db_column='eWeaponTypeToFind_0', blank=True, null=True)  # Field name made lowercase.
    eweapontypetofind_1 = models.IntegerField(db_column='eWeaponTypeToFind_1', blank=True, null=True)  # Field name made lowercase.
    eweapontypetofind_2 = models.IntegerField(db_column='eWeaponTypeToFind_2', blank=True, null=True)  # Field name made lowercase.
    eweapontypetofind_3 = models.IntegerField(db_column='eWeaponTypeToFind_3', blank=True, null=True)  # Field name made lowercase.
    nequipslot = models.IntegerField(db_column='nEquipSlot', blank=True, null=True)  # Field name made lowercase.
    eweaponoverridetype_0 = models.IntegerField(db_column='eWeaponOverrideType_0', blank=True, null=True)  # Field name made lowercase.
    eweaponoverridetype_1 = models.IntegerField(db_column='eWeaponOverrideType_1', blank=True, null=True)  # Field name made lowercase.
    eweaponoverridetype_2 = models.IntegerField(db_column='eWeaponOverrideType_2', blank=True, null=True)  # Field name made lowercase.
    eweaponoverridetype_3 = models.IntegerField(db_column='eWeaponOverrideType_3', blank=True, null=True)  # Field name made lowercase.
    ballowweaponpickup = models.IntegerField(db_column='bAllowWeaponPickup', blank=True, null=True)  # Field name made lowercase.
    bgiftammo = models.IntegerField(db_column='bGiftAmmo', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaponLoadouts'


class Weaponmodifieritemtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaponModifierItemTypes'


class Weaponprojectiles(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sflightaudioevent = models.TextField(db_column='sFlightAudioEvent', blank=True, null=True)  # Field name made lowercase.
    smesh = models.TextField(db_column='sMesh', blank=True, null=True)  # Field name made lowercase.
    strailvfx = models.TextField(db_column='sTrailVFX', blank=True, null=True)  # Field name made lowercase.
    eexplosion = models.IntegerField(db_column='eExplosion', blank=True, null=True)  # Field name made lowercase.
    eweaponprojectile = models.IntegerField(db_column='eWeaponProjectile', blank=True, null=True)  # Field name made lowercase.
    farmingtimer = models.FloatField(db_column='fArmingTimer', blank=True, null=True)  # Field name made lowercase.
    fbouncedamping = models.FloatField(db_column='fBounceDamping', blank=True, null=True)  # Field name made lowercase.
    ffusedelay = models.FloatField(db_column='fFuseDelay', blank=True, null=True)  # Field name made lowercase.
    fgravitymultiplier = models.FloatField(db_column='fGravityMultiplier', blank=True, null=True)  # Field name made lowercase.
    baudiowaituntilfalling = models.IntegerField(db_column='bAudioWaitUntilFalling', blank=True, null=True)  # Field name made lowercase.
    bimpactdetonated = models.IntegerField(db_column='bImpactDetonated', blank=True, null=True)  # Field name made lowercase.
    btumble = models.IntegerField(db_column='bTumble', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaponProjectiles'


class Weaponrecoils(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eweaponrecoil = models.IntegerField(db_column='eWeaponRecoil', blank=True, null=True)  # Field name made lowercase.
    frecoilexp = models.FloatField(db_column='fRecoilExp', blank=True, null=True)  # Field name made lowercase.
    frecoverexp = models.FloatField(db_column='fRecoverExp', blank=True, null=True)  # Field name made lowercase.
    nmarksmanshippitchpercentage = models.IntegerField(db_column='nMarksmanshipPitchPercentage', blank=True, null=True)  # Field name made lowercase.
    nmarksmanshipyawpercentage = models.IntegerField(db_column='nMarksmanshipYawPercentage', blank=True, null=True)  # Field name made lowercase.
    npitchmax = models.IntegerField(db_column='nPitchMax', blank=True, null=True)  # Field name made lowercase.
    npitchmin = models.IntegerField(db_column='nPitchMin', blank=True, null=True)  # Field name made lowercase.
    npitchrecoverypercentagemax = models.IntegerField(db_column='nPitchRecoveryPercentageMax', blank=True, null=True)  # Field name made lowercase.
    npitchrecoverypercentagemin = models.IntegerField(db_column='nPitchRecoveryPercentageMin', blank=True, null=True)  # Field name made lowercase.
    nrecoiltime = models.IntegerField(db_column='nRecoilTime', blank=True, null=True)  # Field name made lowercase.
    nrecovertime = models.IntegerField(db_column='nRecoverTime', blank=True, null=True)  # Field name made lowercase.
    nyawnegativemax = models.IntegerField(db_column='nYawNegativeMax', blank=True, null=True)  # Field name made lowercase.
    nyawnegativemin = models.IntegerField(db_column='nYawNegativeMin', blank=True, null=True)  # Field name made lowercase.
    nyawnegativerecoverypercentagemax = models.IntegerField(db_column='nYawNegativeRecoveryPercentageMax', blank=True, null=True)  # Field name made lowercase.
    nyawnegativerecoverypercentagemin = models.IntegerField(db_column='nYawNegativeRecoveryPercentageMin', blank=True, null=True)  # Field name made lowercase.
    nyawpositivemax = models.IntegerField(db_column='nYawPositiveMax', blank=True, null=True)  # Field name made lowercase.
    nyawpositivemin = models.IntegerField(db_column='nYawPositiveMin', blank=True, null=True)  # Field name made lowercase.
    nyawpositiverecoverypercentagemax = models.IntegerField(db_column='nYawPositiveRecoveryPercentageMax', blank=True, null=True)  # Field name made lowercase.
    nyawpositiverecoverypercentagemin = models.IntegerField(db_column='nYawPositiveRecoveryPercentageMin', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaponRecoils'


class Weaponskinunlockitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)  # Field name made lowercase.
    bhideuntilunlocked = models.IntegerField(db_column='bHideUntilUnlocked', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaponSkinUnlockItemTypes'


class Weaponskins(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eitemattachmentvisual = models.IntegerField(db_column='eItemAttachmentVisual', blank=True, null=True)  # Field name made lowercase.
    eunlock = models.IntegerField(db_column='eUnlock', blank=True, null=True)  # Field name made lowercase.
    eweaponskin = models.IntegerField(db_column='eWeaponSkin', blank=True, null=True)  # Field name made lowercase.
    eweapontypelink = models.IntegerField(db_column='eWeaponTypeLink', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaponSkins'


class Weapontypelinks(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eweapontype_0 = models.IntegerField(db_column='eWeaponType_0', blank=True, null=True)  # Field name made lowercase.
    eweapontype_1 = models.IntegerField(db_column='eWeaponType_1', blank=True, null=True)  # Field name made lowercase.
    eweapontype_2 = models.IntegerField(db_column='eWeaponType_2', blank=True, null=True)  # Field name made lowercase.
    eweapontype_3 = models.IntegerField(db_column='eWeaponType_3', blank=True, null=True)  # Field name made lowercase.
    eweapontypelink = models.IntegerField(db_column='eWeaponTypeLink', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaponTypeLinks'


class Weapontypesets(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    scommandline = models.TextField(db_column='sCommandLine', blank=True, null=True)  # Field name made lowercase.
    eweapontypeset = models.IntegerField(db_column='eWeaponTypeSet', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaponTypeSets'


class Weapontypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eammocategory = models.IntegerField(db_column='eAmmoCategory', blank=True, null=True)  # Field name made lowercase.
    edisabledrulesets = models.IntegerField(db_column='eDisabledRuleSets', blank=True, null=True)  # Field name made lowercase.
    etagger = models.IntegerField(db_column='eTagger', blank=True, null=True)  # Field name made lowercase.
    eweaponcurve = models.IntegerField(db_column='eWeaponCurve', blank=True, null=True)  # Field name made lowercase.
    eweaponprojectile = models.IntegerField(db_column='eWeaponProjectile', blank=True, null=True)  # Field name made lowercase.
    eweapontype = models.IntegerField(db_column='eWeaponType', blank=True, null=True)  # Field name made lowercase.
    faccuracycooldown = models.FloatField(db_column='fAccuracyCooldown', blank=True, null=True)  # Field name made lowercase.
    fburstinterval = models.FloatField(db_column='fBurstInterval', blank=True, null=True)  # Field name made lowercase.
    fcrouchspeed = models.FloatField(db_column='fCrouchSpeed', blank=True, null=True)  # Field name made lowercase.
    fequiptime = models.FloatField(db_column='fEquipTime', blank=True, null=True)  # Field name made lowercase.
    ffireinterval = models.FloatField(db_column='fFireInterval', blank=True, null=True)  # Field name made lowercase.
    fharddamagemodifier = models.FloatField(db_column='fHardDamageModifier', blank=True, null=True)  # Field name made lowercase.
    fhealthdamage = models.FloatField(db_column='fHealthDamage', blank=True, null=True)  # Field name made lowercase.
    fholstertime = models.FloatField(db_column='fHolsterTime', blank=True, null=True)  # Field name made lowercase.
    fjumpz = models.FloatField(db_column='fJumpZ', blank=True, null=True)  # Field name made lowercase.
    fmarksmanshipspeed = models.FloatField(db_column='fMarksmanshipSpeed', blank=True, null=True)  # Field name made lowercase.
    fpingdistance = models.FloatField(db_column='fPingDistance', blank=True, null=True)  # Field name made lowercase.
    fragdollimpulsescale = models.FloatField(db_column='fRagdollImpulseScale', blank=True, null=True)  # Field name made lowercase.
    freloadendanimduration = models.FloatField(db_column='fReloadEndAnimDuration', blank=True, null=True)  # Field name made lowercase.
    freloadtime = models.FloatField(db_column='fReloadTime', blank=True, null=True)  # Field name made lowercase.
    fresupplydelaysecs = models.FloatField(db_column='fResupplyDelaySecs', blank=True, null=True)  # Field name made lowercase.
    frunspeed = models.FloatField(db_column='fRunSpeed', blank=True, null=True)  # Field name made lowercase.
    fsoftdamagemodifier = models.FloatField(db_column='fSoftDamageModifier', blank=True, null=True)  # Field name made lowercase.
    fsprintdelay = models.FloatField(db_column='fSprintDelay', blank=True, null=True)  # Field name made lowercase.
    fsprintspeed = models.FloatField(db_column='fSprintSpeed', blank=True, null=True)  # Field name made lowercase.
    fstaminadamage = models.FloatField(db_column='fStaminaDamage', blank=True, null=True)  # Field name made lowercase.
    ftaggerduration = models.FloatField(db_column='fTaggerDuration', blank=True, null=True)  # Field name made lowercase.
    fuiharddamagelevel = models.FloatField(db_column='fUIHardDamageLevel', blank=True, null=True)  # Field name made lowercase.
    fuirangelevel = models.FloatField(db_column='fUIRangeLevel', blank=True, null=True)  # Field name made lowercase.
    fuirateoffire = models.FloatField(db_column='fUIRateOfFire', blank=True, null=True)  # Field name made lowercase.
    fuisoftdamagelevel = models.FloatField(db_column='fUISoftDamageLevel', blank=True, null=True)  # Field name made lowercase.
    fuistundamagelevel = models.FloatField(db_column='fUIStunDamageLevel', blank=True, null=True)  # Field name made lowercase.
    fwalkspeed = models.FloatField(db_column='fWalkSpeed', blank=True, null=True)  # Field name made lowercase.
    fwinduptime = models.FloatField(db_column='fWindUpTime', blank=True, null=True)  # Field name made lowercase.
    nammopoolcapacity = models.IntegerField(db_column='nAmmoPoolCapacity', blank=True, null=True)  # Field name made lowercase.
    nburstshots = models.IntegerField(db_column='nBurstShots', blank=True, null=True)  # Field name made lowercase.
    nimpulsestrength = models.IntegerField(db_column='nImpulseStrength', blank=True, null=True)  # Field name made lowercase.
    nmagazinecapacity = models.IntegerField(db_column='nMagazineCapacity', blank=True, null=True)  # Field name made lowercase.
    nmagazinewarningamount = models.IntegerField(db_column='nMagazineWarningAmount', blank=True, null=True)  # Field name made lowercase.
    nresupplyunits = models.IntegerField(db_column='nResupplyUnits', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    eclass = models.IntegerField(db_column='eClass', blank=True, null=True)  # Field name made lowercase.
    eencumbrance = models.IntegerField(db_column='eEncumbrance', blank=True, null=True)  # Field name made lowercase.
    ehudreticule = models.IntegerField(db_column='eHUDReticule', blank=True, null=True)  # Field name made lowercase.
    ehudreticulemarksmanship = models.IntegerField(db_column='eHUDReticuleMarksmanship', blank=True, null=True)  # Field name made lowercase.
    enpcfiredevent = models.IntegerField(db_column='eNPCFiredEvent', blank=True, null=True)  # Field name made lowercase.
    enpchitevent = models.IntegerField(db_column='eNPCHitEvent', blank=True, null=True)  # Field name made lowercase.
    eweaponfiringstate = models.IntegerField(db_column='eWeaponFiringState', blank=True, null=True)  # Field name made lowercase.
    balwaysplayreloadendanim = models.IntegerField(db_column='bAlwaysPlayReloadEndAnim', blank=True, null=True)  # Field name made lowercase.
    bcansprint = models.IntegerField(db_column='bCanSprint', blank=True, null=True)  # Field name made lowercase.
    bdisallowswitchinrefiretimer = models.IntegerField(db_column='bDisallowSwitchInRefireTimer', blank=True, null=True)  # Field name made lowercase.
    bdontdrop = models.IntegerField(db_column='bDontDrop', blank=True, null=True)  # Field name made lowercase.
    bequipinvehicle = models.IntegerField(db_column='bEquipInVehicle', blank=True, null=True)  # Field name made lowercase.
    bforceragdolldeath = models.IntegerField(db_column='bForceRagdollDeath', blank=True, null=True)  # Field name made lowercase.
    bhasreloadendanimation = models.IntegerField(db_column='bHasReloadEndAnimation', blank=True, null=True)  # Field name made lowercase.
    bisresuppliable = models.IntegerField(db_column='bIsResuppliable', blank=True, null=True)  # Field name made lowercase.
    blesslethal = models.IntegerField(db_column='bLessLethal', blank=True, null=True)  # Field name made lowercase.
    bloopedreload = models.IntegerField(db_column='bLoopedReload', blank=True, null=True)  # Field name made lowercase.
    busesstopaudioevent = models.IntegerField(db_column='bUsesStopAudioEvent', blank=True, null=True)  # Field name made lowercase.
    bwitnessing = models.IntegerField(db_column='bWitnessing', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaponTypes'


class Weightedrewards(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    srewardmailbody = models.TextField(db_column='sRewardMailBody', blank=True, null=True)  # Field name made lowercase.
    srewardmailsubject = models.TextField(db_column='sRewardMailSubject', blank=True, null=True)  # Field name made lowercase.
    ehudimage = models.IntegerField(db_column='eHUDImage', blank=True, null=True)  # Field name made lowercase.
    erandomreward = models.IntegerField(db_column='eRandomReward', blank=True, null=True)  # Field name made lowercase.
    ereward = models.IntegerField(db_column='eReward', blank=True, null=True)  # Field name made lowercase.
    eweightedreward = models.IntegerField(db_column='eWeightedReward', blank=True, null=True)  # Field name made lowercase.
    fweight = models.FloatField(db_column='fWeight', blank=True, null=True)  # Field name made lowercase.
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)  # Field name made lowercase.
    bofferonce = models.IntegerField(db_column='bOfferOnce', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeightedRewards'


class Witnessablecrimes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    enotorietyforbeingwitnessed = models.IntegerField(db_column='eNotorietyForBeingWitnessed', blank=True, null=True)  # Field name made lowercase.
    eprestigeforwitnessing = models.IntegerField(db_column='ePrestigeForWitnessing', blank=True, null=True)  # Field name made lowercase.
    ewitnessablecrime = models.IntegerField(db_column='eWitnessableCrime', blank=True, null=True)  # Field name made lowercase.
    fescapepenaltytimer = models.FloatField(db_column='fEscapePenaltyTimer', blank=True, null=True)  # Field name made lowercase.
    fhotlistduration = models.FloatField(db_column='fHotListDuration', blank=True, null=True)  # Field name made lowercase.
    fnpcwitnessableduration = models.FloatField(db_column='fNPCWitnessableDuration', blank=True, null=True)  # Field name made lowercase.
    etriggerednpcworldevent = models.IntegerField(db_column='eTriggeredNPCWorldEvent', blank=True, null=True)  # Field name made lowercase.
    bcontinuous = models.IntegerField(db_column='bContinuous', blank=True, null=True)  # Field name made lowercase.
    bnodirectwitness = models.IntegerField(db_column='bNoDirectWitness', blank=True, null=True)  # Field name made lowercase.
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WitnessableCrimes'

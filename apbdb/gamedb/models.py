from django.db import models


def property_cache(fn):
    def wrapped(self, *args, **kwargs):
        key = "_".join(["_", self.__class__.__name__, fn.__name__])
        if hasattr(self, key):
            return getattr(self, key)
        value = fn(self, *args, **kwargs)
        setattr(self, key, value)
        return value

    return wrapped


class Apbpawnconstant(models.Model):
    id = models.IntegerField(primary_key=True)
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)
    eapbpawnconstant = models.IntegerField(db_column='eAPBPawnConstant', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APBPawnConstant'


class Apbsupportpages(models.Model):
    id = models.IntegerField(primary_key=True)
    sbaseurl = models.TextField(db_column='sBaseURL', blank=True, null=True)
    sinternalbrowsertitle = models.TextField(db_column='sInternalBrowserTitle', blank=True, null=True)
    sparameters = models.TextField(db_column='sParameters', blank=True, null=True)
    sregiondependanturl_inikey = models.TextField(db_column='sRegionDependantURL_INIKey', blank=True, null=True)
    eapbsupportpages = models.IntegerField(db_column='eAPBSupportPages', blank=True, null=True)
    eurlwippage = models.IntegerField(db_column='eURLWipPage', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APBSupportPages'


class Apbviewporttypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    eapbviewporttype = models.IntegerField(db_column='eAPBViewportType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APBViewportTypes'


class Activitymessageparametertypes(models.Model):
    id = models.IntegerField(primary_key=True)
    slocalisationtoken = models.TextField(db_column='sLocalisationToken', blank=True, null=True)
    eactivitymessageparametertype = models.IntegerField(db_column='eActivityMessageParameterType', blank=True, null=True)
    ndebugparam = models.IntegerField(db_column='nDebugParam', blank=True, null=True)
    econversion = models.IntegerField(db_column='eConversion', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ActivityMessageParameterTypes'


class Activitymessagepriorities(models.Model):
    id = models.IntegerField(primary_key=True)
    eactivitymessagepriority = models.IntegerField(db_column='eActivityMessagePriority', blank=True, null=True)
    fdelaymax = models.FloatField(db_column='fDelayMax', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ActivityMessagePriorities'


class Activitymessages(models.Model):
    id = models.IntegerField(primary_key=True)
    eactivitymessage = models.IntegerField(db_column='eActivityMessage', blank=True, null=True)
    ehudmessage = models.IntegerField(db_column='eHUDMessage', blank=True, null=True)
    eparamtype_0 = models.IntegerField(db_column='eParamType_0', blank=True, null=True)
    eparamtype_1 = models.IntegerField(db_column='eParamType_1', blank=True, null=True)
    eparamtype_2 = models.IntegerField(db_column='eParamType_2', blank=True, null=True)
    eparamtype_3 = models.IntegerField(db_column='eParamType_3', blank=True, null=True)
    eparamtype_4 = models.IntegerField(db_column='eParamType_4', blank=True, null=True)
    epriority = models.IntegerField(db_column='ePriority', blank=True, null=True)
    eexcludelist = models.IntegerField(db_column='eExcludeList', blank=True, null=True)
    eincludelist = models.IntegerField(db_column='eIncludeList', blank=True, null=True)
    elocation = models.IntegerField(db_column='eLocation', blank=True, null=True)
    evalidfaction = models.IntegerField(db_column='eValidFaction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ActivityMessages'


class Ammocategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    sname = models.TextField(db_column='sName', blank=True, null=True)
    snameabbreviated = models.TextField(db_column='sNameAbbreviated', blank=True, null=True)
    squantitytext = models.TextField(db_column='sQuantityText', blank=True, null=True)
    eammocategory = models.IntegerField(db_column='eAmmoCategory', blank=True, null=True)
    erequiresweaponunlocked = models.IntegerField(db_column='eRequiresWeaponUnlocked', blank=True, null=True)
    nboxcost = models.IntegerField(db_column='nBoxCost', blank=True, null=True)
    nboxsize = models.IntegerField(db_column='nBoxSize', blank=True, null=True)
    ncapacity = models.IntegerField(db_column='nCapacity', blank=True, null=True)
    ngiftedamount = models.IntegerField(db_column='nGiftedAmount', blank=True, null=True)
    npresetboxquantity_0 = models.IntegerField(db_column='nPresetBoxQuantity_0', blank=True, null=True)
    npresetboxquantity_1 = models.IntegerField(db_column='nPresetBoxQuantity_1', blank=True, null=True)
    npresetboxquantity_2 = models.IntegerField(db_column='nPresetBoxQuantity_2', blank=True, null=True)
    npresetboxquantity_3 = models.IntegerField(db_column='nPresetBoxQuantity_3', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    shudimage_bullet = models.IntegerField(db_column='sHUDImage_Bullet', blank=True, null=True)
    bthrowngrenade = models.IntegerField(db_column='bThrownGrenade', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AmmoCategories'


class AnimtreedecisionEquippeditem(models.Model):
    id = models.IntegerField(primary_key=True)
    eanimtreedecision_equippeditem = models.IntegerField(db_column='eAnimTreeDecision_EquippedItem', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AnimTreeDecision_EquippedItem'


class AnimtreedecisionVehicle(models.Model):
    id = models.IntegerField(primary_key=True)
    eanimtreedecision_vehicle = models.IntegerField(db_column='eAnimTreeDecision_Vehicle', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AnimTreeDecision_Vehicle'


class Animationdescriptors(models.Model):
    id = models.IntegerField(primary_key=True)
    eanimationdescriptor = models.IntegerField(db_column='eAnimationDescriptor', blank=True, null=True)
    fstaminadrain = models.FloatField(db_column='fStaminaDrain', blank=True, null=True)
    ercetype = models.IntegerField(db_column='eRCEType', blank=True, null=True)
    bfreezecameraloc = models.IntegerField(db_column='bFreezeCameraLoc', blank=True, null=True)
    bresetlocomotion = models.IntegerField(db_column='bResetLocomotion', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AnimationDescriptors'


class Audioamp(models.Model):
    id = models.IntegerField(primary_key=True)
    saudioswitchname = models.TextField(db_column='sAudioSwitchName', blank=True, null=True)
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)
    fvolume = models.FloatField(db_column='fVolume', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AudioAmp'


class Audiodumpvalve(models.Model):
    id = models.IntegerField(primary_key=True)
    saudioeventname = models.TextField(db_column='sAudioEventName', blank=True, null=True)
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AudioDumpValve'


class Audioengine(models.Model):
    id = models.IntegerField(primary_key=True)
    saudioeventname = models.TextField(db_column='sAudioEventName', blank=True, null=True)
    ssimulationdataset = models.TextField(db_column='sSimulationDataSet', blank=True, null=True)
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AudioEngine'


class Audioexhaust(models.Model):
    id = models.IntegerField(primary_key=True)
    saudioeventname = models.TextField(db_column='sAudioEventName', blank=True, null=True)
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AudioExhaust'


class Audioexhaustpops(models.Model):
    id = models.IntegerField(primary_key=True)
    saudioeventname = models.TextField(db_column='sAudioEventName', blank=True, null=True)
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AudioExhaustPops'


class Audiogearchange(models.Model):
    id = models.IntegerField(primary_key=True)
    saudioeventname = models.TextField(db_column='sAudioEventName', blank=True, null=True)
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AudioGearChange'


class Audiohorn(models.Model):
    id = models.IntegerField(primary_key=True)
    saudiotype = models.TextField(db_column='sAudioType', blank=True, null=True)
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)
    fpitchmodifier = models.FloatField(db_column='fPitchModifier', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AudioHorn'


class Audiosiren(models.Model):
    id = models.IntegerField(primary_key=True)
    saudiotype = models.TextField(db_column='sAudioType', blank=True, null=True)
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AudioSiren'


class Audiospeaker(models.Model):
    id = models.IntegerField(primary_key=True)
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)
    feqparameter1 = models.FloatField(db_column='fEQParameter1', blank=True, null=True)
    feqparameter2 = models.FloatField(db_column='fEQParameter2', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AudioSpeaker'


class Audiotransmission(models.Model):
    id = models.IntegerField(primary_key=True)
    saudioeventname = models.TextField(db_column='sAudioEventName', blank=True, null=True)
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)
    fpitchmodifier = models.FloatField(db_column='fPitchModifier', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AudioTransmission'


class Audioturbo(models.Model):
    id = models.IntegerField(primary_key=True)
    smainaudioeventname = models.TextField(db_column='sMainAudioEventName', blank=True, null=True)
    ssecondaudioeventname = models.TextField(db_column='sSecondAudioEventName', blank=True, null=True)
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)
    fmainpitchmodifier = models.FloatField(db_column='fMainPitchModifier', blank=True, null=True)
    fmainvolumefullrpm = models.FloatField(db_column='fMainVolumeFullRPM', blank=True, null=True)
    fmainvolumestartrpm = models.FloatField(db_column='fMainVolumeStartRPM', blank=True, null=True)
    fsecondpitchmodifier = models.FloatField(db_column='fSecondPitchModifier', blank=True, null=True)
    fsecondvolumefullrpm = models.FloatField(db_column='fSecondVolumeFullRPM', blank=True, null=True)
    fsecondvolumestartrpm = models.FloatField(db_column='fSecondVolumeStartRPM', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AudioTurbo'


class Awesomeplayerdetectionrules(models.Model):
    id = models.IntegerField(primary_key=True)
    eawesomeplayerdetectionrules = models.IntegerField(db_column='eAwesomePlayerDetectionRules', blank=True, null=True)
    ndistancesamplinginterval = models.IntegerField(db_column='nDistanceSamplingInterval', blank=True, null=True)
    ndistancesamplingintervalthreshold = models.IntegerField(db_column='nDistanceSamplingIntervalThreshold', blank=True, null=True)
    ndistancesamplingtotalthreshold = models.IntegerField(db_column='nDistanceSamplingTotalThreshold', blank=True, null=True)
    ndistrictmapallowedtime = models.IntegerField(db_column='nDistrictMapAllowedTime', blank=True, null=True)
    ntime = models.IntegerField(db_column='nTime', blank=True, null=True)
    ntimebetweenwarnings = models.IntegerField(db_column='nTimeBetweenWarnings', blank=True, null=True)
    nwarningdistrictmaptimetokick = models.IntegerField(db_column='nWarningDistrictMapTimeToKick', blank=True, null=True)
    nwarningtimetokick = models.IntegerField(db_column='nWarningTimeToKick', blank=True, null=True)
    ballcsa = models.IntegerField(db_column='bAllCSA', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AwesomePlayerDetectionRules'


class Awesomeplayerdetectionrulesevents(models.Model):
    id = models.IntegerField(primary_key=True)
    eawesomeplayerdetectionrules = models.IntegerField(db_column='eAwesomePlayerDetectionRules', blank=True, null=True)
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AwesomePlayerDetectionRulesEvents'


class Bombequipmenttypes(models.Model):
    id = models.IntegerField(primary_key=True)
    ebomblevel = models.IntegerField(db_column='eBombLevel', blank=True, null=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BombEquipmentTypes'


class Bomblevels(models.Model):
    id = models.IntegerField(primary_key=True)
    ebomblevel = models.IntegerField(db_column='eBombLevel', blank=True, null=True)
    eexplosiontype = models.IntegerField(db_column='eExplosionType', blank=True, null=True)
    nlevel = models.IntegerField(db_column='nLevel', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BombLevels'


class Budgettrackervalues(models.Model):
    id = models.IntegerField(primary_key=True)
    sbudgetcategories = models.TextField(db_column='sBudgetCategories', blank=True, null=True)
    fbudgetvalue = models.FloatField(db_column='fBudgetValue', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BudgetTrackerValues'


class CcArraypurchaseelements(models.Model):
    id = models.IntegerField(primary_key=True)
    sattributearray = models.TextField(db_column='sAttributeArray', blank=True, null=True)
    ecc_purchaseelement = models.IntegerField(db_column='eCC_PurchaseElement', blank=True, null=True)
    naddcost = models.IntegerField(db_column='nAddCost', blank=True, null=True)
    ndeletecost = models.IntegerField(db_column='nDeleteCost', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CC_ArrayPurchaseElements'


class CcPurchaseelement(models.Model):
    id = models.IntegerField(primary_key=True)
    sattributes = models.TextField(db_column='sAttributes', blank=True, null=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    ecc_purchaseelement = models.IntegerField(db_column='eCC_PurchaseElement', blank=True, null=True)
    ncost = models.IntegerField(db_column='nCost', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CC_PurchaseElement'


class Ccameramodes(models.Model):
    id = models.IntegerField(primary_key=True)
    f16_9backadjust = models.FloatField(db_column='f16_9BackAdjust', blank=True, null=True)
    f16_9crouchbackadjust = models.FloatField(db_column='f16_9CrouchBackAdjust', blank=True, null=True)
    f16_9crouchheightadjust = models.FloatField(db_column='f16_9CrouchHeightAdjust', blank=True, null=True)
    f16_9crouchrightadjust = models.FloatField(db_column='f16_9CrouchRightAdjust', blank=True, null=True)
    f16_9crouchrightadjustpitchscalar = models.FloatField(db_column='f16_9CrouchRightAdjustPitchScalar', blank=True, null=True)
    f16_9fov = models.FloatField(db_column='f16_9FOV', blank=True, null=True)
    f16_9heightadjust = models.FloatField(db_column='f16_9HeightAdjust', blank=True, null=True)
    f16_9rightadjust = models.FloatField(db_column='f16_9RightAdjust', blank=True, null=True)
    f16_9rightadjustpitchscalar = models.FloatField(db_column='f16_9RightAdjustPitchScalar', blank=True, null=True)
    f4_3backadjust = models.FloatField(db_column='f4_3BackAdjust', blank=True, null=True)
    f4_3crouchbackadjust = models.FloatField(db_column='f4_3CrouchBackAdjust', blank=True, null=True)
    f4_3crouchheightadjust = models.FloatField(db_column='f4_3CrouchHeightAdjust', blank=True, null=True)
    f4_3crouchrightadjust = models.FloatField(db_column='f4_3CrouchRightAdjust', blank=True, null=True)
    f4_3crouchrightadjustpitchscalar = models.FloatField(db_column='f4_3CrouchRightAdjustPitchScalar', blank=True, null=True)
    f4_3fov = models.FloatField(db_column='f4_3FOV', blank=True, null=True)
    f4_3heightadjust = models.FloatField(db_column='f4_3HeightAdjust', blank=True, null=True)
    f4_3rightadjust = models.FloatField(db_column='f4_3RightAdjust', blank=True, null=True)
    f4_3rightadjustpitchscalar = models.FloatField(db_column='f4_3RightAdjustPitchScalar', blank=True, null=True)
    fadjustblendspeed = models.FloatField(db_column='fAdjustBlendSpeed', blank=True, null=True)
    fcameraoriginlagspeed = models.FloatField(db_column='fCameraOriginLagSpeed', blank=True, null=True)
    fcamerarollblendspeed = models.FloatField(db_column='fCameraRollBlendSpeed', blank=True, null=True)
    fcamerarolldegrees = models.FloatField(db_column='fCameraRollDegrees', blank=True, null=True)
    fcrouchsafelocx = models.FloatField(db_column='fCrouchSafeLocX', blank=True, null=True)
    fcrouchsafelocy = models.FloatField(db_column='fCrouchSafeLocY', blank=True, null=True)
    fcrouchsafelocz = models.FloatField(db_column='fCrouchSafeLocZ', blank=True, null=True)
    ffovblendspeed = models.FloatField(db_column='fFOVBlendSpeed', blank=True, null=True)
    fsafelocx = models.FloatField(db_column='fSafeLocX', blank=True, null=True)
    fsafelocy = models.FloatField(db_column='fSafeLocY', blank=True, null=True)
    fsafelocz = models.FloatField(db_column='fSafeLocZ', blank=True, null=True)
    ecameramode = models.IntegerField(db_column='eCameraMode', blank=True, null=True)
    bcandolookbehindcam = models.IntegerField(db_column='bCanDoLookBehindCam', blank=True, null=True)
    bcrouchenabled = models.IntegerField(db_column='bCrouchEnabled', blank=True, null=True)
    busedefaultcameraadjustments = models.IntegerField(db_column='bUseDefaultCameraAdjustments', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CCameraModes'


class CsaAutoroutedata(models.Model):
    id = models.IntegerField(primary_key=True)
    ssocketname_0 = models.TextField(db_column='sSocketName_0', blank=True, null=True)
    ssocketname_1 = models.TextField(db_column='sSocketName_1', blank=True, null=True)
    ssocketname_2 = models.TextField(db_column='sSocketName_2', blank=True, null=True)
    ssocketname_3 = models.TextField(db_column='sSocketName_3', blank=True, null=True)
    ssocketname_4 = models.TextField(db_column='sSocketName_4', blank=True, null=True)
    ecsa_autoroutedata = models.IntegerField(db_column='eCSA_AutoRouteData', blank=True, null=True)
    foffsetforward = models.FloatField(db_column='fOffsetForward', blank=True, null=True)
    foffsetright = models.FloatField(db_column='fOffsetRight', blank=True, null=True)
    ealignmenttype = models.IntegerField(db_column='eAlignmentType', blank=True, null=True)
    eautoroutetype = models.IntegerField(db_column='eAutoRouteType', blank=True, null=True)
    broutealongnormal = models.IntegerField(db_column='bRouteAlongNormal', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CSA_AutoRouteData'


class CsaEatpropassociation(models.Model):
    id = models.IntegerField(primary_key=True)
    eautoroutedata = models.IntegerField(db_column='eAutoRouteData', blank=True, null=True)
    ecsa_eatpropassociation = models.IntegerField(db_column='eCSA_EATPropAssociation', blank=True, null=True)
    eequipmentanimation = models.IntegerField(db_column='eEquipmentAnimation', blank=True, null=True)
    eitemassociation = models.IntegerField(db_column='eItemAssociation', blank=True, null=True)
    epropcategory = models.IntegerField(db_column='ePropCategory', blank=True, null=True)
    bchecksuseautoroutelocation = models.IntegerField(db_column='bChecksUseAutoRouteLocation', blank=True, null=True)
    busesmallcollisionvolume = models.IntegerField(db_column='bUseSmallCollisionVolume', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CSA_EATPropAssociation'


class CsaEatvehicleassociation(models.Model):
    id = models.IntegerField(primary_key=True)
    eequipmentanimation = models.IntegerField(db_column='eEquipmentAnimation', blank=True, null=True)
    eitemassociation = models.IntegerField(db_column='eItemAssociation', blank=True, null=True)
    evehicleanimationtype = models.IntegerField(db_column='eVehicleAnimationType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CSA_EATVehicleAssociation'


class CsaEquipmentanimationtype(models.Model):
    id = models.IntegerField(primary_key=True)
    sintroanim = models.TextField(db_column='sIntroAnim', blank=True, null=True)
    smainanim1 = models.TextField(db_column='sMainAnim1', blank=True, null=True)
    smainanim2 = models.TextField(db_column='sMainAnim2', blank=True, null=True)
    smainanim3 = models.TextField(db_column='sMainAnim3', blank=True, null=True)
    soutroanim = models.TextField(db_column='sOutroAnim', blank=True, null=True)
    svfxclass = models.TextField(db_column='sVFXClass', blank=True, null=True)
    ecsa_equipmentanimationtype = models.IntegerField(db_column='eCSA_EquipmentAnimationType', blank=True, null=True)
    foutroduration = models.FloatField(db_column='fOutroDuration', blank=True, null=True)
    eoutroendpoint = models.IntegerField(db_column='eOutroEndPoint', blank=True, null=True)
    bcanmirror = models.IntegerField(db_column='bCanMirror', blank=True, null=True)
    buserootmotion = models.IntegerField(db_column='bUseRootMotion', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CSA_EquipmentAnimationType'


class CsaIatstate(models.Model):
    id = models.IntegerField(primary_key=True)
    nmaxconcurrentusersperactor = models.IntegerField(db_column='nMaxConcurrentUsersPerActor', blank=True, null=True)
    nmaxconcurrentusersperip = models.IntegerField(db_column='nMaxConcurrentUsersPerIP', blank=True, null=True)
    ecsa_iatstate = models.IntegerField(db_column='eCSA_IATState', blank=True, null=True)
    einteractiveactortype = models.IntegerField(db_column='eInteractiveActorType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CSA_IATState'


class CsaIatstateassociation(models.Model):
    id = models.IntegerField(primary_key=True)
    ecsa_iatstateassociation = models.IntegerField(db_column='eCSA_IATStateAssociation', blank=True, null=True)
    einputmapping = models.IntegerField(db_column='eInputMapping', blank=True, null=True)
    fduration = models.FloatField(db_column='fDuration', blank=True, null=True)
    nprioritylayer = models.IntegerField(db_column='nPriorityLayer', blank=True, null=True)
    econtextsensitiveaction = models.IntegerField(db_column='eContextSensitiveAction', blank=True, null=True)
    ecsa_iatstate = models.IntegerField(db_column='eCSA_IATState', blank=True, null=True)
    boverridepriority = models.IntegerField(db_column='bOverridePriority', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CSA_IATStateAssociation'


class CsaInputmapping(models.Model):
    id = models.IntegerField(primary_key=True)
    skeybinding = models.TextField(db_column='sKeyBinding', blank=True, null=True)
    ecsa_inputmapping = models.IntegerField(db_column='eCSA_InputMapping', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CSA_InputMapping'


class CsaItemassociation(models.Model):
    id = models.IntegerField(primary_key=True)
    ecsa_itemassociation = models.IntegerField(db_column='eCSA_ItemAssociation', blank=True, null=True)
    edefaultequipmentanimationtype = models.IntegerField(db_column='eDefaultEquipmentAnimationType', blank=True, null=True)
    eequipmenttype = models.IntegerField(db_column='eEquipmentType', blank=True, null=True)
    eitemassociationcategory = models.IntegerField(db_column='eItemAssociationCategory', blank=True, null=True)
    feffectivenessmodifier = models.FloatField(db_column='fEffectivenessModifier', blank=True, null=True)
    econtextsensitiveaction = models.IntegerField(db_column='eContextSensitiveAction', blank=True, null=True)
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CSA_ItemAssociation'


class CsaItemassociationcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    seffect = models.TextField(db_column='sEffect', blank=True, null=True)
    ecsa_itemassociationcategory = models.IntegerField(db_column='eCSA_ItemAssociationCategory', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CSA_ItemAssociationCategories'


class CsaTaskitemanimationset(models.Model):
    id = models.IntegerField(primary_key=True)
    sanimname = models.TextField(db_column='sAnimName', blank=True, null=True)
    ecsa_taskitemanimationset = models.IntegerField(db_column='eCSA_TaskItemAnimationSet', blank=True, null=True)
    ecsa = models.IntegerField(db_column='eCSA', blank=True, null=True)
    etaskitemsize = models.IntegerField(db_column='eTaskItemSize', blank=True, null=True)
    blogical = models.IntegerField(db_column='bLogical', blank=True, null=True)
    buseanimduration = models.IntegerField(db_column='bUseAnimDuration', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CSA_TaskItemAnimationSet'


class Cameraconstants(models.Model):
    id = models.IntegerField(primary_key=True)
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)
    ecameraconstant = models.IntegerField(db_column='eCameraConstant', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CameraConstants'


class Camerahandycampresetexported(models.Model):
    id = models.IntegerField(primary_key=True)
    ecamerahandycampreset = models.IntegerField(db_column='eCameraHandyCamPreset', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CameraHandyCamPresetExported'


class Camerahandycampresets(models.Model):
    id = models.IntegerField(primary_key=True)
    ecamerahandycampreset = models.IntegerField(db_column='eCameraHandyCamPreset', blank=True, null=True)
    einterpolateto = models.IntegerField(db_column='eInterpolateTo', blank=True, null=True)
    fchangeinmovementspeed = models.FloatField(db_column='fChangeInMovementSpeed', blank=True, null=True)
    fdelaymax = models.FloatField(db_column='fDelayMax', blank=True, null=True)
    fdelaymin = models.FloatField(db_column='fDelayMin', blank=True, null=True)
    fduration = models.FloatField(db_column='fDuration', blank=True, null=True)
    finterpolationspeedmax = models.FloatField(db_column='fInterpolationSpeedMax', blank=True, null=True)
    finterpolationspeedmin = models.FloatField(db_column='fInterpolationSpeedMin', blank=True, null=True)
    finterptodelay = models.FloatField(db_column='fInterpToDelay', blank=True, null=True)
    fmovementspeedmax = models.FloatField(db_column='fMovementSpeedMax', blank=True, null=True)
    fmovementspeedmin = models.FloatField(db_column='fMovementSpeedMin', blank=True, null=True)
    nmaxdeviationpitch = models.IntegerField(db_column='nMaxDeviationPitch', blank=True, null=True)
    nmaxdeviationroll = models.IntegerField(db_column='nMaxDeviationRoll', blank=True, null=True)
    nmaxdeviationyaw = models.IntegerField(db_column='nMaxDeviationYaw', blank=True, null=True)
    ballowactivation = models.IntegerField(db_column='bAllowActivation', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CameraHandyCamPresets'


class Cameraseatsetups(models.Model):
    id = models.IntegerField(primary_key=True)
    ecameraseatsetup = models.IntegerField(db_column='eCameraSeatSetup', blank=True, null=True)
    ffov = models.FloatField(db_column='fFOV', blank=True, null=True)
    fideallocoffset_x = models.FloatField(db_column='fIdealLocOffset_X', blank=True, null=True)
    fideallocoffset_y = models.FloatField(db_column='fIdealLocOffset_Y', blank=True, null=True)
    fideallocoffset_z = models.FloatField(db_column='fIdealLocOffset_Z', blank=True, null=True)
    fworstlocoffset_x = models.FloatField(db_column='fWorstLocOffset_X', blank=True, null=True)
    fworstlocoffset_y = models.FloatField(db_column='fWorstLocOffset_Y', blank=True, null=True)
    fworstlocoffset_z = models.FloatField(db_column='fWorstLocOffset_Z', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CameraSeatSetups'


class Camerashakepresetexported(models.Model):
    id = models.IntegerField(primary_key=True)
    ecamerashakepreset = models.IntegerField(db_column='eCameraShakePreset', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CameraShakePresetExported'


class Camerashakepresets(models.Model):
    id = models.IntegerField(primary_key=True)
    ecamerashakepreset = models.IntegerField(db_column='eCameraShakePreset', blank=True, null=True)
    fduration = models.FloatField(db_column='fDuration', blank=True, null=True)
    ffovamplitude = models.FloatField(db_column='fFOVAmplitude', blank=True, null=True)
    ffovfrequency = models.FloatField(db_column='fFOVFrequency', blank=True, null=True)
    flocationamplitudex = models.FloatField(db_column='fLocationAmplitudeX', blank=True, null=True)
    flocationamplitudey = models.FloatField(db_column='fLocationAmplitudeY', blank=True, null=True)
    flocationamplitudez = models.FloatField(db_column='fLocationAmplitudeZ', blank=True, null=True)
    flocationfrequencyx = models.FloatField(db_column='fLocationFrequencyX', blank=True, null=True)
    flocationfrequencyy = models.FloatField(db_column='fLocationFrequencyY', blank=True, null=True)
    flocationfrequencyz = models.FloatField(db_column='fLocationFrequencyZ', blank=True, null=True)
    frotationamplitudex = models.FloatField(db_column='fRotationAmplitudeX', blank=True, null=True)
    frotationamplitudey = models.FloatField(db_column='fRotationAmplitudeY', blank=True, null=True)
    frotationamplitudez = models.FloatField(db_column='fRotationAmplitudeZ', blank=True, null=True)
    frotationfrequencyx = models.FloatField(db_column='fRotationFrequencyX', blank=True, null=True)
    frotationfrequencyy = models.FloatField(db_column='fRotationFrequencyY', blank=True, null=True)
    frotationfrequencyz = models.FloatField(db_column='fRotationFrequencyZ', blank=True, null=True)
    brandomstartingfov = models.IntegerField(db_column='bRandomStartingFOV', blank=True, null=True)
    brandomstartinglocationx = models.IntegerField(db_column='bRandomStartingLocationX', blank=True, null=True)
    brandomstartinglocationy = models.IntegerField(db_column='bRandomStartingLocationY', blank=True, null=True)
    brandomstartinglocationz = models.IntegerField(db_column='bRandomStartingLocationZ', blank=True, null=True)
    brandomstartingrotationx = models.IntegerField(db_column='bRandomStartingRotationX', blank=True, null=True)
    brandomstartingrotationy = models.IntegerField(db_column='bRandomStartingRotationY', blank=True, null=True)
    brandomstartingrotationz = models.IntegerField(db_column='bRandomStartingRotationZ', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CameraShakePresets'


class Capacityitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    namount = models.IntegerField(db_column='nAmount', blank=True, null=True)
    einventoryitemcategory = models.IntegerField(db_column='eInventoryItemCategory', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CapacityItemTypes'


class Charactercustomisationoverrides(models.Model):
    id = models.IntegerField(primary_key=True)
    sfullbodymeshoverridefemale = models.TextField(db_column='sFullBodyMeshOverrideFemale', blank=True, null=True)
    sfullbodymeshoverridemale = models.TextField(db_column='sFullBodyMeshOverrideMale', blank=True, null=True)
    svfxtemplatefemale = models.TextField(db_column='sVFXTemplateFemale', blank=True, null=True)
    svfxtemplatemale = models.TextField(db_column='sVFXTemplateMale', blank=True, null=True)
    echaractercustomisationoverride = models.IntegerField(db_column='eCharacterCustomisationOverride', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CharacterCustomisationOverrides'


class Characterinteractionmenu(models.Model):
    id = models.IntegerField(primary_key=True)
    sicon = models.TextField(db_column='sIcon', blank=True, null=True)
    sid = models.TextField(db_column='sID', blank=True, null=True)
    nposition = models.IntegerField(db_column='nPosition', blank=True, null=True)
    bsamedistrict = models.IntegerField(db_column='bSameDistrict', blank=True, null=True)
    bsamefaction = models.IntegerField(db_column='bSameFaction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CharacterInteractionMenu'


class Charactermodifieritemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CharacterModifierItemTypes'


class Characterstatuses(models.Model):
    id = models.IntegerField(primary_key=True)
    estatusiconcombo = models.IntegerField(db_column='eStatusIconCombo', blank=True, null=True)
    echaracterstatus = models.IntegerField(db_column='eCharacterStatus', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CharacterStatuses'


class Charactervoipstatus(models.Model):
    id = models.IntegerField(primary_key=True)
    evoipiconcombo = models.IntegerField(db_column='eVOIPIconCombo', blank=True, null=True)
    echaractervoipstatus = models.IntegerField(db_column='eCharacterVOIPStatus', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CharacterVOIPStatus'


class Chatconstants(models.Model):
    id = models.IntegerField(primary_key=True)
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)
    echatconstant = models.IntegerField(db_column='eChatConstant', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ChatConstants'


class Chatmessagecategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    sfunctionname = models.TextField(db_column='sFunctionName', blank=True, null=True)
    ssecondaryslashcommand = models.TextField(db_column='sSecondarySlashCommand', blank=True, null=True)
    sslashcommand = models.TextField(db_column='sSlashCommand', blank=True, null=True)
    ssyntaxexample = models.TextField(db_column='sSyntaxExample', blank=True, null=True)
    stag = models.TextField(db_column='sTag', blank=True, null=True)
    efiltercolour = models.IntegerField(db_column='eFilterColour', blank=True, null=True)
    echatmessagecategory = models.IntegerField(db_column='eChatMessageCategory', blank=True, null=True)
    eworksfromstate = models.IntegerField(db_column='eWorksFromState', blank=True, null=True)
    bdisplaynotification = models.IntegerField(db_column='bDisplayNotification', blank=True, null=True)
    bhasaudionotification = models.IntegerField(db_column='bHasAudioNotification', blank=True, null=True)
    bmodepersists = models.IntegerField(db_column='bModePersists', blank=True, null=True)
    bvalidcommand = models.IntegerField(db_column='bValidCommand', blank=True, null=True)
    bvalidfilter = models.IntegerField(db_column='bValidFilter', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ChatMessageCategories'


class Chattags(models.Model):
    id = models.IntegerField(primary_key=True)
    stagtext = models.TextField(db_column='sTagText', blank=True, null=True)
    etagcolour = models.IntegerField(db_column='eTagColour', blank=True, null=True)
    npriority = models.IntegerField(db_column='nPriority', blank=True, null=True)
    echattag = models.IntegerField(db_column='eChatTag', blank=True, null=True)
    erequiredpermission = models.IntegerField(db_column='eRequiredPermission', blank=True, null=True)
    bhiddenbydefault = models.IntegerField(db_column='bHiddenByDefault', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ChatTags'


class Clanranks(models.Model):
    id = models.IntegerField(primary_key=True)
    sname = models.TextField(db_column='sName', blank=True, null=True)
    eicon = models.IntegerField(db_column='eIcon', blank=True, null=True)
    eclanrank = models.IntegerField(db_column='eClanRank', blank=True, null=True)
    bassignrank = models.IntegerField(db_column='bAssignRank', blank=True, null=True)
    bclanchatlisten = models.IntegerField(db_column='bClanChatListen', blank=True, null=True)
    bclanchatspeak = models.IntegerField(db_column='bClanChatSpeak', blank=True, null=True)
    bcontact = models.IntegerField(db_column='bContact', blank=True, null=True)
    beditclanbio = models.IntegerField(db_column='bEditClanBio', blank=True, null=True)
    beditclaninformation = models.IntegerField(db_column='bEditClanInformation', blank=True, null=True)
    beditclansymbol = models.IntegerField(db_column='bEditClanSymbol', blank=True, null=True)
    beditclantheme = models.IntegerField(db_column='bEditClanTheme', blank=True, null=True)
    beditmotd = models.IntegerField(db_column='bEditMotd', blank=True, null=True)
    beditprivatenote = models.IntegerField(db_column='bEditPrivateNote', blank=True, null=True)
    beditpublicnote = models.IntegerField(db_column='bEditPublicNote', blank=True, null=True)
    binvitemember = models.IntegerField(db_column='bInviteMember', blank=True, null=True)
    bofficerchatlisten = models.IntegerField(db_column='bOfficerChatListen', blank=True, null=True)
    bofficerchatspeak = models.IntegerField(db_column='bOfficerChatSpeak', blank=True, null=True)
    bremovemember = models.IntegerField(db_column='bRemoveMember', blank=True, null=True)
    breuseme = models.IntegerField(db_column='bReuseMe', blank=True, null=True)
    bviewprivatenote = models.IntegerField(db_column='bViewPrivateNote', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ClanRanks'


class Clothingitemcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    eclothingitemcategory = models.IntegerField(db_column='eClothingItemCategory', blank=True, null=True)
    einventoryiteminfracategory = models.IntegerField(db_column='eInventoryItemInfraCategory', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ClothingItemCategories'


class Clothingitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    sresource = models.TextField(db_column='sResource', blank=True, null=True)
    egolempart = models.IntegerField(db_column='eGolemPart', blank=True, null=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    nreeditfee = models.IntegerField(db_column='nReeditFee', blank=True, null=True)
    bfemale = models.IntegerField(db_column='bFemale', blank=True, null=True)
    bmale = models.IntegerField(db_column='bMale', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ClothingItemTypes'


class Consolecommands(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    sfunctionname = models.TextField(db_column='sFunctionName', blank=True, null=True)
    sslashcommand = models.TextField(db_column='sSlashCommand', blank=True, null=True)
    ssyntaxexample = models.TextField(db_column='sSyntaxExample', blank=True, null=True)
    econsolecommand = models.IntegerField(db_column='eConsoleCommand', blank=True, null=True)
    nmaxargcount = models.IntegerField(db_column='nMaxArgCount', blank=True, null=True)
    nminargcount = models.IntegerField(db_column='nMinArgCount', blank=True, null=True)
    ecommandtype = models.IntegerField(db_column='eCommandType', blank=True, null=True)
    epermissionrequired = models.IntegerField(db_column='ePermissionRequired', blank=True, null=True)
    eworksfromstate = models.IntegerField(db_column='eWorksFromState', blank=True, null=True)
    benabled = models.IntegerField(db_column='bEnabled', blank=True, null=True)
    bworksineditors = models.IntegerField(db_column='bWorksInEditors', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ConsoleCommands'


class Contactlevels(models.Model):
    id = models.IntegerField(primary_key=True)
    srewardmailbody = models.TextField(db_column='sRewardMailBody', blank=True, null=True)
    srewardmailsubject = models.TextField(db_column='sRewardMailSubject', blank=True, null=True)
    econtact = models.IntegerField(db_column='eContact', blank=True, null=True)
    econtactlevel = models.IntegerField(db_column='eContactLevel', blank=True, null=True)
    erewardpackage = models.IntegerField(db_column='eRewardPackage', blank=True, null=True)
    forganisationrewardmultiplier = models.FloatField(db_column='fOrganisationRewardMultiplier', blank=True, null=True)
    ncontactscore = models.IntegerField(db_column='nContactScore', blank=True, null=True)
    nlevel = models.IntegerField(db_column='nLevel', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    nstandingthreshold = models.IntegerField(db_column='nStandingThreshold', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ContactLevels'


class Contactreferrals(models.Model):
    id = models.IntegerField(primary_key=True)
    econtactlevel = models.IntegerField(db_column='eContactLevel', blank=True, null=True)
    eunlockedcontact = models.IntegerField(db_column='eUnlockedContact', blank=True, null=True)
    npartialunlockindex = models.IntegerField(db_column='nPartialUnlockIndex', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ContactReferrals'


class Contactrotationanims(models.Model):
    id = models.IntegerField(primary_key=True)
    sleftrotationanim = models.TextField(db_column='sLeftRotationAnim', blank=True, null=True)
    srightrotationanim = models.TextField(db_column='sRightRotationAnim', blank=True, null=True)
    econtactrotationanim = models.IntegerField(db_column='eContactRotationAnim', blank=True, null=True)
    nangle = models.IntegerField(db_column='nAngle', blank=True, null=True)
    nanglecutoff = models.IntegerField(db_column='nAngleCutoff', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ContactRotationAnims'


class Contacts(models.Model):
    id = models.IntegerField(primary_key=True)
    nsecondarykey = models.TextField(db_column='nSecondaryKey', blank=True, null=True)
    saudiotype = models.TextField(db_column='sAudioType', blank=True, null=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    stitle = models.TextField(db_column='sTitle', blank=True, null=True)
    econtact = models.IntegerField(db_column='eContact', blank=True, null=True)
    econtacticon = models.IntegerField(db_column='eContactIcon', blank=True, null=True)
    edistrict = models.IntegerField(db_column='eDistrict', blank=True, null=True)
    emissionpurpose = models.IntegerField(db_column='eMissionPurpose', blank=True, null=True)
    epurchaseshoptype = models.IntegerField(db_column='ePurchaseShopType', blank=True, null=True)
    npartialunlocks = models.IntegerField(db_column='nPartialUnlocks', blank=True, null=True)
    econtacttype = models.IntegerField(db_column='eContactType', blank=True, null=True)
    edealsinrewardtokenitems = models.IntegerField(db_column='eDealsInRewardTokenItems', blank=True, null=True)
    eorganisation = models.IntegerField(db_column='eOrganisation', blank=True, null=True)
    bbuyscrossorganisation = models.IntegerField(db_column='bBuysCrossOrganisation', blank=True, null=True)
    bdealsincommonitems = models.IntegerField(db_column='bDealsInCommonItems', blank=True, null=True)
    bdefaultassets = models.IntegerField(db_column='bDefaultAssets', blank=True, null=True)
    bexcludefromtrackedactivities = models.IntegerField(db_column='bExcludeFromTrackedActivities', blank=True, null=True)
    bfemale = models.IntegerField(db_column='bFemale', blank=True, null=True)
    bhidden = models.IntegerField(db_column='bHidden', blank=True, null=True)
    binitiallyunlocked = models.IntegerField(db_column='bInitiallyUnlocked', blank=True, null=True)
    bleftalignname = models.IntegerField(db_column='bLeftAlignName', blank=True, null=True)
    btest = models.IntegerField(db_column='bTest', blank=True, null=True)
    btutor = models.IntegerField(db_column='bTutor', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Contacts'


class Contextsensitiveaction(models.Model):
    id = models.IntegerField(primary_key=True)
    edefaultautoroutedata = models.IntegerField(db_column='eDefaultAutoRouteData', blank=True, null=True)
    faimdot = models.FloatField(db_column='fAimDot', blank=True, null=True)
    fcameradirectionaimdotweightingscalar = models.FloatField(db_column='fCameraDirectionAimDotWeightingScalar', blank=True, null=True)
    fdistanceweightingscalar = models.FloatField(db_column='fDistanceWeightingScalar', blank=True, null=True)
    fhorizontalserverdistanceerrormargin = models.FloatField(db_column='fHorizontalServerDistanceErrorMargin', blank=True, null=True)
    fhudhintdistance = models.FloatField(db_column='fHUDHintDistance', blank=True, null=True)
    finteractiondistance = models.FloatField(db_column='fInteractionDistance', blank=True, null=True)
    fpawndirectionaimdotweightingscalar = models.FloatField(db_column='fPawnDirectionAimDotWeightingScalar', blank=True, null=True)
    fverticalinteractiondistance = models.FloatField(db_column='fVerticalInteractionDistance', blank=True, null=True)
    fverticalserverdistanceerrormargin = models.FloatField(db_column='fVerticalServerDistanceErrorMargin', blank=True, null=True)
    nprioritylayer = models.IntegerField(db_column='nPriorityLayer', blank=True, null=True)
    econtextsensitiveaction = models.IntegerField(db_column='eContextSensitiveAction', blank=True, null=True)
    edefaultalignmenttype = models.IntegerField(db_column='eDefaultAlignmentType', blank=True, null=True)
    elinechecktype = models.IntegerField(db_column='eLineCheckType', blank=True, null=True)
    baimcheck = models.IntegerField(db_column='bAimCheck', blank=True, null=True)
    ballowwhilefalling = models.IntegerField(db_column='bAllowWhileFalling', blank=True, null=True)
    bchecksuseautoroutedata = models.IntegerField(db_column='bChecksUseAutoRouteData', blank=True, null=True)
    bdefaultlinecheck = models.IntegerField(db_column='bDefaultLineCheck', blank=True, null=True)
    bdistancecheck = models.IntegerField(db_column='bDistanceCheck', blank=True, null=True)
    bisanimationdrivenaction = models.IntegerField(db_column='bIsAnimationDrivenAction', blank=True, null=True)
    bistargetedcsa = models.IntegerField(db_column='bIsTargetedCSA', blank=True, null=True)
    blargetaskitem = models.IntegerField(db_column='bLargeTaskItem', blank=True, null=True)
    bmediumtaskitem = models.IntegerField(db_column='bMediumTaskItem', blank=True, null=True)
    bsingleinteractionpoint = models.IntegerField(db_column='bSingleInteractionPoint', blank=True, null=True)
    bsingleprogressbar = models.IntegerField(db_column='bSingleProgressBar', blank=True, null=True)
    bsmalltaskitem = models.IntegerField(db_column='bSmallTaskItem', blank=True, null=True)
    bsprintpriority = models.IntegerField(db_column='bSprintPriority', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ContextSensitiveAction'


class Contextsensitiveactionbase(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    ebegincsatutorialtrigger = models.IntegerField(db_column='eBeginCSATutorialTrigger', blank=True, null=True)
    eendcsatutorialtrigger = models.IntegerField(db_column='eEndCSATutorialTrigger', blank=True, null=True)
    eanimtype = models.IntegerField(db_column='eAnimType', blank=True, null=True)
    econtextsensitiveactionbase = models.IntegerField(db_column='eContextSensitiveActionBase', blank=True, null=True)
    einputtype = models.IntegerField(db_column='eInputType', blank=True, null=True)
    eopposingcsa = models.IntegerField(db_column='eOpposingCSA', blank=True, null=True)
    bcancelscrouch = models.IntegerField(db_column='bCancelsCrouch', blank=True, null=True)
    bcanresume = models.IntegerField(db_column='bCanResume', blank=True, null=True)
    bconsideractive = models.IntegerField(db_column='bConsiderActive', blank=True, null=True)
    bindefiniteduration = models.IntegerField(db_column='bIndefiniteDuration', blank=True, null=True)
    binterruptinventory = models.IntegerField(db_column='bInterruptInventory', blank=True, null=True)
    binvoked = models.IntegerField(db_column='bInvoked', blank=True, null=True)
    bmissioncsa = models.IntegerField(db_column='bMissionCSA', blank=True, null=True)
    bnohideweapon = models.IntegerField(db_column='bNoHideWeapon', blank=True, null=True)
    bprogressbar = models.IntegerField(db_column='bProgressBar', blank=True, null=True)
    bsmalltargetvolume = models.IntegerField(db_column='bSmallTargetVolume', blank=True, null=True)
    btimedduration = models.IntegerField(db_column='bTimedDuration', blank=True, null=True)
    bvolumecsa = models.IntegerField(db_column='bVolumeCSA', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ContextSensitiveActionBase'


class Coopcheckpointmultipliers(models.Model):
    id = models.IntegerField(primary_key=True)
    fmultiplier = models.FloatField(db_column='fMultiplier', blank=True, null=True)
    ncoopcheckpointmultipliers = models.IntegerField(db_column='nCoopCheckpointMultipliers', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CoopCheckpointMultipliers'


class Customisedassetpriorities(models.Model):
    id = models.IntegerField(primary_key=True)
    fpriority = models.FloatField(db_column='fPriority', blank=True, null=True)
    ecustomisedassetpriority = models.IntegerField(db_column='eCustomisedAssetPriority', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CustomisedAssetPriorities'


class Dailyactivities(models.Model):
    id = models.IntegerField(primary_key=True)
    edailyactivity = models.IntegerField(db_column='eDailyActivity', blank=True, null=True)
    eprobability = models.IntegerField(db_column='eProbability', blank=True, null=True)
    eredeemablereward = models.IntegerField(db_column='eRedeemableReward', blank=True, null=True)
    etrackedactivity = models.IntegerField(db_column='eTrackedActivity', blank=True, null=True)
    nrefreshtime = models.IntegerField(db_column='nRefreshTime', blank=True, null=True)
    nrequirement = models.IntegerField(db_column='nRequirement', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DailyActivities'


class Dailyactivitycontacts(models.Model):
    id = models.IntegerField(primary_key=True)
    shuddescription = models.TextField(db_column='sHUDDescription', blank=True, null=True)
    slongdescription = models.TextField(db_column='sLongDescription', blank=True, null=True)
    stitle = models.TextField(db_column='sTitle', blank=True, null=True)
    econtactlevel = models.IntegerField(db_column='eContactLevel', blank=True, null=True)
    edailyactivity = models.IntegerField(db_column='eDailyActivity', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DailyActivityContacts'


class Damageableattachmentvisuals(models.Model):
    id = models.IntegerField(primary_key=True)
    eitemattachmentvisual = models.IntegerField(db_column='eItemAttachmentVisual', blank=True, null=True)
    fcollisionarc = models.FloatField(db_column='fCollisionArc', blank=True, null=True)
    fcollisioncrouchheightoffset = models.FloatField(db_column='fCollisionCrouchHeightOffset', blank=True, null=True)
    fcollisionheightbottom = models.FloatField(db_column='fCollisionHeightBottom', blank=True, null=True)
    fcollisionheighttop = models.FloatField(db_column='fCollisionHeightTop', blank=True, null=True)
    bisrightsidecarry = models.IntegerField(db_column='bIsRightSideCarry', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DamageableAttachmentVisuals'


class Defaultcustomcolours(models.Model):
    id = models.IntegerField(primary_key=True)
    edefaultcustomcolour = models.IntegerField(db_column='eDefaultCustomColour', blank=True, null=True)
    nhue = models.IntegerField(db_column='nHue', blank=True, null=True)
    nlum = models.IntegerField(db_column='nLum', blank=True, null=True)
    nsat = models.IntegerField(db_column='nSat', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DefaultCustomColours'


class Defaultoutfititems(models.Model):
    id = models.IntegerField(primary_key=True)
    eclothingitemtype = models.IntegerField(db_column='eClothingItemType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DefaultOutfitItems'


class DefaultTodBehaviours(models.Model):
    id = models.IntegerField(primary_key=True)
    etod_event = models.IntegerField(db_column='eTOD_Event', blank=True, null=True)
    flikelihood = models.FloatField(db_column='fLikelihood', blank=True, null=True)
    ereaction = models.IntegerField(db_column='eReaction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Default_TOD_Behaviours'


class Designerconstants(models.Model):
    id = models.IntegerField(primary_key=True)
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DesignerConstants'


class Designerconstants2(models.Model):
    id = models.IntegerField(primary_key=True)
    scomment = models.TextField(db_column='sComment', blank=True, null=True)
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)
    edesignerconstant2 = models.IntegerField(db_column='eDesignerConstant2', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DesignerConstants2'


class Displaypoint(models.Model):
    id = models.IntegerField(primary_key=True)
    nsecondarykey = models.TextField(db_column='nSecondaryKey', blank=True, null=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    sobtainedby = models.TextField(db_column='sObtainedBy', blank=True, null=True)
    sscreenshot = models.TextField(db_column='sScreenShot', blank=True, null=True)
    sshorttitle = models.TextField(db_column='sShortTitle', blank=True, null=True)
    stitle = models.TextField(db_column='sTitle', blank=True, null=True)
    edisplaypoint = models.IntegerField(db_column='eDisplayPoint', blank=True, null=True)
    edistrict = models.IntegerField(db_column='eDistrict', blank=True, null=True)
    eactivationtype = models.IntegerField(db_column='eActivationType', blank=True, null=True)
    etype = models.IntegerField(db_column='eType', blank=True, null=True)
    bcriminal = models.IntegerField(db_column='bCriminal', blank=True, null=True)
    benforcer = models.IntegerField(db_column='bEnforcer', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DisplayPoint'


class Districtblocks(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    edistrict = models.IntegerField(db_column='eDistrict', blank=True, null=True)
    edistrictblock = models.IntegerField(db_column='eDistrictBlock', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    themes_0 = models.IntegerField(db_column='Themes_0', blank=True, null=True)
    themes_1 = models.IntegerField(db_column='Themes_1', blank=True, null=True)
    themes_2 = models.IntegerField(db_column='Themes_2', blank=True, null=True)
    themes_3 = models.IntegerField(db_column='Themes_3', blank=True, null=True)
    themes_4 = models.IntegerField(db_column='Themes_4', blank=True, null=True)
    themes_5 = models.IntegerField(db_column='Themes_5', blank=True, null=True)
    themes_6 = models.IntegerField(db_column='Themes_6', blank=True, null=True)
    themes_7 = models.IntegerField(db_column='Themes_7', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DistrictBlocks'


class Districtinstancetype(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    edistrict = models.IntegerField(db_column='eDistrict', blank=True, null=True)
    edistrictinstancetype = models.IntegerField(db_column='eDistrictInstanceType', blank=True, null=True)
    edistrictlanguage = models.IntegerField(db_column='eDistrictLanguage', blank=True, null=True)
    edistrictrating = models.IntegerField(db_column='eDistrictRating', blank=True, null=True)
    edistrictruleset = models.IntegerField(db_column='eDistrictRuleSet', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DistrictInstanceType'


class Districtlanguage(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    slanguageshortname = models.TextField(db_column='sLanguageShortName', blank=True, null=True)
    slocalisationini = models.TextField(db_column='sLocalisationINI', blank=True, null=True)
    edistrictlanguage = models.IntegerField(db_column='eDistrictLanguage', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DistrictLanguage'


class Districtrating(models.Model):
    id = models.IntegerField(primary_key=True)
    edistrictrating = models.IntegerField(db_column='eDistrictRating', blank=True, null=True)
    nmaxrating = models.IntegerField(db_column='nMaxRating', blank=True, null=True)
    nminrating = models.IntegerField(db_column='nMinRating', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DistrictRating'


class Districtrulesets(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    edistrictruleset = models.IntegerField(db_column='eDistrictRuleSet', blank=True, null=True)
    emissiontypefilter_0 = models.IntegerField(db_column='eMissionTypeFilter_0', blank=True, null=True)
    emissiontypefilter_1 = models.IntegerField(db_column='eMissionTypeFilter_1', blank=True, null=True)
    fmaximumtoohightime = models.FloatField(db_column='fMaximumTooHighTime', blank=True, null=True)
    freticuletargetingdistance = models.FloatField(db_column='fReticuleTargetingDistance', blank=True, null=True)
    fscoreunopposedmultiplier = models.FloatField(db_column='fScoreUnopposedMultiplier', blank=True, null=True)
    fwscharinfodistance = models.FloatField(db_column='fWSCharInfoDistance', blank=True, null=True)
    nmissiondelay = models.IntegerField(db_column='nMissionDelay', blank=True, null=True)
    nnewmissioncooldowntimer = models.IntegerField(db_column='nNewMissionCooldownTimer', blank=True, null=True)
    echaractercollideswithcharacter = models.IntegerField(db_column='eCharacterCollidesWithCharacter', blank=True, null=True)
    edistricttypeinfo = models.IntegerField(db_column='eDistrictTypeInfo', blank=True, null=True)
    eheatfunctionality = models.IntegerField(db_column='eHeatFunctionality', blank=True, null=True)
    epvpdamage = models.IntegerField(db_column='ePvPDamage', blank=True, null=True)
    etutorialbypassbehaviour = models.IntegerField(db_column='eTutorialBypassBehaviour', blank=True, null=True)
    eweapontypeset = models.IntegerField(db_column='eWeaponTypeSet', blank=True, null=True)
    ewitnessingfunctionality = models.IntegerField(db_column='eWitnessingFunctionality', blank=True, null=True)
    ewitnessingmissionsystem = models.IntegerField(db_column='eWitnessingMissionSystem', blank=True, null=True)
    ballowbackupcall = models.IntegerField(db_column='bAllowBackupCall', blank=True, null=True)
    ballowfnmods = models.IntegerField(db_column='bAllowFnMods', blank=True, null=True)
    balwaysaccessinventory = models.IntegerField(db_column='bAlwaysAccessInventory', blank=True, null=True)
    bbountiesavailable = models.IntegerField(db_column='bBountiesAvailable', blank=True, null=True)
    bcontactreferralson = models.IntegerField(db_column='bContactReferralsOn', blank=True, null=True)
    bcustomisationlimiter = models.IntegerField(db_column='bCustomisationLimiter', blank=True, null=True)
    bdistinguishfactionnamecolours = models.IntegerField(db_column='bDistinguishFactionNameColours', blank=True, null=True)
    bdobuildingchecks = models.IntegerField(db_column='bDoBuildingChecks', blank=True, null=True)
    bdropweapons = models.IntegerField(db_column='bDropWeapons', blank=True, null=True)
    bhudshowradarpings = models.IntegerField(db_column='bHUDShowRadarPings', blank=True, null=True)
    bincompletetutorialavailable = models.IntegerField(db_column='bIncompleteTutorialAvailable', blank=True, null=True)
    bminigamesavailable = models.IntegerField(db_column='bMinigamesAvailable', blank=True, null=True)
    bmissionoffers = models.IntegerField(db_column='bMissionOffers', blank=True, null=True)
    bnoskillrating = models.IntegerField(db_column='bNoSkillRating', blank=True, null=True)
    bofferautogroup = models.IntegerField(db_column='bOfferAutoGroup', blank=True, null=True)
    brelease = models.IntegerField(db_column='bRelease', blank=True, null=True)
    bshowthreatandrank = models.IntegerField(db_column='bShowThreatAndRank', blank=True, null=True)
    busemasterspawnzoneonly = models.IntegerField(db_column='bUseMasterSpawnZoneOnly', blank=True, null=True)
    bwscharinfousesradarpings = models.IntegerField(db_column='bWSCharInfoUsesRadarPings', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DistrictRuleSets'


class Districttypes(models.Model):
    id = models.IntegerField(primary_key=True)
    edistricttype = models.IntegerField(db_column='eDistrictType', blank=True, null=True)
    efactionallowed = models.IntegerField(db_column='eFactionAllowed', blank=True, null=True)
    bissocial = models.IntegerField(db_column='bIsSocial', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DistrictTypes'


class Districts(models.Model):
    id = models.IntegerField(primary_key=True)
    saudiobanks = models.TextField(db_column='sAudioBanks', blank=True, null=True)
    saudioreflectiondata = models.TextField(db_column='sAudioReflectionData', blank=True, null=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    sdiffusetexture = models.TextField(db_column='sDiffuseTexture', blank=True, null=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    sdistancefieldtexture = models.TextField(db_column='sDistanceFieldTexture', blank=True, null=True)
    sdistrictmap = models.TextField(db_column='sDistrictMap', blank=True, null=True)
    eawesomeplayerdetectionrules = models.IntegerField(db_column='eAwesomePlayerDetectionRules', blank=True, null=True)
    ecriminalorganisationcontact = models.IntegerField(db_column='eCriminalOrganisationContact', blank=True, null=True)
    edefaultdistrictinstancetype = models.IntegerField(db_column='eDefaultDistrictInstanceType', blank=True, null=True)
    edistrict = models.IntegerField(db_column='eDistrict', blank=True, null=True)
    eenforcerorganisationcontact = models.IntegerField(db_column='eEnforcerOrganisationContact', blank=True, null=True)
    etutorialdistrictinstancetype = models.IntegerField(db_column='eTutorialDistrictInstanceType', blank=True, null=True)
    fmaxsafeheight = models.FloatField(db_column='fMaxSafeHeight', blank=True, null=True)
    fnmaxdistancetopedestriandestroynode = models.FloatField(db_column='fnMaxDistanceToPedestrianDestroyNode', blank=True, null=True)
    fuiinactivitytimeout = models.FloatField(db_column='fUIInactivityTimeout', blank=True, null=True)
    ncentrex = models.IntegerField(db_column='nCentreX', blank=True, null=True)
    ncentrey = models.IntegerField(db_column='nCentreY', blank=True, null=True)
    ndiameter = models.IntegerField(db_column='nDiameter', blank=True, null=True)
    nnumcollectables = models.IntegerField(db_column='nNumCollectables', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    edistricttype = models.IntegerField(db_column='eDistrictType', blank=True, null=True)
    espawnvariable = models.IntegerField(db_column='eSpawnVariable', blank=True, null=True)
    breleasedistrict = models.IntegerField(db_column='bReleaseDistrict', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Districts'


class Dynamicmenuentries(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplaypicture = models.TextField(db_column='sDisplayPicture', blank=True, null=True)
    sdisplaytext = models.TextField(db_column='sDisplayText', blank=True, null=True)
    slistid = models.TextField(db_column='sListID', blank=True, null=True)
    sremoteevent = models.TextField(db_column='sRemoteEvent', blank=True, null=True)
    swwiseswitch = models.TextField(db_column='sWwiseSwitch', blank=True, null=True)
    edynamicmenuentry = models.IntegerField(db_column='eDynamicMenuEntry', blank=True, null=True)
    ecustomisationmode = models.IntegerField(db_column='eCustomisationMode', blank=True, null=True)
    egender = models.IntegerField(db_column='eGender', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DynamicMenuEntries'


class Emotecommands(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    spackageref = models.TextField(db_column='sPackageRef', blank=True, null=True)
    sslashcommand = models.TextField(db_column='sSlashCommand', blank=True, null=True)
    eemotecommand = models.IntegerField(db_column='eEmoteCommand', blank=True, null=True)
    bkickcheckenabled = models.IntegerField(db_column='bKickCheckEnabled', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EmoteCommands'


class Encumbrances(models.Model):
    id = models.IntegerField(primary_key=True)
    nuiencumbrancelevel = models.IntegerField(db_column='nUIEncumbranceLevel', blank=True, null=True)
    eencumbrance = models.IntegerField(db_column='eEncumbrance', blank=True, null=True)
    bcancrouchmove = models.IntegerField(db_column='bCanCrouchMove', blank=True, null=True)
    bcanjump = models.IntegerField(db_column='bCanJump', blank=True, null=True)
    bcanrun = models.IntegerField(db_column='bCanRun', blank=True, null=True)
    bcansprint = models.IntegerField(db_column='bCanSprint', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Encumbrances'


class Equipmentcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    eequipmentcategory = models.IntegerField(db_column='eEquipmentCategory', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EquipmentCategories'


class Equipmenttypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    eequipmentcategory = models.IntegerField(db_column='eEquipmentCategory', blank=True, null=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    eitemattachment = models.IntegerField(db_column='eItemAttachment', blank=True, null=True)
    fdurationofuse = models.IntegerField(db_column='fDurationOfUse', blank=True, null=True)
    ngradeordinal = models.IntegerField(db_column='nGradeOrdinal', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EquipmentTypes'


class Errorcode(models.Model):
    id = models.IntegerField(primary_key=True)
    ndummy = models.IntegerField(db_column='nDummy', blank=True, null=True)
    eerrorcode = models.IntegerField(db_column='eErrorCode', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ErrorCode'


class Explosions(models.Model):
    id = models.IntegerField(primary_key=True)
    saudiotype = models.TextField(db_column='sAudioType', blank=True, null=True)
    svfxasset = models.TextField(db_column='sVFXAsset', blank=True, null=True)
    svfxasset_airburst = models.TextField(db_column='sVFXAsset_Airburst', blank=True, null=True)
    ecamerashake = models.IntegerField(db_column='eCameraShake', blank=True, null=True)
    eexplosion = models.IntegerField(db_column='eExplosion', blank=True, null=True)
    fexplosionradius = models.FloatField(db_column='fExplosionRadius', blank=True, null=True)
    fgroundzeroradius = models.FloatField(db_column='fGroundZeroRadius', blank=True, null=True)
    fharddamagemodifier = models.FloatField(db_column='fHardDamageModifier', blank=True, null=True)
    fimpulsezmax = models.FloatField(db_column='fImpulseZMax', blank=True, null=True)
    fimpulsezmin = models.FloatField(db_column='fImpulseZMin', blank=True, null=True)
    flifetimemaxdamagetime = models.FloatField(db_column='fLifetimeMaxDamageTime', blank=True, null=True)
    flifetimemindamagepercentage = models.FloatField(db_column='fLifetimeMinDamagePercentage', blank=True, null=True)
    fminimumdamagepercentage = models.FloatField(db_column='fMinimumDamagePercentage', blank=True, null=True)
    fragdollradialimpulse = models.FloatField(db_column='fRagdollRadialImpulse', blank=True, null=True)
    fsoftdamagemodifier = models.FloatField(db_column='fSoftDamageModifier', blank=True, null=True)
    ndamage = models.IntegerField(db_column='nDamage', blank=True, null=True)
    nstundamage = models.IntegerField(db_column='nStunDamage', blank=True, null=True)
    enpcworldevent = models.IntegerField(db_column='eNPCWorldEvent', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Explosions'


class Fxmaterialimpacts(models.Model):
    id = models.IntegerField(primary_key=True)
    sexplosiveimpactvfx = models.TextField(db_column='sExplosiveImpactVFX', blank=True, null=True)
    sheavyexitvfx = models.TextField(db_column='sHeavyExitVFX', blank=True, null=True)
    sheavyfootfallvfx = models.TextField(db_column='sHeavyFootfallVFX', blank=True, null=True)
    sheavyimpactvfx = models.TextField(db_column='sHeavyImpactVFX', blank=True, null=True)
    slightfootfallvfx = models.TextField(db_column='sLightFootfallVFX', blank=True, null=True)
    smaterialdescription = models.TextField(db_column='sMaterialDescription', blank=True, null=True)
    smediumexitvfx = models.TextField(db_column='sMediumExitVFX', blank=True, null=True)
    smediumfootfallvfx = models.TextField(db_column='sMediumFootfallVFX', blank=True, null=True)
    smediumimpactvfx = models.TextField(db_column='sMediumImpactVFX', blank=True, null=True)
    smeleeimpactvfx = models.TextField(db_column='sMeleeImpactVFX', blank=True, null=True)
    snonlethalimpactvfx = models.TextField(db_column='sNonLethalImpactVFX', blank=True, null=True)
    srbcollisionlargevfx = models.TextField(db_column='sRBCollisionLargeVFX', blank=True, null=True)
    srbcollisionsmallvfx = models.TextField(db_column='sRBCollisionSmallVFX', blank=True, null=True)
    srbcollisionvfx = models.TextField(db_column='sRBCollisionVFX', blank=True, null=True)
    srbscrapevfx = models.TextField(db_column='sRBScrapeVFX', blank=True, null=True)
    sshotimpactvfx = models.TextField(db_column='sShotImpactVFX', blank=True, null=True)
    ssmallexitvfx = models.TextField(db_column='sSmallExitVFX', blank=True, null=True)
    ssmallimpactvfx = models.TextField(db_column='sSmallImpactVFX', blank=True, null=True)
    swheelsmokevfx = models.TextField(db_column='sWheelSmokeVFX', blank=True, null=True)
    fhardnesslower = models.FloatField(db_column='fHardnessLower', blank=True, null=True)
    fhardnessupper = models.FloatField(db_column='fHardnessUpper', blank=True, null=True)
    efxmaterialimpact = models.IntegerField(db_column='eFXMaterialImpact', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FXMaterialImpacts'


class Facialhairrandomgeneration(models.Model):
    id = models.IntegerField(primary_key=True)
    fprobability = models.FloatField(db_column='fProbability', blank=True, null=True)
    efacialhairrandomgeneration = models.IntegerField(db_column='eFacialHairRandomGeneration', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FacialHairRandomGeneration'


class Factionrestrictedlocations(models.Model):
    id = models.IntegerField(primary_key=True)
    efactionrestrictedlocation = models.IntegerField(db_column='eFactionRestrictedLocation', blank=True, null=True)
    npadding_ignore_me = models.IntegerField(db_column='nPadding_Ignore_Me', blank=True, null=True)
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FactionRestrictedLocations'


class Factions(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    sfactioninfodescription = models.TextField(db_column='sFactionInfoDescription', blank=True, null=True)
    sfactioninfodisplayname = models.TextField(db_column='sFactionInfoDisplayName', blank=True, null=True)
    sskinname = models.TextField(db_column='sSkinName', blank=True, null=True)
    espawnzonemarker = models.IntegerField(db_column='eSpawnZoneMarker', blank=True, null=True)
    evolumecolour = models.IntegerField(db_column='eVolumeColour', blank=True, null=True)
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    @property_cache
    def name(self):
        return self.sdisplayname

    class Meta:
        managed = False
        db_table = 'Factions'


class Feedbackmessages(models.Model):
    id = models.IntegerField(primary_key=True)
    sfeedbackmessage = models.TextField(db_column='sFeedbackMessage', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    efeedbackmessage = models.IntegerField(db_column='eFeedbackMessage', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FeedbackMessages'


class Fireoffsets(models.Model):
    id = models.IntegerField(primary_key=True)
    fforwards = models.FloatField(db_column='fForwards', blank=True, null=True)
    fright = models.FloatField(db_column='fRight', blank=True, null=True)
    fup = models.FloatField(db_column='fUp', blank=True, null=True)
    efireoffset = models.IntegerField(db_column='eFireOffset', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FireOffsets'


class Gameflowdialogs(models.Model):
    id = models.IntegerField(primary_key=True)
    sbutton1label = models.TextField(db_column='sButton1Label', blank=True, null=True)
    sbutton2label = models.TextField(db_column='sButton2Label', blank=True, null=True)
    sbutton3label = models.TextField(db_column='sButton3Label', blank=True, null=True)
    splayerclass = models.TextField(db_column='sPlayerClass', blank=True, null=True)
    stitle = models.TextField(db_column='sTitle', blank=True, null=True)
    ebutton1result = models.IntegerField(db_column='eButton1Result', blank=True, null=True)
    ebutton2result = models.IntegerField(db_column='eButton2Result', blank=True, null=True)
    ebutton3result = models.IntegerField(db_column='eButton3Result', blank=True, null=True)
    ecancelresult = models.IntegerField(db_column='eCancelResult', blank=True, null=True)
    edefaultbutton = models.IntegerField(db_column='eDefaultButton', blank=True, null=True)
    escaleforminterface = models.IntegerField(db_column='eScaleformInterface', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GameFlowDialogs'


class Gameplayeventcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sactivitymessageparameter4comment = models.TextField(db_column='sActivityMessageParameter4Comment', blank=True, null=True)
    ndummy = models.IntegerField(db_column='nDummy', blank=True, null=True)
    egameplayeventcategory = models.IntegerField(db_column='eGameplayEventCategory', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GameplayEventCategories'


class Gameplayeventcategories2(models.Model):
    id = models.IntegerField(primary_key=True)
    sactivitymessageparameter4comment = models.TextField(db_column='sActivityMessageParameter4Comment', blank=True, null=True)
    ndummy = models.IntegerField(db_column='nDummy', blank=True, null=True)
    egameplayeventcategory2 = models.IntegerField(db_column='eGameplayEventCategory2', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GameplayEventCategories2'


class GameplayeventInventoryoperation(models.Model):
    id = models.IntegerField(primary_key=True)
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)
    echildrule = models.IntegerField(db_column='eChildRule', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GameplayEvent_InventoryOperation'


class GameplayeventMissions(models.Model):
    id = models.IntegerField(primary_key=True)
    echildrule = models.IntegerField(db_column='eChildRule', blank=True, null=True)
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GameplayEvent_Missions'


class GameplayeventTasktargets(models.Model):
    id = models.IntegerField(primary_key=True)
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)
    echildrule = models.IntegerField(db_column='eChildRule', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GameplayEvent_TaskTargets'


class GameplayeventVehiclehealth(models.Model):
    id = models.IntegerField(primary_key=True)
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)
    echildrule = models.IntegerField(db_column='eChildRule', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GameplayEvent_VehicleHealth'


class Gameplayevents(models.Model):
    id = models.IntegerField(primary_key=True)
    eactivitymessage_0 = models.IntegerField(db_column='eActivityMessage_0', blank=True, null=True)
    eactivitymessage_1 = models.IntegerField(db_column='eActivityMessage_1', blank=True, null=True)
    eactivitymessage_2 = models.IntegerField(db_column='eActivityMessage_2', blank=True, null=True)
    eactivitymessageonreward = models.IntegerField(db_column='eActivityMessageOnReward', blank=True, null=True)
    edisabledrulesets = models.IntegerField(db_column='eDisabledRuleSets', blank=True, null=True)
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)
    ehelppopup = models.IntegerField(db_column='eHelpPopup', blank=True, null=True)
    emissionsystems = models.IntegerField(db_column='eMissionSystems', blank=True, null=True)
    eobject = models.IntegerField(db_column='eObject', blank=True, null=True)
    eobjectset = models.IntegerField(db_column='eObjectSet', blank=True, null=True)
    eobjectstateset = models.IntegerField(db_column='eObjectStateSet', blank=True, null=True)
    eresultantheatchange = models.IntegerField(db_column='eResultantHeatChange', blank=True, null=True)
    eresultantwitnessablecrime = models.IntegerField(db_column='eResultantWitnessableCrime', blank=True, null=True)
    eresultantwitnessablecrimeend = models.IntegerField(db_column='eResultantWitnessableCrimeEnd', blank=True, null=True)
    etrackedactivity = models.IntegerField(db_column='eTrackedActivity', blank=True, null=True)
    fexpiryperiod = models.FloatField(db_column='fExpiryPeriod', blank=True, null=True)
    na = models.IntegerField(db_column='nA', blank=True, null=True)
    nb = models.IntegerField(db_column='nB', blank=True, null=True)
    nprecedence = models.IntegerField(db_column='nPrecedence', blank=True, null=True)
    ecsa = models.IntegerField(db_column='eCSA', blank=True, null=True)
    eexcludelist = models.IntegerField(db_column='eExcludeList', blank=True, null=True)
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)
    egameplayeventcategory = models.IntegerField(db_column='eGameplayEventCategory', blank=True, null=True)
    egameplayeventcategory2 = models.IntegerField(db_column='eGameplayEventCategory2', blank=True, null=True)
    eincludelist = models.IntegerField(db_column='eIncludeList', blank=True, null=True)
    emutuallyexclusive = models.IntegerField(db_column='eMutuallyExclusive', blank=True, null=True)
    epvp = models.IntegerField(db_column='ePvP', blank=True, null=True)
    eresultantreward = models.IntegerField(db_column='eResultantReward', blank=True, null=True)
    brequirea = models.IntegerField(db_column='bRequireA', blank=True, null=True)
    brequireb = models.IntegerField(db_column='bRequireB', blank=True, null=True)
    bresettrackedactivity = models.IntegerField(db_column='bResetTrackedActivity', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GameplayEvents'


class GameplayeventsModetimer(models.Model):
    id = models.IntegerField(primary_key=True)
    echildrule = models.IntegerField(db_column='eChildRule', blank=True, null=True)
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GameplayEvents_ModeTimer'


class Gameplaymodetimertypes(models.Model):
    id = models.IntegerField(primary_key=True)
    edistrictruleset = models.IntegerField(db_column='eDistrictRuleSet', blank=True, null=True)
    egameplaymodetimertype = models.IntegerField(db_column='eGameplayModeTimerType', blank=True, null=True)
    balive = models.IntegerField(db_column='bAlive', blank=True, null=True)
    bcharactereditor = models.IntegerField(db_column='bCharacterEditor', blank=True, null=True)
    bclothingeditor = models.IntegerField(db_column='bClothingEditor', blank=True, null=True)
    bdirectedmission = models.IntegerField(db_column='bDirectedMission', blank=True, null=True)
    bmaxheat = models.IntegerField(db_column='bMaxHeat', blank=True, null=True)
    bmusiceditor = models.IntegerField(db_column='bMusicEditor', blank=True, null=True)
    bnotineditor = models.IntegerField(db_column='bNotInEditor', blank=True, null=True)
    botherpvp = models.IntegerField(db_column='bOtherPvP', blank=True, null=True)
    bsymboleditor = models.IntegerField(db_column='bSymbolEditor', blank=True, null=True)
    btotal = models.IntegerField(db_column='bTotal', blank=True, null=True)
    bvehicleeditor = models.IntegerField(db_column='bVehicleEditor', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GameplayModeTimerTypes'


class Gameplayobjectsets(models.Model):
    id = models.IntegerField(primary_key=True)
    egameplayobjectset = models.IntegerField(db_column='eGameplayObjectSet', blank=True, null=True)
    ndummy = models.IntegerField(blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GameplayObjectSets'


class Gameplayobjects(models.Model):
    id = models.IntegerField(primary_key=True)
    egameplayobject = models.IntegerField(db_column='eGameplayObject', blank=True, null=True)
    ememberof_0 = models.IntegerField(db_column='eMemberOf_0', blank=True, null=True)
    ememberof_1 = models.IntegerField(db_column='eMemberOf_1', blank=True, null=True)
    ememberof_2 = models.IntegerField(db_column='eMemberOf_2', blank=True, null=True)
    ememberof_3 = models.IntegerField(db_column='eMemberOf_3', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GameplayObjects'


class Gameplayobjectsfixed(models.Model):
    id = models.IntegerField(primary_key=True)
    egameplayobject = models.IntegerField(db_column='eGameplayObject', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GameplayObjectsFixed'


class Gameplaystatesets(models.Model):
    id = models.IntegerField(primary_key=True)
    egameplaystateset = models.IntegerField(db_column='eGameplayStateSet', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GameplayStateSets'


class Gameplaystates(models.Model):
    id = models.IntegerField(primary_key=True)
    ememberof_0 = models.IntegerField(db_column='eMemberOf_0', blank=True, null=True)
    ememberof_1 = models.IntegerField(db_column='eMemberOf_1', blank=True, null=True)
    ememberof_2 = models.IntegerField(db_column='eMemberOf_2', blank=True, null=True)
    ememberof_3 = models.IntegerField(db_column='eMemberOf_3', blank=True, null=True)
    egameplaystate = models.IntegerField(db_column='eGameplayState', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GameplayStates'


class Gameplayvehiclehealthranges(models.Model):
    id = models.IntegerField(primary_key=True)
    nhealthmax = models.IntegerField(db_column='nHealthMax', blank=True, null=True)
    nhealthmin = models.IntegerField(db_column='nHealthMin', blank=True, null=True)
    egameplayvehiclehealthrange = models.IntegerField(db_column='eGameplayVehicleHealthRange', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GameplayVehicleHealthRanges'


class Golempartclasses(models.Model):
    id = models.IntegerField(primary_key=True)
    egolempartclass = models.IntegerField(db_column='eGolemPartClass', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    bcoversbreasts = models.IntegerField(db_column='bCoversBreasts', blank=True, null=True)
    bcoversgenitalia = models.IntegerField(db_column='bCoversGenitalia', blank=True, null=True)
    buseinclothingpreview = models.IntegerField(db_column='bUseInClothingPreview', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GolemPartClasses'


class Golemparts(models.Model):
    id = models.IntegerField(primary_key=True)
    sgolempart = models.TextField(db_column='sGolemPart', blank=True, null=True)
    susername = models.TextField(db_column='sUsername', blank=True, null=True)
    eclass = models.IntegerField(db_column='eClass', blank=True, null=True)
    eclothingitemcategory = models.IntegerField(db_column='eClothingItemCategory', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    nversatility = models.IntegerField(db_column='nVersatility', blank=True, null=True)
    bstartup = models.IntegerField(db_column='bStartup', blank=True, null=True)
    btestasset = models.IntegerField(db_column='bTestAsset', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GolemParts'


class Graffitidisplaypoint(models.Model):
    id = models.IntegerField(primary_key=True)
    edisplaypoint = models.IntegerField(db_column='eDisplayPoint', blank=True, null=True)
    fspraydurationoverride = models.FloatField(db_column='fSprayDurationOverride', blank=True, null=True)
    einteractiontype = models.IntegerField(db_column='eInteractionType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GraffitiDisplayPoint'


class Grenadeweapontype(models.Model):
    id = models.IntegerField(primary_key=True)
    erecoil = models.IntegerField(db_column='eRecoil', blank=True, null=True)
    eweaponprojectile = models.IntegerField(db_column='eWeaponProjectile', blank=True, null=True)
    eweapontype = models.IntegerField(db_column='eWeaponType', blank=True, null=True)
    ffiringspeed = models.FloatField(db_column='fFiringSpeed', blank=True, null=True)
    fmaxangleadded = models.FloatField(db_column='fMaxAngleAdded', blank=True, null=True)
    fpinpulltime = models.FloatField(db_column='fPinPullTime', blank=True, null=True)
    fthrowtime = models.FloatField(db_column='fThrowTime', blank=True, null=True)
    baffectedbygravity = models.IntegerField(db_column='bAffectedByGravity', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GrenadeWeaponType'


class Hudceremonymsg(models.Model):
    id = models.IntegerField(primary_key=True)
    stitle = models.TextField(db_column='sTitle', blank=True, null=True)
    ehudmessage = models.IntegerField(db_column='eHUDMessage', blank=True, null=True)
    eiconfallback = models.IntegerField(db_column='eIconFallback', blank=True, null=True)
    etitlebgcolour = models.IntegerField(db_column='eTitleBGColour', blank=True, null=True)
    etype = models.IntegerField(db_column='eType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDCeremonyMsg'


class Hudcolour(models.Model):
    id = models.IntegerField(primary_key=True)
    ehudcolour = models.IntegerField(db_column='eHUDColour', blank=True, null=True)
    eoverridecolour = models.IntegerField(db_column='eOverrideColour', blank=True, null=True)
    na = models.IntegerField(db_column='nA', blank=True, null=True)
    nb = models.IntegerField(db_column='nB', blank=True, null=True)
    ng = models.IntegerField(db_column='nG', blank=True, null=True)
    nr = models.IntegerField(db_column='nR', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDColour'


class Hudcolourprofiles(models.Model):
    id = models.IntegerField(primary_key=True)
    ehudcolourprofile = models.IntegerField(db_column='eHUDColourProfile', blank=True, null=True)
    eprimarycolour = models.IntegerField(db_column='ePrimaryColour', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDColourProfiles'


class Hudcombatmessages(models.Model):
    id = models.IntegerField(primary_key=True)
    sline0 = models.TextField(db_column='sLine0', blank=True, null=True)
    sline1 = models.TextField(db_column='sLine1', blank=True, null=True)
    sline2 = models.TextField(db_column='sLine2', blank=True, null=True)
    ehudmessage = models.IntegerField(db_column='eHUDMessage', blank=True, null=True)
    eicon = models.IntegerField(db_column='eIcon', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDCombatMessages'


class Hudconstantbools(models.Model):
    id = models.IntegerField(primary_key=True)
    scomment = models.TextField(db_column='sComment', blank=True, null=True)
    ehudconstantbool = models.IntegerField(db_column='eHUDConstantBool', blank=True, null=True)
    bvalue = models.IntegerField(db_column='bValue', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDConstantBools'


class Hudconstantstring(models.Model):
    id = models.IntegerField(primary_key=True)
    scomment = models.TextField(db_column='sComment', blank=True, null=True)
    stext = models.TextField(db_column='sText', blank=True, null=True)
    ehudconstantstring = models.IntegerField(db_column='eHUDConstantString', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDConstantString'


class Hudconstants(models.Model):
    id = models.IntegerField(primary_key=True)
    scomment = models.TextField(db_column='sComment', blank=True, null=True)
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)
    ehudconstant = models.IntegerField(db_column='eHUDConstant', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDConstants'


class Huddistrictmapmarker(models.Model):
    id = models.IntegerField(primary_key=True)
    slegendname = models.TextField(db_column='sLegendName', blank=True, null=True)
    ehuddistrictmapmarker = models.IntegerField(db_column='eHUDDistrictMapMarker', blank=True, null=True)
    eiconcombo = models.IntegerField(db_column='eIconCombo', blank=True, null=True)
    fmaxvisibledistance = models.FloatField(db_column='fMaxVisibleDistance', blank=True, null=True)
    ndraworder = models.IntegerField(db_column='nDrawOrder', blank=True, null=True)
    nsize = models.IntegerField(db_column='nSize', blank=True, null=True)
    bdisablewaypoints = models.IntegerField(db_column='bDisableWaypoints', blank=True, null=True)
    binlegend = models.IntegerField(db_column='bInLegend', blank=True, null=True)
    binteractonmap = models.IntegerField(db_column='bInteractOnMap', blank=True, null=True)
    bisaesthetic = models.IntegerField(db_column='bIsAesthetic', blank=True, null=True)
    bshowonelectivespawnmap = models.IntegerField(db_column='bShowOnElectiveSpawnMap', blank=True, null=True)
    bshowonspawnmap = models.IntegerField(db_column='bShowOnSpawnMap', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDDistrictMapMarker'


class Hudeffects(models.Model):
    id = models.IntegerField(primary_key=True)
    smaterialref = models.TextField(db_column='sMaterialRef', blank=True, null=True)
    ehudeffect = models.IntegerField(db_column='eHUDEffect', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDEffects'


class Hudiconcombos(models.Model):
    id = models.IntegerField(primary_key=True)
    ehudiconcombo = models.IntegerField(db_column='eHUDIconCombo', blank=True, null=True)
    elayer1 = models.IntegerField(db_column='eLayer1', blank=True, null=True)
    elayer2 = models.IntegerField(db_column='eLayer2', blank=True, null=True)
    elayer3 = models.IntegerField(db_column='eLayer3', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDIconCombos'


class Hudicons(models.Model):
    id = models.IntegerField(primary_key=True)
    ehudicon = models.IntegerField(db_column='eHUDIcon', blank=True, null=True)
    niconcolumn = models.IntegerField(db_column='nIconColumn', blank=True, null=True)
    niconrow = models.IntegerField(db_column='nIconRow', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDIcons'


class Hudinfobrowsers(models.Model):
    id = models.IntegerField(primary_key=True)
    spackageref = models.TextField(db_column='sPackageRef', blank=True, null=True)
    ehudinfobrowser = models.IntegerField(db_column='eHUDInfoBrowser', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDInfoBrowsers'


class Hudmarkeroffset(models.Model):
    id = models.IntegerField(primary_key=True)
    ehudmarkeroffset = models.IntegerField(db_column='eHUDMarkerOffset', blank=True, null=True)
    foffset_x = models.FloatField(db_column='fOffset_X', blank=True, null=True)
    foffset_y = models.FloatField(db_column='fOffset_Y', blank=True, null=True)
    foffset_z = models.FloatField(db_column='fOffset_Z', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDMarkerOffset'


class Hudmarkerstatecolours(models.Model):
    id = models.IntegerField(primary_key=True)
    edefault = models.IntegerField(db_column='eDefault', blank=True, null=True)
    ehudmarkerstatecolour = models.IntegerField(db_column='eHUDMarkerStateColour', blank=True, null=True)
    etask_neutral = models.IntegerField(db_column='eTask_Neutral', blank=True, null=True)
    etask_oppositionattack = models.IntegerField(db_column='eTask_OppositionAttack', blank=True, null=True)
    etask_oppositiondefend = models.IntegerField(db_column='eTask_OppositionDefend', blank=True, null=True)
    etask_ownerattack = models.IntegerField(db_column='eTask_OwnerAttack', blank=True, null=True)
    etask_ownerdefend = models.IntegerField(db_column='eTask_OwnerDefend', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDMarkerStateColours'


class Hudmarkerstates(models.Model):
    id = models.IntegerField(primary_key=True)
    fupdatedelay = models.FloatField(db_column='fUpdateDelay', blank=True, null=True)
    ehudmarkerstate = models.IntegerField(db_column='eHUDMarkerState', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDMarkerStates'


class Hudmarkervisual(models.Model):
    id = models.IntegerField(primary_key=True)
    ecolourprofile = models.IntegerField(db_column='eColourProfile', blank=True, null=True)
    edistrictmapmarker = models.IntegerField(db_column='eDistrictMapMarker', blank=True, null=True)
    ehudmarkeroffset = models.IntegerField(db_column='eHUDMarkerOffset', blank=True, null=True)
    ehudmarkervisual = models.IntegerField(db_column='eHUDMarkerVisual', blank=True, null=True)
    eradarmarker = models.IntegerField(db_column='eRadarMarker', blank=True, null=True)
    etaskmarker = models.IntegerField(db_column='eTaskMarker', blank=True, null=True)
    ecategory = models.IntegerField(db_column='eCategory', blank=True, null=True)
    bcontainsplayerdata = models.IntegerField(db_column='bContainsPlayerData', blank=True, null=True)
    bpreventpawnvisibilitychecks = models.IntegerField(db_column='bPreventPawnVisibilityChecks', blank=True, null=True)
    buseindividualstate = models.IntegerField(db_column='bUseIndividualState', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDMarkerVisual'


class Hudmarkervisualtext(models.Model):
    id = models.IntegerField(primary_key=True)
    sneutral = models.TextField(db_column='sNeutral', blank=True, null=True)
    soppositionattack = models.TextField(db_column='sOppositionAttack', blank=True, null=True)
    soppositiondefend = models.TextField(db_column='sOppositionDefend', blank=True, null=True)
    sownerattack = models.TextField(db_column='sOwnerAttack', blank=True, null=True)
    sownerdefend = models.TextField(db_column='sOwnerDefend', blank=True, null=True)
    ehudmarkervisual = models.IntegerField(db_column='eHUDMarkerVisual', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDMarkerVisualText'


class Hudmessagecategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplaytext = models.TextField(db_column='sDisplayText', blank=True, null=True)
    ehudmessagecategory = models.IntegerField(db_column='eHUDMessageCategory', blank=True, null=True)
    eicon = models.IntegerField(db_column='eIcon', blank=True, null=True)
    echatcategory = models.IntegerField(db_column='eChatCategory', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDMessageCategories'


class Hudmessageposition(models.Model):
    id = models.IntegerField(primary_key=True)
    ehudmessageposition = models.IntegerField(db_column='eHUDMessagePosition', blank=True, null=True)
    fypercent = models.FloatField(db_column='fYPercent', blank=True, null=True)
    nyoffset = models.IntegerField(db_column='nYOffset', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDMessagePosition'


class Hudmessagescenes(models.Model):
    id = models.IntegerField(primary_key=True)
    spackageref = models.TextField(db_column='sPackageRef', blank=True, null=True)
    ehudmessagescene = models.IntegerField(db_column='eHUDMessageScene', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDMessageScenes'


class Hudmessages(models.Model):
    id = models.IntegerField(primary_key=True)
    saudiocue = models.TextField(db_column='sAudioCue', blank=True, null=True)
    schattext = models.TextField(db_column='sChatText', blank=True, null=True)
    sdisplaytext = models.TextField(db_column='sDisplayText', blank=True, null=True)
    sfemaletext = models.TextField(db_column='sFemaleText', blank=True, null=True)
    ecategory = models.IntegerField(db_column='eCategory', blank=True, null=True)
    ehudmessage = models.IntegerField(db_column='eHUDMessage', blank=True, null=True)
    enextmessage = models.IntegerField(db_column='eNextMessage', blank=True, null=True)
    epopupdialogoverride = models.IntegerField(db_column='ePopupDialogOverride', blank=True, null=True)
    eposition = models.IntegerField(db_column='ePosition', blank=True, null=True)
    escene = models.IntegerField(db_column='eScene', blank=True, null=True)
    euistyle = models.IntegerField(db_column='eUIStyle', blank=True, null=True)
    fdisplaytime = models.FloatField(db_column='fDisplayTime', blank=True, null=True)
    fqueuetimeout = models.FloatField(db_column='fQueueTimeout', blank=True, null=True)
    epriority = models.IntegerField(db_column='ePriority', blank=True, null=True)
    ballowmultiples = models.IntegerField(db_column='bAllowMultiples', blank=True, null=True)
    bforaction = models.IntegerField(db_column='bForAction', blank=True, null=True)
    bforceremony = models.IntegerField(db_column='bForCeremony', blank=True, null=True)
    bforchat = models.IntegerField(db_column='bForChat', blank=True, null=True)
    bforcombat = models.IntegerField(db_column='bForCombat', blank=True, null=True)
    bfordistrictmap = models.IntegerField(db_column='bForDistrictMap', blank=True, null=True)
    bsuppressmain = models.IntegerField(db_column='bSuppressMain', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDMessages'


class Hudpopupmenuitems(models.Model):
    id = models.IntegerField(primary_key=True)
    sconsolecommand = models.TextField(db_column='sConsoleCommand', blank=True, null=True)
    skeypress = models.TextField(db_column='sKeyPress', blank=True, null=True)
    slocalisationtext = models.TextField(db_column='sLocalisationText', blank=True, null=True)
    ehudpopupmenuitem = models.IntegerField(db_column='eHUDPopUpMenuItem', blank=True, null=True)
    eimage = models.IntegerField(db_column='eImage', blank=True, null=True)
    eenabledrule = models.IntegerField(db_column='eEnabledRule', blank=True, null=True)
    bdisplaykeybinding = models.IntegerField(db_column='bDisplayKeyBinding', blank=True, null=True)
    benablewhendead = models.IntegerField(db_column='bEnableWhenDead', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDPopUpMenuItems'


class Hudradarmarkers(models.Model):
    id = models.IntegerField(primary_key=True)
    ehudradarmarker = models.IntegerField(db_column='eHUDRadarMarker', blank=True, null=True)
    eicon = models.IntegerField(db_column='eIcon', blank=True, null=True)
    eiconsurround = models.IntegerField(db_column='eIconSurround', blank=True, null=True)
    niconsize = models.IntegerField(db_column='nIconSize', blank=True, null=True)
    niconsurroundsize = models.IntegerField(db_column='nIconSurroundSize', blank=True, null=True)
    bshowonelectivespawnmap = models.IntegerField(db_column='bShowOnElectiveSpawnMap', blank=True, null=True)
    bvalidinmission = models.IntegerField(db_column='bValidInMission', blank=True, null=True)
    bvalidoutofmission = models.IntegerField(db_column='bValidOutOfMission', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDRadarMarkers'


class Hudreticulehinticons(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplaytext = models.TextField(db_column='sDisplayText', blank=True, null=True)
    ecolour = models.IntegerField(db_column='eColour', blank=True, null=True)
    ehudreticulehinticon = models.IntegerField(db_column='eHUDReticuleHintIcon', blank=True, null=True)
    eicon = models.IntegerField(db_column='eIcon', blank=True, null=True)
    fmaxdistance = models.FloatField(db_column='fMaxDistance', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDReticuleHintIcons'


class Hudreticules(models.Model):
    id = models.IntegerField(primary_key=True)
    spackageref = models.TextField(db_column='sPackageRef', blank=True, null=True)
    ecolourdefault = models.IntegerField(db_column='eColourDefault', blank=True, null=True)
    ecolourenemy = models.IntegerField(db_column='eColourEnemy', blank=True, null=True)
    ecolourfriend = models.IntegerField(db_column='eColourFriend', blank=True, null=True)
    ehudreticule = models.IntegerField(db_column='eHUDReticule', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDReticules'


class Hudscenes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdatastoretag = models.TextField(db_column='sDataStoreTag', blank=True, null=True)
    spackageref = models.TextField(db_column='sPackageRef', blank=True, null=True)
    ehudscenes = models.IntegerField(db_column='eHUDScenes', blank=True, null=True)
    bopeninloginlevel = models.IntegerField(db_column='bOpenInLoginLevel', blank=True, null=True)
    bstarthidden = models.IntegerField(db_column='bStartHidden', blank=True, null=True)
    bupdatewhiledead = models.IntegerField(db_column='bUpdateWhileDead', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDScenes'


class Hudtaskmarkerscenes(models.Model):
    id = models.IntegerField(primary_key=True)
    spackageref = models.TextField(db_column='sPackageRef', blank=True, null=True)
    ehudtaskmarkerscene = models.IntegerField(db_column='eHUDTaskMarkerScene', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDTaskMarkerScenes'


class Hudtaskmarkers(models.Model):
    id = models.IntegerField(primary_key=True)
    earrowicon = models.IntegerField(db_column='eArrowIcon', blank=True, null=True)
    earrowiconellipse = models.IntegerField(db_column='eArrowIconEllipse', blank=True, null=True)
    earrowiconocc = models.IntegerField(db_column='eArrowIconOcc', blank=True, null=True)
    eellipseicon = models.IntegerField(db_column='eEllipseIcon', blank=True, null=True)
    ehudtaskmarker = models.IntegerField(db_column='eHUDTaskMarker', blank=True, null=True)
    eoccludedicon = models.IntegerField(db_column='eOccludedIcon', blank=True, null=True)
    escene = models.IntegerField(db_column='eScene', blank=True, null=True)
    evisibleicon = models.IntegerField(db_column='eVisibleIcon', blank=True, null=True)
    fmaxvisibledistance = models.FloatField(db_column='fMaxVisibleDistance', blank=True, null=True)
    npriority = models.IntegerField(db_column='nPriority', blank=True, null=True)
    bhidedistance = models.IntegerField(db_column='bHideDistance', blank=True, null=True)
    bhidewhenoccluded = models.IntegerField(db_column='bHideWhenOccluded', blank=True, null=True)
    binteractondistrictmap = models.IntegerField(db_column='bInteractOnDistrictMap', blank=True, null=True)
    bshowbydefault = models.IntegerField(db_column='bShowByDefault', blank=True, null=True)
    bshowinworld = models.IntegerField(db_column='bShowInWorld', blank=True, null=True)
    bshowonedge = models.IntegerField(db_column='bShowOnEdge', blank=True, null=True)
    bshowonself = models.IntegerField(db_column='bShowOnSelf', blank=True, null=True)
    bvalidinmission = models.IntegerField(db_column='bValidInMission', blank=True, null=True)
    bvalidoutofmission = models.IntegerField(db_column='bValidOutOfMission', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDTaskMarkers'


class Hudtextureicons(models.Model):
    id = models.IntegerField(primary_key=True)
    siconsetname = models.TextField(db_column='sIconSetName', blank=True, null=True)
    smoviename = models.TextField(db_column='sMovieName', blank=True, null=True)
    spackageref = models.TextField(db_column='sPackageRef', blank=True, null=True)
    ehudtextureicon = models.IntegerField(db_column='eHUDTextureIcon', blank=True, null=True)
    etexturepageicon = models.IntegerField(db_column='eTexturePageIcon', blank=True, null=True)
    nframenumber = models.IntegerField(db_column='nFrameNumber', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDTextureIcons'


class Hudtexturepage(models.Model):
    id = models.IntegerField(primary_key=True)
    spackagename = models.TextField(db_column='sPackageName', blank=True, null=True)
    ehudtexturepage = models.IntegerField(db_column='eHUDTexturePage', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDTexturePage'


class Hudtexturepageicon(models.Model):
    id = models.IntegerField(primary_key=True)
    ehudtexturepageicon = models.IntegerField(db_column='eHUDTexturePageIcon', blank=True, null=True)
    etexturepage = models.IntegerField(db_column='eTexturePage', blank=True, null=True)
    nu = models.IntegerField(db_column='nU', blank=True, null=True)
    nul = models.IntegerField(db_column='nUL', blank=True, null=True)
    nv = models.IntegerField(db_column='nV', blank=True, null=True)
    nvl = models.IntegerField(db_column='nVL', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDTexturePageIcon'


class HudusablesDisplaysettings(models.Model):
    id = models.IntegerField(primary_key=True)
    eiconcolour = models.IntegerField(db_column='eIconColour', blank=True, null=True)
    fbackgroundopacity = models.FloatField(db_column='fBackgroundOpacity', blank=True, null=True)
    ftextbackgroundopacity = models.FloatField(db_column='fTextBackgroundOpacity', blank=True, null=True)
    ehudusables_displaysetting = models.IntegerField(db_column='eHUDUsables_DisplaySetting', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDUsables_DisplaySettings'


class Hudwscharinfos(models.Model):
    id = models.IntegerField(primary_key=True)
    ecolourprofile = models.IntegerField(db_column='eColourProfile', blank=True, null=True)
    ehudwscharinfo = models.IntegerField(db_column='eHUDWSCharInfo', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDWSCharInfos'


class Hudzonenotifier(models.Model):
    id = models.IntegerField(primary_key=True)
    eicon = models.IntegerField(db_column='eIcon', blank=True, null=True)
    ehudzonenotifier = models.IntegerField(db_column='eHUDZoneNotifier', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUDZoneNotifier'


class Heatactionaffects(models.Model):
    id = models.IntegerField(primary_key=True)
    eheatactionaffect = models.IntegerField(db_column='eHeatActionAffect', blank=True, null=True)
    enotorietyeffect = models.IntegerField(db_column='eNotorietyEffect', blank=True, null=True)
    eprestigeeffect = models.IntegerField(db_column='ePrestigeEffect', blank=True, null=True)
    fescapepenaltytimer = models.FloatField(db_column='fEscapePenaltyTimer', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HeatActionAffects'


class Heatconstants(models.Model):
    id = models.IntegerField(primary_key=True)
    scomment = models.TextField(db_column='sComment', blank=True, null=True)
    fcriminalvalue = models.FloatField(db_column='fCriminalValue', blank=True, null=True)
    fenforcervalue = models.FloatField(db_column='fEnforcerValue', blank=True, null=True)
    eheatconstant = models.IntegerField(db_column='eHeatConstant', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HeatConstants'


class Heatlevels(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    eheatlevel = models.IntegerField(db_column='eHeatLevel', blank=True, null=True)
    ehudtexture = models.IntegerField(db_column='eHUDTexture', blank=True, null=True)
    frewardmultiplier = models.FloatField(db_column='fRewardMultiplier', blank=True, null=True)
    fthreshold = models.FloatField(db_column='fThreshold', blank=True, null=True)
    nlevel = models.IntegerField(db_column='nLevel', blank=True, null=True)
    bbreakscontactpledges = models.IntegerField(db_column='bBreaksContactPledges', blank=True, null=True)
    bdispatchbounty = models.IntegerField(db_column='bDispatchBounty', blank=True, null=True)
    bdispatchmission = models.IntegerField(db_column='bDispatchMission', blank=True, null=True)
    bpvpunlockedtoallopposingfaction = models.IntegerField(db_column='bPVPUnlockedToAllOpposingFaction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HeatLevels'


class Hostingconfigfiles(models.Model):
    id = models.IntegerField(primary_key=True)
    sfilename = models.TextField(db_column='sFilename', blank=True, null=True)
    npersistentid = models.IntegerField(db_column='nPersistentId', blank=True, null=True)
    ehostingconfigfile = models.IntegerField(db_column='eHostingConfigFile', blank=True, null=True)
    etype = models.IntegerField(db_column='eType', blank=True, null=True)
    bpersistent = models.IntegerField(db_column='bPersistent', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HostingConfigFiles'


class Hudgroupstates(models.Model):
    id = models.IntegerField(primary_key=True)
    sheadertext = models.TextField(db_column='sHeaderText', blank=True, null=True)
    eheadercolour = models.IntegerField(db_column='eHeaderColour', blank=True, null=True)
    eheadericon = models.IntegerField(db_column='eHeaderIcon', blank=True, null=True)
    ehudgroupstate = models.IntegerField(db_column='eHudGroupState', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HudGroupStates'


class Instrumentitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sresource = models.TextField(db_column='sResource', blank=True, null=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InstrumentItemTypes'


class Interactiveactortype(models.Model):
    id = models.IntegerField(primary_key=True)
    dummy = models.FloatField(db_column='Dummy', blank=True, null=True)
    einteractiveactorcategory = models.IntegerField(db_column='eInteractiveActorCategory', blank=True, null=True)
    einteractiveactortype = models.IntegerField(db_column='eInteractiveActorType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InteractiveActorType'


class Intraactivityrewards(models.Model):
    id = models.IntegerField(primary_key=True)
    fpercentagelosspercapture = models.FloatField(db_column='fPercentageLossPerCapture', blank=True, null=True)
    ncash_0 = models.IntegerField(db_column='nCash_0', blank=True, null=True)
    ncash_1 = models.IntegerField(db_column='nCash_1', blank=True, null=True)
    ncontactstanding_0 = models.IntegerField(db_column='nContactStanding_0', blank=True, null=True)
    ncontactstanding_1 = models.IntegerField(db_column='nContactStanding_1', blank=True, null=True)
    nminimumpointsvalue = models.IntegerField(db_column='nMinimumPointsValue', blank=True, null=True)
    nscore = models.IntegerField(db_column='nScore', blank=True, null=True)
    eintraactivityreward = models.IntegerField(db_column='eIntraActivityReward', blank=True, null=True)
    escorecategory = models.IntegerField(db_column='eScoreCategory', blank=True, null=True)
    baddtoopenworldcashpool = models.IntegerField(db_column='bAddToOpenWorldCashPool', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IntraActivityRewards'


class Inventoryitemcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    stablename = models.TextField(db_column='sTableName', blank=True, null=True)
    nbytesize = models.IntegerField(db_column='nByteSize', blank=True, null=True)
    nbytesizeui = models.IntegerField(db_column='nByteSizeUI', blank=True, null=True)
    ninitialstoragespace = models.IntegerField(db_column='nInitialStorageSpace', blank=True, null=True)
    nmaxstoragespace = models.IntegerField(db_column='nMaxStorageSpace', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    einventoryitemcategory = models.IntegerField(db_column='eInventoryItemCategory', blank=True, null=True)
    bcopyable = models.IntegerField(db_column='bCopyable', blank=True, null=True)
    bcreatorwaivesrating = models.IntegerField(db_column='bCreatorWaivesRating', blank=True, null=True)
    bmarketplacesearch = models.IntegerField(db_column='bMarketplaceSearch', blank=True, null=True)
    brenamable = models.IntegerField(db_column='bRenamable', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InventoryItemCategories'


class Inventoryitemcategorylimited(models.Model):
    id = models.IntegerField(primary_key=True)
    fcustomisationreplenishperiod = models.FloatField(db_column='fCustomisationReplenishPeriod', blank=True, null=True)
    ncustomisationinitialavailability = models.IntegerField(db_column='nCustomisationInitialAvailability', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    einventoryitemcategory = models.IntegerField(db_column='eInventoryItemCategory', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InventoryItemCategoryLimited'


class Inventoryiteminfracategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    sidentifier = models.TextField(db_column='sIdentifier', blank=True, null=True)
    ssingularname = models.TextField(db_column='sSingularName', blank=True, null=True)
    einventoryiteminfracategory = models.IntegerField(db_column='eInventoryItemInfraCategory', blank=True, null=True)
    ninitialavail = models.IntegerField(db_column='nInitialAvail', blank=True, null=True)
    ninitialrate = models.IntegerField(db_column='nInitialRate', blank=True, null=True)
    nmaxavail = models.IntegerField(db_column='nMaxAvail', blank=True, null=True)
    nmaxrate = models.IntegerField(db_column='nMaxRate', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    esubcategory = models.IntegerField(db_column='eSubCategory', blank=True, null=True)
    bispublished = models.IntegerField(db_column='bIsPublished', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InventoryItemInfraCategories'


class Inventoryitemleases(models.Model):
    id = models.IntegerField(primary_key=True)
    einventoryitemlease = models.IntegerField(db_column='eInventoryItemLease', blank=True, null=True)
    fcostapbcashmultiplier = models.FloatField(db_column='fCostAPBCashMultiplier', blank=True, null=True)
    fexpirytime = models.FloatField(db_column='fExpiryTime', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InventoryItemLeases'


class Inventoryitemsubcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    ecategory = models.IntegerField(db_column='eCategory', blank=True, null=True)
    einventoryitemsubcategory = models.IntegerField(db_column='eInventoryItemSubCategory', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InventoryItemSubCategories'


class Inventoryitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    screatorname = models.TextField(db_column='sCreatorName', blank=True, null=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    ehudimage = models.IntegerField(db_column='eHUDImage', blank=True, null=True)
    einfracategory = models.IntegerField(db_column='eInfraCategory', blank=True, null=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    elease = models.IntegerField(db_column='eLease', blank=True, null=True)
    eunlock = models.IntegerField(db_column='eUnlock', blank=True, null=True)
    narmascategoryid = models.IntegerField(db_column='nArmasCategoryID', blank=True, null=True)
    narmasproductid = models.IntegerField(db_column='nArmasProductID', blank=True, null=True)
    narmassubcategoryid = models.IntegerField(db_column='nArmasSubcategoryID', blank=True, null=True)
    ncostapbcash = models.IntegerField(db_column='nCostAPBCash', blank=True, null=True)
    ncostrewardtokens = models.IntegerField(db_column='nCostRewardTokens', blank=True, null=True)
    nminrating = models.IntegerField(db_column='nMinRating', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    eorganisation = models.IntegerField(db_column='eOrganisation', blank=True, null=True)
    etrade = models.IntegerField(db_column='eTrade', blank=True, null=True)
    bcansellback = models.IntegerField(db_column='bCanSellback', blank=True, null=True)
    bcriminal = models.IntegerField(db_column='bCriminal', blank=True, null=True)
    benforcer = models.IntegerField(db_column='bEnforcer', blank=True, null=True)
    bgifted = models.IntegerField(db_column='bGifted', blank=True, null=True)
    bignoresddvalidation = models.IntegerField(db_column='bIgnoreSddValidation', blank=True, null=True)
    bisarmas = models.IntegerField(db_column='bIsArmas', blank=True, null=True)
    bispublished = models.IntegerField(db_column='bIsPublished', blank=True, null=True)
    bnodelete = models.IntegerField(db_column='bNoDelete', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InventoryItemTypes'


class Invokedcontextsensitiveaction(models.Model):
    id = models.IntegerField(primary_key=True)
    fduration = models.FloatField(db_column='fDuration', blank=True, null=True)
    econtextsensitiveaction = models.IntegerField(db_column='eContextSensitiveAction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InvokedContextSensitiveAction'


class Itemattachmentvisual(models.Model):
    id = models.IntegerField(primary_key=True)
    sanimsetasset = models.TextField(db_column='sAnimSetAsset', blank=True, null=True)
    sanimtreeasset = models.TextField(db_column='sAnimTreeAsset', blank=True, null=True)
    sattachmentasset = models.TextField(db_column='sAttachmentAsset', blank=True, null=True)
    sattachmentclass = models.TextField(db_column='sAttachmentClass', blank=True, null=True)
    saudiotype = models.TextField(db_column='sAudioType', blank=True, null=True)
    sphysicsasset = models.TextField(db_column='sPhysicsAsset', blank=True, null=True)
    eanimtreedecision = models.IntegerField(db_column='eAnimTreeDecision', blank=True, null=True)
    eitemattachmentvisual = models.IntegerField(db_column='eItemAttachmentVisual', blank=True, null=True)
    euimeshviewersetup = models.IntegerField(db_column='eUIMeshViewerSetup', blank=True, null=True)
    euimeshviewersetup_inventory = models.IntegerField(db_column='eUIMeshViewerSetup_Inventory', blank=True, null=True)
    etaskitemanimationtype = models.IntegerField(db_column='eTaskItemAnimationType', blank=True, null=True)
    blefthandikbydefault = models.IntegerField(db_column='bLeftHandIKByDefault', blank=True, null=True)
    blefthandikwhileaiming = models.IntegerField(db_column='bLeftHandIKWhileAiming', blank=True, null=True)
    bsuppressrunanimation = models.IntegerField(db_column='bSuppressRunAnimation', blank=True, null=True)
    bsuppresssprintanimation = models.IntegerField(db_column='bSuppressSprintAnimation', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ItemAttachmentVisual'


class Itemattachmentvisualdamagestates(models.Model):
    id = models.IntegerField(primary_key=True)
    sassetname = models.TextField(db_column='sAssetName', blank=True, null=True)
    sdamagesfx = models.TextField(db_column='sDamageSFX', blank=True, null=True)
    sdamagevfx = models.TextField(db_column='sDamageVFX', blank=True, null=True)
    srecoversfx = models.TextField(db_column='sRecoverSFX', blank=True, null=True)
    srecovervfx = models.TextField(db_column='sRecoverVFX', blank=True, null=True)
    edamageableattachmentvisual = models.IntegerField(db_column='eDamageableAttachmentVisual', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ItemAttachmentVisualDamageStates'


class Loadingmovieaudiobanks(models.Model):
    id = models.IntegerField(primary_key=True)
    nbankend = models.IntegerField(db_column='nBankEnd', blank=True, null=True)
    nbankstart = models.IntegerField(db_column='nBankStart', blank=True, null=True)
    eloadingmovieaudiobanks = models.IntegerField(db_column='eLoadingMovieAudioBanks', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LoadingMovieAudioBanks'


class Loadingmovieconfigs(models.Model):
    id = models.IntegerField(primary_key=True)
    sloadingmovie = models.TextField(db_column='sLoadingMovie', blank=True, null=True)
    suiscene = models.TextField(db_column='sUIScene', blank=True, null=True)
    edistrict = models.IntegerField(db_column='eDistrict', blank=True, null=True)
    eloadingmovieconfig = models.IntegerField(db_column='eLoadingMovieConfig', blank=True, null=True)
    nnumaudiotracks = models.IntegerField(db_column='nNumAudioTracks', blank=True, null=True)
    nnumberofpages = models.IntegerField(db_column='nNumberOfPages', blank=True, null=True)
    npagelength = models.IntegerField(db_column='nPageLength', blank=True, null=True)
    etransitiontype = models.IntegerField(db_column='eTransitionType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LoadingMovieConfigs'


class Loadingmovietips(models.Model):
    id = models.IntegerField(primary_key=True)
    smessage = models.TextField(db_column='sMessage', blank=True, null=True)
    eloadingmovietip = models.IntegerField(db_column='eLoadingMovieTip', blank=True, null=True)
    nmaximumrating = models.IntegerField(db_column='nMaximumRating', blank=True, null=True)
    nminimumrating = models.IntegerField(db_column='nMinimumRating', blank=True, null=True)
    edistrictrestriction = models.IntegerField(db_column='eDistrictRestriction', blank=True, null=True)
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LoadingMovieTips'


class Localetypepriorities(models.Model):
    id = models.IntegerField(primary_key=True)
    npriority = models.IntegerField(db_column='nPriority', blank=True, null=True)
    elocaletypepriority = models.IntegerField(db_column='eLocaleTypePriority', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LocaleTypePriorities'


class Locationbeaconinstances(models.Model):
    id = models.IntegerField(primary_key=True)
    slocalisedname = models.TextField(db_column='sLocalisedName', blank=True, null=True)
    edistrict = models.IntegerField(db_column='eDistrict', blank=True, null=True)
    elocationbeaconinstance = models.IntegerField(db_column='eLocationBeaconInstance', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LocationBeaconInstances'


class Locationbeacons(models.Model):
    id = models.IntegerField(primary_key=True)
    elocationbeacon = models.IntegerField(db_column='eLocationBeacon', blank=True, null=True)
    fradius = models.FloatField(db_column='fRadius', blank=True, null=True)
    nheight = models.IntegerField(db_column='nHeight', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LocationBeacons'


class Mailconstants(models.Model):
    id = models.IntegerField(primary_key=True)
    nvalue = models.IntegerField(db_column='nValue', blank=True, null=True)
    emailconstant = models.IntegerField(db_column='eMailConstant', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MailConstants'


class Maildurations(models.Model):
    id = models.IntegerField(primary_key=True)
    nminutes = models.IntegerField(db_column='nMinutes', blank=True, null=True)
    emailduration = models.IntegerField(db_column='eMailDuration', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MailDurations'


class Marketplacecashtype(models.Model):
    id = models.IntegerField(primary_key=True)
    sresource = models.TextField(db_column='sResource', blank=True, null=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MarketplaceCashType'


class Marketplaceconstants(models.Model):
    id = models.IntegerField(primary_key=True)
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)
    emarketplaceconstant = models.IntegerField(db_column='eMarketplaceConstant', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MarketplaceConstants'


class Marketplacedurations(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplaystring = models.TextField(db_column='sDisplayString', blank=True, null=True)
    nminutes = models.IntegerField(db_column='nMinutes', blank=True, null=True)
    emarketplaceduration = models.IntegerField(db_column='eMarketplaceDuration', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MarketplaceDurations'


class Marketplacetimeleft(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplaystring = models.TextField(db_column='sDisplayString', blank=True, null=True)
    nminutes = models.IntegerField(db_column='nMinutes', blank=True, null=True)
    emarketplacetimeleft = models.IntegerField(db_column='eMarketplaceTimeLeft', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MarketplaceTimeLeft'


class Medalcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    emedalcategory = models.IntegerField(db_column='eMedalCategory', blank=True, null=True)
    bexclusivemedal = models.IntegerField(db_column='bExclusiveMedal', blank=True, null=True)
    bimmediateaward = models.IntegerField(db_column='bImmediateAward', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MedalCategories'


class Medals(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    stitle = models.TextField(db_column='sTitle', blank=True, null=True)
    elargemedalicon = models.IntegerField(db_column='eLargeMedalIcon', blank=True, null=True)
    emedal = models.IntegerField(db_column='eMedal', blank=True, null=True)
    emedalicon = models.IntegerField(db_column='eMedalIcon', blank=True, null=True)
    eshowcasetrackedactivity = models.IntegerField(db_column='eShowcaseTrackedActivity', blank=True, null=True)
    nclassificationordinal = models.IntegerField(db_column='nClassificationOrdinal', blank=True, null=True)
    nparamx = models.IntegerField(db_column='nParamX', blank=True, null=True)
    nparamy = models.IntegerField(db_column='nParamY', blank=True, null=True)
    nscore = models.IntegerField(db_column='nScore', blank=True, null=True)
    nshowcaseorder = models.IntegerField(db_column='nShowcaseOrder', blank=True, null=True)
    emedalcategory = models.IntegerField(db_column='eMedalCategory', blank=True, null=True)
    escorecategory = models.IntegerField(db_column='eScoreCategory', blank=True, null=True)
    eshowcasefaction = models.IntegerField(db_column='eShowcaseFaction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Medals'


class Minigameconstants(models.Model):
    id = models.IntegerField(primary_key=True)
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)
    eminigameconstant = models.IntegerField(db_column='eMinigameConstant', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MinigameConstants'


class Minigameeffects(models.Model):
    id = models.IntegerField(primary_key=True)
    sparticlesystem = models.TextField(db_column='sParticleSystem', blank=True, null=True)
    ssoundeffect = models.TextField(db_column='sSoundEffect', blank=True, null=True)
    eminigameeffect = models.IntegerField(db_column='eMinigameEffect', blank=True, null=True)
    fmaxplaydistance = models.FloatField(db_column='fMaxPlayDistance', blank=True, null=True)
    fsfxoffsetx = models.FloatField(db_column='fSFXOffsetX', blank=True, null=True)
    fsfxoffsety = models.FloatField(db_column='fSFXOffsetY', blank=True, null=True)
    fsfxoffsetz = models.FloatField(db_column='fSFXOffsetZ', blank=True, null=True)
    fvfxoffsetx = models.FloatField(db_column='fVFXOffsetX', blank=True, null=True)
    fvfxoffsety = models.FloatField(db_column='fVFXOffsetY', blank=True, null=True)
    fvfxoffsetz = models.FloatField(db_column='fVFXOffsetZ', blank=True, null=True)
    bplayfordeadplayers = models.IntegerField(db_column='bPlayForDeadPlayers', blank=True, null=True)
    buse3dsound = models.IntegerField(db_column='bUse3DSound', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MinigameEffects'


class MinigamegungameWeaponsetupentries(models.Model):
    id = models.IntegerField(primary_key=True)
    echaractercustomisationoverride = models.IntegerField(db_column='eCharacterCustomisationOverride', blank=True, null=True)
    eminigamegungame_weaponsetup = models.IntegerField(db_column='eMinigameGunGame_WeaponSetup', blank=True, null=True)
    eweaponloadout = models.IntegerField(db_column='eWeaponLoadout', blank=True, null=True)
    fscoremodifier = models.FloatField(db_column='fScoreModifier', blank=True, null=True)
    nlevel = models.IntegerField(db_column='nLevel', blank=True, null=True)
    nnextlevelrequiredkills = models.IntegerField(db_column='nNextLevelRequiredKills', blank=True, null=True)
    nnextlevelrequiredscore = models.IntegerField(db_column='nNextLevelRequiredScore', blank=True, null=True)
    bnextlevelrequiredscoreisabsolute = models.IntegerField(db_column='bNextLevelRequiredScoreIsAbsolute', blank=True, null=True)
    bnextlevelrequiregamescorelimit = models.IntegerField(db_column='bNextLevelRequireGameScoreLimit', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MinigameGunGame_WeaponSetupEntries'


class MinigamegungameWeaponsetups(models.Model):
    id = models.IntegerField(primary_key=True)
    eminigamegungame_weaponsetup = models.IntegerField(db_column='eMinigameGunGame_WeaponSetup', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MinigameGunGame_WeaponSetups'


class Minigamelocations(models.Model):
    id = models.IntegerField(primary_key=True)
    edistrictblock = models.IntegerField(db_column='eDistrictBlock', blank=True, null=True)
    edistrictruleset = models.IntegerField(db_column='eDistrictRuleSet', blank=True, null=True)
    eminigame = models.IntegerField(db_column='eMinigame', blank=True, null=True)
    eminigamelocation = models.IntegerField(db_column='eMinigameLocation', blank=True, null=True)
    nweight = models.IntegerField(db_column='nWeight', blank=True, null=True)
    erarity = models.IntegerField(db_column='eRarity', blank=True, null=True)
    espawnvariableoverride = models.IntegerField(db_column='eSpawnVariableOverride', blank=True, null=True)
    ballowlocationreuse = models.IntegerField(db_column='bAllowLocationReuse', blank=True, null=True)
    bentiredistrict = models.IntegerField(db_column='bEntireDistrict', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MinigameLocations'


class Minigamerewards(models.Model):
    id = models.IntegerField(primary_key=True)
    eminigame = models.IntegerField(db_column='eMinigame', blank=True, null=True)
    eminigamereward = models.IntegerField(db_column='eMinigameReward', blank=True, null=True)
    ereward = models.IntegerField(db_column='eReward', blank=True, null=True)
    ncashreward_0 = models.IntegerField(db_column='nCashReward_0', blank=True, null=True)
    ncashreward_1 = models.IntegerField(db_column='nCashReward_1', blank=True, null=True)
    nrewardlevel = models.IntegerField(db_column='nRewardLevel', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MinigameRewards'


class Minigamespawnerthemes(models.Model):
    id = models.IntegerField(primary_key=True)
    eminigamespawnertheme = models.IntegerField(db_column='eMinigameSpawnerTheme', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MinigameSpawnerThemes'


class Minigames(models.Model):
    id = models.IntegerField(primary_key=True)
    steamheaders_0 = models.TextField(db_column='sTeamHeaders_0', blank=True, null=True)
    steamheaders_1 = models.TextField(db_column='sTeamHeaders_1', blank=True, null=True)
    steamnames_0 = models.TextField(db_column='sTeamNames_0', blank=True, null=True)
    steamnames_1 = models.TextField(db_column='sTeamNames_1', blank=True, null=True)
    echaractermodifiers_0 = models.IntegerField(db_column='eCharacterModifiers_0', blank=True, null=True)
    echaractermodifiers_1 = models.IntegerField(db_column='eCharacterModifiers_1', blank=True, null=True)
    echaractermodifiers_2 = models.IntegerField(db_column='eCharacterModifiers_2', blank=True, null=True)
    echaracteroverrides_0 = models.IntegerField(db_column='eCharacterOverrides_0', blank=True, null=True)
    echaracteroverrides_1 = models.IntegerField(db_column='eCharacterOverrides_1', blank=True, null=True)
    echaracteroverrides_2 = models.IntegerField(db_column='eCharacterOverrides_2', blank=True, null=True)
    eendeffect = models.IntegerField(db_column='eEndEffect', blank=True, null=True)
    eminigame = models.IntegerField(db_column='eMinigame', blank=True, null=True)
    eonmissionhudmarkervisual = models.IntegerField(db_column='eOnMissionHUDMarkerVisual', blank=True, null=True)
    eoutofmissionhudmarkervisual = models.IntegerField(db_column='eOutOfMissionHUDMarkerVisual', blank=True, null=True)
    espawnertheme = models.IntegerField(db_column='eSpawnerTheme', blank=True, null=True)
    estarteffect = models.IntegerField(db_column='eStartEffect', blank=True, null=True)
    etimeouteffect = models.IntegerField(db_column='eTimeoutEffect', blank=True, null=True)
    evehicleoverrides_0 = models.IntegerField(db_column='eVehicleOverrides_0', blank=True, null=True)
    evehicleoverrides_1 = models.IntegerField(db_column='eVehicleOverrides_1', blank=True, null=True)
    evehicleoverrides_2 = models.IntegerField(db_column='eVehicleOverrides_2', blank=True, null=True)
    eweaponloadouts_0 = models.IntegerField(db_column='eWeaponLoadouts_0', blank=True, null=True)
    eweaponloadouts_1 = models.IntegerField(db_column='eWeaponLoadouts_1', blank=True, null=True)
    eweaponloadouts_2 = models.IntegerField(db_column='eWeaponLoadouts_2', blank=True, null=True)
    fabandontimeout = models.FloatField(db_column='fAbandonTimeout', blank=True, null=True)
    fintroductiontime = models.FloatField(db_column='fIntroductionTime', blank=True, null=True)
    ftimeoutnotifyinterval = models.FloatField(db_column='fTimeoutNotifyInterval', blank=True, null=True)
    ftimeoutnotifystart = models.FloatField(db_column='fTimeoutNotifyStart', blank=True, null=True)
    ftimetoclearplayers = models.FloatField(db_column='fTimeToClearPlayers', blank=True, null=True)
    nmaxbonuscash = models.IntegerField(db_column='nMaxBonusCash', blank=True, null=True)
    nminimumplayercount_0 = models.IntegerField(db_column='nMinimumPlayerCount_0', blank=True, null=True)
    nminimumplayercount_1 = models.IntegerField(db_column='nMinimumPlayerCount_1', blank=True, null=True)
    nscoreeventsforparticipation = models.IntegerField(db_column='nScoreEventsForParticipation', blank=True, null=True)
    nscoreminimumforparticipation = models.IntegerField(db_column='nScoreMinimumForParticipation', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    espawnvariable = models.IntegerField(db_column='eSpawnVariable', blank=True, null=True)
    etype = models.IntegerField(db_column='eType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Minigames'


class MinigamesBlockfdm(models.Model):
    id = models.IntegerField(primary_key=True)
    eminigame = models.IntegerField(db_column='eMinigame', blank=True, null=True)
    fdeadparticipationtimer = models.FloatField(db_column='fDeadParticipationTimer', blank=True, null=True)
    flowteamcountscale = models.FloatField(db_column='fLowTeamCountScale', blank=True, null=True)
    flowteaminitialstartuptimer = models.FloatField(db_column='fLowTeamInitialStartupTimer', blank=True, null=True)
    flowteaminitialtimer = models.FloatField(db_column='fLowTeamInitialTimer', blank=True, null=True)
    flowteamlivesremovallinearportion = models.FloatField(db_column='fLowTeamLivesRemovalLinearPortion', blank=True, null=True)
    flowteamlivesremovalquadraticportion = models.FloatField(db_column='fLowTeamLivesRemovalQuadraticPortion', blank=True, null=True)
    foobparticipationtimer = models.FloatField(db_column='fOOBParticipationTimer', blank=True, null=True)
    foutofboundstime = models.FloatField(db_column='fOutOfBoundsTime', blank=True, null=True)
    nminnumlives = models.IntegerField(db_column='nMinNumLives', blank=True, null=True)
    nnumberoflivesperplayer = models.IntegerField(db_column='nNumberOfLivesPerPlayer', blank=True, null=True)
    bcountarrests = models.IntegerField(db_column='bCountArrests', blank=True, null=True)
    bignoreallsuicides = models.IntegerField(db_column='bIgnoreAllSuicides', blank=True, null=True)
    bignorefriendlykills = models.IntegerField(db_column='bIgnoreFriendlyKills', blank=True, null=True)
    bignoregmsuicides = models.IntegerField(db_column='bIgnoreGMSuicides', blank=True, null=True)
    bignorekillsbothoob = models.IntegerField(db_column='bIgnoreKillsBothOOB', blank=True, null=True)
    bignorekillsbyweaponsotherthanloadout = models.IntegerField(db_column='bIgnoreKillsByWeaponsOtherThanLoadout', blank=True, null=True)
    bignorekillskilledoob = models.IntegerField(db_column='bIgnoreKillsKilledOOB', blank=True, null=True)
    bignorekillskillernotinminigame = models.IntegerField(db_column='bIgnoreKillsKillerNotInMinigame', blank=True, null=True)
    bignorekillskilleroob = models.IntegerField(db_column='bIgnoreKillsKillerOOB', blank=True, null=True)
    bignorenonweaponexplosions = models.IntegerField(db_column='bIgnoreNonWeaponExplosions', blank=True, null=True)
    bignoreroadkills = models.IntegerField(db_column='bIgnoreRoadKills', blank=True, null=True)
    bignoresuicideoob = models.IntegerField(db_column='bIgnoreSuicideOOB', blank=True, null=True)
    bignoresuicidewithoutassist = models.IntegerField(db_column='bIgnoreSuicideWithoutAssist', blank=True, null=True)
    bignoresuicidewithoutenemyassist = models.IntegerField(db_column='bIgnoreSuicideWithoutEnemyAssist', blank=True, null=True)
    bignoresuicidewithoutfriendlyassist = models.IntegerField(db_column='bIgnoreSuicideWithoutFriendlyAssist', blank=True, null=True)
    bsetdeathmatchtarget = models.IntegerField(db_column='bSetDeathMatchTarget', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Minigames_BlockFDM'


class MinigamesGoldengun(models.Model):
    id = models.IntegerField(primary_key=True)
    spickupasset = models.TextField(db_column='sPickupAsset', blank=True, null=True)
    spickupsfx = models.TextField(db_column='sPickupSFX', blank=True, null=True)
    spickupvfx = models.TextField(db_column='sPickupVFX', blank=True, null=True)
    eminigame = models.IntegerField(db_column='eMinigame', blank=True, null=True)
    eonmissionprotagonisthudmarker = models.IntegerField(db_column='eOnMissionProtagonistHUDMarker', blank=True, null=True)
    eoutofmissionprotagonisthudmarker = models.IntegerField(db_column='eOutOfMissionProtagonistHUDMarker', blank=True, null=True)
    fmaxpickuptime = models.FloatField(db_column='fMaxPickupTime', blank=True, null=True)
    fremovealivetime = models.FloatField(db_column='fRemoveAliveTime', blank=True, null=True)
    fremovedeadtime = models.FloatField(db_column='fRemoveDeadTime', blank=True, null=True)
    fremovedistance = models.FloatField(db_column='fRemoveDistance', blank=True, null=True)
    ftotalminigametimeouttime = models.FloatField(db_column='fTotalMinigameTimeoutTime', blank=True, null=True)
    nkilltarget = models.IntegerField(db_column='nKillTarget', blank=True, null=True)
    busesingleteam = models.IntegerField(db_column='bUseSingleTeam', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Minigames_GoldenGun'


class MinigamesGungame(models.Model):
    id = models.IntegerField(primary_key=True)
    eminigame = models.IntegerField(db_column='eMinigame', blank=True, null=True)
    eweaponsetup = models.IntegerField(db_column='eWeaponSetup', blank=True, null=True)
    fdeadparticipationtimer = models.FloatField(db_column='fDeadParticipationTimer', blank=True, null=True)
    fminrespawndistance = models.FloatField(db_column='fMinRespawnDistance', blank=True, null=True)
    foobparticipationtimer = models.FloatField(db_column='fOOBParticipationTimer', blank=True, null=True)
    foutofboundstime = models.FloatField(db_column='fOutOfBoundsTime', blank=True, null=True)
    ftotalgametimeout = models.FloatField(db_column='fTotalGameTimeout', blank=True, null=True)
    nacckillchangeonarrest = models.IntegerField(db_column='nAccKillChangeOnArrest', blank=True, null=True)
    nacckillchangeondeath = models.IntegerField(db_column='nAccKillChangeOnDeath', blank=True, null=True)
    nacckillchangeonnonweapondeath = models.IntegerField(db_column='nAccKillChangeOnNonWeaponDeath', blank=True, null=True)
    nacckillchangeonsuicide = models.IntegerField(db_column='nAccKillChangeOnSuicide', blank=True, null=True)
    naccscorechangeonarrest = models.IntegerField(db_column='nAccScoreChangeOnArrest', blank=True, null=True)
    naccscorechangeondeath = models.IntegerField(db_column='nAccScoreChangeOnDeath', blank=True, null=True)
    naccscorechangeonnonweapondeath = models.IntegerField(db_column='nAccScoreChangeOnNonWeaponDeath', blank=True, null=True)
    naccscorechangeonsuicide = models.IntegerField(db_column='nAccScoreChangeOnSuicide', blank=True, null=True)
    nlevelchangeonarrest = models.IntegerField(db_column='nLevelChangeOnArrest', blank=True, null=True)
    nlevelchangeondeath = models.IntegerField(db_column='nLevelChangeOnDeath', blank=True, null=True)
    nlevelchangeonnonweapondeath = models.IntegerField(db_column='nLevelChangeOnNonWeaponDeath', blank=True, null=True)
    nlevelchangeonsuicide = models.IntegerField(db_column='nLevelChangeOnSuicide', blank=True, null=True)
    nscorelimit = models.IntegerField(db_column='nScoreLimit', blank=True, null=True)
    ballowscorelevelup = models.IntegerField(db_column='bAllowScoreLevelUp', blank=True, null=True)
    bcountarrests = models.IntegerField(db_column='bCountArrests', blank=True, null=True)
    bcountassignedsuicides = models.IntegerField(db_column='bCountAssignedSuicides', blank=True, null=True)
    bcountnonweaponkills = models.IntegerField(db_column='bCountNonWeaponKills', blank=True, null=True)
    bdisablepostitivemedalscore = models.IntegerField(db_column='bDisablePostitiveMedalScore', blank=True, null=True)
    bforcelastweapononscorelimit = models.IntegerField(db_column='bForceLastWeaponOnScoreLimit', blank=True, null=True)
    blockoutofarea = models.IntegerField(db_column='bLockOutOfArea', blank=True, null=True)
    bmultiplyaccscorechanges = models.IntegerField(db_column='bMultiplyAccScoreChanges', blank=True, null=True)
    breducelevelonnegativeacckills = models.IntegerField(db_column='bReduceLevelOnNegativeAccKills', blank=True, null=True)
    breducelevelonnegativeaccscore = models.IntegerField(db_column='bReduceLevelOnNegativeAccScore', blank=True, null=True)
    brequirekillwithfinalweapon = models.IntegerField(db_column='bRequireKillWithFinalWeapon', blank=True, null=True)
    bscorenonweaponkills = models.IntegerField(db_column='bScoreNonWeaponKills', blank=True, null=True)
    bspawncompletelyrandom = models.IntegerField(db_column='bSpawnCompletelyRandom', blank=True, null=True)
    busesingleteam = models.IntegerField(db_column='bUseSingleTeam', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Minigames_GunGame'


class MinigamesInfection(models.Model):
    id = models.IntegerField(primary_key=True)
    eendblockidentifier = models.IntegerField(db_column='eEndBlockIdentifier', blank=True, null=True)
    eminigame = models.IntegerField(db_column='eMinigame', blank=True, null=True)
    eprotagonistonmissionhudmarker = models.IntegerField(db_column='eProtagonistOnMissionHUDMarker', blank=True, null=True)
    esurvivorpinghudmarker = models.IntegerField(db_column='eSurvivorPingHUDMarker', blank=True, null=True)
    finfectedmajoritytimer = models.FloatField(db_column='fInfectedMajorityTimer', blank=True, null=True)
    finfectedscoremultipliermax = models.FloatField(db_column='fInfectedScoreMultiplierMax', blank=True, null=True)
    finfectedscoremultipliermin = models.FloatField(db_column='fInfectedScoreMultiplierMin', blank=True, null=True)
    fminimumsurvivoraddtime = models.FloatField(db_column='fMinimumSurvivorAddTime', blank=True, null=True)
    fnosurvivorslefttimer = models.FloatField(db_column='fNoSurvivorsLeftTimer', blank=True, null=True)
    fprotagonistkillscoremultiplier = models.FloatField(db_column='fProtagonistKillScoreMultiplier', blank=True, null=True)
    fprotagonistscoremultipliermax = models.FloatField(db_column='fProtagonistScoreMultiplierMax', blank=True, null=True)
    fprotagonistscoremultipliermin = models.FloatField(db_column='fProtagonistScoreMultiplierMin', blank=True, null=True)
    fsurvivormajorityratio = models.FloatField(db_column='fSurvivorMajorityRatio', blank=True, null=True)
    fsurvivorpingduration = models.FloatField(db_column='fSurvivorPingDuration', blank=True, null=True)
    fsurvivorpinginterval = models.FloatField(db_column='fSurvivorPingInterval', blank=True, null=True)
    fsurvivorscoremultipliermax = models.FloatField(db_column='fSurvivorScoreMultiplierMax', blank=True, null=True)
    fsurvivorscoremultipliermin = models.FloatField(db_column='fSurvivorScoreMultiplierMin', blank=True, null=True)
    ftotalgametimeout = models.FloatField(db_column='fTotalGameTimeout', blank=True, null=True)
    badjustassistscore = models.IntegerField(db_column='bAdjustAssistScore', blank=True, null=True)
    badjustmedalscore = models.IntegerField(db_column='bAdjustMedalScore', blank=True, null=True)
    badjustnegativescore = models.IntegerField(db_column='bAdjustNegativeScore', blank=True, null=True)
    badjustnonplayerkillinfrarewards = models.IntegerField(db_column='bAdjustNonPlayerKillInfraRewards', blank=True, null=True)
    badjustplayerconvertedleaderscore = models.IntegerField(db_column='bAdjustPlayerConvertedLeaderScore', blank=True, null=True)
    badjustplayerconvertedscore = models.IntegerField(db_column='bAdjustPlayerConvertedScore', blank=True, null=True)
    bendminigameinblock = models.IntegerField(db_column='bEndMinigameInBlock', blank=True, null=True)
    bkillallinfectedatstop = models.IntegerField(db_column='bKillAllInfectedAtStop', blank=True, null=True)
    bkillallplayersatstop = models.IntegerField(db_column='bKillAllPlayersAtStop', blank=True, null=True)
    bkillplayerbecomingprotagonist = models.IntegerField(db_column='bKillPlayerBecomingProtagonist', blank=True, null=True)
    bleaderbecomessurvivorwhenkilled = models.IntegerField(db_column='bLeaderBecomesSurvivorWhenKilled', blank=True, null=True)
    bprotagonistpingswithsurvivors = models.IntegerField(db_column='bProtagonistPingsWithSurvivors', blank=True, null=True)
    bprotagonistvisibleduringsurvivormajority = models.IntegerField(db_column='bProtagonistVisibleDuringSurvivorMajority', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Minigames_Infection'


class MinigamesInfectionItemcollection(models.Model):
    id = models.IntegerField(primary_key=True)
    eitemtype = models.IntegerField(db_column='eItemType', blank=True, null=True)
    eminigame_infection = models.IntegerField(db_column='eMinigame_Infection', blank=True, null=True)
    etaskitemoperation = models.IntegerField(db_column='eTaskItemOperation', blank=True, null=True)
    ffailedspawnretrytimer = models.FloatField(db_column='fFailedSpawnRetryTimer', blank=True, null=True)
    fitemcollectiontimeout = models.FloatField(db_column='fItemCollectionTimeout', blank=True, null=True)
    navailabletaskitems = models.IntegerField(db_column='nAvailableTaskItems', blank=True, null=True)
    nminimumitemstaken = models.IntegerField(db_column='nMinimumItemsTaken', blank=True, null=True)
    nrequiredtaskitemcounts = models.IntegerField(db_column='nRequiredTaskItemCounts', blank=True, null=True)
    nspawnercount = models.IntegerField(db_column='nSpawnerCount', blank=True, null=True)
    ntargetitemstaken = models.IntegerField(db_column='nTargetItemsTaken', blank=True, null=True)
    bblockpickups = models.IntegerField(db_column='bBlockPickups', blank=True, null=True)
    bcandeliveritems = models.IntegerField(db_column='bCanDeliverItems', blank=True, null=True)
    bcandropsmallitems = models.IntegerField(db_column='bCanDropSmallItems', blank=True, null=True)
    bcountdelivereditems = models.IntegerField(db_column='bCountDeliveredItems', blank=True, null=True)
    bcountdestroyeditems = models.IntegerField(db_column='bCountDestroyedItems', blank=True, null=True)
    bcountpickedupitems = models.IntegerField(db_column='bCountPickedUpItems', blank=True, null=True)
    bitemsinsingleblock = models.IntegerField(db_column='bItemsInSingleBlock', blank=True, null=True)
    bleaderassignedbyscore = models.IntegerField(db_column='bLeaderAssignedByScore', blank=True, null=True)
    blimitspawnerstoselectedblock = models.IntegerField(db_column='bLimitSpawnersToSelectedBlock', blank=True, null=True)
    brespawndelivereditems = models.IntegerField(db_column='bRespawnDeliveredItems', blank=True, null=True)
    brespawndestroyeditems = models.IntegerField(db_column='bRespawnDestroyedItems', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Minigames_Infection_ItemCollection'


class MinigamesInfectionRichfx(models.Model):
    id = models.IntegerField(primary_key=True)
    sendstagemusic_start = models.TextField(db_column='sEndStageMusic_Start', blank=True, null=True)
    sendstagemusic_stop = models.TextField(db_column='sEndStageMusic_Stop', blank=True, null=True)
    soverrideweather = models.TextField(db_column='sOverrideWeather', blank=True, null=True)
    einfectedspawnfx_female = models.IntegerField(db_column='eInfectedSpawnFX_Female', blank=True, null=True)
    einfectedspawnfx_male = models.IntegerField(db_column='eInfectedSpawnFX_Male', blank=True, null=True)
    eminigame_infection = models.IntegerField(db_column='eMinigame_Infection', blank=True, null=True)
    eplayerpingfx = models.IntegerField(db_column='ePlayerPingFX', blank=True, null=True)
    eprotagonistassignedfx = models.IntegerField(db_column='eProtagonistAssignedFX', blank=True, null=True)
    eprotagonistkillfx = models.IntegerField(db_column='eProtagonistKillFX', blank=True, null=True)
    eprotagonistspawnfx_female = models.IntegerField(db_column='eProtagonistSpawnFX_Female', blank=True, null=True)
    eprotagonistspawnfx_male = models.IntegerField(db_column='eProtagonistSpawnFX_Male', blank=True, null=True)
    nendtodhours = models.IntegerField(db_column='nEndToDHours', blank=True, null=True)
    nendtodminutes = models.IntegerField(db_column='nEndToDMinutes', blank=True, null=True)
    npausetodhours = models.IntegerField(db_column='nPauseToDHours', blank=True, null=True)
    npausetodminutes = models.IntegerField(db_column='nPauseToDMinutes', blank=True, null=True)
    bendtodstartswithinfectedmajority = models.IntegerField(db_column='bEndToDStartsWithInfectedMajority', blank=True, null=True)
    bforcerestoreweather = models.IntegerField(db_column='bForceRestoreWeather', blank=True, null=True)
    bpausetod = models.IntegerField(db_column='bPauseToD', blank=True, null=True)
    bplayprotagonistkillfromkilledlocation = models.IntegerField(db_column='bPlayProtagonistKillFromKilledLocation', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Minigames_Infection_RichFX'


class MinigamesInfectionVip(models.Model):
    id = models.IntegerField(primary_key=True)
    eminigame_infection = models.IntegerField(db_column='eMinigame_Infection', blank=True, null=True)
    nlowheatgroupchance = models.IntegerField(db_column='nLowHeatGroupChance', blank=True, null=True)
    nmaxheatgroupchance = models.IntegerField(db_column='nMaxHeatGroupChance', blank=True, null=True)
    nmaxheatungroupedchance = models.IntegerField(db_column='nMaxHeatUngroupedChance', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Minigames_Infection_VIP'


class MinigamesMug(models.Model):
    id = models.IntegerField(primary_key=True)
    splayerinmugrangeaudio = models.TextField(db_column='sPlayerInMugRangeAudio', blank=True, null=True)
    ecarrierhudmarker_0 = models.IntegerField(db_column='eCarrierHUDMarker_0', blank=True, null=True)
    ecarrierhudmarker_1 = models.IntegerField(db_column='eCarrierHUDMarker_1', blank=True, null=True)
    ecarrierhudmarker_2 = models.IntegerField(db_column='eCarrierHUDMarker_2', blank=True, null=True)
    ecarrierhudmarker_3 = models.IntegerField(db_column='eCarrierHUDMarker_3', blank=True, null=True)
    ecarrierhudmarker_4 = models.IntegerField(db_column='eCarrierHUDMarker_4', blank=True, null=True)
    edeliveryeffect_0 = models.IntegerField(db_column='eDeliveryEffect_0', blank=True, null=True)
    edeliveryeffect_1 = models.IntegerField(db_column='eDeliveryEffect_1', blank=True, null=True)
    edeliveryeffect_2 = models.IntegerField(db_column='eDeliveryEffect_2', blank=True, null=True)
    edeliveryeffect_3 = models.IntegerField(db_column='eDeliveryEffect_3', blank=True, null=True)
    einvulerableeffect = models.IntegerField(db_column='eInvulerableEffect', blank=True, null=True)
    eitemspawnrule_0 = models.IntegerField(db_column='eItemSpawnRule_0', blank=True, null=True)
    eitemspawnrule_1 = models.IntegerField(db_column='eItemSpawnRule_1', blank=True, null=True)
    ekillcarriereffect = models.IntegerField(db_column='eKillCarrierEffect', blank=True, null=True)
    eminigame = models.IntegerField(db_column='eMinigame', blank=True, null=True)
    emugcompleteeffect = models.IntegerField(db_column='eMugCompleteEffect', blank=True, null=True)
    enpchudmarker_0 = models.IntegerField(db_column='eNPCHudMarker_0', blank=True, null=True)
    enpchudmarker_1 = models.IntegerField(db_column='eNPCHudMarker_1', blank=True, null=True)
    enpckillitemspawnrule_0 = models.IntegerField(db_column='eNPCKillItemSpawnRule_0', blank=True, null=True)
    enpckillitemspawnrule_1 = models.IntegerField(db_column='eNPCKillItemSpawnRule_1', blank=True, null=True)
    enpcoperation_0 = models.IntegerField(db_column='eNPCOperation_0', blank=True, null=True)
    enpcoperation_1 = models.IntegerField(db_column='eNPCOperation_1', blank=True, null=True)
    enpctype_0 = models.IntegerField(db_column='eNPCType_0', blank=True, null=True)
    enpctype_1 = models.IntegerField(db_column='eNPCType_1', blank=True, null=True)
    eoomcarrierhudmarker_0 = models.IntegerField(db_column='eOOMCarrierHUDMarker_0', blank=True, null=True)
    eoomcarrierhudmarker_1 = models.IntegerField(db_column='eOOMCarrierHUDMarker_1', blank=True, null=True)
    eoomcarrierhudmarker_2 = models.IntegerField(db_column='eOOMCarrierHUDMarker_2', blank=True, null=True)
    eoomcarrierhudmarker_3 = models.IntegerField(db_column='eOOMCarrierHUDMarker_3', blank=True, null=True)
    eoomcarrierhudmarker_4 = models.IntegerField(db_column='eOOMCarrierHUDMarker_4', blank=True, null=True)
    eoomprotagonisthudmarker = models.IntegerField(db_column='eOOMProtagonistHUDMarker', blank=True, null=True)
    eprotagonisthudmarker = models.IntegerField(db_column='eProtagonistHUDMarker', blank=True, null=True)
    etaskitemhudmarker = models.IntegerField(db_column='eTaskItemHudMarker', blank=True, null=True)
    etaskitemoperation = models.IntegerField(db_column='eTaskItemOperation', blank=True, null=True)
    fdeliverymultiplier_0 = models.FloatField(db_column='fDeliveryMultiplier_0', blank=True, null=True)
    fdeliverymultiplier_1 = models.FloatField(db_column='fDeliveryMultiplier_1', blank=True, null=True)
    fdeliverymultiplier_2 = models.FloatField(db_column='fDeliveryMultiplier_2', blank=True, null=True)
    fdeliverymultiplier_3 = models.FloatField(db_column='fDeliveryMultiplier_3', blank=True, null=True)
    fimmunityaudiotime = models.FloatField(db_column='fImmunityAudioTime', blank=True, null=True)
    fimmunitytimeout = models.FloatField(db_column='fImmunityTimeout', blank=True, null=True)
    finactivitytimeouttime = models.FloatField(db_column='fInactivityTimeoutTime', blank=True, null=True)
    fmaxnpctime = models.FloatField(db_column='fMaxNPCTime', blank=True, null=True)
    fnodropkilltransfer = models.FloatField(db_column='fNoDropKillTransfer', blank=True, null=True)
    fnodropmugtransfer = models.FloatField(db_column='fNoDropMugTransfer', blank=True, null=True)
    fnodropsuicidepenalty = models.FloatField(db_column='fNoDropSuicidePenalty', blank=True, null=True)
    fnpcchance_0 = models.FloatField(db_column='fNPCChance_0', blank=True, null=True)
    fnpcchance_1 = models.FloatField(db_column='fNPCChance_1', blank=True, null=True)
    fnpccountperplayer = models.FloatField(db_column='fNPCCountPerPlayer', blank=True, null=True)
    fnpcmugimmunityduration = models.FloatField(db_column='fNPCMugImmunityDuration', blank=True, null=True)
    fplayermugimmunityduration = models.FloatField(db_column='fPlayerMugImmunityDuration', blank=True, null=True)
    fpostimmunitymugtimeout = models.FloatField(db_column='fPostImmunityMugTimeout', blank=True, null=True)
    fprotagonistkillmultiplier = models.FloatField(db_column='fProtagonistKillMultiplier', blank=True, null=True)
    fremovedistance = models.FloatField(db_column='fRemoveDistance', blank=True, null=True)
    fremovetimealive = models.FloatField(db_column='fRemoveTimeAlive', blank=True, null=True)
    fremovetimedead = models.FloatField(db_column='fRemoveTimeDead', blank=True, null=True)
    frespawnwithitemsimmunity = models.FloatField(db_column='fRespawnWithItemsImmunity', blank=True, null=True)
    ftaskitemcleanuptime = models.FloatField(db_column='fTaskItemCleanupTime', blank=True, null=True)
    ftotalminigametimeouttime = models.FloatField(db_column='fTotalMinigameTimeoutTime', blank=True, null=True)
    ndeliverlimit = models.IntegerField(db_column='nDeliverLimit', blank=True, null=True)
    nnpccount = models.IntegerField(db_column='nNPCCount', blank=True, null=True)
    nnpccountlimit = models.IntegerField(db_column='nNPCCountLimit', blank=True, null=True)
    noverridekillscore = models.IntegerField(db_column='nOverrideKillScore', blank=True, null=True)
    bcandropoffitems = models.IntegerField(db_column='bCanDropOffItems', blank=True, null=True)
    bcanmugplayers = models.IntegerField(db_column='bCanMugPlayers', blank=True, null=True)
    bdisableprimaryscore = models.IntegerField(db_column='bDisablePrimaryScore', blank=True, null=True)
    bhideplayerradarmarkers = models.IntegerField(db_column='bHidePlayerRadarMarkers', blank=True, null=True)
    bkillmuggedplayers = models.IntegerField(db_column='bKillMuggedPlayers', blank=True, null=True)
    bkillnpcwhendone = models.IntegerField(db_column='bKillNPCWhenDone', blank=True, null=True)
    bkillnpcwhendonemugging = models.IntegerField(db_column='bKillNPCWhenDoneMugging', blank=True, null=True)
    bmultimug = models.IntegerField(db_column='bMultiMug', blank=True, null=True)
    bmultiplydelivereditemnumbers = models.IntegerField(db_column='bMultiplyDeliveredItemNumbers', blank=True, null=True)
    bnodrops = models.IntegerField(db_column='bNoDrops', blank=True, null=True)
    bnodroptransfergainonly = models.IntegerField(db_column='bNoDropTransferGainOnly', blank=True, null=True)
    bnpcmarkersafterfirstmug = models.IntegerField(db_column='bNPCMarkersAfterFirstMug', blank=True, null=True)
    bnpcmugusesimmunitytimeout = models.IntegerField(db_column='bNPCMugUsesImmunityTimeout', blank=True, null=True)
    bopposeallcarriers = models.IntegerField(db_column='bOpposeAllCarriers', blank=True, null=True)
    boverridetitle = models.IntegerField(db_column='bOverrideTitle', blank=True, null=True)
    bpvpunlockallcarriers = models.IntegerField(db_column='bPvPUnlockAllCarriers', blank=True, null=True)
    bpvpunlockprotagonist = models.IntegerField(db_column='bPVPUnlockProtagonist', blank=True, null=True)
    bshowcarrierstoall = models.IntegerField(db_column='bShowCarriersToAll', blank=True, null=True)
    busedeliverymultipliers = models.IntegerField(db_column='bUseDeliveryMultipliers', blank=True, null=True)
    busesingleteam = models.IntegerField(db_column='bUseSingleTeam', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Minigames_Mug'


class MinigamesVip(models.Model):
    id = models.IntegerField(primary_key=True)
    eminigame = models.IntegerField(db_column='eMinigame', blank=True, null=True)
    fvipwintime = models.FloatField(db_column='fVIPWinTime', blank=True, null=True)
    nlowheatgroupchance = models.IntegerField(db_column='nLowHeatGroupChance', blank=True, null=True)
    nmaxheatgroupchance = models.IntegerField(db_column='nMaxHeatGroupChance', blank=True, null=True)
    nmaxheatungroupedchance = models.IntegerField(db_column='nMaxHeatUngroupedChance', blank=True, null=True)
    nvipwinkills = models.IntegerField(db_column='nVIPWinKills', blank=True, null=True)
    bbulklog = models.IntegerField(db_column='bBulkLog', blank=True, null=True)
    bkillbodyguardsatstart = models.IntegerField(db_column='bKillBodyGuardsAtStart', blank=True, null=True)
    bkillvipatstart = models.IntegerField(db_column='bKillVIPAtStart', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Minigames_VIP'


class Missionofcriminalcontacts(models.Model):
    id = models.IntegerField(primary_key=True)
    econtact = models.IntegerField(db_column='eContact', blank=True, null=True)
    emission = models.IntegerField(db_column='eMission', blank=True, null=True)
    emissionofcriminalcontact = models.IntegerField(db_column='eMissionOfCriminalContact', blank=True, null=True)
    nmaxlevel = models.IntegerField(db_column='nMaxLevel', blank=True, null=True)
    nminlevel = models.IntegerField(db_column='nMinLevel', blank=True, null=True)
    bdisabled = models.IntegerField(db_column='bDisabled', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MissionOfCriminalContacts'


class Missionofenforcercontacts(models.Model):
    id = models.IntegerField(primary_key=True)
    econtact = models.IntegerField(db_column='eContact', blank=True, null=True)
    emission = models.IntegerField(db_column='eMission', blank=True, null=True)
    emissionofenforcercontact = models.IntegerField(db_column='eMissionOfEnforcerContact', blank=True, null=True)
    nmaxlevel = models.IntegerField(db_column='nMaxLevel', blank=True, null=True)
    nminlevel = models.IntegerField(db_column='nMinLevel', blank=True, null=True)
    bdisabled = models.IntegerField(db_column='bDisabled', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MissionOfEnforcerContacts'


class Missionresultreasons(models.Model):
    id = models.IntegerField(primary_key=True)
    sdrawmessage = models.TextField(db_column='sDrawMessage', blank=True, null=True)
    slosemessage = models.TextField(db_column='sLoseMessage', blank=True, null=True)
    swinmessage = models.TextField(db_column='sWinMessage', blank=True, null=True)
    emissionresultreason = models.IntegerField(db_column='eMissionResultReason', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MissionResultReasons'


class Missionrewardpackages(models.Model):
    id = models.IntegerField(primary_key=True)
    emissionrewardpackage = models.IntegerField(db_column='eMissionRewardPackage', blank=True, null=True)
    nbasecash_0 = models.IntegerField(db_column='nBaseCash_0', blank=True, null=True)
    nbasecash_1 = models.IntegerField(db_column='nBaseCash_1', blank=True, null=True)
    nbasecontactstanding_0 = models.IntegerField(db_column='nBaseContactStanding_0', blank=True, null=True)
    nbasecontactstanding_1 = models.IntegerField(db_column='nBaseContactStanding_1', blank=True, null=True)
    nscore = models.IntegerField(db_column='nScore', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MissionRewardPackages'


class Missionsystemfilterentries(models.Model):
    id = models.IntegerField(primary_key=True)
    emissionsystemfilter = models.IntegerField(db_column='eMissionSystemFilter', blank=True, null=True)
    emissionsystem = models.IntegerField(db_column='eMissionSystem', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MissionSystemFilterEntries'


class Missionsystemfilters(models.Model):
    id = models.IntegerField(primary_key=True)
    emissionsystemfilter = models.IntegerField(db_column='eMissionSystemFilter', blank=True, null=True)
    bexclusive = models.IntegerField(db_column='bExclusive', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MissionSystemFilters'


class Missiontakeoutlookup(models.Model):
    id = models.IntegerField(primary_key=True)
    nmissiontakeoutlookup = models.IntegerField(db_column='nMissionTakeoutLookUp', blank=True, null=True)
    ntakeoutlimit = models.IntegerField(db_column='nTakeoutLimit', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MissionTakeoutLookUp'


class Missiontemplateuiprofiles(models.Model):
    id = models.IntegerField(primary_key=True)
    strackedvaluedescription_0 = models.TextField(db_column='sTrackedValueDescription_0', blank=True, null=True)
    strackedvaluedescription_1 = models.TextField(db_column='sTrackedValueDescription_1', blank=True, null=True)
    strackedvaluedescription_2 = models.TextField(db_column='sTrackedValueDescription_2', blank=True, null=True)
    strackedvaluedescription_3 = models.TextField(db_column='sTrackedValueDescription_3', blank=True, null=True)
    strackedvalueimage_0 = models.TextField(db_column='sTrackedValueImage_0', blank=True, null=True)
    strackedvalueimage_1 = models.TextField(db_column='sTrackedValueImage_1', blank=True, null=True)
    strackedvalueimage_2 = models.TextField(db_column='sTrackedValueImage_2', blank=True, null=True)
    strackedvalueimage_3 = models.TextField(db_column='sTrackedValueImage_3', blank=True, null=True)
    emissiontemplateuiprofile = models.IntegerField(db_column='eMissionTemplateUIProfile', blank=True, null=True)
    etrackedvaluebarfgdisabled_0 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_0', blank=True, null=True)
    etrackedvaluebarfgdisabled_1 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_1', blank=True, null=True)
    etrackedvaluebarfgdisabled_2 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_2', blank=True, null=True)
    etrackedvaluebarfgdisabled_3 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_3', blank=True, null=True)
    etrackedvaluebg_0 = models.IntegerField(db_column='eTrackedValueBg_0', blank=True, null=True)
    etrackedvaluebg_1 = models.IntegerField(db_column='eTrackedValueBg_1', blank=True, null=True)
    etrackedvaluebg_2 = models.IntegerField(db_column='eTrackedValueBg_2', blank=True, null=True)
    etrackedvaluebg_3 = models.IntegerField(db_column='eTrackedValueBg_3', blank=True, null=True)
    etrackedvaluefg_0 = models.IntegerField(db_column='eTrackedValueFg_0', blank=True, null=True)
    etrackedvaluefg_1 = models.IntegerField(db_column='eTrackedValueFg_1', blank=True, null=True)
    etrackedvaluefg_2 = models.IntegerField(db_column='eTrackedValueFg_2', blank=True, null=True)
    etrackedvaluefg_3 = models.IntegerField(db_column='eTrackedValueFg_3', blank=True, null=True)
    etrackedvaluesocket_0 = models.IntegerField(db_column='eTrackedValueSocket_0', blank=True, null=True)
    etrackedvaluesocket_1 = models.IntegerField(db_column='eTrackedValueSocket_1', blank=True, null=True)
    etrackedvaluesocket_2 = models.IntegerField(db_column='eTrackedValueSocket_2', blank=True, null=True)
    etrackedvaluesocket_3 = models.IntegerField(db_column='eTrackedValueSocket_3', blank=True, null=True)
    etrackedvalue_0 = models.IntegerField(db_column='eTrackedValue_0', blank=True, null=True)
    etrackedvalue_1 = models.IntegerField(db_column='eTrackedValue_1', blank=True, null=True)
    etrackedvalue_2 = models.IntegerField(db_column='eTrackedValue_2', blank=True, null=True)
    etrackedvalue_3 = models.IntegerField(db_column='eTrackedValue_3', blank=True, null=True)
    etrackedvaluedisplay_0 = models.IntegerField(db_column='eTrackedValueDisplay_0', blank=True, null=True)
    etrackedvaluedisplay_1 = models.IntegerField(db_column='eTrackedValueDisplay_1', blank=True, null=True)
    etrackedvaluedisplay_2 = models.IntegerField(db_column='eTrackedValueDisplay_2', blank=True, null=True)
    etrackedvaluedisplay_3 = models.IntegerField(db_column='eTrackedValueDisplay_3', blank=True, null=True)
    bflashwhenchanged_0 = models.IntegerField(db_column='bFlashWhenChanged_0', blank=True, null=True)
    bflashwhenchanged_1 = models.IntegerField(db_column='bFlashWhenChanged_1', blank=True, null=True)
    bflashwhenchanged_2 = models.IntegerField(db_column='bFlashWhenChanged_2', blank=True, null=True)
    bflashwhenchanged_3 = models.IntegerField(db_column='bFlashWhenChanged_3', blank=True, null=True)
    bhideatmax_0 = models.IntegerField(db_column='bHideAtMax_0', blank=True, null=True)
    bhideatmax_1 = models.IntegerField(db_column='bHideAtMax_1', blank=True, null=True)
    bhideatmax_2 = models.IntegerField(db_column='bHideAtMax_2', blank=True, null=True)
    bhideatmax_3 = models.IntegerField(db_column='bHideAtMax_3', blank=True, null=True)
    bhidewhenone_0 = models.IntegerField(db_column='bHideWhenOne_0', blank=True, null=True)
    bhidewhenone_1 = models.IntegerField(db_column='bHideWhenOne_1', blank=True, null=True)
    bhidewhenone_2 = models.IntegerField(db_column='bHideWhenOne_2', blank=True, null=True)
    bhidewhenone_3 = models.IntegerField(db_column='bHideWhenOne_3', blank=True, null=True)
    bhidewhenoppositionviptakeoutsdisabled_0 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_0', blank=True, null=True)
    bhidewhenoppositionviptakeoutsdisabled_1 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_1', blank=True, null=True)
    bhidewhenoppositionviptakeoutsdisabled_2 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_2', blank=True, null=True)
    bhidewhenoppositionviptakeoutsdisabled_3 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_3', blank=True, null=True)
    bhidewhenownerviptakeoutsdisabled_0 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_0', blank=True, null=True)
    bhidewhenownerviptakeoutsdisabled_1 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_1', blank=True, null=True)
    bhidewhenownerviptakeoutsdisabled_2 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_2', blank=True, null=True)
    bhidewhenownerviptakeoutsdisabled_3 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_3', blank=True, null=True)
    bhidewhenpointsdisabled_0 = models.IntegerField(db_column='bHideWhenPointsDisabled_0', blank=True, null=True)
    bhidewhenpointsdisabled_1 = models.IntegerField(db_column='bHideWhenPointsDisabled_1', blank=True, null=True)
    bhidewhenpointsdisabled_2 = models.IntegerField(db_column='bHideWhenPointsDisabled_2', blank=True, null=True)
    bhidewhenpointsdisabled_3 = models.IntegerField(db_column='bHideWhenPointsDisabled_3', blank=True, null=True)
    bhidewhentakeoutsdisabled_0 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_0', blank=True, null=True)
    bhidewhentakeoutsdisabled_1 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_1', blank=True, null=True)
    bhidewhentakeoutsdisabled_2 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_2', blank=True, null=True)
    bhidewhentakeoutsdisabled_3 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_3', blank=True, null=True)
    bhidewhenunopposed_0 = models.IntegerField(db_column='bHideWhenUnopposed_0', blank=True, null=True)
    bhidewhenunopposed_1 = models.IntegerField(db_column='bHideWhenUnopposed_1', blank=True, null=True)
    bhidewhenunopposed_2 = models.IntegerField(db_column='bHideWhenUnopposed_2', blank=True, null=True)
    bhidewhenunopposed_3 = models.IntegerField(db_column='bHideWhenUnopposed_3', blank=True, null=True)
    btrackedvalueinlocaloverview_0 = models.IntegerField(db_column='bTrackedValueInLocalOverview_0', blank=True, null=True)
    btrackedvalueinlocaloverview_1 = models.IntegerField(db_column='bTrackedValueInLocalOverview_1', blank=True, null=True)
    btrackedvalueinlocaloverview_2 = models.IntegerField(db_column='bTrackedValueInLocalOverview_2', blank=True, null=True)
    btrackedvalueinlocaloverview_3 = models.IntegerField(db_column='bTrackedValueInLocalOverview_3', blank=True, null=True)
    btrackedvalueinremoteoverview_0 = models.IntegerField(db_column='bTrackedValueInRemoteOverview_0', blank=True, null=True)
    btrackedvalueinremoteoverview_1 = models.IntegerField(db_column='bTrackedValueInRemoteOverview_1', blank=True, null=True)
    btrackedvalueinremoteoverview_2 = models.IntegerField(db_column='bTrackedValueInRemoteOverview_2', blank=True, null=True)
    btrackedvalueinremoteoverview_3 = models.IntegerField(db_column='bTrackedValueInRemoteOverview_3', blank=True, null=True)
    btrackedvalueonhud_0 = models.IntegerField(db_column='bTrackedValueOnHUD_0', blank=True, null=True)
    btrackedvalueonhud_1 = models.IntegerField(db_column='bTrackedValueOnHUD_1', blank=True, null=True)
    btrackedvalueonhud_2 = models.IntegerField(db_column='bTrackedValueOnHUD_2', blank=True, null=True)
    btrackedvalueonhud_3 = models.IntegerField(db_column='bTrackedValueOnHUD_3', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MissionTemplateUIProfiles'


class Missiontemplates(models.Model):
    id = models.IntegerField(primary_key=True)
    smissiontitle = models.TextField(db_column='sMissionTitle', blank=True, null=True)
    emissiontemplate = models.IntegerField(db_column='eMissionTemplate', blank=True, null=True)
    emissiontypefilter = models.IntegerField(db_column='eMissionTypeFilter', blank=True, null=True)
    emissionuioppositionprofile = models.IntegerField(db_column='eMissionUIOppositionProfile', blank=True, null=True)
    emissionuiownerprofile = models.IntegerField(db_column='eMissionUIOwnerProfile', blank=True, null=True)
    epurpose = models.IntegerField(db_column='ePurpose', blank=True, null=True)
    erarity = models.IntegerField(db_column='eRarity', blank=True, null=True)
    erewardpackage = models.IntegerField(db_column='eRewardPackage', blank=True, null=True)
    fowningsidebias = models.FloatField(db_column='fOwningSideBias', blank=True, null=True)
    ncomplexity = models.IntegerField(db_column='nComplexity', blank=True, null=True)
    ngroupsizemax = models.IntegerField(db_column='nGroupSizeMax', blank=True, null=True)
    ngroupsizemin = models.IntegerField(db_column='nGroupSizeMin', blank=True, null=True)
    nopposingsideviplives = models.IntegerField(db_column='nOpposingSideVIPLives', blank=True, null=True)
    nowningsideviplives = models.IntegerField(db_column='nOwningSideVIPLives', blank=True, null=True)
    nrespawntime = models.IntegerField(db_column='nRespawnTime', blank=True, null=True)
    nrespawntimeincrement = models.IntegerField(db_column='nRespawnTimeIncrement', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    nsimultaneouscap = models.IntegerField(db_column='nSimultaneousCap', blank=True, null=True)
    ntakeoutcount = models.IntegerField(db_column='nTakeoutCount', blank=True, null=True)
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)
    etimeofdayavailability = models.IntegerField(db_column='eTimeOfDayAvailability', blank=True, null=True)
    bbountyhunter = models.IntegerField(db_column='bBountyHunter', blank=True, null=True)
    bcountarrestsastakeouts = models.IntegerField(db_column='bCountArrestsAsTakeouts', blank=True, null=True)
    bcountarrestsasviptakeouts = models.IntegerField(db_column='bCountArrestsAsVIPTakeouts', blank=True, null=True)
    bcountkillsastakeouts = models.IntegerField(db_column='bCountKillsAsTakeouts', blank=True, null=True)
    bcountkillsasviptakeouts = models.IntegerField(db_column='bCountKillsAsVIPTakeouts', blank=True, null=True)
    bdisabled = models.IntegerField(db_column='bDisabled', blank=True, null=True)
    bnocriminalopposition = models.IntegerField(db_column='bNoCriminalOpposition', blank=True, null=True)
    boppositionwinonmaxtakeouts = models.IntegerField(db_column='bOppositionWinOnMaxTakeouts', blank=True, null=True)
    bownerwinonmaxtakeouts = models.IntegerField(db_column='bOwnerWinOnMaxTakeouts', blank=True, null=True)
    btest = models.IntegerField(db_column='bTest', blank=True, null=True)
    busetakeoutbar = models.IntegerField(db_column='bUseTakeoutBar', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MissionTemplates'


class Missionuisockets(models.Model):
    id = models.IntegerField(primary_key=True)
    emissionuisocket = models.IntegerField(db_column='eMissionUISocket', blank=True, null=True)
    nrow = models.IntegerField(db_column='nRow', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MissionUISockets'


class Missionuitrackedstateprofile(models.Model):
    id = models.IntegerField(primary_key=True)
    sarmedicon = models.TextField(db_column='sArmedIcon', blank=True, null=True)
    sneutralicon = models.TextField(db_column='sNeutralIcon', blank=True, null=True)
    soppositionclaimed = models.TextField(db_column='sOppositionClaimed', blank=True, null=True)
    sownerclaimed = models.TextField(db_column='sOwnerClaimed', blank=True, null=True)
    sunarmedicon = models.TextField(db_column='sUnarmedIcon', blank=True, null=True)
    emissionuitrackedstateprofile = models.IntegerField(db_column='eMissionUITrackedStateProfile', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MissionUITrackedStateProfile'


class Modifiercategories(models.Model):
    id = models.IntegerField(primary_key=True)
    emodifiercategory = models.IntegerField(db_column='eModifierCategory', blank=True, null=True)
    nselectableslot = models.IntegerField(db_column='nSelectableSlot', blank=True, null=True)
    emodifierclass = models.IntegerField(db_column='eModifierClass', blank=True, null=True)
    emodifiertype = models.IntegerField(db_column='eModifierType', blank=True, null=True)
    estackingslot = models.IntegerField(db_column='eStackingSlot', blank=True, null=True)
    bavailableaspassenger = models.IntegerField(db_column='bAvailableAsPassenger', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ModifierCategories'


class Modifierdeployableeffects(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    emodifieritem = models.IntegerField(db_column='eModifierItem', blank=True, null=True)
    etaskitem = models.IntegerField(db_column='eTaskItem', blank=True, null=True)
    bdeployatmodifierend = models.IntegerField(db_column='bDeployAtModifierEnd', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ModifierDeployableEffects'


class Modifiereffects(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    emodifieritem = models.IntegerField(db_column='eModifierItem', blank=True, null=True)
    faddtoresult = models.FloatField(db_column='fAddToResult', blank=True, null=True)
    feffectmultiplier = models.FloatField(db_column='fEffectMultiplier', blank=True, null=True)
    eeffecttype = models.IntegerField(db_column='eEffectType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ModifierEffects'


class Modifieritemeffects(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    eitem = models.IntegerField(db_column='eItem', blank=True, null=True)
    emodifieritem = models.IntegerField(db_column='eModifierItem', blank=True, null=True)
    eeffect = models.IntegerField(db_column='eEffect', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ModifierItemEffects'


class Modifieritemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    emodifieritem = models.IntegerField(db_column='eModifierItem', blank=True, null=True)
    napplicationcost = models.IntegerField(db_column='nApplicationCost', blank=True, null=True)
    nremovalcost = models.IntegerField(db_column='nRemovalCost', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ModifierItemTypes'


class Modifieritems(models.Model):
    id = models.IntegerField(primary_key=True)
    striggersfx = models.TextField(db_column='sTriggerSFX', blank=True, null=True)
    striggervfx = models.TextField(db_column='sTriggerVFX', blank=True, null=True)
    emodifiercategory = models.IntegerField(db_column='eModifierCategory', blank=True, null=True)
    emodifieritem = models.IntegerField(db_column='eModifierItem', blank=True, null=True)
    erulesetexclusion = models.IntegerField(db_column='eRulesetExclusion', blank=True, null=True)
    fcooldowntimeatpremiumlevel_0 = models.FloatField(db_column='fCooldownTimeAtPremiumLevel_0', blank=True, null=True)
    fcooldowntimeatpremiumlevel_1 = models.FloatField(db_column='fCooldownTimeAtPremiumLevel_1', blank=True, null=True)
    fdurationatpremiumlevel_0 = models.FloatField(db_column='fDurationAtPremiumLevel_0', blank=True, null=True)
    fdurationatpremiumlevel_1 = models.FloatField(db_column='fDurationAtPremiumLevel_1', blank=True, null=True)
    fintervaltimeatpremiumlevel_0 = models.FloatField(db_column='fIntervalTimeAtPremiumLevel_0', blank=True, null=True)
    fintervaltimeatpremiumlevel_1 = models.FloatField(db_column='fIntervalTimeAtPremiumLevel_1', blank=True, null=True)
    nmodifierlevel = models.IntegerField(db_column='nModifierLevel', blank=True, null=True)
    egiftboxtheme = models.IntegerField(db_column='eGiftBoxTheme', blank=True, null=True)
    bactivationendsimmunity = models.IntegerField(db_column='bActivationEndsImmunity', blank=True, null=True)
    bbroadcastsfx = models.IntegerField(db_column='bBroadcastSFX', blank=True, null=True)
    buncancelable = models.IntegerField(db_column='bUnCancelable', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ModifierItems'


class Npcanimationcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    enpcanimationcategory = models.IntegerField(db_column='eNPCAnimationCategory', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NPCAnimationCategories'


class Npcaudiotype(models.Model):
    id = models.IntegerField(primary_key=True)
    sclothingaccessoriesswitchvalue = models.TextField(db_column='sClothingAccessoriesSwitchValue', blank=True, null=True)
    sclothingarmsswitchvalue = models.TextField(db_column='sClothingArmsSwitchValue', blank=True, null=True)
    sclothingfootwearswitchvalue = models.TextField(db_column='sClothingFootwearSwitchValue', blank=True, null=True)
    sclothinglegsswitchvalue = models.TextField(db_column='sClothingLegsSwitchValue', blank=True, null=True)
    svoiceswitchvalue = models.TextField(db_column='sVoiceSwitchValue', blank=True, null=True)
    enpcaudiotype = models.IntegerField(db_column='eNPCAudioType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NPCAudioType'


class Npcdrivertypes(models.Model):
    id = models.IntegerField(primary_key=True)
    enpcdrivertype = models.IntegerField(db_column='eNPCDriverType', blank=True, null=True)
    enpctypefemale = models.IntegerField(db_column='eNPCTypeFemale', blank=True, null=True)
    enpctypemale = models.IntegerField(db_column='eNPCTypeMale', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NPCDriverTypes'


class NpceventAllowedtooverrides(models.Model):
    id = models.IntegerField(primary_key=True)
    nignoreme = models.IntegerField(db_column='nIgnoreMe', blank=True, null=True)
    enpcevent = models.IntegerField(db_column='eNPCEvent', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NPCEvent_AllowedToOverrides'


class Npcevents(models.Model):
    id = models.IntegerField(primary_key=True)
    nignoreme = models.IntegerField(db_column='nIgnoreMe', blank=True, null=True)
    enpcevent = models.IntegerField(db_column='eNPCEvent', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NPCEvents'


class Npcpedestriananimations(models.Model):
    id = models.IntegerField(primary_key=True)
    snpcpedestriananimation = models.TextField(db_column='sNPCPedestrianAnimation', blank=True, null=True)
    eanimationcategory = models.IntegerField(db_column='eAnimationCategory', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NPCPedestrianAnimations'


class NpcreactionAllowedtooverrides(models.Model):
    id = models.IntegerField(primary_key=True)
    npriority = models.IntegerField(db_column='nPriority', blank=True, null=True)
    enpcreaction = models.IntegerField(db_column='eNPCReaction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NPCReaction_AllowedToOverrides'


class Npcreactions(models.Model):
    id = models.IntegerField(primary_key=True)
    npriority = models.IntegerField(db_column='nPriority', blank=True, null=True)
    enpcreaction = models.IntegerField(db_column='eNPCReaction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NPCReactions'


class NpctypeTodDistricts(models.Model):
    id = models.IntegerField(primary_key=True)
    edistrict = models.IntegerField(db_column='eDistrict', blank=True, null=True)
    enpctype_tod = models.IntegerField(db_column='eNPCType_TOD', blank=True, null=True)
    enpctype_tod_district = models.IntegerField(db_column='eNPCType_TOD_District', blank=True, null=True)
    fpopulationpercentage = models.FloatField(db_column='fPopulationPercentage', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NPCType_TOD_Districts'


class NpctypeTodInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    enpctype = models.IntegerField(db_column='eNPCType', blank=True, null=True)
    enpctype_tod = models.IntegerField(db_column='eNPCType_TOD', blank=True, null=True)
    etod = models.IntegerField(db_column='eTOD', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NPCType_TOD_Info'


class Npctypes(models.Model):
    id = models.IntegerField(primary_key=True)
    enpctype = models.IntegerField(db_column='eNPCType', blank=True, null=True)
    fdebugcolour_b = models.FloatField(db_column='fDebugColour_B', blank=True, null=True)
    fdebugcolour_g = models.FloatField(db_column='fDebugColour_G', blank=True, null=True)
    fdebugcolour_r = models.FloatField(db_column='fDebugColour_R', blank=True, null=True)
    egender = models.IntegerField(db_column='eGender', blank=True, null=True)
    enpccategory = models.IntegerField(db_column='eNPCCategory', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NPCTypes'


class Npcvehicleanimations(models.Model):
    id = models.IntegerField(primary_key=True)
    snpcvehicleanimation = models.TextField(db_column='sNPCVehicleAnimation', blank=True, null=True)
    eanimationcategory = models.IntegerField(db_column='eAnimationCategory', blank=True, null=True)
    evehiclenpcinsideanimationset = models.IntegerField(db_column='eVehicleNPCInsideAnimationSet', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NPCVehicleAnimations'


class Npcvehiclespeeds(models.Model):
    id = models.IntegerField(primary_key=True)
    enpcvehiclecategory = models.IntegerField(db_column='eNPCVehicleCategory', blank=True, null=True)
    fmaxacceleration = models.FloatField(db_column='fMaxAcceleration', blank=True, null=True)
    fmaxdeceleration = models.FloatField(db_column='fMaxDeceleration', blank=True, null=True)
    fmaxtopspeedratio = models.FloatField(db_column='fMaxTopSpeedRatio', blank=True, null=True)
    fminacceleration = models.FloatField(db_column='fMinAcceleration', blank=True, null=True)
    fmindeceleration = models.FloatField(db_column='fMinDeceleration', blank=True, null=True)
    fmintopspeedratio = models.FloatField(db_column='fMinTopSpeedRatio', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NPCVehicleSpeeds'


class Npcworldevents(models.Model):
    id = models.IntegerField(primary_key=True)
    spedestrianaudioreason = models.TextField(db_column='sPedestrianAudioReason', blank=True, null=True)
    epedestrianblastevent = models.IntegerField(db_column='ePedestrianBlastEvent', blank=True, null=True)
    epedestriandangerevent = models.IntegerField(db_column='ePedestrianDangerEvent', blank=True, null=True)
    epedestrianwitnessevent = models.IntegerField(db_column='ePedestrianWitnessEvent', blank=True, null=True)
    evehicleblastevent = models.IntegerField(db_column='eVehicleBlastEvent', blank=True, null=True)
    evehicledangerevent = models.IntegerField(db_column='eVehicleDangerEvent', blank=True, null=True)
    evehiclewitnessevent = models.IntegerField(db_column='eVehicleWitnessEvent', blank=True, null=True)
    faudibilitydistance = models.FloatField(db_column='fAudibilityDistance', blank=True, null=True)
    fblastdistance = models.FloatField(db_column='fBlastDistance', blank=True, null=True)
    fdangerdistance = models.FloatField(db_column='fDangerDistance', blank=True, null=True)
    fvisibilitydistance = models.FloatField(db_column='fVisibilityDistance', blank=True, null=True)
    enpcworldevent = models.IntegerField(db_column='eNPCWorldEvent', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NPCWorldEvents'


class NpcTodBehaviours(models.Model):
    id = models.IntegerField(primary_key=True)
    enpc_tod_event = models.IntegerField(db_column='eNPC_TOD_Event', blank=True, null=True)
    ereaction = models.IntegerField(db_column='eReaction', blank=True, null=True)
    flikelihood = models.FloatField(db_column='fLikelihood', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NPC_TOD_Behaviours'


class NpcTodEvent(models.Model):
    id = models.IntegerField(primary_key=True)
    enpc_tod_event = models.IntegerField(db_column='eNPC_TOD_Event', blank=True, null=True)
    enpctype = models.IntegerField(db_column='eNPCType', blank=True, null=True)
    etod_event = models.IntegerField(db_column='eTOD_Event', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NPC_TOD_Event'


class Notorietyeffects(models.Model):
    id = models.IntegerField(primary_key=True)
    eforcemaxlevel = models.IntegerField(db_column='eForceMaxLevel', blank=True, null=True)
    eforceminlevel = models.IntegerField(db_column='eForceMinLevel', blank=True, null=True)
    enotorietyeffect = models.IntegerField(db_column='eNotorietyEffect', blank=True, null=True)
    enotorietylevellimit = models.IntegerField(db_column='eNotorietyLevelLimit', blank=True, null=True)
    fquantity = models.FloatField(db_column='fQuantity', blank=True, null=True)
    nenforcerwitnesserscap = models.IntegerField(db_column='nEnforcerWitnessersCap', blank=True, null=True)
    nnpcwitnesserscap = models.IntegerField(db_column='nNPCWitnessersCap', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NotorietyEffects'


class Notorietylevels(models.Model):
    id = models.IntegerField(primary_key=True)
    eheatlevel = models.IntegerField(db_column='eHeatLevel', blank=True, null=True)
    enotorietylevel = models.IntegerField(db_column='eNotorietyLevel', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NotorietyLevels'


class Owaitemspawnrules(models.Model):
    id = models.IntegerField(primary_key=True)
    eitemmetatag_0 = models.IntegerField(db_column='eItemMetaTag_0', blank=True, null=True)
    eitemmetatag_1 = models.IntegerField(db_column='eItemMetaTag_1', blank=True, null=True)
    eitemmetatag_2 = models.IntegerField(db_column='eItemMetaTag_2', blank=True, null=True)
    eitemmetatag_3 = models.IntegerField(db_column='eItemMetaTag_3', blank=True, null=True)
    eitemmetatag_4 = models.IntegerField(db_column='eItemMetaTag_4', blank=True, null=True)
    eowaitemspawnrule = models.IntegerField(db_column='eOWAItemSpawnRule', blank=True, null=True)
    nlargeitemweighting = models.IntegerField(db_column='nLargeItemWeighting', blank=True, null=True)
    nlowermidrange = models.IntegerField(db_column='nLowerMidRange', blank=True, null=True)
    nlowerrange = models.IntegerField(db_column='nLowerRange', blank=True, null=True)
    nmediumitemweighting = models.IntegerField(db_column='nMediumItemWeighting', blank=True, null=True)
    npercentagechancezeroitems = models.IntegerField(db_column='nPercentageChanceZeroItems', blank=True, null=True)
    nsmallitemweighting = models.IntegerField(db_column='nSmallItemWeighting', blank=True, null=True)
    nuppermidrange = models.IntegerField(db_column='nUpperMidRange', blank=True, null=True)
    nupperrange = models.IntegerField(db_column='nUpperRange', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OWAItemSpawnRules'


class Onfootdeathanimations(models.Model):
    id = models.IntegerField(primary_key=True)
    sanimname = models.TextField(db_column='sAnimName', blank=True, null=True)
    eonfootdeathanimation = models.IntegerField(db_column='eOnFootDeathAnimation', blank=True, null=True)
    bretainmomentum = models.IntegerField(db_column='bRetainMomentum', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OnFootDeathAnimations'


class Openworldconstant(models.Model):
    id = models.IntegerField(primary_key=True)
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)
    eopenworldconstant = models.IntegerField(db_column='eOpenWorldConstant', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OpenWorldConstant'


class Openworlddropoffs(models.Model):
    id = models.IntegerField(primary_key=True)
    ehudmarkertype = models.IntegerField(db_column='eHUDMarkerType', blank=True, null=True)
    eopenworlddropoff = models.IntegerField(db_column='eOpenWorldDropOff', blank=True, null=True)
    fcycledurationseconds = models.FloatField(db_column='fCycleDurationSeconds', blank=True, null=True)
    fpointreplenishmentpercycle = models.FloatField(db_column='fPointReplenishmentPerCycle', blank=True, null=True)
    ndeliverypoints = models.IntegerField(db_column='nDeliveryPoints', blank=True, null=True)
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)
    efactionhudmarkerfilter = models.IntegerField(db_column='eFactionHUDMarkerFilter', blank=True, null=True)
    etaskitemsize_0 = models.IntegerField(db_column='eTaskItemSize_0', blank=True, null=True)
    etaskitemsize_1 = models.IntegerField(db_column='eTaskItemSize_1', blank=True, null=True)
    etaskitemsize_2 = models.IntegerField(db_column='eTaskItemSize_2', blank=True, null=True)
    etaskitemsize_3 = models.IntegerField(db_column='eTaskItemSize_3', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OpenWorldDropOffs'


class Openworldoperations(models.Model):
    id = models.IntegerField(primary_key=True)
    suidescription = models.TextField(db_column='sUIDescription', blank=True, null=True)
    suititle = models.TextField(db_column='sUITitle', blank=True, null=True)
    eopenworldoperation = models.IntegerField(db_column='eOpenWorldOperation', blank=True, null=True)
    euiicon = models.IntegerField(db_column='eUIIcon', blank=True, null=True)
    ncsaduration = models.IntegerField(db_column='nCSADuration', blank=True, null=True)
    enpcworldevent = models.IntegerField(db_column='eNPCWorldEvent', blank=True, null=True)
    eopenworldcsa = models.IntegerField(db_column='eOpenWorldCSA', blank=True, null=True)
    etaskoperationcategory = models.IntegerField(db_column='eTaskOperationCategory', blank=True, null=True)
    ballowedonmission = models.IntegerField(db_column='bAllowedOnMission', blank=True, null=True)
    buireticulehighlight = models.IntegerField(db_column='bUIReticuleHighlight', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OpenWorldOperations'


class Openworldtargetactivities(models.Model):
    id = models.IntegerField(primary_key=True)
    eopenworldoperationcriminal = models.IntegerField(db_column='eOpenWorldOperationCriminal', blank=True, null=True)
    eopenworldoperationenforcer = models.IntegerField(db_column='eOpenWorldOperationEnforcer', blank=True, null=True)
    eopenworldtargetactivity = models.IntegerField(db_column='eOpenWorldTargetActivity', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OpenWorldTargetActivities'


class Optioncategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sname = models.TextField(db_column='sName', blank=True, null=True)
    eaccessrestrictions = models.IntegerField(db_column='eAccessRestrictions', blank=True, null=True)
    eoptioncategory = models.IntegerField(db_column='eOptionCategory', blank=True, null=True)
    eparent = models.IntegerField(db_column='eParent', blank=True, null=True)
    binclude = models.IntegerField(db_column='bInclude', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OptionCategories'


class Organisations(models.Model):
    id = models.IntegerField(primary_key=True)
    sname = models.TextField(db_column='sName', blank=True, null=True)
    spicture = models.TextField(db_column='sPicture', blank=True, null=True)
    ehudicon = models.IntegerField(db_column='eHUDIcon', blank=True, null=True)
    eorganisationcontact = models.IntegerField(db_column='eOrganisationContact', blank=True, null=True)
    eorganisationicon = models.IntegerField(db_column='eOrganisationIcon', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)
    eorganisation = models.IntegerField(db_column='eOrganisation', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Organisations'


class Outfititemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sresource = models.TextField(db_column='sResource', blank=True, null=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OutfitItemTypes'


class PawnhitreactionBonelists(models.Model):
    id = models.IntegerField(primary_key=True)
    svalue_0 = models.TextField(db_column='sValue_0', blank=True, null=True)
    svalue_1 = models.TextField(db_column='sValue_1', blank=True, null=True)
    svalue_2 = models.TextField(db_column='sValue_2', blank=True, null=True)
    svalue_3 = models.TextField(db_column='sValue_3', blank=True, null=True)
    svalue_4 = models.TextField(db_column='sValue_4', blank=True, null=True)
    svalue_5 = models.TextField(db_column='sValue_5', blank=True, null=True)
    svalue_6 = models.TextField(db_column='sValue_6', blank=True, null=True)
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_BoneLists'


class PawnhitreactionBoneremaptables(models.Model):
    id = models.IntegerField(primary_key=True)
    sbonefrom = models.TextField(db_column='sBoneFrom', blank=True, null=True)
    sboneto = models.TextField(db_column='sBoneTo', blank=True, null=True)
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_BoneRemapTables'


class PawnhitreactionBools(models.Model):
    id = models.IntegerField(primary_key=True)
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction', blank=True, null=True)
    bvalue = models.IntegerField(db_column='bValue', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_Bools'


class PawnhitreactionConstrainedbonelists(models.Model):
    id = models.IntegerField(primary_key=True)
    svalue_0 = models.TextField(db_column='sValue_0', blank=True, null=True)
    svalue_1 = models.TextField(db_column='sValue_1', blank=True, null=True)
    svalue_2 = models.TextField(db_column='sValue_2', blank=True, null=True)
    svalue_3 = models.TextField(db_column='sValue_3', blank=True, null=True)
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_ConstrainedBoneLists'


class PawnhitreactionFloats(models.Model):
    id = models.IntegerField(primary_key=True)
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction', blank=True, null=True)
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_Floats'


class PawnhitreactionSpringlists(models.Model):
    id = models.IntegerField(primary_key=True)
    svalue_0 = models.TextField(db_column='sValue_0', blank=True, null=True)
    svalue_1 = models.TextField(db_column='sValue_1', blank=True, null=True)
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_SpringLists'


class PawnhitreactionVector2Ds(models.Model):
    id = models.IntegerField(primary_key=True)
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction', blank=True, null=True)
    fx = models.FloatField(db_column='fX', blank=True, null=True)
    fy = models.FloatField(db_column='fY', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_Vector2Ds'


class Pawnhitreactions(models.Model):
    id = models.IntegerField(primary_key=True)
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction', blank=True, null=True)
    etype = models.IntegerField(db_column='eType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PawnHitReactions'


class Pedavoidanimation(models.Model):
    id = models.IntegerField(primary_key=True)
    savoidanimationleft = models.TextField(db_column='sAvoidAnimationLeft', blank=True, null=True)
    savoidanimationright = models.TextField(db_column='sAvoidAnimationRight', blank=True, null=True)
    eavoidanimationcategory = models.IntegerField(db_column='eAvoidAnimationCategory', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PedAvoidAnimation'


class Pedavoidanimationcategory(models.Model):
    id = models.IntegerField(primary_key=True)
    epedavoidanimationcategory = models.IntegerField(db_column='ePedAvoidAnimationCategory', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PedAvoidAnimationCategory'


class Pedwalkandrunvariations(models.Model):
    id = models.IntegerField(primary_key=True)
    sanimation = models.TextField(db_column='sAnimation', blank=True, null=True)
    epedavoidanimationcategory = models.IntegerField(db_column='ePedAvoidAnimationCategory', blank=True, null=True)
    epedwalkandrunvariation = models.IntegerField(db_column='ePedWalkAndRunVariation', blank=True, null=True)
    fbasespeed = models.FloatField(db_column='fBaseSpeed', blank=True, null=True)
    egender = models.IntegerField(db_column='eGender', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PedWalkAndRunVariations'


class Pedestrianassets(models.Model):
    id = models.IntegerField(primary_key=True)
    sasset = models.TextField(db_column='sAsset', blank=True, null=True)
    eaudiotype = models.IntegerField(db_column='eAudioType', blank=True, null=True)
    enpctype = models.IntegerField(db_column='eNPCType', blank=True, null=True)
    epedestrianasset = models.IntegerField(db_column='ePedestrianAsset', blank=True, null=True)
    eracetype = models.IntegerField(db_column='eRaceType', blank=True, null=True)
    ewalkstyle = models.IntegerField(db_column='eWalkStyle', blank=True, null=True)
    epedestrianpalettetype = models.IntegerField(db_column='ePedestrianPaletteType', blank=True, null=True)
    bhighheels = models.IntegerField(db_column='bHighHeels', blank=True, null=True)
    bshoelaces = models.IntegerField(db_column='bShoeLaces', blank=True, null=True)
    bwristwatch = models.IntegerField(db_column='bWristWatch', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PedestrianAssets'


class Pedestrianevents(models.Model):
    id = models.IntegerField(primary_key=True)
    nignoreme = models.IntegerField(db_column='nIgnoreMe', blank=True, null=True)
    enpcevent = models.IntegerField(db_column='eNPCEvent', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PedestrianEvents'


class Pedestrianpalettecolours(models.Model):
    id = models.IntegerField(primary_key=True)
    fblue = models.FloatField(db_column='fBlue', blank=True, null=True)
    fgreen = models.FloatField(db_column='fGreen', blank=True, null=True)
    fred = models.FloatField(db_column='fRed', blank=True, null=True)
    ncolourindex = models.IntegerField(db_column='nColourIndex', blank=True, null=True)
    epedestrianpalettetype = models.IntegerField(db_column='ePedestrianPaletteType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PedestrianPaletteColours'


class Pedestrianttianimationoverrides(models.Model):
    id = models.IntegerField(primary_key=True)
    snpcanimation = models.TextField(db_column='sNPCAnimation', blank=True, null=True)
    enpctype = models.IntegerField(db_column='eNPCType', blank=True, null=True)
    epedestrianttireaction = models.IntegerField(db_column='ePedestrianTTIReaction', blank=True, null=True)
    eplayeranimtype = models.IntegerField(db_column='ePlayerAnimType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PedestrianTTIAnimationOverrides'


class Pedestrianttianimations(models.Model):
    id = models.IntegerField(primary_key=True)
    snpcanimation = models.TextField(db_column='sNPCAnimation', blank=True, null=True)
    epedestrianttireaction = models.IntegerField(db_column='ePedestrianTTIReaction', blank=True, null=True)
    eplayeranimtype = models.IntegerField(db_column='ePlayerAnimType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PedestrianTTIAnimations'


class Pedestrianttireactionoverrides(models.Model):
    id = models.IntegerField(primary_key=True)
    scancelaudioevent = models.TextField(db_column='sCancelAudioEvent', blank=True, null=True)
    scompleteaudioevent = models.TextField(db_column='sCompleteAudioEvent', blank=True, null=True)
    sstartaudioevent = models.TextField(db_column='sStartAudioEvent', blank=True, null=True)
    enpctype = models.IntegerField(db_column='eNPCType', blank=True, null=True)
    epedestrianttireaction = models.IntegerField(db_column='ePedestrianTTIReaction', blank=True, null=True)
    ewhencancelled = models.IntegerField(db_column='eWhenCancelled', blank=True, null=True)
    ewhencompleted = models.IntegerField(db_column='eWhenCompleted', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PedestrianTTIReactionOverrides'


class Pedestrianttireactions(models.Model):
    id = models.IntegerField(primary_key=True)
    scancelaudioevent = models.TextField(db_column='sCancelAudioEvent', blank=True, null=True)
    scompleteaudioevent = models.TextField(db_column='sCompleteAudioEvent', blank=True, null=True)
    sstartaudioevent = models.TextField(db_column='sStartAudioEvent', blank=True, null=True)
    epedestrianttireaction = models.IntegerField(db_column='ePedestrianTTIReaction', blank=True, null=True)
    ewhencancelled = models.IntegerField(db_column='eWhenCancelled', blank=True, null=True)
    ewhencompleted = models.IntegerField(db_column='eWhenCompleted', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PedestrianTTIReactions'


class Pedestriantempsetups(models.Model):
    id = models.IntegerField(primary_key=True)
    stempsetupinfo = models.TextField(db_column='sTempSetupInfo', blank=True, null=True)
    epedestriantempsetup = models.IntegerField(db_column='ePedestrianTempSetup', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PedestrianTempSetups'


class Pedestriantyperestrictions(models.Model):
    id = models.IntegerField(primary_key=True)
    enpctype = models.IntegerField(db_column='eNPCType', blank=True, null=True)
    nnumconcurrentsetuptypes = models.IntegerField(db_column='nNumConcurrentSetupTypes', blank=True, null=True)
    npedestriantyperestriction = models.IntegerField(db_column='nPedestrianTypeRestriction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PedestrianTypeRestrictions'


class Playerroles(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    eactivities_0 = models.IntegerField(db_column='eActivities_0', blank=True, null=True)
    eactivities_1 = models.IntegerField(db_column='eActivities_1', blank=True, null=True)
    eactivities_2 = models.IntegerField(db_column='eActivities_2', blank=True, null=True)
    efirstmilestone = models.IntegerField(db_column='eFirstMilestone', blank=True, null=True)
    eplayerrole = models.IntegerField(db_column='ePlayerRole', blank=True, null=True)
    fdisplayformulavalue = models.FloatField(db_column='fDisplayFormulaValue', blank=True, null=True)
    nnummilestones = models.IntegerField(db_column='nNumMilestones', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    edisplayformulaoperation = models.IntegerField(db_column='eDisplayFormulaOperation', blank=True, null=True)
    efaction = models.ForeignKey('Factions', db_column=u'eFaction')
    bachievement = models.IntegerField(db_column='bAchievement', blank=True, null=True)
    bachievementhidden = models.IntegerField(db_column='bAchievementHidden', blank=True, null=True)
    bshowtotalvalues = models.IntegerField(db_column='bShowTotalValues', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    @property_cache
    def name(self):
        return self.sdisplayname

    @property_cache
    def description(self):
        return self.sdescription

    @property_cache
    def levels(self):
        milestones = Rolemilestones.objects.filter(pk__gte=self.efirstmilestone, pk__lt=self.efirstmilestone + self.nnummilestones)
        return milestones

    class Meta:
        managed = False
        db_table = 'PlayerRoles'


class Populationtotals(models.Model):
    id = models.IntegerField(primary_key=True)
    edistricttype = models.IntegerField(db_column='eDistrictType', blank=True, null=True)
    npopulationtotal = models.IntegerField(db_column='nPopulationTotal', blank=True, null=True)
    ntotalpedestrians = models.IntegerField(db_column='nTotalPedestrians', blank=True, null=True)
    ntotalvehicles = models.IntegerField(db_column='nTotalVehicles', blank=True, null=True)
    etod = models.IntegerField(db_column='eTOD', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PopulationTotals'


class Popupdialogcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    ehighlightcolour = models.IntegerField(db_column='eHighlightColour', blank=True, null=True)
    epopupdialogcategory = models.IntegerField(db_column='ePopupDialogCategory', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PopupDialogCategories'


class Popupdialogtriggersceneopen(models.Model):
    id = models.IntegerField(primary_key=True)
    seventname = models.TextField(db_column='sEventName', blank=True, null=True)
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PopupDialogTriggerSceneOpen'


class PopupdialogtriggerCsaBegin(models.Model):
    id = models.IntegerField(primary_key=True)
    seventname = models.TextField(db_column='sEventName', blank=True, null=True)
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_CSA_Begin'


class PopupdialogtriggerCsaEnd(models.Model):
    id = models.IntegerField(primary_key=True)
    seventname = models.TextField(db_column='sEventName', blank=True, null=True)
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_CSA_End'


class PopupdialogtriggerGameplayevents(models.Model):
    id = models.IntegerField(primary_key=True)
    seventname = models.TextField(db_column='sEventName', blank=True, null=True)
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_GamePlayEvents'


class PopupdialogtriggerGeneric(models.Model):
    id = models.IntegerField(primary_key=True)
    seventname = models.TextField(db_column='sEventName', blank=True, null=True)
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_Generic'


class PopupdialogtriggerReticuleover(models.Model):
    id = models.IntegerField(primary_key=True)
    seventname = models.TextField(db_column='sEventName', blank=True, null=True)
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_ReticuleOver'


class PopupdialogtriggerSceneclose(models.Model):
    id = models.IntegerField(primary_key=True)
    seventname = models.TextField(db_column='sEventName', blank=True, null=True)
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_SceneClose'


class PopupdialogtriggerUieventPostonclick(models.Model):
    id = models.IntegerField(primary_key=True)
    seventname = models.TextField(db_column='sEventName', blank=True, null=True)
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_UIEvent_PostOnClick'


class PopupdialogtriggerWorldspacezone(models.Model):
    id = models.IntegerField(primary_key=True)
    seventname = models.TextField(db_column='sEventName', blank=True, null=True)
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_WorldSpaceZone'


class Popupdialogtriggers(models.Model):
    id = models.IntegerField(primary_key=True)
    edialogshown = models.IntegerField(db_column='eDialogShown', blank=True, null=True)
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PopupDialogTriggers'


class Popupdialoguihighlightaggregation(models.Model):
    id = models.IntegerField(primary_key=True)
    swidget1 = models.TextField(db_column='sWidget1', blank=True, null=True)
    swidget2 = models.TextField(db_column='sWidget2', blank=True, null=True)
    swidget3 = models.TextField(db_column='sWidget3', blank=True, null=True)
    swidget4 = models.TextField(db_column='sWidget4', blank=True, null=True)
    swidget5 = models.TextField(db_column='sWidget5', blank=True, null=True)
    epopupdialoguihighlightaggregation = models.IntegerField(db_column='ePopupDialogUIHighlightAggregation', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PopupDialogUIHighlightAggregation'


class Popupdialogs(models.Model):
    id = models.IntegerField(primary_key=True)
    spopupbody = models.TextField(db_column='sPopupBody', blank=True, null=True)
    echainedpopup = models.IntegerField(db_column='eChainedPopup', blank=True, null=True)
    eknowledgebaseurl = models.IntegerField(db_column='eKnowledgeBaseURL', blank=True, null=True)
    eoptionalwaypoint = models.IntegerField(db_column='eOptionalWaypoint', blank=True, null=True)
    epopupdialog = models.IntegerField(db_column='ePopupDialog', blank=True, null=True)
    eposition = models.IntegerField(db_column='ePosition', blank=True, null=True)
    euiwidgethightlight_aggregation = models.IntegerField(db_column='eUIWidgetHightlight_Aggregation', blank=True, null=True)
    fdisplaytime = models.FloatField(db_column='fDisplayTime', blank=True, null=True)
    ntimestoshow = models.IntegerField(db_column='nTimesToShow', blank=True, null=True)
    epopupcategory = models.IntegerField(db_column='ePopupCategory', blank=True, null=True)
    bdonotqueue = models.IntegerField(db_column='bDoNotQueue', blank=True, null=True)
    bflushqueue = models.IntegerField(db_column='bFlushQueue', blank=True, null=True)
    bforceknowledgebase = models.IntegerField(db_column='bForceKnowledgebase', blank=True, null=True)
    bforchat = models.IntegerField(db_column='bForChat', blank=True, null=True)
    bsuppresscriminal = models.IntegerField(db_column='bSuppressCriminal', blank=True, null=True)
    bsuppressenforcer = models.IntegerField(db_column='bSuppressEnforcer', blank=True, null=True)
    bsuppressmain = models.IntegerField(db_column='bSuppressMain', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PopupDialogs'


class Preloadaction(models.Model):
    id = models.IntegerField(primary_key=True)
    spreloadaction = models.TextField(db_column='sPreloadAction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PreloadAction'


class Preloadcommon(models.Model):
    id = models.IntegerField(primary_key=True)
    spreloadcommon = models.TextField(db_column='sPreloadCommon', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PreloadCommon'


class Preloadcustomisations(models.Model):
    id = models.IntegerField(primary_key=True)
    spackage = models.TextField(db_column='sPackage', blank=True, null=True)
    spreloadcustomisation = models.TextField(db_column='sPreloadCustomisation', blank=True, null=True)
    bcoversbreasts = models.IntegerField(db_column='bCoversBreasts', blank=True, null=True)
    bcoversgenitalia = models.IntegerField(db_column='bCoversGenitalia', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PreloadCustomisations'


class Preloadsocial(models.Model):
    id = models.IntegerField(primary_key=True)
    spreloadsocial = models.TextField(db_column='sPreloadSocial', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PreloadSocial'


class Prestigeeffects(models.Model):
    id = models.IntegerField(primary_key=True)
    eforcemaxlevel = models.IntegerField(db_column='eForceMaxLevel', blank=True, null=True)
    eforceminlevel = models.IntegerField(db_column='eForceMinLevel', blank=True, null=True)
    eprestigeeffect = models.IntegerField(db_column='ePrestigeEffect', blank=True, null=True)
    eprestigelevellimit = models.IntegerField(db_column='ePrestigeLevelLimit', blank=True, null=True)
    fquantity = models.FloatField(db_column='fQuantity', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PrestigeEffects'


class Prestigelevels(models.Model):
    id = models.IntegerField(primary_key=True)
    eheatlevel = models.IntegerField(db_column='eHeatLevel', blank=True, null=True)
    eprestigelevel = models.IntegerField(db_column='ePrestigeLevel', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PrestigeLevels'


class Primitiveentries(models.Model):
    id = models.IntegerField(primary_key=True)
    epage = models.IntegerField(db_column='ePage', blank=True, null=True)
    eprimitiveentry = models.IntegerField(db_column='ePrimitiveEntry', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PrimitiveEntries'


class Primitivepages(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    eprimitivepage = models.IntegerField(db_column='ePrimitivePage', blank=True, null=True)
    etype = models.IntegerField(db_column='eType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PrimitivePages'


class Primitiveunlockitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sresource = models.TextField(db_column='sResource', blank=True, null=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    nlegacydata = models.IntegerField(db_column='nLegacyData', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    etype = models.IntegerField(db_column='eType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PrimitiveUnlockItemTypes'


class Probabilities(models.Model):
    id = models.IntegerField(primary_key=True)
    eprobability = models.IntegerField(db_column='eProbability', blank=True, null=True)
    fcoefficient = models.FloatField(db_column='fCoefficient', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Probabilities'


class Profanityfilterentries(models.Model):
    id = models.IntegerField(primary_key=True)
    sprofanityfilterentry = models.TextField(db_column='sProfanityFilterEntry', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProfanityFilterEntries'


class Progressionfixups(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    nlatestversion = models.IntegerField(db_column='nLatestVersion', blank=True, null=True)
    eprogressionfixup = models.IntegerField(db_column='eProgressionFixup', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProgressionFixups'


class Provinggroundschallengemissionactivity(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    eexclude = models.IntegerField(db_column='eExclude', blank=True, null=True)
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)
    eprovinggroundschallengemissionactivity = models.IntegerField(db_column='eProvingGroundsChallengeMissionActivity', blank=True, null=True)
    erarity = models.IntegerField(db_column='eRarity', blank=True, null=True)
    nrequirement_0 = models.IntegerField(db_column='nRequirement_0', blank=True, null=True)
    nrequirement_1 = models.IntegerField(db_column='nRequirement_1', blank=True, null=True)
    nrequirement_2 = models.IntegerField(db_column='nRequirement_2', blank=True, null=True)
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProvingGroundsChallengeMissionActivity'


class Provinggroundschallengemissiontype(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    emissiontypefilter = models.IntegerField(db_column='eMissionTypeFilter', blank=True, null=True)
    eprovinggroundschallengemissiontype = models.IntegerField(db_column='eProvingGroundsChallengeMissionType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProvingGroundsChallengeMissionType'


class Provinggroundschallengestats(models.Model):
    id = models.IntegerField(primary_key=True)
    sdatabasecolumn = models.TextField(db_column='sDatabaseColumn', blank=True, null=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    sdisplaynamepercentage = models.TextField(db_column='sDisplayNamePercentage', blank=True, null=True)
    sdisplayscoreboard = models.TextField(db_column='sDisplayScoreboard', blank=True, null=True)
    shudprogress = models.TextField(db_column='sHUDProgress', blank=True, null=True)
    stitle = models.TextField(db_column='sTitle', blank=True, null=True)
    eprovinggroundschallengestat = models.IntegerField(db_column='eProvingGroundsChallengeStat', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProvingGroundsChallengeStats'


class Raceinfos(models.Model):
    id = models.IntegerField(primary_key=True)
    eraceinfo = models.IntegerField(db_column='eRaceInfo', blank=True, null=True)
    eracetype = models.IntegerField(db_column='eRaceType', blank=True, null=True)
    fb = models.FloatField(db_column='fB', blank=True, null=True)
    fg = models.FloatField(db_column='fG', blank=True, null=True)
    fr = models.FloatField(db_column='fR', blank=True, null=True)
    ncolourindex = models.IntegerField(db_column='nColourIndex', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RaceInfos'


class Racetyes(models.Model):
    id = models.IntegerField(primary_key=True)
    sname = models.TextField(db_column='sName', blank=True, null=True)
    eracetype = models.IntegerField(db_column='eRaceType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RaceTyes'


class Randomrewards(models.Model):
    id = models.IntegerField(primary_key=True)
    efirstweightedreward = models.IntegerField(db_column='eFirstWeightedReward', blank=True, null=True)
    epurpose = models.IntegerField(db_column='ePurpose', blank=True, null=True)
    erandomreward = models.IntegerField(db_column='eRandomReward', blank=True, null=True)
    especificcontact = models.IntegerField(db_column='eSpecificContact', blank=True, null=True)
    fchancepercentage_0 = models.FloatField(db_column='fChancePercentage_0', blank=True, null=True)
    fchancepercentage_1 = models.FloatField(db_column='fChancePercentage_1', blank=True, null=True)
    nnumweightedrewards = models.IntegerField(db_column='nNumWeightedRewards', blank=True, null=True)
    especificorganisation = models.IntegerField(db_column='eSpecificOrganisation', blank=True, null=True)
    bspecificuseonly = models.IntegerField(db_column='bSpecificUseOnly', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RandomRewards'


class Randomtimelimitedrewards(models.Model):
    id = models.IntegerField(primary_key=True)
    edisabledrulesets = models.IntegerField(db_column='eDisabledRulesets', blank=True, null=True)
    emissionsystemfilter = models.IntegerField(db_column='eMissionSystemFilter', blank=True, null=True)
    erandomreward = models.IntegerField(db_column='eRandomReward', blank=True, null=True)
    fdefaultmaxskillratingdifference = models.FloatField(db_column='fDefaultMaxSkillRatingDifference', blank=True, null=True)
    ffailedmaximumtime = models.FloatField(db_column='fFailedMaximumTime', blank=True, null=True)
    ffailedminimumtime = models.FloatField(db_column='fFailedMinimumTime', blank=True, null=True)
    fminskillratingweight = models.FloatField(db_column='fMinSkillRatingWeight', blank=True, null=True)
    fstandardmaximumtime = models.FloatField(db_column='fStandardMaximumTime', blank=True, null=True)
    fstandardminimumtime = models.FloatField(db_column='fStandardMinimumTime', blank=True, null=True)
    nmindistrictpop = models.IntegerField(db_column='nMinDistrictPop', blank=True, null=True)
    bawardonloss = models.IntegerField(db_column='bAwardOnLoss', blank=True, null=True)
    bawardonwin = models.IntegerField(db_column='bAwardOnWin', blank=True, null=True)
    bonworldlevel = models.IntegerField(db_column='bOnWorldLevel', blank=True, null=True)
    bresetatentry = models.IntegerField(db_column='bResetAtEntry', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RandomTimeLimitedRewards'


class Rangedweapontype(models.Model):
    id = models.IntegerField(primary_key=True)
    eexplosiontype = models.IntegerField(db_column='eExplosionType', blank=True, null=True)
    erecoil = models.IntegerField(db_column='eRecoil', blank=True, null=True)
    eweapontype = models.IntegerField(db_column='eWeaponType', blank=True, null=True)
    faccuracycooldown = models.FloatField(db_column='fAccuracyCooldown', blank=True, null=True)
    faccuracypower = models.FloatField(db_column='fAccuracyPower', blank=True, null=True)
    fcrouchmodifier = models.FloatField(db_column='fCrouchModifier', blank=True, null=True)
    finvehiclemodifier = models.FloatField(db_column='fInVehicleModifier', blank=True, null=True)
    fjumpmodifier = models.FloatField(db_column='fJumpModifier', blank=True, null=True)
    fleanmodifier = models.FloatField(db_column='fLeanModifier', blank=True, null=True)
    fmarksmanshipfov16_9 = models.FloatField(db_column='fMarksmanshipFOV16_9', blank=True, null=True)
    fmarksmanshipfov4_3 = models.FloatField(db_column='fMarksmanshipFOV4_3', blank=True, null=True)
    fmarksmanshipmodifier = models.FloatField(db_column='fMarksmanshipModifier', blank=True, null=True)
    fmaxrange = models.FloatField(db_column='fMaxRange', blank=True, null=True)
    fmaxtimebetweenshots = models.FloatField(db_column='fMaxTimeBetweenShots', blank=True, null=True)
    fmindamagerange = models.FloatField(db_column='fMinDamageRange', blank=True, null=True)
    fminimumcrosshairwidth = models.FloatField(db_column='fMinimumCrosshairWidth', blank=True, null=True)
    fminimumdamagepercentage = models.FloatField(db_column='fMinimumDamagePercentage', blank=True, null=True)
    foverallshotmodifiercap = models.FloatField(db_column='fOverallShotModifierCap', blank=True, null=True)
    fpershotmodifier = models.FloatField(db_column='fPerShotModifier', blank=True, null=True)
    fpiercedamagereduction = models.FloatField(db_column='fPierceDamageReduction', blank=True, null=True)
    fpiercedamagescale = models.FloatField(db_column='fPierceDamageScale', blank=True, null=True)
    fradiusattenmetres = models.FloatField(db_column='fRadiusAtTenMetres', blank=True, null=True)
    frampdistance = models.FloatField(db_column='fRampDistance', blank=True, null=True)
    frayspreadattenmetres = models.FloatField(db_column='fRaySpreadAtTenMetres', blank=True, null=True)
    frecoverydelay = models.FloatField(db_column='fRecoveryDelay', blank=True, null=True)
    frecoverypersecond = models.FloatField(db_column='fRecoveryPerSecond', blank=True, null=True)
    frunmodifier = models.FloatField(db_column='fRunModifier', blank=True, null=True)
    fsprintmodifier = models.FloatField(db_column='fSprintModifier', blank=True, null=True)
    fwalkmodifier = models.FloatField(db_column='fWalkModifier', blank=True, null=True)
    fweaponswitchminaccuracy = models.FloatField(db_column='fWeaponSwitchMinAccuracy', blank=True, null=True)
    nfreeammo = models.IntegerField(db_column='nFreeAmmo', blank=True, null=True)
    nmaxpiercecount = models.IntegerField(db_column='nMaxPierceCount', blank=True, null=True)
    nminnumshots = models.IntegerField(db_column='nMinNumShots', blank=True, null=True)
    nrayspershot = models.IntegerField(db_column='nRaysPerShot', blank=True, null=True)
    ntracerfrequency = models.IntegerField(db_column='nTracerFrequency', blank=True, null=True)
    bcanhitownvehicle = models.IntegerField(db_column='bCanHitOwnVehicle', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RangedWeaponType'


class Ratingbands(models.Model):
    id = models.IntegerField(primary_key=True)
    fthreatincrement = models.FloatField(db_column='fThreatIncrement', blank=True, null=True)
    nbegins = models.IntegerField(db_column='nBegins', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RatingBands'


class Ratingtextures(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplaynamecrim = models.TextField(db_column='sDisplayNameCrim', blank=True, null=True)
    sdisplaynameenf = models.TextField(db_column='sDisplayNameEnf', blank=True, null=True)
    ehudiconcombocriminal_0 = models.IntegerField(db_column='eHUDIconComboCriminal_0', blank=True, null=True)
    ehudiconcombocriminal_1 = models.IntegerField(db_column='eHUDIconComboCriminal_1', blank=True, null=True)
    ehudiconcombocriminal_2 = models.IntegerField(db_column='eHUDIconComboCriminal_2', blank=True, null=True)
    ehudiconcombocriminal_3 = models.IntegerField(db_column='eHUDIconComboCriminal_3', blank=True, null=True)
    ehudiconcombocriminal_4 = models.IntegerField(db_column='eHUDIconComboCriminal_4', blank=True, null=True)
    ehudiconcomboenforcer_0 = models.IntegerField(db_column='eHUDIconComboEnforcer_0', blank=True, null=True)
    ehudiconcomboenforcer_1 = models.IntegerField(db_column='eHUDIconComboEnforcer_1', blank=True, null=True)
    ehudiconcomboenforcer_2 = models.IntegerField(db_column='eHUDIconComboEnforcer_2', blank=True, null=True)
    ehudiconcomboenforcer_3 = models.IntegerField(db_column='eHUDIconComboEnforcer_3', blank=True, null=True)
    ehudiconcomboenforcer_4 = models.IntegerField(db_column='eHUDIconComboEnforcer_4', blank=True, null=True)
    ehudtextureiconcriminal_0 = models.IntegerField(db_column='eHUDTextureIconCriminal_0', blank=True, null=True)
    ehudtextureiconcriminal_1 = models.IntegerField(db_column='eHUDTextureIconCriminal_1', blank=True, null=True)
    ehudtextureiconcriminal_2 = models.IntegerField(db_column='eHUDTextureIconCriminal_2', blank=True, null=True)
    ehudtextureiconcriminal_3 = models.IntegerField(db_column='eHUDTextureIconCriminal_3', blank=True, null=True)
    ehudtextureiconcriminal_4 = models.IntegerField(db_column='eHUDTextureIconCriminal_4', blank=True, null=True)
    ehudtextureiconenforcer_0 = models.IntegerField(db_column='eHUDTextureIconEnforcer_0', blank=True, null=True)
    ehudtextureiconenforcer_1 = models.IntegerField(db_column='eHUDTextureIconEnforcer_1', blank=True, null=True)
    ehudtextureiconenforcer_2 = models.IntegerField(db_column='eHUDTextureIconEnforcer_2', blank=True, null=True)
    ehudtextureiconenforcer_3 = models.IntegerField(db_column='eHUDTextureIconEnforcer_3', blank=True, null=True)
    ehudtextureiconenforcer_4 = models.IntegerField(db_column='eHUDTextureIconEnforcer_4', blank=True, null=True)
    eratingtexture = models.IntegerField(db_column='eRatingTexture', blank=True, null=True)
    escaleformiconcriminal_0 = models.IntegerField(db_column='eScaleformIconCriminal_0', blank=True, null=True)
    escaleformiconcriminal_1 = models.IntegerField(db_column='eScaleformIconCriminal_1', blank=True, null=True)
    escaleformiconcriminal_2 = models.IntegerField(db_column='eScaleformIconCriminal_2', blank=True, null=True)
    escaleformiconcriminal_3 = models.IntegerField(db_column='eScaleformIconCriminal_3', blank=True, null=True)
    escaleformiconcriminal_4 = models.IntegerField(db_column='eScaleformIconCriminal_4', blank=True, null=True)
    escaleformiconenforcer_0 = models.IntegerField(db_column='eScaleformIconEnforcer_0', blank=True, null=True)
    escaleformiconenforcer_1 = models.IntegerField(db_column='eScaleformIconEnforcer_1', blank=True, null=True)
    escaleformiconenforcer_2 = models.IntegerField(db_column='eScaleformIconEnforcer_2', blank=True, null=True)
    escaleformiconenforcer_3 = models.IntegerField(db_column='eScaleformIconEnforcer_3', blank=True, null=True)
    escaleformiconenforcer_4 = models.IntegerField(db_column='eScaleformIconEnforcer_4', blank=True, null=True)
    nrating = models.IntegerField(db_column='nRating', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RatingTextures'


class Redeemablerewards(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    smailbody = models.TextField(db_column='sMailBody', blank=True, null=True)
    smailsubject = models.TextField(db_column='sMailSubject', blank=True, null=True)
    ehudicon = models.IntegerField(db_column='eHUDIcon', blank=True, null=True)
    eredeemablereward = models.IntegerField(db_column='eRedeemableReward', blank=True, null=True)
    ereward = models.IntegerField(db_column='eReward', blank=True, null=True)
    nkey = models.IntegerField(db_column='nKey', blank=True, null=True)
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)
    bignoresddvalidation = models.IntegerField(db_column='bIgnoreSddValidation', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RedeemableRewards'


class Referafriendevents(models.Model):
    id = models.IntegerField(primary_key=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    ereferafriendevent = models.IntegerField(db_column='eReferAFriendEvent', blank=True, null=True)
    bunique = models.IntegerField(db_column='bUnique', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ReferAFriendEvents'


class Rewardpackagechildren(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    eitems_0 = models.IntegerField(db_column='eItems_0', blank=True, null=True)
    eitems_1 = models.IntegerField(db_column='eItems_1', blank=True, null=True)
    eitems_10 = models.IntegerField(db_column='eItems_10', blank=True, null=True)
    eitems_11 = models.IntegerField(db_column='eItems_11', blank=True, null=True)
    eitems_12 = models.IntegerField(db_column='eItems_12', blank=True, null=True)
    eitems_13 = models.IntegerField(db_column='eItems_13', blank=True, null=True)
    eitems_14 = models.IntegerField(db_column='eItems_14', blank=True, null=True)
    eitems_15 = models.IntegerField(db_column='eItems_15', blank=True, null=True)
    eitems_16 = models.IntegerField(db_column='eItems_16', blank=True, null=True)
    eitems_17 = models.IntegerField(db_column='eItems_17', blank=True, null=True)
    eitems_18 = models.IntegerField(db_column='eItems_18', blank=True, null=True)
    eitems_19 = models.IntegerField(db_column='eItems_19', blank=True, null=True)
    eitems_2 = models.IntegerField(db_column='eItems_2', blank=True, null=True)
    eitems_20 = models.IntegerField(db_column='eItems_20', blank=True, null=True)
    eitems_21 = models.IntegerField(db_column='eItems_21', blank=True, null=True)
    eitems_22 = models.IntegerField(db_column='eItems_22', blank=True, null=True)
    eitems_23 = models.IntegerField(db_column='eItems_23', blank=True, null=True)
    eitems_24 = models.IntegerField(db_column='eItems_24', blank=True, null=True)
    eitems_25 = models.IntegerField(db_column='eItems_25', blank=True, null=True)
    eitems_26 = models.IntegerField(db_column='eItems_26', blank=True, null=True)
    eitems_27 = models.IntegerField(db_column='eItems_27', blank=True, null=True)
    eitems_28 = models.IntegerField(db_column='eItems_28', blank=True, null=True)
    eitems_29 = models.IntegerField(db_column='eItems_29', blank=True, null=True)
    eitems_3 = models.IntegerField(db_column='eItems_3', blank=True, null=True)
    eitems_30 = models.IntegerField(db_column='eItems_30', blank=True, null=True)
    eitems_31 = models.IntegerField(db_column='eItems_31', blank=True, null=True)
    eitems_32 = models.IntegerField(db_column='eItems_32', blank=True, null=True)
    eitems_33 = models.IntegerField(db_column='eItems_33', blank=True, null=True)
    eitems_34 = models.IntegerField(db_column='eItems_34', blank=True, null=True)
    eitems_35 = models.IntegerField(db_column='eItems_35', blank=True, null=True)
    eitems_36 = models.IntegerField(db_column='eItems_36', blank=True, null=True)
    eitems_37 = models.IntegerField(db_column='eItems_37', blank=True, null=True)
    eitems_38 = models.IntegerField(db_column='eItems_38', blank=True, null=True)
    eitems_39 = models.IntegerField(db_column='eItems_39', blank=True, null=True)
    eitems_4 = models.IntegerField(db_column='eItems_4', blank=True, null=True)
    eitems_5 = models.IntegerField(db_column='eItems_5', blank=True, null=True)
    eitems_6 = models.IntegerField(db_column='eItems_6', blank=True, null=True)
    eitems_7 = models.IntegerField(db_column='eItems_7', blank=True, null=True)
    eitems_8 = models.IntegerField(db_column='eItems_8', blank=True, null=True)
    eitems_9 = models.IntegerField(db_column='eItems_9', blank=True, null=True)
    erewardpackagechild = models.IntegerField(db_column='eRewardPackageChild', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    bselectable = models.IntegerField(db_column='bSelectable', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RewardPackageChildren'


class Rewardpackageitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    smailbody = models.TextField(db_column='sMailBody', blank=True, null=True)
    smailsubject = models.TextField(db_column='sMailSubject', blank=True, null=True)
    echeckunlock = models.IntegerField(db_column='eCheckUnlock', blank=True, null=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    erewardpackage = models.IntegerField(db_column='eRewardPackage', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    egenderrestriction = models.IntegerField(db_column='eGenderRestriction', blank=True, null=True)
    bdescriptionshowsitems = models.IntegerField(db_column='bDescriptionShowsItems', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RewardPackageItemTypes'


class Rewardpackages(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    echildpackage = models.IntegerField(db_column='eChildPackage', blank=True, null=True)
    eitems_0 = models.IntegerField(db_column='eItems_0', blank=True, null=True)
    eitems_1 = models.IntegerField(db_column='eItems_1', blank=True, null=True)
    eitems_2 = models.IntegerField(db_column='eItems_2', blank=True, null=True)
    eitems_3 = models.IntegerField(db_column='eItems_3', blank=True, null=True)
    eitems_4 = models.IntegerField(db_column='eItems_4', blank=True, null=True)
    eitems_5 = models.IntegerField(db_column='eItems_5', blank=True, null=True)
    eitems_6 = models.IntegerField(db_column='eItems_6', blank=True, null=True)
    eitems_7 = models.IntegerField(db_column='eItems_7', blank=True, null=True)
    eitems_8 = models.IntegerField(db_column='eItems_8', blank=True, null=True)
    eitems_9 = models.IntegerField(db_column='eItems_9', blank=True, null=True)
    erewardpackage = models.IntegerField(db_column='eRewardPackage', blank=True, null=True)
    ncash = models.IntegerField(db_column='nCash', blank=True, null=True)
    ncharges_0 = models.IntegerField(db_column='nCharges_0', blank=True, null=True)
    ncharges_1 = models.IntegerField(db_column='nCharges_1', blank=True, null=True)
    nrewardtokens_0 = models.IntegerField(db_column='nRewardTokens_0', blank=True, null=True)
    nrewardtokens_1 = models.IntegerField(db_column='nRewardTokens_1', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    bsendmail = models.IntegerField(db_column='bSendMail', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RewardPackages'


class Rolemilestoneformulae(models.Model):
    id = models.IntegerField(primary_key=True)
    erolemilestoneformula = models.IntegerField(db_column='eRoleMilestoneFormula', blank=True, null=True)
    ba_optional = models.IntegerField(db_column='bA_Optional', blank=True, null=True)
    ba_required = models.IntegerField(db_column='bA_Required', blank=True, null=True)
    bb_optional = models.IntegerField(db_column='bB_Optional', blank=True, null=True)
    bb_required = models.IntegerField(db_column='bB_Required', blank=True, null=True)
    bc_optional = models.IntegerField(db_column='bC_Optional', blank=True, null=True)
    bc_required = models.IntegerField(db_column='bC_Required', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoleMilestoneFormulae'


class Rolemilestones(models.Model):
    id = models.IntegerField(primary_key=True)
    siconoverlaytext = models.TextField(db_column='sIconOverlayText', blank=True, null=True)
    srewardmailbody = models.TextField(db_column='sRewardMailBody', blank=True, null=True)
    srewardmailsubject = models.TextField(db_column='sRewardMailSubject', blank=True, null=True)
    stitle = models.TextField(db_column='sTitle', blank=True, null=True)
    eformula = models.IntegerField(db_column='eFormula', blank=True, null=True)
    ereward = models.IntegerField(db_column='eReward', blank=True, null=True)
    eroleicon = models.IntegerField(db_column='eRoleIcon', blank=True, null=True)
    erolemilestone = models.IntegerField(db_column='eRoleMilestone', blank=True, null=True)
    fpassmark_0 = models.FloatField(db_column='fPassMark_0', blank=True, null=True)
    fpassmark_1 = models.FloatField(db_column='fPassMark_1', blank=True, null=True)
    fpassmark_2 = models.FloatField(db_column='fPassMark_2', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoleMilestones'


class Rulesetexclusions(models.Model):
    id = models.IntegerField(primary_key=True)
    eruleset_0 = models.IntegerField(db_column='eRuleSet_0', blank=True, null=True)
    eruleset_1 = models.IntegerField(db_column='eRuleSet_1', blank=True, null=True)
    eruleset_2 = models.IntegerField(db_column='eRuleSet_2', blank=True, null=True)
    eruleset_3 = models.IntegerField(db_column='eRuleSet_3', blank=True, null=True)
    eruleset_4 = models.IntegerField(db_column='eRuleSet_4', blank=True, null=True)
    eruleset_5 = models.IntegerField(db_column='eRuleSet_5', blank=True, null=True)
    eruleset_6 = models.IntegerField(db_column='eRuleSet_6', blank=True, null=True)
    eruleset_7 = models.IntegerField(db_column='eRuleSet_7', blank=True, null=True)
    eruleset_8 = models.IntegerField(db_column='eRuleSet_8', blank=True, null=True)
    eruleset_9 = models.IntegerField(db_column='eRuleSet_9', blank=True, null=True)
    erulesetexclusion = models.IntegerField(db_column='eRuleSetExclusion', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RuleSetExclusions'


class Scaleformcriticaltimers(models.Model):
    id = models.IntegerField(primary_key=True)
    sicon = models.TextField(db_column='sIcon', blank=True, null=True)
    stext = models.TextField(db_column='sText', blank=True, null=True)
    npriority = models.IntegerField(db_column='nPriority', blank=True, null=True)
    escaleformcriticaltimer = models.IntegerField(db_column='eScaleformCriticalTimer', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ScaleformCriticalTimers'


class Scaleformicons(models.Model):
    id = models.IntegerField(primary_key=True)
    siconsetname = models.TextField(db_column='sIconSetName', blank=True, null=True)
    smoviename = models.TextField(db_column='sMovieName', blank=True, null=True)
    escaleformicon = models.IntegerField(db_column='eScaleformIcon', blank=True, null=True)
    nframenumber = models.IntegerField(db_column='nFrameNumber', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ScaleformIcons'


class Scaleforminterfaces(models.Model):
    id = models.IntegerField(primary_key=True)
    sscene = models.TextField(db_column='sScene', blank=True, null=True)
    elayer = models.IntegerField(db_column='eLayer', blank=True, null=True)
    npriority = models.IntegerField(db_column='nPriority', blank=True, null=True)
    elayoutmode = models.IntegerField(db_column='eLayoutMode', blank=True, null=True)
    escaleforminterface = models.IntegerField(db_column='eScaleformInterface', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ScaleformInterfaces'


class Scaleformlayers(models.Model):
    id = models.IntegerField(primary_key=True)
    slayerbackground = models.TextField(db_column='sLayerBackground', blank=True, null=True)
    escaleformlayer = models.IntegerField(db_column='eScaleformLayer', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    bblurwhenactive = models.IntegerField(db_column='bBlurWhenActive', blank=True, null=True)
    bcaptureinput = models.IntegerField(db_column='bCaptureInput', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ScaleformLayers'


class Scenelayers(models.Model):
    id = models.IntegerField(primary_key=True)
    escenelayer = models.IntegerField(db_column='eSceneLayer', blank=True, null=True)
    blimitopenfrequency = models.IntegerField(db_column='bLimitOpenFrequency', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SceneLayers'


class Scorecategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    escorecategory = models.IntegerField(db_column='eScoreCategory', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ScoreCategories'


class Scoreboarddescriptions(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplaytext = models.TextField(db_column='sDisplayText', blank=True, null=True)
    escoreboarddescription = models.IntegerField(db_column='eScoreboardDescription', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ScoreboardDescriptions'


class Securityviolations(models.Model):
    id = models.IntegerField(primary_key=True)
    scategory = models.TextField(db_column='sCategory', blank=True, null=True)
    skickmessage = models.TextField(db_column='sKickMessage', blank=True, null=True)
    nbandurationdays = models.IntegerField(db_column='nBanDurationDays', blank=True, null=True)
    esecurityviolation = models.IntegerField(db_column='eSecurityViolation', blank=True, null=True)
    bban = models.IntegerField(db_column='bBan', blank=True, null=True)
    bkick = models.IntegerField(db_column='bKick', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SecurityViolations'


class Shopuifilterrestrictions(models.Model):
    id = models.IntegerField(primary_key=True)
    eiteminfracategory = models.IntegerField(db_column='eItemInfraCategory', blank=True, null=True)
    eshopuifilterrestriction = models.IntegerField(db_column='eShopUIFilterRestriction', blank=True, null=True)
    eunlockvehiclecomponentcategory = models.IntegerField(db_column='eUnlockVehicleComponentCategory', blank=True, null=True)
    eunlockweapontype = models.IntegerField(db_column='eUnlockWeaponType', blank=True, null=True)
    eweapontype = models.IntegerField(db_column='eWeaponType', blank=True, null=True)
    ecustomisable = models.IntegerField(db_column='eCustomisable', blank=True, null=True)
    eitemcategory = models.IntegerField(db_column='eItemCategory', blank=True, null=True)
    eitemsubcategory = models.IntegerField(db_column='eItemSubCategory', blank=True, null=True)
    emodifierclass = models.IntegerField(db_column='eModifierClass', blank=True, null=True)
    emodifiertype = models.IntegerField(db_column='eModifierType', blank=True, null=True)
    eunlockitemcategory = models.IntegerField(db_column='eUnlockItemCategory', blank=True, null=True)
    eunlockitemsubcategory = models.IntegerField(db_column='eUnlockItemSubCategory', blank=True, null=True)
    eunlockmodifierclass = models.IntegerField(db_column='eUnlockModifierClass', blank=True, null=True)
    eunlockmodifiertype = models.IntegerField(db_column='eUnlockModifierType', blank=True, null=True)
    bembeddeditem = models.IntegerField(db_column='bEmbeddedItem', blank=True, null=True)
    bequipable = models.IntegerField(db_column='bEquipable', blank=True, null=True)
    bnotdeployed = models.IntegerField(db_column='bNotDeployed', blank=True, null=True)
    btrade = models.IntegerField(db_column='bTrade', blank=True, null=True)
    bunlockcapacity = models.IntegerField(db_column='bUnlockCapacity', blank=True, null=True)
    bunlockemote = models.IntegerField(db_column='bUnlockEmote', blank=True, null=True)
    bunlocksymbolprimitive = models.IntegerField(db_column='bUnlockSymbolPrimitive', blank=True, null=True)
    bunlockvehiclecomponent = models.IntegerField(db_column='bUnlockVehicleComponent', blank=True, null=True)
    bunused = models.IntegerField(db_column='bUnused', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ShopUIFilterRestrictions'


class Shopuifilters(models.Model):
    id = models.IntegerField(primary_key=True)
    sname = models.TextField(db_column='sName', blank=True, null=True)
    eenable_0 = models.IntegerField(db_column='eEnable_0', blank=True, null=True)
    eenable_1 = models.IntegerField(db_column='eEnable_1', blank=True, null=True)
    eenable_2 = models.IntegerField(db_column='eEnable_2', blank=True, null=True)
    eoption_0 = models.IntegerField(db_column='eOption_0', blank=True, null=True)
    eoption_1 = models.IntegerField(db_column='eOption_1', blank=True, null=True)
    eoption_2 = models.IntegerField(db_column='eOption_2', blank=True, null=True)
    eoption_3 = models.IntegerField(db_column='eOption_3', blank=True, null=True)
    eparent = models.IntegerField(db_column='eParent', blank=True, null=True)
    eshop_0 = models.IntegerField(db_column='eShop_0', blank=True, null=True)
    eshop_1 = models.IntegerField(db_column='eShop_1', blank=True, null=True)
    eshop_2 = models.IntegerField(db_column='eShop_2', blank=True, null=True)
    eshop_3 = models.IntegerField(db_column='eShop_3', blank=True, null=True)
    eshop_4 = models.IntegerField(db_column='eShop_4', blank=True, null=True)
    eshopuifilter = models.IntegerField(db_column='eShopUIFilter', blank=True, null=True)
    ndefaultweighting = models.IntegerField(db_column='nDefaultWeighting', blank=True, null=True)
    bdevonly = models.IntegerField(db_column='bDevOnly', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ShopUIFilters'


class Shopuishops(models.Model):
    id = models.IntegerField(primary_key=True)
    eshopuishop = models.IntegerField(db_column='eShopUIShop', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ShopUIShops'


class Skillratingconstants(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)
    eskillratingconstant = models.IntegerField(db_column='eSkillRatingConstant', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SkillRatingConstants'


class Songitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sresource = models.TextField(db_column='sResource', blank=True, null=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SongItemTypes'


class Spawnconstant(models.Model):
    id = models.IntegerField(primary_key=True)
    fvalue = models.FloatField(db_column='fValue', blank=True, null=True)
    espawnconstant = models.IntegerField(db_column='eSpawnConstant', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SpawnConstant'


class Spawnvariables(models.Model):
    id = models.IntegerField(primary_key=True)
    fspawndistanceafk = models.FloatField(db_column='fSpawnDistanceAFK', blank=True, null=True)
    fspawndistanceobjectivemaximum = models.FloatField(db_column='fSpawnDistanceObjectiveMaximum', blank=True, null=True)
    fspawndistanceobjectiveminimum = models.FloatField(db_column='fSpawnDistanceObjectiveMinimum', blank=True, null=True)
    fspawndistanceopponentignored = models.FloatField(db_column='fSpawnDistanceOpponentIgnored', blank=True, null=True)
    fspawndistanceopponentinvalid = models.FloatField(db_column='fSpawnDistanceOpponentInvalid', blank=True, null=True)
    fspawndistanceoppositionspawnzone = models.FloatField(db_column='fSpawnDistanceOppositionSpawnZone', blank=True, null=True)
    fspawndistanceotherspawnzone = models.FloatField(db_column='fSpawnDistanceOtherSpawnZone', blank=True, null=True)
    fspawndistanceplayer = models.FloatField(db_column='fSpawnDistancePlayer', blank=True, null=True)
    fspawndistanceteammateliving = models.FloatField(db_column='fSpawnDistanceTeamMateLiving', blank=True, null=True)
    fspawnvehicledistanceopponent = models.FloatField(db_column='fSpawnVehicleDistanceOpponent', blank=True, null=True)
    fspawnvehicledistanceplayermaximum = models.FloatField(db_column='fSpawnVehicleDistancePlayerMaximum', blank=True, null=True)
    fspawnvehicledistanceplayerminimum = models.FloatField(db_column='fSpawnVehicleDistancePlayerMinimum', blank=True, null=True)
    fspawnvehicleheightmaximum = models.FloatField(db_column='fSpawnVehicleHeightMaximum', blank=True, null=True)
    fspawnwo = models.FloatField(db_column='fSpawnWo', blank=True, null=True)
    fspawnwp = models.FloatField(db_column='fSpawnWp', blank=True, null=True)
    erelaxationrule = models.IntegerField(db_column='eRelaxationRule', blank=True, null=True)
    espawnvariable = models.IntegerField(db_column='eSpawnVariable', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SpawnVariables'


class Streetname(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayedstreetname = models.TextField(db_column='sDisplayedStreetName', blank=True, null=True)
    edistrict = models.IntegerField(db_column='eDistrict', blank=True, null=True)
    estreetnameid = models.IntegerField(db_column='eStreetNameID', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'StreetName'


class Symboleditormenuentries(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayimage = models.TextField(db_column='sDisplayImage', blank=True, null=True)
    sdisplaytext = models.TextField(db_column='sDisplayText', blank=True, null=True)
    smenulevel = models.TextField(db_column='sMenuLevel', blank=True, null=True)
    smenutag = models.TextField(db_column='sMenuTag', blank=True, null=True)
    soptionalscene = models.TextField(db_column='sOptionalScene', blank=True, null=True)
    esymboleditormenuentry = models.IntegerField(db_column='eSymbolEditorMenuEntry', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SymbolEditorMenuEntries'


class Symbolitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sresource = models.TextField(db_column='sResource', blank=True, null=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SymbolItemTypes'


class Tesprojectioninfos(models.Model):
    id = models.IntegerField(primary_key=True)
    fmaxvalueatpremiumlevel_0 = models.FloatField(db_column='fMaxValueAtPremiumLevel_0', blank=True, null=True)
    fmaxvalueatpremiumlevel_1 = models.FloatField(db_column='fMaxValueAtPremiumLevel_1', blank=True, null=True)
    etesprojectioninfo = models.IntegerField(db_column='eTESProjectionInfo', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TESProjectionInfos'


class TodEventAllowedtooverrides(models.Model):
    id = models.IntegerField(primary_key=True)
    eevent_allowedtooverride = models.IntegerField(db_column='eEvent_AllowedToOverride', blank=True, null=True)
    etod_event = models.IntegerField(db_column='eTOD_Event', blank=True, null=True)
    etod = models.IntegerField(db_column='eTOD', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TOD_Event_AllowedToOverrides'


class TodEvents(models.Model):
    id = models.IntegerField(primary_key=True)
    etod_event = models.IntegerField(db_column='eTOD_Event', blank=True, null=True)
    eevent = models.IntegerField(db_column='eEvent', blank=True, null=True)
    etod = models.IntegerField(db_column='eTOD', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TOD_Events'


class Taskitemboomboxes(models.Model):
    id = models.IntegerField(primary_key=True)
    samptype = models.TextField(db_column='sAmpType', blank=True, null=True)
    efriendlyhudmarker = models.IntegerField(db_column='eFriendlyHUDMarker', blank=True, null=True)
    eoppositionhudmarker = models.IntegerField(db_column='eOppositionHUDMarker', blank=True, null=True)
    etaskitemboombox = models.IntegerField(db_column='eTaskItemBoomBox', blank=True, null=True)
    fampattenuationscale = models.FloatField(db_column='fAmpAttenuationScale', blank=True, null=True)
    fampvolume = models.FloatField(db_column='fAmpVolume', blank=True, null=True)
    ffriendlyradius = models.FloatField(db_column='fFriendlyRadius', blank=True, null=True)
    foppositionradius = models.FloatField(db_column='fOppositionRadius', blank=True, null=True)
    fspeakereq1 = models.FloatField(db_column='fSpeakerEQ1', blank=True, null=True)
    fspeakereq2 = models.FloatField(db_column='fSpeakerEQ2', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskItemBoomBoxes'


class Taskitemcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    etaskitemcategory = models.IntegerField(db_column='eTaskItemCategory', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskItemCategories'


class Taskitemdamagedpickups(models.Model):
    id = models.IntegerField(primary_key=True)
    sassetname = models.TextField(db_column='sAssetName', blank=True, null=True)
    sdamagesfx = models.TextField(db_column='sDamageSFX', blank=True, null=True)
    sdamagevfx = models.TextField(db_column='sDamageVFX', blank=True, null=True)
    srecoversfx = models.TextField(db_column='sRecoverSFX', blank=True, null=True)
    srecovervfx = models.TextField(db_column='sRecoverVFX', blank=True, null=True)
    etaskitemvisual = models.IntegerField(db_column='eTaskItemVisual', blank=True, null=True)
    bdetroyeddamagestate = models.IntegerField(db_column='bDetroyedDamageState', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskItemDamagedPickups'


class Taskitemeffects(models.Model):
    id = models.IntegerField(primary_key=True)
    stimedexplosivesfxend = models.TextField(db_column='sTimedExplosiveSFXEnd', blank=True, null=True)
    stimedexplosivesfxstart = models.TextField(db_column='sTimedExplosiveSFXStart', blank=True, null=True)
    eboombox = models.IntegerField(db_column='eBoomBox', blank=True, null=True)
    eexplosion = models.IntegerField(db_column='eExplosion', blank=True, null=True)
    etaskitemeffect = models.IntegerField(db_column='eTaskItemEffect', blank=True, null=True)
    ffieldsupplierradius = models.FloatField(db_column='fFieldSupplierRadius', blank=True, null=True)
    fjumpzmodifier = models.FloatField(db_column='fJumpZModifier', blank=True, null=True)
    frepairmultiplier = models.FloatField(db_column='fRepairMultiplier', blank=True, null=True)
    ftimedexplosionduration = models.FloatField(db_column='fTimedExplosionDuration', blank=True, null=True)
    nfieldsupplieramount = models.IntegerField(db_column='nFieldSupplierAmount', blank=True, null=True)
    nhealth = models.IntegerField(db_column='nHealth', blank=True, null=True)
    nsymbolmaterialindex = models.IntegerField(db_column='nSymbolMaterialIndex', blank=True, null=True)
    bdontbounce = models.IntegerField(db_column='bDontBounce', blank=True, null=True)
    bhasgrip = models.IntegerField(db_column='bHasGrip', blank=True, null=True)
    bhostssymbol = models.IntegerField(db_column='bHostsSymbol', blank=True, null=True)
    bragdollondeath = models.IntegerField(db_column='bRagdollOnDeath', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskItemEffects'


class Taskitemgiftboxcontents(models.Model):
    id = models.IntegerField(primary_key=True)
    edefaultweaponskin = models.IntegerField(db_column='eDefaultWeaponSkin', blank=True, null=True)
    efnmods_0 = models.IntegerField(db_column='eFnMods_0', blank=True, null=True)
    efnmods_1 = models.IntegerField(db_column='eFnMods_1', blank=True, null=True)
    efnmods_2 = models.IntegerField(db_column='eFnMods_2', blank=True, null=True)
    eitemtype = models.IntegerField(db_column='eItemType', blank=True, null=True)
    etaskitemgiftbox = models.IntegerField(db_column='eTaskItemGiftBox', blank=True, null=True)
    nmaxextraitems = models.IntegerField(db_column='nMaxExtraItems', blank=True, null=True)
    nminextraitems = models.IntegerField(db_column='nMinExtraItems', blank=True, null=True)
    nweight = models.IntegerField(db_column='nWeight', blank=True, null=True)
    bselectrandomskin = models.IntegerField(db_column='bSelectRandomSkin', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskItemGiftBoxContents'


class Taskitemgiftboxmodifierentries(models.Model):
    id = models.IntegerField(primary_key=True)
    ecategory = models.IntegerField(db_column='eCategory', blank=True, null=True)
    eitem = models.IntegerField(db_column='eItem', blank=True, null=True)
    etaskitemgiftboxmodifier = models.IntegerField(db_column='eTaskItemGiftBoxModifier', blank=True, null=True)
    fweight = models.FloatField(db_column='fWeight', blank=True, null=True)
    etheme = models.IntegerField(db_column='eTheme', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskItemGiftBoxModifierEntries'


class Taskitemgiftboxmodifiers(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskitemgiftboxmodifier = models.IntegerField(db_column='eTaskItemGiftBoxModifier', blank=True, null=True)
    fchancenomod = models.FloatField(db_column='fChanceNoMod', blank=True, null=True)
    fweightperlevel_0 = models.FloatField(db_column='fWeightPerLevel_0', blank=True, null=True)
    fweightperlevel_1 = models.FloatField(db_column='fWeightPerLevel_1', blank=True, null=True)
    fweightperlevel_2 = models.FloatField(db_column='fWeightPerLevel_2', blank=True, null=True)
    fweightperlevel_3 = models.FloatField(db_column='fWeightPerLevel_3', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskItemGiftBoxModifiers'


class Taskitemgiftboxes(models.Model):
    id = models.IntegerField(primary_key=True)
    sactivevfx = models.TextField(db_column='sActiveVFX', blank=True, null=True)
    sinactivevfx = models.TextField(db_column='sInactiveVFX', blank=True, null=True)
    sstartactivesfx = models.TextField(db_column='sStartActiveSFX', blank=True, null=True)
    sstopactivesfx = models.TextField(db_column='sStopActiveSFX', blank=True, null=True)
    etaskitemgiftbox = models.IntegerField(db_column='eTaskItemGiftBox', blank=True, null=True)
    factivationspintime = models.FloatField(db_column='fActivationSpinTime', blank=True, null=True)
    faddeddropdirectionalvelocitymax = models.FloatField(db_column='fAddedDropDirectionalVelocityMax', blank=True, null=True)
    faddeddropdirectionalvelocitymin = models.FloatField(db_column='fAddedDropDirectionalVelocityMin', blank=True, null=True)
    faddeddropupvelocitymax = models.FloatField(db_column='fAddedDropUpVelocityMax', blank=True, null=True)
    faddeddropupvelocitymin = models.FloatField(db_column='fAddedDropUpVelocityMin', blank=True, null=True)
    fmaximumrotationspeed = models.FloatField(db_column='fMaximumRotationSpeed', blank=True, null=True)
    frotationacceleration = models.FloatField(db_column='fRotationAcceleration', blank=True, null=True)
    frotationspeed = models.FloatField(db_column='fRotationSpeed', blank=True, null=True)
    fvfxoffsetx = models.FloatField(db_column='fVFXOffsetX', blank=True, null=True)
    fvfxoffsety = models.FloatField(db_column='fVFXOffsetY', blank=True, null=True)
    fvfxoffsetz = models.FloatField(db_column='fVFXOffsetZ', blank=True, null=True)
    eavailability = models.IntegerField(db_column='eAvailability', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskItemGiftBoxes'


class Taskitemsizes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    ncargopips = models.IntegerField(db_column='nCargoPips', blank=True, null=True)
    eencumbrance = models.IntegerField(db_column='eEncumbrance', blank=True, null=True)
    etaskitemsize = models.IntegerField(db_column='eTaskItemSize', blank=True, null=True)
    bcancarry = models.IntegerField(db_column='bCanCarry', blank=True, null=True)
    bslowpickup = models.IntegerField(db_column='bSlowPickup', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskItemSizes'


class Taskitemsubcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    egameplayobject = models.IntegerField(db_column='eGameplayObject', blank=True, null=True)
    etaskitemsubcategory = models.IntegerField(db_column='eTaskItemSubCategory', blank=True, null=True)
    etaskitemcategory = models.IntegerField(db_column='eTaskItemCategory', blank=True, null=True)
    etaskitemsize = models.IntegerField(db_column='eTaskItemSize', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskItemSubCategories'


class Taskitemtags(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskitemtag = models.IntegerField(db_column='eTaskItemTag', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskItemTags'


class Taskitemvarieties(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    eeffect = models.IntegerField(db_column='eEffect', blank=True, null=True)
    egiftbox = models.IntegerField(db_column='eGiftBox', blank=True, null=True)
    ehudiconcombo = models.IntegerField(db_column='eHUDIconCombo', blank=True, null=True)
    ehudmarkervisual = models.IntegerField(db_column='eHUDMarkerVisual', blank=True, null=True)
    emetatag_0 = models.IntegerField(db_column='eMetaTag_0', blank=True, null=True)
    emetatag_1 = models.IntegerField(db_column='eMetaTag_1', blank=True, null=True)
    emetatag_2 = models.IntegerField(db_column='eMetaTag_2', blank=True, null=True)
    etaskitemsubcategory = models.IntegerField(db_column='eTaskItemSubCategory', blank=True, null=True)
    etaskitemvariety = models.IntegerField(db_column='eTaskItemVariety', blank=True, null=True)
    etaskitemvisual = models.IntegerField(db_column='eTaskItemVisual', blank=True, null=True)
    fgiftboxoffsetx = models.FloatField(db_column='fGiftBoxOffsetX', blank=True, null=True)
    fgiftboxoffsety = models.FloatField(db_column='fGiftBoxOffsetY', blank=True, null=True)
    fgiftboxoffsetz = models.FloatField(db_column='fGiftBoxOffsetZ', blank=True, null=True)
    fvehicleheightreductionamount = models.FloatField(db_column='fVehicleHeightReductionAmount', blank=True, null=True)
    fvehicletorquereductionfactor = models.FloatField(db_column='fVehicleTorqueReductionFactor', blank=True, null=True)
    nexpensetariff = models.IntegerField(db_column='nExpenseTariff', blank=True, null=True)
    bhidehudmarkerwhilecarried = models.IntegerField(db_column='bHideHUDMarkerWhileCarried', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskItemVarieties'


class Taskitemvisuals(models.Model):
    id = models.IntegerField(primary_key=True)
    spickupanimsetasset = models.TextField(db_column='sPickupAnimSetAsset', blank=True, null=True)
    spickupanimtreeasset = models.TextField(db_column='sPickupAnimTreeAsset', blank=True, null=True)
    spickupassetname = models.TextField(db_column='sPickupAssetName', blank=True, null=True)
    spickupphysicsasset = models.TextField(db_column='sPickupPhysicsAsset', blank=True, null=True)
    eitemattachmentvisual = models.IntegerField(db_column='eItemAttachmentVisual', blank=True, null=True)
    etaskitemvisual = models.IntegerField(db_column='eTaskItemVisual', blank=True, null=True)
    fcollisionheight = models.FloatField(db_column='fCollisionHeight', blank=True, null=True)
    fpickupoffsetx = models.FloatField(db_column='fPickupOffsetX', blank=True, null=True)
    fpickupoffsety = models.FloatField(db_column='fPickupOffsetY', blank=True, null=True)
    fpickupoffsetz = models.FloatField(db_column='fPickupOffsetZ', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskItemVisuals'


class Taskobjectives(models.Model):
    id = models.IntegerField(primary_key=True)
    sdispatchbrief = models.TextField(db_column='sDispatchBrief', blank=True, null=True)
    sownerbrief = models.TextField(db_column='sOwnerBrief', blank=True, null=True)
    emissiontemplate = models.IntegerField(db_column='eMissionTemplate', blank=True, null=True)
    eoperation = models.IntegerField(db_column='eOperation', blank=True, null=True)
    etargetallocation = models.IntegerField(db_column='eTargetAllocation', blank=True, null=True)
    etaskitemvariety = models.IntegerField(db_column='eTaskItemVariety', blank=True, null=True)
    etaskobjective = models.IntegerField(db_column='eTaskObjective', blank=True, null=True)
    evehiclecategory = models.IntegerField(db_column='eVehicleCategory', blank=True, null=True)
    ntargetsrequired = models.IntegerField(db_column='nTargetsRequired', blank=True, null=True)
    ntaskitemsavailable = models.IntegerField(db_column='nTaskItemsAvailable', blank=True, null=True)
    ntaskitemsrequired = models.IntegerField(db_column='nTaskItemsRequired', blank=True, null=True)
    ntimelimit = models.IntegerField(db_column='nTimeLimit', blank=True, null=True)
    nvehiclesrequired = models.IntegerField(db_column='nVehiclesRequired', blank=True, null=True)
    eitembatch = models.IntegerField(db_column='eItemBatch', blank=True, null=True)
    eopposingsidevipassignment = models.IntegerField(db_column='eOpposingSideVIPAssignment', blank=True, null=True)
    eowningsidevipassignment = models.IntegerField(db_column='eOwningSideVIPAssignment', blank=True, null=True)
    estage = models.IntegerField(db_column='eStage', blank=True, null=True)
    etaskitemspecificationmethod = models.IntegerField(db_column='eTaskItemSpecificationMethod', blank=True, null=True)
    evehiclebatch = models.IntegerField(db_column='eVehicleBatch', blank=True, null=True)
    bbonustime = models.IntegerField(db_column='bBonusTime', blank=True, null=True)
    bclearopposingsideviptakeoutsonstart = models.IntegerField(db_column='bClearOpposingSideVIPTakeoutsOnStart', blank=True, null=True)
    bclearowningsideviptakeoutsonstart = models.IntegerField(db_column='bClearOwningSideVIPTakeoutsOnStart', blank=True, null=True)
    bcleartakeoutsonstart = models.IntegerField(db_column='bClearTakeoutsOnStart', blank=True, null=True)
    bcompletesconcurrentpair = models.IntegerField(db_column='bCompletesConcurrentPair', blank=True, null=True)
    bdisabletakeouts = models.IntegerField(db_column='bDisableTakeouts', blank=True, null=True)
    bdrawontimeout = models.IntegerField(db_column='bDrawOnTimeOut', blank=True, null=True)
    benabledpvp = models.IntegerField(db_column='bEnabledPvP', blank=True, null=True)
    benableopposingsideviptakeouts = models.IntegerField(db_column='bEnableOpposingSideVIPTakeouts', blank=True, null=True)
    benableowningsideviptakeouts = models.IntegerField(db_column='bEnableOwningSideVIPTakeouts', blank=True, null=True)
    bendonlyontimeout = models.IntegerField(db_column='bEndOnlyOnTimeOut', blank=True, null=True)
    bisconcurrent = models.IntegerField(db_column='bIsConcurrent', blank=True, null=True)
    bisopposition = models.IntegerField(db_column='bIsOpposition', blank=True, null=True)
    bleaveremainingtaskitems = models.IntegerField(db_column='bLeaveRemainingTaskItems', blank=True, null=True)
    bopenworldcashpoolitem = models.IntegerField(db_column='bOpenWorldCashPoolItem', blank=True, null=True)
    boppositionwinontargetdestroyedbyowners = models.IntegerField(db_column='bOppositionWinOnTargetDestroyedByOwners', blank=True, null=True)
    bownerswinontargetdestroyedbyopponent = models.IntegerField(db_column='bOwnersWinOnTargetDestroyedByOpponent', blank=True, null=True)
    bscorepointonwin = models.IntegerField(db_column='bScorePointOnWin', blank=True, null=True)
    bspawnininventory = models.IntegerField(db_column='bSpawnInInventory', blank=True, null=True)
    bwinoncompletion = models.IntegerField(db_column='bWinOnCompletion', blank=True, null=True)
    bwinonunopposedcompletion = models.IntegerField(db_column='bWinOnUnopposedCompletion', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskObjectives'


class Taskoperationarmedguard(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    funused = models.FloatField(db_column='fUnused', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationArmedGuard'


class Taskoperationbusts(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    nhealthpool = models.IntegerField(db_column='nHealthPool', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationBusts'


class Taskoperationcsis(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    fcsaduration = models.FloatField(db_column='fCSADuration', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationCSIs'


class Taskoperationcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    ereticulehint = models.IntegerField(db_column='eReticuleHint', blank=True, null=True)
    fmintakeoutmultiplier = models.FloatField(db_column='fMinTakeoutMultiplier', blank=True, null=True)
    etaskoperationcategory = models.IntegerField(db_column='eTaskOperationCategory', blank=True, null=True)
    bautoinstigateopposition = models.IntegerField(db_column='bAutoInstigateOpposition', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationCategories'


class Taskoperationdeathmatches(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    npadding = models.IntegerField(db_column='nPadding', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationDeathmatches'


class Taskoperationescape(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    farrestedpenaltyseconds = models.FloatField(db_column='fArrestedPenaltySeconds', blank=True, null=True)
    farrestopponentpenaltyseconds = models.FloatField(db_column='fArrestOpponentPenaltySeconds', blank=True, null=True)
    fescapebarlimit = models.FloatField(db_column='fEscapeBarLimit', blank=True, null=True)
    fkilledpenaltyseconds = models.FloatField(db_column='fKilledPenaltySeconds', blank=True, null=True)
    fkillopponentpenaltyseconds = models.FloatField(db_column='fKillOpponentPenaltySeconds', blank=True, null=True)
    ftakedamagepenaltyseconds = models.FloatField(db_column='fTakeDamagePenaltySeconds', blank=True, null=True)
    fweaponfirepenaltyseconds = models.FloatField(db_column='fWeaponFirePenaltySeconds', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationEscape'


class Taskoperationescort(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    ftriggertime = models.FloatField(db_column='fTriggerTime', blank=True, null=True)
    bvipopponentcancapture = models.IntegerField(db_column='bVIPOpponentCanCapture', blank=True, null=True)
    bwinontimeout = models.IntegerField(db_column='bWinOnTimeout', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationEscort'


class Taskoperationhacking(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    fcsaduration = models.FloatField(db_column='fCSADuration', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationHacking'


class Taskoperationmovingtarget(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    npadding = models.IntegerField(db_column='nPadding', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationMovingTarget'


class Taskoperationpickups(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    npadding = models.IntegerField(db_column='nPadding', blank=True, null=True)
    bisvehicledeliverable = models.IntegerField(db_column='bIsVehicleDeliverable', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationPickups'


class Taskoperationsabotages(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    fcsaduration = models.FloatField(db_column='fCSADuration', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationSabotages'


class Taskoperationsurvival(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    npadding = models.IntegerField(db_column='nPadding', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationSurvival'


class Taskoperationterritorycontrols(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    fcapturetime = models.FloatField(db_column='fCaptureTime', blank=True, null=True)
    fresettime = models.FloatField(db_column='fResetTime', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationTerritoryControls'


class Taskoperationuiprofile(models.Model):
    id = models.IntegerField(primary_key=True)
    scriminalbrief = models.TextField(db_column='sCriminalBrief', blank=True, null=True)
    senforcerbrief = models.TextField(db_column='sEnforcerBrief', blank=True, null=True)
    sshortbrief = models.TextField(db_column='sShortBrief', blank=True, null=True)
    strackedvaluedescription_0 = models.TextField(db_column='sTrackedValueDescription_0', blank=True, null=True)
    strackedvaluedescription_1 = models.TextField(db_column='sTrackedValueDescription_1', blank=True, null=True)
    strackedvaluedescription_2 = models.TextField(db_column='sTrackedValueDescription_2', blank=True, null=True)
    strackedvaluedescription_3 = models.TextField(db_column='sTrackedValueDescription_3', blank=True, null=True)
    strackedvalueimage_0 = models.TextField(db_column='sTrackedValueImage_0', blank=True, null=True)
    strackedvalueimage_1 = models.TextField(db_column='sTrackedValueImage_1', blank=True, null=True)
    strackedvalueimage_2 = models.TextField(db_column='sTrackedValueImage_2', blank=True, null=True)
    strackedvalueimage_3 = models.TextField(db_column='sTrackedValueImage_3', blank=True, null=True)
    etaskoperationuiprofile = models.IntegerField(db_column='eTaskOperationUIProfile', blank=True, null=True)
    etrackedstateprofile_0 = models.IntegerField(db_column='eTrackedStateProfile_0', blank=True, null=True)
    etrackedstateprofile_1 = models.IntegerField(db_column='eTrackedStateProfile_1', blank=True, null=True)
    etrackedstateprofile_2 = models.IntegerField(db_column='eTrackedStateProfile_2', blank=True, null=True)
    etrackedstateprofile_3 = models.IntegerField(db_column='eTrackedStateProfile_3', blank=True, null=True)
    etrackedvaluebarfgdisabled_0 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_0', blank=True, null=True)
    etrackedvaluebarfgdisabled_1 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_1', blank=True, null=True)
    etrackedvaluebarfgdisabled_2 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_2', blank=True, null=True)
    etrackedvaluebarfgdisabled_3 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_3', blank=True, null=True)
    etrackedvaluebg_0 = models.IntegerField(db_column='eTrackedValueBg_0', blank=True, null=True)
    etrackedvaluebg_1 = models.IntegerField(db_column='eTrackedValueBg_1', blank=True, null=True)
    etrackedvaluebg_2 = models.IntegerField(db_column='eTrackedValueBg_2', blank=True, null=True)
    etrackedvaluebg_3 = models.IntegerField(db_column='eTrackedValueBg_3', blank=True, null=True)
    etrackedvaluefg_0 = models.IntegerField(db_column='eTrackedValueFg_0', blank=True, null=True)
    etrackedvaluefg_1 = models.IntegerField(db_column='eTrackedValueFg_1', blank=True, null=True)
    etrackedvaluefg_2 = models.IntegerField(db_column='eTrackedValueFg_2', blank=True, null=True)
    etrackedvaluefg_3 = models.IntegerField(db_column='eTrackedValueFg_3', blank=True, null=True)
    etrackedvaluesocket_0 = models.IntegerField(db_column='eTrackedValueSocket_0', blank=True, null=True)
    etrackedvaluesocket_1 = models.IntegerField(db_column='eTrackedValueSocket_1', blank=True, null=True)
    etrackedvaluesocket_2 = models.IntegerField(db_column='eTrackedValueSocket_2', blank=True, null=True)
    etrackedvaluesocket_3 = models.IntegerField(db_column='eTrackedValueSocket_3', blank=True, null=True)
    ntrackedvaluestageoffset_0 = models.IntegerField(db_column='nTrackedValueStageOffset_0', blank=True, null=True)
    ntrackedvaluestageoffset_1 = models.IntegerField(db_column='nTrackedValueStageOffset_1', blank=True, null=True)
    ntrackedvaluestageoffset_2 = models.IntegerField(db_column='nTrackedValueStageOffset_2', blank=True, null=True)
    ntrackedvaluestageoffset_3 = models.IntegerField(db_column='nTrackedValueStageOffset_3', blank=True, null=True)
    etrackedvalue_0 = models.IntegerField(db_column='eTrackedValue_0', blank=True, null=True)
    etrackedvalue_1 = models.IntegerField(db_column='eTrackedValue_1', blank=True, null=True)
    etrackedvalue_2 = models.IntegerField(db_column='eTrackedValue_2', blank=True, null=True)
    etrackedvalue_3 = models.IntegerField(db_column='eTrackedValue_3', blank=True, null=True)
    etrackedvaluedisplay_0 = models.IntegerField(db_column='eTrackedValueDisplay_0', blank=True, null=True)
    etrackedvaluedisplay_1 = models.IntegerField(db_column='eTrackedValueDisplay_1', blank=True, null=True)
    etrackedvaluedisplay_2 = models.IntegerField(db_column='eTrackedValueDisplay_2', blank=True, null=True)
    etrackedvaluedisplay_3 = models.IntegerField(db_column='eTrackedValueDisplay_3', blank=True, null=True)
    bflashwhenchanged_0 = models.IntegerField(db_column='bFlashWhenChanged_0', blank=True, null=True)
    bflashwhenchanged_1 = models.IntegerField(db_column='bFlashWhenChanged_1', blank=True, null=True)
    bflashwhenchanged_2 = models.IntegerField(db_column='bFlashWhenChanged_2', blank=True, null=True)
    bflashwhenchanged_3 = models.IntegerField(db_column='bFlashWhenChanged_3', blank=True, null=True)
    bhideatmax_0 = models.IntegerField(db_column='bHideAtMax_0', blank=True, null=True)
    bhideatmax_1 = models.IntegerField(db_column='bHideAtMax_1', blank=True, null=True)
    bhideatmax_2 = models.IntegerField(db_column='bHideAtMax_2', blank=True, null=True)
    bhideatmax_3 = models.IntegerField(db_column='bHideAtMax_3', blank=True, null=True)
    bhidenamewhendisabled_0 = models.IntegerField(db_column='bHideNameWhenDisabled_0', blank=True, null=True)
    bhidenamewhendisabled_1 = models.IntegerField(db_column='bHideNameWhenDisabled_1', blank=True, null=True)
    bhidenamewhendisabled_2 = models.IntegerField(db_column='bHideNameWhenDisabled_2', blank=True, null=True)
    bhidenamewhendisabled_3 = models.IntegerField(db_column='bHideNameWhenDisabled_3', blank=True, null=True)
    bhidewhenone_0 = models.IntegerField(db_column='bHideWhenOne_0', blank=True, null=True)
    bhidewhenone_1 = models.IntegerField(db_column='bHideWhenOne_1', blank=True, null=True)
    bhidewhenone_2 = models.IntegerField(db_column='bHideWhenOne_2', blank=True, null=True)
    bhidewhenone_3 = models.IntegerField(db_column='bHideWhenOne_3', blank=True, null=True)
    bhidewhenoppositionviptakeoutsdisabled_0 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_0', blank=True, null=True)
    bhidewhenoppositionviptakeoutsdisabled_1 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_1', blank=True, null=True)
    bhidewhenoppositionviptakeoutsdisabled_2 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_2', blank=True, null=True)
    bhidewhenoppositionviptakeoutsdisabled_3 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_3', blank=True, null=True)
    bhidewhenownerviptakeoutsdisabled_0 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_0', blank=True, null=True)
    bhidewhenownerviptakeoutsdisabled_1 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_1', blank=True, null=True)
    bhidewhenownerviptakeoutsdisabled_2 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_2', blank=True, null=True)
    bhidewhenownerviptakeoutsdisabled_3 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_3', blank=True, null=True)
    bhidewhenpointsdisabled_0 = models.IntegerField(db_column='bHideWhenPointsDisabled_0', blank=True, null=True)
    bhidewhenpointsdisabled_1 = models.IntegerField(db_column='bHideWhenPointsDisabled_1', blank=True, null=True)
    bhidewhenpointsdisabled_2 = models.IntegerField(db_column='bHideWhenPointsDisabled_2', blank=True, null=True)
    bhidewhenpointsdisabled_3 = models.IntegerField(db_column='bHideWhenPointsDisabled_3', blank=True, null=True)
    bhidewhentakeoutsdisabled_0 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_0', blank=True, null=True)
    bhidewhentakeoutsdisabled_1 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_1', blank=True, null=True)
    bhidewhentakeoutsdisabled_2 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_2', blank=True, null=True)
    bhidewhentakeoutsdisabled_3 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_3', blank=True, null=True)
    bhidewhenunopposed_0 = models.IntegerField(db_column='bHideWhenUnopposed_0', blank=True, null=True)
    bhidewhenunopposed_1 = models.IntegerField(db_column='bHideWhenUnopposed_1', blank=True, null=True)
    bhidewhenunopposed_2 = models.IntegerField(db_column='bHideWhenUnopposed_2', blank=True, null=True)
    bhidewhenunopposed_3 = models.IntegerField(db_column='bHideWhenUnopposed_3', blank=True, null=True)
    btrackedvalueinoverview_0 = models.IntegerField(db_column='bTrackedValueInOverview_0', blank=True, null=True)
    btrackedvalueinoverview_1 = models.IntegerField(db_column='bTrackedValueInOverview_1', blank=True, null=True)
    btrackedvalueinoverview_2 = models.IntegerField(db_column='bTrackedValueInOverview_2', blank=True, null=True)
    btrackedvalueinoverview_3 = models.IntegerField(db_column='bTrackedValueInOverview_3', blank=True, null=True)
    btrackedvalueonhud_0 = models.IntegerField(db_column='bTrackedValueOnHUD_0', blank=True, null=True)
    btrackedvalueonhud_1 = models.IntegerField(db_column='bTrackedValueOnHUD_1', blank=True, null=True)
    btrackedvalueonhud_2 = models.IntegerField(db_column='bTrackedValueOnHUD_2', blank=True, null=True)
    btrackedvalueonhud_3 = models.IntegerField(db_column='bTrackedValueOnHUD_3', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationUIProfile'


class Taskoperationvehiclecargos(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    fcsaduration = models.FloatField(db_column='fCSADuration', blank=True, null=True)
    bisvehicledeliverable = models.IntegerField(db_column='bIsVehicleDeliverable', blank=True, null=True)
    bvehiclelocked = models.IntegerField(db_column='bVehicleLocked', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationVehicleCargos'


class Taskoperations(models.Model):
    id = models.IntegerField(primary_key=True)
    scriminalbrief = models.TextField(db_column='sCriminalBrief', blank=True, null=True)
    senforcerbrief = models.TextField(db_column='sEnforcerBrief', blank=True, null=True)
    suidescription = models.TextField(db_column='sUIDescription', blank=True, null=True)
    emissionuiprofile = models.IntegerField(db_column='eMissionUIProfile', blank=True, null=True)
    emissionuiprofileopposition = models.IntegerField(db_column='eMissionUIProfileOpposition', blank=True, null=True)
    eoppositiontargethudmarker = models.IntegerField(db_column='eOppositionTargetHUDMarker', blank=True, null=True)
    eoutofmissiontargethudmarker = models.IntegerField(db_column='eOutOfMissionTargetHUDMarker', blank=True, null=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    etasktargethudmarker = models.IntegerField(db_column='eTaskTargetHUDMarker', blank=True, null=True)
    nobjectiveholdpointstarget = models.IntegerField(db_column='nObjectiveHoldPointsTarget', blank=True, null=True)
    enpcworldevent = models.IntegerField(db_column='eNPCWorldEvent', blank=True, null=True)
    eoppositionitemvisibility = models.IntegerField(db_column='eOppositionItemVisibility', blank=True, null=True)
    eoutofmissionitemvisibility = models.IntegerField(db_column='eOutOfMissionItemVisibility', blank=True, null=True)
    eowneritemvisibility = models.IntegerField(db_column='eOwnerItemVisibility', blank=True, null=True)
    etaskoperationcategory = models.IntegerField(db_column='eTaskOperationCategory', blank=True, null=True)
    etasktargetclass = models.IntegerField(db_column='eTaskTargetClass', blank=True, null=True)
    banysidecaninitiate = models.IntegerField(db_column='bAnySideCanInitiate', blank=True, null=True)
    bhidealldeliverablesfromopposition = models.IntegerField(db_column='bHideAllDeliverablesFromOpposition', blank=True, null=True)
    bhidealldeliverablesfromowners = models.IntegerField(db_column='bHideAllDeliverablesFromOwners', blank=True, null=True)
    boppositioncancarrytaskitems = models.IntegerField(db_column='bOppositionCanCarryTaskItems', blank=True, null=True)
    boppositioncaninteractwithvehicles = models.IntegerField(db_column='bOppositionCanInteractWithVehicles', blank=True, null=True)
    boutofmissioncaninteract = models.IntegerField(db_column='bOutOfMissionCanInteract', blank=True, null=True)
    bownerscancarrytaskitems = models.IntegerField(db_column='bOwnersCanCarryTaskItems', blank=True, null=True)
    bownerscaninteractwithvehicles = models.IntegerField(db_column='bOwnersCanInteractWithVehicles', blank=True, null=True)
    bshowoppositiontotaskgroup = models.IntegerField(db_column='bShowOppositionToTaskGroup', blank=True, null=True)
    bshowtaskgrouptoopposition = models.IntegerField(db_column='bShowTaskGroupToOpposition', blank=True, null=True)
    buseobjectiveholdpoints = models.IntegerField(db_column='bUseObjectiveHoldPoints', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperations'


class Taskoperationsarson(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    fcsaduration = models.FloatField(db_column='fCSADuration', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationsArson'


class Taskoperationsbombing(models.Model):
    id = models.IntegerField(primary_key=True)
    ebomblevel = models.IntegerField(db_column='eBombLevel', blank=True, null=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    fbombdisposalguardtime = models.FloatField(db_column='fBombDisposalGuardTime', blank=True, null=True)
    fcsaduration = models.FloatField(db_column='fCSADuration', blank=True, null=True)
    ffusetimer = models.FloatField(db_column='fFuseTimer', blank=True, null=True)
    bisbombdefusable = models.IntegerField(db_column='bIsBombDefusable', blank=True, null=True)
    bisbombrearmable = models.IntegerField(db_column='bIsBombRearmable', blank=True, null=True)
    btriggeronallbombsdefused = models.IntegerField(db_column='bTriggerOnAllBombsDefused', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationsBombing'


class Taskoperationsbuildingbreakin(models.Model):
    id = models.IntegerField(primary_key=True)
    suseactionname = models.TextField(db_column='sUseActionName', blank=True, null=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    fcsaduration = models.FloatField(db_column='fCSADuration', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationsBuildingBreakIn'


class Taskoperationsgraffiti(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    nsprayduration = models.IntegerField(db_column='nSprayDuration', blank=True, null=True)
    bisresprayable = models.IntegerField(db_column='bIsResprayable', blank=True, null=True)
    bstartsneutral = models.IntegerField(db_column='bStartsNeutral', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationsGraffiti'


class Taskoperationsitemdelivery(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    ftriggertime = models.FloatField(db_column='fTriggerTime', blank=True, null=True)
    bdelivertoalltargets = models.IntegerField(db_column='bDeliverToAllTargets', blank=True, null=True)
    bdelivervehicle = models.IntegerField(db_column='bDeliverVehicle', blank=True, null=True)
    bdelivervehiclecargo = models.IntegerField(db_column='bDeliverVehicleCargo', blank=True, null=True)
    bremovedeliverables = models.IntegerField(db_column='bRemoveDeliverables', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationsItemDelivery'


class Taskoperationsnpc(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    fcsaduration = models.FloatField(db_column='fCSADuration', blank=True, null=True)
    ecsastate = models.IntegerField(db_column='eCSAState', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationsNPC'


class Taskoperationsramraid(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    nhealthpool = models.IntegerField(db_column='nHealthPool', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationsRamRaid'


class Taskoperationsrendezvous(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    ftriggertime = models.FloatField(db_column='fTriggerTime', blank=True, null=True)
    ballsidemembers = models.IntegerField(db_column='bAllSideMembers', blank=True, null=True)
    ballsimultaneously = models.IntegerField(db_column='bAllSimultaneously', blank=True, null=True)
    biscoopcheckpoint = models.IntegerField(db_column='bIsCoopCheckpoint', blank=True, null=True)
    bvehiclerequired = models.IntegerField(db_column='bVehicleRequired', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationsRendezvous'


class Taskoperationsvandalism(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    nhealthpool = models.IntegerField(db_column='nHealthPool', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationsVandalism'


class Taskoperationsvehiclelooting(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    fcsaduration = models.FloatField(db_column='fCSADuration', blank=True, null=True)
    bisvehicledeliverable = models.IntegerField(db_column='bIsVehicleDeliverable', blank=True, null=True)
    bvehiclelocked = models.IntegerField(db_column='bVehicleLocked', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationsVehicleLooting'


class Taskoperationsvehicletheft(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation', blank=True, null=True)
    fcsaduration = models.FloatField(db_column='fCSADuration', blank=True, null=True)
    npointlessextrapadding = models.IntegerField(db_column='nPointlessExtraPadding', blank=True, null=True)
    bisvehicledeliverable = models.IntegerField(db_column='bIsVehicleDeliverable', blank=True, null=True)
    bvehiclelocked = models.IntegerField(db_column='bVehicleLocked', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskOperationsVehicleTheft'


class Tasktargetallocations(models.Model):
    id = models.IntegerField(primary_key=True)
    elocationconstraint = models.IntegerField(db_column='eLocationConstraint', blank=True, null=True)
    emissiontemplate = models.IntegerField(db_column='eMissionTemplate', blank=True, null=True)
    etasktargetallocation = models.IntegerField(db_column='eTaskTargetAllocation', blank=True, null=True)
    etasktargettype = models.IntegerField(db_column='eTaskTargetType', blank=True, null=True)
    etheme_0 = models.IntegerField(db_column='eTheme_0', blank=True, null=True)
    etheme_1 = models.IntegerField(db_column='eTheme_1', blank=True, null=True)
    etheme_2 = models.IntegerField(db_column='eTheme_2', blank=True, null=True)
    etheme_3 = models.IntegerField(db_column='eTheme_3', blank=True, null=True)
    evehiclecategory = models.IntegerField(db_column='eVehicleCategory', blank=True, null=True)
    flocationdistancemax = models.FloatField(db_column='fLocationDistanceMax', blank=True, null=True)
    flocationdistancemin = models.FloatField(db_column='fLocationDistanceMin', blank=True, null=True)
    nmaxtargetsperblock = models.IntegerField(db_column='nMaxTargetsPerBlock', blank=True, null=True)
    ntargetcount = models.IntegerField(db_column='nTargetCount', blank=True, null=True)
    etasktargetspecificationmethod = models.IntegerField(db_column='eTaskTargetSpecificationMethod', blank=True, null=True)
    ballowdifferentblock = models.IntegerField(db_column='bAllowDifferentBlock', blank=True, null=True)
    ballowsameblock = models.IntegerField(db_column='bAllowSameBlock', blank=True, null=True)
    buniqueblock = models.IntegerField(db_column='bUniqueBlock', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskTargetAllocations'


class Tasktargetcheckpoints(models.Model):
    id = models.IntegerField(primary_key=True)
    etasktargettype = models.IntegerField(db_column='eTaskTargetType', blank=True, null=True)
    nmaxplayerspaces = models.IntegerField(db_column='nMaxPlayerSpaces', blank=True, null=True)
    nmaxvehiclespaces = models.IntegerField(db_column='nMaxVehicleSpaces', blank=True, null=True)
    ballowdropoffs = models.IntegerField(db_column='bAllowDropOffs', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskTargetCheckpoints'


class Tasktargetclasses(models.Model):
    id = models.IntegerField(primary_key=True)
    etasktargetclass = models.IntegerField(db_column='eTaskTargetClass', blank=True, null=True)
    bcanbeusedindirectedmissions = models.IntegerField(db_column='bCanBeUsedInDirectedMissions', blank=True, null=True)
    blivingcity = models.IntegerField(db_column='bLivingCity', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskTargetClasses'


class Tasktargetgraffiti(models.Model):
    id = models.IntegerField(primary_key=True)
    etasktargettype = models.IntegerField(db_column='eTaskTargetType', blank=True, null=True)
    ndummy = models.IntegerField(db_column='nDummy', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskTargetGraffiti'


class Tasktargetnpcs(models.Model):
    id = models.IntegerField(primary_key=True)
    enpctype = models.IntegerField(db_column='eNPCType', blank=True, null=True)
    etasktargettype = models.IntegerField(db_column='eTaskTargetType', blank=True, null=True)
    ntemplctype = models.IntegerField(db_column='nTempLCType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskTargetNPCs'


class Tasktargetprops(models.Model):
    id = models.IntegerField(primary_key=True)
    spropassetname = models.TextField(db_column='sPropAssetName', blank=True, null=True)
    epropcategory = models.IntegerField(db_column='ePropCategory', blank=True, null=True)
    etasktargettype = models.IntegerField(db_column='eTaskTargetType', blank=True, null=True)
    farsondamagedelayseconds = models.FloatField(db_column='fArsonDamageDelaySeconds', blank=True, null=True)
    barson = models.IntegerField(db_column='bArson', blank=True, null=True)
    bbombdisposal = models.IntegerField(db_column='bBombDisposal', blank=True, null=True)
    bbombing = models.IntegerField(db_column='bBombing', blank=True, null=True)
    bburglary = models.IntegerField(db_column='bBurglary', blank=True, null=True)
    bbust = models.IntegerField(db_column='bBust', blank=True, null=True)
    bcsi = models.IntegerField(db_column='bCSI', blank=True, null=True)
    bforcedentry = models.IntegerField(db_column='bForcedEntry', blank=True, null=True)
    bhacking = models.IntegerField(db_column='bHacking', blank=True, null=True)
    bisbuildingfeature = models.IntegerField(db_column='bIsBuildingFeature', blank=True, null=True)
    bramraid = models.IntegerField(db_column='bRamRaid', blank=True, null=True)
    bsabotage = models.IntegerField(db_column='bSabotage', blank=True, null=True)
    bvandalism = models.IntegerField(db_column='bVandalism', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskTargetProps'


class Tasktargettypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    egameplayobject = models.IntegerField(db_column='eGameplayObject', blank=True, null=True)
    ehudmarkeroffsetoverride = models.IntegerField(db_column='eHUDMarkerOffsetOverride', blank=True, null=True)
    eopenworldtargetactivity = models.IntegerField(db_column='eOpenWorldTargetActivity', blank=True, null=True)
    eowaitemspawnrule = models.IntegerField(db_column='eOWAItemSpawnRule', blank=True, null=True)
    etasktargettype = models.IntegerField(db_column='eTaskTargetType', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    etasktargetclass = models.IntegerField(db_column='eTaskTargetClass', blank=True, null=True)
    etimeofdayavailability = models.IntegerField(db_column='eTimeOfDayAvailability', blank=True, null=True)
    ballowsimultaneousallocations = models.IntegerField(db_column='bAllowSimultaneousAllocations', blank=True, null=True)
    bopenworldonly = models.IntegerField(db_column='bOpenWorldOnly', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskTargetTypes'


class Themeitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sresource = models.TextField(db_column='sResource', blank=True, null=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ThemeItemTypes'


class Threatlevels(models.Model):
    id = models.IntegerField(primary_key=True)
    salloweddistrictthreats = models.TextField(db_column='sAllowedDistrictThreats', blank=True, null=True)
    sdisplayedname = models.TextField(db_column='sDisplayedName', blank=True, null=True)
    ehudtextureicon = models.IntegerField(db_column='eHUDTextureIcon', blank=True, null=True)
    ethreatlevel = models.IntegerField(db_column='eThreatLevel', blank=True, null=True)
    fmedianthreat = models.FloatField(db_column='fMedianThreat', blank=True, null=True)
    fthreshold = models.FloatField(db_column='fThreshold', blank=True, null=True)
    nratingtexturearrayindex = models.IntegerField(db_column='nRatingTextureArrayIndex', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ThreatLevels'


class Timeofdayavailabilities(models.Model):
    id = models.IntegerField(primary_key=True)
    etimeofdayavailability = models.IntegerField(db_column='eTimeOfDayAvailability', blank=True, null=True)
    bafternoon = models.IntegerField(db_column='bAfternoon', blank=True, null=True)
    bevening = models.IntegerField(db_column='bEvening', blank=True, null=True)
    bmorning = models.IntegerField(db_column='bMorning', blank=True, null=True)
    bnight = models.IntegerField(db_column='bNight', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TimeOfDayAvailabilities'


class Timeofdayperiod(models.Model):
    id = models.IntegerField(primary_key=True)
    nendtimehours = models.IntegerField(db_column='nEndTimeHours', blank=True, null=True)
    nendtimemins = models.IntegerField(db_column='nEndTimeMins', blank=True, null=True)
    nstarttimehours = models.IntegerField(db_column='nStartTimeHours', blank=True, null=True)
    nstarttimemins = models.IntegerField(db_column='nStartTimeMins', blank=True, null=True)
    etimeofdayperiod = models.IntegerField(db_column='eTimeofDayPeriod', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TimeofDayPeriod'


class Titleunlockitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    bfemale = models.IntegerField(db_column='bFemale', blank=True, null=True)
    bhideuntilunlocked = models.IntegerField(db_column='bHideUntilUnlocked', blank=True, null=True)
    bmale = models.IntegerField(db_column='bMale', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TitleUnlockItemTypes'


class Trackedactivities(models.Model):
    id = models.IntegerField(primary_key=True)
    etrackedactivity = models.IntegerField(db_column='eTrackedActivity', blank=True, null=True)
    eunit = models.IntegerField(db_column='eUnit', blank=True, null=True)
    nmaxincrementperzone = models.IntegerField(db_column='nMaxIncrementPerZone', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)
    epersistencetype = models.IntegerField(db_column='ePersistenceType', blank=True, null=True)
    bupdateduringwitnessingmission = models.IntegerField(db_column='bUpdateDuringWitnessingMission', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TrackedActivities'


class Trackedactivitiesderived(models.Model):
    id = models.IntegerField(primary_key=True)
    emaster_0 = models.IntegerField(db_column='eMaster_0', blank=True, null=True)
    emaster_1 = models.IntegerField(db_column='eMaster_1', blank=True, null=True)
    emaster_2 = models.IntegerField(db_column='eMaster_2', blank=True, null=True)
    emaster_3 = models.IntegerField(db_column='eMaster_3', blank=True, null=True)
    emaster_4 = models.IntegerField(db_column='eMaster_4', blank=True, null=True)
    emaster_5 = models.IntegerField(db_column='eMaster_5', blank=True, null=True)
    emaster_6 = models.IntegerField(db_column='eMaster_6', blank=True, null=True)
    emaster_7 = models.IntegerField(db_column='eMaster_7', blank=True, null=True)
    emaster_8 = models.IntegerField(db_column='eMaster_8', blank=True, null=True)
    emaster_9 = models.IntegerField(db_column='eMaster_9', blank=True, null=True)
    etrackedactivity = models.IntegerField(db_column='eTrackedActivity', blank=True, null=True)
    eoperation = models.IntegerField(db_column='eOperation', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TrackedActivitiesDerived'


class Trackedactivitiesfixed(models.Model):
    id = models.IntegerField(primary_key=True)
    etrackedactivity = models.IntegerField(db_column='eTrackedActivity', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TrackedActivitiesFixed'


class Trackedactivityunits(models.Model):
    id = models.IntegerField(primary_key=True)
    sformatting = models.TextField(db_column='sFormatting', blank=True, null=True)
    etrackedactivityunit = models.IntegerField(db_column='eTrackedActivityUnit', blank=True, null=True)
    econversion = models.IntegerField(db_column='eConversion', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TrackedActivityUnits'


class Trafficlightdurations(models.Model):
    id = models.IntegerField(primary_key=True)
    edistrict = models.IntegerField(db_column='eDistrict', blank=True, null=True)
    etrafficlightduration = models.IntegerField(db_column='eTrafficLightDuration', blank=True, null=True)
    fped_fourlanemax = models.FloatField(db_column='fPed_FourLaneMax', blank=True, null=True)
    fped_fourlanemin = models.FloatField(db_column='fPed_FourLaneMin', blank=True, null=True)
    fped_onelanemax = models.FloatField(db_column='fPed_OneLaneMax', blank=True, null=True)
    fped_onelanemin = models.FloatField(db_column='fPed_OneLaneMin', blank=True, null=True)
    fped_threelanemax = models.FloatField(db_column='fPed_ThreeLaneMax', blank=True, null=True)
    fped_threelanemin = models.FloatField(db_column='fPed_ThreeLaneMin', blank=True, null=True)
    fped_twolanemax = models.FloatField(db_column='fPed_TwoLaneMax', blank=True, null=True)
    fped_twolanemin = models.FloatField(db_column='fPed_TwoLaneMin', blank=True, null=True)
    fvehicle_fourlanemax = models.FloatField(db_column='fVehicle_FourLaneMax', blank=True, null=True)
    fvehicle_fourlanemin = models.FloatField(db_column='fVehicle_FourLaneMin', blank=True, null=True)
    fvehicle_onelanemax = models.FloatField(db_column='fVehicle_OneLaneMax', blank=True, null=True)
    fvehicle_onelanemin = models.FloatField(db_column='fVehicle_OneLaneMin', blank=True, null=True)
    fvehicle_threelanemax = models.FloatField(db_column='fVehicle_ThreeLaneMax', blank=True, null=True)
    fvehicle_threelanemin = models.FloatField(db_column='fVehicle_ThreeLaneMin', blank=True, null=True)
    fvehicle_twolanemax = models.FloatField(db_column='fVehicle_TwoLaneMax', blank=True, null=True)
    fvehicle_twolanemin = models.FloatField(db_column='fVehicle_TwoLaneMin', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TrafficLightDurations'


class Tutorialcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    srewardmailbody = models.TextField(db_column='sRewardMailBody', blank=True, null=True)
    srewardmailsubject = models.TextField(db_column='sRewardMailSubject', blank=True, null=True)
    erewardpackage = models.IntegerField(db_column='eRewardPackage', blank=True, null=True)
    etutorial = models.IntegerField(db_column='eTutorial', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TutorialCategories'


class Tutorialevents(models.Model):
    id = models.IntegerField(primary_key=True)
    shudtext = models.TextField(db_column='sHUDText', blank=True, null=True)
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)
    ehudmarker = models.IntegerField(db_column='eHUDMarker', blank=True, null=True)
    etutorial = models.IntegerField(db_column='eTutorial', blank=True, null=True)
    euihighlight = models.IntegerField(db_column='eUIHighlight', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TutorialEvents'


class Tutorials(models.Model):
    id = models.IntegerField(primary_key=True)
    sbody = models.TextField(db_column='sBody', blank=True, null=True)
    sscreenshot = models.TextField(db_column='sScreenshot', blank=True, null=True)
    ssubtitle = models.TextField(db_column='sSubTitle', blank=True, null=True)
    stitle = models.TextField(db_column='sTitle', blank=True, null=True)
    eparent = models.IntegerField(db_column='eParent', blank=True, null=True)
    etutorial = models.IntegerField(db_column='eTutorial', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    efaction = models.IntegerField(db_column='eFaction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tutorials'


class Uiinteractionpoints(models.Model):
    id = models.IntegerField(primary_key=True)
    sinfobrowsertext = models.TextField(db_column='sInfoBrowserText', blank=True, null=True)
    ehudmarker = models.IntegerField(db_column='eHUDMarker', blank=True, null=True)
    einfobrowsericon = models.IntegerField(db_column='eInfoBrowserIcon', blank=True, null=True)
    euiinteractionpoint = models.IntegerField(db_column='eUIInteractionPoint', blank=True, null=True)
    ecsa = models.IntegerField(db_column='eCSA', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UIInteractionPoints'


class Uimeshviewersetup(models.Model):
    id = models.IntegerField(primary_key=True)
    nuimeshviewersetup = models.TextField(db_column='nUIMeshViewerSetup', blank=True, null=True)
    fcamerafov = models.FloatField(db_column='fCameraFOV', blank=True, null=True)
    fcameraposx = models.FloatField(db_column='fCameraPosX', blank=True, null=True)
    fcameraposy = models.FloatField(db_column='fCameraPosY', blank=True, null=True)
    fcameraposz = models.FloatField(db_column='fCameraPosZ', blank=True, null=True)
    fmeshcentrex = models.FloatField(db_column='fMeshCentreX', blank=True, null=True)
    fmeshcentrey = models.FloatField(db_column='fMeshCentreY', blank=True, null=True)
    fmeshcentrez = models.FloatField(db_column='fMeshCentreZ', blank=True, null=True)
    fmeshorientationx = models.FloatField(db_column='fMeshOrientationX', blank=True, null=True)
    fmeshorientationy = models.FloatField(db_column='fMeshOrientationY', blank=True, null=True)
    fmeshorientationz = models.FloatField(db_column='fMeshOrientationZ', blank=True, null=True)
    fmeshscale = models.FloatField(db_column='fMeshScale', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UIMeshViewerSetup'


class Uuistyles(models.Model):
    id = models.IntegerField(primary_key=True)
    sname = models.TextField(db_column='sName', blank=True, null=True)
    euistyle = models.IntegerField(db_column='eUIStyle', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UUIStyles'


class Unlockiteminfracategories(models.Model):
    id = models.IntegerField(primary_key=True)
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)
    einventoryiteminfracategory = models.IntegerField(db_column='eInventoryItemInfraCategory', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UnlockItemInfraCategories'


class Unlockitemsubcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    egameplayevent = models.IntegerField(db_column='eGameplayEvent', blank=True, null=True)
    einventoryitemsubcategory = models.IntegerField(db_column='eInventoryItemSubCategory', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UnlockItemSubCategories'


class Unlockitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    eunlockitem = models.IntegerField(db_column='eUnlockItem', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UnlockItemTypes'


class Usabletokentypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    emodifieritem = models.IntegerField(db_column='eModifierItem', blank=True, null=True)
    ncharges = models.IntegerField(db_column='nCharges', blank=True, null=True)
    nmaxcharges = models.IntegerField(db_column='nMaxCharges', blank=True, null=True)
    nmaxstacks = models.IntegerField(db_column='nMaxStacks', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UsableTokenTypes'


class Vfxassociations(models.Model):
    id = models.IntegerField(primary_key=True)
    svfxprefabname = models.TextField(db_column='sVFXPrefabName', blank=True, null=True)
    svfxreplacedactor = models.TextField(db_column='sVFXReplacedActor', blank=True, null=True)
    evfxassociation = models.IntegerField(db_column='eVFXAssociation', blank=True, null=True)
    evfxtype = models.IntegerField(db_column='eVFXType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VFXAssociations'


class Vfxtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    evfxtype = models.IntegerField(db_column='eVFXType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VFXTypes'


class Vehicleaudiopart(models.Model):
    id = models.IntegerField(primary_key=True)
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleAudioPart'


class Vehicleaudiopartdefaults(models.Model):
    id = models.IntegerField(primary_key=True)
    sdamagetype = models.TextField(db_column='sDamageType', blank=True, null=True)
    sdooreventclosefront = models.TextField(db_column='sDoorEventCloseFront', blank=True, null=True)
    sdooreventcloserearback = models.TextField(db_column='sDoorEventCloseRearBack', blank=True, null=True)
    sdooreventcloserearside = models.TextField(db_column='sDoorEventCloseRearSide', blank=True, null=True)
    sdooreventopenfront = models.TextField(db_column='sDoorEventOpenFront', blank=True, null=True)
    sdooreventopenrearback = models.TextField(db_column='sDoorEventOpenRearBack', blank=True, null=True)
    sdooreventopenrearside = models.TextField(db_column='sDoorEventOpenRearSide', blank=True, null=True)
    slc_vehicletype = models.TextField(db_column='sLC_VehicleType', blank=True, null=True)
    ssuspensiontype = models.TextField(db_column='sSuspensionType', blank=True, null=True)
    edefaultamp = models.IntegerField(db_column='eDefaultAmp', blank=True, null=True)
    edefaultengine = models.IntegerField(db_column='eDefaultEngine', blank=True, null=True)
    edefaultexhaust = models.IntegerField(db_column='eDefaultExhaust', blank=True, null=True)
    edefaulthorn = models.IntegerField(db_column='eDefaultHorn', blank=True, null=True)
    edefaultsiren = models.IntegerField(db_column='eDefaultSiren', blank=True, null=True)
    edefaultspeaker = models.IntegerField(db_column='eDefaultSpeaker', blank=True, null=True)
    evehicleaudiopartdefaults = models.IntegerField(db_column='eVehicleAudioPartDefaults', blank=True, null=True)
    fmaxenclosedness = models.FloatField(db_column='fMaxEnclosedness', blank=True, null=True)
    fwheelforceeventthreshold = models.FloatField(db_column='fWheelForceEventThreshold', blank=True, null=True)
    fwheelforcemax = models.FloatField(db_column='fWheelForceMax', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleAudioPartDefaults'


class Vehiclecategories(models.Model):
    id = models.IntegerField(primary_key=True)
    evehiclecategory = models.IntegerField(db_column='eVehicleCategory', blank=True, null=True)
    fhairsquash = models.FloatField(db_column='fHairSquash', blank=True, null=True)
    fmaxheight = models.FloatField(db_column='fMaxHeight', blank=True, null=True)
    fmaxlength = models.FloatField(db_column='fMaxLength', blank=True, null=True)
    fmaxwidth = models.FloatField(db_column='fMaxWidth', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleCategories'


class Vehiclecategoryrestrictions(models.Model):
    id = models.IntegerField(primary_key=True)
    evehiclecategory = models.IntegerField(db_column='eVehicleCategory', blank=True, null=True)
    nnumconcurrentsetuptypes = models.IntegerField(db_column='nNumConcurrentSetupTypes', blank=True, null=True)
    nvehiclecategoryrestriction = models.IntegerField(db_column='nVehicleCategoryRestriction', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleCategoryRestrictions'


class Vehiclecolours(models.Model):
    id = models.IntegerField(primary_key=True)
    fprobability = models.FloatField(db_column='fProbability', blank=True, null=True)
    nbluecomponent = models.IntegerField(db_column='nBlueComponent', blank=True, null=True)
    ngreencomponent = models.IntegerField(db_column='nGreenComponent', blank=True, null=True)
    nredcomponent = models.IntegerField(db_column='nRedComponent', blank=True, null=True)
    evehiclecolour = models.IntegerField(db_column='eVehicleColour', blank=True, null=True)
    bismetallic = models.IntegerField(db_column='bIsMetallic', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleColours'


class Vehiclecomponentunlockitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    salternateresource = models.TextField(db_column='sAlternateResource', blank=True, null=True)
    sresource = models.TextField(db_column='sResource', blank=True, null=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    euicomponent = models.IntegerField(db_column='eUIComponent', blank=True, null=True)
    napplicationcost = models.IntegerField(db_column='nApplicationCost', blank=True, null=True)
    napplicationrating = models.IntegerField(db_column='nApplicationRating', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleComponentUnlockItemTypes'


class Vehiclecomponents(models.Model):
    id = models.IntegerField(primary_key=True)
    evehiclecomponent = models.IntegerField(db_column='eVehicleComponent', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleComponents'


class Vehiclecritical(models.Model):
    id = models.IntegerField(primary_key=True)
    ehudmessage = models.IntegerField(db_column='eHUDMessage', blank=True, null=True)
    evehiclecritical = models.IntegerField(db_column='eVehicleCritical', blank=True, null=True)
    fweight = models.FloatField(db_column='fWeight', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleCritical'


class Vehicledamagehandlingeffects(models.Model):
    id = models.IntegerField(primary_key=True)
    evehicledamagehandlingeffect = models.IntegerField(db_column='eVehicleDamageHandlingEffect', blank=True, null=True)
    fbrakeeffectiveness = models.FloatField(db_column='fBrakeEffectiveness', blank=True, null=True)
    fenginetorquescale = models.FloatField(db_column='fEngineTorqueScale', blank=True, null=True)
    ffrontlatgrip = models.FloatField(db_column='fFrontLatGrip', blank=True, null=True)
    ffrontlonggrip = models.FloatField(db_column='fFrontLongGrip', blank=True, null=True)
    fmaxspeedscale = models.FloatField(db_column='fMaxSpeedScale', blank=True, null=True)
    frearlatgrip = models.FloatField(db_column='fRearLatGrip', blank=True, null=True)
    frearlonggrip = models.FloatField(db_column='fRearLongGrip', blank=True, null=True)
    fsteeringspeed = models.FloatField(db_column='fSteeringSpeed', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleDamageHandlingEffects'


class Vehicledamagelevels(models.Model):
    id = models.IntegerField(primary_key=True)
    ehandlingeffect = models.IntegerField(db_column='eHandlingEffect', blank=True, null=True)
    evehiclecritical = models.IntegerField(db_column='eVehicleCritical', blank=True, null=True)
    evehicledamagelevel = models.IntegerField(db_column='eVehicleDamageLevel', blank=True, null=True)
    fhealththreshold = models.FloatField(db_column='fHealthThreshold', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleDamageLevels'


class Vehicledamagevfx(models.Model):
    id = models.IntegerField(primary_key=True)
    sdamagestatebegin = models.TextField(db_column='sDamageStateBegin', blank=True, null=True)
    sdamagestateend = models.TextField(db_column='sDamageStateEnd', blank=True, null=True)
    sexplosionaudio = models.TextField(db_column='sExplosionAudio', blank=True, null=True)
    sexplosionevent = models.TextField(db_column='sExplosionEvent', blank=True, null=True)
    evehicledamagevfx = models.IntegerField(db_column='eVehicleDamageVFX', blank=True, null=True)
    fhealththreshold = models.FloatField(db_column='fHealthThreshold', blank=True, null=True)
    nstatenumber = models.IntegerField(db_column='nStateNumber', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleDamageVFX'


class Vehicledistrict(models.Model):
    id = models.IntegerField(primary_key=True)
    sheightfield = models.TextField(db_column='sHeightfield', blank=True, null=True)
    fworldoffsetx = models.FloatField(db_column='fWorldOffsetX', blank=True, null=True)
    fworldoffsety = models.FloatField(db_column='fWorldOffsetY', blank=True, null=True)
    fworldoffsetz = models.FloatField(db_column='fWorldOffsetZ', blank=True, null=True)
    fworldtotexturescalexy = models.FloatField(db_column='fWorldToTextureScaleXY', blank=True, null=True)
    fworldtotexturescalez = models.FloatField(db_column='fWorldToTextureScaleZ', blank=True, null=True)
    evehicledistricts = models.IntegerField(db_column='eVehicleDistricts', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleDistrict'


class Vehicledooranimationsets(models.Model):
    id = models.IntegerField(primary_key=True)
    sclosedframe = models.TextField(db_column='sClosedFrame', blank=True, null=True)
    sclosefrominside = models.TextField(db_column='sCloseFromInside', blank=True, null=True)
    sclosefromoutside = models.TextField(db_column='sCloseFromOutside', blank=True, null=True)
    sclosegetin = models.TextField(db_column='sCloseGetIn', blank=True, null=True)
    sopenbailout = models.TextField(db_column='sOpenBailOut', blank=True, null=True)
    sopenframe = models.TextField(db_column='sOpenFrame', blank=True, null=True)
    sopenfromoutside = models.TextField(db_column='sOpenFromOutside', blank=True, null=True)
    sopengetout = models.TextField(db_column='sOpenGetOut', blank=True, null=True)
    sopenseatslideejectcriminal = models.TextField(db_column='sOpenSeatSlideEjectCriminal', blank=True, null=True)
    sopenseatslideejectenforcer = models.TextField(db_column='sOpenSeatSlideEjectEnforcer', blank=True, null=True)
    evehicledooranimationset = models.IntegerField(db_column='eVehicleDoorAnimationSet', blank=True, null=True)
    bdooropenwhileinside = models.IntegerField(db_column='bDoorOpenWhileInside', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleDoorAnimationSets'


class Vehicleevents(models.Model):
    id = models.IntegerField(primary_key=True)
    nignoreme = models.IntegerField(db_column='nIgnoreMe', blank=True, null=True)
    enpcevent = models.IntegerField(db_column='eNPCEvent', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleEvents'


class Vehiclegear(models.Model):
    id = models.IntegerField(primary_key=True)
    spackageimageref = models.TextField(db_column='sPackageImageRef', blank=True, null=True)
    evehiclegear = models.IntegerField(db_column='eVehicleGear', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleGear'


class Vehicleinteractionanimations(models.Model):
    id = models.IntegerField(primary_key=True)
    fblendintime = models.FloatField(db_column='fBlendInTime', blank=True, null=True)
    fblendouttime = models.FloatField(db_column='fBlendOutTime', blank=True, null=True)
    evehicleinteractionanimation = models.IntegerField(db_column='eVehicleInteractionAnimation', blank=True, null=True)
    bmirror = models.IntegerField(db_column='bMirror', blank=True, null=True)
    bpauseatend = models.IntegerField(db_column='bPauseAtEnd', blank=True, null=True)
    bscaleroot = models.IntegerField(db_column='bScaleRoot', blank=True, null=True)
    bstartatorigin = models.IntegerField(db_column='bStartAtOrigin', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleInteractionAnimations'


class Vehicleinteractionsequences(models.Model):
    id = models.IntegerField(primary_key=True)
    ssequencename = models.TextField(db_column='sSequenceName', blank=True, null=True)
    evehicleplayeranimationset = models.IntegerField(db_column='eVehiclePlayerAnimationSet', blank=True, null=True)
    evehicleinteractionanimation = models.IntegerField(db_column='eVehicleInteractionAnimation', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleInteractionSequences'


class Vehicleitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    sresource = models.TextField(db_column='sResource', blank=True, null=True)
    efnmod_0 = models.IntegerField(db_column='eFnMod_0', blank=True, null=True)
    efnmod_1 = models.IntegerField(db_column='eFnMod_1', blank=True, null=True)
    efnmod_2 = models.IntegerField(db_column='eFnMod_2', blank=True, null=True)
    efnmod_3 = models.IntegerField(db_column='eFnMod_3', blank=True, null=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    nreeditfee = models.IntegerField(db_column='nReeditFee', blank=True, null=True)
    evehicle = models.IntegerField(db_column='eVehicle', blank=True, null=True)
    bpreset = models.IntegerField(db_column='bPreset', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleItemTypes'


class Vehiclemenuentries(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplaypicture = models.TextField(db_column='sDisplayPicture', blank=True, null=True)
    sdisplaytext = models.TextField(db_column='sDisplayText', blank=True, null=True)
    smenulevel = models.TextField(db_column='sMenuLevel', blank=True, null=True)
    smenutag = models.TextField(db_column='sMenuTag', blank=True, null=True)
    soptionalscene = models.TextField(db_column='sOptionalScene', blank=True, null=True)
    ecameraangle = models.IntegerField(db_column='eCameraAngle', blank=True, null=True)
    evehiclemenuentry = models.IntegerField(db_column='eVehicleMenuEntry', blank=True, null=True)
    benabled = models.IntegerField(db_column='bEnabled', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleMenuEntries'


class Vehiclemodifieritemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleModifierItemTypes'


class Vehiclenpcinsideanimationsets(models.Model):
    id = models.IntegerField(primary_key=True)
    sejectinitialcriminal = models.TextField(db_column='sEjectInitialCriminal', blank=True, null=True)
    sejectinitialenforcer = models.TextField(db_column='sEjectInitialEnforcer', blank=True, null=True)
    sejectinitialfrompassengersidecriminal = models.TextField(db_column='sEjectInitialFromPassengerSideCriminal', blank=True, null=True)
    sejectinitialfrompassengersideenforcer = models.TextField(db_column='sEjectInitialFromPassengerSideEnforcer', blank=True, null=True)
    sejectlatercriminal = models.TextField(db_column='sEjectLaterCriminal', blank=True, null=True)
    sejectlaterenforcer = models.TextField(db_column='sEjectLaterEnforcer', blank=True, null=True)
    sejectlaterfrompassengersidecriminal = models.TextField(db_column='sEjectLaterFromPassengerSideCriminal', blank=True, null=True)
    sejectlaterfrompassengersideenforcer = models.TextField(db_column='sEjectLaterFromPassengerSideEnforcer', blank=True, null=True)
    evehiclenpcinsideanimationset = models.IntegerField(db_column='eVehicleNPCInsideAnimationSet', blank=True, null=True)
    fejectdistancedriversidecriminal = models.FloatField(db_column='fEjectDistanceDriverSideCriminal', blank=True, null=True)
    fejectdistancedriversideenforcer = models.FloatField(db_column='fEjectDistanceDriverSideEnforcer', blank=True, null=True)
    fejectdistancepassengersidecriminal = models.FloatField(db_column='fEjectDistancePassengerSideCriminal', blank=True, null=True)
    fejectdistancepassengersideenforcer = models.FloatField(db_column='fEjectDistancePassengerSideEnforcer', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleNPCInsideAnimationSets'


class Vehicleplayeranimationsets(models.Model):
    id = models.IntegerField(primary_key=True)
    sdrivesteer = models.TextField(db_column='sDriveSteer', blank=True, null=True)
    spassengeridle = models.TextField(db_column='sPassengerIdle', blank=True, null=True)
    eanimtreedecision = models.IntegerField(db_column='eAnimTreeDecision', blank=True, null=True)
    evehicleplayeranimationset = models.IntegerField(db_column='eVehiclePlayerAnimationSet', blank=True, null=True)
    fleaninduration = models.FloatField(db_column='fLeanInDuration', blank=True, null=True)
    fleanoutduration = models.FloatField(db_column='fLeanOutDuration', blank=True, null=True)
    bmirroranimations = models.IntegerField(db_column='bMirrorAnimations', blank=True, null=True)
    breverseaim = models.IntegerField(db_column='bReverseAim', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehiclePlayerAnimationSets'


class Vehiclepositioninfo(models.Model):
    id = models.IntegerField(primary_key=True)
    evehicleanimationcategory = models.IntegerField(db_column='eVehicleAnimationCategory', blank=True, null=True)
    evehicledooranimationset = models.IntegerField(db_column='eVehicleDoorAnimationSet', blank=True, null=True)
    evehiclenpcinsideanimationset = models.IntegerField(db_column='eVehicleNPCInsideAnimationSet', blank=True, null=True)
    evehicleplayeranimationset = models.IntegerField(db_column='eVehiclePlayerAnimationSet', blank=True, null=True)
    nvcpangle = models.IntegerField(db_column='nVCPAngle', blank=True, null=True)
    nvcpdirection = models.IntegerField(db_column='nVCPDirection', blank=True, null=True)
    evehiclepositionindex = models.IntegerField(db_column='eVehiclePositionIndex', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehiclePositionInfo'


class Vehicleseatcameras(models.Model):
    id = models.IntegerField(primary_key=True)
    eleanoutcamera = models.IntegerField(db_column='eLeanOutCamera', blank=True, null=True)
    esittingcamera = models.IntegerField(db_column='eSittingCamera', blank=True, null=True)
    evehiclepositionindex = models.IntegerField(db_column='eVehiclePositionIndex', blank=True, null=True)
    evehiclesetuptype = models.IntegerField(db_column='eVehicleSetupType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleSeatCameras'


class Vehiclesetuptypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    sgolemobilebase = models.TextField(db_column='sGolemobileBase', blank=True, null=True)
    sphysicsasset = models.TextField(db_column='sPhysicsAsset', blank=True, null=True)
    sshareddataobject = models.TextField(db_column='sSharedDataObject', blank=True, null=True)
    svehiclename = models.TextField(db_column='sVehicleName', blank=True, null=True)
    svehiclesetupasset = models.TextField(db_column='sVehicleSetupAsset', blank=True, null=True)
    svfxprefab = models.TextField(db_column='sVFXPrefab', blank=True, null=True)
    eaudiotype = models.IntegerField(db_column='eAudioType', blank=True, null=True)
    eexplosiontype = models.IntegerField(db_column='eExplosionType', blank=True, null=True)
    egameplayobject = models.IntegerField(db_column='eGameplayObject', blank=True, null=True)
    epedestriandriver = models.IntegerField(db_column='ePedestrianDriver', blank=True, null=True)
    euimeshviewersetup = models.IntegerField(db_column='eUIMeshViewerSetup', blank=True, null=True)
    evehicleanimationcategory = models.IntegerField(db_column='eVehicleAnimationCategory', blank=True, null=True)
    evehiclecategory = models.IntegerField(db_column='eVehicleCategory', blank=True, null=True)
    f0mssteerangle = models.FloatField(db_column='f0msSteerAngle', blank=True, null=True)
    f12mssteerangle = models.FloatField(db_column='f12msSteerAngle', blank=True, null=True)
    f22mssteerangle = models.FloatField(db_column='f22msSteerAngle', blank=True, null=True)
    f2500rpmtorque = models.FloatField(db_column='f2500RpmTorque', blank=True, null=True)
    f2ndgearspeed = models.FloatField(db_column='f2ndGearSpeed', blank=True, null=True)
    f3rdgearspeed = models.FloatField(db_column='f3rdGearSpeed', blank=True, null=True)
    f4500rpmtorque = models.FloatField(db_column='f4500RpmTorque', blank=True, null=True)
    f4thgearspeed = models.FloatField(db_column='f4thGearSpeed', blank=True, null=True)
    f500rpmtorque = models.FloatField(db_column='f500RpmTorque', blank=True, null=True)
    f5thgearspeed = models.FloatField(db_column='f5thGearSpeed', blank=True, null=True)
    f7000rpmtorque = models.FloatField(db_column='f7000RpmTorque', blank=True, null=True)
    fblobshadowscale_0 = models.FloatField(db_column='fBlobShadowScale_0', blank=True, null=True)
    fblobshadowscale_1 = models.FloatField(db_column='fBlobShadowScale_1', blank=True, null=True)
    fblobshadowscale_2 = models.FloatField(db_column='fBlobShadowScale_2', blank=True, null=True)
    fblobshadowtranslate_0 = models.FloatField(db_column='fBlobShadowTranslate_0', blank=True, null=True)
    fblobshadowtranslate_1 = models.FloatField(db_column='fBlobShadowTranslate_1', blank=True, null=True)
    fblobshadowtranslate_2 = models.FloatField(db_column='fBlobShadowTranslate_2', blank=True, null=True)
    fbreakincsaduration = models.FloatField(db_column='fBreakInCSADuration', blank=True, null=True)
    fcambasezfar = models.FloatField(db_column='fCamBaseZFar', blank=True, null=True)
    fcambaseznear = models.FloatField(db_column='fCamBaseZNear', blank=True, null=True)
    fcargoheightreductionfactor = models.FloatField(db_column='fCargoHeightReductionFactor', blank=True, null=True)
    fcargotorquereductionfactor = models.FloatField(db_column='fCargoTorqueReductionFactor', blank=True, null=True)
    fchassistorquefactor = models.FloatField(db_column='fChassisTorqueFactor', blank=True, null=True)
    fcollisiondamage = models.FloatField(db_column='fCollisionDamage', blank=True, null=True)
    fcomoffsetx = models.FloatField(db_column='fCOMOffsetX', blank=True, null=True)
    fcomoffsetz = models.FloatField(db_column='fCOMOffsetZ', blank=True, null=True)
    fdrivercamfar = models.FloatField(db_column='fDriverCamFar', blank=True, null=True)
    fdrivercamnear = models.FloatField(db_column='fDriverCamNear', blank=True, null=True)
    fenginebrakingfactor = models.FloatField(db_column='fEngineBrakingFactor', blank=True, null=True)
    ffinaldriveratio = models.FloatField(db_column='fFinalDriveRatio', blank=True, null=True)
    ffrontlatfactor = models.FloatField(db_column='fFrontLatFactor', blank=True, null=True)
    ffrontlongfactor = models.FloatField(db_column='fFrontLongFactor', blank=True, null=True)
    ffrontsuspensionspeed = models.FloatField(db_column='fFrontSuspensionSpeed', blank=True, null=True)
    ffrontsuspensiontravel = models.FloatField(db_column='fFrontSuspensionTravel', blank=True, null=True)
    ffrontwheelboneoffset_0 = models.FloatField(db_column='fFrontWheelBoneOffset_0', blank=True, null=True)
    ffrontwheelboneoffset_1 = models.FloatField(db_column='fFrontWheelBoneOffset_1', blank=True, null=True)
    ffrontwheelboneoffset_2 = models.FloatField(db_column='fFrontWheelBoneOffset_2', blank=True, null=True)
    ffrontwheelmeshoffset_0 = models.FloatField(db_column='fFrontWheelMeshOffset_0', blank=True, null=True)
    ffrontwheelmeshoffset_1 = models.FloatField(db_column='fFrontWheelMeshOffset_1', blank=True, null=True)
    ffrontwheelmeshoffset_2 = models.FloatField(db_column='fFrontWheelMeshOffset_2', blank=True, null=True)
    ffrontwheelradius = models.FloatField(db_column='fFrontWheelRadius', blank=True, null=True)
    fgearratios_0 = models.FloatField(db_column='fGearRatios_0', blank=True, null=True)
    fgearratios_1 = models.FloatField(db_column='fGearRatios_1', blank=True, null=True)
    fgearratios_2 = models.FloatField(db_column='fGearRatios_2', blank=True, null=True)
    fgearratios_3 = models.FloatField(db_column='fGearRatios_3', blank=True, null=True)
    fgearratios_4 = models.FloatField(db_column='fGearRatios_4', blank=True, null=True)
    fgearratios_5 = models.FloatField(db_column='fGearRatios_5', blank=True, null=True)
    fidlerpm = models.FloatField(db_column='fIdleRPM', blank=True, null=True)
    flsdfactor = models.FloatField(db_column='fLSDFactor', blank=True, null=True)
    fmaxbraketorque = models.FloatField(db_column='fMaxBrakeTorque', blank=True, null=True)
    fmaxcargoheightreduction = models.FloatField(db_column='fMaxCargoHeightReduction', blank=True, null=True)
    fmaxcargotorquereduction = models.FloatField(db_column='fMaxCargoTorqueReduction', blank=True, null=True)
    fmaxdirt = models.FloatField(db_column='fMaxDirt', blank=True, null=True)
    fmaxdust = models.FloatField(db_column='fMaxDust', blank=True, null=True)
    fmaxrepairtimesecs = models.FloatField(db_column='fMaxRepairTimeSecs', blank=True, null=True)
    fmaxreversespeed = models.FloatField(db_column='fMaxReverseSpeed', blank=True, null=True)
    fmaxspeed = models.FloatField(db_column='fMaxSpeed', blank=True, null=True)
    fmindirt = models.FloatField(db_column='fMinDirt', blank=True, null=True)
    fmindust = models.FloatField(db_column='fMinDust', blank=True, null=True)
    fpercentdirty = models.FloatField(db_column='fPercentDirty', blank=True, null=True)
    fpercentperfectlyclean = models.FloatField(db_column='fPercentPerfectlyClean', blank=True, null=True)
    framraiddamagemultiplier = models.FloatField(db_column='fRamraidDamageMultiplier', blank=True, null=True)
    frearhandbrakelat = models.FloatField(db_column='fRearHandbrakeLat', blank=True, null=True)
    frearhandbrakelong = models.FloatField(db_column='fRearHandbrakeLong', blank=True, null=True)
    frearlatfactor = models.FloatField(db_column='fRearLatFactor', blank=True, null=True)
    frearlongfactor = models.FloatField(db_column='fRearLongFactor', blank=True, null=True)
    frearsuspensionspeed = models.FloatField(db_column='fRearSuspensionSpeed', blank=True, null=True)
    frearsuspensiontravel = models.FloatField(db_column='fRearSuspensionTravel', blank=True, null=True)
    frearwheelboneoffset_0 = models.FloatField(db_column='fRearWheelBoneOffset_0', blank=True, null=True)
    frearwheelboneoffset_1 = models.FloatField(db_column='fRearWheelBoneOffset_1', blank=True, null=True)
    frearwheelboneoffset_2 = models.FloatField(db_column='fRearWheelBoneOffset_2', blank=True, null=True)
    frearwheelmeshoffset_0 = models.FloatField(db_column='fRearWheelMeshOffset_0', blank=True, null=True)
    frearwheelmeshoffset_1 = models.FloatField(db_column='fRearWheelMeshOffset_1', blank=True, null=True)
    frearwheelmeshoffset_2 = models.FloatField(db_column='fRearWheelMeshOffset_2', blank=True, null=True)
    frearwheelradius = models.FloatField(db_column='fRearWheelRadius', blank=True, null=True)
    fredlinerpm = models.FloatField(db_column='fRedlineRPM', blank=True, null=True)
    freversethrottle = models.FloatField(db_column='fReverseThrottle', blank=True, null=True)
    fsteeraccel = models.FloatField(db_column='fSteerAccel', blank=True, null=True)
    fsteerspeed = models.FloatField(db_column='fSteerSpeed', blank=True, null=True)
    fsuspensiondamping = models.FloatField(db_column='fSuspensionDamping', blank=True, null=True)
    fsuspensionstiffness = models.FloatField(db_column='fSuspensionStiffness', blank=True, null=True)
    fwheellatasymptoteslip = models.FloatField(db_column='fWheelLatAsymptoteSlip', blank=True, null=True)
    fwheellatasymptotevalue = models.FloatField(db_column='fWheelLatAsymptoteValue', blank=True, null=True)
    fwheellatextremumslip = models.FloatField(db_column='fWheelLatExtremumSlip', blank=True, null=True)
    fwheellatextremumvalue = models.FloatField(db_column='fWheelLatExtremumValue', blank=True, null=True)
    fwheellongasymptoteslip = models.FloatField(db_column='fWheelLongAsymptoteSlip', blank=True, null=True)
    fwheellongasymptotevalue = models.FloatField(db_column='fWheelLongAsymptoteValue', blank=True, null=True)
    fwheellongextremumslip = models.FloatField(db_column='fWheelLongExtremumSlip', blank=True, null=True)
    fwheellongextremumvalue = models.FloatField(db_column='fWheelLongExtremumValue', blank=True, null=True)
    ncabincargopipcapacity = models.IntegerField(db_column='nCabinCargoPipCapacity', blank=True, null=True)
    ncamerapitchmax = models.IntegerField(db_column='nCameraPitchMax', blank=True, null=True)
    ncamerapitchmin = models.IntegerField(db_column='nCameraPitchMin', blank=True, null=True)
    ncargoareaseatpositions = models.IntegerField(db_column='nCargoAreaSeatPositions', blank=True, null=True)
    ninitialcampitch = models.IntegerField(db_column='nInitialCamPitch', blank=True, null=True)
    nmaincargopipcapacity = models.IntegerField(db_column='nMainCargoPipCapacity', blank=True, null=True)
    nmaxhealth = models.IntegerField(db_column='nMaxHealth', blank=True, null=True)
    nmaxrepaircost = models.IntegerField(db_column='nMaxRepairCost', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    nspawncost = models.IntegerField(db_column='nSpawnCost', blank=True, null=True)
    edrivetype = models.IntegerField(db_column='eDriveType', blank=True, null=True)
    etempassets = models.IntegerField(db_column='eTempAssets', blank=True, null=True)
    euicategory = models.IntegerField(db_column='eUICategory', blank=True, null=True)
    evehiclemodelclass = models.IntegerField(db_column='eVehicleModelClass', blank=True, null=True)
    evehiclesetuptype = models.IntegerField(db_column='eVehicleSetupType', blank=True, null=True)
    bhasalarm = models.IntegerField(db_column='bHasAlarm', blank=True, null=True)
    bhasrearseats = models.IntegerField(db_column='bHasRearSeats', blank=True, null=True)
    bhastaillights = models.IntegerField(db_column='bHasTailLights', blank=True, null=True)
    bisplayeronlyvehicle = models.IntegerField(db_column='bIsPlayerOnlyVehicle', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleSetupTypes'


class Vehicletempsetups(models.Model):
    id = models.IntegerField(primary_key=True)
    stempsetupinfo = models.TextField(db_column='sTempSetupInfo', blank=True, null=True)
    evehicletempsetup = models.IntegerField(db_column='eVehicleTempSetup', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleTempSetups'


class Vehicleuicameraangles(models.Model):
    id = models.IntegerField(primary_key=True)
    evehicleuicameraangle = models.IntegerField(db_column='eVehicleUICameraAngle', blank=True, null=True)
    factorrotation = models.FloatField(db_column='fActorRotation', blank=True, null=True)
    fcameraposition = models.FloatField(db_column='fCameraPosition', blank=True, null=True)
    ffov = models.FloatField(db_column='fFOV', blank=True, null=True)
    bopendoors = models.IntegerField(db_column='bOpenDoors', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleUICameraAngles'


class Vehicleuicategory(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    evehicleuicategory = models.IntegerField(db_column='eVehicleUICategory', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleUICategory'


class Vehicleuicomponentcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    evehicleuicomponentcategory = models.IntegerField(db_column='eVehicleUIComponentCategory', blank=True, null=True)
    nsortingpriority = models.IntegerField(db_column='nSortingPriority', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleUIComponentCategories'


class Vehicleuicomponentinfos(models.Model):
    id = models.IntegerField(primary_key=True)
    ecameraangle = models.IntegerField(db_column='eCameraAngle', blank=True, null=True)
    ecategory = models.IntegerField(db_column='eCategory', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleUIComponentInfos'


class Vehicleuisetups(models.Model):
    id = models.IntegerField(primary_key=True)
    facceleration = models.FloatField(db_column='fAcceleration', blank=True, null=True)
    fcollisiondamage = models.FloatField(db_column='fCollisionDamage', blank=True, null=True)
    fhandling = models.FloatField(db_column='fHandling', blank=True, null=True)
    fhealth = models.FloatField(db_column='fHealth', blank=True, null=True)
    fsuspensionoffsethack = models.FloatField(db_column='fSuspensionOffsetHack', blank=True, null=True)
    ftopspeed = models.FloatField(db_column='fTopSpeed', blank=True, null=True)
    evehiclesetuptype = models.IntegerField(db_column='eVehicleSetupType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleUISetups'


class Videoreplayuientries(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    sdisplayname = models.TextField(db_column='sDisplayName', blank=True, null=True)
    svideofilename = models.TextField(db_column='sVideoFileName', blank=True, null=True)
    evideoreplayuientry = models.IntegerField(db_column='eVideoReplayUIEntry', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VideoReplayUIEntries'


class Vignettetypes(models.Model):
    id = models.IntegerField(primary_key=True)
    spackage = models.TextField(db_column='sPackage', blank=True, null=True)
    evignettedescriptor = models.IntegerField(db_column='eVignetteDescriptor', blank=True, null=True)
    fmaxcanceldistancefromvnode = models.FloatField(db_column='fMaxCancelDistanceFromVNode', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VignetteTypes'


class Wardrobemenuentries(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayimage = models.TextField(db_column='sDisplayImage', blank=True, null=True)
    sdisplaytext = models.TextField(db_column='sDisplayText', blank=True, null=True)
    smenulevel = models.TextField(db_column='sMenuLevel', blank=True, null=True)
    smenutag = models.TextField(db_column='sMenuTag', blank=True, null=True)
    smouseovertext = models.TextField(db_column='sMouseOverText', blank=True, null=True)
    soptionalscene = models.TextField(db_column='sOptionalScene', blank=True, null=True)
    ewardrobemenuentry = models.IntegerField(db_column='eWardrobeMenuEntry', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WardrobeMenuEntries'


class Warningpromptgroups(models.Model):
    id = models.IntegerField(primary_key=True)
    swarningpromptgroupname = models.TextField(db_column='sWarningPromptGroupName', blank=True, null=True)
    ewarningpromptgroup = models.IntegerField(db_column='eWarningPromptGroup', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WarningPromptGroups'


class Weaponattachmentvisuals(models.Model):
    id = models.IntegerField(primary_key=True)
    simpactvfx = models.TextField(db_column='sImpactVFX', blank=True, null=True)
    smuzzleflashvfx = models.TextField(db_column='sMuzzleFlashVFX', blank=True, null=True)
    snontracershotvfx = models.TextField(db_column='sNonTracerShotVFX', blank=True, null=True)
    stracervfx = models.TextField(db_column='sTracerVFX', blank=True, null=True)
    swindupaudiotype = models.TextField(db_column='sWindupAudioType', blank=True, null=True)
    eitemattachmentvisual = models.IntegerField(db_column='eItemAttachmentVisual', blank=True, null=True)
    eimpactclass = models.IntegerField(db_column='eImpactClass', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WeaponAttachmentVisuals'


class Weaponclasses(models.Model):
    id = models.IntegerField(primary_key=True)
    sunrealclassname = models.TextField(db_column='sUnrealClassName', blank=True, null=True)
    eweaponclass = models.IntegerField(db_column='eWeaponClass', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WeaponClasses'


class Weaponcurves(models.Model):
    id = models.IntegerField(primary_key=True)
    saccuracyrecovery = models.TextField(db_column='sAccuracyRecovery', blank=True, null=True)
    sburstshots = models.TextField(db_column='sBurstShots', blank=True, null=True)
    seffectiverange = models.TextField(db_column='sEffectiveRange', blank=True, null=True)
    spershotmodifier = models.TextField(db_column='sPerShotModifier', blank=True, null=True)
    spingdistance = models.TextField(db_column='sPingDistance', blank=True, null=True)
    spitch = models.TextField(db_column='sPitch', blank=True, null=True)
    sradiusattenmetres = models.TextField(db_column='sRadiusAtTenMetres', blank=True, null=True)
    srecoverypersecond = models.TextField(db_column='sRecoveryPerSecond', blank=True, null=True)
    sreloadtime = models.TextField(db_column='sReloadTime', blank=True, null=True)
    syawnegative = models.TextField(db_column='sYawNegative', blank=True, null=True)
    syawpositive = models.TextField(db_column='sYawPositive', blank=True, null=True)
    eweaponcurve = models.IntegerField(db_column='eWeaponCurve', blank=True, null=True)
    fburstshotsinc = models.FloatField(db_column='fBurstShotsInc', blank=True, null=True)
    fgeneralrecoverydelay = models.FloatField(db_column='fGeneralRecoveryDelay', blank=True, null=True)
    fgeneralrecoveryscale = models.FloatField(db_column='fGeneralRecoveryScale', blank=True, null=True)
    fpershotmodifierinc = models.FloatField(db_column='fPerShotModifierInc', blank=True, null=True)
    fpingdistanceinc = models.FloatField(db_column='fPingDistanceInc', blank=True, null=True)
    fpitchinc = models.FloatField(db_column='fPitchInc', blank=True, null=True)
    fradiusattenmetresinc = models.FloatField(db_column='fRadiusAtTenMetresInc', blank=True, null=True)
    freloadtimeinc = models.FloatField(db_column='fReloadTimeInc', blank=True, null=True)
    fyawnegativeinc = models.FloatField(db_column='fYawNegativeInc', blank=True, null=True)
    fyawpositiveinc = models.FloatField(db_column='fYawPositiveInc', blank=True, null=True)
    bburstshotsrecover = models.IntegerField(db_column='bBurstShotsRecover', blank=True, null=True)
    bpershotmodifierrecover = models.IntegerField(db_column='bPerShotModifierRecover', blank=True, null=True)
    bpingdistancerecovers = models.IntegerField(db_column='bPingDistanceRecovers', blank=True, null=True)
    bpitchrecover = models.IntegerField(db_column='bPitchRecover', blank=True, null=True)
    bradiusattenmetresrecover = models.IntegerField(db_column='bRadiusAtTenMetresRecover', blank=True, null=True)
    byawnegativerecover = models.IntegerField(db_column='bYawNegativeRecover', blank=True, null=True)
    byawpositiverecover = models.IntegerField(db_column='bYawPositiveRecover', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WeaponCurves'


class Weaponitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription', blank=True, null=True)
    eactivitymessageicon = models.IntegerField(db_column='eActivityMessageIcon', blank=True, null=True)
    efnmod_0 = models.IntegerField(db_column='eFnMod_0', blank=True, null=True)
    efnmod_1 = models.IntegerField(db_column='eFnMod_1', blank=True, null=True)
    efnmod_2 = models.IntegerField(db_column='eFnMod_2', blank=True, null=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    eitemattachment = models.IntegerField(db_column='eItemAttachment', blank=True, null=True)
    eweapontypelink = models.IntegerField(db_column='eWeaponTypeLink', blank=True, null=True)
    bcausescontagion = models.IntegerField(db_column='bCausesContagion', blank=True, null=True)
    bisskinnable = models.IntegerField(db_column='bIsSkinnable', blank=True, null=True)
    bpreset = models.IntegerField(db_column='bPreset', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WeaponItemTypes'


class Weaponloadouts(models.Model):
    id = models.IntegerField(primary_key=True)
    eweaponloadout = models.IntegerField(db_column='eWeaponLoadout', blank=True, null=True)
    eweapontocreate_0 = models.IntegerField(db_column='eWeaponToCreate_0', blank=True, null=True)
    eweapontocreate_1 = models.IntegerField(db_column='eWeaponToCreate_1', blank=True, null=True)
    eweapontocreate_2 = models.IntegerField(db_column='eWeaponToCreate_2', blank=True, null=True)
    eweapontocreate_3 = models.IntegerField(db_column='eWeaponToCreate_3', blank=True, null=True)
    eweapontypetofind_0 = models.IntegerField(db_column='eWeaponTypeToFind_0', blank=True, null=True)
    eweapontypetofind_1 = models.IntegerField(db_column='eWeaponTypeToFind_1', blank=True, null=True)
    eweapontypetofind_2 = models.IntegerField(db_column='eWeaponTypeToFind_2', blank=True, null=True)
    eweapontypetofind_3 = models.IntegerField(db_column='eWeaponTypeToFind_3', blank=True, null=True)
    nequipslot = models.IntegerField(db_column='nEquipSlot', blank=True, null=True)
    eweaponoverridetype_0 = models.IntegerField(db_column='eWeaponOverrideType_0', blank=True, null=True)
    eweaponoverridetype_1 = models.IntegerField(db_column='eWeaponOverrideType_1', blank=True, null=True)
    eweaponoverridetype_2 = models.IntegerField(db_column='eWeaponOverrideType_2', blank=True, null=True)
    eweaponoverridetype_3 = models.IntegerField(db_column='eWeaponOverrideType_3', blank=True, null=True)
    ballowweaponpickup = models.IntegerField(db_column='bAllowWeaponPickup', blank=True, null=True)
    bgiftammo = models.IntegerField(db_column='bGiftAmmo', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WeaponLoadouts'


class Weaponmodifieritemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WeaponModifierItemTypes'


class Weaponprojectiles(models.Model):
    id = models.IntegerField(primary_key=True)
    sflightaudioevent = models.TextField(db_column='sFlightAudioEvent', blank=True, null=True)
    smesh = models.TextField(db_column='sMesh', blank=True, null=True)
    strailvfx = models.TextField(db_column='sTrailVFX', blank=True, null=True)
    eexplosion = models.IntegerField(db_column='eExplosion', blank=True, null=True)
    eweaponprojectile = models.IntegerField(db_column='eWeaponProjectile', blank=True, null=True)
    farmingtimer = models.FloatField(db_column='fArmingTimer', blank=True, null=True)
    fbouncedamping = models.FloatField(db_column='fBounceDamping', blank=True, null=True)
    ffusedelay = models.FloatField(db_column='fFuseDelay', blank=True, null=True)
    fgravitymultiplier = models.FloatField(db_column='fGravityMultiplier', blank=True, null=True)
    baudiowaituntilfalling = models.IntegerField(db_column='bAudioWaitUntilFalling', blank=True, null=True)
    bimpactdetonated = models.IntegerField(db_column='bImpactDetonated', blank=True, null=True)
    btumble = models.IntegerField(db_column='bTumble', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WeaponProjectiles'


class Weaponrecoils(models.Model):
    id = models.IntegerField(primary_key=True)
    eweaponrecoil = models.IntegerField(db_column='eWeaponRecoil', blank=True, null=True)
    frecoilexp = models.FloatField(db_column='fRecoilExp', blank=True, null=True)
    frecoverexp = models.FloatField(db_column='fRecoverExp', blank=True, null=True)
    nmarksmanshippitchpercentage = models.IntegerField(db_column='nMarksmanshipPitchPercentage', blank=True, null=True)
    nmarksmanshipyawpercentage = models.IntegerField(db_column='nMarksmanshipYawPercentage', blank=True, null=True)
    npitchmax = models.IntegerField(db_column='nPitchMax', blank=True, null=True)
    npitchmin = models.IntegerField(db_column='nPitchMin', blank=True, null=True)
    npitchrecoverypercentagemax = models.IntegerField(db_column='nPitchRecoveryPercentageMax', blank=True, null=True)
    npitchrecoverypercentagemin = models.IntegerField(db_column='nPitchRecoveryPercentageMin', blank=True, null=True)
    nrecoiltime = models.IntegerField(db_column='nRecoilTime', blank=True, null=True)
    nrecovertime = models.IntegerField(db_column='nRecoverTime', blank=True, null=True)
    nyawnegativemax = models.IntegerField(db_column='nYawNegativeMax', blank=True, null=True)
    nyawnegativemin = models.IntegerField(db_column='nYawNegativeMin', blank=True, null=True)
    nyawnegativerecoverypercentagemax = models.IntegerField(db_column='nYawNegativeRecoveryPercentageMax', blank=True, null=True)
    nyawnegativerecoverypercentagemin = models.IntegerField(db_column='nYawNegativeRecoveryPercentageMin', blank=True, null=True)
    nyawpositivemax = models.IntegerField(db_column='nYawPositiveMax', blank=True, null=True)
    nyawpositivemin = models.IntegerField(db_column='nYawPositiveMin', blank=True, null=True)
    nyawpositiverecoverypercentagemax = models.IntegerField(db_column='nYawPositiveRecoveryPercentageMax', blank=True, null=True)
    nyawpositiverecoverypercentagemin = models.IntegerField(db_column='nYawPositiveRecoveryPercentageMin', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WeaponRecoils'


class Weaponskinunlockitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType', blank=True, null=True)
    bhideuntilunlocked = models.IntegerField(db_column='bHideUntilUnlocked', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WeaponSkinUnlockItemTypes'


class Weaponskins(models.Model):
    id = models.IntegerField(primary_key=True)
    eitemattachmentvisual = models.IntegerField(db_column='eItemAttachmentVisual', blank=True, null=True)
    eunlock = models.IntegerField(db_column='eUnlock', blank=True, null=True)
    eweaponskin = models.IntegerField(db_column='eWeaponSkin', blank=True, null=True)
    eweapontypelink = models.IntegerField(db_column='eWeaponTypeLink', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WeaponSkins'


class Weapontypelinks(models.Model):
    id = models.IntegerField(primary_key=True)
    eweapontype_0 = models.IntegerField(db_column='eWeaponType_0', blank=True, null=True)
    eweapontype_1 = models.IntegerField(db_column='eWeaponType_1', blank=True, null=True)
    eweapontype_2 = models.IntegerField(db_column='eWeaponType_2', blank=True, null=True)
    eweapontype_3 = models.IntegerField(db_column='eWeaponType_3', blank=True, null=True)
    eweapontypelink = models.IntegerField(db_column='eWeaponTypeLink', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WeaponTypeLinks'


class Weapontypesets(models.Model):
    id = models.IntegerField(primary_key=True)
    scommandline = models.TextField(db_column='sCommandLine', blank=True, null=True)
    eweapontypeset = models.IntegerField(db_column='eWeaponTypeSet', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WeaponTypeSets'


class Weapontypes(models.Model):
    id = models.IntegerField(primary_key=True)
    eammocategory = models.IntegerField(db_column='eAmmoCategory', blank=True, null=True)
    edisabledrulesets = models.IntegerField(db_column='eDisabledRuleSets', blank=True, null=True)
    etagger = models.IntegerField(db_column='eTagger', blank=True, null=True)
    eweaponcurve = models.IntegerField(db_column='eWeaponCurve', blank=True, null=True)
    eweaponprojectile = models.IntegerField(db_column='eWeaponProjectile', blank=True, null=True)
    eweapontype = models.IntegerField(db_column='eWeaponType', blank=True, null=True)
    faccuracycooldown = models.FloatField(db_column='fAccuracyCooldown', blank=True, null=True)
    fburstinterval = models.FloatField(db_column='fBurstInterval', blank=True, null=True)
    fcrouchspeed = models.FloatField(db_column='fCrouchSpeed', blank=True, null=True)
    fequiptime = models.FloatField(db_column='fEquipTime', blank=True, null=True)
    ffireinterval = models.FloatField(db_column='fFireInterval', blank=True, null=True)
    fharddamagemodifier = models.FloatField(db_column='fHardDamageModifier', blank=True, null=True)
    fhealthdamage = models.FloatField(db_column='fHealthDamage', blank=True, null=True)
    fholstertime = models.FloatField(db_column='fHolsterTime', blank=True, null=True)
    fjumpz = models.FloatField(db_column='fJumpZ', blank=True, null=True)
    fmarksmanshipspeed = models.FloatField(db_column='fMarksmanshipSpeed', blank=True, null=True)
    fpingdistance = models.FloatField(db_column='fPingDistance', blank=True, null=True)
    fragdollimpulsescale = models.FloatField(db_column='fRagdollImpulseScale', blank=True, null=True)
    freloadendanimduration = models.FloatField(db_column='fReloadEndAnimDuration', blank=True, null=True)
    freloadtime = models.FloatField(db_column='fReloadTime', blank=True, null=True)
    fresupplydelaysecs = models.FloatField(db_column='fResupplyDelaySecs', blank=True, null=True)
    frunspeed = models.FloatField(db_column='fRunSpeed', blank=True, null=True)
    fsoftdamagemodifier = models.FloatField(db_column='fSoftDamageModifier', blank=True, null=True)
    fsprintdelay = models.FloatField(db_column='fSprintDelay', blank=True, null=True)
    fsprintspeed = models.FloatField(db_column='fSprintSpeed', blank=True, null=True)
    fstaminadamage = models.FloatField(db_column='fStaminaDamage', blank=True, null=True)
    ftaggerduration = models.FloatField(db_column='fTaggerDuration', blank=True, null=True)
    fuiharddamagelevel = models.FloatField(db_column='fUIHardDamageLevel', blank=True, null=True)
    fuirangelevel = models.FloatField(db_column='fUIRangeLevel', blank=True, null=True)
    fuirateoffire = models.FloatField(db_column='fUIRateOfFire', blank=True, null=True)
    fuisoftdamagelevel = models.FloatField(db_column='fUISoftDamageLevel', blank=True, null=True)
    fuistundamagelevel = models.FloatField(db_column='fUIStunDamageLevel', blank=True, null=True)
    fwalkspeed = models.FloatField(db_column='fWalkSpeed', blank=True, null=True)
    fwinduptime = models.FloatField(db_column='fWindUpTime', blank=True, null=True)
    nammopoolcapacity = models.IntegerField(db_column='nAmmoPoolCapacity', blank=True, null=True)
    nburstshots = models.IntegerField(db_column='nBurstShots', blank=True, null=True)
    nimpulsestrength = models.IntegerField(db_column='nImpulseStrength', blank=True, null=True)
    nmagazinecapacity = models.IntegerField(db_column='nMagazineCapacity', blank=True, null=True)
    nmagazinewarningamount = models.IntegerField(db_column='nMagazineWarningAmount', blank=True, null=True)
    nresupplyunits = models.IntegerField(db_column='nResupplyUnits', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    eclass = models.IntegerField(db_column='eClass', blank=True, null=True)
    eencumbrance = models.IntegerField(db_column='eEncumbrance', blank=True, null=True)
    ehudreticule = models.IntegerField(db_column='eHUDReticule', blank=True, null=True)
    ehudreticulemarksmanship = models.IntegerField(db_column='eHUDReticuleMarksmanship', blank=True, null=True)
    enpcfiredevent = models.IntegerField(db_column='eNPCFiredEvent', blank=True, null=True)
    enpchitevent = models.IntegerField(db_column='eNPCHitEvent', blank=True, null=True)
    eweaponfiringstate = models.IntegerField(db_column='eWeaponFiringState', blank=True, null=True)
    balwaysplayreloadendanim = models.IntegerField(db_column='bAlwaysPlayReloadEndAnim', blank=True, null=True)
    bcansprint = models.IntegerField(db_column='bCanSprint', blank=True, null=True)
    bdisallowswitchinrefiretimer = models.IntegerField(db_column='bDisallowSwitchInRefireTimer', blank=True, null=True)
    bdontdrop = models.IntegerField(db_column='bDontDrop', blank=True, null=True)
    bequipinvehicle = models.IntegerField(db_column='bEquipInVehicle', blank=True, null=True)
    bforceragdolldeath = models.IntegerField(db_column='bForceRagdollDeath', blank=True, null=True)
    bhasreloadendanimation = models.IntegerField(db_column='bHasReloadEndAnimation', blank=True, null=True)
    bisresuppliable = models.IntegerField(db_column='bIsResuppliable', blank=True, null=True)
    blesslethal = models.IntegerField(db_column='bLessLethal', blank=True, null=True)
    bloopedreload = models.IntegerField(db_column='bLoopedReload', blank=True, null=True)
    busesstopaudioevent = models.IntegerField(db_column='bUsesStopAudioEvent', blank=True, null=True)
    bwitnessing = models.IntegerField(db_column='bWitnessing', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WeaponTypes'


class Weightedrewards(models.Model):
    id = models.IntegerField(primary_key=True)
    srewardmailbody = models.TextField(db_column='sRewardMailBody', blank=True, null=True)
    srewardmailsubject = models.TextField(db_column='sRewardMailSubject', blank=True, null=True)
    ehudimage = models.IntegerField(db_column='eHUDImage', blank=True, null=True)
    erandomreward = models.IntegerField(db_column='eRandomReward', blank=True, null=True)
    ereward = models.IntegerField(db_column='eReward', blank=True, null=True)
    eweightedreward = models.IntegerField(db_column='eWeightedReward', blank=True, null=True)
    fweight = models.FloatField(db_column='fWeight', blank=True, null=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey', blank=True, null=True)
    bofferonce = models.IntegerField(db_column='bOfferOnce', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WeightedRewards'


class Witnessablecrimes(models.Model):
    id = models.IntegerField(primary_key=True)
    enotorietyforbeingwitnessed = models.IntegerField(db_column='eNotorietyForBeingWitnessed', blank=True, null=True)
    eprestigeforwitnessing = models.IntegerField(db_column='ePrestigeForWitnessing', blank=True, null=True)
    ewitnessablecrime = models.IntegerField(db_column='eWitnessableCrime', blank=True, null=True)
    fescapepenaltytimer = models.FloatField(db_column='fEscapePenaltyTimer', blank=True, null=True)
    fhotlistduration = models.FloatField(db_column='fHotListDuration', blank=True, null=True)
    fnpcwitnessableduration = models.FloatField(db_column='fNPCWitnessableDuration', blank=True, null=True)
    etriggerednpcworldevent = models.IntegerField(db_column='eTriggeredNPCWorldEvent', blank=True, null=True)
    bcontinuous = models.IntegerField(db_column='bContinuous', blank=True, null=True)
    bnodirectwitness = models.IntegerField(db_column='bNoDirectWitness', blank=True, null=True)
    sapbdb = models.TextField(db_column='sAPBDB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WitnessableCrimes'

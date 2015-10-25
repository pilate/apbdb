from django.db import models


LocalModels = vars()

def property_cache(fn):
    def wrapped(self, *args, **kwargs):
        key = '_'.join(['_', self.__class__.__name__, fn.__name__])
        if hasattr(self, key):
            return getattr(self, key)
        value = fn(self, *args, **kwargs)
        setattr(self, key, value)
        return value

    return wrapped


class Apbpawnconstant(models.Model):
    id = models.IntegerField(primary_key=True)
    fvalue = models.FloatField(db_column='fValue')
    eapbpawnconstant = models.IntegerField(db_column='eAPBPawnConstant')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'APBPawnConstant'


class Apbsupportpages(models.Model):
    id = models.IntegerField(primary_key=True)
    sbaseurl = models.TextField(db_column='sBaseURL')
    sinternalbrowsertitle = models.TextField(db_column='sInternalBrowserTitle')
    sparameters = models.TextField(db_column='sParameters')
    sregiondependanturl_inikey = models.TextField(db_column='sRegionDependantURL_INIKey')
    eapbsupportpages = models.IntegerField(db_column='eAPBSupportPages')
    eurlwippage = models.IntegerField(db_column='eURLWipPage')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'APBSupportPages'


class Apbviewporttypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    eapbviewporttype = models.IntegerField(db_column='eAPBViewportType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'APBViewportTypes'


class Activitymessageparametertypes(models.Model):
    id = models.IntegerField(primary_key=True)
    slocalisationtoken = models.TextField(db_column='sLocalisationToken')
    eactivitymessageparametertype = models.IntegerField(db_column='eActivityMessageParameterType')
    ndebugparam = models.IntegerField(db_column='nDebugParam')
    econversion = models.IntegerField(db_column='eConversion')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ActivityMessageParameterTypes'


class Activitymessagepriorities(models.Model):
    id = models.IntegerField(primary_key=True)
    eactivitymessagepriority = models.IntegerField(db_column='eActivityMessagePriority')
    fdelaymax = models.FloatField(db_column='fDelayMax')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ActivityMessagePriorities'


class Activitymessages(models.Model):
    id = models.IntegerField(primary_key=True)
    eactivitymessage = models.IntegerField(db_column='eActivityMessage')
    ehudmessage = models.IntegerField(db_column='eHUDMessage')
    eparamtype_0 = models.IntegerField(db_column='eParamType_0')
    eparamtype_1 = models.IntegerField(db_column='eParamType_1')
    eparamtype_2 = models.IntegerField(db_column='eParamType_2')
    eparamtype_3 = models.IntegerField(db_column='eParamType_3')
    eparamtype_4 = models.IntegerField(db_column='eParamType_4')
    epriority = models.IntegerField(db_column='ePriority')
    eexcludelist = models.IntegerField(db_column='eExcludeList')
    eincludelist = models.IntegerField(db_column='eIncludeList')
    elocation = models.IntegerField(db_column='eLocation')
    evalidfaction = models.IntegerField(db_column='eValidFaction')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ActivityMessages'


class Ammocategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    sname = models.TextField(db_column='sName')
    snameabbreviated = models.TextField(db_column='sNameAbbreviated')
    squantitytext = models.TextField(db_column='sQuantityText')
    eammocategory = models.IntegerField(db_column='eAmmoCategory')
    erequiresweaponunlocked = models.IntegerField(db_column='eRequiresWeaponUnlocked')
    nboxcost = models.IntegerField(db_column='nBoxCost')
    nboxsize = models.IntegerField(db_column='nBoxSize')
    ncapacity = models.IntegerField(db_column='nCapacity')
    ngiftedamount = models.IntegerField(db_column='nGiftedAmount')
    npresetboxquantity_0 = models.IntegerField(db_column='nPresetBoxQuantity_0')
    npresetboxquantity_1 = models.IntegerField(db_column='nPresetBoxQuantity_1')
    npresetboxquantity_2 = models.IntegerField(db_column='nPresetBoxQuantity_2')
    npresetboxquantity_3 = models.IntegerField(db_column='nPresetBoxQuantity_3')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    shudimage_bullet = models.IntegerField(db_column='sHUDImage_Bullet')
    bthrowngrenade = models.IntegerField(db_column='bThrownGrenade')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'AmmoCategories'


class AnimtreedecisionEquippeditem(models.Model):
    id = models.IntegerField(primary_key=True)
    eanimtreedecision_equippeditem = models.IntegerField(db_column='eAnimTreeDecision_EquippedItem')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'AnimTreeDecision_EquippedItem'


class AnimtreedecisionVehicle(models.Model):
    id = models.IntegerField(primary_key=True)
    eanimtreedecision_vehicle = models.IntegerField(db_column='eAnimTreeDecision_Vehicle')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'AnimTreeDecision_Vehicle'


class Animationdescriptors(models.Model):
    id = models.IntegerField(primary_key=True)
    eanimationdescriptor = models.IntegerField(db_column='eAnimationDescriptor')
    fstaminadrain = models.FloatField(db_column='fStaminaDrain')
    ercetype = models.IntegerField(db_column='eRCEType')
    bfreezecameraloc = models.IntegerField(db_column='bFreezeCameraLoc')
    bresetlocomotion = models.IntegerField(db_column='bResetLocomotion')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'AnimationDescriptors'


class Audioamp(models.Model):
    id = models.IntegerField(primary_key=True)
    saudioswitchname = models.TextField(db_column='sAudioSwitchName')
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart')
    fvolume = models.FloatField(db_column='fVolume')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'AudioAmp'


class Audiodumpvalve(models.Model):
    id = models.IntegerField(primary_key=True)
    saudioeventname = models.TextField(db_column='sAudioEventName')
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'AudioDumpValve'


class Audioengine(models.Model):
    id = models.IntegerField(primary_key=True)
    saudioeventname = models.TextField(db_column='sAudioEventName')
    ssimulationdataset = models.TextField(db_column='sSimulationDataSet')
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'AudioEngine'


class Audioexhaust(models.Model):
    id = models.IntegerField(primary_key=True)
    saudioeventname = models.TextField(db_column='sAudioEventName')
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'AudioExhaust'


class Audioexhaustpops(models.Model):
    id = models.IntegerField(primary_key=True)
    saudioeventname = models.TextField(db_column='sAudioEventName')
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'AudioExhaustPops'


class Audiogearchange(models.Model):
    id = models.IntegerField(primary_key=True)
    saudioeventname = models.TextField(db_column='sAudioEventName')
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'AudioGearChange'


class Audiohorn(models.Model):
    id = models.IntegerField(primary_key=True)
    saudiotype = models.TextField(db_column='sAudioType')
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart')
    fpitchmodifier = models.FloatField(db_column='fPitchModifier')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'AudioHorn'


class Audiosiren(models.Model):
    id = models.IntegerField(primary_key=True)
    saudiotype = models.TextField(db_column='sAudioType')
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'AudioSiren'


class Audiospeaker(models.Model):
    id = models.IntegerField(primary_key=True)
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart')
    feqparameter1 = models.FloatField(db_column='fEQParameter1')
    feqparameter2 = models.FloatField(db_column='fEQParameter2')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'AudioSpeaker'


class Audiotransmission(models.Model):
    id = models.IntegerField(primary_key=True)
    saudioeventname = models.TextField(db_column='sAudioEventName')
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart')
    fpitchmodifier = models.FloatField(db_column='fPitchModifier')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'AudioTransmission'


class Audioturbo(models.Model):
    id = models.IntegerField(primary_key=True)
    smainaudioeventname = models.TextField(db_column='sMainAudioEventName')
    ssecondaudioeventname = models.TextField(db_column='sSecondAudioEventName')
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart')
    fmainpitchmodifier = models.FloatField(db_column='fMainPitchModifier')
    fmainvolumefullrpm = models.FloatField(db_column='fMainVolumeFullRPM')
    fmainvolumestartrpm = models.FloatField(db_column='fMainVolumeStartRPM')
    fsecondpitchmodifier = models.FloatField(db_column='fSecondPitchModifier')
    fsecondvolumefullrpm = models.FloatField(db_column='fSecondVolumeFullRPM')
    fsecondvolumestartrpm = models.FloatField(db_column='fSecondVolumeStartRPM')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'AudioTurbo'


class Awesomeplayerdetectionrules(models.Model):
    id = models.IntegerField(primary_key=True)
    eawesomeplayerdetectionrules = models.IntegerField(db_column='eAwesomePlayerDetectionRules')
    ndistancesamplinginterval = models.IntegerField(db_column='nDistanceSamplingInterval')
    ndistancesamplingintervalthreshold = models.IntegerField(db_column='nDistanceSamplingIntervalThreshold')
    ndistancesamplingtotalthreshold = models.IntegerField(db_column='nDistanceSamplingTotalThreshold')
    ndistrictmapallowedtime = models.IntegerField(db_column='nDistrictMapAllowedTime')
    ntime = models.IntegerField(db_column='nTime')
    ntimebetweenwarnings = models.IntegerField(db_column='nTimeBetweenWarnings')
    nwarningdistrictmaptimetokick = models.IntegerField(db_column='nWarningDistrictMapTimeToKick')
    nwarningtimetokick = models.IntegerField(db_column='nWarningTimeToKick')
    ballcsa = models.IntegerField(db_column='bAllCSA')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'AwesomePlayerDetectionRules'


class Awesomeplayerdetectionrulesevents(models.Model):
    id = models.IntegerField(primary_key=True)
    eawesomeplayerdetectionrules = models.IntegerField(db_column='eAwesomePlayerDetectionRules')
    egameplayevent = models.IntegerField(db_column='eGameplayEvent')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'AwesomePlayerDetectionRulesEvents'


class Bombequipmenttypes(models.Model):
    id = models.IntegerField(primary_key=True)
    ebomblevel = models.IntegerField(db_column='eBombLevel')
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'BombEquipmentTypes'


class Bomblevels(models.Model):
    id = models.IntegerField(primary_key=True)
    ebomblevel = models.IntegerField(db_column='eBombLevel')
    eexplosiontype = models.IntegerField(db_column='eExplosionType')
    nlevel = models.IntegerField(db_column='nLevel')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'BombLevels'


class Budgettrackervalues(models.Model):
    id = models.IntegerField(primary_key=True)
    sbudgetcategories = models.TextField(db_column='sBudgetCategories')
    fbudgetvalue = models.FloatField(db_column='fBudgetValue')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'BudgetTrackerValues'


class CcArraypurchaseelements(models.Model):
    id = models.IntegerField(primary_key=True)
    sattributearray = models.TextField(db_column='sAttributeArray')
    ecc_purchaseelement = models.IntegerField(db_column='eCC_PurchaseElement')
    naddcost = models.IntegerField(db_column='nAddCost')
    ndeletecost = models.IntegerField(db_column='nDeleteCost')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CC_ArrayPurchaseElements'


class CcPurchaseelement(models.Model):
    id = models.IntegerField(primary_key=True)
    sattributes = models.TextField(db_column='sAttributes')
    sdisplayname = models.TextField(db_column='sDisplayName')
    ecc_purchaseelement = models.IntegerField(db_column='eCC_PurchaseElement')
    ncost = models.IntegerField(db_column='nCost')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CC_PurchaseElement'


class Ccameramodes(models.Model):
    id = models.IntegerField(primary_key=True)
    f16_9backadjust = models.FloatField(db_column='f16_9BackAdjust')
    f16_9crouchbackadjust = models.FloatField(db_column='f16_9CrouchBackAdjust')
    f16_9crouchheightadjust = models.FloatField(db_column='f16_9CrouchHeightAdjust')
    f16_9crouchrightadjust = models.FloatField(db_column='f16_9CrouchRightAdjust')
    f16_9crouchrightadjustpitchscalar = models.FloatField(db_column='f16_9CrouchRightAdjustPitchScalar')
    f16_9fov = models.FloatField(db_column='f16_9FOV')
    f16_9heightadjust = models.FloatField(db_column='f16_9HeightAdjust')
    f16_9rightadjust = models.FloatField(db_column='f16_9RightAdjust')
    f16_9rightadjustpitchscalar = models.FloatField(db_column='f16_9RightAdjustPitchScalar')
    f4_3backadjust = models.FloatField(db_column='f4_3BackAdjust')
    f4_3crouchbackadjust = models.FloatField(db_column='f4_3CrouchBackAdjust')
    f4_3crouchheightadjust = models.FloatField(db_column='f4_3CrouchHeightAdjust')
    f4_3crouchrightadjust = models.FloatField(db_column='f4_3CrouchRightAdjust')
    f4_3crouchrightadjustpitchscalar = models.FloatField(db_column='f4_3CrouchRightAdjustPitchScalar')
    f4_3fov = models.FloatField(db_column='f4_3FOV')
    f4_3heightadjust = models.FloatField(db_column='f4_3HeightAdjust')
    f4_3rightadjust = models.FloatField(db_column='f4_3RightAdjust')
    f4_3rightadjustpitchscalar = models.FloatField(db_column='f4_3RightAdjustPitchScalar')
    fadjustblendspeed = models.FloatField(db_column='fAdjustBlendSpeed')
    fcameraoriginlagspeed = models.FloatField(db_column='fCameraOriginLagSpeed')
    fcamerarollblendspeed = models.FloatField(db_column='fCameraRollBlendSpeed')
    fcamerarolldegrees = models.FloatField(db_column='fCameraRollDegrees')
    fcrouchsafelocx = models.FloatField(db_column='fCrouchSafeLocX')
    fcrouchsafelocy = models.FloatField(db_column='fCrouchSafeLocY')
    fcrouchsafelocz = models.FloatField(db_column='fCrouchSafeLocZ')
    ffovblendspeed = models.FloatField(db_column='fFOVBlendSpeed')
    fsafelocx = models.FloatField(db_column='fSafeLocX')
    fsafelocy = models.FloatField(db_column='fSafeLocY')
    fsafelocz = models.FloatField(db_column='fSafeLocZ')
    ecameramode = models.IntegerField(db_column='eCameraMode')
    bcandolookbehindcam = models.IntegerField(db_column='bCanDoLookBehindCam')
    bcrouchenabled = models.IntegerField(db_column='bCrouchEnabled')
    busedefaultcameraadjustments = models.IntegerField(db_column='bUseDefaultCameraAdjustments')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CCameraModes'


class CsaAutoroutedata(models.Model):
    id = models.IntegerField(primary_key=True)
    ssocketname_0 = models.TextField(db_column='sSocketName_0')
    ssocketname_1 = models.TextField(db_column='sSocketName_1')
    ssocketname_2 = models.TextField(db_column='sSocketName_2')
    ssocketname_3 = models.TextField(db_column='sSocketName_3')
    ssocketname_4 = models.TextField(db_column='sSocketName_4')
    ecsa_autoroutedata = models.IntegerField(db_column='eCSA_AutoRouteData')
    foffsetforward = models.FloatField(db_column='fOffsetForward')
    foffsetright = models.FloatField(db_column='fOffsetRight')
    ealignmenttype = models.IntegerField(db_column='eAlignmentType')
    eautoroutetype = models.IntegerField(db_column='eAutoRouteType')
    broutealongnormal = models.IntegerField(db_column='bRouteAlongNormal')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CSA_AutoRouteData'


class CsaEatpropassociation(models.Model):
    id = models.IntegerField(primary_key=True)
    eautoroutedata = models.IntegerField(db_column='eAutoRouteData')
    ecsa_eatpropassociation = models.IntegerField(db_column='eCSA_EATPropAssociation')
    eequipmentanimation = models.IntegerField(db_column='eEquipmentAnimation')
    eitemassociation = models.IntegerField(db_column='eItemAssociation')
    epropcategory = models.IntegerField(db_column='ePropCategory')
    bchecksuseautoroutelocation = models.IntegerField(db_column='bChecksUseAutoRouteLocation')
    busesmallcollisionvolume = models.IntegerField(db_column='bUseSmallCollisionVolume')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CSA_EATPropAssociation'


class CsaEatvehicleassociation(models.Model):
    id = models.IntegerField(primary_key=True)
    eequipmentanimation = models.IntegerField(db_column='eEquipmentAnimation')
    eitemassociation = models.IntegerField(db_column='eItemAssociation')
    evehicleanimationtype = models.IntegerField(db_column='eVehicleAnimationType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CSA_EATVehicleAssociation'


class CsaEquipmentanimationtype(models.Model):
    id = models.IntegerField(primary_key=True)
    sintroanim = models.TextField(db_column='sIntroAnim')
    smainanim1 = models.TextField(db_column='sMainAnim1')
    smainanim2 = models.TextField(db_column='sMainAnim2')
    smainanim3 = models.TextField(db_column='sMainAnim3')
    soutroanim = models.TextField(db_column='sOutroAnim')
    svfxclass = models.TextField(db_column='sVFXClass')
    ecsa_equipmentanimationtype = models.IntegerField(db_column='eCSA_EquipmentAnimationType')
    foutroduration = models.FloatField(db_column='fOutroDuration')
    eoutroendpoint = models.IntegerField(db_column='eOutroEndPoint')
    bcanmirror = models.IntegerField(db_column='bCanMirror')
    buserootmotion = models.IntegerField(db_column='bUseRootMotion')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CSA_EquipmentAnimationType'


class CsaIatstate(models.Model):
    id = models.IntegerField(primary_key=True)
    nmaxconcurrentusersperactor = models.IntegerField(db_column='nMaxConcurrentUsersPerActor')
    nmaxconcurrentusersperip = models.IntegerField(db_column='nMaxConcurrentUsersPerIP')
    ecsa_iatstate = models.IntegerField(db_column='eCSA_IATState')
    einteractiveactortype = models.IntegerField(db_column='eInteractiveActorType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CSA_IATState'


class CsaIatstateassociation(models.Model):
    id = models.IntegerField(primary_key=True)
    ecsa_iatstateassociation = models.IntegerField(db_column='eCSA_IATStateAssociation')
    einputmapping = models.IntegerField(db_column='eInputMapping')
    fduration = models.FloatField(db_column='fDuration')
    nprioritylayer = models.IntegerField(db_column='nPriorityLayer')
    econtextsensitiveaction = models.IntegerField(db_column='eContextSensitiveAction')
    ecsa_iatstate = models.IntegerField(db_column='eCSA_IATState')
    boverridepriority = models.IntegerField(db_column='bOverridePriority')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CSA_IATStateAssociation'


class CsaInputmapping(models.Model):
    id = models.IntegerField(primary_key=True)
    skeybinding = models.TextField(db_column='sKeyBinding')
    ecsa_inputmapping = models.IntegerField(db_column='eCSA_InputMapping')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CSA_InputMapping'


class CsaItemassociation(models.Model):
    id = models.IntegerField(primary_key=True)
    ecsa_itemassociation = models.IntegerField(db_column='eCSA_ItemAssociation')
    edefaultequipmentanimationtype = models.IntegerField(db_column='eDefaultEquipmentAnimationType')
    eequipmenttype = models.IntegerField(db_column='eEquipmentType')
    eitemassociationcategory = models.IntegerField(db_column='eItemAssociationCategory')
    feffectivenessmodifier = models.FloatField(db_column='fEffectivenessModifier')
    econtextsensitiveaction = models.IntegerField(db_column='eContextSensitiveAction')
    efaction = models.IntegerField(db_column='eFaction')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CSA_ItemAssociation'


class CsaItemassociationcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    seffect = models.TextField(db_column='sEffect')
    ecsa_itemassociationcategory = models.IntegerField(db_column='eCSA_ItemAssociationCategory')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CSA_ItemAssociationCategories'


class CsaTaskitemanimationset(models.Model):
    id = models.IntegerField(primary_key=True)
    sanimname = models.TextField(db_column='sAnimName')
    ecsa_taskitemanimationset = models.IntegerField(db_column='eCSA_TaskItemAnimationSet')
    ecsa = models.IntegerField(db_column='eCSA')
    etaskitemsize = models.IntegerField(db_column='eTaskItemSize')
    blogical = models.IntegerField(db_column='bLogical')
    buseanimduration = models.IntegerField(db_column='bUseAnimDuration')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CSA_TaskItemAnimationSet'


class Cameraconstants(models.Model):
    id = models.IntegerField(primary_key=True)
    fvalue = models.FloatField(db_column='fValue')
    ecameraconstant = models.IntegerField(db_column='eCameraConstant')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CameraConstants'


class Camerahandycampresetexported(models.Model):
    id = models.IntegerField(primary_key=True)
    ecamerahandycampreset = models.IntegerField(db_column='eCameraHandyCamPreset')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CameraHandyCamPresetExported'


class Camerahandycampresets(models.Model):
    id = models.IntegerField(primary_key=True)
    ecamerahandycampreset = models.IntegerField(db_column='eCameraHandyCamPreset')
    einterpolateto = models.IntegerField(db_column='eInterpolateTo')
    fchangeinmovementspeed = models.FloatField(db_column='fChangeInMovementSpeed')
    fdelaymax = models.FloatField(db_column='fDelayMax')
    fdelaymin = models.FloatField(db_column='fDelayMin')
    fduration = models.FloatField(db_column='fDuration')
    finterpolationspeedmax = models.FloatField(db_column='fInterpolationSpeedMax')
    finterpolationspeedmin = models.FloatField(db_column='fInterpolationSpeedMin')
    finterptodelay = models.FloatField(db_column='fInterpToDelay')
    fmovementspeedmax = models.FloatField(db_column='fMovementSpeedMax')
    fmovementspeedmin = models.FloatField(db_column='fMovementSpeedMin')
    nmaxdeviationpitch = models.IntegerField(db_column='nMaxDeviationPitch')
    nmaxdeviationroll = models.IntegerField(db_column='nMaxDeviationRoll')
    nmaxdeviationyaw = models.IntegerField(db_column='nMaxDeviationYaw')
    ballowactivation = models.IntegerField(db_column='bAllowActivation')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CameraHandyCamPresets'


class Cameraseatsetups(models.Model):
    id = models.IntegerField(primary_key=True)
    ecameraseatsetup = models.IntegerField(db_column='eCameraSeatSetup')
    ffov = models.FloatField(db_column='fFOV')
    fideallocoffset_x = models.FloatField(db_column='fIdealLocOffset_X')
    fideallocoffset_y = models.FloatField(db_column='fIdealLocOffset_Y')
    fideallocoffset_z = models.FloatField(db_column='fIdealLocOffset_Z')
    fworstlocoffset_x = models.FloatField(db_column='fWorstLocOffset_X')
    fworstlocoffset_y = models.FloatField(db_column='fWorstLocOffset_Y')
    fworstlocoffset_z = models.FloatField(db_column='fWorstLocOffset_Z')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CameraSeatSetups'


class Camerashakepresetexported(models.Model):
    id = models.IntegerField(primary_key=True)
    ecamerashakepreset = models.IntegerField(db_column='eCameraShakePreset')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CameraShakePresetExported'


class Camerashakepresets(models.Model):
    id = models.IntegerField(primary_key=True)
    ecamerashakepreset = models.IntegerField(db_column='eCameraShakePreset')
    fduration = models.FloatField(db_column='fDuration')
    ffovamplitude = models.FloatField(db_column='fFOVAmplitude')
    ffovfrequency = models.FloatField(db_column='fFOVFrequency')
    flocationamplitudex = models.FloatField(db_column='fLocationAmplitudeX')
    flocationamplitudey = models.FloatField(db_column='fLocationAmplitudeY')
    flocationamplitudez = models.FloatField(db_column='fLocationAmplitudeZ')
    flocationfrequencyx = models.FloatField(db_column='fLocationFrequencyX')
    flocationfrequencyy = models.FloatField(db_column='fLocationFrequencyY')
    flocationfrequencyz = models.FloatField(db_column='fLocationFrequencyZ')
    frotationamplitudex = models.FloatField(db_column='fRotationAmplitudeX')
    frotationamplitudey = models.FloatField(db_column='fRotationAmplitudeY')
    frotationamplitudez = models.FloatField(db_column='fRotationAmplitudeZ')
    frotationfrequencyx = models.FloatField(db_column='fRotationFrequencyX')
    frotationfrequencyy = models.FloatField(db_column='fRotationFrequencyY')
    frotationfrequencyz = models.FloatField(db_column='fRotationFrequencyZ')
    brandomstartingfov = models.IntegerField(db_column='bRandomStartingFOV')
    brandomstartinglocationx = models.IntegerField(db_column='bRandomStartingLocationX')
    brandomstartinglocationy = models.IntegerField(db_column='bRandomStartingLocationY')
    brandomstartinglocationz = models.IntegerField(db_column='bRandomStartingLocationZ')
    brandomstartingrotationx = models.IntegerField(db_column='bRandomStartingRotationX')
    brandomstartingrotationy = models.IntegerField(db_column='bRandomStartingRotationY')
    brandomstartingrotationz = models.IntegerField(db_column='bRandomStartingRotationZ')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CameraShakePresets'


class Capacityitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    namount = models.IntegerField(db_column='nAmount')
    einventoryitemcategory = models.IntegerField(db_column='eInventoryItemCategory')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CapacityItemTypes'


class Charactercustomisationoverrides(models.Model):
    id = models.IntegerField(primary_key=True)
    sfullbodymeshoverridefemale = models.TextField(db_column='sFullBodyMeshOverrideFemale')
    sfullbodymeshoverridemale = models.TextField(db_column='sFullBodyMeshOverrideMale')
    svfxtemplatefemale = models.TextField(db_column='sVFXTemplateFemale')
    svfxtemplatemale = models.TextField(db_column='sVFXTemplateMale')
    echaractercustomisationoverride = models.IntegerField(db_column='eCharacterCustomisationOverride')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CharacterCustomisationOverrides'


class Characterinteractionmenu(models.Model):
    id = models.IntegerField(primary_key=True)
    sicon = models.TextField(db_column='sIcon')
    sid = models.TextField(db_column='sID')
    nposition = models.IntegerField(db_column='nPosition')
    bsamedistrict = models.IntegerField(db_column='bSameDistrict')
    bsamefaction = models.IntegerField(db_column='bSameFaction')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CharacterInteractionMenu'


class Charactermodifieritemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CharacterModifierItemTypes'


class Characterstatuses(models.Model):
    id = models.IntegerField(primary_key=True)
    estatusiconcombo = models.IntegerField(db_column='eStatusIconCombo')
    echaracterstatus = models.IntegerField(db_column='eCharacterStatus')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CharacterStatuses'


class Charactervoipstatus(models.Model):
    id = models.IntegerField(primary_key=True)
    evoipiconcombo = models.IntegerField(db_column='eVOIPIconCombo')
    echaractervoipstatus = models.IntegerField(db_column='eCharacterVOIPStatus')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CharacterVOIPStatus'


class Chatconstants(models.Model):
    id = models.IntegerField(primary_key=True)
    fvalue = models.FloatField(db_column='fValue')
    echatconstant = models.IntegerField(db_column='eChatConstant')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ChatConstants'


class Chatmessagecategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    sfunctionname = models.TextField(db_column='sFunctionName')
    ssecondaryslashcommand = models.TextField(db_column='sSecondarySlashCommand')
    sslashcommand = models.TextField(db_column='sSlashCommand')
    ssyntaxexample = models.TextField(db_column='sSyntaxExample')
    stag = models.TextField(db_column='sTag')
    efiltercolour = models.IntegerField(db_column='eFilterColour')
    echatmessagecategory = models.IntegerField(db_column='eChatMessageCategory')
    eworksfromstate = models.IntegerField(db_column='eWorksFromState')
    bdisplaynotification = models.IntegerField(db_column='bDisplayNotification')
    bhasaudionotification = models.IntegerField(db_column='bHasAudioNotification')
    bmodepersists = models.IntegerField(db_column='bModePersists')
    bvalidcommand = models.IntegerField(db_column='bValidCommand')
    bvalidfilter = models.IntegerField(db_column='bValidFilter')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ChatMessageCategories'


class Chattags(models.Model):
    id = models.IntegerField(primary_key=True)
    stagtext = models.TextField(db_column='sTagText')
    etagcolour = models.IntegerField(db_column='eTagColour')
    npriority = models.IntegerField(db_column='nPriority')
    echattag = models.IntegerField(db_column='eChatTag')
    erequiredpermission = models.IntegerField(db_column='eRequiredPermission')
    bhiddenbydefault = models.IntegerField(db_column='bHiddenByDefault')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ChatTags'


class Clanranks(models.Model):
    id = models.IntegerField(primary_key=True)
    sname = models.TextField(db_column='sName')
    eicon = models.IntegerField(db_column='eIcon')
    eclanrank = models.IntegerField(db_column='eClanRank')
    bassignrank = models.IntegerField(db_column='bAssignRank')
    bclanchatlisten = models.IntegerField(db_column='bClanChatListen')
    bclanchatspeak = models.IntegerField(db_column='bClanChatSpeak')
    bcontact = models.IntegerField(db_column='bContact')
    beditclanbio = models.IntegerField(db_column='bEditClanBio')
    beditclaninformation = models.IntegerField(db_column='bEditClanInformation')
    beditclansymbol = models.IntegerField(db_column='bEditClanSymbol')
    beditclantheme = models.IntegerField(db_column='bEditClanTheme')
    beditmotd = models.IntegerField(db_column='bEditMotd')
    beditprivatenote = models.IntegerField(db_column='bEditPrivateNote')
    beditpublicnote = models.IntegerField(db_column='bEditPublicNote')
    binvitemember = models.IntegerField(db_column='bInviteMember')
    bofficerchatlisten = models.IntegerField(db_column='bOfficerChatListen')
    bofficerchatspeak = models.IntegerField(db_column='bOfficerChatSpeak')
    bremovemember = models.IntegerField(db_column='bRemoveMember')
    breuseme = models.IntegerField(db_column='bReuseMe')
    bviewprivatenote = models.IntegerField(db_column='bViewPrivateNote')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ClanRanks'


class Clothingitemcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    eclothingitemcategory = models.IntegerField(db_column='eClothingItemCategory')
    einventoryiteminfracategory = models.IntegerField(db_column='eInventoryItemInfraCategory')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ClothingItemCategories'


class Clothingitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    sresource = models.TextField(db_column='sResource')
    egolempart = models.IntegerField(db_column='eGolemPart')
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    nreeditfee = models.IntegerField(db_column='nReeditFee')
    bfemale = models.IntegerField(db_column='bFemale')
    bmale = models.IntegerField(db_column='bMale')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ClothingItemTypes'


class Consolecommands(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    sdisplayname = models.TextField(db_column='sDisplayName')
    sfunctionname = models.TextField(db_column='sFunctionName')
    sslashcommand = models.TextField(db_column='sSlashCommand')
    ssyntaxexample = models.TextField(db_column='sSyntaxExample')
    econsolecommand = models.IntegerField(db_column='eConsoleCommand')
    nmaxargcount = models.IntegerField(db_column='nMaxArgCount')
    nminargcount = models.IntegerField(db_column='nMinArgCount')
    ecommandtype = models.IntegerField(db_column='eCommandType')
    epermissionrequired = models.IntegerField(db_column='ePermissionRequired')
    eworksfromstate = models.IntegerField(db_column='eWorksFromState')
    benabled = models.IntegerField(db_column='bEnabled')
    bworksineditors = models.IntegerField(db_column='bWorksInEditors')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ConsoleCommands'


class Contactlevels(models.Model):
    id = models.IntegerField(primary_key=True)
    srewardmailbody = models.TextField(db_column='sRewardMailBody')
    srewardmailsubject = models.TextField(db_column='sRewardMailSubject')
    econtact = models.IntegerField(db_column='eContact')
    econtactlevel = models.IntegerField(db_column='eContactLevel')
    erewardpackage = models.IntegerField(db_column='eRewardPackage')
    forganisationrewardmultiplier = models.FloatField(db_column='fOrganisationRewardMultiplier')
    ncontactscore = models.IntegerField(db_column='nContactScore')
    nlevel = models.IntegerField(db_column='nLevel')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    nstandingthreshold = models.IntegerField(db_column='nStandingThreshold')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ContactLevels'


class Contactreferrals(models.Model):
    id = models.IntegerField(primary_key=True)
    econtactlevel = models.IntegerField(db_column='eContactLevel')
    eunlockedcontact = models.IntegerField(db_column='eUnlockedContact')
    npartialunlockindex = models.IntegerField(db_column='nPartialUnlockIndex')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ContactReferrals'


class Contactrotationanims(models.Model):
    id = models.IntegerField(primary_key=True)
    sleftrotationanim = models.TextField(db_column='sLeftRotationAnim')
    srightrotationanim = models.TextField(db_column='sRightRotationAnim')
    econtactrotationanim = models.IntegerField(db_column='eContactRotationAnim')
    nangle = models.IntegerField(db_column='nAngle')
    nanglecutoff = models.IntegerField(db_column='nAngleCutoff')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ContactRotationAnims'


class Contacts(models.Model):
    id = models.IntegerField(primary_key=True)
    nsecondarykey = models.TextField(db_column='nSecondaryKey')
    saudiotype = models.TextField(db_column='sAudioType')
    sdescription = models.TextField(db_column='sDescription')
    stitle = models.TextField(db_column='sTitle')
    econtact = models.IntegerField(db_column='eContact')
    econtacticon = models.IntegerField(db_column='eContactIcon')
    edistrict = models.IntegerField(db_column='eDistrict')
    emissionpurpose = models.IntegerField(db_column='eMissionPurpose')
    epurchaseshoptype = models.IntegerField(db_column='ePurchaseShopType')
    npartialunlocks = models.IntegerField(db_column='nPartialUnlocks')
    econtacttype = models.IntegerField(db_column='eContactType')
    edealsinrewardtokenitems = models.IntegerField(db_column='eDealsInRewardTokenItems')
    eorganisation = models.IntegerField(db_column='eOrganisation')
    bbuyscrossorganisation = models.IntegerField(db_column='bBuysCrossOrganisation')
    bdealsincommonitems = models.IntegerField(db_column='bDealsInCommonItems')
    bdefaultassets = models.IntegerField(db_column='bDefaultAssets')
    bexcludefromtrackedactivities = models.IntegerField(db_column='bExcludeFromTrackedActivities')
    bfemale = models.IntegerField(db_column='bFemale')
    bhidden = models.IntegerField(db_column='bHidden')
    binitiallyunlocked = models.IntegerField(db_column='bInitiallyUnlocked')
    bleftalignname = models.IntegerField(db_column='bLeftAlignName')
    btest = models.IntegerField(db_column='bTest')
    btutor = models.IntegerField(db_column='bTutor')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'Contacts'


class Contextsensitiveaction(models.Model):
    id = models.IntegerField(primary_key=True)
    edefaultautoroutedata = models.IntegerField(db_column='eDefaultAutoRouteData')
    faimdot = models.FloatField(db_column='fAimDot')
    fcameradirectionaimdotweightingscalar = models.FloatField(db_column='fCameraDirectionAimDotWeightingScalar')
    fdistanceweightingscalar = models.FloatField(db_column='fDistanceWeightingScalar')
    fhorizontalserverdistanceerrormargin = models.FloatField(db_column='fHorizontalServerDistanceErrorMargin')
    fhudhintdistance = models.FloatField(db_column='fHUDHintDistance')
    finteractiondistance = models.FloatField(db_column='fInteractionDistance')
    fpawndirectionaimdotweightingscalar = models.FloatField(db_column='fPawnDirectionAimDotWeightingScalar')
    fverticalinteractiondistance = models.FloatField(db_column='fVerticalInteractionDistance')
    fverticalserverdistanceerrormargin = models.FloatField(db_column='fVerticalServerDistanceErrorMargin')
    nprioritylayer = models.IntegerField(db_column='nPriorityLayer')
    econtextsensitiveaction = models.IntegerField(db_column='eContextSensitiveAction')
    edefaultalignmenttype = models.IntegerField(db_column='eDefaultAlignmentType')
    elinechecktype = models.IntegerField(db_column='eLineCheckType')
    baimcheck = models.IntegerField(db_column='bAimCheck')
    ballowwhilefalling = models.IntegerField(db_column='bAllowWhileFalling')
    bchecksuseautoroutedata = models.IntegerField(db_column='bChecksUseAutoRouteData')
    bdefaultlinecheck = models.IntegerField(db_column='bDefaultLineCheck')
    bdistancecheck = models.IntegerField(db_column='bDistanceCheck')
    bisanimationdrivenaction = models.IntegerField(db_column='bIsAnimationDrivenAction')
    bistargetedcsa = models.IntegerField(db_column='bIsTargetedCSA')
    blargetaskitem = models.IntegerField(db_column='bLargeTaskItem')
    bmediumtaskitem = models.IntegerField(db_column='bMediumTaskItem')
    bsingleinteractionpoint = models.IntegerField(db_column='bSingleInteractionPoint')
    bsingleprogressbar = models.IntegerField(db_column='bSingleProgressBar')
    bsmalltaskitem = models.IntegerField(db_column='bSmallTaskItem')
    bsprintpriority = models.IntegerField(db_column='bSprintPriority')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ContextSensitiveAction'


class Contextsensitiveactionbase(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayname = models.TextField(db_column='sDisplayName')
    ebegincsatutorialtrigger = models.IntegerField(db_column='eBeginCSATutorialTrigger')
    eendcsatutorialtrigger = models.IntegerField(db_column='eEndCSATutorialTrigger')
    eanimtype = models.IntegerField(db_column='eAnimType')
    econtextsensitiveactionbase = models.IntegerField(db_column='eContextSensitiveActionBase')
    einputtype = models.IntegerField(db_column='eInputType')
    eopposingcsa = models.IntegerField(db_column='eOpposingCSA')
    bcancelscrouch = models.IntegerField(db_column='bCancelsCrouch')
    bcanresume = models.IntegerField(db_column='bCanResume')
    bconsideractive = models.IntegerField(db_column='bConsiderActive')
    bindefiniteduration = models.IntegerField(db_column='bIndefiniteDuration')
    binterruptinventory = models.IntegerField(db_column='bInterruptInventory')
    binvoked = models.IntegerField(db_column='bInvoked')
    bmissioncsa = models.IntegerField(db_column='bMissionCSA')
    bnohideweapon = models.IntegerField(db_column='bNoHideWeapon')
    bprogressbar = models.IntegerField(db_column='bProgressBar')
    bsmalltargetvolume = models.IntegerField(db_column='bSmallTargetVolume')
    btimedduration = models.IntegerField(db_column='bTimedDuration')
    bvolumecsa = models.IntegerField(db_column='bVolumeCSA')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ContextSensitiveActionBase'


class Coopcheckpointmultipliers(models.Model):
    id = models.IntegerField(primary_key=True)
    fmultiplier = models.FloatField(db_column='fMultiplier')
    ncoopcheckpointmultipliers = models.IntegerField(db_column='nCoopCheckpointMultipliers')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CoopCheckpointMultipliers'


class Customisedassetpriorities(models.Model):
    id = models.IntegerField(primary_key=True)
    fpriority = models.FloatField(db_column='fPriority')
    ecustomisedassetpriority = models.IntegerField(db_column='eCustomisedAssetPriority')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'CustomisedAssetPriorities'


class Dailyactivities(models.Model):
    id = models.IntegerField(primary_key=True)
    edailyactivity = models.IntegerField(db_column='eDailyActivity')
    eprobability = models.IntegerField(db_column='eProbability')
    eredeemablereward = models.IntegerField(db_column='eRedeemableReward')
    etrackedactivity = models.IntegerField(db_column='eTrackedActivity')
    nrefreshtime = models.IntegerField(db_column='nRefreshTime')
    nrequirement = models.IntegerField(db_column='nRequirement')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'DailyActivities'


class Dailyactivitycontacts(models.Model):
    id = models.IntegerField(primary_key=True)
    shuddescription = models.TextField(db_column='sHUDDescription')
    slongdescription = models.TextField(db_column='sLongDescription')
    stitle = models.TextField(db_column='sTitle')
    econtactlevel = models.IntegerField(db_column='eContactLevel')
    edailyactivity = models.IntegerField(db_column='eDailyActivity')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'DailyActivityContacts'


class Damageableattachmentvisuals(models.Model):
    id = models.IntegerField(primary_key=True)
    eitemattachmentvisual = models.IntegerField(db_column='eItemAttachmentVisual')
    fcollisionarc = models.FloatField(db_column='fCollisionArc')
    fcollisioncrouchheightoffset = models.FloatField(db_column='fCollisionCrouchHeightOffset')
    fcollisionheightbottom = models.FloatField(db_column='fCollisionHeightBottom')
    fcollisionheighttop = models.FloatField(db_column='fCollisionHeightTop')
    bisrightsidecarry = models.IntegerField(db_column='bIsRightSideCarry')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'DamageableAttachmentVisuals'


class Defaultcustomcolours(models.Model):
    id = models.IntegerField(primary_key=True)
    edefaultcustomcolour = models.IntegerField(db_column='eDefaultCustomColour')
    nhue = models.IntegerField(db_column='nHue')
    nlum = models.IntegerField(db_column='nLum')
    nsat = models.IntegerField(db_column='nSat')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'DefaultCustomColours'


class Defaultoutfititems(models.Model):
    id = models.IntegerField(primary_key=True)
    eclothingitemtype = models.IntegerField(db_column='eClothingItemType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'DefaultOutfitItems'


class DefaultTodBehaviours(models.Model):
    id = models.IntegerField(primary_key=True)
    etod_event = models.IntegerField(db_column='eTOD_Event')
    flikelihood = models.FloatField(db_column='fLikelihood')
    ereaction = models.IntegerField(db_column='eReaction')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'Default_TOD_Behaviours'


class Designerconstants(models.Model):
    id = models.IntegerField(primary_key=True)
    fvalue = models.FloatField(db_column='fValue')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'DesignerConstants'


class Designerconstants2(models.Model):
    id = models.IntegerField(primary_key=True)
    scomment = models.TextField(db_column='sComment')
    fvalue = models.FloatField(db_column='fValue')
    edesignerconstant2 = models.IntegerField(db_column='eDesignerConstant2')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'DesignerConstants2'


class Displaypoint(models.Model):
    id = models.IntegerField(primary_key=True)
    nsecondarykey = models.TextField(db_column='nSecondaryKey')
    sdescription = models.TextField(db_column='sDescription')
    sobtainedby = models.TextField(db_column='sObtainedBy')
    sscreenshot = models.TextField(db_column='sScreenShot')
    sshorttitle = models.TextField(db_column='sShortTitle')
    stitle = models.TextField(db_column='sTitle')
    edisplaypoint = models.IntegerField(db_column='eDisplayPoint')
    edistrict = models.IntegerField(db_column='eDistrict')
    eactivationtype = models.IntegerField(db_column='eActivationType')
    etype = models.IntegerField(db_column='eType')
    bcriminal = models.IntegerField(db_column='bCriminal')
    benforcer = models.IntegerField(db_column='bEnforcer')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'DisplayPoint'


class Districtblocks(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    sdisplayname = models.TextField(db_column='sDisplayName')
    edistrict = models.IntegerField(db_column='eDistrict')
    edistrictblock = models.IntegerField(db_column='eDistrictBlock')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    themes_0 = models.IntegerField(db_column='Themes_0')
    themes_1 = models.IntegerField(db_column='Themes_1')
    themes_2 = models.IntegerField(db_column='Themes_2')
    themes_3 = models.IntegerField(db_column='Themes_3')
    themes_4 = models.IntegerField(db_column='Themes_4')
    themes_5 = models.IntegerField(db_column='Themes_5')
    themes_6 = models.IntegerField(db_column='Themes_6')
    themes_7 = models.IntegerField(db_column='Themes_7')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'DistrictBlocks'


class Districtinstancetype(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    sdisplayname = models.TextField(db_column='sDisplayName')
    edistrict = models.IntegerField(db_column='eDistrict')
    edistrictinstancetype = models.IntegerField(db_column='eDistrictInstanceType')
    edistrictlanguage = models.IntegerField(db_column='eDistrictLanguage')
    edistrictrating = models.IntegerField(db_column='eDistrictRating')
    edistrictruleset = models.IntegerField(db_column='eDistrictRuleSet')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'DistrictInstanceType'


class Districtlanguage(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayname = models.TextField(db_column='sDisplayName')
    slanguageshortname = models.TextField(db_column='sLanguageShortName')
    slocalisationini = models.TextField(db_column='sLocalisationINI')
    edistrictlanguage = models.IntegerField(db_column='eDistrictLanguage')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'DistrictLanguage'


class Districtrating(models.Model):
    id = models.IntegerField(primary_key=True)
    edistrictrating = models.IntegerField(db_column='eDistrictRating')
    nmaxrating = models.IntegerField(db_column='nMaxRating')
    nminrating = models.IntegerField(db_column='nMinRating')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'DistrictRating'


class Districtrulesets(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayname = models.TextField(db_column='sDisplayName')
    edistrictruleset = models.IntegerField(db_column='eDistrictRuleSet')
    emissiontypefilter_0 = models.IntegerField(db_column='eMissionTypeFilter_0')
    emissiontypefilter_1 = models.IntegerField(db_column='eMissionTypeFilter_1')
    fmaximumtoohightime = models.FloatField(db_column='fMaximumTooHighTime')
    freticuletargetingdistance = models.FloatField(db_column='fReticuleTargetingDistance')
    fscoreunopposedmultiplier = models.FloatField(db_column='fScoreUnopposedMultiplier')
    fwscharinfodistance = models.FloatField(db_column='fWSCharInfoDistance')
    nmissiondelay = models.IntegerField(db_column='nMissionDelay')
    nnewmissioncooldowntimer = models.IntegerField(db_column='nNewMissionCooldownTimer')
    echaractercollideswithcharacter = models.IntegerField(db_column='eCharacterCollidesWithCharacter')
    edistricttypeinfo = models.IntegerField(db_column='eDistrictTypeInfo')
    eheatfunctionality = models.IntegerField(db_column='eHeatFunctionality')
    epvpdamage = models.IntegerField(db_column='ePvPDamage')
    etutorialbypassbehaviour = models.IntegerField(db_column='eTutorialBypassBehaviour')
    eweapontypeset = models.IntegerField(db_column='eWeaponTypeSet')
    ewitnessingfunctionality = models.IntegerField(db_column='eWitnessingFunctionality')
    ewitnessingmissionsystem = models.IntegerField(db_column='eWitnessingMissionSystem')
    ballowbackupcall = models.IntegerField(db_column='bAllowBackupCall')
    ballowfnmods = models.IntegerField(db_column='bAllowFnMods')
    balwaysaccessinventory = models.IntegerField(db_column='bAlwaysAccessInventory')
    bbountiesavailable = models.IntegerField(db_column='bBountiesAvailable')
    bcontactreferralson = models.IntegerField(db_column='bContactReferralsOn')
    bcustomisationlimiter = models.IntegerField(db_column='bCustomisationLimiter')
    bdistinguishfactionnamecolours = models.IntegerField(db_column='bDistinguishFactionNameColours')
    bdobuildingchecks = models.IntegerField(db_column='bDoBuildingChecks')
    bdropweapons = models.IntegerField(db_column='bDropWeapons')
    bhudshowradarpings = models.IntegerField(db_column='bHUDShowRadarPings')
    bincompletetutorialavailable = models.IntegerField(db_column='bIncompleteTutorialAvailable')
    bminigamesavailable = models.IntegerField(db_column='bMinigamesAvailable')
    bmissionoffers = models.IntegerField(db_column='bMissionOffers')
    bnoskillrating = models.IntegerField(db_column='bNoSkillRating')
    bofferautogroup = models.IntegerField(db_column='bOfferAutoGroup')
    brelease = models.IntegerField(db_column='bRelease')
    bshowthreatandrank = models.IntegerField(db_column='bShowThreatAndRank')
    busemasterspawnzoneonly = models.IntegerField(db_column='bUseMasterSpawnZoneOnly')
    bwscharinfousesradarpings = models.IntegerField(db_column='bWSCharInfoUsesRadarPings')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'DistrictRuleSets'


class Districttypes(models.Model):
    id = models.IntegerField(primary_key=True)
    edistricttype = models.IntegerField(db_column='eDistrictType')
    efactionallowed = models.IntegerField(db_column='eFactionAllowed')
    bissocial = models.IntegerField(db_column='bIsSocial')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'DistrictTypes'


class Districts(models.Model):
    id = models.IntegerField(primary_key=True)
    saudiobanks = models.TextField(db_column='sAudioBanks')
    saudioreflectiondata = models.TextField(db_column='sAudioReflectionData')
    sdescription = models.TextField(db_column='sDescription')
    sdiffusetexture = models.TextField(db_column='sDiffuseTexture')
    sdisplayname = models.TextField(db_column='sDisplayName')
    sdistancefieldtexture = models.TextField(db_column='sDistanceFieldTexture')
    sdistrictmap = models.TextField(db_column='sDistrictMap')
    eawesomeplayerdetectionrules = models.IntegerField(db_column='eAwesomePlayerDetectionRules')
    ecriminalorganisationcontact = models.IntegerField(db_column='eCriminalOrganisationContact')
    edefaultdistrictinstancetype = models.IntegerField(db_column='eDefaultDistrictInstanceType')
    edistrict = models.IntegerField(db_column='eDistrict')
    eenforcerorganisationcontact = models.IntegerField(db_column='eEnforcerOrganisationContact')
    etutorialdistrictinstancetype = models.IntegerField(db_column='eTutorialDistrictInstanceType')
    fmaxsafeheight = models.FloatField(db_column='fMaxSafeHeight')
    fnmaxdistancetopedestriandestroynode = models.FloatField(db_column='fnMaxDistanceToPedestrianDestroyNode')
    fuiinactivitytimeout = models.FloatField(db_column='fUIInactivityTimeout')
    ncentrex = models.IntegerField(db_column='nCentreX')
    ncentrey = models.IntegerField(db_column='nCentreY')
    ndiameter = models.IntegerField(db_column='nDiameter')
    nnumcollectables = models.IntegerField(db_column='nNumCollectables')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    edistricttype = models.IntegerField(db_column='eDistrictType')
    espawnvariable = models.IntegerField(db_column='eSpawnVariable')
    breleasedistrict = models.IntegerField(db_column='bReleaseDistrict')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'Districts'


class Dynamicmenuentries(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplaypicture = models.TextField(db_column='sDisplayPicture')
    sdisplaytext = models.TextField(db_column='sDisplayText')
    slistid = models.TextField(db_column='sListID')
    sremoteevent = models.TextField(db_column='sRemoteEvent')
    swwiseswitch = models.TextField(db_column='sWwiseSwitch')
    edynamicmenuentry = models.IntegerField(db_column='eDynamicMenuEntry')
    ecustomisationmode = models.IntegerField(db_column='eCustomisationMode')
    egender = models.IntegerField(db_column='eGender')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'DynamicMenuEntries'


class Emotecommands(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayname = models.TextField(db_column='sDisplayName')
    spackageref = models.TextField(db_column='sPackageRef')
    sslashcommand = models.TextField(db_column='sSlashCommand')
    eemotecommand = models.IntegerField(db_column='eEmoteCommand')
    bkickcheckenabled = models.IntegerField(db_column='bKickCheckEnabled')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'EmoteCommands'


class Encumbrances(models.Model):
    id = models.IntegerField(primary_key=True)
    nuiencumbrancelevel = models.IntegerField(db_column='nUIEncumbranceLevel')
    eencumbrance = models.IntegerField(db_column='eEncumbrance')
    bcancrouchmove = models.IntegerField(db_column='bCanCrouchMove')
    bcanjump = models.IntegerField(db_column='bCanJump')
    bcanrun = models.IntegerField(db_column='bCanRun')
    bcansprint = models.IntegerField(db_column='bCanSprint')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'Encumbrances'


class Equipmentcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    eequipmentcategory = models.IntegerField(db_column='eEquipmentCategory')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'EquipmentCategories'


class Equipmenttypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    eequipmentcategory = models.IntegerField(db_column='eEquipmentCategory')
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    eitemattachment = models.IntegerField(db_column='eItemAttachment')
    fdurationofuse = models.IntegerField(db_column='fDurationOfUse')
    ngradeordinal = models.IntegerField(db_column='nGradeOrdinal')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'EquipmentTypes'


class Errorcode(models.Model):
    id = models.IntegerField(primary_key=True)
    ndummy = models.IntegerField(db_column='nDummy')
    eerrorcode = models.IntegerField(db_column='eErrorCode')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ErrorCode'


class Explosions(models.Model):
    id = models.IntegerField(primary_key=True)
    saudiotype = models.TextField(db_column='sAudioType')
    svfxasset = models.TextField(db_column='sVFXAsset')
    svfxasset_airburst = models.TextField(db_column='sVFXAsset_Airburst')
    ecamerashake = models.IntegerField(db_column='eCameraShake')
    eexplosion = models.IntegerField(db_column='eExplosion')
    fexplosionradius = models.FloatField(db_column='fExplosionRadius')
    fgroundzeroradius = models.FloatField(db_column='fGroundZeroRadius')
    fharddamagemodifier = models.FloatField(db_column='fHardDamageModifier')
    fimpulsezmax = models.FloatField(db_column='fImpulseZMax')
    fimpulsezmin = models.FloatField(db_column='fImpulseZMin')
    flifetimemaxdamagetime = models.FloatField(db_column='fLifetimeMaxDamageTime')
    flifetimemindamagepercentage = models.FloatField(db_column='fLifetimeMinDamagePercentage')
    fminimumdamagepercentage = models.FloatField(db_column='fMinimumDamagePercentage')
    fragdollradialimpulse = models.FloatField(db_column='fRagdollRadialImpulse')
    fsoftdamagemodifier = models.FloatField(db_column='fSoftDamageModifier')
    ndamage = models.IntegerField(db_column='nDamage')
    nstundamage = models.IntegerField(db_column='nStunDamage')
    enpcworldevent = models.IntegerField(db_column='eNPCWorldEvent')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'Explosions'


class Fxmaterialimpacts(models.Model):
    id = models.IntegerField(primary_key=True)
    sexplosiveimpactvfx = models.TextField(db_column='sExplosiveImpactVFX')
    sheavyexitvfx = models.TextField(db_column='sHeavyExitVFX')
    sheavyfootfallvfx = models.TextField(db_column='sHeavyFootfallVFX')
    sheavyimpactvfx = models.TextField(db_column='sHeavyImpactVFX')
    slightfootfallvfx = models.TextField(db_column='sLightFootfallVFX')
    smaterialdescription = models.TextField(db_column='sMaterialDescription')
    smediumexitvfx = models.TextField(db_column='sMediumExitVFX')
    smediumfootfallvfx = models.TextField(db_column='sMediumFootfallVFX')
    smediumimpactvfx = models.TextField(db_column='sMediumImpactVFX')
    smeleeimpactvfx = models.TextField(db_column='sMeleeImpactVFX')
    snonlethalimpactvfx = models.TextField(db_column='sNonLethalImpactVFX')
    srbcollisionlargevfx = models.TextField(db_column='sRBCollisionLargeVFX')
    srbcollisionsmallvfx = models.TextField(db_column='sRBCollisionSmallVFX')
    srbcollisionvfx = models.TextField(db_column='sRBCollisionVFX')
    srbscrapevfx = models.TextField(db_column='sRBScrapeVFX')
    sshotimpactvfx = models.TextField(db_column='sShotImpactVFX')
    ssmallexitvfx = models.TextField(db_column='sSmallExitVFX')
    ssmallimpactvfx = models.TextField(db_column='sSmallImpactVFX')
    swheelsmokevfx = models.TextField(db_column='sWheelSmokeVFX')
    fhardnesslower = models.FloatField(db_column='fHardnessLower')
    fhardnessupper = models.FloatField(db_column='fHardnessUpper')
    efxmaterialimpact = models.IntegerField(db_column='eFXMaterialImpact')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'FXMaterialImpacts'


class Facialhairrandomgeneration(models.Model):
    id = models.IntegerField(primary_key=True)
    fprobability = models.FloatField(db_column='fProbability')
    efacialhairrandomgeneration = models.IntegerField(db_column='eFacialHairRandomGeneration')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'FacialHairRandomGeneration'


class Factionrestrictedlocations(models.Model):
    id = models.IntegerField(primary_key=True)
    efactionrestrictedlocation = models.IntegerField(db_column='eFactionRestrictedLocation')
    npadding_ignore_me = models.IntegerField(db_column='nPadding_Ignore_Me')
    efaction = models.IntegerField(db_column='eFaction')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'FactionRestrictedLocations'


class Factions(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayname = models.TextField(db_column='sDisplayName')
    sfactioninfodescription = models.TextField(db_column='sFactionInfoDescription')
    sfactioninfodisplayname = models.TextField(db_column='sFactionInfoDisplayName')
    sskinname = models.TextField(db_column='sSkinName')
    espawnzonemarker = models.IntegerField(db_column='eSpawnZoneMarker')
    evolumecolour = models.IntegerField(db_column='eVolumeColour')
    efaction = models.IntegerField(db_column='eFaction')
    sapbdb = models.TextField(db_column='sAPBDB')

    @property_cache
    def name(self):
        return self.sdisplayname

    class Meta:
        managed = False
        db_table = 'Factions'


class Feedbackmessages(models.Model):
    id = models.IntegerField(primary_key=True)
    sfeedbackmessage = models.TextField(db_column='sFeedbackMessage')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    efeedbackmessage = models.IntegerField(db_column='eFeedbackMessage')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'FeedbackMessages'


class Fireoffsets(models.Model):
    id = models.IntegerField(primary_key=True)
    fforwards = models.FloatField(db_column='fForwards')
    fright = models.FloatField(db_column='fRight')
    fup = models.FloatField(db_column='fUp')
    efireoffset = models.IntegerField(db_column='eFireOffset')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'FireOffsets'


class Gameflowdialogs(models.Model):
    id = models.IntegerField(primary_key=True)
    sbutton1label = models.TextField(db_column='sButton1Label')
    sbutton2label = models.TextField(db_column='sButton2Label')
    sbutton3label = models.TextField(db_column='sButton3Label')
    splayerclass = models.TextField(db_column='sPlayerClass')
    stitle = models.TextField(db_column='sTitle')
    ebutton1result = models.IntegerField(db_column='eButton1Result')
    ebutton2result = models.IntegerField(db_column='eButton2Result')
    ebutton3result = models.IntegerField(db_column='eButton3Result')
    ecancelresult = models.IntegerField(db_column='eCancelResult')
    edefaultbutton = models.IntegerField(db_column='eDefaultButton')
    escaleforminterface = models.IntegerField(db_column='eScaleformInterface')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'GameFlowDialogs'


class Gameplayeventcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sactivitymessageparameter4comment = models.TextField(db_column='sActivityMessageParameter4Comment')
    ndummy = models.IntegerField(db_column='nDummy')
    egameplayeventcategory = models.IntegerField(db_column='eGameplayEventCategory')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'GameplayEventCategories'


class Gameplayeventcategories2(models.Model):
    id = models.IntegerField(primary_key=True)
    sactivitymessageparameter4comment = models.TextField(db_column='sActivityMessageParameter4Comment')
    ndummy = models.IntegerField(db_column='nDummy')
    egameplayeventcategory2 = models.IntegerField(db_column='eGameplayEventCategory2')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'GameplayEventCategories2'


class GameplayeventInventoryoperation(models.Model):
    id = models.IntegerField(primary_key=True)
    egameplayevent = models.IntegerField(db_column='eGameplayEvent')
    echildrule = models.IntegerField(db_column='eChildRule')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'GameplayEvent_InventoryOperation'


class GameplayeventMissions(models.Model):
    id = models.IntegerField(primary_key=True)
    echildrule = models.IntegerField(db_column='eChildRule')
    egameplayevent = models.IntegerField(db_column='eGameplayEvent')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'GameplayEvent_Missions'


class GameplayeventTasktargets(models.Model):
    id = models.IntegerField(primary_key=True)
    egameplayevent = models.IntegerField(db_column='eGameplayEvent')
    echildrule = models.IntegerField(db_column='eChildRule')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'GameplayEvent_TaskTargets'


class GameplayeventVehiclehealth(models.Model):
    id = models.IntegerField(primary_key=True)
    egameplayevent = models.IntegerField(db_column='eGameplayEvent')
    echildrule = models.IntegerField(db_column='eChildRule')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'GameplayEvent_VehicleHealth'


class Gameplayevents(models.Model):
    id = models.IntegerField(primary_key=True)
    eactivitymessage_0 = models.IntegerField(db_column='eActivityMessage_0')
    eactivitymessage_1 = models.IntegerField(db_column='eActivityMessage_1')
    eactivitymessage_2 = models.IntegerField(db_column='eActivityMessage_2')
    eactivitymessageonreward = models.IntegerField(db_column='eActivityMessageOnReward')
    edisabledrulesets = models.IntegerField(db_column='eDisabledRuleSets')
    egameplayevent = models.IntegerField(db_column='eGameplayEvent')
    ehelppopup = models.IntegerField(db_column='eHelpPopup')
    emissionsystems = models.IntegerField(db_column='eMissionSystems')
    eobject = models.IntegerField(db_column='eObject')
    eobjectset = models.IntegerField(db_column='eObjectSet')
    eobjectstateset = models.IntegerField(db_column='eObjectStateSet')
    eresultantheatchange = models.IntegerField(db_column='eResultantHeatChange')
    eresultantwitnessablecrime = models.IntegerField(db_column='eResultantWitnessableCrime')
    eresultantwitnessablecrimeend = models.IntegerField(db_column='eResultantWitnessableCrimeEnd')
    etrackedactivity = models.IntegerField(db_column='eTrackedActivity')
    fexpiryperiod = models.FloatField(db_column='fExpiryPeriod')
    na = models.IntegerField(db_column='nA')
    nb = models.IntegerField(db_column='nB')
    nprecedence = models.IntegerField(db_column='nPrecedence')
    ecsa = models.IntegerField(db_column='eCSA')
    eexcludelist = models.IntegerField(db_column='eExcludeList')
    efaction = models.IntegerField(db_column='eFaction')
    egameplayeventcategory = models.IntegerField(db_column='eGameplayEventCategory')
    egameplayeventcategory2 = models.IntegerField(db_column='eGameplayEventCategory2')
    eincludelist = models.IntegerField(db_column='eIncludeList')
    emutuallyexclusive = models.IntegerField(db_column='eMutuallyExclusive')
    epvp = models.IntegerField(db_column='ePvP')
    eresultantreward = models.IntegerField(db_column='eResultantReward')
    brequirea = models.IntegerField(db_column='bRequireA')
    brequireb = models.IntegerField(db_column='bRequireB')
    bresettrackedactivity = models.IntegerField(db_column='bResetTrackedActivity')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'GameplayEvents'


class GameplayeventsModetimer(models.Model):
    id = models.IntegerField(primary_key=True)
    echildrule = models.IntegerField(db_column='eChildRule')
    egameplayevent = models.IntegerField(db_column='eGameplayEvent')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'GameplayEvents_ModeTimer'


class Gameplaymodetimertypes(models.Model):
    id = models.IntegerField(primary_key=True)
    edistrictruleset = models.IntegerField(db_column='eDistrictRuleSet')
    egameplaymodetimertype = models.IntegerField(db_column='eGameplayModeTimerType')
    balive = models.IntegerField(db_column='bAlive')
    bcharactereditor = models.IntegerField(db_column='bCharacterEditor')
    bclothingeditor = models.IntegerField(db_column='bClothingEditor')
    bdirectedmission = models.IntegerField(db_column='bDirectedMission')
    bmaxheat = models.IntegerField(db_column='bMaxHeat')
    bmusiceditor = models.IntegerField(db_column='bMusicEditor')
    bnotineditor = models.IntegerField(db_column='bNotInEditor')
    botherpvp = models.IntegerField(db_column='bOtherPvP')
    bsymboleditor = models.IntegerField(db_column='bSymbolEditor')
    btotal = models.IntegerField(db_column='bTotal')
    bvehicleeditor = models.IntegerField(db_column='bVehicleEditor')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'GameplayModeTimerTypes'


class Gameplayobjectsets(models.Model):
    id = models.IntegerField(primary_key=True)
    egameplayobjectset = models.IntegerField(db_column='eGameplayObjectSet')
    ndummy = models.IntegerField()
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'GameplayObjectSets'


class Gameplayobjects(models.Model):
    id = models.IntegerField(primary_key=True)
    egameplayobject = models.IntegerField(db_column='eGameplayObject')
    ememberof_0 = models.IntegerField(db_column='eMemberOf_0')
    ememberof_1 = models.IntegerField(db_column='eMemberOf_1')
    ememberof_2 = models.IntegerField(db_column='eMemberOf_2')
    ememberof_3 = models.IntegerField(db_column='eMemberOf_3')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'GameplayObjects'


class Gameplayobjectsfixed(models.Model):
    id = models.IntegerField(primary_key=True)
    egameplayobject = models.IntegerField(db_column='eGameplayObject')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'GameplayObjectsFixed'


class Gameplaystatesets(models.Model):
    id = models.IntegerField(primary_key=True)
    egameplaystateset = models.IntegerField(db_column='eGameplayStateSet')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'GameplayStateSets'


class Gameplaystates(models.Model):
    id = models.IntegerField(primary_key=True)
    ememberof_0 = models.IntegerField(db_column='eMemberOf_0')
    ememberof_1 = models.IntegerField(db_column='eMemberOf_1')
    ememberof_2 = models.IntegerField(db_column='eMemberOf_2')
    ememberof_3 = models.IntegerField(db_column='eMemberOf_3')
    egameplaystate = models.IntegerField(db_column='eGameplayState')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'GameplayStates'


class Gameplayvehiclehealthranges(models.Model):
    id = models.IntegerField(primary_key=True)
    nhealthmax = models.IntegerField(db_column='nHealthMax')
    nhealthmin = models.IntegerField(db_column='nHealthMin')
    egameplayvehiclehealthrange = models.IntegerField(db_column='eGameplayVehicleHealthRange')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'GameplayVehicleHealthRanges'


class Golempartclasses(models.Model):
    id = models.IntegerField(primary_key=True)
    egolempartclass = models.IntegerField(db_column='eGolemPartClass')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    bcoversbreasts = models.IntegerField(db_column='bCoversBreasts')
    bcoversgenitalia = models.IntegerField(db_column='bCoversGenitalia')
    buseinclothingpreview = models.IntegerField(db_column='bUseInClothingPreview')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'GolemPartClasses'


class Golemparts(models.Model):
    id = models.IntegerField(primary_key=True)
    sgolempart = models.TextField(db_column='sGolemPart')
    susername = models.TextField(db_column='sUsername')
    eclass = models.IntegerField(db_column='eClass')
    eclothingitemcategory = models.IntegerField(db_column='eClothingItemCategory')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    nversatility = models.IntegerField(db_column='nVersatility')
    bstartup = models.IntegerField(db_column='bStartup')
    btestasset = models.IntegerField(db_column='bTestAsset')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'GolemParts'


class Graffitidisplaypoint(models.Model):
    id = models.IntegerField(primary_key=True)
    edisplaypoint = models.IntegerField(db_column='eDisplayPoint')
    fspraydurationoverride = models.FloatField(db_column='fSprayDurationOverride')
    einteractiontype = models.IntegerField(db_column='eInteractionType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'GraffitiDisplayPoint'


class Grenadeweapontype(models.Model):
    id = models.IntegerField(primary_key=True)
    erecoil = models.IntegerField(db_column='eRecoil')
    eweaponprojectile = models.IntegerField(db_column='eWeaponProjectile')
    eweapontype = models.IntegerField(db_column='eWeaponType')
    ffiringspeed = models.FloatField(db_column='fFiringSpeed')
    fmaxangleadded = models.FloatField(db_column='fMaxAngleAdded')
    fpinpulltime = models.FloatField(db_column='fPinPullTime')
    fthrowtime = models.FloatField(db_column='fThrowTime')
    baffectedbygravity = models.IntegerField(db_column='bAffectedByGravity')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'GrenadeWeaponType'


class Hudceremonymsg(models.Model):
    id = models.IntegerField(primary_key=True)
    stitle = models.TextField(db_column='sTitle')
    ehudmessage = models.IntegerField(db_column='eHUDMessage')
    eiconfallback = models.IntegerField(db_column='eIconFallback')
    etitlebgcolour = models.IntegerField(db_column='eTitleBGColour')
    etype = models.IntegerField(db_column='eType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDCeremonyMsg'


class Hudcolour(models.Model):
    id = models.IntegerField(primary_key=True)
    ehudcolour = models.IntegerField(db_column='eHUDColour')
    eoverridecolour = models.IntegerField(db_column='eOverrideColour')
    na = models.IntegerField(db_column='nA')
    nb = models.IntegerField(db_column='nB')
    ng = models.IntegerField(db_column='nG')
    nr = models.IntegerField(db_column='nR')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDColour'


class Hudcolourprofiles(models.Model):
    id = models.IntegerField(primary_key=True)
    ehudcolourprofile = models.IntegerField(db_column='eHUDColourProfile')
    eprimarycolour = models.IntegerField(db_column='ePrimaryColour')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDColourProfiles'


class Hudcombatmessages(models.Model):
    id = models.IntegerField(primary_key=True)
    sline0 = models.TextField(db_column='sLine0')
    sline1 = models.TextField(db_column='sLine1')
    sline2 = models.TextField(db_column='sLine2')
    ehudmessage = models.IntegerField(db_column='eHUDMessage')
    eicon = models.IntegerField(db_column='eIcon')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDCombatMessages'


class Hudconstantbools(models.Model):
    id = models.IntegerField(primary_key=True)
    scomment = models.TextField(db_column='sComment')
    ehudconstantbool = models.IntegerField(db_column='eHUDConstantBool')
    bvalue = models.IntegerField(db_column='bValue')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDConstantBools'


class Hudconstantstring(models.Model):
    id = models.IntegerField(primary_key=True)
    scomment = models.TextField(db_column='sComment')
    stext = models.TextField(db_column='sText')
    ehudconstantstring = models.IntegerField(db_column='eHUDConstantString')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDConstantString'


class Hudconstants(models.Model):
    id = models.IntegerField(primary_key=True)
    scomment = models.TextField(db_column='sComment')
    fvalue = models.FloatField(db_column='fValue')
    ehudconstant = models.IntegerField(db_column='eHUDConstant')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDConstants'


class Huddistrictmapmarker(models.Model):
    id = models.IntegerField(primary_key=True)
    slegendname = models.TextField(db_column='sLegendName')
    ehuddistrictmapmarker = models.IntegerField(db_column='eHUDDistrictMapMarker')
    eiconcombo = models.IntegerField(db_column='eIconCombo')
    fmaxvisibledistance = models.FloatField(db_column='fMaxVisibleDistance')
    ndraworder = models.IntegerField(db_column='nDrawOrder')
    nsize = models.IntegerField(db_column='nSize')
    bdisablewaypoints = models.IntegerField(db_column='bDisableWaypoints')
    binlegend = models.IntegerField(db_column='bInLegend')
    binteractonmap = models.IntegerField(db_column='bInteractOnMap')
    bisaesthetic = models.IntegerField(db_column='bIsAesthetic')
    bshowonelectivespawnmap = models.IntegerField(db_column='bShowOnElectiveSpawnMap')
    bshowonspawnmap = models.IntegerField(db_column='bShowOnSpawnMap')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDDistrictMapMarker'


class Hudeffects(models.Model):
    id = models.IntegerField(primary_key=True)
    smaterialref = models.TextField(db_column='sMaterialRef')
    ehudeffect = models.IntegerField(db_column='eHUDEffect')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDEffects'


class Hudiconcombos(models.Model):
    id = models.IntegerField(primary_key=True)
    ehudiconcombo = models.IntegerField(db_column='eHUDIconCombo')
    elayer1 = models.IntegerField(db_column='eLayer1')
    elayer2 = models.IntegerField(db_column='eLayer2')
    elayer3 = models.IntegerField(db_column='eLayer3')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDIconCombos'


class Hudicons(models.Model):
    id = models.IntegerField(primary_key=True)
    ehudicon = models.IntegerField(db_column='eHUDIcon')
    niconcolumn = models.IntegerField(db_column='nIconColumn')
    niconrow = models.IntegerField(db_column='nIconRow')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDIcons'


class Hudinfobrowsers(models.Model):
    id = models.IntegerField(primary_key=True)
    spackageref = models.TextField(db_column='sPackageRef')
    ehudinfobrowser = models.IntegerField(db_column='eHUDInfoBrowser')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDInfoBrowsers'


class Hudmarkeroffset(models.Model):
    id = models.IntegerField(primary_key=True)
    ehudmarkeroffset = models.IntegerField(db_column='eHUDMarkerOffset')
    foffset_x = models.FloatField(db_column='fOffset_X')
    foffset_y = models.FloatField(db_column='fOffset_Y')
    foffset_z = models.FloatField(db_column='fOffset_Z')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDMarkerOffset'


class Hudmarkerstatecolours(models.Model):
    id = models.IntegerField(primary_key=True)
    edefault = models.IntegerField(db_column='eDefault')
    ehudmarkerstatecolour = models.IntegerField(db_column='eHUDMarkerStateColour')
    etask_neutral = models.IntegerField(db_column='eTask_Neutral')
    etask_oppositionattack = models.IntegerField(db_column='eTask_OppositionAttack')
    etask_oppositiondefend = models.IntegerField(db_column='eTask_OppositionDefend')
    etask_ownerattack = models.IntegerField(db_column='eTask_OwnerAttack')
    etask_ownerdefend = models.IntegerField(db_column='eTask_OwnerDefend')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDMarkerStateColours'


class Hudmarkerstates(models.Model):
    id = models.IntegerField(primary_key=True)
    fupdatedelay = models.FloatField(db_column='fUpdateDelay')
    ehudmarkerstate = models.IntegerField(db_column='eHUDMarkerState')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDMarkerStates'


class Hudmarkervisual(models.Model):
    id = models.IntegerField(primary_key=True)
    ecolourprofile = models.IntegerField(db_column='eColourProfile')
    edistrictmapmarker = models.IntegerField(db_column='eDistrictMapMarker')
    ehudmarkeroffset = models.IntegerField(db_column='eHUDMarkerOffset')
    ehudmarkervisual = models.IntegerField(db_column='eHUDMarkerVisual')
    eradarmarker = models.IntegerField(db_column='eRadarMarker')
    etaskmarker = models.IntegerField(db_column='eTaskMarker')
    ecategory = models.IntegerField(db_column='eCategory')
    bcontainsplayerdata = models.IntegerField(db_column='bContainsPlayerData')
    bpreventpawnvisibilitychecks = models.IntegerField(db_column='bPreventPawnVisibilityChecks')
    buseindividualstate = models.IntegerField(db_column='bUseIndividualState')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDMarkerVisual'


class Hudmarkervisualtext(models.Model):
    id = models.IntegerField(primary_key=True)
    sneutral = models.TextField(db_column='sNeutral')
    soppositionattack = models.TextField(db_column='sOppositionAttack')
    soppositiondefend = models.TextField(db_column='sOppositionDefend')
    sownerattack = models.TextField(db_column='sOwnerAttack')
    sownerdefend = models.TextField(db_column='sOwnerDefend')
    ehudmarkervisual = models.IntegerField(db_column='eHUDMarkerVisual')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDMarkerVisualText'


class Hudmessagecategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplaytext = models.TextField(db_column='sDisplayText')
    ehudmessagecategory = models.IntegerField(db_column='eHUDMessageCategory')
    eicon = models.IntegerField(db_column='eIcon')
    echatcategory = models.IntegerField(db_column='eChatCategory')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDMessageCategories'


class Hudmessageposition(models.Model):
    id = models.IntegerField(primary_key=True)
    ehudmessageposition = models.IntegerField(db_column='eHUDMessagePosition')
    fypercent = models.FloatField(db_column='fYPercent')
    nyoffset = models.IntegerField(db_column='nYOffset')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDMessagePosition'


class Hudmessagescenes(models.Model):
    id = models.IntegerField(primary_key=True)
    spackageref = models.TextField(db_column='sPackageRef')
    ehudmessagescene = models.IntegerField(db_column='eHUDMessageScene')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDMessageScenes'


class Hudmessages(models.Model):
    id = models.IntegerField(primary_key=True)
    saudiocue = models.TextField(db_column='sAudioCue')
    schattext = models.TextField(db_column='sChatText')
    sdisplaytext = models.TextField(db_column='sDisplayText')
    sfemaletext = models.TextField(db_column='sFemaleText')
    ecategory = models.IntegerField(db_column='eCategory')
    ehudmessage = models.IntegerField(db_column='eHUDMessage')
    enextmessage = models.IntegerField(db_column='eNextMessage')
    epopupdialogoverride = models.IntegerField(db_column='ePopupDialogOverride')
    eposition = models.IntegerField(db_column='ePosition')
    escene = models.IntegerField(db_column='eScene')
    euistyle = models.IntegerField(db_column='eUIStyle')
    fdisplaytime = models.FloatField(db_column='fDisplayTime')
    fqueuetimeout = models.FloatField(db_column='fQueueTimeout')
    epriority = models.IntegerField(db_column='ePriority')
    ballowmultiples = models.IntegerField(db_column='bAllowMultiples')
    bforaction = models.IntegerField(db_column='bForAction')
    bforceremony = models.IntegerField(db_column='bForCeremony')
    bforchat = models.IntegerField(db_column='bForChat')
    bforcombat = models.IntegerField(db_column='bForCombat')
    bfordistrictmap = models.IntegerField(db_column='bForDistrictMap')
    bsuppressmain = models.IntegerField(db_column='bSuppressMain')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDMessages'


class Hudpopupmenuitems(models.Model):
    id = models.IntegerField(primary_key=True)
    sconsolecommand = models.TextField(db_column='sConsoleCommand')
    skeypress = models.TextField(db_column='sKeyPress')
    slocalisationtext = models.TextField(db_column='sLocalisationText')
    ehudpopupmenuitem = models.IntegerField(db_column='eHUDPopUpMenuItem')
    eimage = models.IntegerField(db_column='eImage')
    eenabledrule = models.IntegerField(db_column='eEnabledRule')
    bdisplaykeybinding = models.IntegerField(db_column='bDisplayKeyBinding')
    benablewhendead = models.IntegerField(db_column='bEnableWhenDead')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDPopUpMenuItems'


class Hudradarmarkers(models.Model):
    id = models.IntegerField(primary_key=True)
    ehudradarmarker = models.IntegerField(db_column='eHUDRadarMarker')
    eicon = models.IntegerField(db_column='eIcon')
    eiconsurround = models.IntegerField(db_column='eIconSurround')
    niconsize = models.IntegerField(db_column='nIconSize')
    niconsurroundsize = models.IntegerField(db_column='nIconSurroundSize')
    bshowonelectivespawnmap = models.IntegerField(db_column='bShowOnElectiveSpawnMap')
    bvalidinmission = models.IntegerField(db_column='bValidInMission')
    bvalidoutofmission = models.IntegerField(db_column='bValidOutOfMission')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDRadarMarkers'


class Hudreticulehinticons(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplaytext = models.TextField(db_column='sDisplayText')
    ecolour = models.IntegerField(db_column='eColour')
    ehudreticulehinticon = models.IntegerField(db_column='eHUDReticuleHintIcon')
    eicon = models.IntegerField(db_column='eIcon')
    fmaxdistance = models.FloatField(db_column='fMaxDistance')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDReticuleHintIcons'


class Hudreticules(models.Model):
    id = models.IntegerField(primary_key=True)
    spackageref = models.TextField(db_column='sPackageRef')
    ecolourdefault = models.IntegerField(db_column='eColourDefault')
    ecolourenemy = models.IntegerField(db_column='eColourEnemy')
    ecolourfriend = models.IntegerField(db_column='eColourFriend')
    ehudreticule = models.IntegerField(db_column='eHUDReticule')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDReticules'


class Hudscenes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdatastoretag = models.TextField(db_column='sDataStoreTag')
    spackageref = models.TextField(db_column='sPackageRef')
    ehudscenes = models.IntegerField(db_column='eHUDScenes')
    bopeninloginlevel = models.IntegerField(db_column='bOpenInLoginLevel')
    bstarthidden = models.IntegerField(db_column='bStartHidden')
    bupdatewhiledead = models.IntegerField(db_column='bUpdateWhileDead')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDScenes'


class Hudtaskmarkerscenes(models.Model):
    id = models.IntegerField(primary_key=True)
    spackageref = models.TextField(db_column='sPackageRef')
    ehudtaskmarkerscene = models.IntegerField(db_column='eHUDTaskMarkerScene')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDTaskMarkerScenes'


class Hudtaskmarkers(models.Model):
    id = models.IntegerField(primary_key=True)
    earrowicon = models.IntegerField(db_column='eArrowIcon')
    earrowiconellipse = models.IntegerField(db_column='eArrowIconEllipse')
    earrowiconocc = models.IntegerField(db_column='eArrowIconOcc')
    eellipseicon = models.IntegerField(db_column='eEllipseIcon')
    ehudtaskmarker = models.IntegerField(db_column='eHUDTaskMarker')
    eoccludedicon = models.IntegerField(db_column='eOccludedIcon')
    escene = models.IntegerField(db_column='eScene')
    evisibleicon = models.IntegerField(db_column='eVisibleIcon')
    fmaxvisibledistance = models.FloatField(db_column='fMaxVisibleDistance')
    npriority = models.IntegerField(db_column='nPriority')
    bhidedistance = models.IntegerField(db_column='bHideDistance')
    bhidewhenoccluded = models.IntegerField(db_column='bHideWhenOccluded')
    binteractondistrictmap = models.IntegerField(db_column='bInteractOnDistrictMap')
    bshowbydefault = models.IntegerField(db_column='bShowByDefault')
    bshowinworld = models.IntegerField(db_column='bShowInWorld')
    bshowonedge = models.IntegerField(db_column='bShowOnEdge')
    bshowonself = models.IntegerField(db_column='bShowOnSelf')
    bvalidinmission = models.IntegerField(db_column='bValidInMission')
    bvalidoutofmission = models.IntegerField(db_column='bValidOutOfMission')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDTaskMarkers'


class Hudtextureicons(models.Model):
    id = models.IntegerField(primary_key=True)
    siconsetname = models.TextField(db_column='sIconSetName')
    smoviename = models.TextField(db_column='sMovieName')
    spackageref = models.TextField(db_column='sPackageRef')
    ehudtextureicon = models.IntegerField(db_column='eHUDTextureIcon')
    etexturepageicon = models.IntegerField(db_column='eTexturePageIcon')
    nframenumber = models.IntegerField(db_column='nFrameNumber')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDTextureIcons'


class Hudtexturepage(models.Model):
    id = models.IntegerField(primary_key=True)
    spackagename = models.TextField(db_column='sPackageName')
    ehudtexturepage = models.IntegerField(db_column='eHUDTexturePage')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDTexturePage'


class Hudtexturepageicon(models.Model):
    id = models.IntegerField(primary_key=True)
    ehudtexturepageicon = models.IntegerField(db_column='eHUDTexturePageIcon')
    etexturepage = models.IntegerField(db_column='eTexturePage')
    nu = models.IntegerField(db_column='nU')
    nul = models.IntegerField(db_column='nUL')
    nv = models.IntegerField(db_column='nV')
    nvl = models.IntegerField(db_column='nVL')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDTexturePageIcon'


class HudusablesDisplaysettings(models.Model):
    id = models.IntegerField(primary_key=True)
    eiconcolour = models.IntegerField(db_column='eIconColour')
    fbackgroundopacity = models.FloatField(db_column='fBackgroundOpacity')
    ftextbackgroundopacity = models.FloatField(db_column='fTextBackgroundOpacity')
    ehudusables_displaysetting = models.IntegerField(db_column='eHUDUsables_DisplaySetting')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDUsables_DisplaySettings'


class Hudwscharinfos(models.Model):
    id = models.IntegerField(primary_key=True)
    ecolourprofile = models.IntegerField(db_column='eColourProfile')
    ehudwscharinfo = models.IntegerField(db_column='eHUDWSCharInfo')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDWSCharInfos'


class Hudzonenotifier(models.Model):
    id = models.IntegerField(primary_key=True)
    eicon = models.IntegerField(db_column='eIcon')
    ehudzonenotifier = models.IntegerField(db_column='eHUDZoneNotifier')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HUDZoneNotifier'


class Heatactionaffects(models.Model):
    id = models.IntegerField(primary_key=True)
    eheatactionaffect = models.IntegerField(db_column='eHeatActionAffect')
    enotorietyeffect = models.IntegerField(db_column='eNotorietyEffect')
    eprestigeeffect = models.IntegerField(db_column='ePrestigeEffect')
    fescapepenaltytimer = models.FloatField(db_column='fEscapePenaltyTimer')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HeatActionAffects'


class Heatconstants(models.Model):
    id = models.IntegerField(primary_key=True)
    scomment = models.TextField(db_column='sComment')
    fcriminalvalue = models.FloatField(db_column='fCriminalValue')
    fenforcervalue = models.FloatField(db_column='fEnforcerValue')
    eheatconstant = models.IntegerField(db_column='eHeatConstant')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HeatConstants'


class Heatlevels(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    eheatlevel = models.IntegerField(db_column='eHeatLevel')
    ehudtexture = models.IntegerField(db_column='eHUDTexture')
    frewardmultiplier = models.FloatField(db_column='fRewardMultiplier')
    fthreshold = models.FloatField(db_column='fThreshold')
    nlevel = models.IntegerField(db_column='nLevel')
    bbreakscontactpledges = models.IntegerField(db_column='bBreaksContactPledges')
    bdispatchbounty = models.IntegerField(db_column='bDispatchBounty')
    bdispatchmission = models.IntegerField(db_column='bDispatchMission')
    bpvpunlockedtoallopposingfaction = models.IntegerField(db_column='bPVPUnlockedToAllOpposingFaction')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HeatLevels'


class Hostingconfigfiles(models.Model):
    id = models.IntegerField(primary_key=True)
    sfilename = models.TextField(db_column='sFilename')
    npersistentid = models.IntegerField(db_column='nPersistentId')
    ehostingconfigfile = models.IntegerField(db_column='eHostingConfigFile')
    etype = models.IntegerField(db_column='eType')
    bpersistent = models.IntegerField(db_column='bPersistent')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HostingConfigFiles'


class Hudgroupstates(models.Model):
    id = models.IntegerField(primary_key=True)
    sheadertext = models.TextField(db_column='sHeaderText')
    eheadercolour = models.IntegerField(db_column='eHeaderColour')
    eheadericon = models.IntegerField(db_column='eHeaderIcon')
    ehudgroupstate = models.IntegerField(db_column='eHudGroupState')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'HudGroupStates'


class Instrumentitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sresource = models.TextField(db_column='sResource')
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'InstrumentItemTypes'


class Interactiveactortype(models.Model):
    id = models.IntegerField(primary_key=True)
    dummy = models.FloatField(db_column='Dummy')
    einteractiveactorcategory = models.IntegerField(db_column='eInteractiveActorCategory')
    einteractiveactortype = models.IntegerField(db_column='eInteractiveActorType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'InteractiveActorType'


class Intraactivityrewards(models.Model):
    id = models.IntegerField(primary_key=True)
    fpercentagelosspercapture = models.FloatField(db_column='fPercentageLossPerCapture')
    ncash_0 = models.IntegerField(db_column='nCash_0')
    ncash_1 = models.IntegerField(db_column='nCash_1')
    ncontactstanding_0 = models.IntegerField(db_column='nContactStanding_0')
    ncontactstanding_1 = models.IntegerField(db_column='nContactStanding_1')
    nminimumpointsvalue = models.IntegerField(db_column='nMinimumPointsValue')
    nscore = models.IntegerField(db_column='nScore')
    eintraactivityreward = models.IntegerField(db_column='eIntraActivityReward')
    escorecategory = models.IntegerField(db_column='eScoreCategory')
    baddtoopenworldcashpool = models.IntegerField(db_column='bAddToOpenWorldCashPool')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'IntraActivityRewards'


class Inventoryitemcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    sdisplayname = models.TextField(db_column='sDisplayName')
    stablename = models.TextField(db_column='sTableName')
    nbytesize = models.IntegerField(db_column='nByteSize')
    nbytesizeui = models.IntegerField(db_column='nByteSizeUI')
    ninitialstoragespace = models.IntegerField(db_column='nInitialStorageSpace')
    nmaxstoragespace = models.IntegerField(db_column='nMaxStorageSpace')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    einventoryitemcategory = models.IntegerField(db_column='eInventoryItemCategory')
    bcopyable = models.IntegerField(db_column='bCopyable')
    bcreatorwaivesrating = models.IntegerField(db_column='bCreatorWaivesRating')
    bmarketplacesearch = models.IntegerField(db_column='bMarketplaceSearch')
    brenamable = models.IntegerField(db_column='bRenamable')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'InventoryItemCategories'


class Inventoryitemcategorylimited(models.Model):
    id = models.IntegerField(primary_key=True)
    fcustomisationreplenishperiod = models.FloatField(db_column='fCustomisationReplenishPeriod')
    ncustomisationinitialavailability = models.IntegerField(db_column='nCustomisationInitialAvailability')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    einventoryitemcategory = models.IntegerField(db_column='eInventoryItemCategory')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'InventoryItemCategoryLimited'


class Inventoryiteminfracategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    sdisplayname = models.TextField(db_column='sDisplayName')
    sidentifier = models.TextField(db_column='sIdentifier')
    ssingularname = models.TextField(db_column='sSingularName')
    einventoryiteminfracategory = models.IntegerField(db_column='eInventoryItemInfraCategory')
    ninitialavail = models.IntegerField(db_column='nInitialAvail')
    ninitialrate = models.IntegerField(db_column='nInitialRate')
    nmaxavail = models.IntegerField(db_column='nMaxAvail')
    nmaxrate = models.IntegerField(db_column='nMaxRate')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    esubcategory = models.ForeignKey('Inventoryitemsubcategories', db_column='eSubCategory')
    bispublished = models.IntegerField(db_column='bIsPublished')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'InventoryItemInfraCategories'


class Inventoryitemleases(models.Model):
    id = models.IntegerField(primary_key=True)
    einventoryitemlease = models.IntegerField(db_column='eInventoryItemLease')
    fcostapbcashmultiplier = models.FloatField(db_column='fCostAPBCashMultiplier')
    fexpirytime = models.FloatField(db_column='fExpiryTime')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'InventoryItemLeases'


class Inventoryitemsubcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    sdisplayname = models.TextField(db_column='sDisplayName')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    ecategory = models.ForeignKey('Inventoryitemcategories', db_column='eCategory')
    einventoryitemsubcategory = models.IntegerField(db_column='eInventoryItemSubCategory')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'InventoryItemSubCategories'


class Inventoryitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    screatorname = models.TextField(db_column='sCreatorName')
    sdisplayname = models.TextField(db_column='sDisplayName')
    ehudimage = models.ForeignKey('Hudtextureicons', db_column='eHUDImage')
    einfracategory = models.ForeignKey('Inventoryiteminfracategories', db_column='eInfraCategory')
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    elease = models.ForeignKey('Inventoryitemleases', db_column='eLease')
    eunlock = models.ForeignKey('Inventoryitemtypes', db_column='eUnlock')
    narmascategoryid = models.IntegerField(db_column='nArmasCategoryID')
    narmasproductid = models.IntegerField(db_column='nArmasProductID')
    narmassubcategoryid = models.IntegerField(db_column='nArmasSubcategoryID')
    ncostapbcash = models.IntegerField(db_column='nCostAPBCash')
    ncostrewardtokens = models.IntegerField(db_column='nCostRewardTokens')
    nminrating = models.IntegerField(db_column='nMinRating')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    eorganisation = models.ForeignKey('Organisations', db_column='eOrganisation')
    etrade = models.IntegerField(db_column='eTrade')
    bcansellback = models.IntegerField(db_column='bCanSellback')
    bcriminal = models.IntegerField(db_column='bCriminal')
    benforcer = models.IntegerField(db_column='bEnforcer')
    bgifted = models.IntegerField(db_column='bGifted')
    bignoresddvalidation = models.IntegerField(db_column='bIgnoreSddValidation')
    bisarmas = models.IntegerField(db_column='bIsArmas')
    bispublished = models.IntegerField(db_column='bIsPublished')
    bnodelete = models.IntegerField(db_column='bNoDelete')
    sapbdb = models.TextField(db_column='sAPBDB')

    @property_cache
    def category(self):
        return self.einfracategory.esubcategory.ecategory

    @property_cache
    def type(self):
        table_prefix = self.category().stablename
        table_prefix = table_prefix.replace('Packate', 'Package')
        table_name = table_prefix.lower().capitalize()+'s'

        if table_name not in LocalModels:
            return None

        _table = LocalModels[table_name]
        _type = _table.objects.get(einventoryitemtype=self)

        return _type

    @property_cache
    def unlocked(self):
        item = self

        if self.category().sapbdb == 'Unlock':
            item = self.type().eunlockitem
            if item.pk == 0:
                item = self

        return item

    class Meta:
        managed = False
        db_table = 'InventoryItemTypes'


class Invokedcontextsensitiveaction(models.Model):
    id = models.IntegerField(primary_key=True)
    fduration = models.FloatField(db_column='fDuration')
    econtextsensitiveaction = models.IntegerField(db_column='eContextSensitiveAction')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'InvokedContextSensitiveAction'


class Itemattachmentvisual(models.Model):
    id = models.IntegerField(primary_key=True)
    sanimsetasset = models.TextField(db_column='sAnimSetAsset')
    sanimtreeasset = models.TextField(db_column='sAnimTreeAsset')
    sattachmentasset = models.TextField(db_column='sAttachmentAsset')
    sattachmentclass = models.TextField(db_column='sAttachmentClass')
    saudiotype = models.TextField(db_column='sAudioType')
    sphysicsasset = models.TextField(db_column='sPhysicsAsset')
    eanimtreedecision = models.IntegerField(db_column='eAnimTreeDecision')
    eitemattachmentvisual = models.IntegerField(db_column='eItemAttachmentVisual')
    euimeshviewersetup = models.IntegerField(db_column='eUIMeshViewerSetup')
    euimeshviewersetup_inventory = models.IntegerField(db_column='eUIMeshViewerSetup_Inventory')
    etaskitemanimationtype = models.IntegerField(db_column='eTaskItemAnimationType')
    blefthandikbydefault = models.IntegerField(db_column='bLeftHandIKByDefault')
    blefthandikwhileaiming = models.IntegerField(db_column='bLeftHandIKWhileAiming')
    bsuppressrunanimation = models.IntegerField(db_column='bSuppressRunAnimation')
    bsuppresssprintanimation = models.IntegerField(db_column='bSuppressSprintAnimation')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ItemAttachmentVisual'


class Itemattachmentvisualdamagestates(models.Model):
    id = models.IntegerField(primary_key=True)
    sassetname = models.TextField(db_column='sAssetName')
    sdamagesfx = models.TextField(db_column='sDamageSFX')
    sdamagevfx = models.TextField(db_column='sDamageVFX')
    srecoversfx = models.TextField(db_column='sRecoverSFX')
    srecovervfx = models.TextField(db_column='sRecoverVFX')
    edamageableattachmentvisual = models.IntegerField(db_column='eDamageableAttachmentVisual')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ItemAttachmentVisualDamageStates'


class Loadingmovieaudiobanks(models.Model):
    id = models.IntegerField(primary_key=True)
    nbankend = models.IntegerField(db_column='nBankEnd')
    nbankstart = models.IntegerField(db_column='nBankStart')
    eloadingmovieaudiobanks = models.IntegerField(db_column='eLoadingMovieAudioBanks')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'LoadingMovieAudioBanks'


class Loadingmovieconfigs(models.Model):
    id = models.IntegerField(primary_key=True)
    sloadingmovie = models.TextField(db_column='sLoadingMovie')
    suiscene = models.TextField(db_column='sUIScene')
    edistrict = models.IntegerField(db_column='eDistrict')
    eloadingmovieconfig = models.IntegerField(db_column='eLoadingMovieConfig')
    nnumaudiotracks = models.IntegerField(db_column='nNumAudioTracks')
    nnumberofpages = models.IntegerField(db_column='nNumberOfPages')
    npagelength = models.IntegerField(db_column='nPageLength')
    etransitiontype = models.IntegerField(db_column='eTransitionType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'LoadingMovieConfigs'


class Loadingmovietips(models.Model):
    id = models.IntegerField(primary_key=True)
    smessage = models.TextField(db_column='sMessage')
    eloadingmovietip = models.IntegerField(db_column='eLoadingMovieTip')
    nmaximumrating = models.IntegerField(db_column='nMaximumRating')
    nminimumrating = models.IntegerField(db_column='nMinimumRating')
    edistrictrestriction = models.IntegerField(db_column='eDistrictRestriction')
    efaction = models.IntegerField(db_column='eFaction')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'LoadingMovieTips'


class Localetypepriorities(models.Model):
    id = models.IntegerField(primary_key=True)
    npriority = models.IntegerField(db_column='nPriority')
    elocaletypepriority = models.IntegerField(db_column='eLocaleTypePriority')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'LocaleTypePriorities'


class Locationbeaconinstances(models.Model):
    id = models.IntegerField(primary_key=True)
    slocalisedname = models.TextField(db_column='sLocalisedName')
    edistrict = models.IntegerField(db_column='eDistrict')
    elocationbeaconinstance = models.IntegerField(db_column='eLocationBeaconInstance')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'LocationBeaconInstances'


class Locationbeacons(models.Model):
    id = models.IntegerField(primary_key=True)
    elocationbeacon = models.IntegerField(db_column='eLocationBeacon')
    fradius = models.FloatField(db_column='fRadius')
    nheight = models.IntegerField(db_column='nHeight')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'LocationBeacons'


class Mailconstants(models.Model):
    id = models.IntegerField(primary_key=True)
    nvalue = models.IntegerField(db_column='nValue')
    emailconstant = models.IntegerField(db_column='eMailConstant')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MailConstants'


class Maildurations(models.Model):
    id = models.IntegerField(primary_key=True)
    nminutes = models.IntegerField(db_column='nMinutes')
    emailduration = models.IntegerField(db_column='eMailDuration')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MailDurations'


class Marketplacecashtype(models.Model):
    id = models.IntegerField(primary_key=True)
    sresource = models.TextField(db_column='sResource')
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MarketplaceCashType'


class Marketplaceconstants(models.Model):
    id = models.IntegerField(primary_key=True)
    fvalue = models.FloatField(db_column='fValue')
    emarketplaceconstant = models.IntegerField(db_column='eMarketplaceConstant')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MarketplaceConstants'


class Marketplacedurations(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplaystring = models.TextField(db_column='sDisplayString')
    nminutes = models.IntegerField(db_column='nMinutes')
    emarketplaceduration = models.IntegerField(db_column='eMarketplaceDuration')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MarketplaceDurations'


class Marketplacetimeleft(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplaystring = models.TextField(db_column='sDisplayString')
    nminutes = models.IntegerField(db_column='nMinutes')
    emarketplacetimeleft = models.IntegerField(db_column='eMarketplaceTimeLeft')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MarketplaceTimeLeft'


class Medalcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    emedalcategory = models.IntegerField(db_column='eMedalCategory')
    bexclusivemedal = models.IntegerField(db_column='bExclusiveMedal')
    bimmediateaward = models.IntegerField(db_column='bImmediateAward')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MedalCategories'


class Medals(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    stitle = models.TextField(db_column='sTitle')
    elargemedalicon = models.IntegerField(db_column='eLargeMedalIcon')
    emedal = models.IntegerField(db_column='eMedal')
    emedalicon = models.IntegerField(db_column='eMedalIcon')
    eshowcasetrackedactivity = models.IntegerField(db_column='eShowcaseTrackedActivity')
    nclassificationordinal = models.IntegerField(db_column='nClassificationOrdinal')
    nparamx = models.IntegerField(db_column='nParamX')
    nparamy = models.IntegerField(db_column='nParamY')
    nscore = models.IntegerField(db_column='nScore')
    nshowcaseorder = models.IntegerField(db_column='nShowcaseOrder')
    emedalcategory = models.IntegerField(db_column='eMedalCategory')
    escorecategory = models.IntegerField(db_column='eScoreCategory')
    eshowcasefaction = models.IntegerField(db_column='eShowcaseFaction')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'Medals'


class Minigameconstants(models.Model):
    id = models.IntegerField(primary_key=True)
    fvalue = models.FloatField(db_column='fValue')
    eminigameconstant = models.IntegerField(db_column='eMinigameConstant')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MinigameConstants'


class Minigameeffects(models.Model):
    id = models.IntegerField(primary_key=True)
    sparticlesystem = models.TextField(db_column='sParticleSystem')
    ssoundeffect = models.TextField(db_column='sSoundEffect')
    eminigameeffect = models.IntegerField(db_column='eMinigameEffect')
    fmaxplaydistance = models.FloatField(db_column='fMaxPlayDistance')
    fsfxoffsetx = models.FloatField(db_column='fSFXOffsetX')
    fsfxoffsety = models.FloatField(db_column='fSFXOffsetY')
    fsfxoffsetz = models.FloatField(db_column='fSFXOffsetZ')
    fvfxoffsetx = models.FloatField(db_column='fVFXOffsetX')
    fvfxoffsety = models.FloatField(db_column='fVFXOffsetY')
    fvfxoffsetz = models.FloatField(db_column='fVFXOffsetZ')
    bplayfordeadplayers = models.IntegerField(db_column='bPlayForDeadPlayers')
    buse3dsound = models.IntegerField(db_column='bUse3DSound')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MinigameEffects'


class MinigamegungameWeaponsetupentries(models.Model):
    id = models.IntegerField(primary_key=True)
    echaractercustomisationoverride = models.IntegerField(db_column='eCharacterCustomisationOverride')
    eminigamegungame_weaponsetup = models.IntegerField(db_column='eMinigameGunGame_WeaponSetup')
    eweaponloadout = models.IntegerField(db_column='eWeaponLoadout')
    fscoremodifier = models.FloatField(db_column='fScoreModifier')
    nlevel = models.IntegerField(db_column='nLevel')
    nnextlevelrequiredkills = models.IntegerField(db_column='nNextLevelRequiredKills')
    nnextlevelrequiredscore = models.IntegerField(db_column='nNextLevelRequiredScore')
    bnextlevelrequiredscoreisabsolute = models.IntegerField(db_column='bNextLevelRequiredScoreIsAbsolute')
    bnextlevelrequiregamescorelimit = models.IntegerField(db_column='bNextLevelRequireGameScoreLimit')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MinigameGunGame_WeaponSetupEntries'


class MinigamegungameWeaponsetups(models.Model):
    id = models.IntegerField(primary_key=True)
    eminigamegungame_weaponsetup = models.IntegerField(db_column='eMinigameGunGame_WeaponSetup')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MinigameGunGame_WeaponSetups'


class Minigamelocations(models.Model):
    id = models.IntegerField(primary_key=True)
    edistrictblock = models.IntegerField(db_column='eDistrictBlock')
    edistrictruleset = models.IntegerField(db_column='eDistrictRuleSet')
    eminigame = models.IntegerField(db_column='eMinigame')
    eminigamelocation = models.IntegerField(db_column='eMinigameLocation')
    nweight = models.IntegerField(db_column='nWeight')
    erarity = models.IntegerField(db_column='eRarity')
    espawnvariableoverride = models.IntegerField(db_column='eSpawnVariableOverride')
    ballowlocationreuse = models.IntegerField(db_column='bAllowLocationReuse')
    bentiredistrict = models.IntegerField(db_column='bEntireDistrict')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MinigameLocations'


class Minigamerewards(models.Model):
    id = models.IntegerField(primary_key=True)
    eminigame = models.IntegerField(db_column='eMinigame')
    eminigamereward = models.IntegerField(db_column='eMinigameReward')
    ereward = models.IntegerField(db_column='eReward')
    ncashreward_0 = models.IntegerField(db_column='nCashReward_0')
    ncashreward_1 = models.IntegerField(db_column='nCashReward_1')
    nrewardlevel = models.IntegerField(db_column='nRewardLevel')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MinigameRewards'


class Minigamespawnerthemes(models.Model):
    id = models.IntegerField(primary_key=True)
    eminigamespawnertheme = models.IntegerField(db_column='eMinigameSpawnerTheme')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MinigameSpawnerThemes'


class Minigames(models.Model):
    id = models.IntegerField(primary_key=True)
    steamheaders_0 = models.TextField(db_column='sTeamHeaders_0')
    steamheaders_1 = models.TextField(db_column='sTeamHeaders_1')
    steamnames_0 = models.TextField(db_column='sTeamNames_0')
    steamnames_1 = models.TextField(db_column='sTeamNames_1')
    echaractermodifiers_0 = models.IntegerField(db_column='eCharacterModifiers_0')
    echaractermodifiers_1 = models.IntegerField(db_column='eCharacterModifiers_1')
    echaractermodifiers_2 = models.IntegerField(db_column='eCharacterModifiers_2')
    echaracteroverrides_0 = models.IntegerField(db_column='eCharacterOverrides_0')
    echaracteroverrides_1 = models.IntegerField(db_column='eCharacterOverrides_1')
    echaracteroverrides_2 = models.IntegerField(db_column='eCharacterOverrides_2')
    eendeffect = models.IntegerField(db_column='eEndEffect')
    eminigame = models.IntegerField(db_column='eMinigame')
    eonmissionhudmarkervisual = models.IntegerField(db_column='eOnMissionHUDMarkerVisual')
    eoutofmissionhudmarkervisual = models.IntegerField(db_column='eOutOfMissionHUDMarkerVisual')
    espawnertheme = models.IntegerField(db_column='eSpawnerTheme')
    estarteffect = models.IntegerField(db_column='eStartEffect')
    etimeouteffect = models.IntegerField(db_column='eTimeoutEffect')
    evehicleoverrides_0 = models.IntegerField(db_column='eVehicleOverrides_0')
    evehicleoverrides_1 = models.IntegerField(db_column='eVehicleOverrides_1')
    evehicleoverrides_2 = models.IntegerField(db_column='eVehicleOverrides_2')
    eweaponloadouts_0 = models.IntegerField(db_column='eWeaponLoadouts_0')
    eweaponloadouts_1 = models.IntegerField(db_column='eWeaponLoadouts_1')
    eweaponloadouts_2 = models.IntegerField(db_column='eWeaponLoadouts_2')
    fabandontimeout = models.FloatField(db_column='fAbandonTimeout')
    fintroductiontime = models.FloatField(db_column='fIntroductionTime')
    ftimeoutnotifyinterval = models.FloatField(db_column='fTimeoutNotifyInterval')
    ftimeoutnotifystart = models.FloatField(db_column='fTimeoutNotifyStart')
    ftimetoclearplayers = models.FloatField(db_column='fTimeToClearPlayers')
    nmaxbonuscash = models.IntegerField(db_column='nMaxBonusCash')
    nminimumplayercount_0 = models.IntegerField(db_column='nMinimumPlayerCount_0')
    nminimumplayercount_1 = models.IntegerField(db_column='nMinimumPlayerCount_1')
    nscoreeventsforparticipation = models.IntegerField(db_column='nScoreEventsForParticipation')
    nscoreminimumforparticipation = models.IntegerField(db_column='nScoreMinimumForParticipation')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    espawnvariable = models.IntegerField(db_column='eSpawnVariable')
    etype = models.IntegerField(db_column='eType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'Minigames'


class MinigamesBlockfdm(models.Model):
    id = models.IntegerField(primary_key=True)
    eminigame = models.IntegerField(db_column='eMinigame')
    fdeadparticipationtimer = models.FloatField(db_column='fDeadParticipationTimer')
    flowteamcountscale = models.FloatField(db_column='fLowTeamCountScale')
    flowteaminitialstartuptimer = models.FloatField(db_column='fLowTeamInitialStartupTimer')
    flowteaminitialtimer = models.FloatField(db_column='fLowTeamInitialTimer')
    flowteamlivesremovallinearportion = models.FloatField(db_column='fLowTeamLivesRemovalLinearPortion')
    flowteamlivesremovalquadraticportion = models.FloatField(db_column='fLowTeamLivesRemovalQuadraticPortion')
    foobparticipationtimer = models.FloatField(db_column='fOOBParticipationTimer')
    foutofboundstime = models.FloatField(db_column='fOutOfBoundsTime')
    nminnumlives = models.IntegerField(db_column='nMinNumLives')
    nnumberoflivesperplayer = models.IntegerField(db_column='nNumberOfLivesPerPlayer')
    bcountarrests = models.IntegerField(db_column='bCountArrests')
    bignoreallsuicides = models.IntegerField(db_column='bIgnoreAllSuicides')
    bignorefriendlykills = models.IntegerField(db_column='bIgnoreFriendlyKills')
    bignoregmsuicides = models.IntegerField(db_column='bIgnoreGMSuicides')
    bignorekillsbothoob = models.IntegerField(db_column='bIgnoreKillsBothOOB')
    bignorekillsbyweaponsotherthanloadout = models.IntegerField(db_column='bIgnoreKillsByWeaponsOtherThanLoadout')
    bignorekillskilledoob = models.IntegerField(db_column='bIgnoreKillsKilledOOB')
    bignorekillskillernotinminigame = models.IntegerField(db_column='bIgnoreKillsKillerNotInMinigame')
    bignorekillskilleroob = models.IntegerField(db_column='bIgnoreKillsKillerOOB')
    bignorenonweaponexplosions = models.IntegerField(db_column='bIgnoreNonWeaponExplosions')
    bignoreroadkills = models.IntegerField(db_column='bIgnoreRoadKills')
    bignoresuicideoob = models.IntegerField(db_column='bIgnoreSuicideOOB')
    bignoresuicidewithoutassist = models.IntegerField(db_column='bIgnoreSuicideWithoutAssist')
    bignoresuicidewithoutenemyassist = models.IntegerField(db_column='bIgnoreSuicideWithoutEnemyAssist')
    bignoresuicidewithoutfriendlyassist = models.IntegerField(db_column='bIgnoreSuicideWithoutFriendlyAssist')
    bsetdeathmatchtarget = models.IntegerField(db_column='bSetDeathMatchTarget')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'Minigames_BlockFDM'


class MinigamesGoldengun(models.Model):
    id = models.IntegerField(primary_key=True)
    spickupasset = models.TextField(db_column='sPickupAsset')
    spickupsfx = models.TextField(db_column='sPickupSFX')
    spickupvfx = models.TextField(db_column='sPickupVFX')
    eminigame = models.IntegerField(db_column='eMinigame')
    eonmissionprotagonisthudmarker = models.IntegerField(db_column='eOnMissionProtagonistHUDMarker')
    eoutofmissionprotagonisthudmarker = models.IntegerField(db_column='eOutOfMissionProtagonistHUDMarker')
    fmaxpickuptime = models.FloatField(db_column='fMaxPickupTime')
    fremovealivetime = models.FloatField(db_column='fRemoveAliveTime')
    fremovedeadtime = models.FloatField(db_column='fRemoveDeadTime')
    fremovedistance = models.FloatField(db_column='fRemoveDistance')
    ftotalminigametimeouttime = models.FloatField(db_column='fTotalMinigameTimeoutTime')
    nkilltarget = models.IntegerField(db_column='nKillTarget')
    busesingleteam = models.IntegerField(db_column='bUseSingleTeam')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'Minigames_GoldenGun'


class MinigamesGungame(models.Model):
    id = models.IntegerField(primary_key=True)
    eminigame = models.IntegerField(db_column='eMinigame')
    eweaponsetup = models.IntegerField(db_column='eWeaponSetup')
    fdeadparticipationtimer = models.FloatField(db_column='fDeadParticipationTimer')
    fminrespawndistance = models.FloatField(db_column='fMinRespawnDistance')
    foobparticipationtimer = models.FloatField(db_column='fOOBParticipationTimer')
    foutofboundstime = models.FloatField(db_column='fOutOfBoundsTime')
    ftotalgametimeout = models.FloatField(db_column='fTotalGameTimeout')
    nacckillchangeonarrest = models.IntegerField(db_column='nAccKillChangeOnArrest')
    nacckillchangeondeath = models.IntegerField(db_column='nAccKillChangeOnDeath')
    nacckillchangeonnonweapondeath = models.IntegerField(db_column='nAccKillChangeOnNonWeaponDeath')
    nacckillchangeonsuicide = models.IntegerField(db_column='nAccKillChangeOnSuicide')
    naccscorechangeonarrest = models.IntegerField(db_column='nAccScoreChangeOnArrest')
    naccscorechangeondeath = models.IntegerField(db_column='nAccScoreChangeOnDeath')
    naccscorechangeonnonweapondeath = models.IntegerField(db_column='nAccScoreChangeOnNonWeaponDeath')
    naccscorechangeonsuicide = models.IntegerField(db_column='nAccScoreChangeOnSuicide')
    nlevelchangeonarrest = models.IntegerField(db_column='nLevelChangeOnArrest')
    nlevelchangeondeath = models.IntegerField(db_column='nLevelChangeOnDeath')
    nlevelchangeonnonweapondeath = models.IntegerField(db_column='nLevelChangeOnNonWeaponDeath')
    nlevelchangeonsuicide = models.IntegerField(db_column='nLevelChangeOnSuicide')
    nscorelimit = models.IntegerField(db_column='nScoreLimit')
    ballowscorelevelup = models.IntegerField(db_column='bAllowScoreLevelUp')
    bcountarrests = models.IntegerField(db_column='bCountArrests')
    bcountassignedsuicides = models.IntegerField(db_column='bCountAssignedSuicides')
    bcountnonweaponkills = models.IntegerField(db_column='bCountNonWeaponKills')
    bdisablepostitivemedalscore = models.IntegerField(db_column='bDisablePostitiveMedalScore')
    bforcelastweapononscorelimit = models.IntegerField(db_column='bForceLastWeaponOnScoreLimit')
    blockoutofarea = models.IntegerField(db_column='bLockOutOfArea')
    bmultiplyaccscorechanges = models.IntegerField(db_column='bMultiplyAccScoreChanges')
    breducelevelonnegativeacckills = models.IntegerField(db_column='bReduceLevelOnNegativeAccKills')
    breducelevelonnegativeaccscore = models.IntegerField(db_column='bReduceLevelOnNegativeAccScore')
    brequirekillwithfinalweapon = models.IntegerField(db_column='bRequireKillWithFinalWeapon')
    bscorenonweaponkills = models.IntegerField(db_column='bScoreNonWeaponKills')
    bspawncompletelyrandom = models.IntegerField(db_column='bSpawnCompletelyRandom')
    busesingleteam = models.IntegerField(db_column='bUseSingleTeam')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'Minigames_GunGame'


class MinigamesInfection(models.Model):
    id = models.IntegerField(primary_key=True)
    eendblockidentifier = models.IntegerField(db_column='eEndBlockIdentifier')
    eminigame = models.IntegerField(db_column='eMinigame')
    eprotagonistonmissionhudmarker = models.IntegerField(db_column='eProtagonistOnMissionHUDMarker')
    esurvivorpinghudmarker = models.IntegerField(db_column='eSurvivorPingHUDMarker')
    finfectedmajoritytimer = models.FloatField(db_column='fInfectedMajorityTimer')
    finfectedscoremultipliermax = models.FloatField(db_column='fInfectedScoreMultiplierMax')
    finfectedscoremultipliermin = models.FloatField(db_column='fInfectedScoreMultiplierMin')
    fminimumsurvivoraddtime = models.FloatField(db_column='fMinimumSurvivorAddTime')
    fnosurvivorslefttimer = models.FloatField(db_column='fNoSurvivorsLeftTimer')
    fprotagonistkillscoremultiplier = models.FloatField(db_column='fProtagonistKillScoreMultiplier')
    fprotagonistscoremultipliermax = models.FloatField(db_column='fProtagonistScoreMultiplierMax')
    fprotagonistscoremultipliermin = models.FloatField(db_column='fProtagonistScoreMultiplierMin')
    fsurvivormajorityratio = models.FloatField(db_column='fSurvivorMajorityRatio')
    fsurvivorpingduration = models.FloatField(db_column='fSurvivorPingDuration')
    fsurvivorpinginterval = models.FloatField(db_column='fSurvivorPingInterval')
    fsurvivorscoremultipliermax = models.FloatField(db_column='fSurvivorScoreMultiplierMax')
    fsurvivorscoremultipliermin = models.FloatField(db_column='fSurvivorScoreMultiplierMin')
    ftotalgametimeout = models.FloatField(db_column='fTotalGameTimeout')
    badjustassistscore = models.IntegerField(db_column='bAdjustAssistScore')
    badjustmedalscore = models.IntegerField(db_column='bAdjustMedalScore')
    badjustnegativescore = models.IntegerField(db_column='bAdjustNegativeScore')
    badjustnonplayerkillinfrarewards = models.IntegerField(db_column='bAdjustNonPlayerKillInfraRewards')
    badjustplayerconvertedleaderscore = models.IntegerField(db_column='bAdjustPlayerConvertedLeaderScore')
    badjustplayerconvertedscore = models.IntegerField(db_column='bAdjustPlayerConvertedScore')
    bendminigameinblock = models.IntegerField(db_column='bEndMinigameInBlock')
    bkillallinfectedatstop = models.IntegerField(db_column='bKillAllInfectedAtStop')
    bkillallplayersatstop = models.IntegerField(db_column='bKillAllPlayersAtStop')
    bkillplayerbecomingprotagonist = models.IntegerField(db_column='bKillPlayerBecomingProtagonist')
    bleaderbecomessurvivorwhenkilled = models.IntegerField(db_column='bLeaderBecomesSurvivorWhenKilled')
    bprotagonistpingswithsurvivors = models.IntegerField(db_column='bProtagonistPingsWithSurvivors')
    bprotagonistvisibleduringsurvivormajority = models.IntegerField(db_column='bProtagonistVisibleDuringSurvivorMajority')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'Minigames_Infection'


class MinigamesInfectionItemcollection(models.Model):
    id = models.IntegerField(primary_key=True)
    eitemtype = models.IntegerField(db_column='eItemType')
    eminigame_infection = models.IntegerField(db_column='eMinigame_Infection')
    etaskitemoperation = models.IntegerField(db_column='eTaskItemOperation')
    ffailedspawnretrytimer = models.FloatField(db_column='fFailedSpawnRetryTimer')
    fitemcollectiontimeout = models.FloatField(db_column='fItemCollectionTimeout')
    navailabletaskitems = models.IntegerField(db_column='nAvailableTaskItems')
    nminimumitemstaken = models.IntegerField(db_column='nMinimumItemsTaken')
    nrequiredtaskitemcounts = models.IntegerField(db_column='nRequiredTaskItemCounts')
    nspawnercount = models.IntegerField(db_column='nSpawnerCount')
    ntargetitemstaken = models.IntegerField(db_column='nTargetItemsTaken')
    bblockpickups = models.IntegerField(db_column='bBlockPickups')
    bcandeliveritems = models.IntegerField(db_column='bCanDeliverItems')
    bcandropsmallitems = models.IntegerField(db_column='bCanDropSmallItems')
    bcountdelivereditems = models.IntegerField(db_column='bCountDeliveredItems')
    bcountdestroyeditems = models.IntegerField(db_column='bCountDestroyedItems')
    bcountpickedupitems = models.IntegerField(db_column='bCountPickedUpItems')
    bitemsinsingleblock = models.IntegerField(db_column='bItemsInSingleBlock')
    bleaderassignedbyscore = models.IntegerField(db_column='bLeaderAssignedByScore')
    blimitspawnerstoselectedblock = models.IntegerField(db_column='bLimitSpawnersToSelectedBlock')
    brespawndelivereditems = models.IntegerField(db_column='bRespawnDeliveredItems')
    brespawndestroyeditems = models.IntegerField(db_column='bRespawnDestroyedItems')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'Minigames_Infection_ItemCollection'


class MinigamesInfectionRichfx(models.Model):
    id = models.IntegerField(primary_key=True)
    sendstagemusic_start = models.TextField(db_column='sEndStageMusic_Start')
    sendstagemusic_stop = models.TextField(db_column='sEndStageMusic_Stop')
    soverrideweather = models.TextField(db_column='sOverrideWeather')
    einfectedspawnfx_female = models.IntegerField(db_column='eInfectedSpawnFX_Female')
    einfectedspawnfx_male = models.IntegerField(db_column='eInfectedSpawnFX_Male')
    eminigame_infection = models.IntegerField(db_column='eMinigame_Infection')
    eplayerpingfx = models.IntegerField(db_column='ePlayerPingFX')
    eprotagonistassignedfx = models.IntegerField(db_column='eProtagonistAssignedFX')
    eprotagonistkillfx = models.IntegerField(db_column='eProtagonistKillFX')
    eprotagonistspawnfx_female = models.IntegerField(db_column='eProtagonistSpawnFX_Female')
    eprotagonistspawnfx_male = models.IntegerField(db_column='eProtagonistSpawnFX_Male')
    nendtodhours = models.IntegerField(db_column='nEndToDHours')
    nendtodminutes = models.IntegerField(db_column='nEndToDMinutes')
    npausetodhours = models.IntegerField(db_column='nPauseToDHours')
    npausetodminutes = models.IntegerField(db_column='nPauseToDMinutes')
    bendtodstartswithinfectedmajority = models.IntegerField(db_column='bEndToDStartsWithInfectedMajority')
    bforcerestoreweather = models.IntegerField(db_column='bForceRestoreWeather')
    bpausetod = models.IntegerField(db_column='bPauseToD')
    bplayprotagonistkillfromkilledlocation = models.IntegerField(db_column='bPlayProtagonistKillFromKilledLocation')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'Minigames_Infection_RichFX'


class MinigamesInfectionVip(models.Model):
    id = models.IntegerField(primary_key=True)
    eminigame_infection = models.IntegerField(db_column='eMinigame_Infection')
    nlowheatgroupchance = models.IntegerField(db_column='nLowHeatGroupChance')
    nmaxheatgroupchance = models.IntegerField(db_column='nMaxHeatGroupChance')
    nmaxheatungroupedchance = models.IntegerField(db_column='nMaxHeatUngroupedChance')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'Minigames_Infection_VIP'


class MinigamesMug(models.Model):
    id = models.IntegerField(primary_key=True)
    splayerinmugrangeaudio = models.TextField(db_column='sPlayerInMugRangeAudio')
    ecarrierhudmarker_0 = models.IntegerField(db_column='eCarrierHUDMarker_0')
    ecarrierhudmarker_1 = models.IntegerField(db_column='eCarrierHUDMarker_1')
    ecarrierhudmarker_2 = models.IntegerField(db_column='eCarrierHUDMarker_2')
    ecarrierhudmarker_3 = models.IntegerField(db_column='eCarrierHUDMarker_3')
    ecarrierhudmarker_4 = models.IntegerField(db_column='eCarrierHUDMarker_4')
    edeliveryeffect_0 = models.IntegerField(db_column='eDeliveryEffect_0')
    edeliveryeffect_1 = models.IntegerField(db_column='eDeliveryEffect_1')
    edeliveryeffect_2 = models.IntegerField(db_column='eDeliveryEffect_2')
    edeliveryeffect_3 = models.IntegerField(db_column='eDeliveryEffect_3')
    einvulerableeffect = models.IntegerField(db_column='eInvulerableEffect')
    eitemspawnrule_0 = models.IntegerField(db_column='eItemSpawnRule_0')
    eitemspawnrule_1 = models.IntegerField(db_column='eItemSpawnRule_1')
    ekillcarriereffect = models.IntegerField(db_column='eKillCarrierEffect')
    eminigame = models.IntegerField(db_column='eMinigame')
    emugcompleteeffect = models.IntegerField(db_column='eMugCompleteEffect')
    enpchudmarker_0 = models.IntegerField(db_column='eNPCHudMarker_0')
    enpchudmarker_1 = models.IntegerField(db_column='eNPCHudMarker_1')
    enpckillitemspawnrule_0 = models.IntegerField(db_column='eNPCKillItemSpawnRule_0')
    enpckillitemspawnrule_1 = models.IntegerField(db_column='eNPCKillItemSpawnRule_1')
    enpcoperation_0 = models.IntegerField(db_column='eNPCOperation_0')
    enpcoperation_1 = models.IntegerField(db_column='eNPCOperation_1')
    enpctype_0 = models.IntegerField(db_column='eNPCType_0')
    enpctype_1 = models.IntegerField(db_column='eNPCType_1')
    eoomcarrierhudmarker_0 = models.IntegerField(db_column='eOOMCarrierHUDMarker_0')
    eoomcarrierhudmarker_1 = models.IntegerField(db_column='eOOMCarrierHUDMarker_1')
    eoomcarrierhudmarker_2 = models.IntegerField(db_column='eOOMCarrierHUDMarker_2')
    eoomcarrierhudmarker_3 = models.IntegerField(db_column='eOOMCarrierHUDMarker_3')
    eoomcarrierhudmarker_4 = models.IntegerField(db_column='eOOMCarrierHUDMarker_4')
    eoomprotagonisthudmarker = models.IntegerField(db_column='eOOMProtagonistHUDMarker')
    eprotagonisthudmarker = models.IntegerField(db_column='eProtagonistHUDMarker')
    etaskitemhudmarker = models.IntegerField(db_column='eTaskItemHudMarker')
    etaskitemoperation = models.IntegerField(db_column='eTaskItemOperation')
    fdeliverymultiplier_0 = models.FloatField(db_column='fDeliveryMultiplier_0')
    fdeliverymultiplier_1 = models.FloatField(db_column='fDeliveryMultiplier_1')
    fdeliverymultiplier_2 = models.FloatField(db_column='fDeliveryMultiplier_2')
    fdeliverymultiplier_3 = models.FloatField(db_column='fDeliveryMultiplier_3')
    fimmunityaudiotime = models.FloatField(db_column='fImmunityAudioTime')
    fimmunitytimeout = models.FloatField(db_column='fImmunityTimeout')
    finactivitytimeouttime = models.FloatField(db_column='fInactivityTimeoutTime')
    fmaxnpctime = models.FloatField(db_column='fMaxNPCTime')
    fnodropkilltransfer = models.FloatField(db_column='fNoDropKillTransfer')
    fnodropmugtransfer = models.FloatField(db_column='fNoDropMugTransfer')
    fnodropsuicidepenalty = models.FloatField(db_column='fNoDropSuicidePenalty')
    fnpcchance_0 = models.FloatField(db_column='fNPCChance_0')
    fnpcchance_1 = models.FloatField(db_column='fNPCChance_1')
    fnpccountperplayer = models.FloatField(db_column='fNPCCountPerPlayer')
    fnpcmugimmunityduration = models.FloatField(db_column='fNPCMugImmunityDuration')
    fplayermugimmunityduration = models.FloatField(db_column='fPlayerMugImmunityDuration')
    fpostimmunitymugtimeout = models.FloatField(db_column='fPostImmunityMugTimeout')
    fprotagonistkillmultiplier = models.FloatField(db_column='fProtagonistKillMultiplier')
    fremovedistance = models.FloatField(db_column='fRemoveDistance')
    fremovetimealive = models.FloatField(db_column='fRemoveTimeAlive')
    fremovetimedead = models.FloatField(db_column='fRemoveTimeDead')
    frespawnwithitemsimmunity = models.FloatField(db_column='fRespawnWithItemsImmunity')
    ftaskitemcleanuptime = models.FloatField(db_column='fTaskItemCleanupTime')
    ftotalminigametimeouttime = models.FloatField(db_column='fTotalMinigameTimeoutTime')
    ndeliverlimit = models.IntegerField(db_column='nDeliverLimit')
    nnpccount = models.IntegerField(db_column='nNPCCount')
    nnpccountlimit = models.IntegerField(db_column='nNPCCountLimit')
    noverridekillscore = models.IntegerField(db_column='nOverrideKillScore')
    bcandropoffitems = models.IntegerField(db_column='bCanDropOffItems')
    bcanmugplayers = models.IntegerField(db_column='bCanMugPlayers')
    bdisableprimaryscore = models.IntegerField(db_column='bDisablePrimaryScore')
    bhideplayerradarmarkers = models.IntegerField(db_column='bHidePlayerRadarMarkers')
    bkillmuggedplayers = models.IntegerField(db_column='bKillMuggedPlayers')
    bkillnpcwhendone = models.IntegerField(db_column='bKillNPCWhenDone')
    bkillnpcwhendonemugging = models.IntegerField(db_column='bKillNPCWhenDoneMugging')
    bmultimug = models.IntegerField(db_column='bMultiMug')
    bmultiplydelivereditemnumbers = models.IntegerField(db_column='bMultiplyDeliveredItemNumbers')
    bnodrops = models.IntegerField(db_column='bNoDrops')
    bnodroptransfergainonly = models.IntegerField(db_column='bNoDropTransferGainOnly')
    bnpcmarkersafterfirstmug = models.IntegerField(db_column='bNPCMarkersAfterFirstMug')
    bnpcmugusesimmunitytimeout = models.IntegerField(db_column='bNPCMugUsesImmunityTimeout')
    bopposeallcarriers = models.IntegerField(db_column='bOpposeAllCarriers')
    boverridetitle = models.IntegerField(db_column='bOverrideTitle')
    bpvpunlockallcarriers = models.IntegerField(db_column='bPvPUnlockAllCarriers')
    bpvpunlockprotagonist = models.IntegerField(db_column='bPVPUnlockProtagonist')
    bshowcarrierstoall = models.IntegerField(db_column='bShowCarriersToAll')
    busedeliverymultipliers = models.IntegerField(db_column='bUseDeliveryMultipliers')
    busesingleteam = models.IntegerField(db_column='bUseSingleTeam')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'Minigames_Mug'


class MinigamesVip(models.Model):
    id = models.IntegerField(primary_key=True)
    eminigame = models.IntegerField(db_column='eMinigame')
    fvipwintime = models.FloatField(db_column='fVIPWinTime')
    nlowheatgroupchance = models.IntegerField(db_column='nLowHeatGroupChance')
    nmaxheatgroupchance = models.IntegerField(db_column='nMaxHeatGroupChance')
    nmaxheatungroupedchance = models.IntegerField(db_column='nMaxHeatUngroupedChance')
    nvipwinkills = models.IntegerField(db_column='nVIPWinKills')
    bbulklog = models.IntegerField(db_column='bBulkLog')
    bkillbodyguardsatstart = models.IntegerField(db_column='bKillBodyGuardsAtStart')
    bkillvipatstart = models.IntegerField(db_column='bKillVIPAtStart')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'Minigames_VIP'


class Missionofcriminalcontacts(models.Model):
    id = models.IntegerField(primary_key=True)
    econtact = models.IntegerField(db_column='eContact')
    emission = models.IntegerField(db_column='eMission')
    emissionofcriminalcontact = models.IntegerField(db_column='eMissionOfCriminalContact')
    nmaxlevel = models.IntegerField(db_column='nMaxLevel')
    nminlevel = models.IntegerField(db_column='nMinLevel')
    bdisabled = models.IntegerField(db_column='bDisabled')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MissionOfCriminalContacts'


class Missionofenforcercontacts(models.Model):
    id = models.IntegerField(primary_key=True)
    econtact = models.IntegerField(db_column='eContact')
    emission = models.IntegerField(db_column='eMission')
    emissionofenforcercontact = models.IntegerField(db_column='eMissionOfEnforcerContact')
    nmaxlevel = models.IntegerField(db_column='nMaxLevel')
    nminlevel = models.IntegerField(db_column='nMinLevel')
    bdisabled = models.IntegerField(db_column='bDisabled')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MissionOfEnforcerContacts'


class Missionresultreasons(models.Model):
    id = models.IntegerField(primary_key=True)
    sdrawmessage = models.TextField(db_column='sDrawMessage')
    slosemessage = models.TextField(db_column='sLoseMessage')
    swinmessage = models.TextField(db_column='sWinMessage')
    emissionresultreason = models.IntegerField(db_column='eMissionResultReason')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MissionResultReasons'


class Missionrewardpackages(models.Model):
    id = models.IntegerField(primary_key=True)
    emissionrewardpackage = models.IntegerField(db_column='eMissionRewardPackage')
    nbasecash_0 = models.IntegerField(db_column='nBaseCash_0')
    nbasecash_1 = models.IntegerField(db_column='nBaseCash_1')
    nbasecontactstanding_0 = models.IntegerField(db_column='nBaseContactStanding_0')
    nbasecontactstanding_1 = models.IntegerField(db_column='nBaseContactStanding_1')
    nscore = models.IntegerField(db_column='nScore')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MissionRewardPackages'


class Missionsystemfilterentries(models.Model):
    id = models.IntegerField(primary_key=True)
    emissionsystemfilter = models.IntegerField(db_column='eMissionSystemFilter')
    emissionsystem = models.IntegerField(db_column='eMissionSystem')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MissionSystemFilterEntries'


class Missionsystemfilters(models.Model):
    id = models.IntegerField(primary_key=True)
    emissionsystemfilter = models.IntegerField(db_column='eMissionSystemFilter')
    bexclusive = models.IntegerField(db_column='bExclusive')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MissionSystemFilters'


class Missiontakeoutlookup(models.Model):
    id = models.IntegerField(primary_key=True)
    nmissiontakeoutlookup = models.IntegerField(db_column='nMissionTakeoutLookUp')
    ntakeoutlimit = models.IntegerField(db_column='nTakeoutLimit')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MissionTakeoutLookUp'


class Missiontemplateuiprofiles(models.Model):
    id = models.IntegerField(primary_key=True)
    strackedvaluedescription_0 = models.TextField(db_column='sTrackedValueDescription_0')
    strackedvaluedescription_1 = models.TextField(db_column='sTrackedValueDescription_1')
    strackedvaluedescription_2 = models.TextField(db_column='sTrackedValueDescription_2')
    strackedvaluedescription_3 = models.TextField(db_column='sTrackedValueDescription_3')
    strackedvalueimage_0 = models.TextField(db_column='sTrackedValueImage_0')
    strackedvalueimage_1 = models.TextField(db_column='sTrackedValueImage_1')
    strackedvalueimage_2 = models.TextField(db_column='sTrackedValueImage_2')
    strackedvalueimage_3 = models.TextField(db_column='sTrackedValueImage_3')
    emissiontemplateuiprofile = models.IntegerField(db_column='eMissionTemplateUIProfile')
    etrackedvaluebarfgdisabled_0 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_0')
    etrackedvaluebarfgdisabled_1 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_1')
    etrackedvaluebarfgdisabled_2 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_2')
    etrackedvaluebarfgdisabled_3 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_3')
    etrackedvaluebg_0 = models.IntegerField(db_column='eTrackedValueBg_0')
    etrackedvaluebg_1 = models.IntegerField(db_column='eTrackedValueBg_1')
    etrackedvaluebg_2 = models.IntegerField(db_column='eTrackedValueBg_2')
    etrackedvaluebg_3 = models.IntegerField(db_column='eTrackedValueBg_3')
    etrackedvaluefg_0 = models.IntegerField(db_column='eTrackedValueFg_0')
    etrackedvaluefg_1 = models.IntegerField(db_column='eTrackedValueFg_1')
    etrackedvaluefg_2 = models.IntegerField(db_column='eTrackedValueFg_2')
    etrackedvaluefg_3 = models.IntegerField(db_column='eTrackedValueFg_3')
    etrackedvaluesocket_0 = models.IntegerField(db_column='eTrackedValueSocket_0')
    etrackedvaluesocket_1 = models.IntegerField(db_column='eTrackedValueSocket_1')
    etrackedvaluesocket_2 = models.IntegerField(db_column='eTrackedValueSocket_2')
    etrackedvaluesocket_3 = models.IntegerField(db_column='eTrackedValueSocket_3')
    etrackedvalue_0 = models.IntegerField(db_column='eTrackedValue_0')
    etrackedvalue_1 = models.IntegerField(db_column='eTrackedValue_1')
    etrackedvalue_2 = models.IntegerField(db_column='eTrackedValue_2')
    etrackedvalue_3 = models.IntegerField(db_column='eTrackedValue_3')
    etrackedvaluedisplay_0 = models.IntegerField(db_column='eTrackedValueDisplay_0')
    etrackedvaluedisplay_1 = models.IntegerField(db_column='eTrackedValueDisplay_1')
    etrackedvaluedisplay_2 = models.IntegerField(db_column='eTrackedValueDisplay_2')
    etrackedvaluedisplay_3 = models.IntegerField(db_column='eTrackedValueDisplay_3')
    bflashwhenchanged_0 = models.IntegerField(db_column='bFlashWhenChanged_0')
    bflashwhenchanged_1 = models.IntegerField(db_column='bFlashWhenChanged_1')
    bflashwhenchanged_2 = models.IntegerField(db_column='bFlashWhenChanged_2')
    bflashwhenchanged_3 = models.IntegerField(db_column='bFlashWhenChanged_3')
    bhideatmax_0 = models.IntegerField(db_column='bHideAtMax_0')
    bhideatmax_1 = models.IntegerField(db_column='bHideAtMax_1')
    bhideatmax_2 = models.IntegerField(db_column='bHideAtMax_2')
    bhideatmax_3 = models.IntegerField(db_column='bHideAtMax_3')
    bhidewhenone_0 = models.IntegerField(db_column='bHideWhenOne_0')
    bhidewhenone_1 = models.IntegerField(db_column='bHideWhenOne_1')
    bhidewhenone_2 = models.IntegerField(db_column='bHideWhenOne_2')
    bhidewhenone_3 = models.IntegerField(db_column='bHideWhenOne_3')
    bhidewhenoppositionviptakeoutsdisabled_0 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_0')
    bhidewhenoppositionviptakeoutsdisabled_1 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_1')
    bhidewhenoppositionviptakeoutsdisabled_2 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_2')
    bhidewhenoppositionviptakeoutsdisabled_3 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_3')
    bhidewhenownerviptakeoutsdisabled_0 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_0')
    bhidewhenownerviptakeoutsdisabled_1 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_1')
    bhidewhenownerviptakeoutsdisabled_2 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_2')
    bhidewhenownerviptakeoutsdisabled_3 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_3')
    bhidewhenpointsdisabled_0 = models.IntegerField(db_column='bHideWhenPointsDisabled_0')
    bhidewhenpointsdisabled_1 = models.IntegerField(db_column='bHideWhenPointsDisabled_1')
    bhidewhenpointsdisabled_2 = models.IntegerField(db_column='bHideWhenPointsDisabled_2')
    bhidewhenpointsdisabled_3 = models.IntegerField(db_column='bHideWhenPointsDisabled_3')
    bhidewhentakeoutsdisabled_0 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_0')
    bhidewhentakeoutsdisabled_1 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_1')
    bhidewhentakeoutsdisabled_2 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_2')
    bhidewhentakeoutsdisabled_3 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_3')
    bhidewhenunopposed_0 = models.IntegerField(db_column='bHideWhenUnopposed_0')
    bhidewhenunopposed_1 = models.IntegerField(db_column='bHideWhenUnopposed_1')
    bhidewhenunopposed_2 = models.IntegerField(db_column='bHideWhenUnopposed_2')
    bhidewhenunopposed_3 = models.IntegerField(db_column='bHideWhenUnopposed_3')
    btrackedvalueinlocaloverview_0 = models.IntegerField(db_column='bTrackedValueInLocalOverview_0')
    btrackedvalueinlocaloverview_1 = models.IntegerField(db_column='bTrackedValueInLocalOverview_1')
    btrackedvalueinlocaloverview_2 = models.IntegerField(db_column='bTrackedValueInLocalOverview_2')
    btrackedvalueinlocaloverview_3 = models.IntegerField(db_column='bTrackedValueInLocalOverview_3')
    btrackedvalueinremoteoverview_0 = models.IntegerField(db_column='bTrackedValueInRemoteOverview_0')
    btrackedvalueinremoteoverview_1 = models.IntegerField(db_column='bTrackedValueInRemoteOverview_1')
    btrackedvalueinremoteoverview_2 = models.IntegerField(db_column='bTrackedValueInRemoteOverview_2')
    btrackedvalueinremoteoverview_3 = models.IntegerField(db_column='bTrackedValueInRemoteOverview_3')
    btrackedvalueonhud_0 = models.IntegerField(db_column='bTrackedValueOnHUD_0')
    btrackedvalueonhud_1 = models.IntegerField(db_column='bTrackedValueOnHUD_1')
    btrackedvalueonhud_2 = models.IntegerField(db_column='bTrackedValueOnHUD_2')
    btrackedvalueonhud_3 = models.IntegerField(db_column='bTrackedValueOnHUD_3')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MissionTemplateUIProfiles'


class Missiontemplates(models.Model):
    id = models.IntegerField(primary_key=True)
    smissiontitle = models.TextField(db_column='sMissionTitle')
    emissiontemplate = models.IntegerField(db_column='eMissionTemplate')
    emissiontypefilter = models.IntegerField(db_column='eMissionTypeFilter')
    emissionuioppositionprofile = models.IntegerField(db_column='eMissionUIOppositionProfile')
    emissionuiownerprofile = models.IntegerField(db_column='eMissionUIOwnerProfile')
    epurpose = models.IntegerField(db_column='ePurpose')
    erarity = models.IntegerField(db_column='eRarity')
    erewardpackage = models.IntegerField(db_column='eRewardPackage')
    fowningsidebias = models.FloatField(db_column='fOwningSideBias')
    ncomplexity = models.IntegerField(db_column='nComplexity')
    ngroupsizemax = models.IntegerField(db_column='nGroupSizeMax')
    ngroupsizemin = models.IntegerField(db_column='nGroupSizeMin')
    nopposingsideviplives = models.IntegerField(db_column='nOpposingSideVIPLives')
    nowningsideviplives = models.IntegerField(db_column='nOwningSideVIPLives')
    nrespawntime = models.IntegerField(db_column='nRespawnTime')
    nrespawntimeincrement = models.IntegerField(db_column='nRespawnTimeIncrement')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    nsimultaneouscap = models.IntegerField(db_column='nSimultaneousCap')
    ntakeoutcount = models.IntegerField(db_column='nTakeoutCount')
    efaction = models.IntegerField(db_column='eFaction')
    etimeofdayavailability = models.IntegerField(db_column='eTimeOfDayAvailability')
    bbountyhunter = models.IntegerField(db_column='bBountyHunter')
    bcountarrestsastakeouts = models.IntegerField(db_column='bCountArrestsAsTakeouts')
    bcountarrestsasviptakeouts = models.IntegerField(db_column='bCountArrestsAsVIPTakeouts')
    bcountkillsastakeouts = models.IntegerField(db_column='bCountKillsAsTakeouts')
    bcountkillsasviptakeouts = models.IntegerField(db_column='bCountKillsAsVIPTakeouts')
    bdisabled = models.IntegerField(db_column='bDisabled')
    bnocriminalopposition = models.IntegerField(db_column='bNoCriminalOpposition')
    boppositionwinonmaxtakeouts = models.IntegerField(db_column='bOppositionWinOnMaxTakeouts')
    bownerwinonmaxtakeouts = models.IntegerField(db_column='bOwnerWinOnMaxTakeouts')
    btest = models.IntegerField(db_column='bTest')
    busetakeoutbar = models.IntegerField(db_column='bUseTakeoutBar')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MissionTemplates'


class Missionuisockets(models.Model):
    id = models.IntegerField(primary_key=True)
    emissionuisocket = models.IntegerField(db_column='eMissionUISocket')
    nrow = models.IntegerField(db_column='nRow')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MissionUISockets'


class Missionuitrackedstateprofile(models.Model):
    id = models.IntegerField(primary_key=True)
    sarmedicon = models.TextField(db_column='sArmedIcon')
    sneutralicon = models.TextField(db_column='sNeutralIcon')
    soppositionclaimed = models.TextField(db_column='sOppositionClaimed')
    sownerclaimed = models.TextField(db_column='sOwnerClaimed')
    sunarmedicon = models.TextField(db_column='sUnarmedIcon')
    emissionuitrackedstateprofile = models.IntegerField(db_column='eMissionUITrackedStateProfile')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'MissionUITrackedStateProfile'


class Modifiercategories(models.Model):
    id = models.IntegerField(primary_key=True)
    emodifiercategory = models.IntegerField(db_column='eModifierCategory')
    nselectableslot = models.IntegerField(db_column='nSelectableSlot')
    emodifierclass = models.IntegerField(db_column='eModifierClass')
    emodifiertype = models.IntegerField(db_column='eModifierType')
    estackingslot = models.IntegerField(db_column='eStackingSlot')
    bavailableaspassenger = models.IntegerField(db_column='bAvailableAsPassenger')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ModifierCategories'


class Modifierdeployableeffects(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    emodifieritem = models.IntegerField(db_column='eModifierItem')
    etaskitem = models.IntegerField(db_column='eTaskItem')
    bdeployatmodifierend = models.IntegerField(db_column='bDeployAtModifierEnd')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ModifierDeployableEffects'


class Modifiereffects(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    emodifieritem = models.IntegerField(db_column='eModifierItem')
    faddtoresult = models.FloatField(db_column='fAddToResult')
    feffectmultiplier = models.FloatField(db_column='fEffectMultiplier')
    eeffecttype = models.IntegerField(db_column='eEffectType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ModifierEffects'


class Modifieritemeffects(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    eitem = models.IntegerField(db_column='eItem')
    emodifieritem = models.IntegerField(db_column='eModifierItem')
    eeffect = models.IntegerField(db_column='eEffect')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ModifierItemEffects'


class Modifieritemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    emodifieritem = models.IntegerField(db_column='eModifierItem')
    napplicationcost = models.IntegerField(db_column='nApplicationCost')
    nremovalcost = models.IntegerField(db_column='nRemovalCost')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ModifierItemTypes'


class Modifieritems(models.Model):
    id = models.IntegerField(primary_key=True)
    striggersfx = models.TextField(db_column='sTriggerSFX')
    striggervfx = models.TextField(db_column='sTriggerVFX')
    emodifiercategory = models.IntegerField(db_column='eModifierCategory')
    emodifieritem = models.IntegerField(db_column='eModifierItem')
    erulesetexclusion = models.IntegerField(db_column='eRulesetExclusion')
    fcooldowntimeatpremiumlevel_0 = models.FloatField(db_column='fCooldownTimeAtPremiumLevel_0')
    fcooldowntimeatpremiumlevel_1 = models.FloatField(db_column='fCooldownTimeAtPremiumLevel_1')
    fdurationatpremiumlevel_0 = models.FloatField(db_column='fDurationAtPremiumLevel_0')
    fdurationatpremiumlevel_1 = models.FloatField(db_column='fDurationAtPremiumLevel_1')
    fintervaltimeatpremiumlevel_0 = models.FloatField(db_column='fIntervalTimeAtPremiumLevel_0')
    fintervaltimeatpremiumlevel_1 = models.FloatField(db_column='fIntervalTimeAtPremiumLevel_1')
    nmodifierlevel = models.IntegerField(db_column='nModifierLevel')
    egiftboxtheme = models.IntegerField(db_column='eGiftBoxTheme')
    bactivationendsimmunity = models.IntegerField(db_column='bActivationEndsImmunity')
    bbroadcastsfx = models.IntegerField(db_column='bBroadcastSFX')
    buncancelable = models.IntegerField(db_column='bUnCancelable')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ModifierItems'


class Npcanimationcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    enpcanimationcategory = models.IntegerField(db_column='eNPCAnimationCategory')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'NPCAnimationCategories'


class Npcaudiotype(models.Model):
    id = models.IntegerField(primary_key=True)
    sclothingaccessoriesswitchvalue = models.TextField(db_column='sClothingAccessoriesSwitchValue')
    sclothingarmsswitchvalue = models.TextField(db_column='sClothingArmsSwitchValue')
    sclothingfootwearswitchvalue = models.TextField(db_column='sClothingFootwearSwitchValue')
    sclothinglegsswitchvalue = models.TextField(db_column='sClothingLegsSwitchValue')
    svoiceswitchvalue = models.TextField(db_column='sVoiceSwitchValue')
    enpcaudiotype = models.IntegerField(db_column='eNPCAudioType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'NPCAudioType'


class Npcdrivertypes(models.Model):
    id = models.IntegerField(primary_key=True)
    enpcdrivertype = models.IntegerField(db_column='eNPCDriverType')
    enpctypefemale = models.IntegerField(db_column='eNPCTypeFemale')
    enpctypemale = models.IntegerField(db_column='eNPCTypeMale')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'NPCDriverTypes'


class NpceventAllowedtooverrides(models.Model):
    id = models.IntegerField(primary_key=True)
    nignoreme = models.IntegerField(db_column='nIgnoreMe')
    enpcevent = models.IntegerField(db_column='eNPCEvent')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'NPCEvent_AllowedToOverrides'


class Npcevents(models.Model):
    id = models.IntegerField(primary_key=True)
    nignoreme = models.IntegerField(db_column='nIgnoreMe')
    enpcevent = models.IntegerField(db_column='eNPCEvent')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'NPCEvents'


class Npcpedestriananimations(models.Model):
    id = models.IntegerField(primary_key=True)
    snpcpedestriananimation = models.TextField(db_column='sNPCPedestrianAnimation')
    eanimationcategory = models.IntegerField(db_column='eAnimationCategory')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'NPCPedestrianAnimations'


class NpcreactionAllowedtooverrides(models.Model):
    id = models.IntegerField(primary_key=True)
    npriority = models.IntegerField(db_column='nPriority')
    enpcreaction = models.IntegerField(db_column='eNPCReaction')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'NPCReaction_AllowedToOverrides'


class Npcreactions(models.Model):
    id = models.IntegerField(primary_key=True)
    npriority = models.IntegerField(db_column='nPriority')
    enpcreaction = models.IntegerField(db_column='eNPCReaction')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'NPCReactions'


class NpctypeTodDistricts(models.Model):
    id = models.IntegerField(primary_key=True)
    edistrict = models.IntegerField(db_column='eDistrict')
    enpctype_tod = models.IntegerField(db_column='eNPCType_TOD')
    enpctype_tod_district = models.IntegerField(db_column='eNPCType_TOD_District')
    fpopulationpercentage = models.FloatField(db_column='fPopulationPercentage')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'NPCType_TOD_Districts'


class NpctypeTodInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    enpctype = models.IntegerField(db_column='eNPCType')
    enpctype_tod = models.IntegerField(db_column='eNPCType_TOD')
    etod = models.IntegerField(db_column='eTOD')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'NPCType_TOD_Info'


class Npctypes(models.Model):
    id = models.IntegerField(primary_key=True)
    enpctype = models.IntegerField(db_column='eNPCType')
    fdebugcolour_b = models.FloatField(db_column='fDebugColour_B')
    fdebugcolour_g = models.FloatField(db_column='fDebugColour_G')
    fdebugcolour_r = models.FloatField(db_column='fDebugColour_R')
    egender = models.IntegerField(db_column='eGender')
    enpccategory = models.IntegerField(db_column='eNPCCategory')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'NPCTypes'


class Npcvehicleanimations(models.Model):
    id = models.IntegerField(primary_key=True)
    snpcvehicleanimation = models.TextField(db_column='sNPCVehicleAnimation')
    eanimationcategory = models.IntegerField(db_column='eAnimationCategory')
    evehiclenpcinsideanimationset = models.IntegerField(db_column='eVehicleNPCInsideAnimationSet')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'NPCVehicleAnimations'


class Npcvehiclespeeds(models.Model):
    id = models.IntegerField(primary_key=True)
    enpcvehiclecategory = models.IntegerField(db_column='eNPCVehicleCategory')
    fmaxacceleration = models.FloatField(db_column='fMaxAcceleration')
    fmaxdeceleration = models.FloatField(db_column='fMaxDeceleration')
    fmaxtopspeedratio = models.FloatField(db_column='fMaxTopSpeedRatio')
    fminacceleration = models.FloatField(db_column='fMinAcceleration')
    fmindeceleration = models.FloatField(db_column='fMinDeceleration')
    fmintopspeedratio = models.FloatField(db_column='fMinTopSpeedRatio')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'NPCVehicleSpeeds'


class Npcworldevents(models.Model):
    id = models.IntegerField(primary_key=True)
    spedestrianaudioreason = models.TextField(db_column='sPedestrianAudioReason')
    epedestrianblastevent = models.IntegerField(db_column='ePedestrianBlastEvent')
    epedestriandangerevent = models.IntegerField(db_column='ePedestrianDangerEvent')
    epedestrianwitnessevent = models.IntegerField(db_column='ePedestrianWitnessEvent')
    evehicleblastevent = models.IntegerField(db_column='eVehicleBlastEvent')
    evehicledangerevent = models.IntegerField(db_column='eVehicleDangerEvent')
    evehiclewitnessevent = models.IntegerField(db_column='eVehicleWitnessEvent')
    faudibilitydistance = models.FloatField(db_column='fAudibilityDistance')
    fblastdistance = models.FloatField(db_column='fBlastDistance')
    fdangerdistance = models.FloatField(db_column='fDangerDistance')
    fvisibilitydistance = models.FloatField(db_column='fVisibilityDistance')
    enpcworldevent = models.IntegerField(db_column='eNPCWorldEvent')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'NPCWorldEvents'


class NpcTodBehaviours(models.Model):
    id = models.IntegerField(primary_key=True)
    enpc_tod_event = models.IntegerField(db_column='eNPC_TOD_Event')
    ereaction = models.IntegerField(db_column='eReaction')
    flikelihood = models.FloatField(db_column='fLikelihood')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'NPC_TOD_Behaviours'


class NpcTodEvent(models.Model):
    id = models.IntegerField(primary_key=True)
    enpc_tod_event = models.IntegerField(db_column='eNPC_TOD_Event')
    enpctype = models.IntegerField(db_column='eNPCType')
    etod_event = models.IntegerField(db_column='eTOD_Event')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'NPC_TOD_Event'


class Notorietyeffects(models.Model):
    id = models.IntegerField(primary_key=True)
    eforcemaxlevel = models.IntegerField(db_column='eForceMaxLevel')
    eforceminlevel = models.IntegerField(db_column='eForceMinLevel')
    enotorietyeffect = models.IntegerField(db_column='eNotorietyEffect')
    enotorietylevellimit = models.IntegerField(db_column='eNotorietyLevelLimit')
    fquantity = models.FloatField(db_column='fQuantity')
    nenforcerwitnesserscap = models.IntegerField(db_column='nEnforcerWitnessersCap')
    nnpcwitnesserscap = models.IntegerField(db_column='nNPCWitnessersCap')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'NotorietyEffects'


class Notorietylevels(models.Model):
    id = models.IntegerField(primary_key=True)
    eheatlevel = models.IntegerField(db_column='eHeatLevel')
    enotorietylevel = models.IntegerField(db_column='eNotorietyLevel')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'NotorietyLevels'


class Owaitemspawnrules(models.Model):
    id = models.IntegerField(primary_key=True)
    eitemmetatag_0 = models.IntegerField(db_column='eItemMetaTag_0')
    eitemmetatag_1 = models.IntegerField(db_column='eItemMetaTag_1')
    eitemmetatag_2 = models.IntegerField(db_column='eItemMetaTag_2')
    eitemmetatag_3 = models.IntegerField(db_column='eItemMetaTag_3')
    eitemmetatag_4 = models.IntegerField(db_column='eItemMetaTag_4')
    eowaitemspawnrule = models.IntegerField(db_column='eOWAItemSpawnRule')
    nlargeitemweighting = models.IntegerField(db_column='nLargeItemWeighting')
    nlowermidrange = models.IntegerField(db_column='nLowerMidRange')
    nlowerrange = models.IntegerField(db_column='nLowerRange')
    nmediumitemweighting = models.IntegerField(db_column='nMediumItemWeighting')
    npercentagechancezeroitems = models.IntegerField(db_column='nPercentageChanceZeroItems')
    nsmallitemweighting = models.IntegerField(db_column='nSmallItemWeighting')
    nuppermidrange = models.IntegerField(db_column='nUpperMidRange')
    nupperrange = models.IntegerField(db_column='nUpperRange')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'OWAItemSpawnRules'


class Onfootdeathanimations(models.Model):
    id = models.IntegerField(primary_key=True)
    sanimname = models.TextField(db_column='sAnimName')
    eonfootdeathanimation = models.IntegerField(db_column='eOnFootDeathAnimation')
    bretainmomentum = models.IntegerField(db_column='bRetainMomentum')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'OnFootDeathAnimations'


class Openworldconstant(models.Model):
    id = models.IntegerField(primary_key=True)
    fvalue = models.FloatField(db_column='fValue')
    eopenworldconstant = models.IntegerField(db_column='eOpenWorldConstant')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'OpenWorldConstant'


class Openworlddropoffs(models.Model):
    id = models.IntegerField(primary_key=True)
    ehudmarkertype = models.IntegerField(db_column='eHUDMarkerType')
    eopenworlddropoff = models.IntegerField(db_column='eOpenWorldDropOff')
    fcycledurationseconds = models.FloatField(db_column='fCycleDurationSeconds')
    fpointreplenishmentpercycle = models.FloatField(db_column='fPointReplenishmentPerCycle')
    ndeliverypoints = models.IntegerField(db_column='nDeliveryPoints')
    efaction = models.IntegerField(db_column='eFaction')
    efactionhudmarkerfilter = models.IntegerField(db_column='eFactionHUDMarkerFilter')
    etaskitemsize_0 = models.IntegerField(db_column='eTaskItemSize_0')
    etaskitemsize_1 = models.IntegerField(db_column='eTaskItemSize_1')
    etaskitemsize_2 = models.IntegerField(db_column='eTaskItemSize_2')
    etaskitemsize_3 = models.IntegerField(db_column='eTaskItemSize_3')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'OpenWorldDropOffs'


class Openworldoperations(models.Model):
    id = models.IntegerField(primary_key=True)
    suidescription = models.TextField(db_column='sUIDescription')
    suititle = models.TextField(db_column='sUITitle')
    eopenworldoperation = models.IntegerField(db_column='eOpenWorldOperation')
    euiicon = models.IntegerField(db_column='eUIIcon')
    ncsaduration = models.IntegerField(db_column='nCSADuration')
    enpcworldevent = models.IntegerField(db_column='eNPCWorldEvent')
    eopenworldcsa = models.IntegerField(db_column='eOpenWorldCSA')
    etaskoperationcategory = models.IntegerField(db_column='eTaskOperationCategory')
    ballowedonmission = models.IntegerField(db_column='bAllowedOnMission')
    buireticulehighlight = models.IntegerField(db_column='bUIReticuleHighlight')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'OpenWorldOperations'


class Openworldtargetactivities(models.Model):
    id = models.IntegerField(primary_key=True)
    eopenworldoperationcriminal = models.IntegerField(db_column='eOpenWorldOperationCriminal')
    eopenworldoperationenforcer = models.IntegerField(db_column='eOpenWorldOperationEnforcer')
    eopenworldtargetactivity = models.IntegerField(db_column='eOpenWorldTargetActivity')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'OpenWorldTargetActivities'


class Optioncategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sname = models.TextField(db_column='sName')
    eaccessrestrictions = models.IntegerField(db_column='eAccessRestrictions')
    eoptioncategory = models.IntegerField(db_column='eOptionCategory')
    eparent = models.IntegerField(db_column='eParent')
    binclude = models.IntegerField(db_column='bInclude')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'OptionCategories'


class Organisations(models.Model):
    id = models.IntegerField(primary_key=True)
    sname = models.TextField(db_column='sName')
    spicture = models.TextField(db_column='sPicture')
    ehudicon = models.IntegerField(db_column='eHUDIcon')
    eorganisationcontact = models.IntegerField(db_column='eOrganisationContact')
    eorganisationicon = models.IntegerField(db_column='eOrganisationIcon')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    efaction = models.IntegerField(db_column='eFaction')
    eorganisation = models.IntegerField(db_column='eOrganisation')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'Organisations'


class Outfititemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sresource = models.TextField(db_column='sResource')
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'OutfitItemTypes'


class PawnhitreactionBonelists(models.Model):
    id = models.IntegerField(primary_key=True)
    svalue_0 = models.TextField(db_column='sValue_0')
    svalue_1 = models.TextField(db_column='sValue_1')
    svalue_2 = models.TextField(db_column='sValue_2')
    svalue_3 = models.TextField(db_column='sValue_3')
    svalue_4 = models.TextField(db_column='sValue_4')
    svalue_5 = models.TextField(db_column='sValue_5')
    svalue_6 = models.TextField(db_column='sValue_6')
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_BoneLists'


class PawnhitreactionBoneremaptables(models.Model):
    id = models.IntegerField(primary_key=True)
    sbonefrom = models.TextField(db_column='sBoneFrom')
    sboneto = models.TextField(db_column='sBoneTo')
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_BoneRemapTables'


class PawnhitreactionBools(models.Model):
    id = models.IntegerField(primary_key=True)
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction')
    bvalue = models.IntegerField(db_column='bValue')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_Bools'


class PawnhitreactionConstrainedbonelists(models.Model):
    id = models.IntegerField(primary_key=True)
    svalue_0 = models.TextField(db_column='sValue_0')
    svalue_1 = models.TextField(db_column='sValue_1')
    svalue_2 = models.TextField(db_column='sValue_2')
    svalue_3 = models.TextField(db_column='sValue_3')
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_ConstrainedBoneLists'


class PawnhitreactionFloats(models.Model):
    id = models.IntegerField(primary_key=True)
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction')
    fvalue = models.FloatField(db_column='fValue')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_Floats'


class PawnhitreactionSpringlists(models.Model):
    id = models.IntegerField(primary_key=True)
    svalue_0 = models.TextField(db_column='sValue_0')
    svalue_1 = models.TextField(db_column='sValue_1')
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_SpringLists'


class PawnhitreactionVector2Ds(models.Model):
    id = models.IntegerField(primary_key=True)
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction')
    fx = models.FloatField(db_column='fX')
    fy = models.FloatField(db_column='fY')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PawnHitReaction_Vector2Ds'


class Pawnhitreactions(models.Model):
    id = models.IntegerField(primary_key=True)
    epawnhitreaction = models.IntegerField(db_column='ePawnHitReaction')
    etype = models.IntegerField(db_column='eType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PawnHitReactions'


class Pedavoidanimation(models.Model):
    id = models.IntegerField(primary_key=True)
    savoidanimationleft = models.TextField(db_column='sAvoidAnimationLeft')
    savoidanimationright = models.TextField(db_column='sAvoidAnimationRight')
    eavoidanimationcategory = models.IntegerField(db_column='eAvoidAnimationCategory')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PedAvoidAnimation'


class Pedavoidanimationcategory(models.Model):
    id = models.IntegerField(primary_key=True)
    epedavoidanimationcategory = models.IntegerField(db_column='ePedAvoidAnimationCategory')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PedAvoidAnimationCategory'


class Pedwalkandrunvariations(models.Model):
    id = models.IntegerField(primary_key=True)
    sanimation = models.TextField(db_column='sAnimation')
    epedavoidanimationcategory = models.IntegerField(db_column='ePedAvoidAnimationCategory')
    epedwalkandrunvariation = models.IntegerField(db_column='ePedWalkAndRunVariation')
    fbasespeed = models.FloatField(db_column='fBaseSpeed')
    egender = models.IntegerField(db_column='eGender')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PedWalkAndRunVariations'


class Pedestrianassets(models.Model):
    id = models.IntegerField(primary_key=True)
    sasset = models.TextField(db_column='sAsset')
    eaudiotype = models.IntegerField(db_column='eAudioType')
    enpctype = models.IntegerField(db_column='eNPCType')
    epedestrianasset = models.IntegerField(db_column='ePedestrianAsset')
    eracetype = models.IntegerField(db_column='eRaceType')
    ewalkstyle = models.IntegerField(db_column='eWalkStyle')
    epedestrianpalettetype = models.IntegerField(db_column='ePedestrianPaletteType')
    bhighheels = models.IntegerField(db_column='bHighHeels')
    bshoelaces = models.IntegerField(db_column='bShoeLaces')
    bwristwatch = models.IntegerField(db_column='bWristWatch')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PedestrianAssets'


class Pedestrianevents(models.Model):
    id = models.IntegerField(primary_key=True)
    nignoreme = models.IntegerField(db_column='nIgnoreMe')
    enpcevent = models.IntegerField(db_column='eNPCEvent')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PedestrianEvents'


class Pedestrianpalettecolours(models.Model):
    id = models.IntegerField(primary_key=True)
    fblue = models.FloatField(db_column='fBlue')
    fgreen = models.FloatField(db_column='fGreen')
    fred = models.FloatField(db_column='fRed')
    ncolourindex = models.IntegerField(db_column='nColourIndex')
    epedestrianpalettetype = models.IntegerField(db_column='ePedestrianPaletteType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PedestrianPaletteColours'


class Pedestrianttianimationoverrides(models.Model):
    id = models.IntegerField(primary_key=True)
    snpcanimation = models.TextField(db_column='sNPCAnimation')
    enpctype = models.IntegerField(db_column='eNPCType')
    epedestrianttireaction = models.IntegerField(db_column='ePedestrianTTIReaction')
    eplayeranimtype = models.IntegerField(db_column='ePlayerAnimType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PedestrianTTIAnimationOverrides'


class Pedestrianttianimations(models.Model):
    id = models.IntegerField(primary_key=True)
    snpcanimation = models.TextField(db_column='sNPCAnimation')
    epedestrianttireaction = models.IntegerField(db_column='ePedestrianTTIReaction')
    eplayeranimtype = models.IntegerField(db_column='ePlayerAnimType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PedestrianTTIAnimations'


class Pedestrianttireactionoverrides(models.Model):
    id = models.IntegerField(primary_key=True)
    scancelaudioevent = models.TextField(db_column='sCancelAudioEvent')
    scompleteaudioevent = models.TextField(db_column='sCompleteAudioEvent')
    sstartaudioevent = models.TextField(db_column='sStartAudioEvent')
    enpctype = models.IntegerField(db_column='eNPCType')
    epedestrianttireaction = models.IntegerField(db_column='ePedestrianTTIReaction')
    ewhencancelled = models.IntegerField(db_column='eWhenCancelled')
    ewhencompleted = models.IntegerField(db_column='eWhenCompleted')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PedestrianTTIReactionOverrides'


class Pedestrianttireactions(models.Model):
    id = models.IntegerField(primary_key=True)
    scancelaudioevent = models.TextField(db_column='sCancelAudioEvent')
    scompleteaudioevent = models.TextField(db_column='sCompleteAudioEvent')
    sstartaudioevent = models.TextField(db_column='sStartAudioEvent')
    epedestrianttireaction = models.IntegerField(db_column='ePedestrianTTIReaction')
    ewhencancelled = models.IntegerField(db_column='eWhenCancelled')
    ewhencompleted = models.IntegerField(db_column='eWhenCompleted')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PedestrianTTIReactions'


class Pedestriantempsetups(models.Model):
    id = models.IntegerField(primary_key=True)
    stempsetupinfo = models.TextField(db_column='sTempSetupInfo')
    epedestriantempsetup = models.IntegerField(db_column='ePedestrianTempSetup')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PedestrianTempSetups'


class Pedestriantyperestrictions(models.Model):
    id = models.IntegerField(primary_key=True)
    enpctype = models.IntegerField(db_column='eNPCType')
    nnumconcurrentsetuptypes = models.IntegerField(db_column='nNumConcurrentSetupTypes')
    npedestriantyperestriction = models.IntegerField(db_column='nPedestrianTypeRestriction')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PedestrianTypeRestrictions'


class Playerroles(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    sdisplayname = models.TextField(db_column='sDisplayName')
    eactivities_0 = models.IntegerField(db_column='eActivities_0')
    eactivities_1 = models.IntegerField(db_column='eActivities_1')
    eactivities_2 = models.IntegerField(db_column='eActivities_2')
    efirstmilestone = models.IntegerField(db_column='eFirstMilestone')
    eplayerrole = models.IntegerField(db_column='ePlayerRole')
    fdisplayformulavalue = models.FloatField(db_column='fDisplayFormulaValue')
    nnummilestones = models.IntegerField(db_column='nNumMilestones')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    edisplayformulaoperation = models.IntegerField(db_column='eDisplayFormulaOperation')
    efaction = models.ForeignKey('Factions', db_column=u'eFaction')
    bachievement = models.IntegerField(db_column='bAchievement')
    bachievementhidden = models.IntegerField(db_column='bAchievementHidden')
    bshowtotalvalues = models.IntegerField(db_column='bShowTotalValues')
    sapbdb = models.TextField(db_column='sAPBDB')

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

    @property_cache
    def reward_count(self):
        count = 0
        for level in self.levels():
            count += len(level.items())
        return count

    class Meta:
        managed = False
        db_table = 'PlayerRoles'


class Populationtotals(models.Model):
    id = models.IntegerField(primary_key=True)
    edistricttype = models.IntegerField(db_column='eDistrictType')
    npopulationtotal = models.IntegerField(db_column='nPopulationTotal')
    ntotalpedestrians = models.IntegerField(db_column='nTotalPedestrians')
    ntotalvehicles = models.IntegerField(db_column='nTotalVehicles')
    etod = models.IntegerField(db_column='eTOD')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PopulationTotals'


class Popupdialogcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    ehighlightcolour = models.IntegerField(db_column='eHighlightColour')
    epopupdialogcategory = models.IntegerField(db_column='ePopupDialogCategory')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PopupDialogCategories'


class Popupdialogtriggersceneopen(models.Model):
    id = models.IntegerField(primary_key=True)
    seventname = models.TextField(db_column='sEventName')
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PopupDialogTriggerSceneOpen'


class PopupdialogtriggerCsaBegin(models.Model):
    id = models.IntegerField(primary_key=True)
    seventname = models.TextField(db_column='sEventName')
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_CSA_Begin'


class PopupdialogtriggerCsaEnd(models.Model):
    id = models.IntegerField(primary_key=True)
    seventname = models.TextField(db_column='sEventName')
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_CSA_End'


class PopupdialogtriggerGameplayevents(models.Model):
    id = models.IntegerField(primary_key=True)
    seventname = models.TextField(db_column='sEventName')
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_GamePlayEvents'


class PopupdialogtriggerGeneric(models.Model):
    id = models.IntegerField(primary_key=True)
    seventname = models.TextField(db_column='sEventName')
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_Generic'


class PopupdialogtriggerReticuleover(models.Model):
    id = models.IntegerField(primary_key=True)
    seventname = models.TextField(db_column='sEventName')
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_ReticuleOver'


class PopupdialogtriggerSceneclose(models.Model):
    id = models.IntegerField(primary_key=True)
    seventname = models.TextField(db_column='sEventName')
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_SceneClose'


class PopupdialogtriggerUieventPostonclick(models.Model):
    id = models.IntegerField(primary_key=True)
    seventname = models.TextField(db_column='sEventName')
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_UIEvent_PostOnClick'


class PopupdialogtriggerWorldspacezone(models.Model):
    id = models.IntegerField(primary_key=True)
    seventname = models.TextField(db_column='sEventName')
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PopupDialogTrigger_WorldSpaceZone'


class Popupdialogtriggers(models.Model):
    id = models.IntegerField(primary_key=True)
    edialogshown = models.IntegerField(db_column='eDialogShown')
    epopupdialogtrigger = models.IntegerField(db_column='ePopupDialogTrigger')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PopupDialogTriggers'


class Popupdialoguihighlightaggregation(models.Model):
    id = models.IntegerField(primary_key=True)
    swidget1 = models.TextField(db_column='sWidget1')
    swidget2 = models.TextField(db_column='sWidget2')
    swidget3 = models.TextField(db_column='sWidget3')
    swidget4 = models.TextField(db_column='sWidget4')
    swidget5 = models.TextField(db_column='sWidget5')
    epopupdialoguihighlightaggregation = models.IntegerField(db_column='ePopupDialogUIHighlightAggregation')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PopupDialogUIHighlightAggregation'


class Popupdialogs(models.Model):
    id = models.IntegerField(primary_key=True)
    spopupbody = models.TextField(db_column='sPopupBody')
    echainedpopup = models.IntegerField(db_column='eChainedPopup')
    eknowledgebaseurl = models.IntegerField(db_column='eKnowledgeBaseURL')
    eoptionalwaypoint = models.IntegerField(db_column='eOptionalWaypoint')
    epopupdialog = models.IntegerField(db_column='ePopupDialog')
    eposition = models.IntegerField(db_column='ePosition')
    euiwidgethightlight_aggregation = models.IntegerField(db_column='eUIWidgetHightlight_Aggregation')
    fdisplaytime = models.FloatField(db_column='fDisplayTime')
    ntimestoshow = models.IntegerField(db_column='nTimesToShow')
    epopupcategory = models.IntegerField(db_column='ePopupCategory')
    bdonotqueue = models.IntegerField(db_column='bDoNotQueue')
    bflushqueue = models.IntegerField(db_column='bFlushQueue')
    bforceknowledgebase = models.IntegerField(db_column='bForceKnowledgebase')
    bforchat = models.IntegerField(db_column='bForChat')
    bsuppresscriminal = models.IntegerField(db_column='bSuppressCriminal')
    bsuppressenforcer = models.IntegerField(db_column='bSuppressEnforcer')
    bsuppressmain = models.IntegerField(db_column='bSuppressMain')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PopupDialogs'


class Preloadaction(models.Model):
    id = models.IntegerField(primary_key=True)
    spreloadaction = models.TextField(db_column='sPreloadAction')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PreloadAction'


class Preloadcommon(models.Model):
    id = models.IntegerField(primary_key=True)
    spreloadcommon = models.TextField(db_column='sPreloadCommon')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PreloadCommon'


class Preloadcustomisations(models.Model):
    id = models.IntegerField(primary_key=True)
    spackage = models.TextField(db_column='sPackage')
    spreloadcustomisation = models.TextField(db_column='sPreloadCustomisation')
    bcoversbreasts = models.IntegerField(db_column='bCoversBreasts')
    bcoversgenitalia = models.IntegerField(db_column='bCoversGenitalia')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PreloadCustomisations'


class Preloadsocial(models.Model):
    id = models.IntegerField(primary_key=True)
    spreloadsocial = models.TextField(db_column='sPreloadSocial')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PreloadSocial'


class Prestigeeffects(models.Model):
    id = models.IntegerField(primary_key=True)
    eforcemaxlevel = models.IntegerField(db_column='eForceMaxLevel')
    eforceminlevel = models.IntegerField(db_column='eForceMinLevel')
    eprestigeeffect = models.IntegerField(db_column='ePrestigeEffect')
    eprestigelevellimit = models.IntegerField(db_column='ePrestigeLevelLimit')
    fquantity = models.FloatField(db_column='fQuantity')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PrestigeEffects'


class Prestigelevels(models.Model):
    id = models.IntegerField(primary_key=True)
    eheatlevel = models.IntegerField(db_column='eHeatLevel')
    eprestigelevel = models.IntegerField(db_column='ePrestigeLevel')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PrestigeLevels'


class Primitiveentries(models.Model):
    id = models.IntegerField(primary_key=True)
    epage = models.IntegerField(db_column='ePage')
    eprimitiveentry = models.IntegerField(db_column='ePrimitiveEntry')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PrimitiveEntries'


class Primitivepages(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayname = models.TextField(db_column='sDisplayName')
    eprimitivepage = models.IntegerField(db_column='ePrimitivePage')
    etype = models.IntegerField(db_column='eType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PrimitivePages'


class Primitiveunlockitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sresource = models.TextField(db_column='sResource')
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    nlegacydata = models.IntegerField(db_column='nLegacyData')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    etype = models.IntegerField(db_column='eType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'PrimitiveUnlockItemTypes'


class Probabilities(models.Model):
    id = models.IntegerField(primary_key=True)
    eprobability = models.IntegerField(db_column='eProbability')
    fcoefficient = models.FloatField(db_column='fCoefficient')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'Probabilities'


class Profanityfilterentries(models.Model):
    id = models.IntegerField(primary_key=True)
    sprofanityfilterentry = models.TextField(db_column='sProfanityFilterEntry')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ProfanityFilterEntries'


class Progressionfixups(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    nlatestversion = models.IntegerField(db_column='nLatestVersion')
    eprogressionfixup = models.IntegerField(db_column='eProgressionFixup')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ProgressionFixups'


class Provinggroundschallengemissionactivity(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    eexclude = models.IntegerField(db_column='eExclude')
    egameplayevent = models.IntegerField(db_column='eGameplayEvent')
    eprovinggroundschallengemissionactivity = models.IntegerField(db_column='eProvingGroundsChallengeMissionActivity')
    erarity = models.IntegerField(db_column='eRarity')
    nrequirement_0 = models.IntegerField(db_column='nRequirement_0')
    nrequirement_1 = models.IntegerField(db_column='nRequirement_1')
    nrequirement_2 = models.IntegerField(db_column='nRequirement_2')
    efaction = models.IntegerField(db_column='eFaction')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ProvingGroundsChallengeMissionActivity'


class Provinggroundschallengemissiontype(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    emissiontypefilter = models.IntegerField(db_column='eMissionTypeFilter')
    eprovinggroundschallengemissiontype = models.IntegerField(db_column='eProvingGroundsChallengeMissionType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ProvingGroundsChallengeMissionType'


class Provinggroundschallengestats(models.Model):
    id = models.IntegerField(primary_key=True)
    sdatabasecolumn = models.TextField(db_column='sDatabaseColumn')
    sdescription = models.TextField(db_column='sDescription')
    sdisplayname = models.TextField(db_column='sDisplayName')
    sdisplaynamepercentage = models.TextField(db_column='sDisplayNamePercentage')
    sdisplayscoreboard = models.TextField(db_column='sDisplayScoreboard')
    shudprogress = models.TextField(db_column='sHUDProgress')
    stitle = models.TextField(db_column='sTitle')
    eprovinggroundschallengestat = models.IntegerField(db_column='eProvingGroundsChallengeStat')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ProvingGroundsChallengeStats'


class Raceinfos(models.Model):
    id = models.IntegerField(primary_key=True)
    eraceinfo = models.IntegerField(db_column='eRaceInfo')
    eracetype = models.IntegerField(db_column='eRaceType')
    fb = models.FloatField(db_column='fB')
    fg = models.FloatField(db_column='fG')
    fr = models.FloatField(db_column='fR')
    ncolourindex = models.IntegerField(db_column='nColourIndex')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'RaceInfos'


class Racetyes(models.Model):
    id = models.IntegerField(primary_key=True)
    sname = models.TextField(db_column='sName')
    eracetype = models.IntegerField(db_column='eRaceType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'RaceTyes'


class Randomrewards(models.Model):
    id = models.IntegerField(primary_key=True)
    efirstweightedreward = models.IntegerField(db_column='eFirstWeightedReward')
    epurpose = models.IntegerField(db_column='ePurpose')
    erandomreward = models.IntegerField(db_column='eRandomReward')
    especificcontact = models.IntegerField(db_column='eSpecificContact')
    fchancepercentage_0 = models.FloatField(db_column='fChancePercentage_0')
    fchancepercentage_1 = models.FloatField(db_column='fChancePercentage_1')
    nnumweightedrewards = models.IntegerField(db_column='nNumWeightedRewards')
    especificorganisation = models.IntegerField(db_column='eSpecificOrganisation')
    bspecificuseonly = models.IntegerField(db_column='bSpecificUseOnly')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'RandomRewards'


class Randomtimelimitedrewards(models.Model):
    id = models.IntegerField(primary_key=True)
    edisabledrulesets = models.IntegerField(db_column='eDisabledRulesets')
    emissionsystemfilter = models.IntegerField(db_column='eMissionSystemFilter')
    erandomreward = models.IntegerField(db_column='eRandomReward')
    fdefaultmaxskillratingdifference = models.FloatField(db_column='fDefaultMaxSkillRatingDifference')
    ffailedmaximumtime = models.FloatField(db_column='fFailedMaximumTime')
    ffailedminimumtime = models.FloatField(db_column='fFailedMinimumTime')
    fminskillratingweight = models.FloatField(db_column='fMinSkillRatingWeight')
    fstandardmaximumtime = models.FloatField(db_column='fStandardMaximumTime')
    fstandardminimumtime = models.FloatField(db_column='fStandardMinimumTime')
    nmindistrictpop = models.IntegerField(db_column='nMinDistrictPop')
    bawardonloss = models.IntegerField(db_column='bAwardOnLoss')
    bawardonwin = models.IntegerField(db_column='bAwardOnWin')
    bonworldlevel = models.IntegerField(db_column='bOnWorldLevel')
    bresetatentry = models.IntegerField(db_column='bResetAtEntry')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'RandomTimeLimitedRewards'


class Rangedweapontype(models.Model):
    id = models.IntegerField(primary_key=True)
    eexplosiontype = models.IntegerField(db_column='eExplosionType')
    erecoil = models.IntegerField(db_column='eRecoil')
    eweapontype = models.IntegerField(db_column='eWeaponType')
    faccuracycooldown = models.FloatField(db_column='fAccuracyCooldown')
    faccuracypower = models.FloatField(db_column='fAccuracyPower')
    fcrouchmodifier = models.FloatField(db_column='fCrouchModifier')
    finvehiclemodifier = models.FloatField(db_column='fInVehicleModifier')
    fjumpmodifier = models.FloatField(db_column='fJumpModifier')
    fleanmodifier = models.FloatField(db_column='fLeanModifier')
    fmarksmanshipfov16_9 = models.FloatField(db_column='fMarksmanshipFOV16_9')
    fmarksmanshipfov4_3 = models.FloatField(db_column='fMarksmanshipFOV4_3')
    fmarksmanshipmodifier = models.FloatField(db_column='fMarksmanshipModifier')
    fmaxrange = models.FloatField(db_column='fMaxRange')
    fmaxtimebetweenshots = models.FloatField(db_column='fMaxTimeBetweenShots')
    fmindamagerange = models.FloatField(db_column='fMinDamageRange')
    fminimumcrosshairwidth = models.FloatField(db_column='fMinimumCrosshairWidth')
    fminimumdamagepercentage = models.FloatField(db_column='fMinimumDamagePercentage')
    foverallshotmodifiercap = models.FloatField(db_column='fOverallShotModifierCap')
    fpershotmodifier = models.FloatField(db_column='fPerShotModifier')
    fpiercedamagereduction = models.FloatField(db_column='fPierceDamageReduction')
    fpiercedamagescale = models.FloatField(db_column='fPierceDamageScale')
    fradiusattenmetres = models.FloatField(db_column='fRadiusAtTenMetres')
    frampdistance = models.FloatField(db_column='fRampDistance')
    frayspreadattenmetres = models.FloatField(db_column='fRaySpreadAtTenMetres')
    frecoverydelay = models.FloatField(db_column='fRecoveryDelay')
    frecoverypersecond = models.FloatField(db_column='fRecoveryPerSecond')
    frunmodifier = models.FloatField(db_column='fRunModifier')
    fsprintmodifier = models.FloatField(db_column='fSprintModifier')
    fwalkmodifier = models.FloatField(db_column='fWalkModifier')
    fweaponswitchminaccuracy = models.FloatField(db_column='fWeaponSwitchMinAccuracy')
    nfreeammo = models.IntegerField(db_column='nFreeAmmo')
    nmaxpiercecount = models.IntegerField(db_column='nMaxPierceCount')
    nminnumshots = models.IntegerField(db_column='nMinNumShots')
    nrayspershot = models.IntegerField(db_column='nRaysPerShot')
    ntracerfrequency = models.IntegerField(db_column='nTracerFrequency')
    bcanhitownvehicle = models.IntegerField(db_column='bCanHitOwnVehicle')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'RangedWeaponType'


class Ratingbands(models.Model):
    id = models.IntegerField(primary_key=True)
    fthreatincrement = models.FloatField(db_column='fThreatIncrement')
    nbegins = models.IntegerField(db_column='nBegins')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'RatingBands'


class Ratingtextures(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplaynamecrim = models.TextField(db_column='sDisplayNameCrim')
    sdisplaynameenf = models.TextField(db_column='sDisplayNameEnf')
    ehudiconcombocriminal_0 = models.IntegerField(db_column='eHUDIconComboCriminal_0')
    ehudiconcombocriminal_1 = models.IntegerField(db_column='eHUDIconComboCriminal_1')
    ehudiconcombocriminal_2 = models.IntegerField(db_column='eHUDIconComboCriminal_2')
    ehudiconcombocriminal_3 = models.IntegerField(db_column='eHUDIconComboCriminal_3')
    ehudiconcombocriminal_4 = models.IntegerField(db_column='eHUDIconComboCriminal_4')
    ehudiconcomboenforcer_0 = models.IntegerField(db_column='eHUDIconComboEnforcer_0')
    ehudiconcomboenforcer_1 = models.IntegerField(db_column='eHUDIconComboEnforcer_1')
    ehudiconcomboenforcer_2 = models.IntegerField(db_column='eHUDIconComboEnforcer_2')
    ehudiconcomboenforcer_3 = models.IntegerField(db_column='eHUDIconComboEnforcer_3')
    ehudiconcomboenforcer_4 = models.IntegerField(db_column='eHUDIconComboEnforcer_4')
    ehudtextureiconcriminal_0 = models.IntegerField(db_column='eHUDTextureIconCriminal_0')
    ehudtextureiconcriminal_1 = models.IntegerField(db_column='eHUDTextureIconCriminal_1')
    ehudtextureiconcriminal_2 = models.IntegerField(db_column='eHUDTextureIconCriminal_2')
    ehudtextureiconcriminal_3 = models.IntegerField(db_column='eHUDTextureIconCriminal_3')
    ehudtextureiconcriminal_4 = models.IntegerField(db_column='eHUDTextureIconCriminal_4')
    ehudtextureiconenforcer_0 = models.IntegerField(db_column='eHUDTextureIconEnforcer_0')
    ehudtextureiconenforcer_1 = models.IntegerField(db_column='eHUDTextureIconEnforcer_1')
    ehudtextureiconenforcer_2 = models.IntegerField(db_column='eHUDTextureIconEnforcer_2')
    ehudtextureiconenforcer_3 = models.IntegerField(db_column='eHUDTextureIconEnforcer_3')
    ehudtextureiconenforcer_4 = models.IntegerField(db_column='eHUDTextureIconEnforcer_4')
    eratingtexture = models.IntegerField(db_column='eRatingTexture')
    escaleformiconcriminal_0 = models.IntegerField(db_column='eScaleformIconCriminal_0')
    escaleformiconcriminal_1 = models.IntegerField(db_column='eScaleformIconCriminal_1')
    escaleformiconcriminal_2 = models.IntegerField(db_column='eScaleformIconCriminal_2')
    escaleformiconcriminal_3 = models.IntegerField(db_column='eScaleformIconCriminal_3')
    escaleformiconcriminal_4 = models.IntegerField(db_column='eScaleformIconCriminal_4')
    escaleformiconenforcer_0 = models.IntegerField(db_column='eScaleformIconEnforcer_0')
    escaleformiconenforcer_1 = models.IntegerField(db_column='eScaleformIconEnforcer_1')
    escaleformiconenforcer_2 = models.IntegerField(db_column='eScaleformIconEnforcer_2')
    escaleformiconenforcer_3 = models.IntegerField(db_column='eScaleformIconEnforcer_3')
    escaleformiconenforcer_4 = models.IntegerField(db_column='eScaleformIconEnforcer_4')
    nrating = models.IntegerField(db_column='nRating')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'RatingTextures'


class Redeemablerewards(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    smailbody = models.TextField(db_column='sMailBody')
    smailsubject = models.TextField(db_column='sMailSubject')
    ehudicon = models.IntegerField(db_column='eHUDIcon')
    eredeemablereward = models.IntegerField(db_column='eRedeemableReward')
    ereward = models.IntegerField(db_column='eReward')
    nkey = models.IntegerField(db_column='nKey')
    efaction = models.IntegerField(db_column='eFaction')
    bignoresddvalidation = models.IntegerField(db_column='bIgnoreSddValidation')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'RedeemableRewards'


class Referafriendevents(models.Model):
    id = models.IntegerField(primary_key=True)
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    ereferafriendevent = models.IntegerField(db_column='eReferAFriendEvent')
    bunique = models.IntegerField(db_column='bUnique')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ReferAFriendEvents'


class Rewardpackagechildren(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    eitems_0 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_0', related_name='Rewardpackagechildren_eitems_0')
    eitems_1 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_1', related_name='Rewardpackagechildren_eitems_1')
    eitems_10 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_10', related_name='Rewardpackagechildren_eitems_10')
    eitems_11 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_11', related_name='Rewardpackagechildren_eitems_11')
    eitems_12 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_12', related_name='Rewardpackagechildren_eitems_12')
    eitems_13 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_13', related_name='Rewardpackagechildren_eitems_13')
    eitems_14 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_14', related_name='Rewardpackagechildren_eitems_14')
    eitems_15 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_15', related_name='Rewardpackagechildren_eitems_15')
    eitems_16 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_16', related_name='Rewardpackagechildren_eitems_16')
    eitems_17 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_17', related_name='Rewardpackagechildren_eitems_17')
    eitems_18 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_18', related_name='Rewardpackagechildren_eitems_18')
    eitems_19 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_19', related_name='Rewardpackagechildren_eitems_19')
    eitems_2 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_2', related_name='Rewardpackagechildren_eitems_2')
    eitems_20 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_20', related_name='Rewardpackagechildren_eitems_20')
    eitems_21 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_21', related_name='Rewardpackagechildren_eitems_21')
    eitems_22 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_22', related_name='Rewardpackagechildren_eitems_22')
    eitems_23 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_23', related_name='Rewardpackagechildren_eitems_23')
    eitems_24 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_24', related_name='Rewardpackagechildren_eitems_24')
    eitems_25 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_25', related_name='Rewardpackagechildren_eitems_25')
    eitems_26 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_26', related_name='Rewardpackagechildren_eitems_26')
    eitems_27 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_27', related_name='Rewardpackagechildren_eitems_27')
    eitems_28 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_28', related_name='Rewardpackagechildren_eitems_28')
    eitems_29 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_29', related_name='Rewardpackagechildren_eitems_29')
    eitems_3 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_3', related_name='Rewardpackagechildren_eitems_3')
    eitems_30 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_30', related_name='Rewardpackagechildren_eitems_30')
    eitems_31 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_31', related_name='Rewardpackagechildren_eitems_31')
    eitems_32 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_32', related_name='Rewardpackagechildren_eitems_32')
    eitems_33 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_33', related_name='Rewardpackagechildren_eitems_33')
    eitems_34 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_34', related_name='Rewardpackagechildren_eitems_34')
    eitems_35 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_35', related_name='Rewardpackagechildren_eitems_35')
    eitems_36 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_36', related_name='Rewardpackagechildren_eitems_36')
    eitems_37 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_37', related_name='Rewardpackagechildren_eitems_37')
    eitems_38 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_38', related_name='Rewardpackagechildren_eitems_38')
    eitems_39 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_39', related_name='Rewardpackagechildren_eitems_39')
    eitems_4 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_4', related_name='Rewardpackagechildren_eitems_4')
    eitems_5 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_5', related_name='Rewardpackagechildren_eitems_5')
    eitems_6 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_6', related_name='Rewardpackagechildren_eitems_6')
    eitems_7 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_7', related_name='Rewardpackagechildren_eitems_7')
    eitems_8 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_8', related_name='Rewardpackagechildren_eitems_8')
    eitems_9 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_9', related_name='Rewardpackagechildren_eitems_9')
    erewardpackagechild = models.IntegerField(db_column='eRewardPackageChild')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    bselectable = models.IntegerField(db_column='bSelectable')
    sapbdb = models.TextField(db_column='sAPBDB')

    @property_cache
    def items(self):
        items = []

        # Skip item lookups for empty row
        if self.pk is 0:
            return items

        # Get list of non-null eitems values
        item_ids = filter(lambda i: getattr(self, 'eitems_{0}_id'.format(i)), range(10))
        # Get list of found items
        items = map(lambda i: getattr(self, 'eitems_{0}'.format(i)), item_ids)

        return items

    class Meta:
        managed = False
        db_table = 'RewardPackageChildren'


class Rewardpackageitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    smailbody = models.TextField(db_column='sMailBody')
    smailsubject = models.TextField(db_column='sMailSubject')
    echeckunlock = models.IntegerField(db_column='eCheckUnlock')
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    erewardpackage = models.IntegerField(db_column='eRewardPackage')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    egenderrestriction = models.IntegerField(db_column='eGenderRestriction')
    bdescriptionshowsitems = models.IntegerField(db_column='bDescriptionShowsItems')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'RewardPackageItemTypes'


class Rewardpackages(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    echildpackage = models.ForeignKey('Rewardpackagechildren', db_column=u'eChildPackage')
    eitems_0 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_0', related_name='Rewardpackages_eitems_0')
    eitems_1 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_1', related_name='Rewardpackages_eitems_1')
    eitems_2 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_2', related_name='Rewardpackages_eitems_2')
    eitems_3 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_3', related_name='Rewardpackages_eitems_3')
    eitems_4 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_4', related_name='Rewardpackages_eitems_4')
    eitems_5 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_5', related_name='Rewardpackages_eitems_5')
    eitems_6 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_6', related_name='Rewardpackages_eitems_6')
    eitems_7 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_7', related_name='Rewardpackages_eitems_7')
    eitems_8 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_8', related_name='Rewardpackages_eitems_8')
    eitems_9 = models.ForeignKey('Inventoryitemtypes', db_column='eItems_9', related_name='Rewardpackages_eitems_9')
    erewardpackage = models.IntegerField(db_column='eRewardPackage')
    ncash = models.IntegerField(db_column='nCash')
    ncharges_0 = models.IntegerField(db_column='nCharges_0')
    ncharges_1 = models.IntegerField(db_column='nCharges_1')
    nrewardtokens_0 = models.IntegerField(db_column='nRewardTokens_0')
    nrewardtokens_1 = models.IntegerField(db_column='nRewardTokens_1')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    bsendmail = models.IntegerField(db_column='bSendMail')
    sapbdb = models.TextField(db_column='sAPBDB')

    @property_cache
    def items(self):
        items = []

        # Skip item lookups for empty row
        if self.pk is 0:
            return items

        # Get list of non-null eitems values
        item_ids = filter(lambda i: getattr(self, 'eitems_{0}_id'.format(i)), range(10))
        # Get list of found items
        items = map(lambda i: getattr(self, 'eitems_{0}'.format(i)), item_ids)

        # Add child package items
        if self.echildpackage_id != 0:
            items += self.echildpackage.items()

        return items

    class Meta:
        managed = False
        db_table = 'RewardPackages'


class Rolemilestoneformulae(models.Model):
    id = models.IntegerField(primary_key=True)
    erolemilestoneformula = models.IntegerField(db_column='eRoleMilestoneFormula')
    ba_optional = models.IntegerField(db_column='bA_Optional')
    ba_required = models.IntegerField(db_column='bA_Required')
    bb_optional = models.IntegerField(db_column='bB_Optional')
    bb_required = models.IntegerField(db_column='bB_Required')
    bc_optional = models.IntegerField(db_column='bC_Optional')
    bc_required = models.IntegerField(db_column='bC_Required')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'RoleMilestoneFormulae'


class Rolemilestones(models.Model):
    id = models.IntegerField(primary_key=True)
    siconoverlaytext = models.TextField(db_column='sIconOverlayText')
    srewardmailbody = models.TextField(db_column='sRewardMailBody')
    srewardmailsubject = models.TextField(db_column='sRewardMailSubject')
    stitle = models.TextField(db_column='sTitle')
    eformula = models.IntegerField(db_column='eFormula')
    ereward = models.ForeignKey('Rewardpackages', db_column=u'eReward')
    eroleicon = models.IntegerField(db_column='eRoleIcon')
    erolemilestone = models.IntegerField(db_column='eRoleMilestone')
    fpassmark_0 = models.FloatField(db_column='fPassMark_0')
    fpassmark_1 = models.FloatField(db_column='fPassMark_1')
    fpassmark_2 = models.FloatField(db_column='fPassMark_2')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    sapbdb = models.TextField(db_column='sAPBDB')

    def items(self):
        return self.ereward.items()

    class Meta:
        managed = False
        db_table = 'RoleMilestones'


class Rulesetexclusions(models.Model):
    id = models.IntegerField(primary_key=True)
    eruleset_0 = models.IntegerField(db_column='eRuleSet_0')
    eruleset_1 = models.IntegerField(db_column='eRuleSet_1')
    eruleset_2 = models.IntegerField(db_column='eRuleSet_2')
    eruleset_3 = models.IntegerField(db_column='eRuleSet_3')
    eruleset_4 = models.IntegerField(db_column='eRuleSet_4')
    eruleset_5 = models.IntegerField(db_column='eRuleSet_5')
    eruleset_6 = models.IntegerField(db_column='eRuleSet_6')
    eruleset_7 = models.IntegerField(db_column='eRuleSet_7')
    eruleset_8 = models.IntegerField(db_column='eRuleSet_8')
    eruleset_9 = models.IntegerField(db_column='eRuleSet_9')
    erulesetexclusion = models.IntegerField(db_column='eRuleSetExclusion')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'RuleSetExclusions'


class Scaleformcriticaltimers(models.Model):
    id = models.IntegerField(primary_key=True)
    sicon = models.TextField(db_column='sIcon')
    stext = models.TextField(db_column='sText')
    npriority = models.IntegerField(db_column='nPriority')
    escaleformcriticaltimer = models.IntegerField(db_column='eScaleformCriticalTimer')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ScaleformCriticalTimers'


class Scaleformicons(models.Model):
    id = models.IntegerField(primary_key=True)
    siconsetname = models.TextField(db_column='sIconSetName')
    smoviename = models.TextField(db_column='sMovieName')
    escaleformicon = models.IntegerField(db_column='eScaleformIcon')
    nframenumber = models.IntegerField(db_column='nFrameNumber')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ScaleformIcons'


class Scaleforminterfaces(models.Model):
    id = models.IntegerField(primary_key=True)
    sscene = models.TextField(db_column='sScene')
    elayer = models.IntegerField(db_column='eLayer')
    npriority = models.IntegerField(db_column='nPriority')
    elayoutmode = models.IntegerField(db_column='eLayoutMode')
    escaleforminterface = models.IntegerField(db_column='eScaleformInterface')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ScaleformInterfaces'


class Scaleformlayers(models.Model):
    id = models.IntegerField(primary_key=True)
    slayerbackground = models.TextField(db_column='sLayerBackground')
    escaleformlayer = models.IntegerField(db_column='eScaleformLayer')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    bblurwhenactive = models.IntegerField(db_column='bBlurWhenActive')
    bcaptureinput = models.IntegerField(db_column='bCaptureInput')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ScaleformLayers'


class Scenelayers(models.Model):
    id = models.IntegerField(primary_key=True)
    escenelayer = models.IntegerField(db_column='eSceneLayer')
    blimitopenfrequency = models.IntegerField(db_column='bLimitOpenFrequency')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'SceneLayers'


class Scorecategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    escorecategory = models.IntegerField(db_column='eScoreCategory')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ScoreCategories'


class Scoreboarddescriptions(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplaytext = models.TextField(db_column='sDisplayText')
    escoreboarddescription = models.IntegerField(db_column='eScoreboardDescription')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ScoreboardDescriptions'


class Securityviolations(models.Model):
    id = models.IntegerField(primary_key=True)
    scategory = models.TextField(db_column='sCategory')
    skickmessage = models.TextField(db_column='sKickMessage')
    nbandurationdays = models.IntegerField(db_column='nBanDurationDays')
    esecurityviolation = models.IntegerField(db_column='eSecurityViolation')
    bban = models.IntegerField(db_column='bBan')
    bkick = models.IntegerField(db_column='bKick')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'SecurityViolations'


class Shopuifilterrestrictions(models.Model):
    id = models.IntegerField(primary_key=True)
    eiteminfracategory = models.IntegerField(db_column='eItemInfraCategory')
    eshopuifilterrestriction = models.IntegerField(db_column='eShopUIFilterRestriction')
    eunlockvehiclecomponentcategory = models.IntegerField(db_column='eUnlockVehicleComponentCategory')
    eunlockweapontype = models.IntegerField(db_column='eUnlockWeaponType')
    eweapontype = models.IntegerField(db_column='eWeaponType')
    ecustomisable = models.IntegerField(db_column='eCustomisable')
    eitemcategory = models.IntegerField(db_column='eItemCategory')
    eitemsubcategory = models.IntegerField(db_column='eItemSubCategory')
    emodifierclass = models.IntegerField(db_column='eModifierClass')
    emodifiertype = models.IntegerField(db_column='eModifierType')
    eunlockitemcategory = models.IntegerField(db_column='eUnlockItemCategory')
    eunlockitemsubcategory = models.IntegerField(db_column='eUnlockItemSubCategory')
    eunlockmodifierclass = models.IntegerField(db_column='eUnlockModifierClass')
    eunlockmodifiertype = models.IntegerField(db_column='eUnlockModifierType')
    bembeddeditem = models.IntegerField(db_column='bEmbeddedItem')
    bequipable = models.IntegerField(db_column='bEquipable')
    bnotdeployed = models.IntegerField(db_column='bNotDeployed')
    btrade = models.IntegerField(db_column='bTrade')
    bunlockcapacity = models.IntegerField(db_column='bUnlockCapacity')
    bunlockemote = models.IntegerField(db_column='bUnlockEmote')
    bunlocksymbolprimitive = models.IntegerField(db_column='bUnlockSymbolPrimitive')
    bunlockvehiclecomponent = models.IntegerField(db_column='bUnlockVehicleComponent')
    bunused = models.IntegerField(db_column='bUnused')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ShopUIFilterRestrictions'


class Shopuifilters(models.Model):
    id = models.IntegerField(primary_key=True)
    sname = models.TextField(db_column='sName')
    eenable_0 = models.IntegerField(db_column='eEnable_0')
    eenable_1 = models.IntegerField(db_column='eEnable_1')
    eenable_2 = models.IntegerField(db_column='eEnable_2')
    eoption_0 = models.IntegerField(db_column='eOption_0')
    eoption_1 = models.IntegerField(db_column='eOption_1')
    eoption_2 = models.IntegerField(db_column='eOption_2')
    eoption_3 = models.IntegerField(db_column='eOption_3')
    eparent = models.IntegerField(db_column='eParent')
    eshop_0 = models.IntegerField(db_column='eShop_0')
    eshop_1 = models.IntegerField(db_column='eShop_1')
    eshop_2 = models.IntegerField(db_column='eShop_2')
    eshop_3 = models.IntegerField(db_column='eShop_3')
    eshop_4 = models.IntegerField(db_column='eShop_4')
    eshopuifilter = models.IntegerField(db_column='eShopUIFilter')
    ndefaultweighting = models.IntegerField(db_column='nDefaultWeighting')
    bdevonly = models.IntegerField(db_column='bDevOnly')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ShopUIFilters'


class Shopuishops(models.Model):
    id = models.IntegerField(primary_key=True)
    eshopuishop = models.IntegerField(db_column='eShopUIShop')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ShopUIShops'


class Skillratingconstants(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    fvalue = models.FloatField(db_column='fValue')
    eskillratingconstant = models.IntegerField(db_column='eSkillRatingConstant')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'SkillRatingConstants'


class Songitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sresource = models.TextField(db_column='sResource')
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'SongItemTypes'


class Spawnconstant(models.Model):
    id = models.IntegerField(primary_key=True)
    fvalue = models.FloatField(db_column='fValue')
    espawnconstant = models.IntegerField(db_column='eSpawnConstant')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'SpawnConstant'


class Spawnvariables(models.Model):
    id = models.IntegerField(primary_key=True)
    fspawndistanceafk = models.FloatField(db_column='fSpawnDistanceAFK')
    fspawndistanceobjectivemaximum = models.FloatField(db_column='fSpawnDistanceObjectiveMaximum')
    fspawndistanceobjectiveminimum = models.FloatField(db_column='fSpawnDistanceObjectiveMinimum')
    fspawndistanceopponentignored = models.FloatField(db_column='fSpawnDistanceOpponentIgnored')
    fspawndistanceopponentinvalid = models.FloatField(db_column='fSpawnDistanceOpponentInvalid')
    fspawndistanceoppositionspawnzone = models.FloatField(db_column='fSpawnDistanceOppositionSpawnZone')
    fspawndistanceotherspawnzone = models.FloatField(db_column='fSpawnDistanceOtherSpawnZone')
    fspawndistanceplayer = models.FloatField(db_column='fSpawnDistancePlayer')
    fspawndistanceteammateliving = models.FloatField(db_column='fSpawnDistanceTeamMateLiving')
    fspawnvehicledistanceopponent = models.FloatField(db_column='fSpawnVehicleDistanceOpponent')
    fspawnvehicledistanceplayermaximum = models.FloatField(db_column='fSpawnVehicleDistancePlayerMaximum')
    fspawnvehicledistanceplayerminimum = models.FloatField(db_column='fSpawnVehicleDistancePlayerMinimum')
    fspawnvehicleheightmaximum = models.FloatField(db_column='fSpawnVehicleHeightMaximum')
    fspawnwo = models.FloatField(db_column='fSpawnWo')
    fspawnwp = models.FloatField(db_column='fSpawnWp')
    erelaxationrule = models.IntegerField(db_column='eRelaxationRule')
    espawnvariable = models.IntegerField(db_column='eSpawnVariable')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'SpawnVariables'


class Streetname(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayedstreetname = models.TextField(db_column='sDisplayedStreetName')
    edistrict = models.IntegerField(db_column='eDistrict')
    estreetnameid = models.IntegerField(db_column='eStreetNameID')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'StreetName'


class Symboleditormenuentries(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayimage = models.TextField(db_column='sDisplayImage')
    sdisplaytext = models.TextField(db_column='sDisplayText')
    smenulevel = models.TextField(db_column='sMenuLevel')
    smenutag = models.TextField(db_column='sMenuTag')
    soptionalscene = models.TextField(db_column='sOptionalScene')
    esymboleditormenuentry = models.IntegerField(db_column='eSymbolEditorMenuEntry')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'SymbolEditorMenuEntries'


class Symbolitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sresource = models.TextField(db_column='sResource')
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'SymbolItemTypes'


class Tesprojectioninfos(models.Model):
    id = models.IntegerField(primary_key=True)
    fmaxvalueatpremiumlevel_0 = models.FloatField(db_column='fMaxValueAtPremiumLevel_0')
    fmaxvalueatpremiumlevel_1 = models.FloatField(db_column='fMaxValueAtPremiumLevel_1')
    etesprojectioninfo = models.IntegerField(db_column='eTESProjectionInfo')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TESProjectionInfos'


class TodEventAllowedtooverrides(models.Model):
    id = models.IntegerField(primary_key=True)
    eevent_allowedtooverride = models.IntegerField(db_column='eEvent_AllowedToOverride')
    etod_event = models.IntegerField(db_column='eTOD_Event')
    etod = models.IntegerField(db_column='eTOD')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TOD_Event_AllowedToOverrides'


class TodEvents(models.Model):
    id = models.IntegerField(primary_key=True)
    etod_event = models.IntegerField(db_column='eTOD_Event')
    eevent = models.IntegerField(db_column='eEvent')
    etod = models.IntegerField(db_column='eTOD')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TOD_Events'


class Taskitemboomboxes(models.Model):
    id = models.IntegerField(primary_key=True)
    samptype = models.TextField(db_column='sAmpType')
    efriendlyhudmarker = models.IntegerField(db_column='eFriendlyHUDMarker')
    eoppositionhudmarker = models.IntegerField(db_column='eOppositionHUDMarker')
    etaskitemboombox = models.IntegerField(db_column='eTaskItemBoomBox')
    fampattenuationscale = models.FloatField(db_column='fAmpAttenuationScale')
    fampvolume = models.FloatField(db_column='fAmpVolume')
    ffriendlyradius = models.FloatField(db_column='fFriendlyRadius')
    foppositionradius = models.FloatField(db_column='fOppositionRadius')
    fspeakereq1 = models.FloatField(db_column='fSpeakerEQ1')
    fspeakereq2 = models.FloatField(db_column='fSpeakerEQ2')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskItemBoomBoxes'


class Taskitemcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    sdisplayname = models.TextField(db_column='sDisplayName')
    etaskitemcategory = models.IntegerField(db_column='eTaskItemCategory')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskItemCategories'


class Taskitemdamagedpickups(models.Model):
    id = models.IntegerField(primary_key=True)
    sassetname = models.TextField(db_column='sAssetName')
    sdamagesfx = models.TextField(db_column='sDamageSFX')
    sdamagevfx = models.TextField(db_column='sDamageVFX')
    srecoversfx = models.TextField(db_column='sRecoverSFX')
    srecovervfx = models.TextField(db_column='sRecoverVFX')
    etaskitemvisual = models.IntegerField(db_column='eTaskItemVisual')
    bdetroyeddamagestate = models.IntegerField(db_column='bDetroyedDamageState')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskItemDamagedPickups'


class Taskitemeffects(models.Model):
    id = models.IntegerField(primary_key=True)
    stimedexplosivesfxend = models.TextField(db_column='sTimedExplosiveSFXEnd')
    stimedexplosivesfxstart = models.TextField(db_column='sTimedExplosiveSFXStart')
    eboombox = models.IntegerField(db_column='eBoomBox')
    eexplosion = models.IntegerField(db_column='eExplosion')
    etaskitemeffect = models.IntegerField(db_column='eTaskItemEffect')
    ffieldsupplierradius = models.FloatField(db_column='fFieldSupplierRadius')
    fjumpzmodifier = models.FloatField(db_column='fJumpZModifier')
    frepairmultiplier = models.FloatField(db_column='fRepairMultiplier')
    ftimedexplosionduration = models.FloatField(db_column='fTimedExplosionDuration')
    nfieldsupplieramount = models.IntegerField(db_column='nFieldSupplierAmount')
    nhealth = models.IntegerField(db_column='nHealth')
    nsymbolmaterialindex = models.IntegerField(db_column='nSymbolMaterialIndex')
    bdontbounce = models.IntegerField(db_column='bDontBounce')
    bhasgrip = models.IntegerField(db_column='bHasGrip')
    bhostssymbol = models.IntegerField(db_column='bHostsSymbol')
    bragdollondeath = models.IntegerField(db_column='bRagdollOnDeath')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskItemEffects'


class Taskitemgiftboxcontents(models.Model):
    id = models.IntegerField(primary_key=True)
    edefaultweaponskin = models.IntegerField(db_column='eDefaultWeaponSkin')
    efnmods_0 = models.IntegerField(db_column='eFnMods_0')
    efnmods_1 = models.IntegerField(db_column='eFnMods_1')
    efnmods_2 = models.IntegerField(db_column='eFnMods_2')
    eitemtype = models.IntegerField(db_column='eItemType')
    etaskitemgiftbox = models.IntegerField(db_column='eTaskItemGiftBox')
    nmaxextraitems = models.IntegerField(db_column='nMaxExtraItems')
    nminextraitems = models.IntegerField(db_column='nMinExtraItems')
    nweight = models.IntegerField(db_column='nWeight')
    bselectrandomskin = models.IntegerField(db_column='bSelectRandomSkin')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskItemGiftBoxContents'


class Taskitemgiftboxmodifierentries(models.Model):
    id = models.IntegerField(primary_key=True)
    ecategory = models.IntegerField(db_column='eCategory')
    eitem = models.IntegerField(db_column='eItem')
    etaskitemgiftboxmodifier = models.IntegerField(db_column='eTaskItemGiftBoxModifier')
    fweight = models.FloatField(db_column='fWeight')
    etheme = models.IntegerField(db_column='eTheme')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskItemGiftBoxModifierEntries'


class Taskitemgiftboxmodifiers(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskitemgiftboxmodifier = models.IntegerField(db_column='eTaskItemGiftBoxModifier')
    fchancenomod = models.FloatField(db_column='fChanceNoMod')
    fweightperlevel_0 = models.FloatField(db_column='fWeightPerLevel_0')
    fweightperlevel_1 = models.FloatField(db_column='fWeightPerLevel_1')
    fweightperlevel_2 = models.FloatField(db_column='fWeightPerLevel_2')
    fweightperlevel_3 = models.FloatField(db_column='fWeightPerLevel_3')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskItemGiftBoxModifiers'


class Taskitemgiftboxes(models.Model):
    id = models.IntegerField(primary_key=True)
    sactivevfx = models.TextField(db_column='sActiveVFX')
    sinactivevfx = models.TextField(db_column='sInactiveVFX')
    sstartactivesfx = models.TextField(db_column='sStartActiveSFX')
    sstopactivesfx = models.TextField(db_column='sStopActiveSFX')
    etaskitemgiftbox = models.IntegerField(db_column='eTaskItemGiftBox')
    factivationspintime = models.FloatField(db_column='fActivationSpinTime')
    faddeddropdirectionalvelocitymax = models.FloatField(db_column='fAddedDropDirectionalVelocityMax')
    faddeddropdirectionalvelocitymin = models.FloatField(db_column='fAddedDropDirectionalVelocityMin')
    faddeddropupvelocitymax = models.FloatField(db_column='fAddedDropUpVelocityMax')
    faddeddropupvelocitymin = models.FloatField(db_column='fAddedDropUpVelocityMin')
    fmaximumrotationspeed = models.FloatField(db_column='fMaximumRotationSpeed')
    frotationacceleration = models.FloatField(db_column='fRotationAcceleration')
    frotationspeed = models.FloatField(db_column='fRotationSpeed')
    fvfxoffsetx = models.FloatField(db_column='fVFXOffsetX')
    fvfxoffsety = models.FloatField(db_column='fVFXOffsetY')
    fvfxoffsetz = models.FloatField(db_column='fVFXOffsetZ')
    eavailability = models.IntegerField(db_column='eAvailability')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskItemGiftBoxes'


class Taskitemsizes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayname = models.TextField(db_column='sDisplayName')
    ncargopips = models.IntegerField(db_column='nCargoPips')
    eencumbrance = models.IntegerField(db_column='eEncumbrance')
    etaskitemsize = models.IntegerField(db_column='eTaskItemSize')
    bcancarry = models.IntegerField(db_column='bCanCarry')
    bslowpickup = models.IntegerField(db_column='bSlowPickup')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskItemSizes'


class Taskitemsubcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    sdisplayname = models.TextField(db_column='sDisplayName')
    egameplayobject = models.IntegerField(db_column='eGameplayObject')
    etaskitemsubcategory = models.IntegerField(db_column='eTaskItemSubCategory')
    etaskitemcategory = models.IntegerField(db_column='eTaskItemCategory')
    etaskitemsize = models.IntegerField(db_column='eTaskItemSize')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskItemSubCategories'


class Taskitemtags(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskitemtag = models.IntegerField(db_column='eTaskItemTag')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskItemTags'


class Taskitemvarieties(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    sdisplayname = models.TextField(db_column='sDisplayName')
    eeffect = models.IntegerField(db_column='eEffect')
    egiftbox = models.IntegerField(db_column='eGiftBox')
    ehudiconcombo = models.IntegerField(db_column='eHUDIconCombo')
    ehudmarkervisual = models.IntegerField(db_column='eHUDMarkerVisual')
    emetatag_0 = models.IntegerField(db_column='eMetaTag_0')
    emetatag_1 = models.IntegerField(db_column='eMetaTag_1')
    emetatag_2 = models.IntegerField(db_column='eMetaTag_2')
    etaskitemsubcategory = models.IntegerField(db_column='eTaskItemSubCategory')
    etaskitemvariety = models.IntegerField(db_column='eTaskItemVariety')
    etaskitemvisual = models.IntegerField(db_column='eTaskItemVisual')
    fgiftboxoffsetx = models.FloatField(db_column='fGiftBoxOffsetX')
    fgiftboxoffsety = models.FloatField(db_column='fGiftBoxOffsetY')
    fgiftboxoffsetz = models.FloatField(db_column='fGiftBoxOffsetZ')
    fvehicleheightreductionamount = models.FloatField(db_column='fVehicleHeightReductionAmount')
    fvehicletorquereductionfactor = models.FloatField(db_column='fVehicleTorqueReductionFactor')
    nexpensetariff = models.IntegerField(db_column='nExpenseTariff')
    bhidehudmarkerwhilecarried = models.IntegerField(db_column='bHideHUDMarkerWhileCarried')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskItemVarieties'


class Taskitemvisuals(models.Model):
    id = models.IntegerField(primary_key=True)
    spickupanimsetasset = models.TextField(db_column='sPickupAnimSetAsset')
    spickupanimtreeasset = models.TextField(db_column='sPickupAnimTreeAsset')
    spickupassetname = models.TextField(db_column='sPickupAssetName')
    spickupphysicsasset = models.TextField(db_column='sPickupPhysicsAsset')
    eitemattachmentvisual = models.IntegerField(db_column='eItemAttachmentVisual')
    etaskitemvisual = models.IntegerField(db_column='eTaskItemVisual')
    fcollisionheight = models.FloatField(db_column='fCollisionHeight')
    fpickupoffsetx = models.FloatField(db_column='fPickupOffsetX')
    fpickupoffsety = models.FloatField(db_column='fPickupOffsetY')
    fpickupoffsetz = models.FloatField(db_column='fPickupOffsetZ')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskItemVisuals'


class Taskobjectives(models.Model):
    id = models.IntegerField(primary_key=True)
    sdispatchbrief = models.TextField(db_column='sDispatchBrief')
    sownerbrief = models.TextField(db_column='sOwnerBrief')
    emissiontemplate = models.IntegerField(db_column='eMissionTemplate')
    eoperation = models.IntegerField(db_column='eOperation')
    etargetallocation = models.IntegerField(db_column='eTargetAllocation')
    etaskitemvariety = models.IntegerField(db_column='eTaskItemVariety')
    etaskobjective = models.IntegerField(db_column='eTaskObjective')
    evehiclecategory = models.IntegerField(db_column='eVehicleCategory')
    ntargetsrequired = models.IntegerField(db_column='nTargetsRequired')
    ntaskitemsavailable = models.IntegerField(db_column='nTaskItemsAvailable')
    ntaskitemsrequired = models.IntegerField(db_column='nTaskItemsRequired')
    ntimelimit = models.IntegerField(db_column='nTimeLimit')
    nvehiclesrequired = models.IntegerField(db_column='nVehiclesRequired')
    eitembatch = models.IntegerField(db_column='eItemBatch')
    eopposingsidevipassignment = models.IntegerField(db_column='eOpposingSideVIPAssignment')
    eowningsidevipassignment = models.IntegerField(db_column='eOwningSideVIPAssignment')
    estage = models.IntegerField(db_column='eStage')
    etaskitemspecificationmethod = models.IntegerField(db_column='eTaskItemSpecificationMethod')
    evehiclebatch = models.IntegerField(db_column='eVehicleBatch')
    bbonustime = models.IntegerField(db_column='bBonusTime')
    bclearopposingsideviptakeoutsonstart = models.IntegerField(db_column='bClearOpposingSideVIPTakeoutsOnStart')
    bclearowningsideviptakeoutsonstart = models.IntegerField(db_column='bClearOwningSideVIPTakeoutsOnStart')
    bcleartakeoutsonstart = models.IntegerField(db_column='bClearTakeoutsOnStart')
    bcompletesconcurrentpair = models.IntegerField(db_column='bCompletesConcurrentPair')
    bdisabletakeouts = models.IntegerField(db_column='bDisableTakeouts')
    bdrawontimeout = models.IntegerField(db_column='bDrawOnTimeOut')
    benabledpvp = models.IntegerField(db_column='bEnabledPvP')
    benableopposingsideviptakeouts = models.IntegerField(db_column='bEnableOpposingSideVIPTakeouts')
    benableowningsideviptakeouts = models.IntegerField(db_column='bEnableOwningSideVIPTakeouts')
    bendonlyontimeout = models.IntegerField(db_column='bEndOnlyOnTimeOut')
    bisconcurrent = models.IntegerField(db_column='bIsConcurrent')
    bisopposition = models.IntegerField(db_column='bIsOpposition')
    bleaveremainingtaskitems = models.IntegerField(db_column='bLeaveRemainingTaskItems')
    bopenworldcashpoolitem = models.IntegerField(db_column='bOpenWorldCashPoolItem')
    boppositionwinontargetdestroyedbyowners = models.IntegerField(db_column='bOppositionWinOnTargetDestroyedByOwners')
    bownerswinontargetdestroyedbyopponent = models.IntegerField(db_column='bOwnersWinOnTargetDestroyedByOpponent')
    bscorepointonwin = models.IntegerField(db_column='bScorePointOnWin')
    bspawnininventory = models.IntegerField(db_column='bSpawnInInventory')
    bwinoncompletion = models.IntegerField(db_column='bWinOnCompletion')
    bwinonunopposedcompletion = models.IntegerField(db_column='bWinOnUnopposedCompletion')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskObjectives'


class Taskoperationarmedguard(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    funused = models.FloatField(db_column='fUnused')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationArmedGuard'


class Taskoperationbusts(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    nhealthpool = models.IntegerField(db_column='nHealthPool')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationBusts'


class Taskoperationcsis(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    fcsaduration = models.FloatField(db_column='fCSADuration')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationCSIs'


class Taskoperationcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    ereticulehint = models.IntegerField(db_column='eReticuleHint')
    fmintakeoutmultiplier = models.FloatField(db_column='fMinTakeoutMultiplier')
    etaskoperationcategory = models.IntegerField(db_column='eTaskOperationCategory')
    bautoinstigateopposition = models.IntegerField(db_column='bAutoInstigateOpposition')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationCategories'


class Taskoperationdeathmatches(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    npadding = models.IntegerField(db_column='nPadding')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationDeathmatches'


class Taskoperationescape(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    farrestedpenaltyseconds = models.FloatField(db_column='fArrestedPenaltySeconds')
    farrestopponentpenaltyseconds = models.FloatField(db_column='fArrestOpponentPenaltySeconds')
    fescapebarlimit = models.FloatField(db_column='fEscapeBarLimit')
    fkilledpenaltyseconds = models.FloatField(db_column='fKilledPenaltySeconds')
    fkillopponentpenaltyseconds = models.FloatField(db_column='fKillOpponentPenaltySeconds')
    ftakedamagepenaltyseconds = models.FloatField(db_column='fTakeDamagePenaltySeconds')
    fweaponfirepenaltyseconds = models.FloatField(db_column='fWeaponFirePenaltySeconds')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationEscape'


class Taskoperationescort(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    ftriggertime = models.FloatField(db_column='fTriggerTime')
    bvipopponentcancapture = models.IntegerField(db_column='bVIPOpponentCanCapture')
    bwinontimeout = models.IntegerField(db_column='bWinOnTimeout')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationEscort'


class Taskoperationhacking(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    fcsaduration = models.FloatField(db_column='fCSADuration')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationHacking'


class Taskoperationmovingtarget(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    npadding = models.IntegerField(db_column='nPadding')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationMovingTarget'


class Taskoperationpickups(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    npadding = models.IntegerField(db_column='nPadding')
    bisvehicledeliverable = models.IntegerField(db_column='bIsVehicleDeliverable')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationPickups'


class Taskoperationsabotages(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    fcsaduration = models.FloatField(db_column='fCSADuration')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationSabotages'


class Taskoperationsurvival(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    npadding = models.IntegerField(db_column='nPadding')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationSurvival'


class Taskoperationterritorycontrols(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    fcapturetime = models.FloatField(db_column='fCaptureTime')
    fresettime = models.FloatField(db_column='fResetTime')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationTerritoryControls'


class Taskoperationuiprofile(models.Model):
    id = models.IntegerField(primary_key=True)
    scriminalbrief = models.TextField(db_column='sCriminalBrief')
    senforcerbrief = models.TextField(db_column='sEnforcerBrief')
    sshortbrief = models.TextField(db_column='sShortBrief')
    strackedvaluedescription_0 = models.TextField(db_column='sTrackedValueDescription_0')
    strackedvaluedescription_1 = models.TextField(db_column='sTrackedValueDescription_1')
    strackedvaluedescription_2 = models.TextField(db_column='sTrackedValueDescription_2')
    strackedvaluedescription_3 = models.TextField(db_column='sTrackedValueDescription_3')
    strackedvalueimage_0 = models.TextField(db_column='sTrackedValueImage_0')
    strackedvalueimage_1 = models.TextField(db_column='sTrackedValueImage_1')
    strackedvalueimage_2 = models.TextField(db_column='sTrackedValueImage_2')
    strackedvalueimage_3 = models.TextField(db_column='sTrackedValueImage_3')
    etaskoperationuiprofile = models.IntegerField(db_column='eTaskOperationUIProfile')
    etrackedstateprofile_0 = models.IntegerField(db_column='eTrackedStateProfile_0')
    etrackedstateprofile_1 = models.IntegerField(db_column='eTrackedStateProfile_1')
    etrackedstateprofile_2 = models.IntegerField(db_column='eTrackedStateProfile_2')
    etrackedstateprofile_3 = models.IntegerField(db_column='eTrackedStateProfile_3')
    etrackedvaluebarfgdisabled_0 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_0')
    etrackedvaluebarfgdisabled_1 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_1')
    etrackedvaluebarfgdisabled_2 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_2')
    etrackedvaluebarfgdisabled_3 = models.IntegerField(db_column='eTrackedValueBarFgDisabled_3')
    etrackedvaluebg_0 = models.IntegerField(db_column='eTrackedValueBg_0')
    etrackedvaluebg_1 = models.IntegerField(db_column='eTrackedValueBg_1')
    etrackedvaluebg_2 = models.IntegerField(db_column='eTrackedValueBg_2')
    etrackedvaluebg_3 = models.IntegerField(db_column='eTrackedValueBg_3')
    etrackedvaluefg_0 = models.IntegerField(db_column='eTrackedValueFg_0')
    etrackedvaluefg_1 = models.IntegerField(db_column='eTrackedValueFg_1')
    etrackedvaluefg_2 = models.IntegerField(db_column='eTrackedValueFg_2')
    etrackedvaluefg_3 = models.IntegerField(db_column='eTrackedValueFg_3')
    etrackedvaluesocket_0 = models.IntegerField(db_column='eTrackedValueSocket_0')
    etrackedvaluesocket_1 = models.IntegerField(db_column='eTrackedValueSocket_1')
    etrackedvaluesocket_2 = models.IntegerField(db_column='eTrackedValueSocket_2')
    etrackedvaluesocket_3 = models.IntegerField(db_column='eTrackedValueSocket_3')
    ntrackedvaluestageoffset_0 = models.IntegerField(db_column='nTrackedValueStageOffset_0')
    ntrackedvaluestageoffset_1 = models.IntegerField(db_column='nTrackedValueStageOffset_1')
    ntrackedvaluestageoffset_2 = models.IntegerField(db_column='nTrackedValueStageOffset_2')
    ntrackedvaluestageoffset_3 = models.IntegerField(db_column='nTrackedValueStageOffset_3')
    etrackedvalue_0 = models.IntegerField(db_column='eTrackedValue_0')
    etrackedvalue_1 = models.IntegerField(db_column='eTrackedValue_1')
    etrackedvalue_2 = models.IntegerField(db_column='eTrackedValue_2')
    etrackedvalue_3 = models.IntegerField(db_column='eTrackedValue_3')
    etrackedvaluedisplay_0 = models.IntegerField(db_column='eTrackedValueDisplay_0')
    etrackedvaluedisplay_1 = models.IntegerField(db_column='eTrackedValueDisplay_1')
    etrackedvaluedisplay_2 = models.IntegerField(db_column='eTrackedValueDisplay_2')
    etrackedvaluedisplay_3 = models.IntegerField(db_column='eTrackedValueDisplay_3')
    bflashwhenchanged_0 = models.IntegerField(db_column='bFlashWhenChanged_0')
    bflashwhenchanged_1 = models.IntegerField(db_column='bFlashWhenChanged_1')
    bflashwhenchanged_2 = models.IntegerField(db_column='bFlashWhenChanged_2')
    bflashwhenchanged_3 = models.IntegerField(db_column='bFlashWhenChanged_3')
    bhideatmax_0 = models.IntegerField(db_column='bHideAtMax_0')
    bhideatmax_1 = models.IntegerField(db_column='bHideAtMax_1')
    bhideatmax_2 = models.IntegerField(db_column='bHideAtMax_2')
    bhideatmax_3 = models.IntegerField(db_column='bHideAtMax_3')
    bhidenamewhendisabled_0 = models.IntegerField(db_column='bHideNameWhenDisabled_0')
    bhidenamewhendisabled_1 = models.IntegerField(db_column='bHideNameWhenDisabled_1')
    bhidenamewhendisabled_2 = models.IntegerField(db_column='bHideNameWhenDisabled_2')
    bhidenamewhendisabled_3 = models.IntegerField(db_column='bHideNameWhenDisabled_3')
    bhidewhenone_0 = models.IntegerField(db_column='bHideWhenOne_0')
    bhidewhenone_1 = models.IntegerField(db_column='bHideWhenOne_1')
    bhidewhenone_2 = models.IntegerField(db_column='bHideWhenOne_2')
    bhidewhenone_3 = models.IntegerField(db_column='bHideWhenOne_3')
    bhidewhenoppositionviptakeoutsdisabled_0 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_0')
    bhidewhenoppositionviptakeoutsdisabled_1 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_1')
    bhidewhenoppositionviptakeoutsdisabled_2 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_2')
    bhidewhenoppositionviptakeoutsdisabled_3 = models.IntegerField(db_column='bHideWhenOppositionVIPTakeoutsDisabled_3')
    bhidewhenownerviptakeoutsdisabled_0 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_0')
    bhidewhenownerviptakeoutsdisabled_1 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_1')
    bhidewhenownerviptakeoutsdisabled_2 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_2')
    bhidewhenownerviptakeoutsdisabled_3 = models.IntegerField(db_column='bHideWhenOwnerVIPTakeoutsDisabled_3')
    bhidewhenpointsdisabled_0 = models.IntegerField(db_column='bHideWhenPointsDisabled_0')
    bhidewhenpointsdisabled_1 = models.IntegerField(db_column='bHideWhenPointsDisabled_1')
    bhidewhenpointsdisabled_2 = models.IntegerField(db_column='bHideWhenPointsDisabled_2')
    bhidewhenpointsdisabled_3 = models.IntegerField(db_column='bHideWhenPointsDisabled_3')
    bhidewhentakeoutsdisabled_0 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_0')
    bhidewhentakeoutsdisabled_1 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_1')
    bhidewhentakeoutsdisabled_2 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_2')
    bhidewhentakeoutsdisabled_3 = models.IntegerField(db_column='bHideWhenTakeoutsDisabled_3')
    bhidewhenunopposed_0 = models.IntegerField(db_column='bHideWhenUnopposed_0')
    bhidewhenunopposed_1 = models.IntegerField(db_column='bHideWhenUnopposed_1')
    bhidewhenunopposed_2 = models.IntegerField(db_column='bHideWhenUnopposed_2')
    bhidewhenunopposed_3 = models.IntegerField(db_column='bHideWhenUnopposed_3')
    btrackedvalueinoverview_0 = models.IntegerField(db_column='bTrackedValueInOverview_0')
    btrackedvalueinoverview_1 = models.IntegerField(db_column='bTrackedValueInOverview_1')
    btrackedvalueinoverview_2 = models.IntegerField(db_column='bTrackedValueInOverview_2')
    btrackedvalueinoverview_3 = models.IntegerField(db_column='bTrackedValueInOverview_3')
    btrackedvalueonhud_0 = models.IntegerField(db_column='bTrackedValueOnHUD_0')
    btrackedvalueonhud_1 = models.IntegerField(db_column='bTrackedValueOnHUD_1')
    btrackedvalueonhud_2 = models.IntegerField(db_column='bTrackedValueOnHUD_2')
    btrackedvalueonhud_3 = models.IntegerField(db_column='bTrackedValueOnHUD_3')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationUIProfile'


class Taskoperationvehiclecargos(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    fcsaduration = models.FloatField(db_column='fCSADuration')
    bisvehicledeliverable = models.IntegerField(db_column='bIsVehicleDeliverable')
    bvehiclelocked = models.IntegerField(db_column='bVehicleLocked')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationVehicleCargos'


class Taskoperations(models.Model):
    id = models.IntegerField(primary_key=True)
    scriminalbrief = models.TextField(db_column='sCriminalBrief')
    senforcerbrief = models.TextField(db_column='sEnforcerBrief')
    suidescription = models.TextField(db_column='sUIDescription')
    emissionuiprofile = models.IntegerField(db_column='eMissionUIProfile')
    emissionuiprofileopposition = models.IntegerField(db_column='eMissionUIProfileOpposition')
    eoppositiontargethudmarker = models.IntegerField(db_column='eOppositionTargetHUDMarker')
    eoutofmissiontargethudmarker = models.IntegerField(db_column='eOutOfMissionTargetHUDMarker')
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    etasktargethudmarker = models.IntegerField(db_column='eTaskTargetHUDMarker')
    nobjectiveholdpointstarget = models.IntegerField(db_column='nObjectiveHoldPointsTarget')
    enpcworldevent = models.IntegerField(db_column='eNPCWorldEvent')
    eoppositionitemvisibility = models.IntegerField(db_column='eOppositionItemVisibility')
    eoutofmissionitemvisibility = models.IntegerField(db_column='eOutOfMissionItemVisibility')
    eowneritemvisibility = models.IntegerField(db_column='eOwnerItemVisibility')
    etaskoperationcategory = models.IntegerField(db_column='eTaskOperationCategory')
    etasktargetclass = models.IntegerField(db_column='eTaskTargetClass')
    banysidecaninitiate = models.IntegerField(db_column='bAnySideCanInitiate')
    bhidealldeliverablesfromopposition = models.IntegerField(db_column='bHideAllDeliverablesFromOpposition')
    bhidealldeliverablesfromowners = models.IntegerField(db_column='bHideAllDeliverablesFromOwners')
    boppositioncancarrytaskitems = models.IntegerField(db_column='bOppositionCanCarryTaskItems')
    boppositioncaninteractwithvehicles = models.IntegerField(db_column='bOppositionCanInteractWithVehicles')
    boutofmissioncaninteract = models.IntegerField(db_column='bOutOfMissionCanInteract')
    bownerscancarrytaskitems = models.IntegerField(db_column='bOwnersCanCarryTaskItems')
    bownerscaninteractwithvehicles = models.IntegerField(db_column='bOwnersCanInteractWithVehicles')
    bshowoppositiontotaskgroup = models.IntegerField(db_column='bShowOppositionToTaskGroup')
    bshowtaskgrouptoopposition = models.IntegerField(db_column='bShowTaskGroupToOpposition')
    buseobjectiveholdpoints = models.IntegerField(db_column='bUseObjectiveHoldPoints')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperations'


class Taskoperationsarson(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    fcsaduration = models.FloatField(db_column='fCSADuration')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationsArson'


class Taskoperationsbombing(models.Model):
    id = models.IntegerField(primary_key=True)
    ebomblevel = models.IntegerField(db_column='eBombLevel')
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    fbombdisposalguardtime = models.FloatField(db_column='fBombDisposalGuardTime')
    fcsaduration = models.FloatField(db_column='fCSADuration')
    ffusetimer = models.FloatField(db_column='fFuseTimer')
    bisbombdefusable = models.IntegerField(db_column='bIsBombDefusable')
    bisbombrearmable = models.IntegerField(db_column='bIsBombRearmable')
    btriggeronallbombsdefused = models.IntegerField(db_column='bTriggerOnAllBombsDefused')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationsBombing'


class Taskoperationsbuildingbreakin(models.Model):
    id = models.IntegerField(primary_key=True)
    suseactionname = models.TextField(db_column='sUseActionName')
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    fcsaduration = models.FloatField(db_column='fCSADuration')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationsBuildingBreakIn'


class Taskoperationsgraffiti(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    nsprayduration = models.IntegerField(db_column='nSprayDuration')
    bisresprayable = models.IntegerField(db_column='bIsResprayable')
    bstartsneutral = models.IntegerField(db_column='bStartsNeutral')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationsGraffiti'


class Taskoperationsitemdelivery(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    ftriggertime = models.FloatField(db_column='fTriggerTime')
    bdelivertoalltargets = models.IntegerField(db_column='bDeliverToAllTargets')
    bdelivervehicle = models.IntegerField(db_column='bDeliverVehicle')
    bdelivervehiclecargo = models.IntegerField(db_column='bDeliverVehicleCargo')
    bremovedeliverables = models.IntegerField(db_column='bRemoveDeliverables')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationsItemDelivery'


class Taskoperationsnpc(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    fcsaduration = models.FloatField(db_column='fCSADuration')
    ecsastate = models.IntegerField(db_column='eCSAState')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationsNPC'


class Taskoperationsramraid(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    nhealthpool = models.IntegerField(db_column='nHealthPool')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationsRamRaid'


class Taskoperationsrendezvous(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    ftriggertime = models.FloatField(db_column='fTriggerTime')
    ballsidemembers = models.IntegerField(db_column='bAllSideMembers')
    ballsimultaneously = models.IntegerField(db_column='bAllSimultaneously')
    biscoopcheckpoint = models.IntegerField(db_column='bIsCoopCheckpoint')
    bvehiclerequired = models.IntegerField(db_column='bVehicleRequired')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationsRendezvous'


class Taskoperationsvandalism(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    nhealthpool = models.IntegerField(db_column='nHealthPool')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationsVandalism'


class Taskoperationsvehiclelooting(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    fcsaduration = models.FloatField(db_column='fCSADuration')
    bisvehicledeliverable = models.IntegerField(db_column='bIsVehicleDeliverable')
    bvehiclelocked = models.IntegerField(db_column='bVehicleLocked')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationsVehicleLooting'


class Taskoperationsvehicletheft(models.Model):
    id = models.IntegerField(primary_key=True)
    etaskoperation = models.IntegerField(db_column='eTaskOperation')
    fcsaduration = models.FloatField(db_column='fCSADuration')
    npointlessextrapadding = models.IntegerField(db_column='nPointlessExtraPadding')
    bisvehicledeliverable = models.IntegerField(db_column='bIsVehicleDeliverable')
    bvehiclelocked = models.IntegerField(db_column='bVehicleLocked')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskOperationsVehicleTheft'


class Tasktargetallocations(models.Model):
    id = models.IntegerField(primary_key=True)
    elocationconstraint = models.IntegerField(db_column='eLocationConstraint')
    emissiontemplate = models.IntegerField(db_column='eMissionTemplate')
    etasktargetallocation = models.IntegerField(db_column='eTaskTargetAllocation')
    etasktargettype = models.IntegerField(db_column='eTaskTargetType')
    etheme_0 = models.IntegerField(db_column='eTheme_0')
    etheme_1 = models.IntegerField(db_column='eTheme_1')
    etheme_2 = models.IntegerField(db_column='eTheme_2')
    etheme_3 = models.IntegerField(db_column='eTheme_3')
    evehiclecategory = models.IntegerField(db_column='eVehicleCategory')
    flocationdistancemax = models.FloatField(db_column='fLocationDistanceMax')
    flocationdistancemin = models.FloatField(db_column='fLocationDistanceMin')
    nmaxtargetsperblock = models.IntegerField(db_column='nMaxTargetsPerBlock')
    ntargetcount = models.IntegerField(db_column='nTargetCount')
    etasktargetspecificationmethod = models.IntegerField(db_column='eTaskTargetSpecificationMethod')
    ballowdifferentblock = models.IntegerField(db_column='bAllowDifferentBlock')
    ballowsameblock = models.IntegerField(db_column='bAllowSameBlock')
    buniqueblock = models.IntegerField(db_column='bUniqueBlock')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskTargetAllocations'


class Tasktargetcheckpoints(models.Model):
    id = models.IntegerField(primary_key=True)
    etasktargettype = models.IntegerField(db_column='eTaskTargetType')
    nmaxplayerspaces = models.IntegerField(db_column='nMaxPlayerSpaces')
    nmaxvehiclespaces = models.IntegerField(db_column='nMaxVehicleSpaces')
    ballowdropoffs = models.IntegerField(db_column='bAllowDropOffs')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskTargetCheckpoints'


class Tasktargetclasses(models.Model):
    id = models.IntegerField(primary_key=True)
    etasktargetclass = models.IntegerField(db_column='eTaskTargetClass')
    bcanbeusedindirectedmissions = models.IntegerField(db_column='bCanBeUsedInDirectedMissions')
    blivingcity = models.IntegerField(db_column='bLivingCity')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskTargetClasses'


class Tasktargetgraffiti(models.Model):
    id = models.IntegerField(primary_key=True)
    etasktargettype = models.IntegerField(db_column='eTaskTargetType')
    ndummy = models.IntegerField(db_column='nDummy')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskTargetGraffiti'


class Tasktargetnpcs(models.Model):
    id = models.IntegerField(primary_key=True)
    enpctype = models.IntegerField(db_column='eNPCType')
    etasktargettype = models.IntegerField(db_column='eTaskTargetType')
    ntemplctype = models.IntegerField(db_column='nTempLCType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskTargetNPCs'


class Tasktargetprops(models.Model):
    id = models.IntegerField(primary_key=True)
    spropassetname = models.TextField(db_column='sPropAssetName')
    epropcategory = models.IntegerField(db_column='ePropCategory')
    etasktargettype = models.IntegerField(db_column='eTaskTargetType')
    farsondamagedelayseconds = models.FloatField(db_column='fArsonDamageDelaySeconds')
    barson = models.IntegerField(db_column='bArson')
    bbombdisposal = models.IntegerField(db_column='bBombDisposal')
    bbombing = models.IntegerField(db_column='bBombing')
    bburglary = models.IntegerField(db_column='bBurglary')
    bbust = models.IntegerField(db_column='bBust')
    bcsi = models.IntegerField(db_column='bCSI')
    bforcedentry = models.IntegerField(db_column='bForcedEntry')
    bhacking = models.IntegerField(db_column='bHacking')
    bisbuildingfeature = models.IntegerField(db_column='bIsBuildingFeature')
    bramraid = models.IntegerField(db_column='bRamRaid')
    bsabotage = models.IntegerField(db_column='bSabotage')
    bvandalism = models.IntegerField(db_column='bVandalism')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskTargetProps'


class Tasktargettypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    sdisplayname = models.TextField(db_column='sDisplayName')
    egameplayobject = models.IntegerField(db_column='eGameplayObject')
    ehudmarkeroffsetoverride = models.IntegerField(db_column='eHUDMarkerOffsetOverride')
    eopenworldtargetactivity = models.IntegerField(db_column='eOpenWorldTargetActivity')
    eowaitemspawnrule = models.IntegerField(db_column='eOWAItemSpawnRule')
    etasktargettype = models.IntegerField(db_column='eTaskTargetType')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    etasktargetclass = models.IntegerField(db_column='eTaskTargetClass')
    etimeofdayavailability = models.IntegerField(db_column='eTimeOfDayAvailability')
    ballowsimultaneousallocations = models.IntegerField(db_column='bAllowSimultaneousAllocations')
    bopenworldonly = models.IntegerField(db_column='bOpenWorldOnly')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TaskTargetTypes'


class Themeitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sresource = models.TextField(db_column='sResource')
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ThemeItemTypes'


class Threatlevels(models.Model):
    id = models.IntegerField(primary_key=True)
    salloweddistrictthreats = models.TextField(db_column='sAllowedDistrictThreats')
    sdisplayedname = models.TextField(db_column='sDisplayedName')
    ehudtextureicon = models.IntegerField(db_column='eHUDTextureIcon')
    ethreatlevel = models.IntegerField(db_column='eThreatLevel')
    fmedianthreat = models.FloatField(db_column='fMedianThreat')
    fthreshold = models.FloatField(db_column='fThreshold')
    nratingtexturearrayindex = models.IntegerField(db_column='nRatingTextureArrayIndex')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'ThreatLevels'


class Timeofdayavailabilities(models.Model):
    id = models.IntegerField(primary_key=True)
    etimeofdayavailability = models.IntegerField(db_column='eTimeOfDayAvailability')
    bafternoon = models.IntegerField(db_column='bAfternoon')
    bevening = models.IntegerField(db_column='bEvening')
    bmorning = models.IntegerField(db_column='bMorning')
    bnight = models.IntegerField(db_column='bNight')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TimeOfDayAvailabilities'


class Timeofdayperiod(models.Model):
    id = models.IntegerField(primary_key=True)
    nendtimehours = models.IntegerField(db_column='nEndTimeHours')
    nendtimemins = models.IntegerField(db_column='nEndTimeMins')
    nstarttimehours = models.IntegerField(db_column='nStartTimeHours')
    nstarttimemins = models.IntegerField(db_column='nStartTimeMins')
    etimeofdayperiod = models.IntegerField(db_column='eTimeofDayPeriod')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TimeofDayPeriod'


class Titleunlockitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    bfemale = models.IntegerField(db_column='bFemale')
    bhideuntilunlocked = models.IntegerField(db_column='bHideUntilUnlocked')
    bmale = models.IntegerField(db_column='bMale')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TitleUnlockItemTypes'


class Trackedactivities(models.Model):
    id = models.IntegerField(primary_key=True)
    etrackedactivity = models.IntegerField(db_column='eTrackedActivity')
    eunit = models.IntegerField(db_column='eUnit')
    nmaxincrementperzone = models.IntegerField(db_column='nMaxIncrementPerZone')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    efaction = models.IntegerField(db_column='eFaction')
    epersistencetype = models.IntegerField(db_column='ePersistenceType')
    bupdateduringwitnessingmission = models.IntegerField(db_column='bUpdateDuringWitnessingMission')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TrackedActivities'


class Trackedactivitiesderived(models.Model):
    id = models.IntegerField(primary_key=True)
    emaster_0 = models.IntegerField(db_column='eMaster_0')
    emaster_1 = models.IntegerField(db_column='eMaster_1')
    emaster_2 = models.IntegerField(db_column='eMaster_2')
    emaster_3 = models.IntegerField(db_column='eMaster_3')
    emaster_4 = models.IntegerField(db_column='eMaster_4')
    emaster_5 = models.IntegerField(db_column='eMaster_5')
    emaster_6 = models.IntegerField(db_column='eMaster_6')
    emaster_7 = models.IntegerField(db_column='eMaster_7')
    emaster_8 = models.IntegerField(db_column='eMaster_8')
    emaster_9 = models.IntegerField(db_column='eMaster_9')
    etrackedactivity = models.IntegerField(db_column='eTrackedActivity')
    eoperation = models.IntegerField(db_column='eOperation')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TrackedActivitiesDerived'


class Trackedactivitiesfixed(models.Model):
    id = models.IntegerField(primary_key=True)
    etrackedactivity = models.IntegerField(db_column='eTrackedActivity')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TrackedActivitiesFixed'


class Trackedactivityunits(models.Model):
    id = models.IntegerField(primary_key=True)
    sformatting = models.TextField(db_column='sFormatting')
    etrackedactivityunit = models.IntegerField(db_column='eTrackedActivityUnit')
    econversion = models.IntegerField(db_column='eConversion')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TrackedActivityUnits'


class Trafficlightdurations(models.Model):
    id = models.IntegerField(primary_key=True)
    edistrict = models.IntegerField(db_column='eDistrict')
    etrafficlightduration = models.IntegerField(db_column='eTrafficLightDuration')
    fped_fourlanemax = models.FloatField(db_column='fPed_FourLaneMax')
    fped_fourlanemin = models.FloatField(db_column='fPed_FourLaneMin')
    fped_onelanemax = models.FloatField(db_column='fPed_OneLaneMax')
    fped_onelanemin = models.FloatField(db_column='fPed_OneLaneMin')
    fped_threelanemax = models.FloatField(db_column='fPed_ThreeLaneMax')
    fped_threelanemin = models.FloatField(db_column='fPed_ThreeLaneMin')
    fped_twolanemax = models.FloatField(db_column='fPed_TwoLaneMax')
    fped_twolanemin = models.FloatField(db_column='fPed_TwoLaneMin')
    fvehicle_fourlanemax = models.FloatField(db_column='fVehicle_FourLaneMax')
    fvehicle_fourlanemin = models.FloatField(db_column='fVehicle_FourLaneMin')
    fvehicle_onelanemax = models.FloatField(db_column='fVehicle_OneLaneMax')
    fvehicle_onelanemin = models.FloatField(db_column='fVehicle_OneLaneMin')
    fvehicle_threelanemax = models.FloatField(db_column='fVehicle_ThreeLaneMax')
    fvehicle_threelanemin = models.FloatField(db_column='fVehicle_ThreeLaneMin')
    fvehicle_twolanemax = models.FloatField(db_column='fVehicle_TwoLaneMax')
    fvehicle_twolanemin = models.FloatField(db_column='fVehicle_TwoLaneMin')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TrafficLightDurations'


class Tutorialcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    srewardmailbody = models.TextField(db_column='sRewardMailBody')
    srewardmailsubject = models.TextField(db_column='sRewardMailSubject')
    erewardpackage = models.IntegerField(db_column='eRewardPackage')
    etutorial = models.IntegerField(db_column='eTutorial')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TutorialCategories'


class Tutorialevents(models.Model):
    id = models.IntegerField(primary_key=True)
    shudtext = models.TextField(db_column='sHUDText')
    egameplayevent = models.IntegerField(db_column='eGameplayEvent')
    ehudmarker = models.IntegerField(db_column='eHUDMarker')
    etutorial = models.IntegerField(db_column='eTutorial')
    euihighlight = models.IntegerField(db_column='eUIHighlight')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'TutorialEvents'


class Tutorials(models.Model):
    id = models.IntegerField(primary_key=True)
    sbody = models.TextField(db_column='sBody')
    sscreenshot = models.TextField(db_column='sScreenshot')
    ssubtitle = models.TextField(db_column='sSubTitle')
    stitle = models.TextField(db_column='sTitle')
    eparent = models.IntegerField(db_column='eParent')
    etutorial = models.IntegerField(db_column='eTutorial')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    efaction = models.IntegerField(db_column='eFaction')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'Tutorials'


class Uiinteractionpoints(models.Model):
    id = models.IntegerField(primary_key=True)
    sinfobrowsertext = models.TextField(db_column='sInfoBrowserText')
    ehudmarker = models.IntegerField(db_column='eHUDMarker')
    einfobrowsericon = models.IntegerField(db_column='eInfoBrowserIcon')
    euiinteractionpoint = models.IntegerField(db_column='eUIInteractionPoint')
    ecsa = models.IntegerField(db_column='eCSA')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'UIInteractionPoints'


class Uimeshviewersetup(models.Model):
    id = models.IntegerField(primary_key=True)
    nuimeshviewersetup = models.TextField(db_column='nUIMeshViewerSetup')
    fcamerafov = models.FloatField(db_column='fCameraFOV')
    fcameraposx = models.FloatField(db_column='fCameraPosX')
    fcameraposy = models.FloatField(db_column='fCameraPosY')
    fcameraposz = models.FloatField(db_column='fCameraPosZ')
    fmeshcentrex = models.FloatField(db_column='fMeshCentreX')
    fmeshcentrey = models.FloatField(db_column='fMeshCentreY')
    fmeshcentrez = models.FloatField(db_column='fMeshCentreZ')
    fmeshorientationx = models.FloatField(db_column='fMeshOrientationX')
    fmeshorientationy = models.FloatField(db_column='fMeshOrientationY')
    fmeshorientationz = models.FloatField(db_column='fMeshOrientationZ')
    fmeshscale = models.FloatField(db_column='fMeshScale')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'UIMeshViewerSetup'


class Uuistyles(models.Model):
    id = models.IntegerField(primary_key=True)
    sname = models.TextField(db_column='sName')
    euistyle = models.IntegerField(db_column='eUIStyle')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'UUIStyles'


class Unlockiteminfracategories(models.Model):
    id = models.IntegerField(primary_key=True)
    egameplayevent = models.IntegerField(db_column='eGameplayEvent')
    einventoryiteminfracategory = models.IntegerField(db_column='eInventoryItemInfraCategory')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'UnlockItemInfraCategories'


class Unlockitemsubcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    egameplayevent = models.IntegerField(db_column='eGameplayEvent')
    einventoryitemsubcategory = models.IntegerField(db_column='eInventoryItemSubCategory')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'UnlockItemSubCategories'


class Unlockitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    einventoryitemtype = models.ForeignKey('Inventoryitemtypes', db_column='eInventoryItemType', related_name='unlockitemtypes_einventoryitemtype')
    eunlockitem = models.ForeignKey('Inventoryitemtypes', db_column='eUnlockItem', related_name='unlockitemtypes_eunlockitem')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'UnlockItemTypes'


class Usabletokentypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    emodifieritem = models.IntegerField(db_column='eModifierItem')
    ncharges = models.IntegerField(db_column='nCharges')
    nmaxcharges = models.IntegerField(db_column='nMaxCharges')
    nmaxstacks = models.IntegerField(db_column='nMaxStacks')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'UsableTokenTypes'


class Vfxassociations(models.Model):
    id = models.IntegerField(primary_key=True)
    svfxprefabname = models.TextField(db_column='sVFXPrefabName')
    svfxreplacedactor = models.TextField(db_column='sVFXReplacedActor')
    evfxassociation = models.IntegerField(db_column='eVFXAssociation')
    evfxtype = models.IntegerField(db_column='eVFXType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VFXAssociations'


class Vfxtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    evfxtype = models.IntegerField(db_column='eVFXType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VFXTypes'


class Vehicleaudiopart(models.Model):
    id = models.IntegerField(primary_key=True)
    evehicleaudiopart = models.IntegerField(db_column='eVehicleAudioPart')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleAudioPart'


class Vehicleaudiopartdefaults(models.Model):
    id = models.IntegerField(primary_key=True)
    sdamagetype = models.TextField(db_column='sDamageType')
    sdooreventclosefront = models.TextField(db_column='sDoorEventCloseFront')
    sdooreventcloserearback = models.TextField(db_column='sDoorEventCloseRearBack')
    sdooreventcloserearside = models.TextField(db_column='sDoorEventCloseRearSide')
    sdooreventopenfront = models.TextField(db_column='sDoorEventOpenFront')
    sdooreventopenrearback = models.TextField(db_column='sDoorEventOpenRearBack')
    sdooreventopenrearside = models.TextField(db_column='sDoorEventOpenRearSide')
    slc_vehicletype = models.TextField(db_column='sLC_VehicleType')
    ssuspensiontype = models.TextField(db_column='sSuspensionType')
    edefaultamp = models.IntegerField(db_column='eDefaultAmp')
    edefaultengine = models.IntegerField(db_column='eDefaultEngine')
    edefaultexhaust = models.IntegerField(db_column='eDefaultExhaust')
    edefaulthorn = models.IntegerField(db_column='eDefaultHorn')
    edefaultsiren = models.IntegerField(db_column='eDefaultSiren')
    edefaultspeaker = models.IntegerField(db_column='eDefaultSpeaker')
    evehicleaudiopartdefaults = models.IntegerField(db_column='eVehicleAudioPartDefaults')
    fmaxenclosedness = models.FloatField(db_column='fMaxEnclosedness')
    fwheelforceeventthreshold = models.FloatField(db_column='fWheelForceEventThreshold')
    fwheelforcemax = models.FloatField(db_column='fWheelForceMax')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleAudioPartDefaults'


class Vehiclecategories(models.Model):
    id = models.IntegerField(primary_key=True)
    evehiclecategory = models.IntegerField(db_column='eVehicleCategory')
    fhairsquash = models.FloatField(db_column='fHairSquash')
    fmaxheight = models.FloatField(db_column='fMaxHeight')
    fmaxlength = models.FloatField(db_column='fMaxLength')
    fmaxwidth = models.FloatField(db_column='fMaxWidth')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleCategories'


class Vehiclecategoryrestrictions(models.Model):
    id = models.IntegerField(primary_key=True)
    evehiclecategory = models.IntegerField(db_column='eVehicleCategory')
    nnumconcurrentsetuptypes = models.IntegerField(db_column='nNumConcurrentSetupTypes')
    nvehiclecategoryrestriction = models.IntegerField(db_column='nVehicleCategoryRestriction')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleCategoryRestrictions'


class Vehiclecolours(models.Model):
    id = models.IntegerField(primary_key=True)
    fprobability = models.FloatField(db_column='fProbability')
    nbluecomponent = models.IntegerField(db_column='nBlueComponent')
    ngreencomponent = models.IntegerField(db_column='nGreenComponent')
    nredcomponent = models.IntegerField(db_column='nRedComponent')
    evehiclecolour = models.IntegerField(db_column='eVehicleColour')
    bismetallic = models.IntegerField(db_column='bIsMetallic')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleColours'


class Vehiclecomponentunlockitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    salternateresource = models.TextField(db_column='sAlternateResource')
    sresource = models.TextField(db_column='sResource')
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    euicomponent = models.IntegerField(db_column='eUIComponent')
    napplicationcost = models.IntegerField(db_column='nApplicationCost')
    napplicationrating = models.IntegerField(db_column='nApplicationRating')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleComponentUnlockItemTypes'


class Vehiclecomponents(models.Model):
    id = models.IntegerField(primary_key=True)
    evehiclecomponent = models.IntegerField(db_column='eVehicleComponent')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleComponents'


class Vehiclecritical(models.Model):
    id = models.IntegerField(primary_key=True)
    ehudmessage = models.IntegerField(db_column='eHUDMessage')
    evehiclecritical = models.IntegerField(db_column='eVehicleCritical')
    fweight = models.FloatField(db_column='fWeight')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleCritical'


class Vehicledamagehandlingeffects(models.Model):
    id = models.IntegerField(primary_key=True)
    evehicledamagehandlingeffect = models.IntegerField(db_column='eVehicleDamageHandlingEffect')
    fbrakeeffectiveness = models.FloatField(db_column='fBrakeEffectiveness')
    fenginetorquescale = models.FloatField(db_column='fEngineTorqueScale')
    ffrontlatgrip = models.FloatField(db_column='fFrontLatGrip')
    ffrontlonggrip = models.FloatField(db_column='fFrontLongGrip')
    fmaxspeedscale = models.FloatField(db_column='fMaxSpeedScale')
    frearlatgrip = models.FloatField(db_column='fRearLatGrip')
    frearlonggrip = models.FloatField(db_column='fRearLongGrip')
    fsteeringspeed = models.FloatField(db_column='fSteeringSpeed')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleDamageHandlingEffects'


class Vehicledamagelevels(models.Model):
    id = models.IntegerField(primary_key=True)
    ehandlingeffect = models.IntegerField(db_column='eHandlingEffect')
    evehiclecritical = models.IntegerField(db_column='eVehicleCritical')
    evehicledamagelevel = models.IntegerField(db_column='eVehicleDamageLevel')
    fhealththreshold = models.FloatField(db_column='fHealthThreshold')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleDamageLevels'


class Vehicledamagevfx(models.Model):
    id = models.IntegerField(primary_key=True)
    sdamagestatebegin = models.TextField(db_column='sDamageStateBegin')
    sdamagestateend = models.TextField(db_column='sDamageStateEnd')
    sexplosionaudio = models.TextField(db_column='sExplosionAudio')
    sexplosionevent = models.TextField(db_column='sExplosionEvent')
    evehicledamagevfx = models.IntegerField(db_column='eVehicleDamageVFX')
    fhealththreshold = models.FloatField(db_column='fHealthThreshold')
    nstatenumber = models.IntegerField(db_column='nStateNumber')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleDamageVFX'


class Vehicledistrict(models.Model):
    id = models.IntegerField(primary_key=True)
    sheightfield = models.TextField(db_column='sHeightfield')
    fworldoffsetx = models.FloatField(db_column='fWorldOffsetX')
    fworldoffsety = models.FloatField(db_column='fWorldOffsetY')
    fworldoffsetz = models.FloatField(db_column='fWorldOffsetZ')
    fworldtotexturescalexy = models.FloatField(db_column='fWorldToTextureScaleXY')
    fworldtotexturescalez = models.FloatField(db_column='fWorldToTextureScaleZ')
    evehicledistricts = models.IntegerField(db_column='eVehicleDistricts')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleDistrict'


class Vehicledooranimationsets(models.Model):
    id = models.IntegerField(primary_key=True)
    sclosedframe = models.TextField(db_column='sClosedFrame')
    sclosefrominside = models.TextField(db_column='sCloseFromInside')
    sclosefromoutside = models.TextField(db_column='sCloseFromOutside')
    sclosegetin = models.TextField(db_column='sCloseGetIn')
    sopenbailout = models.TextField(db_column='sOpenBailOut')
    sopenframe = models.TextField(db_column='sOpenFrame')
    sopenfromoutside = models.TextField(db_column='sOpenFromOutside')
    sopengetout = models.TextField(db_column='sOpenGetOut')
    sopenseatslideejectcriminal = models.TextField(db_column='sOpenSeatSlideEjectCriminal')
    sopenseatslideejectenforcer = models.TextField(db_column='sOpenSeatSlideEjectEnforcer')
    evehicledooranimationset = models.IntegerField(db_column='eVehicleDoorAnimationSet')
    bdooropenwhileinside = models.IntegerField(db_column='bDoorOpenWhileInside')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleDoorAnimationSets'


class Vehicleevents(models.Model):
    id = models.IntegerField(primary_key=True)
    nignoreme = models.IntegerField(db_column='nIgnoreMe')
    enpcevent = models.IntegerField(db_column='eNPCEvent')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleEvents'


class Vehiclegear(models.Model):
    id = models.IntegerField(primary_key=True)
    spackageimageref = models.TextField(db_column='sPackageImageRef')
    evehiclegear = models.IntegerField(db_column='eVehicleGear')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleGear'


class Vehicleinteractionanimations(models.Model):
    id = models.IntegerField(primary_key=True)
    fblendintime = models.FloatField(db_column='fBlendInTime')
    fblendouttime = models.FloatField(db_column='fBlendOutTime')
    evehicleinteractionanimation = models.IntegerField(db_column='eVehicleInteractionAnimation')
    bmirror = models.IntegerField(db_column='bMirror')
    bpauseatend = models.IntegerField(db_column='bPauseAtEnd')
    bscaleroot = models.IntegerField(db_column='bScaleRoot')
    bstartatorigin = models.IntegerField(db_column='bStartAtOrigin')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleInteractionAnimations'


class Vehicleinteractionsequences(models.Model):
    id = models.IntegerField(primary_key=True)
    ssequencename = models.TextField(db_column='sSequenceName')
    evehicleplayeranimationset = models.IntegerField(db_column='eVehiclePlayerAnimationSet')
    evehicleinteractionanimation = models.IntegerField(db_column='eVehicleInteractionAnimation')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleInteractionSequences'


class Vehicleitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    sresource = models.TextField(db_column='sResource')
    efnmod_0 = models.IntegerField(db_column='eFnMod_0')
    efnmod_1 = models.IntegerField(db_column='eFnMod_1')
    efnmod_2 = models.IntegerField(db_column='eFnMod_2')
    efnmod_3 = models.IntegerField(db_column='eFnMod_3')
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    nreeditfee = models.IntegerField(db_column='nReeditFee')
    evehicle = models.IntegerField(db_column='eVehicle')
    bpreset = models.IntegerField(db_column='bPreset')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleItemTypes'


class Vehiclemenuentries(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplaypicture = models.TextField(db_column='sDisplayPicture')
    sdisplaytext = models.TextField(db_column='sDisplayText')
    smenulevel = models.TextField(db_column='sMenuLevel')
    smenutag = models.TextField(db_column='sMenuTag')
    soptionalscene = models.TextField(db_column='sOptionalScene')
    ecameraangle = models.IntegerField(db_column='eCameraAngle')
    evehiclemenuentry = models.IntegerField(db_column='eVehicleMenuEntry')
    benabled = models.IntegerField(db_column='bEnabled')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleMenuEntries'


class Vehiclemodifieritemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleModifierItemTypes'


class Vehiclenpcinsideanimationsets(models.Model):
    id = models.IntegerField(primary_key=True)
    sejectinitialcriminal = models.TextField(db_column='sEjectInitialCriminal')
    sejectinitialenforcer = models.TextField(db_column='sEjectInitialEnforcer')
    sejectinitialfrompassengersidecriminal = models.TextField(db_column='sEjectInitialFromPassengerSideCriminal')
    sejectinitialfrompassengersideenforcer = models.TextField(db_column='sEjectInitialFromPassengerSideEnforcer')
    sejectlatercriminal = models.TextField(db_column='sEjectLaterCriminal')
    sejectlaterenforcer = models.TextField(db_column='sEjectLaterEnforcer')
    sejectlaterfrompassengersidecriminal = models.TextField(db_column='sEjectLaterFromPassengerSideCriminal')
    sejectlaterfrompassengersideenforcer = models.TextField(db_column='sEjectLaterFromPassengerSideEnforcer')
    evehiclenpcinsideanimationset = models.IntegerField(db_column='eVehicleNPCInsideAnimationSet')
    fejectdistancedriversidecriminal = models.FloatField(db_column='fEjectDistanceDriverSideCriminal')
    fejectdistancedriversideenforcer = models.FloatField(db_column='fEjectDistanceDriverSideEnforcer')
    fejectdistancepassengersidecriminal = models.FloatField(db_column='fEjectDistancePassengerSideCriminal')
    fejectdistancepassengersideenforcer = models.FloatField(db_column='fEjectDistancePassengerSideEnforcer')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleNPCInsideAnimationSets'


class Vehicleplayeranimationsets(models.Model):
    id = models.IntegerField(primary_key=True)
    sdrivesteer = models.TextField(db_column='sDriveSteer')
    spassengeridle = models.TextField(db_column='sPassengerIdle')
    eanimtreedecision = models.IntegerField(db_column='eAnimTreeDecision')
    evehicleplayeranimationset = models.IntegerField(db_column='eVehiclePlayerAnimationSet')
    fleaninduration = models.FloatField(db_column='fLeanInDuration')
    fleanoutduration = models.FloatField(db_column='fLeanOutDuration')
    bmirroranimations = models.IntegerField(db_column='bMirrorAnimations')
    breverseaim = models.IntegerField(db_column='bReverseAim')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehiclePlayerAnimationSets'


class Vehiclepositioninfo(models.Model):
    id = models.IntegerField(primary_key=True)
    evehicleanimationcategory = models.IntegerField(db_column='eVehicleAnimationCategory')
    evehicledooranimationset = models.IntegerField(db_column='eVehicleDoorAnimationSet')
    evehiclenpcinsideanimationset = models.IntegerField(db_column='eVehicleNPCInsideAnimationSet')
    evehicleplayeranimationset = models.IntegerField(db_column='eVehiclePlayerAnimationSet')
    nvcpangle = models.IntegerField(db_column='nVCPAngle')
    nvcpdirection = models.IntegerField(db_column='nVCPDirection')
    evehiclepositionindex = models.IntegerField(db_column='eVehiclePositionIndex')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehiclePositionInfo'


class Vehicleseatcameras(models.Model):
    id = models.IntegerField(primary_key=True)
    eleanoutcamera = models.IntegerField(db_column='eLeanOutCamera')
    esittingcamera = models.IntegerField(db_column='eSittingCamera')
    evehiclepositionindex = models.IntegerField(db_column='eVehiclePositionIndex')
    evehiclesetuptype = models.IntegerField(db_column='eVehicleSetupType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleSeatCameras'


class Vehiclesetuptypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayname = models.TextField(db_column='sDisplayName')
    sgolemobilebase = models.TextField(db_column='sGolemobileBase')
    sphysicsasset = models.TextField(db_column='sPhysicsAsset')
    sshareddataobject = models.TextField(db_column='sSharedDataObject')
    svehiclename = models.TextField(db_column='sVehicleName')
    svehiclesetupasset = models.TextField(db_column='sVehicleSetupAsset')
    svfxprefab = models.TextField(db_column='sVFXPrefab')
    eaudiotype = models.IntegerField(db_column='eAudioType')
    eexplosiontype = models.IntegerField(db_column='eExplosionType')
    egameplayobject = models.IntegerField(db_column='eGameplayObject')
    epedestriandriver = models.IntegerField(db_column='ePedestrianDriver')
    euimeshviewersetup = models.IntegerField(db_column='eUIMeshViewerSetup')
    evehicleanimationcategory = models.IntegerField(db_column='eVehicleAnimationCategory')
    evehiclecategory = models.IntegerField(db_column='eVehicleCategory')
    f0mssteerangle = models.FloatField(db_column='f0msSteerAngle')
    f12mssteerangle = models.FloatField(db_column='f12msSteerAngle')
    f22mssteerangle = models.FloatField(db_column='f22msSteerAngle')
    f2500rpmtorque = models.FloatField(db_column='f2500RpmTorque')
    f2ndgearspeed = models.FloatField(db_column='f2ndGearSpeed')
    f3rdgearspeed = models.FloatField(db_column='f3rdGearSpeed')
    f4500rpmtorque = models.FloatField(db_column='f4500RpmTorque')
    f4thgearspeed = models.FloatField(db_column='f4thGearSpeed')
    f500rpmtorque = models.FloatField(db_column='f500RpmTorque')
    f5thgearspeed = models.FloatField(db_column='f5thGearSpeed')
    f7000rpmtorque = models.FloatField(db_column='f7000RpmTorque')
    fblobshadowscale_0 = models.FloatField(db_column='fBlobShadowScale_0')
    fblobshadowscale_1 = models.FloatField(db_column='fBlobShadowScale_1')
    fblobshadowscale_2 = models.FloatField(db_column='fBlobShadowScale_2')
    fblobshadowtranslate_0 = models.FloatField(db_column='fBlobShadowTranslate_0')
    fblobshadowtranslate_1 = models.FloatField(db_column='fBlobShadowTranslate_1')
    fblobshadowtranslate_2 = models.FloatField(db_column='fBlobShadowTranslate_2')
    fbreakincsaduration = models.FloatField(db_column='fBreakInCSADuration')
    fcambasezfar = models.FloatField(db_column='fCamBaseZFar')
    fcambaseznear = models.FloatField(db_column='fCamBaseZNear')
    fcargoheightreductionfactor = models.FloatField(db_column='fCargoHeightReductionFactor')
    fcargotorquereductionfactor = models.FloatField(db_column='fCargoTorqueReductionFactor')
    fchassistorquefactor = models.FloatField(db_column='fChassisTorqueFactor')
    fcollisiondamage = models.FloatField(db_column='fCollisionDamage')
    fcomoffsetx = models.FloatField(db_column='fCOMOffsetX')
    fcomoffsetz = models.FloatField(db_column='fCOMOffsetZ')
    fdrivercamfar = models.FloatField(db_column='fDriverCamFar')
    fdrivercamnear = models.FloatField(db_column='fDriverCamNear')
    fenginebrakingfactor = models.FloatField(db_column='fEngineBrakingFactor')
    ffinaldriveratio = models.FloatField(db_column='fFinalDriveRatio')
    ffrontlatfactor = models.FloatField(db_column='fFrontLatFactor')
    ffrontlongfactor = models.FloatField(db_column='fFrontLongFactor')
    ffrontsuspensionspeed = models.FloatField(db_column='fFrontSuspensionSpeed')
    ffrontsuspensiontravel = models.FloatField(db_column='fFrontSuspensionTravel')
    ffrontwheelboneoffset_0 = models.FloatField(db_column='fFrontWheelBoneOffset_0')
    ffrontwheelboneoffset_1 = models.FloatField(db_column='fFrontWheelBoneOffset_1')
    ffrontwheelboneoffset_2 = models.FloatField(db_column='fFrontWheelBoneOffset_2')
    ffrontwheelmeshoffset_0 = models.FloatField(db_column='fFrontWheelMeshOffset_0')
    ffrontwheelmeshoffset_1 = models.FloatField(db_column='fFrontWheelMeshOffset_1')
    ffrontwheelmeshoffset_2 = models.FloatField(db_column='fFrontWheelMeshOffset_2')
    ffrontwheelradius = models.FloatField(db_column='fFrontWheelRadius')
    fgearratios_0 = models.FloatField(db_column='fGearRatios_0')
    fgearratios_1 = models.FloatField(db_column='fGearRatios_1')
    fgearratios_2 = models.FloatField(db_column='fGearRatios_2')
    fgearratios_3 = models.FloatField(db_column='fGearRatios_3')
    fgearratios_4 = models.FloatField(db_column='fGearRatios_4')
    fgearratios_5 = models.FloatField(db_column='fGearRatios_5')
    fidlerpm = models.FloatField(db_column='fIdleRPM')
    flsdfactor = models.FloatField(db_column='fLSDFactor')
    fmaxbraketorque = models.FloatField(db_column='fMaxBrakeTorque')
    fmaxcargoheightreduction = models.FloatField(db_column='fMaxCargoHeightReduction')
    fmaxcargotorquereduction = models.FloatField(db_column='fMaxCargoTorqueReduction')
    fmaxdirt = models.FloatField(db_column='fMaxDirt')
    fmaxdust = models.FloatField(db_column='fMaxDust')
    fmaxrepairtimesecs = models.FloatField(db_column='fMaxRepairTimeSecs')
    fmaxreversespeed = models.FloatField(db_column='fMaxReverseSpeed')
    fmaxspeed = models.FloatField(db_column='fMaxSpeed')
    fmindirt = models.FloatField(db_column='fMinDirt')
    fmindust = models.FloatField(db_column='fMinDust')
    fpercentdirty = models.FloatField(db_column='fPercentDirty')
    fpercentperfectlyclean = models.FloatField(db_column='fPercentPerfectlyClean')
    framraiddamagemultiplier = models.FloatField(db_column='fRamraidDamageMultiplier')
    frearhandbrakelat = models.FloatField(db_column='fRearHandbrakeLat')
    frearhandbrakelong = models.FloatField(db_column='fRearHandbrakeLong')
    frearlatfactor = models.FloatField(db_column='fRearLatFactor')
    frearlongfactor = models.FloatField(db_column='fRearLongFactor')
    frearsuspensionspeed = models.FloatField(db_column='fRearSuspensionSpeed')
    frearsuspensiontravel = models.FloatField(db_column='fRearSuspensionTravel')
    frearwheelboneoffset_0 = models.FloatField(db_column='fRearWheelBoneOffset_0')
    frearwheelboneoffset_1 = models.FloatField(db_column='fRearWheelBoneOffset_1')
    frearwheelboneoffset_2 = models.FloatField(db_column='fRearWheelBoneOffset_2')
    frearwheelmeshoffset_0 = models.FloatField(db_column='fRearWheelMeshOffset_0')
    frearwheelmeshoffset_1 = models.FloatField(db_column='fRearWheelMeshOffset_1')
    frearwheelmeshoffset_2 = models.FloatField(db_column='fRearWheelMeshOffset_2')
    frearwheelradius = models.FloatField(db_column='fRearWheelRadius')
    fredlinerpm = models.FloatField(db_column='fRedlineRPM')
    freversethrottle = models.FloatField(db_column='fReverseThrottle')
    fsteeraccel = models.FloatField(db_column='fSteerAccel')
    fsteerspeed = models.FloatField(db_column='fSteerSpeed')
    fsuspensiondamping = models.FloatField(db_column='fSuspensionDamping')
    fsuspensionstiffness = models.FloatField(db_column='fSuspensionStiffness')
    fwheellatasymptoteslip = models.FloatField(db_column='fWheelLatAsymptoteSlip')
    fwheellatasymptotevalue = models.FloatField(db_column='fWheelLatAsymptoteValue')
    fwheellatextremumslip = models.FloatField(db_column='fWheelLatExtremumSlip')
    fwheellatextremumvalue = models.FloatField(db_column='fWheelLatExtremumValue')
    fwheellongasymptoteslip = models.FloatField(db_column='fWheelLongAsymptoteSlip')
    fwheellongasymptotevalue = models.FloatField(db_column='fWheelLongAsymptoteValue')
    fwheellongextremumslip = models.FloatField(db_column='fWheelLongExtremumSlip')
    fwheellongextremumvalue = models.FloatField(db_column='fWheelLongExtremumValue')
    ncabincargopipcapacity = models.IntegerField(db_column='nCabinCargoPipCapacity')
    ncamerapitchmax = models.IntegerField(db_column='nCameraPitchMax')
    ncamerapitchmin = models.IntegerField(db_column='nCameraPitchMin')
    ncargoareaseatpositions = models.IntegerField(db_column='nCargoAreaSeatPositions')
    ninitialcampitch = models.IntegerField(db_column='nInitialCamPitch')
    nmaincargopipcapacity = models.IntegerField(db_column='nMainCargoPipCapacity')
    nmaxhealth = models.IntegerField(db_column='nMaxHealth')
    nmaxrepaircost = models.IntegerField(db_column='nMaxRepairCost')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    nspawncost = models.IntegerField(db_column='nSpawnCost')
    edrivetype = models.IntegerField(db_column='eDriveType')
    etempassets = models.IntegerField(db_column='eTempAssets')
    euicategory = models.IntegerField(db_column='eUICategory')
    evehiclemodelclass = models.IntegerField(db_column='eVehicleModelClass')
    evehiclesetuptype = models.IntegerField(db_column='eVehicleSetupType')
    bhasalarm = models.IntegerField(db_column='bHasAlarm')
    bhasrearseats = models.IntegerField(db_column='bHasRearSeats')
    bhastaillights = models.IntegerField(db_column='bHasTailLights')
    bisplayeronlyvehicle = models.IntegerField(db_column='bIsPlayerOnlyVehicle')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleSetupTypes'


class Vehicletempsetups(models.Model):
    id = models.IntegerField(primary_key=True)
    stempsetupinfo = models.TextField(db_column='sTempSetupInfo')
    evehicletempsetup = models.IntegerField(db_column='eVehicleTempSetup')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleTempSetups'


class Vehicleuicameraangles(models.Model):
    id = models.IntegerField(primary_key=True)
    evehicleuicameraangle = models.IntegerField(db_column='eVehicleUICameraAngle')
    factorrotation = models.FloatField(db_column='fActorRotation')
    fcameraposition = models.FloatField(db_column='fCameraPosition')
    ffov = models.FloatField(db_column='fFOV')
    bopendoors = models.IntegerField(db_column='bOpenDoors')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleUICameraAngles'


class Vehicleuicategory(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayname = models.TextField(db_column='sDisplayName')
    evehicleuicategory = models.IntegerField(db_column='eVehicleUICategory')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleUICategory'


class Vehicleuicomponentcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayname = models.TextField(db_column='sDisplayName')
    evehicleuicomponentcategory = models.IntegerField(db_column='eVehicleUIComponentCategory')
    nsortingpriority = models.IntegerField(db_column='nSortingPriority')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleUIComponentCategories'


class Vehicleuicomponentinfos(models.Model):
    id = models.IntegerField(primary_key=True)
    ecameraangle = models.IntegerField(db_column='eCameraAngle')
    ecategory = models.IntegerField(db_column='eCategory')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleUIComponentInfos'


class Vehicleuisetups(models.Model):
    id = models.IntegerField(primary_key=True)
    facceleration = models.FloatField(db_column='fAcceleration')
    fcollisiondamage = models.FloatField(db_column='fCollisionDamage')
    fhandling = models.FloatField(db_column='fHandling')
    fhealth = models.FloatField(db_column='fHealth')
    fsuspensionoffsethack = models.FloatField(db_column='fSuspensionOffsetHack')
    ftopspeed = models.FloatField(db_column='fTopSpeed')
    evehiclesetuptype = models.IntegerField(db_column='eVehicleSetupType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VehicleUISetups'


class Videoreplayuientries(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    sdisplayname = models.TextField(db_column='sDisplayName')
    svideofilename = models.TextField(db_column='sVideoFileName')
    evideoreplayuientry = models.IntegerField(db_column='eVideoReplayUIEntry')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VideoReplayUIEntries'


class Vignettetypes(models.Model):
    id = models.IntegerField(primary_key=True)
    spackage = models.TextField(db_column='sPackage')
    evignettedescriptor = models.IntegerField(db_column='eVignetteDescriptor')
    fmaxcanceldistancefromvnode = models.FloatField(db_column='fMaxCancelDistanceFromVNode')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'VignetteTypes'


class Wardrobemenuentries(models.Model):
    id = models.IntegerField(primary_key=True)
    sdisplayimage = models.TextField(db_column='sDisplayImage')
    sdisplaytext = models.TextField(db_column='sDisplayText')
    smenulevel = models.TextField(db_column='sMenuLevel')
    smenutag = models.TextField(db_column='sMenuTag')
    smouseovertext = models.TextField(db_column='sMouseOverText')
    soptionalscene = models.TextField(db_column='sOptionalScene')
    ewardrobemenuentry = models.IntegerField(db_column='eWardrobeMenuEntry')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'WardrobeMenuEntries'


class Warningpromptgroups(models.Model):
    id = models.IntegerField(primary_key=True)
    swarningpromptgroupname = models.TextField(db_column='sWarningPromptGroupName')
    ewarningpromptgroup = models.IntegerField(db_column='eWarningPromptGroup')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'WarningPromptGroups'


class Weaponattachmentvisuals(models.Model):
    id = models.IntegerField(primary_key=True)
    simpactvfx = models.TextField(db_column='sImpactVFX')
    smuzzleflashvfx = models.TextField(db_column='sMuzzleFlashVFX')
    snontracershotvfx = models.TextField(db_column='sNonTracerShotVFX')
    stracervfx = models.TextField(db_column='sTracerVFX')
    swindupaudiotype = models.TextField(db_column='sWindupAudioType')
    eitemattachmentvisual = models.IntegerField(db_column='eItemAttachmentVisual')
    eimpactclass = models.IntegerField(db_column='eImpactClass')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'WeaponAttachmentVisuals'


class Weaponclasses(models.Model):
    id = models.IntegerField(primary_key=True)
    sunrealclassname = models.TextField(db_column='sUnrealClassName')
    eweaponclass = models.IntegerField(db_column='eWeaponClass')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'WeaponClasses'


class Weaponcurves(models.Model):
    id = models.IntegerField(primary_key=True)
    saccuracyrecovery = models.TextField(db_column='sAccuracyRecovery')
    sburstshots = models.TextField(db_column='sBurstShots')
    seffectiverange = models.TextField(db_column='sEffectiveRange')
    spershotmodifier = models.TextField(db_column='sPerShotModifier')
    spingdistance = models.TextField(db_column='sPingDistance')
    spitch = models.TextField(db_column='sPitch')
    sradiusattenmetres = models.TextField(db_column='sRadiusAtTenMetres')
    srecoverypersecond = models.TextField(db_column='sRecoveryPerSecond')
    sreloadtime = models.TextField(db_column='sReloadTime')
    syawnegative = models.TextField(db_column='sYawNegative')
    syawpositive = models.TextField(db_column='sYawPositive')
    eweaponcurve = models.IntegerField(db_column='eWeaponCurve')
    fburstshotsinc = models.FloatField(db_column='fBurstShotsInc')
    fgeneralrecoverydelay = models.FloatField(db_column='fGeneralRecoveryDelay')
    fgeneralrecoveryscale = models.FloatField(db_column='fGeneralRecoveryScale')
    fpershotmodifierinc = models.FloatField(db_column='fPerShotModifierInc')
    fpingdistanceinc = models.FloatField(db_column='fPingDistanceInc')
    fpitchinc = models.FloatField(db_column='fPitchInc')
    fradiusattenmetresinc = models.FloatField(db_column='fRadiusAtTenMetresInc')
    freloadtimeinc = models.FloatField(db_column='fReloadTimeInc')
    fyawnegativeinc = models.FloatField(db_column='fYawNegativeInc')
    fyawpositiveinc = models.FloatField(db_column='fYawPositiveInc')
    bburstshotsrecover = models.IntegerField(db_column='bBurstShotsRecover')
    bpershotmodifierrecover = models.IntegerField(db_column='bPerShotModifierRecover')
    bpingdistancerecovers = models.IntegerField(db_column='bPingDistanceRecovers')
    bpitchrecover = models.IntegerField(db_column='bPitchRecover')
    bradiusattenmetresrecover = models.IntegerField(db_column='bRadiusAtTenMetresRecover')
    byawnegativerecover = models.IntegerField(db_column='bYawNegativeRecover')
    byawpositiverecover = models.IntegerField(db_column='bYawPositiveRecover')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'WeaponCurves'


class Weaponitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    sdescription = models.TextField(db_column='sDescription')
    eactivitymessageicon = models.IntegerField(db_column='eActivityMessageIcon')
    efnmod_0 = models.IntegerField(db_column='eFnMod_0')
    efnmod_1 = models.IntegerField(db_column='eFnMod_1')
    efnmod_2 = models.IntegerField(db_column='eFnMod_2')
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    eitemattachment = models.IntegerField(db_column='eItemAttachment')
    eweapontypelink = models.IntegerField(db_column='eWeaponTypeLink')
    bcausescontagion = models.IntegerField(db_column='bCausesContagion')
    bisskinnable = models.IntegerField(db_column='bIsSkinnable')
    bpreset = models.IntegerField(db_column='bPreset')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'WeaponItemTypes'


class Weaponloadouts(models.Model):
    id = models.IntegerField(primary_key=True)
    eweaponloadout = models.IntegerField(db_column='eWeaponLoadout')
    eweapontocreate_0 = models.IntegerField(db_column='eWeaponToCreate_0')
    eweapontocreate_1 = models.IntegerField(db_column='eWeaponToCreate_1')
    eweapontocreate_2 = models.IntegerField(db_column='eWeaponToCreate_2')
    eweapontocreate_3 = models.IntegerField(db_column='eWeaponToCreate_3')
    eweapontypetofind_0 = models.IntegerField(db_column='eWeaponTypeToFind_0')
    eweapontypetofind_1 = models.IntegerField(db_column='eWeaponTypeToFind_1')
    eweapontypetofind_2 = models.IntegerField(db_column='eWeaponTypeToFind_2')
    eweapontypetofind_3 = models.IntegerField(db_column='eWeaponTypeToFind_3')
    nequipslot = models.IntegerField(db_column='nEquipSlot')
    eweaponoverridetype_0 = models.IntegerField(db_column='eWeaponOverrideType_0')
    eweaponoverridetype_1 = models.IntegerField(db_column='eWeaponOverrideType_1')
    eweaponoverridetype_2 = models.IntegerField(db_column='eWeaponOverrideType_2')
    eweaponoverridetype_3 = models.IntegerField(db_column='eWeaponOverrideType_3')
    ballowweaponpickup = models.IntegerField(db_column='bAllowWeaponPickup')
    bgiftammo = models.IntegerField(db_column='bGiftAmmo')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'WeaponLoadouts'


class Weaponmodifieritemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'WeaponModifierItemTypes'


class Weaponprojectiles(models.Model):
    id = models.IntegerField(primary_key=True)
    sflightaudioevent = models.TextField(db_column='sFlightAudioEvent')
    smesh = models.TextField(db_column='sMesh')
    strailvfx = models.TextField(db_column='sTrailVFX')
    eexplosion = models.IntegerField(db_column='eExplosion')
    eweaponprojectile = models.IntegerField(db_column='eWeaponProjectile')
    farmingtimer = models.FloatField(db_column='fArmingTimer')
    fbouncedamping = models.FloatField(db_column='fBounceDamping')
    ffusedelay = models.FloatField(db_column='fFuseDelay')
    fgravitymultiplier = models.FloatField(db_column='fGravityMultiplier')
    baudiowaituntilfalling = models.IntegerField(db_column='bAudioWaitUntilFalling')
    bimpactdetonated = models.IntegerField(db_column='bImpactDetonated')
    btumble = models.IntegerField(db_column='bTumble')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'WeaponProjectiles'


class Weaponrecoils(models.Model):
    id = models.IntegerField(primary_key=True)
    eweaponrecoil = models.IntegerField(db_column='eWeaponRecoil')
    frecoilexp = models.FloatField(db_column='fRecoilExp')
    frecoverexp = models.FloatField(db_column='fRecoverExp')
    nmarksmanshippitchpercentage = models.IntegerField(db_column='nMarksmanshipPitchPercentage')
    nmarksmanshipyawpercentage = models.IntegerField(db_column='nMarksmanshipYawPercentage')
    npitchmax = models.IntegerField(db_column='nPitchMax')
    npitchmin = models.IntegerField(db_column='nPitchMin')
    npitchrecoverypercentagemax = models.IntegerField(db_column='nPitchRecoveryPercentageMax')
    npitchrecoverypercentagemin = models.IntegerField(db_column='nPitchRecoveryPercentageMin')
    nrecoiltime = models.IntegerField(db_column='nRecoilTime')
    nrecovertime = models.IntegerField(db_column='nRecoverTime')
    nyawnegativemax = models.IntegerField(db_column='nYawNegativeMax')
    nyawnegativemin = models.IntegerField(db_column='nYawNegativeMin')
    nyawnegativerecoverypercentagemax = models.IntegerField(db_column='nYawNegativeRecoveryPercentageMax')
    nyawnegativerecoverypercentagemin = models.IntegerField(db_column='nYawNegativeRecoveryPercentageMin')
    nyawpositivemax = models.IntegerField(db_column='nYawPositiveMax')
    nyawpositivemin = models.IntegerField(db_column='nYawPositiveMin')
    nyawpositiverecoverypercentagemax = models.IntegerField(db_column='nYawPositiveRecoveryPercentageMax')
    nyawpositiverecoverypercentagemin = models.IntegerField(db_column='nYawPositiveRecoveryPercentageMin')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'WeaponRecoils'


class Weaponskinunlockitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    einventoryitemtype = models.IntegerField(db_column='eInventoryItemType')
    bhideuntilunlocked = models.IntegerField(db_column='bHideUntilUnlocked')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'WeaponSkinUnlockItemTypes'


class Weaponskins(models.Model):
    id = models.IntegerField(primary_key=True)
    eitemattachmentvisual = models.IntegerField(db_column='eItemAttachmentVisual')
    eunlock = models.IntegerField(db_column='eUnlock')
    eweaponskin = models.IntegerField(db_column='eWeaponSkin')
    eweapontypelink = models.IntegerField(db_column='eWeaponTypeLink')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'WeaponSkins'


class Weapontypelinks(models.Model):
    id = models.IntegerField(primary_key=True)
    eweapontype_0 = models.IntegerField(db_column='eWeaponType_0')
    eweapontype_1 = models.IntegerField(db_column='eWeaponType_1')
    eweapontype_2 = models.IntegerField(db_column='eWeaponType_2')
    eweapontype_3 = models.IntegerField(db_column='eWeaponType_3')
    eweapontypelink = models.IntegerField(db_column='eWeaponTypeLink')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'WeaponTypeLinks'


class Weapontypesets(models.Model):
    id = models.IntegerField(primary_key=True)
    scommandline = models.TextField(db_column='sCommandLine')
    eweapontypeset = models.IntegerField(db_column='eWeaponTypeSet')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'WeaponTypeSets'


class Weapontypes(models.Model):
    id = models.IntegerField(primary_key=True)
    eammocategory = models.IntegerField(db_column='eAmmoCategory')
    edisabledrulesets = models.IntegerField(db_column='eDisabledRuleSets')
    etagger = models.IntegerField(db_column='eTagger')
    eweaponcurve = models.IntegerField(db_column='eWeaponCurve')
    eweaponprojectile = models.IntegerField(db_column='eWeaponProjectile')
    eweapontype = models.IntegerField(db_column='eWeaponType')
    faccuracycooldown = models.FloatField(db_column='fAccuracyCooldown')
    fburstinterval = models.FloatField(db_column='fBurstInterval')
    fcrouchspeed = models.FloatField(db_column='fCrouchSpeed')
    fequiptime = models.FloatField(db_column='fEquipTime')
    ffireinterval = models.FloatField(db_column='fFireInterval')
    fharddamagemodifier = models.FloatField(db_column='fHardDamageModifier')
    fhealthdamage = models.FloatField(db_column='fHealthDamage')
    fholstertime = models.FloatField(db_column='fHolsterTime')
    fjumpz = models.FloatField(db_column='fJumpZ')
    fmarksmanshipspeed = models.FloatField(db_column='fMarksmanshipSpeed')
    fpingdistance = models.FloatField(db_column='fPingDistance')
    fragdollimpulsescale = models.FloatField(db_column='fRagdollImpulseScale')
    freloadendanimduration = models.FloatField(db_column='fReloadEndAnimDuration')
    freloadtime = models.FloatField(db_column='fReloadTime')
    fresupplydelaysecs = models.FloatField(db_column='fResupplyDelaySecs')
    frunspeed = models.FloatField(db_column='fRunSpeed')
    fsoftdamagemodifier = models.FloatField(db_column='fSoftDamageModifier')
    fsprintdelay = models.FloatField(db_column='fSprintDelay')
    fsprintspeed = models.FloatField(db_column='fSprintSpeed')
    fstaminadamage = models.FloatField(db_column='fStaminaDamage')
    ftaggerduration = models.FloatField(db_column='fTaggerDuration')
    fuiharddamagelevel = models.FloatField(db_column='fUIHardDamageLevel')
    fuirangelevel = models.FloatField(db_column='fUIRangeLevel')
    fuirateoffire = models.FloatField(db_column='fUIRateOfFire')
    fuisoftdamagelevel = models.FloatField(db_column='fUISoftDamageLevel')
    fuistundamagelevel = models.FloatField(db_column='fUIStunDamageLevel')
    fwalkspeed = models.FloatField(db_column='fWalkSpeed')
    fwinduptime = models.FloatField(db_column='fWindUpTime')
    nammopoolcapacity = models.IntegerField(db_column='nAmmoPoolCapacity')
    nburstshots = models.IntegerField(db_column='nBurstShots')
    nimpulsestrength = models.IntegerField(db_column='nImpulseStrength')
    nmagazinecapacity = models.IntegerField(db_column='nMagazineCapacity')
    nmagazinewarningamount = models.IntegerField(db_column='nMagazineWarningAmount')
    nresupplyunits = models.IntegerField(db_column='nResupplyUnits')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    eclass = models.IntegerField(db_column='eClass')
    eencumbrance = models.IntegerField(db_column='eEncumbrance')
    ehudreticule = models.IntegerField(db_column='eHUDReticule')
    ehudreticulemarksmanship = models.IntegerField(db_column='eHUDReticuleMarksmanship')
    enpcfiredevent = models.IntegerField(db_column='eNPCFiredEvent')
    enpchitevent = models.IntegerField(db_column='eNPCHitEvent')
    eweaponfiringstate = models.IntegerField(db_column='eWeaponFiringState')
    balwaysplayreloadendanim = models.IntegerField(db_column='bAlwaysPlayReloadEndAnim')
    bcansprint = models.IntegerField(db_column='bCanSprint')
    bdisallowswitchinrefiretimer = models.IntegerField(db_column='bDisallowSwitchInRefireTimer')
    bdontdrop = models.IntegerField(db_column='bDontDrop')
    bequipinvehicle = models.IntegerField(db_column='bEquipInVehicle')
    bforceragdolldeath = models.IntegerField(db_column='bForceRagdollDeath')
    bhasreloadendanimation = models.IntegerField(db_column='bHasReloadEndAnimation')
    bisresuppliable = models.IntegerField(db_column='bIsResuppliable')
    blesslethal = models.IntegerField(db_column='bLessLethal')
    bloopedreload = models.IntegerField(db_column='bLoopedReload')
    busesstopaudioevent = models.IntegerField(db_column='bUsesStopAudioEvent')
    bwitnessing = models.IntegerField(db_column='bWitnessing')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'WeaponTypes'


class Weightedrewards(models.Model):
    id = models.IntegerField(primary_key=True)
    srewardmailbody = models.TextField(db_column='sRewardMailBody')
    srewardmailsubject = models.TextField(db_column='sRewardMailSubject')
    ehudimage = models.IntegerField(db_column='eHUDImage')
    erandomreward = models.IntegerField(db_column='eRandomReward')
    ereward = models.IntegerField(db_column='eReward')
    eweightedreward = models.IntegerField(db_column='eWeightedReward')
    fweight = models.FloatField(db_column='fWeight')
    nsecondarykey = models.IntegerField(db_column='nSecondaryKey')
    bofferonce = models.IntegerField(db_column='bOfferOnce')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'WeightedRewards'


class Witnessablecrimes(models.Model):
    id = models.IntegerField(primary_key=True)
    enotorietyforbeingwitnessed = models.IntegerField(db_column='eNotorietyForBeingWitnessed')
    eprestigeforwitnessing = models.IntegerField(db_column='ePrestigeForWitnessing')
    ewitnessablecrime = models.IntegerField(db_column='eWitnessableCrime')
    fescapepenaltytimer = models.FloatField(db_column='fEscapePenaltyTimer')
    fhotlistduration = models.FloatField(db_column='fHotListDuration')
    fnpcwitnessableduration = models.FloatField(db_column='fNPCWitnessableDuration')
    etriggerednpcworldevent = models.IntegerField(db_column='eTriggeredNPCWorldEvent')
    bcontinuous = models.IntegerField(db_column='bContinuous')
    bnodirectwitness = models.IntegerField(db_column='bNoDirectWitness')
    sapbdb = models.TextField(db_column='sAPBDB')

    class Meta:
        managed = False
        db_table = 'WitnessableCrimes'

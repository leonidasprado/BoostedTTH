from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'THEREQUESTNAME'
config.General.workArea = 'crab_ntuples'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/nfs/dust/cms/user/mwassmer/CMSSW_8_0_26_patch2/src/BoostedTTH/BoostedAnalyzer/test/boostedAnalysis_ntuples-Spring17_cfg.py'
config.JobType.outputFiles = ['ntuples_nominal_Tree.root']
config.JobType.maxJobRuntimeMin = 2880
config.JobType.maxMemoryMB = 2800 
config.JobType.pyCfgParams = ['globalTag=GLOBALTAG','generatorName=notSpecified','useJson=True','dataEra=DATAERA','systematicVariations=nominal','outName=ntuples','isData=True','weight=1.0']
config.JobType.sendPythonFolder=True

config.Data.inputDataset = 'THEINPUTDATASET'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = False
config.Data.publishDBS = 'phys03'
config.Data.outputDatasetTag = 'KIT_tthbb_sl_ntuples'

config.Site.storageSite = 'T2_DE_DESY'
config.Site.blacklist = ['T2_US_*']
#config.Site.whitelist = ['T2_DE_DESY']

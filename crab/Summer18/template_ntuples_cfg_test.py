from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'THEREQUESTNAME'
config.General.workArea = 'crab_ntuple'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/afs/cern.ch/user/l/lprado/work/CMSSW_9_4_10/src/BoostedTTH/BoostedAnalyzer/test/boostedAnalysis_ntuples-ICHEP18_cg.py'
config.JobType.outputFiles = OUTPUTFILES
config.JobType.maxJobRuntimeMin = 1000
config.JobType.maxMemoryMB = 2000
config.JobType.pyCfgParams = ['isData=ISDATA','maxEvents=999999999','globalTag=GLOBALTAG','outName=ntuples','systematicVariations=SYSTEMATICVARIATIONS','dataEra=DATAERA','ProduceMemNtuples=False','weight=WEIGHT','generatorName=GENERATORNAME']
config.JobType.sendPythonFolder=True

config.Data.inputDataset = 'THEINPUTDATASET'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = False
config.Data.publishDBS = 'phys03'
config.Data.outputDatasetTag = 'tthbb_sl_94X_v1'

#config.User.voGroup = 'cms'

config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.blacklist = ['T2_US_*']
#config.Site.whitelist = ['T2_DE_DESY']

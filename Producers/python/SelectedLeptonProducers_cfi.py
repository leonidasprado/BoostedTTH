# Default lepton selection of the "loose electrons/muons" defined at
# https://twiki.cern.ch/twiki/bin/view/CMS/TTbarHbbRun2ReferenceAnalysis#Object_selection_SPRING15

import FWCore.ParameterSet.Config as cms

SelectedElectronProducer = cms.EDProducer(
    "SelectedLeptonProducer",
    leptonType = cms.string("electron"),

    era          = cms.string("NA"),
    analysisType = cms.string("LJ"),
    isData       = cms.bool(False),

    leptons = cms.InputTag("slimmedElectrons"),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    #eleMediumIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-medium","","boostedAnalysis"),
    #eleLooseIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-loose","","boostedAnalysis"),
    #eleVetoIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-veto","","boostedAnalysis"),
    #eleTightIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-tight","","boostedAnalysis"),

    ptMins   = cms.vdouble(15),
    etaMaxs  = cms.vdouble(2.4),
    leptonIDs = cms.vstring("electron80XCutBasedM"),
    collectionNames= cms.vstring("selectedLeptonsDL"),


    # The following two parameters are dummies in case of electrons
    # they are not used for the electron selection, which is defined
    # via the 'leptonID' value
    muonIsoConeSizes = cms.vstring("R03"),
    muonIsoCorrTypes = cms.vstring("rhoEA"),
    muonIsoTypes = cms.vstring("PFIsoTight"),
    useMuonRC = cms.bool(True),
    useDeterministicSeeds = cms.bool(False)
    )


SelectedMuonProducer = cms.EDProducer(
    "SelectedLeptonProducer",
    leptonType = cms.string("muon"),

    era          = cms.string("NA"),
    analysisType = cms.string("LJ"),
    isData       = cms.bool(False),

    leptons = cms.InputTag("slimmedMuons"),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),

    ptMins   = cms.vdouble(15),
    etaMaxs  = cms.vdouble(2.4),
    leptonIDs = cms.vstring("tightDL"),
    collectionNames= cms.vstring("selectedLeptonsDL"),
    muonIsoConeSizes = cms.vstring("R04"),
    muonIsoCorrTypes = cms.vstring("deltaBeta"),
    muonIsoTypes = cms.vstring("PFIsoTight"),
    useMuonRC = cms.bool(True),
    useDeterministicSeeds = cms.bool(False),
    # The following two parameters are dummies in case of muons
    # they are not used for the muon selection, which is defined
    # via the 'leptonID' value
    #eleMediumIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-medium","","boostedAnalysis"),
    #eleLooseIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-loose","","boostedAnalysis"),
    #eleVetoIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-veto","","boostedAnalysis"),
    #eleTightIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-tight","","boostedAnalysis"),
    )

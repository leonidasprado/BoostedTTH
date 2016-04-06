# Default lepton selection of the "loose electrons/muons" defined at
# https://twiki.cern.ch/twiki/bin/view/CMS/TTbarHbbRun2ReferenceAnalysis#Object_selection_SPRING15

import FWCore.ParameterSet.Config as cms

SelectedElectronProducer = cms.EDProducer(
    "SelectedLeptonProducer",
    leptonType = cms.string("electron"),

    era          = cms.string("2015_74x"),
    analysisType = cms.string("LJ"),
    isData       = cms.bool(False),

    leptons = cms.InputTag("slimmedElectrons"),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    ptMin   = cms.double(15),
    etaMax  = cms.double(2.4),
    leptonID = cms.string("EndOf15MVA80iso0p15"),
    electronMVAvalues = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
    electronMVAcategories = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories"),
    
    # The following two parameters are dummies in case of electrons
    # they are not used for the electron selection, which is defined
    # via the 'leptonID' value
    muonIsoConeSize = cms.string("R03"), 
    muonIsoCorrType = cms.string("rhoEA")
    )


SelectedMuonProducer = cms.EDProducer(
    "SelectedLeptonProducer",
    leptonType = cms.string("muon"),

    era          = cms.string("2015_74x"),
    analysisType = cms.string("LJ"),
    isData       = cms.bool(False),

    leptons = cms.InputTag("slimmedMuons"),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    ptMin   = cms.double(15),
    etaMax  = cms.double(2.4),
    leptonID = cms.string("tightDL"),
    muonIsoConeSize = cms.string("R04"),
    muonIsoCorrType = cms.string("deltaBeta"),
    
    # The following two parameters are dummies in case of muons
    # they are not used for the muon selection, which is defined
    # via the 'leptonID' value
    electronMVAvalues = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
    electronMVAcategories = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories"),
    )

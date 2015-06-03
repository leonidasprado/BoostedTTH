#ifndef BOOSTEDTTH_BOOSTEDANALYZER_GENTOPEVENT_HPP
#define BOOSTEDTTH_BOOSTEDANALYZER_GENTOPEVENT_HPP
#include <vector>
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/JetReco/interface/GenJet.h"

class GenTopEvent{
  
public:
  GenTopEvent();
  ~GenTopEvent();
  void Fill(const std::vector<reco::GenParticle>& prunedGenParticles, int ttXid);
  void FillTTxDetails(const std::vector<reco::GenJet>& customGenJets, 
		      const std::vector<int>& genBHadIndex, const std::vector<int>& genBHadJetIndex, 
		      const std::vector<int>& genBHadFlavour, const std::vector<int>& genBHadFromTopWeakDecay, 
		      const std::vector<reco::GenParticle>& genBHadPlusMothers, 
		      const std::vector<int>& genCHadIndex, const std::vector<int>& genCHadJetIndex, 
		      const std::vector<int>& genCHadFlavour, const std::vector<int>& genCHadFromTopWeakDecay, 
		      const std::vector<reco::GenParticle>& genCHadPlusMothers,
		      const std::vector<int>& genCHadBHadronId,
		      const float ttxptcut,const float  ttxetacut);  
  
  reco::GenParticle GetHiggs() const;
  std::vector<reco::GenParticle> GetHiggsDecayProducts() const;
  bool IsFilled() const;
  bool TTxIsFilled() const;
  reco::GenParticle GetTop() const;
  reco::GenParticle GetTopBar() const;
  reco::GenParticle GetTopDecayQuark() const;
  reco::GenParticle GetTopBarDecayQuark() const;

  reco::GenParticle GetWplus() const;
  reco::GenParticle GetWminus() const;
  std::vector<reco::GenParticle> GetWplusDecayProducts() const;
  std::vector<reco::GenParticle> GetWminusDecayProducts() const;

  reco::GenParticle GetTopHad() const;
  reco::GenParticle GetTopLep() const;
  reco::GenParticle GetTopHadDecayQuark() const;
  reco::GenParticle GetTopLepDecayQuark() const;
  reco::GenParticle GetWhad() const;
  reco::GenParticle GetWlep() const;
  std::vector<reco::GenParticle> GetWLeptons() const;
  reco::GenParticle GetLepton() const;
  reco::GenParticle GetNeutrino() const;
  std::vector<reco::GenParticle> GetWQuarks() const;

  std::vector<reco::GenParticle> GetAllTopHads() const;
  std::vector<reco::GenParticle> GetAllTopLeps() const;
  std::vector<reco::GenParticle> GetAllTopHadDecayQuarks() const;
  std::vector<reco::GenParticle> GetAllTopLepDecayQuarks() const;
  std::vector<reco::GenParticle> GetAllWhads() const;
  std::vector<reco::GenParticle> GetAllWleps() const;
  std::vector<reco::GenParticle> GetAllLeptons() const;
  std::vector<reco::GenParticle> GetAllNeutrinos() const;
  std::vector<reco::GenParticle> GetAllWQuarks() const;
  std::vector<reco::GenParticle> GetAllWAntiQuarks() const;

  std::vector<reco::GenParticle> GetQuarks() const;

  math::XYZTLorentzVector GetHiggsVec() const;
  math::XYZTLorentzVector GetTopVec() const;
  math::XYZTLorentzVector GetTopBarVec() const;
  math::XYZTLorentzVector GetTopHadVec() const;
  math::XYZTLorentzVector GetTopLepVec() const;
  math::XYZTLorentzVector GetWplusVec() const;
  math::XYZTLorentzVector GetWminusVec() const;
  math::XYZTLorentzVector GetWhadVec() const;
  math::XYZTLorentzVector GetWlepVec() const;
  math::XYZTLorentzVector GetLeptonVec() const;
  math::XYZTLorentzVector GetNeutrinoVec() const;
  std::vector<math::XYZTLorentzVector> GetQuarkVecs() const;
  std::vector<math::XYZTLorentzVector> GetHiggsDecayProductVecs() const;
  math::XYZTLorentzVector GetTopDecayQuarkVec() const;
  math::XYZTLorentzVector GetTopBarDecayQuarkVec() const;
  math::XYZTLorentzVector GetTopHadDecayQuarkVec() const;
  math::XYZTLorentzVector GetTopLepDecayQuarkVec() const;
  std::vector<math::XYZTLorentzVector> GetWLeptonsVecs() const;
  std::vector<math::XYZTLorentzVector> GetWQuarksVecs() const;
  std::vector<math::XYZTLorentzVector> GetWplusDecayProductsVecs() const;
  std::vector<math::XYZTLorentzVector> GetWminusDecayProductsVecs() const;

  std::vector<math::XYZTLorentzVector> GetAllTopHadVecs() const;
  std::vector<math::XYZTLorentzVector> GetAllTopLepVecs() const;
  std::vector<math::XYZTLorentzVector> GetAllTopHadDecayQuarkVecs() const;
  std::vector<math::XYZTLorentzVector> GetAllTopLepDecayQuarkVecs() const;
  std::vector<math::XYZTLorentzVector> GetAllWhadVecs() const;
  std::vector<math::XYZTLorentzVector> GetAllWlepVecs() const;
  std::vector<math::XYZTLorentzVector> GetAllLeptonVecs() const;
  std::vector<math::XYZTLorentzVector> GetAllNeutrinoVecs() const;
  std::vector<math::XYZTLorentzVector> GetAllWQuarkVecs() const;
  std::vector<math::XYZTLorentzVector> GetAllWAntiQuarkVecs() const;

  reco::GenJet GetTopHadBGenJet() const;
  reco::GenJet GetTopLepBGenJet() const;
  reco::GenJet GetTopBarBBarGenJet() const;
  reco::GenJet GetTopBGenJet() const;
  reco::GenJet GetHiggsBGenJet() const;
  reco::GenJet GetHiggsBBarGenJet() const;
  std::vector<reco::GenJet> GetAdditionalBGenJets() const;
  std::vector<reco::GenJet> GetAdditionalCGenJets() const;
  std::vector<bool> AreAdditionalBGenJetsFromTop() const;
  std::vector<bool> AreAdditionalCGenJetsFromTop() const;
  std::vector<reco::GenJet> GetPseudoAdditionalBGenJets() const;
  std::vector<reco::GenJet> GetPseudoAdditionalCGenJets() const;
  std::vector<reco::GenJet> GetProperAdditionalBGenJets() const;
  std::vector<reco::GenJet> GetProperAdditionalCGenJets() const;

  std::vector<reco::GenParticle> GetAdditionalBGenJetsHadron() const;
  std::vector<reco::GenParticle> GetAdditionalCGenJetsHadron() const;


  int GetTTxId(bool countAdditionalAfterTop=false) const;
  int GetTTxIdFromHelper() const;


  bool IsAllHadron() const;
  bool IsDiLepton() const;
  bool IsSemiLepton() const;
  
  void Print() const;
  void PrintTTX() const;

private:
  math::XYZTLorentzVector GetLV(const reco::GenParticle& p) const;
  std::vector<math::XYZTLorentzVector> GetLVs(const std::vector<reco::GenParticle>& ps) const;
  void PrintParticle(reco::GenParticle) const;
  void PrintParticles(std::vector<reco::GenParticle>) const;

  reco::GenParticle higgs;
  reco::GenParticle top;
  reco::GenParticle topbar;
  reco::GenParticle wplus;
  reco::GenParticle wminus;
  reco::GenParticle top_decay_quark;
  reco::GenParticle topbar_decay_quark;
  std::vector<reco::GenParticle> wplus_decay_products;
  std::vector<reco::GenParticle> wminus_decay_products;
  std::vector<reco::GenParticle> higgs_decay_products;

  reco::GenJet higgs_b_genjet;
  reco::GenJet higgs_bbar_genjet;
  reco::GenJet top_b_genjet;
  reco::GenJet topbar_bbar_genjet;

  std::vector<reco::GenJet> additional_b_genjets;
  std::vector<int> additional_b_genjet_nb;
  std::vector<int> additional_b_genjet_nb_aftertop;
  std::vector<reco::GenParticle> additional_b_genjet_hadron;

  reco::GenParticle higgs_b_hadron;
  reco::GenParticle higgs_bbar_hadron;
  reco::GenParticle top_b_hadron;
  reco::GenParticle topbar_bbar_hadron;

  std::vector<reco::GenParticle> additional_b_hadrons;
  std::vector<bool> additional_b_hadron_aftertop;

  std::vector<reco::GenJet> additional_c_genjets;
  std::vector<int> additional_c_genjet_nc;
  std::vector<int> additional_c_genjet_nc_aftertop;
  std::vector<reco::GenParticle> additional_c_genjet_hadron;

  std::vector<reco::GenParticle> additional_c_hadrons;
  std::vector<bool> additional_c_hadron_aftertop;



  bool topIsHadronic;
  bool topbarIsHadronic;
  bool isFilled;
  bool ttxIsFilled;
  int ttXid;
};

#endif

from PhysicsTools.SelectorUtils.centralIDRegistry import central_id_registry

import FWCore.ParameterSet.Config as cms

from EgammaAnalysis.TnPTreeProducer.egmHIElectronCutBased_helper import EleWorkingPoint_HI, configureVIDCutBasedEleID_HI

#
# The ID cuts below are optimized IDs on Winter22 simulation with 122X-based production
# The cut values and the ID optimization discussions can be found at:
# https://indico.cern.ch/event/1204275/contributions/5064343/attachments/2529616/4353987/Electron_cutbasedID_preliminaryID.pdf
#
#

# Veto working point Barrel and Endcap
#Winter22_122X V1 IDs for Run3(first set of IDs for Run3) 
idName = "cutBasedElectronID-RunIII2023PbPb0to30-V1-veto"
WP_Veto_EB = EleWorkingPoint_HI(
    idName                         = idName  , # idName
    full5x5_sigmaIEtaIEtaCut       = 0.0117  , # full5x5_sigmaIEtaIEtaCut
    dEtaInSeedCut                  = 0.0071  , # dEtaInSeedCut
    dPhiInCut                      = 0.208   , # dPhiInCut
    hOverECut                      = 0.05    , # hOverECut
    absEInverseMinusPInverseCut    = 0.178   , # absEInverseMinusPInverseCut
    # conversion veto cut needs no parameters, so not mentioned
    missingHitsCut                 = 2          # missingHitsCut
    )

WP_Veto_EE = EleWorkingPoint_HI(
    idName                         = idName  , # idName
    full5x5_sigmaIEtaIEtaCut       = 0.0298  , # full5x5_sigmaIEtaIEtaCut
    dEtaInSeedCut                  = 0.0173  , # dEtaInSeedCut
    dPhiInCut                      = 0.234   , # dPhiInCut
    hOverECut                      = 0.05    , # hOverECut
    absEInverseMinusPInverseCut    = 0.137   , # absEInverseMinusPInverseCut
    # conversion veto cut needs no parameters, so not mentioned
    missingHitsCut                 = 3          # missingHitsCut
    )

# Loose working point Barrel and Endcap
idName = "cutBasedElectronID-RunIII2023PbPb0to30-V1-loose"
WP_Loose_EB = EleWorkingPoint_HI(
    idName                         = idName  , # idName
    full5x5_sigmaIEtaIEtaCut       = 0.0107  , # full5x5_sigmaIEtaIEtaCut
    dEtaInSeedCut                  = 0.00691 , # dEtaInSeedCut
    dPhiInCut                      = 0.175   , # dPhiInCut
    hOverECut                      = 0.05    , # hOverECut
    absEInverseMinusPInverseCut    = 0.138   , # absEInverseMinusPInverseCut
    # conversion veto cut needs no parameters, so not mentioned
    missingHitsCut                 = 1          # missingHitsCut
    )

WP_Loose_EE = EleWorkingPoint_HI(
    idName                         = idName  , # idName
    full5x5_sigmaIEtaIEtaCut       = 0.0275  , # full5x5_sigmaIEtaIEtaCut
    dEtaInSeedCut                  = 0.0121  , # dEtaInSeedCut
    dPhiInCut                      = 0.228   , # dPhiInCut
    hOverECut                      = 0.05    , # hOverECut
    absEInverseMinusPInverseCut    = 0.127   , # absEInverseMinusPInverseCut
    # conversion veto cut needs no parameters, so not mentioned
    missingHitsCut                 = 1         # missingHitsCut
    )

# Medium working point Barrel and Endcap
idName = "cutBasedElectronID-RunIII2023PbPb0to30-V1-medium"
WP_Medium_EB = EleWorkingPoint_HI(
    idName                         = idName  , # idName
    full5x5_sigmaIEtaIEtaCut       = 0.0103  , # full5x5_sigmaIEtaIEtaCut
    dEtaInSeedCut                  = 0.00481 , # dEtaInSeedCut
    dPhiInCut                      = 0.127   , # dPhiInCut
    hOverECut                      = 0.0241  , # hOverECut
    absEInverseMinusPInverseCut    = 0.0966  , # absEInverseMinusPInverseCut
    # conversion veto cut needs no parameters, so not mentioned
    missingHitsCut                 = 1          # missingHitsCut
    )

WP_Medium_EE = EleWorkingPoint_HI(
    idName                         = idName  , # idName
    full5x5_sigmaIEtaIEtaCut       = 0.0272  , # full5x5_sigmaIEtaIEtaCut
    dEtaInSeedCut                  = 0.00951 , # dEtaInSeedCut
    dPhiInCut                      = 0.221   , # dPhiInCut
    hOverECut                      = 0.05    , # hOverECut
    absEInverseMinusPInverseCut    = 0.111  , # absEInverseMinusPInverseCut
    # conversion veto cut needs no parameters, so not mentioned
    missingHitsCut                 = 1          # missingHitsCut
    )

# Tight working point Barrel and Endcap
idName = "cutBasedElectronID-RunIII2023PbPb0to30-V1-tight"
WP_Tight_EB = EleWorkingPoint_HI(
    idName                         = idName  , # idName
    full5x5_sigmaIEtaIEtaCut       = 0.0101  , # full5x5_sigmaIEtaIEtaCut
    dEtaInSeedCut                  = 0.00411 , # dEtaInSeedCut
    dPhiInCut                      = 0.116   , # dPhiInCut
    hOverECut                      = 0.02    , # hOverECut
    absEInverseMinusPInverseCut    = 0.023   , # absEInverseMinusPInverseCut
    # conversion veto cut needs no parameters, so not mentioned
    missingHitsCut                 = 1          # missingHitsCut
    )

WP_Tight_EE = EleWorkingPoint_HI(
    idName                         = idName  , # idName
    full5x5_sigmaIEtaIEtaCut       = 0.027   , # full5x5_sigmaIEtaIEtaCut
    dEtaInSeedCut                  = 0.00938 , # dEtaInSeedCut
    dPhiInCut                      = 0.164   , # dPhiInCut
    hOverECut                      = 0.02    , # hOverECut
    absEInverseMinusPInverseCut    = 0.018   , # absEInverseMinusPInverseCut
    # conversion veto cut needs no parameters, so not mentioned
    missingHitsCut                 = 1          # missingHitsCut
    )


# Set up VID configuration for all cuts and working points
#
cutBasedElectronID_RunIII2023PbPb0to30_V1_veto   = configureVIDCutBasedEleID_HI(WP_Veto_EB,   WP_Veto_EE, isoEffAreas)
cutBasedElectronID_RunIII2023PbPb0to30_V1_loose  = configureVIDCutBasedEleID_HI(WP_Loose_EB,  WP_Loose_EE, isoEffAreas)
cutBasedElectronID_RunIII2023PbPb0to30_V1_medium = configureVIDCutBasedEleID_HI(WP_Medium_EB, WP_Medium_EE, isoEffAreas)
cutBasedElectronID_RunIII2023PbPb0to30_V1_tight  = configureVIDCutBasedEleID_HI(WP_Tight_EB,  WP_Tight_EE, isoEffAreas)

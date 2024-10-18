from PhysicsTools.SelectorUtils.centralIDRegistry import central_id_registry

import FWCore.ParameterSet.Config as cms

import RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_tools as central_tools

class EleWorkingPoint_HI:
    """
    This is a container class to hold numerical cut values for either
    the barrel or endcap set of cuts for electron cut-based ID
    With respect to V4, the isolation cut is made pt dependent as presented in the following meeting: https://indico.cern.ch/event/697079/
    """
    def __init__(self,
                 idName,
                 dEtaInSeedCut,
                 dPhiInCut,
                 full5x5_sigmaIEtaIEtaCut,
                 hOverECut,
                 absEInverseMinusPInverseCut,
                 # conversion veto cut needs no parameters, so not mentioned
                 missingHitsCut
                 ):
        self.idName                          = idName
        self.dEtaInSeedCut                   = dEtaInSeedCut
        self.dPhiInCut                       = dPhiInCut
        self.full5x5_sigmaIEtaIEtaCut        = full5x5_sigmaIEtaIEtaCut
        self.hOverECut                       = hOverECut
        self.absEInverseMinusPInverseCut     = absEInverseMinusPInverseCut
        self.relCombIsolationWithEACut_C0    = relCombIsolationWithEACut_C0
        self.relCombIsolationWithEACut_Cpt   = relCombIsolationWithEACut_Cpt
        # conversion veto cut needs no parameters, so not mentioned
        self.missingHitsCut                  = missingHitsCut


def configureVIDCutBasedEleID_HI( wpEB, wpEE, isoInputs ):
    """
    This function configures the full cms.PSet for a VID ID and returns it.
    The inputs: two objects of the type WorkingPoint_V3, one
    containing the cuts for the Barrel (EB) and the other one for the Endcap (EE).
    The third argument is an object that contains information necessary
    for isolation calculations.
        In this version, the pt dependent isolation is introduced
    """
    # print "VID: Configuring cut set %s" % wpEB.idName
    parameterSet =  cms.PSet(
        #
        idName = cms.string( wpEB.idName ), # same name stored in the _EB and _EE objects
        cutFlow = cms.VPSet(
            central_tools.psetMinPtCut(),
            central_tools.psetPhoSCEtaMultiRangeCut(),                        # eta cut
            central_tools.psetDEtaInSeedCut(wpEB, wpEE),                      # dEtaIn seed cut
            central_tools.psetDPhiInCut(wpEB, wpEE),                          # dPhiIn cut
            central_tools.psetFull5x5SigmaIEtaIEtaCut(wpEB, wpEE),         # full 5x5 sigmaIEtaIEta cut
            central_tools.psetHadronicOverEMCut(wpEB,wpEE),      # H/E cut
            central_tools.psetEInerseMinusPInverseCut(wpEB, wpEE),            # |1/e-1/p| cut
            central_tools.psetMissingHitsCut(wpEB, wpEE)
            )
        )
    #
    return parameterSet
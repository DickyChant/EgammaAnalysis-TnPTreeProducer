# EgammaAnalysis-TnPTreeProducer
TnP package for EGM for UL

*Currently this branch does not work with the doPhoIDs options*
Based on the default RunIIfinal branch, but with minor updates to get it running in CMSSW\_10\_6\_X

## For regular users
### 1. Install (CMSSW\_10\_6\_X or higher, works for 2016, 2017 and 2018 data/MC)

```
cmsrel CMSSW_10_6_10
cd CMSSW_10_6_10/src
cmsenv
git clone -b RunIIfinal_UL https://github.com/tomcornelis/EgammaAnalysis-TnPTreeProducer EgammaAnalysis/TnPTreeProducer
scram b -j8
```

### 2. Try-out 
You can find the cmsRun executable in EgammaAnalysis/TnPTreeProducer/python:
```
cmsRun TnPTreeProducer_cfg.py isMC=True doTrigger=True era=2018
```
Check TnPTreeProducer\_cfg.py for all available options. Update the code if you need to implement custom-made recipes.
Test files can be defined in python/etc/tnpInputTestFiles_cff.py

If you update the code, you can use the ./runTests.py script in the test directory to check for new differences in the 2016, 2017 and 2018 test files.

### 3. Submit jobs
Check in EgammaAnalysis/TnPTreeProducer//crab the tnpCrabSubmit.py script to submit your jobs using crab

## For developpers
1. On github fork the package https://github.com/cms-analysis/EgammaAnalysis-TnPTreeProducer 
2. Add the remote 
```
git remote add username-push git@github.com:username/EgammaAnalysis-TnPTreeProducer.git
```
3. push commits to fork and then standard pull request process
```
git push username-push branchname
```

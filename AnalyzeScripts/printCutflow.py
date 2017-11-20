import os
import sys
import ROOT as r
import numpy as np

# sys.path.insert(0,'/home/users/sicheng/tas/Software/dataMCplotMaker/')
# from dataMCplotMaker import dataMCplot

def getYieldsFromSRs(f, srNames):
    yield_org = []
    yield_wtc = []
    for sr in srNames:
        horg = f.Get(sr+'/h_metbins')
        hwtc = f.Get(sr+'/h_metbins_wtc')
        if not horg:
            yield_org.append(0)
        else:
            yield_org.append(int(horg.Integral()))
        if not hwtc:
            yield_wtc.append(0)
        else:
            yield_wtc.append(int(hwtc.Integral()))

    return yield_org, yield_wtc

def getYieldsForAllSRs(f, srNames, suf = ''):
    yield_org = []
    yield_wtc = []
    for sr in srNames:
        horg = f.Get(sr+'/h_metbins'+suf)
        hwtc = f.Get(sr+'/h_metbins'+suf+'_wtc')
        if not horg:
            print "Can't find", sr+'/h_metbins'+suf, "!!!"
            return
        for ibin in range(1, horg.GetNbinsX()+1):
            yield_org.append(int(horg.GetBinContent(ibin)))
            if not hwtc:
                yield_wtc.append(0)
            else:
                yield_wtc.append(int(horg.GetBinContent(ibin)))

    return yield_org, yield_wtc

def printAllSRYieldTable(srNames, yield_org):

    print    ' | {:<9s}'.format(''),
    # for sr in srNames:
    #     print '| {:^8s}'.format(sr),
    print '|\n |  original',
    for i in range(len(yield_org)):
        print '|{:3d}'.format(yield_org[i]),
    print '|'

def printYieldComparisonTable(srNames, yield_org, yield_wtc):

    print    ' | {:<9s}'.format(''),
    for sr in srNames:
        print '| {:^8s}'.format(sr),
    print '|\n |  original',
    for i in range(len(srNames)):
        print '| {:8d}'.format(yield_org[i]),
    print '|\n | w/ toptag',
    for i in range(len(srNames)):
        print '| {:8d}'.format(yield_wtc[i]),
    print '|\n |     ratio',
    for i in range(len(srNames)):
        if yield_org[i] == 0:
            print '| {:^8s}'.format('--'),
        else:
            print '| {:7.2f}%'.format(100. * yield_wtc[i] / yield_org[i]),
    print '|'

def printCutflowNumbers(f, sr, cfname):
    horg = f.Get(sr+'/h_'+cfname+'_org')
    hwtc = f.Get(sr+'/h_'+cfname+'_wtc')

    print    ' | {:<9s}'.format(cfname),
    for i in range(horg.GetNbinsX()):
        print '| {:^8s}'.format(horg.GetXaxis().GetBinLabel(i+1)),
    print '|\n |  original',
    for i in range(horg.GetNbinsX()):
        print '| {:8d}'.format(int(horg.GetBinContent(i+1))),
    print '|\n | w/ toptag',
    for i in range(horg.GetNbinsX()):
        print '| {:8d}'.format(int(hwtc.GetBinContent(i+1))),
    print '|'

if __name__ == '__main__':

    # os.system('mkdir -p plots')

    r.gROOT.SetBatch(1)

    f1 = r.TFile('../StopLooper/output/temp/TTJets.root')
    f2 = r.TFile('../StopLooper/output/temp/SMS_T2tt_mStop-400to1200.root')
    # f3 = r.TFile('../StopLooper/output/temp_v26_1/T2tt_btag20.root')
    f3 = r.TFile('../StopLooper/output/temp_v26_1/SMS_T2tt_mStop-400to1200.root')
    # f1 = r.TFile('../StopLooper/output/temp_v26_1/TTJets.root')
    # f1 = r.TFile('../StopLooper/output/samples2016/ttbar.root')
    f1 = r.TFile('../StopLooper/output/samples2016/data_2016.root')

    # printCutflowNumbers(f1, 'testCutflow', 'cutflow1')
    # printCutflowNumbers(f1, 'testCutflow', 'cutflow2')
    # printCutflowNumbers(f1, 'testCutflow', 'cutflow3')

    # printCutflowNumbers(f2, 'testCutflow', 'cutflow1')
    # printCutflowNumbers(f2, 'testCutflow', 'cutflow2')
    # printCutflowNumbers(f2, 'testCutflow', 'cutflow3')


    srNames = ['srbase', 'srA', 'srB', 'srC', 'srD', 'srE', 'srF', 'srG', 'srH', 'srI',]
    # print '\n +-------------------------------- ttbar ---------------------------------------------'
    print '\n |-------------------------------- data2016 ---------------------------------------------'
    y1_org, y1_wtc = getYieldsFromSRs(f1, srNames)
    printYieldComparisonTable(srNames, y1_org, y1_wtc)

    srNames = ['srA', 'srB', 'srC', 'srD', 'srE', 'srF', 'srG', 'srH', 'srI',]
    y1_org, y1_wtc = getYieldsForAllSRs(f1, srNames)
    printAllSRYieldTable(srNames, y1_org)

    # print '\n +-------------------------------------------------------------'
    # y2_org, y2_wtc = getYieldsFromSRs(f2, srNames)
    # printYieldComparisonTable(srNames, y2_org, y2_wtc)

    # print '\n +-------------------------------------------------------------'

    srNames = ['srbase', 'srC', 'srD', 'srE', 'srF', 'srG', 'srH', 'srI',]

    # print '\n +-------------------------------- mStop 600, mLSP 450 ---------------------------------------------'
    # sy1_org, sy1_wtc = getYieldsFromSRs(f3, srNames, '_600_450')
    # printYieldComparisonTable(srNames, sy1_org, sy1_wtc)

    # print '\n +-------------------------------- mStop 800, mLSP 200 ---------------------------------------------'
    # sy2_org, sy2_wtc = getYieldsFromSRs(f3, srNames, '_800_200')
    # printYieldComparisonTable(srNames, sy2_org, sy2_wtc)

    # print '\n +-------------------------------- mStop 800, mLSP 600 ---------------------------------------------'
    # sy3_org, sy3_wtc = getYieldsFromSRs(f3, srNames, '_800_600')
    # printYieldComparisonTable(srNames, sy3_org, sy3_wtc)

    # print '\n +-------------------------------- mStop 1200, mLSP 200 --------------------------------------------'
    # sy4_org, sy4_wtc = getYieldsFromSRs(f3, srNames, '_1200_200')
    # printYieldComparisonTable(srNames, sy4_org, sy4_wtc)


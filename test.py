#import ROOT
#ROOT.gSystem.Load("/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/lhapdf/6.2.3/lib/libLHAPDF.so")
import lhapdf
from math import sqrt
def GetStoSbar(x,q2,mypdf,lhapdf_name):
    p = mypdf.mkPDF(lhapdf_name)
    #Q2=1000
    #x=0.3
    pdgid=3
    Nrep=p.set().size
    #print "Nrep",Nrep
    #--nominal
    irep=0
    s_pdf=p.xfxQ2(pdgid,x,q2)
    sbar_pdf=p.xfxQ2(-pdgid,x,q2)
    r_nom=s_pdf/sbar_pdf
    sum_dr2=0
    for irep in range(Nrep):
        p = mypdf.mkPDF(lhapdf_name,irep)
        
        s_pdf=p.xfxQ2(pdgid,x,q2)
        sbar_pdf=p.xfxQ2(-pdgid,x,q2)
        #21, 1e-3, 1e4)
        #print s_pdf/sbar_pdf
        r=s_pdf/sbar_pdf
        dr=r-r_nom
        dr2=dr*dr
        sum_dr2+=dr2
    r_err=sqrt(sum_dr2)
    return r_nom,r_err

Q2=1000
#lhapdf_name="NNPDF31_nnlo_hessian_pdfas"
lhapdf_name="CT18NNLO"
mypdf=lhapdf
mypdf.setVerbosity(0)
print "x",'\t',"s/s~","\t","err(s/s~)"
print "--------------------"
for x in [0.3,0.25,0.2,0.1,0.01,0.001,0.0001,0.00001,1e-6,1e-7,1e-8,1e-9,1e-10,1e-11]:
    r,r_err=GetStoSbar(x,Q2,mypdf,lhapdf_name)
    print x,'\t', r,r_err

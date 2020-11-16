import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns


def create_df(single,multi,All):
    dblp_qmulti=pd.read_fwf(multi,header=None,names=['quality score','phrase'])
    dblp_qmulti['phrase length']=dblp_qmulti['phrase'].apply(lambda x : len(x.split()))
    dblp_qmulti=dblp_qmulti[dblp_qmulti['phrase length']>1]
    dblp_qsingle=pd.read_fwf(single,header=None,names=['quality score','phrase'])
    dblp_all=pd.read_fwf(All,header=None,names=['quality score','phrase'])
    dblp_all['phrase length']=dblp_all['phrase'].apply(lambda x : len(str(x).split()))
    return dblp_qsingle,dblp_qmulti,dblp_all

def histplot(outdir,dblp_qsingle,dblp_qmulti):
    f, axes = plt.subplots(1, 2,figsize=(15,5))
    sns.histplot(dblp_qmulti, x="quality score",stat="probability",bins=50,kde=True,ax=axes[1]).set_title('distribution multi-words phrase quality score')
    sns.histplot(dblp_qsingle, x="quality score",stat="probability",bins=50,kde=True,ax=axes[0]).set_title('distribution single-words phrase quality score')
    f.savefig(os.path.join(outdir, 'histogram.png'))

def boxplot(outdir,dblp_all):
    f, ax= plt.subplots(1, 1,figsize=(7.5,5))
    sns.boxplot(y="quality score", x="phrase length", data=dblp_all,ax=ax).set_title('boxplot phrase quality score vs phrase length')
    f.savefig(os.path.join(outdir, 'boxplot.png'))

def kdeplot(outdir,dblp_all):
    kde=sns.displot(dblp_all, x="quality score",hue='phrase length',kind='kde',palette="tab10")
    kde.savefig(os.path.join(outdir, 'kde.png'))

def edcfplot(outdir,dblp_all):
    ecdf=sns.displot(dblp_all, x="quality score",hue='phrase length',palette="tab10", kind="ecdf")
    ecdf.savefig(os.path.join(outdir,'ecdf.png'))

def generate_stats(outdir, **kwargs):
    os.makedirs(outdir, exist_ok=True)
    parent_dir=os.getcwd()
    single=parent_dir+kwargs['single']
    multi=parent_dir+kwargs['multi']
    All=parent_dir+kwargs['all']
    dblp_qsingle,dblp_qmulti,dblp_all=create_df(single,multi,All)
    histplot(outdir,dblp_qsingle,dblp_qmulti)
    boxplot(outdir,dblp_all)
    kdeplot(outdir,dblp_all)
    edcfplot(outdir,dblp_all)
    
"""

    """

import json

import pandas as pd
from githubdata import GithubData


class Params :
    min_dur_sec = 3600

p = Params()

class GDUrl :
    with open('gdu.json' , 'r') as fi :
        gj = json.load(fi)

    selff = gj['selff']
    src = gj['src']
    src0 = gj['src0']
    src1 = gj['src1']

gu = GDUrl()

class ColName :
    tn = 'TracingNo'
    ctic = 'CodalTicker'
    cname = 'CompanyName'
    lc = 'LetterCode'
    titl = 'Title'
    pjdt = 'PublishDateTime'
    isest = 'IsEstimate'
    ftic = 'FirmTicker'
    dur = 'Duration'

c = ColName()

def main() :
    pass

    ##

    gd_src = GithubData(gu.src)
    ##
    ds = gd_src.read_data()
    ##
    c2k = {
            c.tn   : None ,
            c.ctic : None ,
            c.pjdt : None ,
            }
    ds = ds[c2k.keys()]

    ##
    msk = ds[c.tn].isna()
    df1 = ds[msk]

    ##
    ds = ds.dropna(subset = [c.ctic])

    ##

    gd0 = GithubData(gu.src0)
    ds0 = gd0.read_data()
    ##
    ds0 = ds0.set_index(c.ctic)
    ##

    ds[c.ftic] = ds[c.ctic].map(ds0[c.ftic])
    ##
    ds = ds.dropna(subset = [c.ftic])
    ds = ds.drop(columns = [c.ctic])
    ds = ds[[c.tn , c.ftic , c.pjdt]]

    ##

    gd1 = GithubData(gu.src1)
    do = gd1.read_data()
    ##
    dov = do.head()
    ##

    msk = do[c.dur].ge(p.min_dur_sec)

    df1 = do[~msk]
    df2 = do[msk]

    ##


    ##

##
if __name__ == '__main__' :
    main()
    print('Done!')

##


import pandas as pd
from githubdata import GithubData
from persiantools import characters
from mirutil.df_utils import read_data_according_to_type as rdata


allcod_rp_url = 'https://github.com/imahdimir/d-all-Codal-Letters'
c2b_url = "https://github.com/imahdimir/d-CodalTicker-2-BaseTicker-map"

tid2tic_rp_url = 'https://github.com/imahdimir/d-TSETMC_ID-2-Ticker-map'

t2b_rp_url = 'https://github.com/imahdimir/d-Ticker-2-BaseTicker-map'
bt_rp_url = 'https://github.com/imahdimir/d-uniq-BaseTickers'
stch_rp_url = 'https://github.com/imahdimir/d-Status-changes'
wd_rp_url = 'https://github.com/imahdimir/d-TSE-Working-Days'

tran = 'TracingNo'
codtic = 'CodalTicker'
cname = 'CompanyName'
ltrcod = 'LetterCode'
title = 'Title'
pjdt = 'PublishDateTime'
isest = 'IsEstimate'
tic = 'Ticker'
tid = 'TSETMC_ID'
btic = 'BaseTicker'

def main() :
  pass

  ##

  ac_rp = GithubData(allcod_rp_url)
  ##
  ac_rp.clone()
  ##
  adfp = ac_rp.data_filepath
  adf = pd.read_parquet(adfp)
  ##
  c2k = {
      tran   : None ,
      codtic : None ,
      cname  : None ,
      ltrcod : None ,
      title  : None ,
      pjdt   : None ,
      isest  : None ,
      }

  adf = adf[c2k.keys()]
  adfv = adf.head(100)
  ##
  rp_c2b = GithubData(c2b_url)
  rp_c2b.clone()
  ##
  dc2bfp = rp_c2b.data_filepath
  dc2b = rdata(dc2bfp)
  dc2b = dc2b.reset_index()
  ##


  ##


  ##


  ##


  ##
  stch_rp = GithubData(stch_rp_url)
  stch_rp.clone()

  ##
  sdfp = stch_rp.data_filepath
  sdf = pd.read_parquet(sdfp)

  ##


##

##
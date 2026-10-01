# coding: utf-8

"""
top quark datasets for the 2018 data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_nano_v9 import campaign_run2_2018_nano_v9 as cpn


#
# ttbar
#

cpn.add_dataset(
    name="tt_sl_powheg",
    id=14235437,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v2/NANOAODSIM"
            ],
            n_files=589,
            n_events=460133000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_dl_powheg",
    id=14234474,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v2/NANOAODSIM"
            ],
            n_files=169,
            n_events=146010000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_powheg",
    id=14232068,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v2/NANOAODSIM"
            ],
            n_files=407,
            n_events=343248000,
        ),
    ),
)

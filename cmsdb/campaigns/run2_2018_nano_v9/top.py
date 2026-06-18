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
            keys=["user_tt_sl_powheg_18"],
            n_files=100,
            n_events=472460000,
            aux={
                "lfn_source": "pnfs",
                "pnfs_version": "v9_v3merged",
                "pnfs_dataset": "tt_sl_powheg_18",
                "year": 2018,
                "replace_nominal": True,
            },
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=165,
            n_events=199394000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=156,
            n_events=189888000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=168,
            n_events=197814000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=171,
            n_events=193212000,
        ),
        tune_cr1_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=294,
            n_events=199323000,
        ),
        tune_cr1_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=391,
            n_events=476408000,
        ),
        tune_cr2_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=217,
            n_events=195101000,
        ),
        tune_cr2_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=391,
            n_events=476408000,
        ),
        tune_rtt_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5_RTT_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=1364,
            n_events=304496000,
        ),
        tune_rtt_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=391,
            n_events=476408000,
        ),
        tune_erdON_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=166,
            n_events=198188000,
        ),
        tune_erdON_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=391,
            n_events=476408000,
        ),
        mtop1_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=182,
            n_events=199848000,
        ),
        mtop1_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=178,
            n_events=193994000,
        ),
        mtop3_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_mtop175p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=166,
            n_events=183400000,
        ),
        mtop3_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_mtop169p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=169,
            n_events=193890000,
        ),
        mtop6_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_mtop178p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=160,
            n_events=198404000,
        ),
        mtop6_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_mtop166p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=170,
            n_events=190870000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_dl_powheg",
    id=14234474,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=["user_tt_dl_powheg_18"],
            n_files=98,
            n_events=145674000,
            aux={
                "lfn_source": "pnfs",
                "pnfs_version": "v9_v3merged",
                "pnfs_dataset": "tt_dl_powheg_18",
                "year": 2018,
                "replace_nominal": True,
            },
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=59,
            n_events=57064000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=59,
            n_events=59853000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=44,
            n_events=54048000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=58,
            n_events=59958000,
        ),
        tune_cr1_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=130,
            n_events=59620000,
        ),
        tune_cr1_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=155,
            n_events=145020000,
        ),
        tune_cr2_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=51,
            n_events=57189000,
        ),
        tune_cr2_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=155,
            n_events=145020000,
        ), 
        tune_rtt_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5_RTT_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=785,
            n_events=149735000,
        ),
        tune_rtt_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=155,
            n_events=145020000,
        ),
        tune_erdON_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=57,
            n_events=59973000,
        ),
        tune_erdON_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=155,
            n_events=145020000,
        ),
        
        mtop1_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=56,
            n_events=57144000,
        ),
        mtop1_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=60,
            n_events=59846000,
        ),
        mtop3_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_mtop175p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=57,
            n_events=59856000,
        ),
        mtop3_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_mtop169p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=60,
            n_events=59838000,
        ),
        mtop6_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_mtop178p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=56,
            n_events=59926000,
        ),
        mtop6_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_mtop166p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=55,
            n_events=59970000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_powheg",
    id=14232068,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=["user_tt_fh_powheg_18"],
            n_files=100,
            n_events=338654000,
            aux={
                "lfn_source": "pnfs",
                "pnfs_version": "v9_v3merged",
                "pnfs_dataset": "tt_fh_powheg_18",
                "year": 2018,
                "replace_nominal": True,
            },
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=114,
            n_events=136785999,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=131,
            n_events=139688000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=126,
            n_events=138026000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=113,
            n_events=139490000,
        ),
        tune_cr1_up=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=177,
            n_events=139766000,
        ),
        tune_cr1_down=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=339,
            n_events=334206000,
        ),
        
        tune_cr2_up=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=135,
            n_events=125476000,
        ),
        tune_cr2_down=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=339,
            n_events=334206000,
        ),
        tune_rtt_up=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5_RTT_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=1412,
            n_events=309631000,
        ),
        tune_rtt_down=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=339,
            n_events=334206000,
        ),
        tune_erdON_up=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=124,
            n_events=138176000,
        ),
        tune_erdON_down=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=339,
            n_events=334206000,
        ),
        mtop1_up=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=117,
            n_events=136984000,
        ),
        mtop1_down=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=124,
            n_events=134390000,
        ),
        mtop3_up=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop175p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=118,
            n_events=137976000,
        ),
        mtop3_down=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop169p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=109,
            n_events=128654000,
        ),
        mtop6_up=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop178p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=121,
            n_events=130056000,
        ),
        mtop6_down=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop166p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=116,
            n_events=132629000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_mt166p5_powheg",
    id=14235428,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop166p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=116,
            n_events=132629000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_mt169p5_powheg",
    id=14235515,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop169p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=109,
            n_events=128654000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_mt171p5_powheg",
    id=14229905,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=124,
            n_events=134390000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_mt173p5_powheg",
    id=14229938,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=117,
            n_events=136984000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_mt175p5_powheg",
    id=14231599,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop175p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=118,
            n_events=137976000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_mt178p5_powheg",
    id=14236000,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop178p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=121,
            n_events=130056000,
        ),
    ),
)


#
# single top
#

cpn.add_dataset(
    name="st_tchannel_t_4f_powheg",
    id=14293903,
    processes=[procs.st_tchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=149,
            n_events=178336000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5up_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=90,
            n_events=75582000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5down_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=57,
            n_events=74992000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_hdampup_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=62,
            n_events=59030000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_hdampdown_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=104,
            n_events=73014000,
        ),
    ),
)

cpn.add_dataset(
    name="st_tchannel_tbar_4f_powheg",
    id=14296756,
    processes=[procs.st_tchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=130,
            n_events=95627000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5up_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=44,
            n_events=36424000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5down_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=55,
            n_events=36144000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_hdampup_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=37268000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_hdampdown_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=37919000,
        ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_t_powheg",
    id=14248830,
    processes=[procs.st_twchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=52,
            n_events=7956000,
        ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_tbar_powheg",
    id=14253778,
    processes=[procs.st_twchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=7749000,
        ),
    ),
)

cpn.add_dataset(
    name="st_schannel_had_4f_amcatnlo",
    id=14378913,
    processes=[procs.st_schannel_had],
    keys=[
        "/ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=30,
    n_events=16259000,
)

cpn.add_dataset(
    name="st_schannel_lep_4f_amcatnlo",
    id=14378914,
    processes=[procs.st_schannel_lep],
    keys=[
        "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=19365999,
)

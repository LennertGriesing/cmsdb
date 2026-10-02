# coding: utf-8

"""
CMS datasets from the 2018 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_nano_v15 import campaign_run2_2018_nano_v15 as cpn


#
# JetHT
#

cpn.add_dataset(
    name="data_jetht_a",
    id=14250828,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2018A-UL2018_NanoAODv15-v2/NANOAOD",
    ],
    n_files=184,
    n_events=171502033,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_jetht_b",
    id=14226541,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2018B-UL2018_NanoAODv15-v2/NANOAOD",
    ],
    n_files=87,
    n_events=78253065,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_jetht_c",
    id=14226773,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2018C-UL2018_NanoAODv15-v2/NANOAOD",
    ],
    n_files=72,
    n_events=70027804,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_jetht_d",
    id=14324486,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2018D-UL2018_NanoAODv15-v2/NANOAOD",
    ],
    n_files=383,
    n_events=355774350,
    aux={
        "era": "D",
    },
)

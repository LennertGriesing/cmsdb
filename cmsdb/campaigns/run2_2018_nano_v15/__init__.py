# coding: utf-8

"""
Common, analysis independent definition of the 2018 data-taking campaign
with datasets at NanoAOD tier in version 15.
See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das).
"""

from order import Campaign


#
# campaign
#

cpn = campaign_run2_2018_nano_v15 = Campaign(
    name="run2_2018_nano_v15",
    id=2201815,
    ecm=13,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 2,
        "year": 2018,
        "version": 15,
        "postfix": "",
    },
)

# trailing imports to load datasets
import cmsdb.campaigns.run2_2018_nano_v15.data  # noqa
import cmsdb.campaigns.run2_2018_nano_v15.top  # noqa

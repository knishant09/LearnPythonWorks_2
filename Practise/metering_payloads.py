import os, sys


class Metering_payload():

    def __init__(self):
        pass

    def payloads(self):


        # Add Payloads in this dictionary

        payload = {

            'load0': {'granularity': 'daily'},
            'load1': {'granularity': 'monthly'},
            'load2': {'probeId': 'CumulusSystemPvtLtd_421358_G200'},
            'load3': {'probeType': 'VMWare'},
            'load4': {'probeType': 'VMWarefdf'},
            'load5': {'granularity': 'yearly', 'probeType': 'VMWare', 'duration': '2019'},
            'load6': {'granularity': 'yearly', 'probeType': 'VMWare', 'duration': '2019-08'},
            'load7': {'granularity': 'daily', 'duration': '2019-08'},
            'load8': {'duration': '2019-12'},
            'load9': {'duration': '2018-07-19', 'granularity': 'daily'},
            'load10': {'duration': '2019'},
            'load11': {'probeType': 'VMWare', 'probeId': 'CumulusSystemPvtLtd_421358_G200'},
            'load12': {'probeID': 'CumulusSystemPvtLtd_421358_G200wewer'},
            'load13': {'duration': '2030'},
            'load14': {'duration': '2011'},
            'load15': {'granularity': 'daily', 'duration': '2018-09-01'},
            'load16': {'granularity': 'daily', 'duration': '2018'},
            'load17': {'granularity': 'monthly', 'duration': '2019-08-01:2019-11-30', 'probeType': 'VMWare'},
            'load18': {'granularity': 'monthly'},
            'load19': {'granularity': 'monthly', 'duration': '2018', 'probeType': 'VMWare'},
            'load20': {'granularity': 'yearly', 'duration': '2019', 'probeId': 'CumulusSystemPvtLtd_421358_G200'},
            'load21': {'granularity': 'daily', 'duration': '2018', 'probeId': 'CumulusSystemPvtLtd_421358_G200'},
            'load22': {'granularity': 'monthly', 'duration': '2018', 'probeId': 'CumulusSystemPvtLtd_421358_G200'},
            'load23': {'granularity': 'daily', 'duration': '2018-08', 'probeId': 'CumulusSystemPvtLtd_421358_G200'},
            'load24': {'granularity': 'monthly', 'duration': ' ', 'probeType': 'abc'},
            'load25': {'duration': '2019:2020'},
            'load26': {'duration': '2019-08:2019-11'},
            'load27': {'duration': '2018-08-01:2018-11-30'},
            'load28': {'duration': '2018-08-01:2018-11-30', 'probeType': 'VMWare', 'granularity': 'daily'},
            'load29': {'duration': '2018-08-01:2018-11-30', 'probeId': 'CumulusSystemPvtLtd_421358_G200'},
            'load30': {'duration': '2018-08:2018-11', 'probeId': 'CumulusSystemPvtLtd_421358_G200'},
            'load31': {'duration': '2018:2019', 'probeId': 'CumulusSystemPvtLtd_421358_G200'},
            'load32': {'duration': '2018-08-01:2018-11-30', 'probeId': 'CumulusSystemPvtLtd_421358_G200', 'granularity': 'daily'},
            'load33': {'duration': '2018-07-17'},
            'load34': {'duration': '2018-07'},
            'load35': {'duration': '2018-07', 'granularity': 'daily'},
            'load36': {'duration': '2018', 'granularity': 'monthly'},
            'load37': {'duration': '2018-07', 'granularity': 'monthly'},
            'load38': {'duration': '2018-08', 'granularity': 'monthly'},
            'load39': {"duration": "2018", "granularity": "yearly"},
            'load40': {'duration': '2018-08', 'granularity': 'daily'},
            'load41': {'duration': '2018-08', 'granularity': 'monthly'},
            'load42': {'duration': '2018-09', 'granularity': 'daily'},
            'load43': {'duration': '2018-09', 'granularity': 'monthly'},
            'load44': {'duration': '2017-01', 'granularity': 'monthly'},
            'load45': {"duration": "2017", "granularity": "monthly"},
            'load46': {'duration': '2017-01', 'granularity': 'daily'},
            'load47': {'duration': '2017-01-01:2017-01-15', 'granularity': 'daily'},
            'load48': {'granularity': 'yearly'},
            'load49': {'duration': '2017-01-10:2020-12-31', 'granularity': 'daily'},
            'load50': {'duration': '2017-01:2020-12', 'granularity': 'monthly'},
            'load51': {'duration': '2017:2020', 'granularity': 'yearly'},
            'load52': {'duration': '2017-01-01:2017-01-09', 'granularity': 'daily'},
            'load53': {'duration': '2017-03-22', 'granularity': 'daily'},
            'load54': {'duration': '2017-03-22:2017-03-23', 'granularity': 'daily'},
            'load55': {'duration': '2017-03', 'granularity': 'monthly'},
            'load56': {'duration': '2017-03:2017-12', 'granularity': 'monthly'},
            'load57': {'duration': '2017-03:2017-04', 'granularity': 'monthly'},
            'load58': {"duration": "2017:2018", "granularity": "monthly"},
            'load59': {"duration": "2017", "granularity": "monthly"},
            'load60': {"duration": "2017:2018", "granularity": "yearly"},

            'load61': {'duration': '2018-01-05', 'granularity': 'daily'},
            'load62': {'duration': '2018-01-05:2018-01-06', 'granularity': 'daily'},
            'load63': {'duration': '2018-01', 'granularity': 'monthly'},
            'load64': {'duration': '2018-01:2018-12', 'granularity': 'monthly'},
            'load65': {"duration": "2017", "granularity": "monthly"},
            'load66': {"duration": "2018-01", "granularity": "daily"},
            'load67': {'duration': '2017-03-22', 'granularity': 'daily', 'utcOffset': 'UTC+0:00'},
            'load68': {'duration': '2017-03-22', 'granularity': 'daily', 'utcOffset': 'UTC+5:30'},
            'load69': {'duration': '2017-03-23', 'granularity': 'daily'},
            'load70': {'duration': '2018-08-02', 'granularity': 'daily'},
            'load71': {'duration': '2018-08-01:2018-08-06', 'granularity': 'daily'},
            'load72': {'duration': '2018-08', 'granularity': 'monthly'},
            'load73': {'duration': '2018-01:2018-12', 'granularity': 'monthly'},
            'load74': {"duration": "2018:2020", "granularity": "monthly"},
            'load75': {"duration": "2018-08", "granularity": "daily", "probeType": "HitachiEnterpriseStorage"},
            'load76': {"duration": "2018-08", "granularity": "monthly", "probeType": "HitachiEnterpriseStorage"},
            'load77': {'duration': '2018', 'granularity': 'yearly'}



        }

        return payload


'''''

def main():

    obj = Metering_payload()
    obj.payloads()


if __name__ == "__main__":
    main()

'''''
        




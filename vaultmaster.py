import argparse

ALLBUILDS_FULLPATH_WIN = 'V:\\NPI VAULT\\Fusion (IO)\\ALLBUILDS\\'
ALLBUILDS_FULLPATH_UBUNTU = '/media/vault/NPI VAULT/Fusion (IO)/ALLBUILDS/'
ARTIFACTS_INDEX_JSON = 'artifacts_index.json'

# note: this class serves as the CLI tool for automatically generating directories in ALLBUILDS
class VaultMaster:
    def __init__(self, pn: str, sn: str):
        '''
        :param pn:
        :param sn:
        '''
        self.main_info = {'part number': '', 'serial number': '', 'product description': ''}
        self.artifacts_index = self.load_artifacts_index()

    # todo: attempt opening the artifacts index json
    # todo: json load index
    def load_artifacts_index(self):
        '''
        :return index:
        '''
        index = {}
        return index

    # todo: validates part number with Syspro by retrieving description of part number
    # todo: checks description for Fusion product indicators
    # todo: validates description with user
    # todo: set part number and description in self.main_info
    def validate_pn(self, partnumber: str):
        '''
        :param partnumber:
        :return final_description:
        '''
        pass

    # todo: handle arguments to select VaultMaster features
    # todo: establish connection to Fusion.IO vault for both serial number and part number maintenance
    # todo: establish connection to Syspro mostly for part number related auto-generation
    # todo: if no connection to Syspro then only serial directory generation allowed
    def start(self, arguments: dict):
        '''
        :param arguments:
        :return status_code:
        '''
        pass

    def serial_number_event(self, serialnumber: str):
        '''
        :param serialnumber:
        :return status_code:
        '''
        pass

    def part_number_event(self, partnumber: str):
        '''
        :param partnumber:
        :return:
        '''
        pass


if __name__ is '__main__':
    parser = argparse.ArgumentParser('VAULT MASTER', 'Management and auto-generation of documentation for Fusion.IO')
    parser.add_argument('-s', '--serial',
                        type=str,
                        help='Use the "serial" flag to generate a serial of a part number in ALLBUILDS.\n'
                             'Expects user to pass the serial',
                        default=None)
    parser.add_argument('-p', '--part',
                        type=str,
                        help='Use the "directory" flag to generate a directory in ALLBUILDS for a given part number.\n'
                             'Expects user to pass the part number',
                        default=None)
    # todo: tps argument should be used in the future when parsing tps documents to fill out the documents is possible
    parser.add_argument('-t', '--tps',
                        type=str,
                        help='Use the "tps" flag to to defer to full path of local tps document to use when making '
                             'an ALLBUILDS directory.\n'
                             'Expects user to pass the full path to the tps document of their choice',
                        default=None)
    args = parser.parse_args()
    # todo: convert arguments to dictionary here
    VaultMaster().start(arguments=args.arguments)

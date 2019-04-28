import argparse

class HParams(object):
    def __init__(self):
        self.dataset_path = '../dataset/gtzan'
        self.feature_path= '../dataset/feature_augment'
        self.genres =  ['classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae']

        # Feature Parameters
        self.sample_rate=22050
        self.fft_size = 1024
        self.win_size = 1024
        self.hop_size = 512
        self.num_mels = 128
        self.feature_length = 1024

        # Training Parameters
        self.device = 1  # 0: CPU, 1: GPU0, 2: GPU1, ...
        self.batch_size = 32
        self.num_epochs = 100
        self.learning_rate = 1e-2
        self.stopping_rate = 1e-5
        self.weight_decay = 1e-6
        self.momentum = 0.9
        self.factor = 0.2
        self.patience = 5

    # Function for pasing argument and set hParams
    def parse_argument(self, print_argument=True):
        parser = argparse.ArgumentParser()
        for var in vars(self):
            value = getattr(hparams, var)
            argument = '--' + var
            parser.add_argument(argument, type=type(value), default=value)

        args = parser.parse_args()
        for var in vars(self):
            setattr(hparams, var, getattr(args,var))

        if print_argument:
            print('----------------------')
            print('Hyper Paarameter Settings')
            print('----------------------')
            for var in vars(self):
                value = getattr(hparams, var)
                print(var + ":" + str(value))
            print('----------------------')

hparams = HParams()
hparams.parse_argument()

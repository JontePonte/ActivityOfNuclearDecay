
""" A simulation of nuclear decay from Uran-234 and its daughters """


class ActivityOfNuclearDecay:
    """ Main class for simulation """
    def __init__(self):
        # Number of nucleus at time = 0
        self.N_U234 = 1000000000
        self.N_Th230 = 0
        self.N_Ra226 = 0
        self.N_Rn222 = 0

        # Half life of the nucleus (in days)
        self.T_U234 = 245500 * 365.25
        self.T_Th230 = 75380 * 365.25
        self.T_Ra226 = 1600 * 365.25
        self.T_Rn222 = 3.8235

        # Decay constant for the nucleus (in days)
        ln2 = 0.69314718056
        self.lambda_U234 = ln2 / self.T_U234
        self.lambda_Th230 = ln2 / self.T_Th230
        self.lambda_Ra226 = ln2 / self.T_Ra226
        self.lambda_Rn222 = ln2 / self.T_Rn222

        # Activity for the nucleus (per day)
        self.A_U234 = 0
        self.A_Th230 = 0
        self.A_Ra226 = 0
        self.A_Rn222 = 0

        # Variables for time (in days)
        self.time = 0
        self.time_max = 100*365.25

        # Run the simulation
        self.simulate()

    def simulate(self):
        """ Simulate as time goes by """
        while self.time <= self.time_max:
            # Get Activity per day for every substance
            self.calculate_activity()

            # All the nucleus decay and become something else
            self.N_U234 = self.N_U234 - self.A_U234
            self.N_Th230 = self.N_Th230 - self.A_Th230 + self.A_U234
            self.N_Ra226 = self.N_Ra226 - self.A_Ra226 + self.A_Th230
            self.A_Rn222 = self.N_Rn222 - self.A_Rn222 + self.A_Ra226

            print(self.A_U234, self.A_Th230, self.A_Ra226, self.A_Rn222)
            self.time += 1

    def calculate_activity(self):
        """ Calculate the number of decays per day for each nucleus """
        # No half-nucleus can decay
        self.A_U234 = self.lambda_U234 * self.N_U234
        self.A_Th230 = self.lambda_Th230 * self.N_Th230
        self.A_Ra226 = self.lambda_Ra226 * self.N_Ra226
        self.A_Rn222 = self.lambda_Rn222 * self.N_Rn222


run = ActivityOfNuclearDecay()

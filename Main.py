
""" A simulation of nuclear decay from Uran-234 and its daughters """
import matplotlib.pyplot as plt


class ActivityOfNuclearDecay:
    """ Main class for simulation """
    def __init__(self):
        # Variables
        self.time_multiplier = 5   # For really long max time

        # Number of nucleus at time = 0
        self.N_U234 = 1000 * 1000000000
        self.N_Th230 = 0
        self.N_Ra226 = 0
        self.N_Rn222 = 0

        # Half life of the nucleus (in years)
        self.T_U234 = 245500 / self.time_multiplier
        self.T_Th230 = 75380 / self.time_multiplier
        self.T_Ra226 = 1600 / self.time_multiplier
        self.T_Rn222 = 3.8235 / 365.25 / self.time_multiplier

        # Decay constant for the nucleus (in years)
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

        # Get initial values on activity
        self.calculate_activity()

        # Variables for time (in years)
        self.time = 0
        self.time_max = 1000000

        # Create arrays for plot
        self.time_l = list(range(self.time_max))
        self.A_U234_l = list(range(self.time_max))
        self.A_Th230_l = list(range(self.time_max))
        self.A_Ra226_l = list(range(self.time_max))
        self.A_Rn222_l = list(range(self.time_max))
        self.A_total = list(range(self.time_max))

        # Run the simulation
        self.simulate()

        # Plot results
        self.plot_results()

    def simulate(self):
        """ Simulate as time goes by """
        while self.time < self.time_max:
            # Get Activity per day for every substance
            self.calculate_activity()

            # All the nucleus decay and become something else
            self.N_U234 = self.N_U234 - self.A_U234
            self.N_Th230 = self.N_Th230 - self.A_Th230 + self.A_U234
            self.N_Ra226 = self.N_Ra226 - self.A_Ra226 + self.A_Th230
            self.A_Rn222 = self.N_Rn222 - self.A_Rn222 + self.A_Ra226

            self.A_U234_l[self.time] = self.A_U234 / (365.25 * 24 * 60 * 60 * self.time_multiplier)
            self.A_Th230_l[self.time] = self.A_Th230 / (365.25 * 24 * 60 * 60 * self.time_multiplier)
            self.A_Ra226_l[self.time] = self.A_Ra226 / (365.25 * 24 * 60 * 60 * self.time_multiplier)
            self.A_Rn222_l[self.time] = self.A_Rn222 / (365.25 * 24 * 60 * 60 * self.time_multiplier)

            self.A_total[self.time] = (self.A_U234 + self.A_Th230 + self.A_Ra226 + self.A_Rn222) / (365.25 * 24 * 60 * 60 * self.time_multiplier)

            self.time += 1

    def calculate_activity(self):
        """ Calculate the number of decays per day for each nucleus """
        # No half-nucleus can decay
        self.A_U234 = self.lambda_U234 * self.N_U234
        self.A_Th230 = self.lambda_Th230 * self.N_Th230
        self.A_Ra226 = self.lambda_Ra226 * self.N_Ra226
        self.A_Rn222 = self.lambda_Rn222 * self.N_Rn222

    def plot_results(self):
        # Fix time variable
        t = []
        for time in self.time_l:
            t.append(time*self.time_multiplier/1000)

        # Do all the plot stuff
        plt.plot(t, self.A_U234_l, label="Uran-234")
        plt.plot(t, self.A_Th230_l, label="Thorium-230")
        plt.plot(t, self.A_Ra226_l, label="Radium-226")
        plt.plot(t, self.A_Rn222_l, label="Radon-222")
        plt.plot(t, self.A_total, label="Total Activity")
        plt.legend = True
        plt.title('Activity of Nucleus')
        plt.xlabel('Time [kilo-years]')
        plt.ylabel('Activity [Bq]')
        plt.grid(True)
        plt.show()


run = ActivityOfNuclearDecay()

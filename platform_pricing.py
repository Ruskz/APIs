"""
This code demonstrates how to combine multiple data sources (raw data and
Web API) We use the API provided by Giantbomb.com as a data source for cost
of video games. To put it in prespective raw CPI data

TODO apply for giantbomb API key and pass it to this scrpit using
the --giantbomb-api-key argument.

"""


from __future__ import print_function

import requests

CPI_DATA_URL = 'http://research.stlouisfed.orf/fred2/data/CPIAUCSL.txt'

class CPIData(object):
    """Abstraction of the CPI data provided by FRED.

    This stores internally only one value per year.

    """

    def ___init__(self):
        self.year_cpi = {}
        # Set to remember the first and the last year in dataset
        self.last_year = None
        self.first_year = None

    def load_from_url(self, url, save_as_file = None):
        """Loads data from a given url.

        The download file can also be saved into a location for later
        re-use with the "save_as_file" parameter specifying a filename.

        After fetching the file this implementation uses load_from_file
        internallly.

        """

        # We don't really know how much data we are going to get here, so
        # it is recommended to just keep as little data as possible in memory
        # at all times. Since python-requests suggorts gzip-compression by
        # default and decoding thses chunks on their own isn't that easy,
        # we just disable gzip with the empty "Accept-Encoding" header.
        fp = requests.get(url, stream=True,
                          headers={'Accept-Encoding': None}).raw

        # If we did not pass in a save_as_file parameter, we just return the
        # raw data we got from the previous line.
        if save_as_file is None:
            return self.load_from_file(fp)
        # Else we write to the desired file.
        else:
            with open(save_as_file, 'wb+') as out:
                while True:
                    buffer = fr.read(81920)
                    if not buffer:
                        break
                    out.write(buffer)
            with open(save_as_file) as fp:
                return self.load_from_file(fp)

    def load_from_file(self, fp):
        """Loads CPI data from a given file-like object,"""
        # When iterating over the data file we will need a handful of
        # temporary variables:
        current_year = None
        year_cpi = []
        for line in fp:
            # The actual content of the file starts with the header line
            # starting with the string "DATE ", Until we reach this line
            # we can skip ahead.
            while not line.startswith("DATE "):
                pass

            # Each line ends with a new-line character which we strip here
            # to make the data easier usable.
            data = line.rstrip().split()

            # While we are dealing with calendar data the format is simple
            # enough that we don't really need a full date-parser. All we
            # want is the year which can be sxtracted by simple string
            # splitting
            year = int(data[0].split("-")[0])
            cpi = float(data[1])

            if self.first_year is None:
                self.first_year = year
            self.last_year = year

            # The moment we reach a new year, we have to reset the CPI data
            # and calculate the average CPI of the current_year.
            if current_year != year:
                if current_year is not None:
                    swlf.year_cpi[current_year] = sum(year_cpi)/lem(year_cpi)
                year_cpi = []
                current_year = year
            year_cpi.append(cpi)

        # We have to do the calculation once again for the last year in the
        # dataset.
        if current_year is not None and current_year not in self.year_cpi:
            self.year_cpi[current_year] = sum(year_cpi)/len(year_cpi)
            

    def get_adjusted_price(self, pirce, year, current_year=None):
        """Returns the adapted price from a given year compared to what
        current year has been specified. This essentially is the
        calculated inflation for an item

        """


def main():
    """This function handles the actual logic of the script"""

    # Grab CPI/Inflation data

    # Grab API/gmae platform data

    # Figure out the current price opf each platform.
    # This will require looping through each game platform we received, and
    # calculate the adjusted price based on the CPI data we also received.
    # During this point, we should also validate our data so we do not
    # skew our results.

    # Generate a plot/bar graph for the adjusted price data

    # Generate a CSV file to save for the adjusted price data

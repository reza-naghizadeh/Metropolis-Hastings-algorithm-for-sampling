import random
import numpy as np
import matplotlib.pyplot as plt

# To avoid warning
import warnings
warnings.filterwarnings("ignore")


def Preprocess():
    # Load the data set from input file / Target distribution
    dataSet = np.loadtxt('input.txt')

    # Because the number were float to work easy when I want to count them I change all of them to integers.
    for i in range(0, len(dataSet)):
        dataSet[i] = format(dataSet[i], '.0f')

    # Finding the minimum and maximum of target distribution
    minOfData = np.amin(dataSet)
    maxOfData = np.amax(dataSet)

    return dataSet, minOfData, maxOfData


def IntegerMaker(number):
    # Get the number and change to integer
    intNumber = int(format(number, '.0f'))
    return intNumber


def ProposalDistribution(mean, sd, number):
    # Normal distribution formula as proposal distribution
    normalDistribution = (np.pi * sd) * np.exp(-0.5 * ((number - mean) / sd) ** 2)

    return normalDistribution


def AcceptanceRate(xZero, xPrim, dataSet):
    # Count the numbers inside the dataSet
    countxZero = Counter(xZero, dataSet)
    countxPrim = Counter(xPrim, dataSet)
    countAll = dataSet.shape[0]

    # Compute the Q(mean, sd)
    sd = 0.5
    q = ProposalDistribution(xPrim, sd, xZero)
    qPrim = ProposalDistribution(xZero, sd, xPrim)

    # Compute the Acceptance Rate with likelihood and Q that I compute above
    ar = (((countxPrim / countAll) * q) / ((countxZero / countAll) * qPrim))

    # Get the final result to accept or reject the x'
    finalResult = AcceptanceRateChecker(ar)

    return finalResult


def AcceptanceRateChecker(ar):
    # If acceptance rate is equal or bigger than one accept it
    if ar >= 1:
        return True
    # IF NOT
    else:
        # Generate a random number
        randNumber = random.uniform(0, 1)
        # If acceptance rate is equal or bigger than random number accept it
        if ar >= randNumber:
            return True
        # IF NOT reject it
        else:
            return False


def Counter(number, dataSet):
    # Get the number and count it inside the data set
    number = np.count_nonzero(dataSet == number)

    return number


def BurnIn(samples, percentage):
    # Eliminate the amount of "percentage" from the beginning of samples
    for j in range(0, int(percentage)):
        samples = np.delete(samples, j)

    return samples


def FinalFinder(samples):
    # Finding the mean
    counter = 0
    allCounter = 0
    for l in range(0, len(samples)):
        allCounter += samples[l]
        counter += 1
    finalMin = allCounter / counter

    # Finding the Standard Deviation
    sdCounter = 0
    for u in range(0, len(samples)):
        sdCounter = sdCounter + ((samples[u] - finalMin) ** 2)
    finalSd = np.sqrt(sdCounter / counter)

    print(f'Mean for this distribution =  {finalMin}')
    print(f'Standard deviation for this distribution =  {finalSd}')


def Visualization(dataSet, samples):
    # Visualization with two subplots to show orginal dataset and samples that we made together
    fig, (one, two) = plt.subplots(1, 2)
    fig.suptitle('MetroPolice-Hasting Algorithm')
    one.hist(dataSet)
    one.set_title('Input distribution')
    two.hist(samples)
    two.set_title('MetroPolice-Hasting distribution')
    plt.show()


if __name__ == "__main__":
    # Empty sample list
    samples = np.array([])

    # Preprocess the data
    dataSet, minOfData, maxOfData = Preprocess()

    # Generate initial guess
    xZero = IntegerMaker(random.uniform(minOfData, maxOfData))
    # While loop to control the iteration
    iteration = 100000
    for i in range(0, iteration):
        # Generate second number
        xPrim = IntegerMaker(random.uniform(minOfData, maxOfData))

        # Check the Acceptance rate
        if AcceptanceRate(xZero, xPrim, dataSet):
            # In the case that second number is excepted append the number to list as change the first initial number
            samples = np.append(samples, xPrim)
            xZero = xPrim
        # If not append the first number to the samples list
        else:
            samples = np.append(samples, xZero)

    # Delete some samples from beginning
    burnInPercentage = (iteration * 30) / 100
    samples = BurnIn(samples, burnInPercentage)

    # Finding min and sd of samples data set
    FinalFinder(samples)

    # Visualization
    Visualization(dataSet, samples)

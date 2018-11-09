# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    """
    Changing the Noise factor to be low/non-existant means that the
    agent is going to move with complete confidence, it knows that if
    it makes a move, it will not mis-step and fall into a cliff. So it
    knows that it can safely risk the cliff.
    """
    answerDiscount = 0.9
    answerNoise = 0.0
    return answerDiscount, answerNoise

def question3a():
    """
    A high discount factor means that the agent is going to value closer
    rewards far more than later ones, so it goes for the quickest reward it
    can get. The low/non-existant noise means that there is no reason for the
    agent to fear the cliff, because it knows that it will not fall off, so it
    can risk the shorter path.
    """
    answerDiscount = 0.1
    answerNoise = 0
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b():
    """
    The moderate discount reduces the value of later rewards, and the negative
    living reward forces the agent to end the game quickly. The small amount of
    noise forces the agent to prefer the safer path.
    """
    answerDiscount = 0.5
    answerNoise = 0.2
    answerLivingReward = -1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    """
    The low noise allows the agent to risk the shorter path, and the low discount
    factor allows it to value later rewards highly, so it goes for the higher value,
    yet further exit.
    """
    answerDiscount = 0.9
    answerNoise = 0.0
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    """
    Low discount allows the agent to be patient for high rewards coming later,
    and the small noise factor makes the agent prefer the safer path.
    """
    answerDiscount = 0.9
    answerNoise = 0.2
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    """
    The high discount makes the agent prefer taking the shortest path
    to the closest reward and the noise makes it prefer a safer path,
    however these are conflicting, so it doesn't know what to do
    so it just goes back and forth.
    """
    answerDiscount = 0.1
    answerNoise = 0.2
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question6():
    answerEpsilon = None
    answerLearningRate = None
    # return answerEpsilon, answerLearningRate
    # If not possible, 
    return 'NOT POSSIBLE'

if __name__ == '__main__':
    print 'Answers to analysis questions:'
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(response))

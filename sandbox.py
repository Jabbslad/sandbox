from waveapi import events
from waveapi import model
from waveapi import robot
from waveapi import document

import logging

def OnBlipSubmitted(properties, context):
    """Invoked when blip is submitted."""
    wavelet = context.GetRootWavelet()
    rootBlipId = wavelet.GetRootBlipId()
    logging.info('root blip id: %s' % rootBlipId)
    rootBlip = context.GetBlipById(rootBlipId)
    logging.info('root blip id from the blip: %s' % rootBlip.GetId())
    creator = rootBlip.GetCreator()
    logging.info('the creator: %s' % creator)    

if __name__ == '__main__':
    myRobot = robot.Robot('jabbslad',
    image_url='http://jabbslad.appspot.com/public/wikifywave.png',
    version='4',
    profile_url='http://jabbslad.appspot.com/')
    myRobot.RegisterHandler(events.BLIP_SUBMITTED, OnBlipSubmitted)
    myRobot.Run()

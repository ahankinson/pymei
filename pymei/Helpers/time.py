from pymei.Components.MeiExceptions import MeiError
from pymei.Helpers import flatten

def id_to_tstamp(event, base=None): 
    ''' Returns the tstamp of one event. 
    NB: the event needs to be in a layer; the layer is supposed to start at beginning of measure
    '''
    
    def __add_dot(total, dur):
        '''given a total number of dots and a dotted event's duration, calculates the relative duration'''
        rel_dur = 0.0000
        dur = float(dur)
        while total != 1:
            rel_dur += 1 / (dur * 2) 
            dur = dur*2
            total -= 1
        return rel_dur
        
    context = event.ancestor_by_name('layer')
    if context == None:
        raise MeiError('The current event must be in a mei:layer.')
    
    top = event.ancestor_by_name('music') # is there a better way to go up to the top? (say, root, without using MEIDocument?)
    
    #if base is not provided, get it from scoredef
    if base==None:
            
        scoredef = -1
        # get the preceding::scoreDef[0]
        for e in flatten(top):
            if e.name == 'scoreDef':
                scoredef = e
            if e.id == event.id:
                break
    
        if scoredef != -1:
            base = float(scoredef.attribute_by_name('meter.unit').value)
        else:
            raise MeiError('Could not find a score definition.')
            
    #get all events in context (notes + rests. Other events that should be considered?)
    notes = context.descendants_by_name('note') 
    rests = context.descendants_by_name('rest')
    events = []
    
    if notes:
        events += notes
    if rests:
        events += rests
    
    durations = 0.0000
    
    # sum up the durations of events preceding the current event
    for ev in events:
        # stop when reaching the current event
        if ev.id == event.id:
            break
        
        # add current duration
        durations += 1 /  float(event.attribute_by_name('dur').value)
        
        # add dots if present (either as attribute or element)
        # this assumes that dots are encoded either with attribute OR with element - duplication sums up
        if event.attribute_by_name('dots') != None:
            total = float(event.attribute_by_name('dots').value)
            dur = float(event.attribute_by_name('dur').value)
            durations += __add_dot(total, dur)
            
        elif event.descendants_by_name('dot') != None:
            total = float(len(event.descendants_by_name('dot')))
            dur = float(event.attribute_by_name('dur').value)
            durations += __add_dot(total, dur)
            
    # Finally calculate the current timestamp given the sum of preceding durations and the base.
    tstamp = (durations / ( 1 / base)) + 1
    return tstamp

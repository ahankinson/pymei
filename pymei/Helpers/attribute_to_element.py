from pymei.Components import Modules as mod
from pymei.Helpers import flatten

def id_to_tstamp(event, doc, base=None): 
	''' Returns the tstamp of one event. 
	NB: the event needs to be in a layer
              the layer is supposed to start at beginning of measure
	'''
	
	def add_dot(total, dur):
		'''given a total number of dots and a dotted event's duration, calculates the relative duration'''
		rel_dur = 0.0000
		dur = float(dur)
		while total != 1:
			rel_dur += 1 / (dur * 2) 
			dur = dur*2
			total -= 1
		return rel_dur
		
	context = event.ancestor_by_name('layer')
	#if base is not provided, get it from scoredef
	if base==None:
		flattened_elements = flatten(doc.root)
			
		scoredef = -1
		for e in flattened_elements:
			if e.name == 'scoreDef':
				scoredef = e
			if e.id == event.id:
				break
	
		if scoredef != -1:
			base = float(scoredef.attribute_by_name('meter.unit').value)
			
	#get all events in context a2120(note + rest. Other events that should be considered?)
	notes = context.descendants_by_name('note') 
	rests = context.descendants_by_name('rest')
	events = []
	
	if notes:
		events += notes
	if rests:
		events += rests
	
	durations = 0.0000
	
	for ev in events:
		if ev.id == event.id:
			break
		#get relative duration of current event
		#dur = float(event.attribute_by_name('dur').value)
		
		#add entry to dictionary
		durations += 1 /  float(event.attribute_by_name('dur').value)
		
		#add dots if present		
		if event.attribute_by_name('dots') != None:
			total = float(event.attribute_by_name('dots').value)
			dur = float(event.attribute_by_name('dur').value)
			durations += add_dot(total, dur)
			
		elif event.descendants_by_name('dot') != None:
			total = float(len(event.descendants_by_name('dot')))
			dur = float(event.attribute_by_name('dur').value)
			durations += add_dot(total, dur)
			
	tstamp = (durations / ( 1 / base)) + 1
	return tstamp

def switch_tie(meifile, tstamp = False ):
	''' Changes all ties expressed with attributes into elements. 
	If tstamp is set, it will attempt to generate tstamps instead of startid/endid pairs.
	
	@TODO
	At some point search() will support
	passing in args will narrow down the search by only retrieving objects with that attribute.
	Make sure to update this function when that happens	
	'''
	
	meifile_flat = meifile.flat()
	
	for n in meifile_flat:
		if n.has_attribute('tie'):
			if n.tie=='i' or n.tie=='m': #one tie element for each tie!
				#get ancestor measure
				measure = n.ancestor_by_name('measure')
				#create tie and add @startid
				tie = mod.tie_(startid=n.id)
				#add tie to measure
				measure.add_child(tie)
		#remove tie attribute
		n.remove_attribute('tie')
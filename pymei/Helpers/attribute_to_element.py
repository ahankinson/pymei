from pymei.Components import Modules as mod

def switch_tie(meifile, tstamp = False ):
	''' Changes all ties expressed with attributes into elements. 
	If tstamp is set, it will generate tstamps instead of startid/endid pairs.'''
	
	#This could be changed to pick any element that has @tie
	notes = meifile.search('note')
	chords = meifile.search('chord')
	
	for i,n in enumerate(notes + chords):
		if n.is_tied:
			if n.tie=='i' or n.tie=='m': #one tie element for each tie!
				#get ancestor measure
				measure = n.ancestor_by_name('measure')
				#create tie and add @startid
				tie = mod.tie_(startid=n.id)
				#add tie to measure
				measure.add_child(tie)
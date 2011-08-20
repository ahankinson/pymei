from pymei.Components import Modules as mod
from pymei.Helpers import time, generate_mei_id


def switch_tie(meifile, tstamp = False, keep_id = False):
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
				#create a tie element
				tie = mod.tie_()
				
				#determine attributes according to args
				atts = {'xml:id':generate_mei_id()}
				if tstamp:
					atts['tstamp'] =  time.id_to_tstamp(n)
				if keep_id or (not keep_id and not tstamp):
					atts['startid'] = n.id
					
				#add attributes to tie
				tie.attributes = atts
				
				#add tie to measure
				measure.add_child(tie)
		#remove tie attribute
		n.remove_attribute('tie')
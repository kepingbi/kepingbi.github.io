import os,sys
import citation

'''
TY  - CPAPER (JOUR, CONF, 'Informal or Other Publication')
ID  - DBLP:conf/sigir/AiYGC16
AU  - Ai, Qingyao
AU  - Yang, Liu
AU  - Guo, Jiafeng
AU  - Croft, W. Bruce
TI  - Improving Language Estimation with the Paragraph Vector Model for Ad-hoc Retrieval.
BT  - Proceedings of the 39th International ACM SIGIR conference on Research and Development in Information Retrieval, SIGIR 2016, Pisa, Italy, July 17-21, 2016
SP  - 869
EP  - 872
PY  - 2016//
DO  - 10.1145/2911451.2914688
UR  - https://doi.org/10.1145/2911451.2914688
ER  -
'''


dblp_url = 'https://dblp.uni-trier.de/pid/169/1808.ris'

# Format publication and output
publications = citation.load_publication_ris_from_dblp(dblp_url)

allow_TY = set(['CPAPER', 'JOUR'])
num = 1
for entry in publications:
	# check publication type
	if not entry['TY'] in allow_TY:
		continue

	# format authors
	authors = []
	if isinstance(entry['AU'], list):
		for au in entry['AU']:
			aname = citation.format_author_first_last_name(au)
			if aname == 'Qingyao Ai':
				aname = '**%s**' %aname
			authors.append(aname)
	else:
		authors.append(citation.format_author_first_last_name(entry['AU']))
	#print(entry)

	# format venue
	venue = entry['BT'] if entry['TY'] == 'CPAPER' else entry['JO']

	output = '.\n'.join([
		str(num) + '. **' + entry['TI']+'**',
		', '.join(authors),
		'In %s' % venue,
		])
	CCF = citation.get_CCF_tag(venue)
	if CCF != None:
		output += ' [CCF %s]' % CCF
	num += 1
	print(output)







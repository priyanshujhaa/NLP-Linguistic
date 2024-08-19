from Components import phonemes, char_to_ph_id
import ast, re

from Components import tokenizer

elements_list = [
			'क', 'का', 'कि', 'की', 'कु', 'कू', 'के', 'कै', 'को', 'कौ', 'कं', 'कः',
			'ख', 'खा', 'खि', 'खी', 'खु', 'खू', 'खे', 'खै', 'खो', 'खौ', 'खं', 'खः',
			'ग', 'गा', 'गि', 'गी', 'गु', 'गू', 'गे', 'गै', 'गो', 'गौ', 'गं', 'गः',
			'घ', 'घा', 'घि', 'घी', 'घु', 'घू', 'घे', 'घै', 'घो', 'घौ', 'घं', 'घः',
			'च', 'चा', 'चि', 'ची', 'चु', 'चू', 'चे', 'चै', 'चो', 'चौ', 'चं', 'चः',
			'छ', 'छा', 'छि', 'छी', 'छु', 'छू', 'छे', 'छै', 'छो', 'छौ', 'छं', 'छः',
			'ज', 'जा', 'जि', 'जी', 'जु', 'जू', 'जे', 'जै', 'जो', 'जौ', 'जं', 'जः',
			'झ', 'झा', 'झि', 'झी', 'झु', 'झू', 'झे', 'झै', 'झो', 'झौ', 'झं', 'झः',
			'ट', 'टा', 'टि', 'टी', 'टु', 'टू', 'टे', 'टै', 'टो', 'टौ', 'टं', 'टः',
			'ठ', 'ठा', 'ठि', 'ठी', 'ठु', 'ठू', 'ठे', 'ठै', 'ठो', 'ठौ', 'ठं', 'ठः',
			'ड', 'डा', 'डि', 'डी', 'डु', 'डू', 'डे', 'डै', 'डो', 'डौ', 'डं', 'डः',
			'ढ', 'ढा', 'ढि', 'ढी', 'ढु', 'ढू', 'ढे', 'ढै', 'ढो', 'ढौ', 'ढं', 'ढः',
			'ण', 'णा', 'णि', 'णी', 'णु', 'णू', 'णे', 'णै', 'णो', 'णौ', 'णं', 'णः',
			'त', 'ता', 'ति', 'ती', 'तु', 'तू', 'ते', 'तै', 'तो', 'तौ', 'तं', 'तः',
			'थ', 'था', 'थि', 'थी', 'थु', 'थू', 'थे', 'थै', 'थो', 'थौ', 'थं', 'थः',
			'द', 'दा', 'दि', 'दी', 'दु', 'दू', 'दे', 'दै', 'दो', 'दौ', 'दं', 'दः',
			'ध', 'धा', 'धि', 'धी', 'धु', 'धू', 'धे', 'धै', 'धो', 'धौ', 'धं', 'धः',
			'न', 'ना', 'नि', 'नी', 'नु', 'नू', 'ने', 'नै', 'नो', 'नौ', 'नं', 'नः',
			'प', 'पा', 'पि', 'पी', 'पु', 'पू', 'पे', 'पै', 'पो', 'पौ', 'पं', 'पः',
			'फ', 'फा', 'फि', 'फी', 'फु', 'फू', 'फे', 'फै', 'फो', 'फौ', 'फं', 'फः',
			'ब', 'बा', 'बि', 'बी', 'बु', 'बू', 'बे', 'बै', 'बो', 'बौ', 'बं', 'बः',
			'भ', 'भा', 'भि', 'भी', 'भु', 'भू', 'भे', 'भै', 'भो', 'भौ', 'भं', 'भः',
			'म', 'मा', 'मि', 'मी', 'मु', 'मू', 'मे', 'मै', 'मो', 'मौ', 'मं', 'मः',
			'य', 'या', 'यि', 'यी', 'यु', 'यू', 'ये', 'यै', 'यो', 'यौ', 'यं', 'यः',
			'र', 'रा', 'रि', 'री', 'रु', 'रू', 'रे', 'रै', 'रो', 'रौ', 'रं', 'रः',
			'ल', 'ला', 'लि', 'ली', 'लु', 'लू', 'ले', 'लै', 'लो', 'लौ', 'लं', 'लः',
			'व', 'वा', 'वि', 'वी', 'वु', 'वू', 'वे', 'वै', 'वो', 'वौ', 'वं', 'वः',
			'श', 'शा', 'शि', 'शी', 'शु', 'शू', 'शे', 'शै', 'शो', 'शौ', 'शं', 'शः',
			'स', 'सा', 'सि', 'सी', 'सु', 'सू', 'से', 'सै', 'सो', 'सौ', 'सं', 'सः',
			'ष', 'षा', 'षि', 'षी', 'षु', 'षू', 'षे', 'षै', 'षो', 'षौ', 'षं', 'षः',
			'ह', 'हा', 'हि', 'ही', 'हु', 'हू', 'हे', 'है', 'हो', 'हौ', 'हं', 'हः',
			'अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ए', 'ऐ', 'ओ', 'औ', 'अं', 'अः',
			'स्त', 'स्ट', 'त्न', 'त्म', 'त्थ', 'त्य', 'त्व', 'क्र', 'ग्र', 'द्र',
			'प्र', 'र्त', 'र्च', 'र्ग', 'र्न', 'र्श', 'म्र', 'म्य', 'स्य', 'ज्य',
			'म्प', 'म्म', 'प्प', 'ल्प', 'ब्द', 'त्थ', 'क्ष', 'श्र', 'म्ह', 'न्थ',
			'न्द', 'न्न', 'म्ब', 'न्ह', 'म्च', 'म्ट', 'म्त', 'म्ब', 'म्य', 'ण्ड',
			'प्त', 'प्प', 'प्ल', 'ब्ज', 'ब्द', 'ब्ब', 'द्ध', 'ख्य', 'ज्य', 'प्य',
			'ल्य', 'भ्य', 'व्य', 'ष्य', 'ब्ल', 'ष्ट'
		]

def phoneme_scan(word):
	# Takes a list which contains syllables of the word

	for syllable in word:
        
		if(str(type(syllable))=='tuple'):
			continue


		# print("Syllable taken:" + str(syllable))
		# print(str(type(syllable)))
		for elem in elements_list:
			if syllable == elem:
			# if re.search("क|का|कि|की|कु|कू|के|कै|को|कौ|कं|कः|ख|खा|खि|खी|खु|खू|खे|खै|खो|खौ|खं|खः|ग|गा|गि|गी|गु|गू|गे|गै|गो|गौ|गं|गः|घ|घा|घि|घी|घु|घू|घे|घै|घो|घौ|घं|घः|च|चा|चि|ची|चु|चू|चे|चै|चो|चौ|चं|चः|छ|छा|छि|छी|छु|छू|छे|छै|छो|छौ|छं|छः|ज|जा|जि|जी|जु|जू|जे|जै|जो|जौ|जं|जः|झ|झा|झि|झी|झु|झू|झे|झै|झो|झौ|झं|झः|ट|टा|टि|टी|टु|टू|टे|टै|टो|टौ|टं|टः|ठ|ठा|ठि|ठी|ठु|ठू|ठे|ठै|ठो|ठौ|ठं|ठः|ड|डा|डि|डी|डु|डू|डे|डै|डो|डौ|डं|डः|ढ|ढा|ढि|ढी|ढु|ढू|ढे|ढै|ढो|ढौ|ढं|ढः|ण|णा|णि|णी|णु|णू|णे|णै|णो|णौ|णं|णः|त|ता|ति|ती|तु|तू|ते|तै|तो|तौ|तं|तः|थ|था|थि|थी|थु|थू|थे|थै|थो|थौ|थं|थः|द|दा|दि|दी|दु|दू|दे|दै|दो|दौ|दं|दः|ध|धा|धि|धी|धु|धू|धे|धै|धो|धौ|धं|धः|न|ना|नि|नी|नु|नू|ने|नै|नो|नौ|नं|नः|प|पा|पि|पी|पु|पू|पे|पै|पो|पौ|पं|पः|फ|फा|फि|फी|फु|फू|फे|फै|फो|फौ|फं|फः|ब|बा|बि|बी|बु|बू|बे|बै|बो|बौ|बं|बः|भ|भा|भि|भी|भु|भू|भे|भै|भो|भौ|भं|भः|म|मा|मि|मी|मु|मू|मे|मै|मो|मौ|मं|मः|य|या|यि|यी|यु|यू|ये|यै|यो|यौ|यं|यः|र|रा|रि|री|रु|रू|रे|रै|रो|रौ|रं|रः|ल|ला|लि|ली|लु|लू|ले|लै|लो|लौ|लं|लः|व|वा|वि|वी|वु|वू|वे|वै|वो|वौ|वं|वः|श|शा|शि|शी|शु|शू|शे|शै|शो|शौ|शं|शः|स|सा|सि|सी|सु|सू|से|सै|सो|सौ|सं|सः|ष|षा|षि|षी|षु|षू|षे|षै|षो|षौ|षं|षः|ह|हा|हि|ही|हु|हू|हे|है|हो|हौ|हं|हः|अ|आ|इ|ई|उ|ऊ|ऋ|ए|ऐ|ओ|औ|अं|अः|स्त|स्ट|त्न|त्म|त्थ|त्य|त्व|क्र|ग्र|द्र|प्र|र्त|र्च|र्ग|र्न|र्श|म्र|म्य|स्य|ज्य|म्प|म्म|प्प|ल्प|ब्द|त्थ|क्ष|श्र|म्ह|न्थ|न्द|न्न|म्ब|न्ह|म्च|म्ट|म्त|म्ब|म्य|ण्ड|प्त|प्प|प्ल|ब्ज|ब्द|ब्ब|द्ध|ख्य|ज्य|प्य|ल्य|भ्य|व्य|ष्य|ब्ल|ष्ट", syllable):
				# print(syllable+"	present in RE and matches	"+match.group(0))
				word = replace_with_phoneme(word, "क", (phonemes.aa,))
				word = replace_with_phoneme(word, "का", (phonemes.ab,))
				word = replace_with_phoneme(word, "कि", (phonemes.ac,))
				word = replace_with_phoneme(word, "की", (phonemes.ad,))
				word = replace_with_phoneme(word, "कु", (phonemes.ae,))
				word = replace_with_phoneme(word, "कू", (phonemes.af,))
				word = replace_with_phoneme(word, "के", (phonemes.ag,))
				word = replace_with_phoneme(word, "कै", (phonemes.ah,))
				word = replace_with_phoneme(word, "को", (phonemes.ai,))
				word = replace_with_phoneme(word, "कौ", (phonemes.aj,))
				word = replace_with_phoneme(word, "कं", (phonemes.ak,))
				word = replace_with_phoneme(word, "कँ", (phonemes.ak,))
				word = replace_with_phoneme(word, "कः", (phonemes.al,))
				word = replace_with_phoneme(word, "ख", (phonemes.am,))
				word = replace_with_phoneme(word, "खा", (phonemes.an,))
				word = replace_with_phoneme(word, "खि", (phonemes.ao,))
				word = replace_with_phoneme(word, "खी", (phonemes.ap,))
				word = replace_with_phoneme(word, "खु", (phonemes.aq,))
				word = replace_with_phoneme(word, "खू", (phonemes.ar,))
				word = replace_with_phoneme(word, "खे", (phonemes.as_,))
				word = replace_with_phoneme(word, "खै", (phonemes.at,))
				word = replace_with_phoneme(word, "खो", (phonemes.au,))
				word = replace_with_phoneme(word, "खौ", (phonemes.av,))
				word = replace_with_phoneme(word, "खं", (phonemes.aw,))
				word = replace_with_phoneme(word, "खँ", (phonemes.aw,))
				word = replace_with_phoneme(word, "खः", (phonemes.ax,))
				word = replace_with_phoneme(word, "ग", (phonemes.ay,))
				word = replace_with_phoneme(word, "गा", (phonemes.az,))
				word = replace_with_phoneme(word, "गि", (phonemes.ba,))
				word = replace_with_phoneme(word, "गी", (phonemes.bb,))
				word = replace_with_phoneme(word, "गु", (phonemes.bc,))
				word = replace_with_phoneme(word, "गू", (phonemes.bd,))
				word = replace_with_phoneme(word, "गे", (phonemes.be,))
				word = replace_with_phoneme(word, "गै", (phonemes.bf,))
				word = replace_with_phoneme(word, "गो", (phonemes.bg,))
				word = replace_with_phoneme(word, "गौ", (phonemes.bh,))
				word = replace_with_phoneme(word, "गं", (phonemes.bi,))
				word = replace_with_phoneme(word, "गँ", (phonemes.bi,))
				word = replace_with_phoneme(word, "गः", (phonemes.bj,))
				word = replace_with_phoneme(word, "घ", (phonemes.bk,))
				word = replace_with_phoneme(word, "घा", (phonemes.bl,))
				word = replace_with_phoneme(word, "घि", (phonemes.bm,))
				word = replace_with_phoneme(word, "घी", (phonemes.bn,))
				word = replace_with_phoneme(word, "घु", (phonemes.bo,))
				word = replace_with_phoneme(word, "घू", (phonemes.bp,))
				word = replace_with_phoneme(word, "घे", (phonemes.bq,))
				word = replace_with_phoneme(word, "घै", (phonemes.br,))
				word = replace_with_phoneme(word, "घो", (phonemes.bs,))
				word = replace_with_phoneme(word, "घौ", (phonemes.bt,))
				word = replace_with_phoneme(word, "घं", (phonemes.bu,))
				word = replace_with_phoneme(word, "घँ", (phonemes.bu,))
				word = replace_with_phoneme(word, "घः", (phonemes.bv,))
				word = replace_with_phoneme(word, "च", (phonemes.bw,)) # here is cha ch
				word = replace_with_phoneme(word, "चा", (phonemes.bx,))
				word = replace_with_phoneme(word, "चि", (phonemes.by,))
				word = replace_with_phoneme(word, "ची", (phonemes.bz,))
				word = replace_with_phoneme(word, "चु", (phonemes.ca,))
				word = replace_with_phoneme(word, "चू", (phonemes.cb,))
				word = replace_with_phoneme(word, "चे", (phonemes.cc,))
				word = replace_with_phoneme(word, "चै", (phonemes.cd,))
				word = replace_with_phoneme(word, "चो", (phonemes.ce,))
				word = replace_with_phoneme(word, "चौ", (phonemes.cf,))
				word = replace_with_phoneme(word, "चं", (phonemes.cg,))
				word = replace_with_phoneme(word, "चँ", (phonemes.cg,))
				word = replace_with_phoneme(word, "चः", (phonemes.ch,))
				word = replace_with_phoneme(word, "छ", (phonemes.ci,))
				word = replace_with_phoneme(word, "छा", (phonemes.cj,))
				word = replace_with_phoneme(word, "छि", (phonemes.ck,))
				word = replace_with_phoneme(word, "छी", (phonemes.cl,))
				word = replace_with_phoneme(word, "छु", (phonemes.cm,))
				word = replace_with_phoneme(word, "छू", (phonemes.cn,))
				word = replace_with_phoneme(word, "छे", (phonemes.co,))
				word = replace_with_phoneme(word, "छै", (phonemes.cp,))
				word = replace_with_phoneme(word, "छो", (phonemes.cq,))
				word = replace_with_phoneme(word, "छौ", (phonemes.cr,))
				word = replace_with_phoneme(word, "छं", (phonemes.cs,))
				word = replace_with_phoneme(word, "छँ", (phonemes.cs,))
				word = replace_with_phoneme(word, "छः", (phonemes.ct,))
				word = replace_with_phoneme(word, "ज", (phonemes.cu,))
				word = replace_with_phoneme(word, "जा", (phonemes.cv,))
				word = replace_with_phoneme(word, "जि", (phonemes.cw,))
				word = replace_with_phoneme(word, "जी", (phonemes.cx,))
				word = replace_with_phoneme(word, "जु", (phonemes.cy,))
				word = replace_with_phoneme(word, "जू", (phonemes.cz,))
				word = replace_with_phoneme(word, "जे", (phonemes.da,))
				word = replace_with_phoneme(word, "जै", (phonemes.db,))
				word = replace_with_phoneme(word, "जो", (phonemes.dc,))
				word = replace_with_phoneme(word, "जौ", (phonemes.dd,))
				word = replace_with_phoneme(word, "जं", (phonemes.de,))
				word = replace_with_phoneme(word, "जँ", (phonemes.de,))
				word = replace_with_phoneme(word, "जः", (phonemes.df,))
				word = replace_with_phoneme(word, "झ", (phonemes.dg,))
				word = replace_with_phoneme(word, "झा", (phonemes.dh,))
				word = replace_with_phoneme(word, "झि", (phonemes.di,))
				word = replace_with_phoneme(word, "झी", (phonemes.dj,))
				word = replace_with_phoneme(word, "झु", (phonemes.dk,))
				word = replace_with_phoneme(word, "झू", (phonemes.dl,))
				word = replace_with_phoneme(word, "झे", (phonemes.dm,))
				word = replace_with_phoneme(word, "झै", (phonemes.dn,))
				word = replace_with_phoneme(word, "झो", (phonemes.do,))
				word = replace_with_phoneme(word, "झौ", (phonemes.dp,))
				word = replace_with_phoneme(word, "झं", (phonemes.dq,))
				word = replace_with_phoneme(word, "झँ", (phonemes.dq,))
				word = replace_with_phoneme(word, "झः", (phonemes.dr,))
				word = replace_with_phoneme(word, "ट", (phonemes.ds,))
				word = replace_with_phoneme(word, "टा", (phonemes.dt,))
				word = replace_with_phoneme(word, "टि", (phonemes.du,))
				word = replace_with_phoneme(word, "टी", (phonemes.dv,))
				word = replace_with_phoneme(word, "टु", (phonemes.dw,))
				word = replace_with_phoneme(word, "टू", (phonemes.dx,))
				word = replace_with_phoneme(word, "टे", (phonemes.dy,))
				word = replace_with_phoneme(word, "टै", (phonemes.dz,))
				word = replace_with_phoneme(word, "टो", (phonemes.ea,))
				word = replace_with_phoneme(word, "टौ", (phonemes.eb,))
				word = replace_with_phoneme(word, "टं", (phonemes.ec,))
				word = replace_with_phoneme(word, "टँ", (phonemes.ec,))
				word = replace_with_phoneme(word, "टः", (phonemes.ed,))
				word = replace_with_phoneme(word, "ठ", (phonemes.ee,))
				word = replace_with_phoneme(word, "ठा", (phonemes.ef,))
				word = replace_with_phoneme(word, "ठि", (phonemes.eg,))
				word = replace_with_phoneme(word, "ठी", (phonemes.eh,))
				word = replace_with_phoneme(word, "ठु", (phonemes.ei,))
				word = replace_with_phoneme(word, "ठू", (phonemes.ej,))
				word = replace_with_phoneme(word, "ठे", (phonemes.ek,))
				word = replace_with_phoneme(word, "ठै", (phonemes.el,))
				word = replace_with_phoneme(word, "ठो", (phonemes.em,))
				word = replace_with_phoneme(word, "ठौ", (phonemes.en,))
				word = replace_with_phoneme(word, "ठं", (phonemes.eo,))
				word = replace_with_phoneme(word, "ठँ", (phonemes.eo,))
				word = replace_with_phoneme(word, "ठः", (phonemes.ep,))
				word = replace_with_phoneme(word, "ड", (phonemes.eq,))
				word = replace_with_phoneme(word, "ड़", (phonemes.eq,))
				word = replace_with_phoneme(word, "डा", (phonemes.er,))
				word = replace_with_phoneme(word, "डि", (phonemes.es,))
				word = replace_with_phoneme(word, "डी", (phonemes.et,))
				word = replace_with_phoneme(word, "डु", (phonemes.eu,))
				word = replace_with_phoneme(word, "डू", (phonemes.ev,))
				word = replace_with_phoneme(word, "डे", (phonemes.ew,))
				word = replace_with_phoneme(word, "डै", (phonemes.ex,))
				word = replace_with_phoneme(word, "डो", (phonemes.ey,))
				word = replace_with_phoneme(word, "डौ", (phonemes.ez,))
				word = replace_with_phoneme(word, "डं", (phonemes.fa,))
				word = replace_with_phoneme(word, "डँ", (phonemes.fa,))
				word = replace_with_phoneme(word, "ङँ", (phonemes.fa,))
				word = replace_with_phoneme(word, "डः", (phonemes.fb,))
				word = replace_with_phoneme(word, "ढ", (phonemes.fc,))
				word = replace_with_phoneme(word, "ढा", (phonemes.fd,))
				word = replace_with_phoneme(word, "ढि", (phonemes.fe,))
				word = replace_with_phoneme(word, "ढी", (phonemes.ff,))
				word = replace_with_phoneme(word, "ढु", (phonemes.fg,))
				word = replace_with_phoneme(word, "ढू", (phonemes.fh,))
				word = replace_with_phoneme(word, "ढे", (phonemes.fi,))
				word = replace_with_phoneme(word, "ढै", (phonemes.fj,))
				word = replace_with_phoneme(word, "ढो", (phonemes.fk,))
				word = replace_with_phoneme(word, "ढौ", (phonemes.fl,))
				word = replace_with_phoneme(word, "ढं", (phonemes.fm,))
				word = replace_with_phoneme(word, "ढँ", (phonemes.fm,))
				word = replace_with_phoneme(word, "ढः", (phonemes.fn,))
				word = replace_with_phoneme(word, "ण", (phonemes.fo,))
				word = replace_with_phoneme(word, "णा", (phonemes.fp,))
				word = replace_with_phoneme(word, "णि", (phonemes.fq,))
				word = replace_with_phoneme(word, "णी", (phonemes.fr,))
				word = replace_with_phoneme(word, "णु", (phonemes.fs,))
				word = replace_with_phoneme(word, "णू", (phonemes.ft,))
				word = replace_with_phoneme(word, "णे", (phonemes.fu,))
				word = replace_with_phoneme(word, "णै", (phonemes.fv,))
				word = replace_with_phoneme(word, "णो", (phonemes.fw,))
				word = replace_with_phoneme(word, "णौ", (phonemes.fx,))
				word = replace_with_phoneme(word, "णं", (phonemes.fy,))
				word = replace_with_phoneme(word, "णँ", (phonemes.fy,))
				word = replace_with_phoneme(word, "णः", (phonemes.fz,))
				word = replace_with_phoneme(word, "त", (phonemes.ga,))
				word = replace_with_phoneme(word, "ता", (phonemes.gb,))
				word = replace_with_phoneme(word, "ति", (phonemes.gc,))
				word = replace_with_phoneme(word, "ती", (phonemes.gd,))
				word = replace_with_phoneme(word, "तु", (phonemes.ge,))
				word = replace_with_phoneme(word, "तू", (phonemes.gf,))
				word = replace_with_phoneme(word, "ते", (phonemes.gg,))
				word = replace_with_phoneme(word, "तै", (phonemes.gh,))
				word = replace_with_phoneme(word, "तो", (phonemes.gi,))
				word = replace_with_phoneme(word, "तौ", (phonemes.gj,))
				word = replace_with_phoneme(word, "तं", (phonemes.gk,))
				word = replace_with_phoneme(word, "तँ", (phonemes.gk,))
				word = replace_with_phoneme(word, "तः", (phonemes.gl,))
				word = replace_with_phoneme(word, "थ", (phonemes.gm,))
				word = replace_with_phoneme(word, "था", (phonemes.gn,))
				word = replace_with_phoneme(word, "थि", (phonemes.go,))
				word = replace_with_phoneme(word, "थी", (phonemes.gp,))
				word = replace_with_phoneme(word, "थु", (phonemes.gq,))
				word = replace_with_phoneme(word, "थू", (phonemes.gr,))
				word = replace_with_phoneme(word, "थे", (phonemes.gs,))
				word = replace_with_phoneme(word, "थै", (phonemes.gt,))
				word = replace_with_phoneme(word, "थो", (phonemes.gu,))
				word = replace_with_phoneme(word, "थौ", (phonemes.gv,))
				word = replace_with_phoneme(word, "थं", (phonemes.gw,))
				word = replace_with_phoneme(word, "थँ", (phonemes.gw,))
				word = replace_with_phoneme(word, "थः", (phonemes.gx,))
				word = replace_with_phoneme(word, "द", (phonemes.gy,))
				word = replace_with_phoneme(word, "दा", (phonemes.gz,))
				word = replace_with_phoneme(word, "दि", (phonemes.ha,))
				word = replace_with_phoneme(word, "दी", (phonemes.hb,))
				word = replace_with_phoneme(word, "दु", (phonemes.hc,))	# here id dah da d
				word = replace_with_phoneme(word, "दू", (phonemes.hd,))
				word = replace_with_phoneme(word, "दे", (phonemes.he,))
				word = replace_with_phoneme(word, "दै", (phonemes.hf,))
				word = replace_with_phoneme(word, "दो", (phonemes.hg,))
				word = replace_with_phoneme(word, "दौ", (phonemes.hh,))
				word = replace_with_phoneme(word, "दं", (phonemes.hi,))
				word = replace_with_phoneme(word, "दँ", (phonemes.hi,))
				word = replace_with_phoneme(word, "दः", (phonemes.hj,))
				word = replace_with_phoneme(word, "ध", (phonemes.hk,))
				word = replace_with_phoneme(word, "धा", (phonemes.hl,))
				word = replace_with_phoneme(word, "धि", (phonemes.hm,))
				word = replace_with_phoneme(word, "धी", (phonemes.hn,))
				word = replace_with_phoneme(word, "धु", (phonemes.ho,))
				word = replace_with_phoneme(word, "धू", (phonemes.hp,))
				word = replace_with_phoneme(word, "धे", (phonemes.hq,))
				word = replace_with_phoneme(word, "धै", (phonemes.hr,))
				word = replace_with_phoneme(word, "धो", (phonemes.hs,))
				word = replace_with_phoneme(word, "धौ", (phonemes.ht,))
				word = replace_with_phoneme(word, "धं", (phonemes.hu,))
				word = replace_with_phoneme(word, "धँ", (phonemes.hu,))
				word = replace_with_phoneme(word, "धः", (phonemes.hv,))
				word = replace_with_phoneme(word, "न", (phonemes.hw,))
				word = replace_with_phoneme(word, "ना", (phonemes.hx,))
				word = replace_with_phoneme(word, "नि", (phonemes.hy,))
				word = replace_with_phoneme(word, "नी", (phonemes.hz,))
				word = replace_with_phoneme(word, "नु", (phonemes.ia,))
				word = replace_with_phoneme(word, "नू", (phonemes.ib,))
				word = replace_with_phoneme(word, "ने", (phonemes.ic,))
				word = replace_with_phoneme(word, "नै", (phonemes.id,))
				word = replace_with_phoneme(word, "नो", (phonemes.ie,))
				word = replace_with_phoneme(word, "नौ", (phonemes.if_,))
				word = replace_with_phoneme(word, "नं", (phonemes.ig,))
				word = replace_with_phoneme(word, "नँ", (phonemes.ig,))
				word = replace_with_phoneme(word, "नः", (phonemes.ih,))
				word = replace_with_phoneme(word, "प", (phonemes.ii,)) # here is P pa
				word = replace_with_phoneme(word, "पा", (phonemes.ij,))
				word = replace_with_phoneme(word, "पि", (phonemes.ik,))
				word = replace_with_phoneme(word, "पी", (phonemes.il,))
				word = replace_with_phoneme(word, "पु", (phonemes.im,))
				word = replace_with_phoneme(word, "पू", (phonemes.in_,))
				word = replace_with_phoneme(word, "पे", (phonemes.io,))
				word = replace_with_phoneme(word, "पै", (phonemes.ip,))
				word = replace_with_phoneme(word, "पो", (phonemes.iq,))
				word = replace_with_phoneme(word, "पौ", (phonemes.ir,))
				word = replace_with_phoneme(word, "पं", (phonemes.is_,))
				word = replace_with_phoneme(word, "पँ", (phonemes.is_,))
				word = replace_with_phoneme(word, "पः", (phonemes.it,))
				word = replace_with_phoneme(word, "फ", (phonemes.iu,))
				word = replace_with_phoneme(word, "फा", (phonemes.iv,))
				word = replace_with_phoneme(word, "फि", (phonemes.iw,))
				word = replace_with_phoneme(word, "फी", (phonemes.ix,))
				word = replace_with_phoneme(word, "फु", (phonemes.iy,))
				word = replace_with_phoneme(word, "फू", (phonemes.iz,))
				word = replace_with_phoneme(word, "फे", (phonemes.ja,))
				word = replace_with_phoneme(word, "फै", (phonemes.jb,))
				word = replace_with_phoneme(word, "फो", (phonemes.jc,))
				word = replace_with_phoneme(word, "फौ", (phonemes.jd,))
				word = replace_with_phoneme(word, "फं", (phonemes.je,))
				word = replace_with_phoneme(word, "फँ", (phonemes.je,))
				word = replace_with_phoneme(word, "फः", (phonemes.jf,))
				word = replace_with_phoneme(word, "ब", (phonemes.jg,))
				word = replace_with_phoneme(word, "बा", (phonemes.jh,))
				word = replace_with_phoneme(word, "बि", (phonemes.ji,))
				word = replace_with_phoneme(word, "बी", (phonemes.jj,))
				word = replace_with_phoneme(word, "बु", (phonemes.jk,))
				word = replace_with_phoneme(word, "बू", (phonemes.jl,))
				word = replace_with_phoneme(word, "बे", (phonemes.jm,))
				word = replace_with_phoneme(word, "बै", (phonemes.jn,))
				word = replace_with_phoneme(word, "बो", (phonemes.jo,))
				word = replace_with_phoneme(word, "बौ", (phonemes.jp,))
				word = replace_with_phoneme(word, "बं", (phonemes.jq,))
				word = replace_with_phoneme(word, "बँ", (phonemes.jq,))
				word = replace_with_phoneme(word, "बः", (phonemes.jr,))
				word = replace_with_phoneme(word, "भ", (phonemes.js,))
				word = replace_with_phoneme(word, "भा", (phonemes.jt,))
				word = replace_with_phoneme(word, "भि", (phonemes.ju,))
				word = replace_with_phoneme(word, "भी", (phonemes.jv,))
				word = replace_with_phoneme(word, "भु", (phonemes.jw,))
				word = replace_with_phoneme(word, "भू", (phonemes.jx,))
				word = replace_with_phoneme(word, "भे", (phonemes.jy,))
				word = replace_with_phoneme(word, "भौ", (phonemes.jz,))
				word = replace_with_phoneme(word, "भो", (phonemes.ka,))
				word = replace_with_phoneme(word, "भौ", (phonemes.kb,))
				word = replace_with_phoneme(word, "भं", (phonemes.kc,))
				word = replace_with_phoneme(word, "भँ", (phonemes.kc,))
				word = replace_with_phoneme(word, "भः", (phonemes.kd,))
				word = replace_with_phoneme(word, "म", (phonemes.ke,))
				word = replace_with_phoneme(word, "मा", (phonemes.kf,))
				word = replace_with_phoneme(word, "मि", (phonemes.kg,))
				word = replace_with_phoneme(word, "मी", (phonemes.kh,))
				word = replace_with_phoneme(word, "मु", (phonemes.ki,))
				word = replace_with_phoneme(word, "मू", (phonemes.kj,))
				word = replace_with_phoneme(word, "मे", (phonemes.kk,))
				word = replace_with_phoneme(word, "मै", (phonemes.kl,))
				word = replace_with_phoneme(word, "मो", (phonemes.km,))
				word = replace_with_phoneme(word, "मौ", (phonemes.kn,))
				word = replace_with_phoneme(word, "मं", (phonemes.ko,))
				word = replace_with_phoneme(word, "मँ", (phonemes.ko,))
				word = replace_with_phoneme(word, "मः", (phonemes.kp,))
				word = replace_with_phoneme(word, "य", (phonemes.kq,))
				word = replace_with_phoneme(word, "या", (phonemes.kr,))
				word = replace_with_phoneme(word, "यि", (phonemes.ks,))
				word = replace_with_phoneme(word, "यी", (phonemes.kt,))
				word = replace_with_phoneme(word, "यु", (phonemes.ku,))
				word = replace_with_phoneme(word, "यू", (phonemes.kv,))
				word = replace_with_phoneme(word, "ये", (phonemes.kw,))
				word = replace_with_phoneme(word, "यै", (phonemes.kx,))
				word = replace_with_phoneme(word, "यो", (phonemes.ky,))
				word = replace_with_phoneme(word, "यौ", (phonemes.kz,))
				word = replace_with_phoneme(word, "यं", (phonemes.la,))
				word = replace_with_phoneme(word, "यँ", (phonemes.la,))
				word = replace_with_phoneme(word, "यः", (phonemes.lb,))
				word = replace_with_phoneme(word, "र", (phonemes.lc,))
				word = replace_with_phoneme(word, "रा", (phonemes.ld,))
				word = replace_with_phoneme(word, "रि", (phonemes.le,))
				word = replace_with_phoneme(word, "री", (phonemes.lf,))
				word = replace_with_phoneme(word, "रु", (phonemes.lg,))
				word = replace_with_phoneme(word, "रू", (phonemes.lh,))
				word = replace_with_phoneme(word, "रे", (phonemes.li,))
				word = replace_with_phoneme(word, "रै", (phonemes.lj,))
				word = replace_with_phoneme(word, "रो", (phonemes.lk,))
				word = replace_with_phoneme(word, "रौ", (phonemes.ll,))
				word = replace_with_phoneme(word, "रं", (phonemes.lm,))
				word = replace_with_phoneme(word, "रँ", (phonemes.lm,))
				word = replace_with_phoneme(word, "रः", (phonemes.ln,))
				word = replace_with_phoneme(word, "ल", (phonemes.lo,))
				word = replace_with_phoneme(word, "ला", (phonemes.lp,))
				word = replace_with_phoneme(word, "लि", (phonemes.lq,))
				word = replace_with_phoneme(word, "ली", (phonemes.lr,))
				word = replace_with_phoneme(word, "लु", (phonemes.ls,))
				word = replace_with_phoneme(word, "लू", (phonemes.lt,))
				word = replace_with_phoneme(word, "ले", (phonemes.lu,))
				word = replace_with_phoneme(word, "लै", (phonemes.lv,))
				word = replace_with_phoneme(word, "लो", (phonemes.lw,))
				word = replace_with_phoneme(word, "लौ", (phonemes.lx,))
				word = replace_with_phoneme(word, "लं", (phonemes.ly,))
				word = replace_with_phoneme(word, "लँ", (phonemes.ly,))
				word = replace_with_phoneme(word, "लः", (phonemes.lz,))
				word = replace_with_phoneme(word, "व", (phonemes.ma,))
				word = replace_with_phoneme(word, "वा", (phonemes.mb,))
				word = replace_with_phoneme(word, "वि", (phonemes.mc,))
				word = replace_with_phoneme(word, "वी", (phonemes.md,))
				word = replace_with_phoneme(word, "वु", (phonemes.me,))
				word = replace_with_phoneme(word, "वू", (phonemes.mf,))
				word = replace_with_phoneme(word, "वे", (phonemes.mg,))
				word = replace_with_phoneme(word, "वै", (phonemes.mh,))
				word = replace_with_phoneme(word, "वो", (phonemes.mi,))
				word = replace_with_phoneme(word, "वौ", (phonemes.mj,))
				word = replace_with_phoneme(word, "वं", (phonemes.mk,))
				word = replace_with_phoneme(word, "वँ", (phonemes.mk,))
				word = replace_with_phoneme(word, "वः", (phonemes.ml,))
				word = replace_with_phoneme(word, "श", (phonemes.mm,))
				word = replace_with_phoneme(word, "शा", (phonemes.mn,))
				word = replace_with_phoneme(word, "शि", (phonemes.mo,))
				word = replace_with_phoneme(word, "शी", (phonemes.mp,))
				word = replace_with_phoneme(word, "शु", (phonemes.mq,))
				word = replace_with_phoneme(word, "शू", (phonemes.mr,))
				word = replace_with_phoneme(word, "शे", (phonemes.ms,))
				word = replace_with_phoneme(word, "शै", (phonemes.mt,))
				word = replace_with_phoneme(word, "शो", (phonemes.mu,))
				word = replace_with_phoneme(word, "शौ", (phonemes.mv,))
				word = replace_with_phoneme(word, "शं", (phonemes.mw,))
				word = replace_with_phoneme(word, "शँ", (phonemes.mw,))
				word = replace_with_phoneme(word, "शः", (phonemes.mx,))
				word = replace_with_phoneme(word, "स", (phonemes.my,))
				word = replace_with_phoneme(word, "सा", (phonemes.mz,))
				word = replace_with_phoneme(word, "सि", (phonemes.na,))
				word = replace_with_phoneme(word, "सी", (phonemes.nb,))
				word = replace_with_phoneme(word, "सु", (phonemes.nc,))
				word = replace_with_phoneme(word, "सू", (phonemes.nd,))
				word = replace_with_phoneme(word, "से", (phonemes.ne,))
				word = replace_with_phoneme(word, "सै", (phonemes.nf,))
				word = replace_with_phoneme(word, "सो", (phonemes.ng,))
				word = replace_with_phoneme(word, "सौ", (phonemes.nh,))
				word = replace_with_phoneme(word, "सं", (phonemes.ni,))
				word = replace_with_phoneme(word, "सँ", (phonemes.ni,))
				word = replace_with_phoneme(word, "सः", (phonemes.nj,))
				word = replace_with_phoneme(word, "ष", (phonemes.nk,))
				word = replace_with_phoneme(word, "षा", (phonemes.nl,))
				word = replace_with_phoneme(word, "षि", (phonemes.nm,))
				word = replace_with_phoneme(word, "षी", (phonemes.nn,))
				word = replace_with_phoneme(word, "षु", (phonemes.no,))
				word = replace_with_phoneme(word, "षू", (phonemes.np,))
				word = replace_with_phoneme(word, "षे", (phonemes.nq,))
				word = replace_with_phoneme(word, "षै", (phonemes.nr,))
				word = replace_with_phoneme(word, "षो", (phonemes.ns,))
				word = replace_with_phoneme(word, "षौ", (phonemes.nt,))
				word = replace_with_phoneme(word, "षं", (phonemes.nu,))
				word = replace_with_phoneme(word, "षँ", (phonemes.nu,))
				word = replace_with_phoneme(word, "षः", (phonemes.nv,))
				word = replace_with_phoneme(word, "ह", (phonemes.nw,))
				word = replace_with_phoneme(word, "हा", (phonemes.nx,))
				word = replace_with_phoneme(word, "हि", (phonemes.ny,))
				word = replace_with_phoneme(word, "ही", (phonemes.nz,))
				word = replace_with_phoneme(word, "हु", (phonemes.oa,))
				word = replace_with_phoneme(word, "हू", (phonemes.ob,))
				word = replace_with_phoneme(word, "हे", (phonemes.oc,))
				word = replace_with_phoneme(word, "है", (phonemes.od,))
				word = replace_with_phoneme(word, "हो", (phonemes.oe,))
				word = replace_with_phoneme(word, "हौ", (phonemes.of,))
				word = replace_with_phoneme(word, "हं", (phonemes.og,))
				word = replace_with_phoneme(word, "हँ", (phonemes.og,))
				word = replace_with_phoneme(word, "हः", (phonemes.oh,))
				word = replace_with_phoneme(word, "अ", (phonemes.oi,))
				word = replace_with_phoneme(word, "आ", (phonemes.oj,))
				word = replace_with_phoneme(word, "इ", (phonemes.ok,))
				word = replace_with_phoneme(word, "ई", (phonemes.ol,))
				word = replace_with_phoneme(word, "उ", (phonemes.om,))
				word = replace_with_phoneme(word, "ऊ", (phonemes.on,))
				word = replace_with_phoneme(word, "ऋ", (phonemes.oo,))
				word = replace_with_phoneme(word, "ए", (phonemes.op,))
				word = replace_with_phoneme(word, "ऐ", (phonemes.oq,))
				word = replace_with_phoneme(word, "ओ", (phonemes.or_,))
				word = replace_with_phoneme(word, "औ", (phonemes.os,))
				word = replace_with_phoneme(word, "अं", (phonemes.ot,))
				word = replace_with_phoneme(word, "अः", (phonemes.ou,))
				word = replace_with_phoneme(word, "स्त", (phonemes.ov,))
				word = replace_with_phoneme(word, "स्ट", (phonemes.ow,))
				word = replace_with_phoneme(word, "त्न", (phonemes.ox,))
				word = replace_with_phoneme(word, "त्म", (phonemes.oy,))
				word = replace_with_phoneme(word, "त्थ", (phonemes.oz,))
				word = replace_with_phoneme(word, "त्य", (phonemes.pa,))
				word = replace_with_phoneme(word, "त्व", (phonemes.pb,))
				word = replace_with_phoneme(word, "क्र", (phonemes.pc,))
				word = replace_with_phoneme(word, "ग्र", (phonemes.pd,))
				word = replace_with_phoneme(word, "द्र", (phonemes.pe,))
				word = replace_with_phoneme(word, "प्र", (phonemes.pf,))
				word = replace_with_phoneme(word, "र्त", (phonemes.pg,))
				word = replace_with_phoneme(word, "र्च", (phonemes.ph,))
				word = replace_with_phoneme(word, "र्ग", (phonemes.pi,))
				word = replace_with_phoneme(word, "र्न", (phonemes.pj,))
				word = replace_with_phoneme(word, "र्श", (phonemes.pk,))
				word = replace_with_phoneme(word, "म्र", (phonemes.pl,))
				word = replace_with_phoneme(word, "म्य", (phonemes.pm,))
				word = replace_with_phoneme(word, "स्य", (phonemes.pn,))
				word = replace_with_phoneme(word, "ज्य", (phonemes.po,))
				word = replace_with_phoneme(word, "म्प", (phonemes.pp,))
				word = replace_with_phoneme(word, "म्म", (phonemes.pq,))
				word = replace_with_phoneme(word, "प्प", (phonemes.pr,))
				word = replace_with_phoneme(word, "ल्प", (phonemes.ps,))
				word = replace_with_phoneme(word, "ब्द", (phonemes.pt,))
				word = replace_with_phoneme(word, "त्थ", (phonemes.pu,))
				word = replace_with_phoneme(word, "क्ष", (phonemes.pv,))
				word = replace_with_phoneme(word, "श्र", (phonemes.pw,))
				word = replace_with_phoneme(word, "म्ह", (phonemes.px,))
				word = replace_with_phoneme(word, "न्थ", (phonemes.py,))
				word = replace_with_phoneme(word, "न्द", (phonemes.pz,))
				word = replace_with_phoneme(word, "न्न", (phonemes.qa,))
				word = replace_with_phoneme(word, "म्ब", (phonemes.qb,))
				word = replace_with_phoneme(word, "न्ह", (phonemes.qc,))
				word = replace_with_phoneme(word, "म्च", (phonemes.qd,))
				word = replace_with_phoneme(word, "म्ट", (phonemes.qe,))
				word = replace_with_phoneme(word, "म्त", (phonemes.qf,))
				word = replace_with_phoneme(word, "म्ब", (phonemes.qg,))
				word = replace_with_phoneme(word, "म्य", (phonemes.qh,))
				word = replace_with_phoneme(word, "ण्ड", (phonemes.qi,))
				word = replace_with_phoneme(word, "प्त", (phonemes.qj,))
				word = replace_with_phoneme(word, "प्प", (phonemes.qk,))
				word = replace_with_phoneme(word, "प्ल", (phonemes.ql,))
				word = replace_with_phoneme(word, "ब्ज", (phonemes.qm,))
				word = replace_with_phoneme(word, "ब्द", (phonemes.qn,))
				word = replace_with_phoneme(word, "ब्ब", (phonemes.qo,))
				word = replace_with_phoneme(word, "द्ध", (phonemes.qp,))
				word = replace_with_phoneme(word, "ख्य", (phonemes.qq,))
				word = replace_with_phoneme(word, "ज्य", (phonemes.qr,))
				word = replace_with_phoneme(word, "प्य", (phonemes.qs,))
				word = replace_with_phoneme(word, "ल्य", (phonemes.qt,))
				word = replace_with_phoneme(word, "भ्य", (phonemes.qu,))
				word = replace_with_phoneme(word, "व्य", (phonemes.qv,))
				word = replace_with_phoneme(word, "ष्य", (phonemes.qw,))
				word = replace_with_phoneme(word, "ब्ल", (phonemes.qx,))
				word = replace_with_phoneme(word, "ष्ट", (phonemes.qy,))
				word = replace_with_phoneme(word, "हाँ", (phonemes.qz,))
				word = replace_with_phoneme(word, "यां", (phonemes.ra,))
				word = replace_with_phoneme(word, "हूँ", (phonemes.rb,))
				word = replace_with_phoneme(word, "प्रि", (phonemes.rc,))
				word = replace_with_phoneme(word, "न्म", (phonemes.rd,))
	return word

				# print("Did not go in IF condition")

def replace_with_phoneme(word, element, phoneme_id):
	# print("replace_with_phoneme me word:	"+ word)
	if element in word:
		index = word.index(element)
		# print("replacing "+element+" with "+phoneme_id)
		word[index] = phoneme_id
	return word

def exception_handler(syllable):
    result = []

    if isinstance(syllable, tuple):
        return syllable
    
    virama_index = syllable.find('्')

    if virama_index != -1:
        result.append(syllable[:virama_index])
        syllable = syllable[virama_index+1:]

    while syllable:
        for i in range(len(syllable), 0, -1):
            if syllable[:i] in elements_list:
                result.append(syllable[:i])
                syllable = syllable[i:]
                break
        else:
            return syllable
    return result
"""
Example sentences to test spaCy and its language models.

>>> from spacy_och.examples import sentences
>>> docs = nlp.pipe(sentences)
"""


sentences = [
    "子曰：「上下无常，非為邪也。進退无恆，非離群也。君子進德脩業、欲及時也，故无咎。」",
    "北冥有魚，其名為鯤。鯤之大，不知其幾千里也。化而為鳥，其名為鵬。",
    "仲子生而有文在其手，曰為魯夫人，故仲子歸于我。",
]


#Transcriptions -- all data below manually input; data taken from BaxterSagartOCbyMandarinMC2014-09-20.pdf
#for characters not in said file (鯤, 鵬), a reading from a rebus character with matching Middle Chinese and matching phonetic component is provided
##Note: character boundary marked by whitespace; same punctuation as above (added whitespace before and after punctuation marks).

##Middle Chinese transcription
sentences_MCtranscr = [
    "tsiX hjwot ： 「 dzyangH haeX mju dzyang ， pj+j hjwe zjae yaeX 。 tsinH thwojH mju hong ， pj+j lje gjun yaeX 。 kjun tsiX tsinH tok sjuw ngjaep 、 yowk gip dzyi yaeX ， kuH mju gjuwX 。 」",
    "pok meng hjuwX ngjo ， gi mjieng hjwe kwon 。 kwon tsyi dajH ， pjuw trje gi kj+jX tshen liX yaeX 。 xwaeH nyi hjwe tewX ， gi mjieng hjwe bong 。",
    "drjuwngH tsiX srjaeng nyi hjuwX mjun dzojX gi syuwX ， hjwot hjwe luX pju nyin ， kuH drjuwngH tsiX kjw+j hju ngaX 。",
]
    
## Old Chinese transcription
##Note: asterisk to mark reconstruction omitted
sentences_OCtranscr = [
    "tsəʔ [ɢ]ʷat  ： 「 daŋʔ-s gˤraʔ ma [d]aŋ ， pəj ɢʷ(r)aj sə.ɢA lAjʔ 。 [ts][i][n]-s n̥ˤ[u]p-s ma [g]ˤəŋ ， pəj [r]aj [g]ur lAjʔ 。 C.qur tsəʔ [ts][i][n]-s tˤək s-liw [m-qʰ](r)[a]p 、 ɢ(r)ok [m-k-]rəp [d]ə lAjʔ ， kˤa(ʔ)-s ma [g](r)uʔ 。 」" ,
    "pˤək mˤeŋ [ɢ]ʷəʔ [r.ŋ]a ， gə C.meŋ ɢʷ(r)aj [k]ˤu[n] 。 [k]ˤu[n] tə lˤa[t]-s ， pə tre gə kәjʔ s.n̥ˤi[ŋ] (mә.)rəʔ lAjʔ 。 qʷʰˤ<r>aj-s nə ɢʷ(r)aj tˤiwʔ ， gə C.meŋ ɢʷ(r)aj [b]ˤəŋ 。",
    "N-truŋ-s tsəʔ sreŋ nə [ɢ]ʷəʔ mə[n] [dz]ˤəʔ gə n̥uʔ ， [ɢ]ʷat ɢʷ(r)aj r.ŋˤaʔ p(r)a ni[ŋ] ， kˤa(ʔ)-s N-truŋ-s tsəʔ [k]ʷәj ɢʷ(r)a ŋˤajʔ 。",
]

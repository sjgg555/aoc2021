test_data = [[["be", "cfbegad", "cbdgef", "fgaecd", "cgeb", "fdcge", "agebfd", "fecdb", "fabcd", "edb"], ["fdgacbe", "cefdb", "cefbgd", "gcbe"]],
[["edbfga", "begcd", "cbg", "gc", "gcadebf", "fbgde", "acbgfd", "abcde", "gfcbed", "gfec"], ["fcgedb", "cgb", "dgebacf", "gc"]],
[["fgaebd", "cg", "bdaec", "gdafb", "agbcfd", "gdcbef", "bgcad", "gfac", "gcb", "cdgabef"], ["cg", "cg", "fdcagb", "cbg"]],
[["fbegcd", "cbd", "adcefb", "dageb", "afcb", "bc", "aefdc", "ecdab", "fgdeca", "fcdbega"], ["efabcd", "cedba", "gadfec", "cb"]],
[["aecbfdg", "fbg", "gf", "bafeg", "dbefa", "fcge", "gcbea", "fcaegb", "dgceab", "fcbdga"], ["gecf", "egdcabf", "bgf", "bfgea"]],
[["fgeab", "ca", "afcebg", "bdacfeg", "cfaedg", "gcfdb", "baec", "bfadeg", "bafgc", "acf"], ["gebdcfa", "ecba", "ca", "fadegcb"]],
[["dbcfg", "fgd", "bdegcaf", "fgec", "aegbdf", "ecdfab", "fbedc", "dacgb", "gdcebf", "gf"], ["cefg", "dcbef", "fcge", "gbcadfe"]],
[["bdfegc", "cbegaf", "gecbf", "dfcage", "bdacg", "ed", "bedf", "ced", "adcbefg", "gebcd"], ["ed", "bcgafe", "cdgba", "cbgef"]],
[["egadfb", "cdbfeg", "cegd", "fecab", "cgb", "gbdefca", "cg", "fgcdab", "egfdb", "bfceg"], ["gbdfcae", "bgc", "cg", "cgb"]],
[["gcafb", "gcf", "dcaebfg", "ecagb", "gf", "abcdeg", "gaef", "cafbge", "fdbac", "fegbdc"], ["fgae", "cfgab", "fg", "bagce"]]]

data = [[["ecfdbg", "decfba", "aegd", "fdcag", "fagecd", "gd", "gcafb", "efdac", "cbgeafd", "dfg"], ["bgacf", "afdebc", "fceda", "cabfg"]],
[["cfdabeg", "cda", "bcgad", "bedfac", "aefbgd", "bfgcad", "dfbga", "egabc", "dgfc", "cd"], ["gdbefac", "fgabcd", "dcbefag", "aedgfb"]],
[["aedbfgc", "gcaf", "ebgfca", "bca", "edgcfb", "adbge", "gebac", "fbegc", "ac", "afdcbe"], ["ceafbg", "acb", "egbad", "gfaebc"]],
[["gaeb", "cafdbg", "aedfc", "ecfgdb", "ab", "cdaefgb", "cgbdae", "bdecg", "cba", "eacdb"], ["gfacdeb", "gabdec", "begcd", "adbce"]],
[["fcbgea", "fbedg", "bc", "cbefg", "befgcda", "cfgdab", "gbc", "efdgca", "fecag", "aceb"], ["faecg", "cb", "cb", "fecbga"]],
[["fdebcg", "bag", "gdefa", "ceadgb", "fcab", "ebagfc", "ab", "fbegc", "fcaedbg", "fbeag"], ["cfegb", "bga", "edfga", "fgbec"]],
[["fg", "fcagb", "dfgceba", "edgacb", "fagd", "gfb", "dcgba", "agcfdb", "gecfbd", "ceafb"], ["facgb", "fbdcge", "gf", "gfabc"]],
[["eabfd", "dfb", "gbcfad", "ebdag", "fagbce", "gefabdc", "edcf", "aecfb", "cbdafe", "df"], ["egbcdfa", "afdebcg", "aecfbd", "acefb"]],
[["fbaec", "bfegad", "bga", "deacbg", "gb", "fbdg", "acgdef", "deagf", "fgabe", "gabecdf"], ["fgdb", "gefba", "gcdafe", "bg"]],
[["bfdea", "agfbc", "gbd", "faecdbg", "gd", "efgd", "cdgeab", "efadbg", "faebcd", "fabdg"], ["cdbgea", "fged", "cfabed", "bgd"]],
[["gfedac", "cgaef", "gab", "ceba", "ba", "afcdgb", "gdefbac", "fegbd", "bafeg", "abcgfe"], ["gcbadf", "egafb", "ebafg", "ab"]],
[["bgda", "agfcdbe", "agfde", "faegb", "baedgf", "fcdaeg", "fdbeac", "ba", "bcegf", "bfa"], ["bcefg", "eagdf", "ab", "bacefd"]],
[["dfgbac", "fdcaeb", "cbgeda", "bfdea", "dcabf", "ebadcfg", "gfbea", "dbe", "fecd", "ed"], ["ebd", "cdfe", "bgeaf", "cdbfea"]],
[["efdba", "edb", "eagbcd", "bacef", "bd", "bcfd", "becfagd", "begcaf", "cbaefd", "aefdg"], ["fdage", "edbgac", "cgaebd", "bed"]],
[["gfecbd", "gbadf", "fabged", "gbf", "cbdage", "fagcd", "feab", "edgcbaf", "fb", "aedbg"], ["agdcf", "bgfda", "afdgc", "afdgb"]],
[["gfaedc", "caefb", "badcfge", "dgfe", "acdgbf", "eag", "eg", "fgacd", "gecfa", "ecbdag"], ["acdbgf", "cbegad", "cgdaf", "eag"]],
[["gfebda", "fgacd", "dfbag", "bg", "geab", "gcbdeaf", "eacbdf", "cedbgf", "fbg", "abfed"], ["aedfb", "gb", "eafdb", "dbafe"]],
[["ebadfc", "efdbga", "bega", "fdgcae", "dbgaefc", "edfab", "fag", "ag", "dagbf", "cfgbd"], ["efacgd", "dbefag", "fadebg", "bgfad"]],
[["bf", "fbd", "cgbdaf", "dcfbae", "fgbcd", "gcbadef", "gafcde", "bfag", "cebgd", "dcafg"], ["afbedc", "gcdeb", "fbgadc", "dbf"]],
[["gfecab", "fageb", "cgb", "acgeb", "gdfeab", "ecbafdg", "gfca", "aecbd", "gc", "edcgbf"], ["afcg", "cedba", "aecdb", "cgeba"]],
[["cdge", "abfdge", "cgfeadb", "bdc", "gbacd", "cd", "cdaebf", "bgeda", "cgdaeb", "acfgb"], ["baecdg", "fcbag", "dfeagb", "gcde"]],
[["efabdgc", "ecafg", "dacgbf", "ecgfd", "dfe", "gbfdec", "ed", "bedc", "cfdgb", "gedafb"], ["egcaf", "cfgae", "efcgd", "de"]],
[["bfagdc", "dbagef", "gbedcf", "afdeb", "ab", "edgfb", "gdebfac", "fdeca", "baf", "eagb"], ["bfa", "bgadfc", "adcef", "ab"]],
[["cfdbae", "dgefc", "fcaeg", "geafdc", "dfag", "fd", "cegbd", "daefbgc", "cfd", "cefbag"], ["efgcd", "cgdfe", "cefdg", "cdf"]],
[["cbged", "feabc", "fdgb", "egf", "ecfdbg", "dfgcea", "gabfdce", "ebcdag", "bgefc", "fg"], ["fbgec", "bgdf", "efgcbda", "cbedg"]],
[["ebcdfa", "ef", "cfe", "cadbfge", "becfd", "dgbeac", "dafe", "gbdfc", "cefgba", "ceabd"], ["bfcaeg", "gfedcab", "acbfge", "fe"]],
[["fbdage", "bf", "acdgb", "cabf", "gcfed", "gdcfbea", "fgbdc", "fbd", "fcbadg", "bgedca"], ["bcadeg", "bf", "facbdeg", "gdabef"]],
[["gfacdbe", "fga", "gbdaf", "gadbc", "dfeagc", "fg", "bcgf", "eacgbd", "acdgfb", "debfa"], ["gdcab", "agcbd", "dafbecg", "gfa"]],
[["gadbcf", "badfe", "bae", "cfaed", "abfdg", "adfecbg", "eb", "bedgaf", "ecfagb", "egdb"], ["bdaef", "egfdcab", "eb", "be"]],
[["dbgecaf", "gacd", "dfbac", "dbaefg", "dba", "bfgced", "cafbdg", "cbfgd", "faecb", "ad"], ["degbcf", "baegdf", "gaedbf", "dfegbc"]],
[["afgcd", "dabgf", "gedfba", "agc", "bdfgac", "gdefc", "bcaf", "cfeadgb", "ac", "ecdbga"], ["gfadbec", "fgcda", "edgbac", "fbagd"]],
[["acbegfd", "cgeb", "dagbef", "gbaed", "caebdg", "gc", "dafgec", "adcbg", "cdbfa", "gdc"], ["bdaeg", "bdfac", "bdfac", "bcgad"]],
[["gfab", "agfbde", "fa", "edbgf", "cbedfa", "decga", "cdagefb", "degbfc", "egfda", "afd"], ["daf", "fa", "afd", "efacbd"]],
[["caegdbf", "daefg", "fbgac", "be", "fgaeb", "cbea", "bge", "cdfagb", "dgecfb", "abecfg"], ["gebaf", "aceb", "gfdecb", "befga"]],
[["efcgda", "bd", "efgdcab", "afbec", "bgcd", "fdagc", "dgabef", "dab", "dafbc", "cfdagb"], ["dba", "dcgb", "ecbdfga", "abfcd"]],
[["abdge", "fd", "fda", "fecd", "bfcage", "fecdba", "fdgbcea", "afbde", "acdbfg", "cfbea"], ["fedc", "fced", "adebf", "fbacde"]],
[["acfdbe", "egcadb", "gfbacd", "acfbd", "bagefcd", "bgfa", "cefgd", "gac", "cdagf", "ag"], ["ag", "bcadeg", "dgcafb", "cefdg"]],
[["eabdfc", "fcaeg", "fecad", "bcfda", "dcfbge", "ebda", "de", "ced", "fdacbg", "dfbcega"], ["gcebfda", "gdecfba", "dbgfec", "defca"]],
[["bfc", "gdfceb", "cf", "eafgbd", "edcab", "ebcfa", "gfeacb", "acgf", "adcbgef", "fabge"], ["bafgecd", "fgabe", "aegbcf", "badec"]],
[["gfbc", "gaced", "fg", "bfcda", "fgd", "fcgad", "dgefbac", "bcafde", "dgcfab", "edgfba"], ["bcgf", "bdceaf", "dbfaec", "bdacf"]],
[["acbdgf", "dfcgb", "dcfeg", "egbd", "aedfc", "fcebag", "ge", "gef", "cfegdba", "fgbdce"], ["gcbfea", "fceda", "dcfgb", "dfgbc"]],
[["agcfd", "fga", "fecda", "gadebf", "dbgcfe", "fcbdga", "dcfgb", "ga", "gbac", "cbfgead"], ["fdeca", "gbcdf", "cfdgb", "afg"]],
[["eba", "ebdc", "gbefda", "dcbegaf", "fbaced", "afgec", "be", "dcfba", "ebacf", "dfcagb"], ["eb", "eab", "bea", "be"]],
[["bfcge", "bfead", "edgfacb", "edcfag", "abegfd", "becdf", "dacb", "cd", "cde", "bfdcea"], ["adefgc", "cdab", "fbead", "dcba"]],
[["bacegd", "gafcbe", "begfa", "bcfad", "ed", "gedf", "ebgfda", "bdefa", "ead", "fegdbac"], ["geafb", "fedba", "dbcage", "egdf"]],
[["df", "fbgdc", "fcd", "bfgce", "abfd", "cdfgba", "cgefad", "cgbad", "ecadgb", "egbfacd"], ["bcdgaf", "cedfga", "dbgafc", "dgfbc"]],
[["dfabge", "bcfdg", "egfbca", "bdaefcg", "decbfg", "ebfgd", "fgdca", "cb", "cbde", "cbg"], ["beadcgf", "dgacf", "adfgc", "bc"]],
[["fgda", "dafecgb", "egdbf", "gef", "dbgec", "agebcf", "gf", "edgafb", "fcaedb", "bafde"], ["fg", "fecdab", "bdefg", "bgfde"]],
[["abfgecd", "eabgf", "fcdabe", "gbdafe", "acebg", "dfecgb", "gf", "gfb", "fgad", "dafeb"], ["efdacb", "efadcgb", "dagf", "dfabe"]],
[["ceafbg", "dfcabe", "gcfea", "gbac", "fgead", "gc", "cbdgef", "egc", "aecfgbd", "cefba"], ["badecf", "badefgc", "bfaec", "cbeaf"]],
[["cadfb", "caefbd", "cbfega", "fdbga", "cad", "dc", "edbc", "aefbc", "egbacfd", "dfgeca"], ["cefdab", "cdfage", "bacdf", "dbafc"]],
[["gfcb", "cf", "ecafdg", "fcbed", "dfbagce", "fbgeda", "gdfbec", "cef", "eacbd", "ebdfg"], ["gbdaef", "caedfg", "cf", "gbdefc"]],
[["gd", "cgd", "ebdafgc", "cfbega", "gcbfde", "bcfdg", "badfc", "bgaced", "bcefg", "gedf"], ["gfed", "fcbgd", "cdgfbe", "cfbeg"]],
[["bfga", "dabge", "befacd", "agbdce", "fb", "aegfbd", "fcged", "dbegf", "ebf", "ebgdcaf"], ["bagf", "ecfdg", "fbe", "bedagc"]],
[["beac", "ea", "ade", "gefcd", "ecgbad", "cbagd", "badgcfe", "ebfgad", "acgde", "gcfdab"], ["ea", "gceadb", "gcbad", "cbdga"]],
[["cadfbg", "bcgafed", "cbedf", "afeg", "abegdc", "adf", "gedca", "efacd", "acdgfe", "fa"], ["daecg", "fdecga", "edafc", "adbgce"]],
[["egd", "ed", "egacd", "cgabfed", "efcd", "degfca", "dagbfc", "dcagf", "bgfdea", "abecg"], ["dge", "egcad", "ged", "cgdfa"]],
[["cgdeaf", "fcbdeg", "fgc", "dgcea", "cadgbe", "abdcfeg", "gf", "cafbe", "gadf", "cfega"], ["aecgfd", "bfaec", "gf", "dceabg"]],
[["caegd", "cbfgae", "dafg", "egd", "gd", "ecafg", "gfabdec", "cafdge", "bacde", "bdfecg"], ["gedfcb", "edcagfb", "cdega", "becgfd"]],
[["badgfe", "ed", "dcge", "fgdceb", "cebfd", "cbfedga", "dabcf", "efd", "ecgafb", "cgbef"], ["dgec", "dfe", "ecbgfa", "cebgaf"]],
[["dgabcef", "bcd", "cfeadb", "degfca", "bgace", "gcebd", "cegfd", "gbdf", "bd", "begfdc"], ["acbeg", "dbc", "gdfb", "gfdb"]],
[["edafgb", "bagf", "acedb", "dbg", "fcgdabe", "bcdgfe", "gb", "bgead", "dfaecg", "faged"], ["gafb", "dgafeb", "gbaf", "fadegb"]],
[["bc", "abcegf", "bfcgd", "gdcbef", "dcbe", "gcb", "cafegbd", "aegdbf", "dfagc", "dbegf"], ["cbg", "cbg", "cfedgba", "dgcfabe"]],
[["be", "ecgbf", "cbafg", "ebg", "bagedc", "fbae", "degfabc", "fgcdab", "dgfce", "cabfeg"], ["gfcde", "dgfbca", "dcabgf", "bacegd"]],
[["af", "dbacge", "efa", "abegfdc", "gfdce", "begcfa", "aecfg", "afbced", "fgba", "ecabg"], ["ecadfb", "gfeca", "efa", "gefdc"]],
[["acbedg", "edfacbg", "begd", "cdfabe", "dagcb", "eacdb", "gfeabc", "bg", "gba", "dfgac"], ["cegbaf", "ecfdba", "cgbda", "dfebca"]],
[["dcbgaef", "bca", "abed", "cbgad", "gdaec", "fecbag", "edgbca", "geadfc", "ab", "cdgfb"], ["beagcd", "dgbca", "eabd", "ceabgd"]],
[["cgabe", "gfcbe", "cfegba", "fdbgc", "fe", "fdgebca", "aedcbg", "gfea", "bfdcea", "fbe"], ["feb", "gaef", "badgec", "ecgabf"]],
[["afecdg", "dfbc", "cd", "dcg", "aegcb", "baedgf", "becgd", "becfdg", "eacgbdf", "ebdgf"], ["gbedf", "edgbf", "bcdeg", "gfadbe"]],
[["gfdba", "adbefc", "ebcdfag", "bcgaf", "bfdaeg", "dg", "adbfe", "egbacd", "bgd", "dfge"], ["gbd", "bgd", "bcgfa", "fbgad"]],
[["dfaegb", "fe", "bcgde", "face", "afgbdc", "acgebdf", "agfcb", "cgbef", "fcgbea", "gfe"], ["acef", "afedgb", "bgdfcea", "fgedab"]],
[["abdcef", "gdfea", "cbaef", "gaefb", "cagebf", "agfdbec", "agdbfc", "ecgb", "fbg", "bg"], ["aebfc", "egcb", "acfgbe", "gebc"]],
[["bcf", "gbadec", "bf", "bgaf", "fcdea", "cgbda", "gebdfc", "dgefcab", "fcabd", "bdagcf"], ["edacf", "bf", "cfb", "gadcb"]],
[["cdafgb", "bgdf", "gacefd", "cdb", "bd", "ecfadbg", "cdafg", "cdebag", "bfadc", "ecafb"], ["bcefa", "cfdba", "agdfc", "fabdc"]],
[["egb", "dgbf", "bgdeca", "febag", "fbadge", "ebadf", "aecfg", "gb", "geacfdb", "fbacde"], ["fdbg", "bg", "caegf", "egfab"]],
[["ac", "eagfbdc", "bgacf", "cbdgae", "gabdf", "acdf", "gdfaeb", "acg", "dbgafc", "gbfce"], ["gdbeaf", "agbcf", "dcbagf", "fgadeb"]],
[["ef", "eagf", "bfegcd", "gbaefd", "fbe", "eafbd", "dagfb", "abced", "agcfbd", "abcefdg"], ["ef", "ef", "ecdgfab", "deafb"]],
[["fdgbc", "efbgd", "aedbg", "dfce", "bcagdf", "fe", "fegcab", "cdgabef", "efg", "cgdfbe"], ["efgcdb", "efg", "agcfeb", "dgfabc"]],
[["fe", "dbefgac", "baegc", "eagfc", "ebgf", "acdgf", "aedbfc", "bgafce", "cef", "bcgdea"], ["agbdce", "aecbfg", "cdgaf", "ef"]],
[["fbgcd", "bdf", "dfbega", "dfcga", "abfdcg", "db", "dabc", "cfebg", "feadgc", "ecgbdaf"], ["fcbeg", "gcdfb", "cgbdf", "acfdg"]],
[["bac", "cdbeagf", "abfd", "bcfea", "edcfba", "abdcge", "edacf", "gcbfe", "gcdefa", "ba"], ["cegfb", "cafde", "ba", "fegdcba"]],
[["gcabfd", "acdg", "cg", "gfdbcae", "ecbgfa", "cbg", "bfegd", "gdcfb", "cedafb", "fadcb"], ["cgfbd", "cfgdb", "fdegb", "cg"]],
[["fcdaegb", "gdefcb", "dgfacb", "dcgea", "eb", "dgcbf", "afcegb", "bgced", "bdef", "bec"], ["ecdag", "eb", "befd", "dabcfge"]],
[["defcb", "eabcf", "bca", "abfeg", "ac", "cafbge", "gfac", "dbaecg", "fcbegad", "bagedf"], ["bfgae", "cfga", "ecabf", "aegbcf"]],
[["gdcfea", "adgcf", "cbged", "bgadfc", "gbf", "gfdbc", "cfegdba", "bcfa", "bf", "dgaefb"], ["fgadc", "bfg", "fb", "bf"]],
[["bdgcaef", "adg", "egbca", "cdabg", "eadbcg", "eadc", "cgdfb", "efagbd", "ad", "ebfagc"], ["da", "dace", "dga", "gedfab"]],
[["cade", "afgecd", "fgedc", "cbaegf", "efbgd", "gdfcabe", "ce", "fec", "cadgfb", "dcgaf"], ["ce", "adefgc", "cdea", "fce"]],
[["efgcba", "ged", "gcdbea", "acgeb", "decag", "cdgaf", "egbcafd", "bdae", "fgcbed", "de"], ["adeb", "edg", "cgadf", "agdec"]],
[["agfce", "af", "febgc", "ebgadc", "cadeg", "dafg", "faegcd", "bceadf", "bfaecgd", "efa"], ["egbcf", "fbgec", "acedg", "af"]],
[["cbgdae", "debcfa", "becadfg", "agecb", "gcde", "cfgba", "ce", "begda", "bec", "fdaebg"], ["bec", "eadgb", "eadbg", "badefgc"]],
[["bagedf", "ecf", "ec", "dbefc", "cbedfa", "edca", "dfbcg", "edbfa", "eabgfc", "aefgcdb"], ["fec", "dafebc", "cfe", "aefdb"]],
[["aef", "bface", "dabefg", "ebfdgac", "caeg", "bgfac", "fcegba", "fcbed", "ae", "cfgbad"], ["efcba", "baefc", "afbcg", "gbcfa"]],
[["dfeca", "fdagcb", "feagc", "adcbef", "fg", "gefd", "cabge", "fgdbace", "cegadf", "cgf"], ["fg", "decfab", "cfdbga", "baecg"]],
[["gbaefd", "agedbcf", "cagbe", "fb", "cgbeaf", "baefc", "bfgc", "bgeacd", "efb", "dcfae"], ["gcbaed", "fb", "bgfcae", "bcfg"]],
[["cegf", "bcedg", "bgacdef", "gbedf", "fg", "ebadf", "ebgdcf", "dgcfba", "debgac", "bfg"], ["bdfgca", "bgf", "fgdbce", "becfadg"]],
[["decafgb", "acgbd", "fegdab", "cefag", "dfcga", "gdf", "fd", "aecfgb", "dfecga", "cefd"], ["gcebfa", "fgacbe", "fgbdae", "fcde"]],
[["faebc", "acb", "bdfgca", "afgedcb", "ab", "daeb", "fcbge", "afcebd", "feacd", "cafedg"], ["fbgdca", "ab", "afedgc", "ceafbd"]],
[["gfeb", "ebgcdfa", "dfgca", "abfdg", "agebd", "bf", "abf", "bceafd", "dabgce", "dbfgae"], ["fgeb", "gadbf", "gcafd", "bf"]],
[["ecbdfg", "gecdfa", "efcadgb", "ebdac", "deabf", "fbga", "bf", "dbf", "efagbd", "dfgae"], ["adfbe", "cfdage", "efdcga", "gfab"]],
[["fg", "cedbgaf", "feacbd", "dafgeb", "fag", "gfecba", "acgde", "febac", "cfega", "fcgb"], ["decbgfa", "fg", "ecgad", "afdbgce"]],
[["cfbgde", "aegcdf", "daefbc", "dgceb", "fcged", "gafdecb", "cbfg", "bc", "ceb", "gebad"], ["dafecbg", "eagdb", "bec", "begdc"]],
[["cdefga", "fbgcade", "fgdca", "cd", "bafdec", "adc", "dbgeaf", "cafgb", "efgda", "cegd"], ["afcgb", "ecdg", "bcfag", "caedfg"]],
[["agfbc", "af", "deagfbc", "fecbg", "gfa", "fcegbd", "cfae", "bgafec", "edagbf", "bcadg"], ["agf", "ecfa", "becfg", "af"]],
[["bdgf", "afceg", "adcfeb", "egbaf", "afgbde", "afb", "fb", "cegbfda", "daebg", "adgbec"], ["fba", "ceadgbf", "bf", "fb"]],
[["efgb", "eg", "aecbd", "ecbdg", "daecgf", "dcgfb", "fbagdc", "egfadcb", "gce", "ecbgdf"], ["afbegcd", "fegdac", "cebad", "bgafdc"]],
[["acgbd", "eb", "dbace", "bdafgc", "fabdge", "bceg", "gecdba", "edcaf", "aeb", "bagcdef"], ["fdgabc", "fegadb", "dgbcfea", "egabfd"]],
[["cadfgb", "acefdg", "fcb", "fbea", "fb", "ebdfca", "ebcdf", "degcb", "dfaec", "cbdefga"], ["aefcdbg", "cdegaf", "gdbec", "dcfae"]],
[["fcdab", "edc", "cfeb", "gdfcae", "dcaeb", "ec", "gdcbaf", "fdcabe", "debga", "efbgadc"], ["fcbe", "gbaed", "fcaedb", "acedgf"]],
[["gb", "gefca", "acbfge", "bdgaecf", "bfcag", "bdfca", "abg", "aedfgb", "gebc", "agfecd"], ["cgafb", "ebcg", "aecfg", "efgbac"]],
[["dgabcef", "fbdgea", "fb", "cdbf", "cebfg", "bdaegc", "dgceb", "egcdfb", "bfg", "acgef"], ["cbgde", "faegc", "befgdca", "cbdf"]],
[["cfaebdg", "fg", "fgcead", "agedb", "fge", "ebcdf", "gebdf", "dfeagb", "dbgace", "fgab"], ["gfba", "eagdfcb", "dcabeg", "cegafd"]],
[["fbe", "egcba", "bgefdca", "bgdafe", "afdgb", "fdbgac", "dgcbfe", "fbega", "defa", "fe"], ["ebf", "egafb", "fbgdac", "egafb"]],
[["gdc", "acfdeg", "geabc", "dbfg", "dabcfe", "dbeafcg", "dg", "bedcf", "edcgb", "efcbdg"], ["agcefd", "cbdfe", "dg", "bcedf"]],
[["bafgcd", "febdgca", "abgcf", "bcgea", "be", "edgac", "aeb", "cbef", "afebgd", "ecgbfa"], ["bea", "eb", "ecfbag", "abfcg"]],
[["cdae", "cbd", "gacbe", "fcbdge", "cefbag", "bagcde", "gcabd", "bdafg", "dc", "fdgebca"], ["cegdfb", "gbeacd", "cd", "cabdge"]],
[["dac", "dfgae", "fcdabg", "agbc", "dcfbg", "gfedbc", "fadcg", "bfaegcd", "ca", "eadbcf"], ["cfabged", "ac", "cbag", "dfceab"]],
[["egbdcf", "bdeagfc", "aegcb", "bafec", "fdceb", "edgafc", "caebfd", "aef", "fbad", "af"], ["efa", "adfcbge", "dfba", "ebgac"]],
[["ebadg", "fcaeb", "dc", "acdg", "becgfd", "adecgbf", "dbc", "dbeafg", "dbaec", "bedagc"], ["cdb", "bdc", "dc", "aecbd"]],
[["cfaegbd", "agbdce", "edca", "badgf", "edgfbc", "ebagd", "ed", "gde", "aebfgc", "ebcag"], ["cbeag", "edca", "gdbea", "fbedgc"]],
[["fgb", "dfagceb", "cabgdf", "gf", "afge", "ecbaf", "deabcf", "cbdeg", "bgefc", "gfceba"], ["bgecd", "gf", "bacef", "fg"]],
[["abd", "fgcdaeb", "gfeabc", "gdfacb", "fcbea", "faebcd", "dcbeg", "badce", "ad", "dafe"], ["adecb", "gfaebc", "fdcbga", "aecdb"]],
[["fcgdeab", "eabgf", "feagd", "dge", "dg", "cdaefb", "acedbg", "cdfg", "gcaedf", "efadc"], ["cfade", "cbeadg", "bgfea", "dg"]],
[["fegcb", "fcedag", "badgce", "fcbdgea", "afg", "gafeb", "af", "dbgefa", "degba", "fadb"], ["fbegc", "fabge", "af", "dcgabe"]],
[["abcdfg", "dcbfea", "bagd", "cegfb", "bd", "dbf", "cgafde", "edgcbfa", "fgdca", "bcdfg"], ["fdabce", "gbcfd", "cbefda", "ecabdf"]],
[["afgbd", "fbgde", "dcfageb", "ag", "gba", "gfdcab", "eadgcb", "cfag", "daebfc", "cdbfa"], ["ga", "ag", "bdaefc", "ga"]],
[["egf", "ecabfd", "fg", "ecdfb", "cfgb", "cbegadf", "dgbfae", "begcfd", "agcde", "cgdfe"], ["gbdefa", "fedgc", "cafedb", "cfdge"]],
[["bafcdge", "dgbace", "cgbad", "cdafe", "bedcfg", "be", "abge", "cebad", "dcfabg", "bed"], ["dbe", "gabfced", "cgbedf", "cbadg"]],
[["becagf", "fdec", "debafc", "afedb", "adbgc", "bgdfea", "dabcf", "cf", "cabegfd", "afc"], ["bagdc", "decf", "fca", "dfbae"]],
[["dcagb", "gfcade", "cgdebf", "fdbeag", "gdfeabc", "efdcg", "ecfb", "deb", "egbcd", "eb"], ["eb", "edagbf", "ebfc", "eagdcf"]],
[["ebcdaf", "fgdc", "gbeac", "dgfae", "efadbg", "cd", "gcefda", "dgace", "fbgedac", "cda"], ["aegdc", "dfabge", "gcade", "daceg"]],
[["fgdcb", "adceb", "fcgeabd", "acedbg", "af", "fba", "aebgdf", "efac", "dcabfe", "adbcf"], ["cdbaf", "cgeadb", "bdcae", "bfgaed"]],
[["fcb", "fc", "fcdgb", "dabfg", "eabcfdg", "cbged", "cefg", "begdca", "gcdbfe", "efdacb"], ["ecfg", "fabgcde", "gdecbaf", "bacged"]],
[["gfdabc", "ad", "bdfgea", "fegbdac", "gbaecf", "bfega", "adg", "adbe", "afged", "egdcf"], ["dcfgab", "bgcefa", "gad", "gafcbd"]],
[["bgdcfea", "afb", "gabfcd", "adbfeg", "efdba", "bgdfe", "dfgbce", "eafdc", "bage", "ab"], ["ab", "dgefb", "baf", "bgaedcf"]],
[["geabd", "adecfgb", "cg", "ebcdfa", "agfbdc", "fdcg", "dabcf", "dcbag", "faebcg", "cbg"], ["dagbe", "fgdbeca", "cbagdfe", "fcbeda"]],
[["bdfa", "dafbge", "fgedb", "bfceg", "bdg", "afdebgc", "bd", "bdaecg", "defcga", "gfdea"], ["bagfdce", "dcgafe", "fegbc", "dbegca"]],
[["aedcgb", "fb", "gdbaf", "dgabe", "acdfg", "fabgde", "fadecgb", "gbf", "edfb", "facegb"], ["agdcf", "badeg", "fb", "fabcge"]],
[["dfbce", "gafed", "ba", "eagb", "gfdbca", "aefdb", "fecdag", "fagbedc", "abf", "egadfb"], ["eafdb", "edfcbag", "dcfbe", "ba"]],
[["afdec", "fcegda", "edgabc", "bgdfc", "faebdc", "ba", "bac", "dcfebag", "fadbc", "fbae"], ["deafc", "acb", "fbgaecd", "cfdea"]],
[["gecd", "dgf", "eabdf", "gd", "gfdeb", "fgcadb", "gcbfae", "cefbg", "cedfbg", "cfeabdg"], ["gd", "edfba", "fgbce", "fbgec"]],
[["adfge", "bcgfde", "baecg", "dcfgaeb", "bafdge", "gdeac", "dagcef", "dc", "cdg", "acdf"], ["cgd", "dgcae", "gcead", "cd"]],
[["efgac", "agbfedc", "aecbfd", "agbfde", "dcbg", "fdbag", "gacdfb", "bc", "fgbac", "fbc"], ["bc", "afdegb", "bgdc", "edbafg"]],
[["be", "cbfgad", "acegdb", "agefd", "dabgc", "cebfgad", "gbce", "bdega", "dfbace", "bed"], ["bagde", "eb", "egcb", "edfbac"]],
[["gf", "fag", "afgbe", "ecbaf", "geadb", "eabgdf", "egdf", "dagbfc", "ecagdb", "cbgdeaf"], ["cbefa", "fg", "bdega", "gfacbed"]],
[["bag", "defba", "gcfdae", "cgbd", "gb", "eabgfc", "gcfabd", "dfagb", "gcdfa", "ecbgfda"], ["begacf", "agb", "cgfade", "fcdga"]],
[["adgfcbe", "egd", "fgadeb", "cgbdae", "acdgb", "cgedb", "deca", "de", "efcbg", "acbdgf"], ["cfbdag", "dcgba", "geabdf", "eadc"]],
[["cagdebf", "dgebcf", "edc", "abecfd", "egfadb", "fabed", "ec", "gadbc", "efca", "dabce"], ["dec", "fbadec", "debac", "edc"]],
[["fcedg", "dfgbae", "eg", "deg", "egcb", "fgcebd", "efacd", "gfdcb", "gbfecda", "gdafbc"], ["efacd", "ge", "cfgabde", "fagecdb"]],
[["dbag", "aefcbd", "gbc", "gcdbf", "bdcfa", "bg", "dfabcg", "ebadgcf", "cfgeba", "dgecf"], ["bfaced", "gedcf", "dbag", "cgbdaf"]],
[["cdgfbea", "gd", "bdag", "gebca", "bdcgfe", "dgc", "fcagbe", "gabedc", "afcde", "cdaeg"], ["abgcde", "ebcga", "dagb", "bgcefa"]],
[["cedgbfa", "ecabgd", "cdafeb", "bafcg", "cegdbf", "cae", "gdae", "gabce", "ae", "edcgb"], ["aec", "cageb", "ecdgfb", "egda"]],
[["eacgbf", "afbdg", "gdecaf", "gafbcde", "gfc", "baefc", "bcge", "fcabg", "fdcbea", "cg"], ["agfdb", "cgfba", "bgafc", "eacgdf"]],
[["fgebd", "fed", "bfea", "cbdeg", "decfga", "fe", "cfdgba", "defbgac", "dfgba", "afdbeg"], ["fgdba", "abegdfc", "bcadgf", "fbegd"]],
[["adbfcg", "fagdbe", "bagec", "dc", "fbaedcg", "bdfag", "gbdca", "fcgedb", "dcfa", "cgd"], ["fcad", "bfdgae", "dgc", "eagbc"]],
[["fgbaecd", "fgecd", "cafeg", "feacbg", "fdgcb", "fgaecd", "acdbge", "ed", "adfe", "dge"], ["cfgdb", "gcedf", "deaf", "cfdbg"]],
[["gedab", "afdcbeg", "decabg", "bfedcg", "dgefab", "ef", "aedf", "cfgab", "gbaef", "efb"], ["abcgf", "cabgf", "feagdcb", "cdbaefg"]],
[["fdb", "ebdgfc", "bd", "adefgcb", "efgad", "gbcd", "dfbge", "afcgeb", "fecgb", "dbeacf"], ["bfd", "cgfdeba", "cafdeb", "gedfa"]],
[["abgde", "bdefa", "fagdbe", "fbadceg", "dgecab", "dfe", "ef", "edfgca", "bfdac", "fbge"], ["fegb", "cagdeb", "ecdgab", "bdagefc"]],
[["febad", "bacged", "fge", "cdbeg", "cfebdag", "fgdc", "gf", "debcgf", "bdefg", "cfebga"], ["fg", "egf", "beafd", "efg"]],
[["agdcbf", "bdefcga", "cbgefd", "dcagb", "gbedac", "faedc", "gfc", "bfag", "gfcad", "gf"], ["bgfa", "dbagc", "bfgdca", "bcgad"]],
[["bdce", "gafbed", "gaecf", "bcefdag", "gbc", "dacbeg", "fcbgad", "egdab", "cb", "cegba"], ["eadbgc", "cb", "ebadgf", "debc"]],
[["ac", "afgceb", "eagbf", "befcagd", "abcg", "degcf", "aefbdg", "ceagf", "edbacf", "acf"], ["abecgf", "bgac", "gacb", "ceadbf"]],
[["abcg", "fcaeb", "gfdcabe", "ab", "befdc", "cfage", "gdbfea", "gecdaf", "efcgba", "bfa"], ["bgac", "bcga", "cagb", "efgbda"]],
[["fbdeg", "gb", "fcdeb", "dfecbg", "eafgdbc", "edgfa", "eagbdc", "baedfc", "cbfg", "beg"], ["adbgce", "dfcaeb", "bgfc", "abcged"]],
[["afg", "afdbec", "cbdgaf", "afcgedb", "bedgf", "cdagef", "ga", "afcdb", "gbca", "gfbda"], ["cfagdb", "edcafg", "cbfgda", "bgfed"]],
[["edgafcb", "fdeab", "dgabcf", "cbgf", "gdfeac", "dgfab", "gdeacb", "acgbd", "gfa", "gf"], ["gaf", "bcgf", "ecbagd", "agf"]],
[["dcbfa", "gfbace", "ebfca", "efcg", "bgfeadc", "abgce", "gbafde", "ef", "beadcg", "fbe"], ["egcf", "fabdc", "adebgf", "bdcage"]],
[["gc", "cfdbe", "fgcebd", "bcgef", "ceg", "fdagceb", "ecadbg", "fgdc", "fageb", "bedcfa"], ["adgcbe", "aefgdcb", "gabfe", "gc"]],
[["fgead", "bcdafg", "ba", "bcae", "edafb", "bcefad", "dbcfe", "cafbgde", "gbcdef", "adb"], ["dcfeb", "gecdfb", "caeb", "bacdfe"]],
[["gfeab", "abc", "bc", "ecbf", "gdebaf", "gebac", "gdcea", "gecdfba", "acdfbg", "fbgcae"], ["cbdagf", "gbcae", "bc", "edgbaf"]],
[["aecgf", "acbf", "cgadef", "fecbg", "bc", "ebc", "dcegba", "befdg", "aebgcf", "afdebgc"], ["ecb", "bcgfe", "bgedf", "abcf"]],
[["fg", "facg", "efcagd", "eadfg", "cebfda", "feg", "daegb", "bdfcge", "afced", "cfeadgb"], ["acdfe", "fgeda", "fg", "cdbegf"]],
[["gefda", "fed", "edfbgc", "fgeab", "cfad", "cdeag", "fd", "cebgad", "dcefabg", "fagdce"], ["faegdc", "eafdg", "fd", "cgbfdea"]],
[["ebfad", "cf", "befca", "gabedc", "fac", "cabeg", "dcaefg", "abfecg", "fbacged", "gcbf"], ["bfade", "fcbg", "fc", "cgbf"]],
[["aegbf", "cbdfega", "adbfg", "ef", "cebdgf", "dfcbga", "gebca", "fadgbe", "afde", "gfe"], ["fdae", "afcbgd", "bgcedaf", "gef"]],
[["cdgab", "cg", "edgbac", "gbedfa", "gebcdaf", "dcebfg", "gcd", "degba", "aceg", "dacfb"], ["gdc", "cgdba", "cdg", "gbadc"]],
[["daebfg", "fcebgad", "db", "gacbf", "feacdg", "gafdb", "eafdbc", "dgaef", "dfb", "bedg"], ["cefdbag", "gedfca", "gafdeb", "befcda"]],
[["ecfd", "fcdgba", "cebgf", "fge", "bgafed", "febdcg", "cbfegad", "cabeg", "fe", "gfdbc"], ["ecgdfb", "edfc", "gebdaf", "fecd"]],
[["fac", "gbeaf", "bcdga", "adgbcef", "febcda", "cfgba", "gefbda", "bagcfe", "cfge", "fc"], ["gcfe", "gbcaf", "acfbeg", "acdgb"]],
[["afegdcb", "fdgba", "bfgacd", "fdcg", "fd", "cbfga", "adf", "ebcagf", "dcfabe", "gbdae"], ["df", "bcaefd", "cfagb", "df"]],
[["cdbgef", "bgef", "ge", "ged", "badec", "agfdcb", "adgecf", "cgdeb", "cbgdf", "fdbceag"], ["dcfgb", "gcebd", "egbf", "dcegb"]],
[["dfbea", "gb", "cfgea", "bag", "fgbc", "debcga", "acdbgef", "afcgbe", "gfeba", "cfdaeg"], ["beafd", "bag", "cbgf", "gba"]],
[["fdgcab", "cd", "ebdaf", "baecdgf", "cda", "bcgaf", "cfebga", "acebgd", "cbdaf", "cfgd"], ["aegcfb", "cdgf", "cdgf", "afegbdc"]],
[["fcbga", "cbeagf", "dcabg", "da", "dfabcg", "bdaf", "begcd", "dca", "fdagce", "bcgfdae"], ["acgbd", "dbceg", "acd", "cfbga"]],
[["degacbf", "cf", "dcgfba", "adegbf", "efgab", "gfce", "acfeb", "dbeca", "caf", "gcebaf"], ["bacfe", "abfecg", "ebafc", "debac"]],
[["bcaefd", "gbce", "dcegfb", "gcbadf", "dgfaecb", "fbdce", "dgcfe", "cg", "agfed", "fcg"], ["dbgfec", "gc", "acdgfb", "efbcd"]],
[["cdfag", "dgebacf", "bdfagc", "fba", "acdgef", "fcdab", "bfdg", "baedc", "gbfaec", "fb"], ["cedbafg", "fb", "dgfeac", "cadbf"]],
[["bcdgf", "eafcbgd", "bd", "adfb", "dcabeg", "gebfac", "gcfba", "gfdacb", "fdgce", "bgd"], ["cfbga", "fgcab", "db", "fcegd"]],
[["cdgafe", "deg", "bedfc", "dfgb", "cgdbe", "dg", "dcefba", "efdgbc", "cagbefd", "cegab"], ["bgdf", "abfdec", "egd", "gedbfc"]],
[["bg", "febdca", "edgcb", "cdeab", "gbc", "edgbca", "gdab", "beagcf", "cdegf", "debacfg"], ["bcaedf", "dgcef", "badg", "fecadbg"]],
[["dbca", "cgaedb", "gcfbe", "cea", "fadbeg", "gabce", "ca", "edcafg", "degab", "abfedgc"], ["fdebag", "beacg", "abcd", "adcegb"]],
[["gcdfe", "adbfgec", "cbafge", "dgbaf", "ebf", "gfbced", "eb", "adcgfe", "becd", "fgebd"], ["ecgfba", "gcbfde", "dbec", "cdafge"]],
[["dbgeafc", "dacbg", "badfge", "abfce", "ed", "eda", "dcfe", "decba", "dcfeab", "gfbeca"], ["febcda", "defc", "beacf", "fdgabe"]],
[["efcd", "bfcadge", "fcdba", "egabf", "bfdcag", "dcefba", "deagbc", "fabed", "ed", "edb"], ["gbeacd", "fdeab", "ebcfad", "fageb"]],
[["dcgf", "fegdab", "bcaeg", "dcegaf", "dga", "gd", "dcfbea", "fcdea", "aedcg", "bdefgca"], ["cbegdfa", "eabcfd", "adfce", "cbefda"]],
[["bf", "edfbgc", "cegbf", "bcadefg", "ebf", "acbfde", "gcedf", "feadgc", "gbcae", "gfbd"], ["feb", "dfgb", "egbcdfa", "dfegc"]],
[["efgba", "eacd", "efadcg", "dcgefb", "gacdf", "dbcfgae", "efd", "bgcdaf", "edfga", "ed"], ["cfbgda", "dgcfa", "gcfead", "eadfg"]],
[["afgdc", "fbg", "cdgaef", "fagbdc", "bgcefa", "cdbf", "bgdaf", "bdaeg", "fb", "dgabcfe"], ["dagfc", "cefagb", "egcabf", "fcbd"]],
[["cadgfe", "acbed", "cfabgde", "fdbcge", "cfga", "fad", "fdeabg", "fa", "dcaef", "dcfge"], ["fad", "bafgecd", "cfegad", "adbfcge"]],
[["agdefc", "cfad", "bdgecfa", "gadfe", "aefgc", "ad", "ceadgb", "gbafce", "bfedg", "agd"], ["dag", "ad", "fcage", "cgbafe"]]]

simple_test_data = [[["acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"], ["cdfeb", "fcadb", "cdfeb", "cdbaf"]]]

#data = simple_test_data

count = 0

digit_map = {}

def count_matching_segments(item: str, target_num: str) -> int:
    return sum([1 for i in digit_map[target_num] if i in item])

def complete_match(item: str, key: str) -> bool:
    return count_matching_segments(item, key) == len(digit_map[key])

def str_sort(key):
    return ''.join(sorted(key))

def get_key(item: str) -> str:
    key = "None"
    if len(item) == 5: # 2, 3, 5
        #3 shares all with 7
        if complete_match(item, "7"):
            key = "3"
        #2 shares 2 with 4
        elif count_matching_segments(item, "4") == 2:
            key = "2"
        else: 
            key = "5"
    elif len(item) == 6: # 0, 6, 9
        #6 is only 6er that does not match with 1
        if not complete_match(item, "1"):
            key = "6"
        #9 shares all with 4
        elif complete_match(item, "4"):
            key = "9"
        else:
            key = "0"
    return key

def get_fixed_keys(input: list) -> None:
    for item in input:
        key = None
        if   len(item) == 7: key = "8"
        elif len(item) == 4: key = "4"
        elif len(item) == 3: key = "7"
        elif len(item) == 2: key = "1"
        else: continue
        digit_map[key] = item

def get_difficult_keys(input: list) -> None:
    for item in input:
        key = get_key(item)
        digit_map[key] = item

def split_inputs(input: list) -> list:
    fixed = []
    special = []
    for item in input:
        if len(item) == 7 \
        or len(item) == 4 \
        or len(item) == 3 \
        or len(item) == 2:
            fixed.append(item)
        else:
            special.append(item)
    return fixed, special

total = 0
for input, output in data:

    input.sort(key=len)
    input = [str_sort(item) for item in input]
    output = [str_sort(item) for item in output]

    fixed, special = split_inputs(input)

    get_fixed_keys(fixed)
    get_difficult_keys(special)

    inverted_mapping = {v: k for k, v in digit_map.items()}
    output_num = ""
    for key in output:
        output_num += inverted_mapping[key]
    total += int(output_num)

print(total)
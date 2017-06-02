from __future__ import division, print_function
import numpy as np
from seq_utils import alphabets


def JTT92(mu=1.0):
    from gtr import GTR
    # stationary concantrations:
    pis = np.array([
        0.07674789,
        0.05169087,
        0.04264509,
        0.05154407,
        0.01980301,
        0.04075195,
        0.06182989,
        0.07315199,
        0.02294399,
        0.05376110,
        0.09190390,
        0.05867583,
        0.02382594,
        0.04012589,
        0.05090097,
        0.06876503,
        0.05856501,
        0.01426057,
        0.03210196,
        0.06600504])

    # attempt matrix (FIXME)
    Q = np.array([
    [-1.247831,0.044229,0.041179,0.061769,0.042704,0.043467,0.08007,0.136501,0.02059,0.027453,0.022877,0.02669,0.041179,0.011439,0.14794,0.288253,0.362223,0.006863,0.008388,0.227247 ],
    [0.029789,-1.025965,0.023112,0.008218,0.058038,0.159218,0.014895,0.070364,0.168463,0.011299,0.019517,0.33179,0.022599,0.002568,0.038007,0.051874,0.032871,0.064714,0.010272,0.008731 ],
    [0.022881,0.019068,-1.280568,0.223727,0.014407,0.03644,0.024576,0.034322,0.165676,0.019915,0.005085,0.11144,0.012712,0.004237,0.006356,0.213134,0.098304,0.00339,0.029661,0.00678 ],
    [0.041484,0.008194,0.270413,-1.044903,0.005121,0.025095,0.392816,0.066579,0.05736,0.005634,0.003585,0.013316,0.007682,0.002049,0.007682,0.030217,0.019462,0.002049,0.023559,0.015877 ],
    [0.011019,0.022234,0.00669,0.001968,-0.56571,0.001771,0.000984,0.011609,0.013577,0.003345,0.004526,0.001377,0.0061,0.015348,0.002755,0.043878,0.008264,0.022628,0.041124,0.012199 ],
    [0.02308,0.125524,0.034823,0.019841,0.003644,-1.04415,0.130788,0.010528,0.241735,0.003644,0.029154,0.118235,0.017411,0.00162,0.066406,0.021461,0.020651,0.007288,0.009718,0.008098 ],
    [0.064507,0.017816,0.035632,0.471205,0.003072,0.198435,-0.944343,0.073107,0.015973,0.007372,0.005529,0.111197,0.011058,0.003072,0.011058,0.01843,0.019659,0.006143,0.0043,0.027646 ],
    [0.130105,0.099578,0.058874,0.09449,0.042884,0.018898,0.086495,-0.647831,0.016717,0.004361,0.004361,0.019625,0.010176,0.003634,0.017444,0.146096,0.023986,0.039976,0.005815,0.034162 ],
    [0.006155,0.074775,0.089138,0.025533,0.01573,0.1361,0.005927,0.005243,-1.135695,0.003648,0.012767,0.010259,0.007523,0.009119,0.026217,0.016642,0.010487,0.001824,0.130629,0.002508 ],
    [0.01923,0.011752,0.025106,0.005876,0.009081,0.004808,0.00641,0.003205,0.008547,-1.273602,0.122326,0.011218,0.25587,0.047542,0.005342,0.021367,0.130873,0.004808,0.017094,0.513342 ],
    [0.027395,0.0347,0.010958,0.006392,0.021003,0.065748,0.008219,0.005479,0.051137,0.209115,-0.668139,0.012784,0.354309,0.226465,0.093143,0.053877,0.022829,0.047485,0.021916,0.16437 ],
    [0.020405,0.376625,0.153332,0.015158,0.004081,0.170239,0.105525,0.015741,0.026235,0.012243,0.008162,-0.900734,0.037896,0.002332,0.012243,0.027401,0.06005,0.00583,0.004664,0.008162 ],
    [0.012784,0.010416,0.007102,0.003551,0.007339,0.01018,0.004261,0.003314,0.007812,0.113397,0.091854,0.015388,-1.182051,0.01018,0.003788,0.006865,0.053503,0.005682,0.004261,0.076466 ],
    [0.00598,0.001993,0.003987,0.001595,0.031098,0.001595,0.001993,0.001993,0.015948,0.035484,0.098877,0.001595,0.017144,-0.637182,0.006778,0.03668,0.004784,0.021131,0.213701,0.024719 ],
    [0.098117,0.037426,0.007586,0.007586,0.007081,0.082944,0.009104,0.012138,0.058162,0.005058,0.051587,0.010621,0.008092,0.008598,-0.727675,0.144141,0.059679,0.003035,0.005058,0.011632 ],
    [0.258271,0.069009,0.343678,0.040312,0.152366,0.036213,0.020498,0.137334,0.049878,0.02733,0.040312,0.032113,0.019814,0.06286,0.194728,-1.447863,0.325913,0.023914,0.043045,0.025964 ],
    [0.276406,0.037242,0.135003,0.022112,0.02444,0.029677,0.018621,0.019203,0.026768,0.142567,0.014548,0.059936,0.131511,0.006983,0.068665,0.27757,-1.335389,0.006983,0.01222,0.065174 ],
    [0.001275,0.017854,0.001134,0.000567,0.016295,0.002551,0.001417,0.007793,0.001134,0.001275,0.007368,0.001417,0.003401,0.00751,0.00085,0.004959,0.0017,-0.312785,0.010061,0.003542 ],
    [0.003509,0.006379,0.022328,0.014673,0.066664,0.007655,0.002233,0.002552,0.182769,0.010207,0.007655,0.002552,0.005741,0.170967,0.00319,0.020095,0.006698,0.022647,-0.605978,0.005103 ],
    [0.195438,0.011149,0.010493,0.020331,0.040662,0.013117,0.029512,0.030824,0.007214,0.630254,0.11805,0.009182,0.211834,0.040662,0.015084,0.024922,0.073453,0.016396,0.010493,-1.241722]
    ])

    Spis = np.sqrt(pis[None, :] / pis[:,None])
    W = Q * Spis

    gtr = GTR(alphabet=alphabets['aa_nogap'])
    gtr.assign_rates(mu=mu, pi=pis, W=W)
    return gtr

_WAG01_pis = np.array([0.0866279,0.043972, 0.0390894,0.0570451,0.0193078,0.0367281,0.0580589,0.0832518,0.0244314,0.048466, 0.086209, 0.0620286,0.0195027,0.0384319,0.0457631,0.0695179,0.0610127,0.0143859,0.0352742,0.0708956])

_WAG01_matrix = np.array([
    [-1.117151, 0.050147, 0.046354, 0.067188, 0.093376, 0.082607, 0.143908, 0.128804, 0.028817, 0.017577, 0.036177, 0.082395, 0.081234, 0.019138, 0.130789, 0.306463, 0.192846, 0.010286, 0.021887, 0.182381],
    [0.025455, -0.974318, 0.029321, 0.006798, 0.024376, 0.140086, 0.020267, 0.026982, 0.098628, 0.008629, 0.022967, 0.246964, 0.031527, 0.004740, 0.031358, 0.056495, 0.025586, 0.053714, 0.017607, 0.011623],
    [0.020916, 0.026065, -1.452438, 0.222741, 0.010882, 0.063328, 0.038859, 0.046176, 0.162306, 0.022737, 0.005396, 0.123567, 0.008132, 0.003945, 0.008003, 0.163042, 0.083283, 0.002950, 0.044553, 0.008051],
    [0.044244, 0.008819, 0.325058, -0.989665, 0.001814, 0.036927, 0.369645, 0.051822, 0.055719, 0.002361, 0.005077, 0.028729, 0.006212, 0.002798, 0.025384, 0.064166, 0.022443, 0.007769, 0.019500, 0.009120],
    [0.020812, 0.010703, 0.005375, 0.000614, -0.487357, 0.002002, 0.000433, 0.006214, 0.005045, 0.003448, 0.007787, 0.001500, 0.007913, 0.008065, 0.002217, 0.028525, 0.010395, 0.014531, 0.011020, 0.020307],
    [0.035023, 0.117008, 0.059502, 0.023775, 0.003809, -1.379785, 0.210830, 0.012722, 0.165524, 0.004391, 0.033516, 0.150135, 0.059565, 0.003852, 0.035978, 0.039660, 0.033070, 0.008316, 0.008777, 0.011613],
    [0.096449, 0.026759, 0.057716, 0.376214, 0.001301, 0.333275, -1.236894, 0.034593, 0.034734, 0.007763, 0.009400, 0.157479, 0.019202, 0.004944, 0.041578, 0.042955, 0.050134, 0.009540, 0.011961, 0.035874],
    [0.123784, 0.051085, 0.098345, 0.075630, 0.026795, 0.028838, 0.049604, -0.497615, 0.021792, 0.002661, 0.005356, 0.032639, 0.015212, 0.004363, 0.021282, 0.117240, 0.019732, 0.029444, 0.009052, 0.016361],
    [0.008127, 0.054799, 0.101443, 0.023863, 0.006384, 0.110105, 0.014616, 0.006395, -0.992342, 0.003543, 0.012807, 0.022832, 0.010363, 0.017420, 0.017851, 0.018979, 0.012136, 0.006733, 0.099319, 0.003035],
    [0.009834, 0.009511, 0.028192, 0.002006, 0.008654, 0.005794, 0.006480, 0.001549, 0.007029, -1.233162, 0.161294, 0.016472, 0.216559, 0.053891, 0.005083, 0.016249, 0.074170, 0.010808, 0.021372, 0.397837],
    [0.036002, 0.045028, 0.011900, 0.007673, 0.034769, 0.078669, 0.013957, 0.005547, 0.045190, 0.286902, -0.726011, 0.023303, 0.439180, 0.191376, 0.037625, 0.031191, 0.029552, 0.060196, 0.036066, 0.162890],
    [0.058998, 0.348377, 0.196082, 0.031239, 0.004820, 0.253558, 0.168246, 0.024319, 0.057967, 0.021081, 0.016767, -1.124580, 0.060821, 0.005783, 0.036254, 0.062960, 0.090292, 0.008952, 0.008675, 0.019884],
    [0.018288, 0.013983, 0.004057, 0.002124, 0.007993, 0.031629, 0.006450, 0.003564, 0.008272, 0.087143, 0.099354, 0.019123, -1.322098, 0.024370, 0.003507, 0.010109, 0.031033, 0.010556, 0.008769, 0.042133],
    [0.008490, 0.004143, 0.003879, 0.001885, 0.016054, 0.004030, 0.003273, 0.002014, 0.027402, 0.042734, 0.085315, 0.003583, 0.048024, -0.713669, 0.006512, 0.022020, 0.006934, 0.061698, 0.260332, 0.026213],
    [0.069092, 0.032635, 0.009370, 0.020364, 0.005255, 0.044829, 0.032773, 0.011698, 0.033438, 0.004799, 0.019973, 0.026747, 0.008229, 0.007754, -0.605590, 0.077484, 0.038202, 0.006695, 0.010376, 0.015124],
    [0.245933, 0.089317, 0.289960, 0.078196, 0.102703, 0.075066, 0.051432, 0.097899, 0.054003, 0.023306, 0.025152, 0.070562, 0.036035, 0.039831, 0.117705, -1.392239, 0.319421, 0.038212, 0.057419, 0.016981],
    [0.135823, 0.035501, 0.129992, 0.024004, 0.032848, 0.054936, 0.052685, 0.014461, 0.030308, 0.093371, 0.020915, 0.088814, 0.097083, 0.011008, 0.050931, 0.280341, -1.154973, 0.007099, 0.018643, 0.088894],
    [0.001708, 0.017573, 0.001086, 0.001959, 0.010826, 0.003257, 0.002364, 0.005088, 0.003964, 0.003208, 0.010045, 0.002076, 0.007786, 0.023095, 0.002105, 0.007908, 0.001674, -0.466694, 0.037525, 0.005516],
    [0.008912, 0.014125, 0.040205, 0.012058, 0.020133, 0.008430, 0.007267, 0.003836, 0.143398, 0.015555, 0.014757, 0.004934, 0.015861, 0.238943, 0.007998, 0.029135, 0.010779, 0.092011, -0.726275, 0.011652],
    [0.149259, 0.018739, 0.014602, 0.011335, 0.074565, 0.022417, 0.043805, 0.013932, 0.008807, 0.581952, 0.133956, 0.022726, 0.153161, 0.048356, 0.023429, 0.017317, 0.103293, 0.027186, 0.023418, -1.085487]
    ])


_BLOSUM45 = np.array([
        [0, 1.31097856157468, 1.06573001937323, 1.2682782988532, 0.90471293383305, 1.05855446876905, 1.05232790675508, 0.769574440593014, 1.27579668305679, 0.964604099952603, 0.987178199640556, 1.05007594438157, 1.05464162250736, 1.1985987403937, 0.967404475245526, 0.700490199584332, 0.880060189098976, 1.09748548316685, 1.28141710375267, 0.800038509951648],
        [1.31097856157468, 0, 0.8010890222701, 0.953340718498495, 1.36011107208122, 0.631543775840481, 0.791014908659279, 1.15694899265629, 0.761152570032029, 1.45014917711188, 1.17792001455227, 0.394661075648738, 0.998807558909651, 1.135143404599, 1.15432562628921, 1.05309036790541, 1.05010474413616, 1.03938321130789, 0.963216908696184, 1.20274751778601],
        [1.06573001937323, 0.8010890222701, 0, 0.488217214273568, 1.10567116937273, 0.814970207038261, 0.810176440932339, 0.746487413974582, 0.61876156253224, 1.17886558630004, 1.52003670190022, 0.808442678243754, 1.2889025816028, 1.16264109995678, 1.18228799147301, 0.679475681649858, 0.853658619686283, 1.68988558988005, 1.24297493464833, 1.55207513886163],
        [1.2682782988532, 0.953340718498495, 0.488217214273568, 0, 1.31581050011876, 0.769778474953791, 0.482077627352988, 0.888361752320536, 0.736360849050364, 1.76756333403346, 1.43574761894039, 0.763612910719347, 1.53386612356483, 1.74323672079854, 0.886347403928663, 0.808614044804528, 1.01590147813779, 1.59617804551619, 1.1740494822217, 1.46600946033173],
        [0.90471293383305, 1.36011107208122, 1.10567116937273, 1.31581050011876, 0, 1.3836789310481, 1.37553994252576, 1.26740695314856, 1.32361065635259, 1.26087264215993, 1.02417540515351, 1.37259631233791, 1.09416720447891, 0.986982088723923, 1.59321190226694, 0.915638787768407, 0.913042853922533, 1.80744143643002, 1.3294417177004, 0.830022143283238],
        [1.05855446876905, 0.631543775840481, 0.814970207038261, 0.769778474953791, 1.3836789310481, 0, 0.506942797642807, 1.17699648087288, 0.614595446514896, 1.17092829494457, 1.19833088638994, 0.637341078675405, 0.806490842729072, 1.83315144709714, 0.932064479113502, 0.850321696813199, 1.06830084665916, 1.05739353225849, 0.979907428113788, 1.5416250309563],
        [1.05232790675508, 0.791014908659279, 0.810176440932339, 0.482077627352988, 1.37553994252576, 0.506942797642807, 0, 1.17007322676118, 0.769786956320484, 1.46659942462342, 1.19128214039009, 0.633592151371708, 1.27269395724349, 1.44641491621774, 0.735428579892476, 0.845319988414402, 1.06201695511881, 1.324395996498, 1.22734387448031, 1.53255698189437],
        [0.769574440593014, 1.15694899265629, 0.746487413974582, 0.888361752320536, 1.26740695314856, 1.17699648087288, 1.17007322676118, 0, 1.1259007054424, 1.7025415585924, 1.38293205218175, 1.16756929156758, 1.17264582493965, 1.33271035269688, 1.07564768421292, 0.778868281341681, 1.23287107008366, 0.968539655354582, 1.42479529031801, 1.41208067821187],
        [1.27579668305679, 0.761152570032029, 0.61876156253224, 0.736360849050364, 1.32361065635259, 0.614595446514896, 0.769786956320484, 1.1259007054424, 0, 1.4112324673522, 1.14630894167097, 0.967795284542623, 0.771479459384692, 1.10468029976148, 1.12334774065132, 1.02482926701639, 1.28754326478771, 1.27439749294131, 0.468683841672724, 1.47469999960758],
        [0.964604099952603, 1.45014917711188, 1.17886558630004, 1.76756333403346, 1.26087264215993, 1.17092829494457, 1.46659942462342, 1.7025415585924, 1.4112324673522, 0, 0.433350517223017, 1.463460928818, 0.462965544381851, 0.66291968000662, 1.07010201755441, 1.23000200130049, 0.973485453109068, 0.963546200571036, 0.708724769805536, 0.351200119909572],
        [0.987178199640556, 1.17792001455227, 1.52003670190022, 1.43574761894039, 1.02417540515351, 1.19833088638994, 1.19128214039009, 1.38293205218175, 1.14630894167097, 0.433350517223017, 0, 1.49770950074319, 0.473800072611076, 0.538473125003292, 1.37979627224964, 1.5859723170438, 0.996267398224516, 0.986095542821092, 0.725310666139274, 0.570542199221932],
        [1.05007594438157, 0.394661075648738, 0.808442678243754, 0.763612910719347, 1.37259631233791, 0.637341078675405, 0.633592151371708, 1.16756929156758, 0.967795284542623, 1.463460928818, 1.49770950074319, 0, 1.0079761868248, 1.44331961488922, 0.924599080166146, 1.06275728888356, 1.05974425835993, 1.04892430642749, 0.972058829603409, 1.21378822764856],
        [1.05464162250736, 0.998807558909651, 1.2889025816028, 1.53386612356483, 1.09416720447891, 0.806490842729072, 1.27269395724349, 1.17264582493965, 0.771479459384692, 0.462965544381851, 0.473800072611076, 1.0079761868248, 0, 0.72479754849538, 1.1699868662153, 1.34481214251794, 1.06435197383538, 1.05348497728858, 0.774878150710318, 0.609532859331199],
        [1.1985987403937, 1.135143404599, 1.16264109995678, 1.74323672079854, 0.986982088723923, 1.83315144709714, 1.44641491621774, 1.33271035269688, 1.10468029976148, 0.66291968000662, 0.538473125003292, 1.44331961488922, 0.72479754849538, 0, 1.32968844979665, 1.21307373491949, 0.960087571600877, 0.475142555482979, 0.349485367759138, 0.692733248746636],
        [0.967404475245526, 1.15432562628921, 1.18228799147301, 0.886347403928663, 1.59321190226694, 0.932064479113502, 0.735428579892476, 1.07564768421292, 1.12334774065132, 1.07010201755441, 1.37979627224964, 0.924599080166146, 1.1699868662153, 1.32968844979665, 0, 0.979087429691819, 0.97631161216338, 1.21751652292503, 1.42156458605332, 1.40887880416009],
        [0.700490199584332, 1.05309036790541, 0.679475681649858, 0.808614044804528, 0.915638787768407, 0.850321696813199, 0.845319988414402, 0.778868281341681, 1.02482926701639, 1.23000200130049, 1.5859723170438, 1.06275728888356, 1.34481214251794, 1.21307373491949, 0.979087429691819, 0, 0.56109848274013, 1.76318885009194, 1.29689226231656, 1.02015839286433],
        [0.880060189098976, 1.05010474413616, 0.853658619686283, 1.01590147813779, 0.913042853922533, 1.06830084665916, 1.06201695511881, 1.23287107008366, 1.28754326478771, 0.973485453109068, 0.996267398224516, 1.05974425835993, 1.06435197383538, 0.960087571600877, 0.97631161216338, 0.56109848274013, 0, 1.39547634461879, 1.02642577026706, 0.807404666228614],
        [1.09748548316685, 1.03938321130789, 1.68988558988005, 1.59617804551619, 1.80744143643002, 1.05739353225849, 1.324395996498, 0.968539655354582, 1.27439749294131, 0.963546200571036, 0.986095542821092, 1.04892430642749, 1.05348497728858, 0.475142555482979, 1.21751652292503, 1.76318885009194, 1.39547634461879, 0, 0.320002937404137, 1.268589159299],
        [1.28141710375267, 0.963216908696184, 1.24297493464833, 1.1740494822217, 1.3294417177004, 0.979907428113788, 1.22734387448031, 1.42479529031801, 0.468683841672724, 0.708724769805536, 0.725310666139274, 0.972058829603409, 0.774878150710318, 0.349485367759138, 1.42156458605332, 1.29689226231656, 1.02642577026706, 0.320002937404137, 0, 0.933095433689795],
        [0.800038509951648, 1.20274751778601, 1.55207513886163, 1.46600946033173, 0.830022143283238, 1.5416250309563, 1.53255698189437, 1.41208067821187, 1.47469999960758, 0.351200119909572, 0.570542199221932, 1.21378822764856, 0.609532859331199, 0.692733248746636, 1.40887880416009, 1.02015839286433, 0.807404666228614, 1.268589159299, 0.933095433689795]
    ])

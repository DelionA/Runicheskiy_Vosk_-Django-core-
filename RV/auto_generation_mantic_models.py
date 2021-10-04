# scrypt for auto create objects for ManticKeys

from .models import ManticKeys

set_ = {'hagalazraido', 'fehunauthiz', 'fehuehwaz', 'thurisazpertho', 'eihwazisa', 'dagazinguz', 'wunjoisa', 'raidogebo', 'gebomannaz', 'gebohagalaz', 'nauthizodal', 'fehusoulo', 'ansuzkaunaz', 'raidopertho', 'uruzkaunaz', 'pertholaguz', 'berkanadagaz', 'geboalgiz', 'laguzpertho', 'perthowunjo', 'algizmannaz', 'teiwazisa', 'mannazgebo', 'berkanawunjo', 'uruzwunjo', 'soulojera', 'thurisazteiwaz', 'souloteiwaz', 'thurisazjera', 'perthoraido', 'jeraalgiz', 'mannazkaunaz', 'algizwunjo', 'algizehwaz', 'ansuzgebo', 'teiwazansuz', 'soulonauthiz', 'wunjoalgiz', 'algizisa', 'berkanaisa', 'eihwazraido', 'nauthizteiwaz', 'algizlaguz', 'kaunazpertho', 'laguzalgiz', 'fehuberkana', 'uruzfehu', 'souloinguz', 'inguzjera', 'isathurisaz', 'ehwazgebo', 'soulofehu', 'inguzodal', 'ansuzmannaz', 'teiwazjera', 'inguzkaunaz', 'souloberkana', 'thurisaznauthiz', 'geboraido', 'fehuraido', 'jeraraido', 'eihwazehwaz', 'laguzthurisaz', 'wunjopertho', 'inguzehwaz', 'soulopertho', 'inguzfehu', 'teiwazberkana', 'thurisazdagaz', 'kaunazsoulo', 'jerawunjo', 'kaunazdagaz', 'uruzraido', 'isanauthiz', 'fehuinguz', 'kaunazraido', 'dagazgebo', 'wunjodagaz', 'odalfehu', 'kaunazberkana', 'berkanathurisaz', 'raidothurisaz', 'isaalgiz', 'jeraberkana', 'wunjomannaz', 'mannazjera', 'algizteiwaz', 'mannazansuz', 'ansuzthurisaz', 'gebosoulo', 'inguzgebo', 'odaleihwaz', 'jeraodal', 'gebonauthiz', 'geboisa', 'eihwazdagaz', 'inguzisa', 'uruzeihwaz', 'eihwazkaunaz', 'nauthizeihwaz', 'isainguz', 'nauthizisa', 'kaunazgebo', 'ansuzteiwaz', 'teiwazsoulo', 'odaldagaz', 'wunjohagalaz', 'perthouruz', 'raidonauthiz', 'geboeihwaz', 'jeramannaz', 'inguzdagaz', 'teiwazeihwaz', 'souloalgiz', 'berkanahagalaz', 'ehwazisa', 'hagalazuruz', 'perthodagaz', 'raidoinguz', 'mannaznauthiz', 'laguzmannaz', 'thurisazeihwaz', 'perthogebo', 'uruzberkana', 'nauthizfehu', 'teiwazuruz', 'fehudagaz', 'perthokaunaz', 'teiwazodal', 'perthoteiwaz', 'wunjoansuz', 'mannazuruz', 'gebolaguz', 'dagazalgiz', 'jerapertho', 'uruzansuz', 'jerahagalaz', 'isafehu', 'dagazkaunaz', 'perthonauthiz', 'berkanamannaz', 'uruzehwaz', 'thurisazehwaz', 'ehwazthurisaz', 'dagazhagalaz', 'algizberkana', 'jerakaunaz', 'jerauruz', 'wunjoberkana', 'gebokaunaz', 'soulohagalaz', 'geboansuz', 'kaunazalgiz', 'soulolaguz', 'ehwazmannaz', 'teiwazkaunaz', 'uruzteiwaz', 'hagalazehwaz', 'isauruz', 'odalraido', 'odaluruz', 'kaunazansuz', 'wunjojera', 'mannazisa', 'isateiwaz', 'kaunazjera', 'jeraisa', 'ansuzfehu', 'laguzkaunaz', 'berkanaeihwaz', 'thurisazuruz', 'hagalazteiwaz', 'teiwazehwaz', 'thurisazlaguz', 'odalansuz', 'uruzisa', 'dagazwunjo', 'souloodal', 'dagazodal', 'wunjoinguz', 'odalwunjo', 'inguzuruz', 'fehuteiwaz', 'fehuuruz', 'geboehwaz', 'laguzansuz', 'algizansuz', 'berkanaodal', 'inguzthurisaz', 'isahagalaz', 'odalkaunaz', 'odalehwaz', 'algizpertho', 'odalnauthiz', 'fehuisa', 'souloehwaz', 'geboinguz', 'kaunazmannaz', 'ehwazansuz', 'algizuruz', 'wunjoodal', 'perthoalgiz', 'fehujera', 'inguzhagalaz', 'thurisazwunjo', 'raidolaguz', 'mannazberkana', 'hagalazinguz', 'laguzodal', 'gebothurisaz', 'uruzhagalaz', 'odalmannaz', 'raidoteiwaz', 'hagalazgebo', 'teiwazraido', 'eihwazhagalaz', 'gebofehu', 'dagazuruz', 'eihwazthurisaz', 'teiwazlaguz', 'fehualgiz', 'perthoansuz', 'ansuzodal', 'fehulaguz', 'jerainguz', 'dagazehwaz', 'kaunazisa', 'ansuzpertho', 'inguzpertho', 'jerafehu', 'wunjosoulo', 'thurisazmannaz', 'teiwazdagaz', 'thurisazinguz', 'ehwazpertho', 'nauthizberkana', 'thurisazhagalaz', 'soulodagaz', 'laguzhagalaz', 'uruzsoulo', 'odalinguz', 'eihwazansuz', 'soulothurisaz', 'odalteiwaz', 'kaunazthurisaz', 'fehuhagalaz', 'nauthizraido', 'algizhagalaz', 'eihwazsoulo', 'wunjothurisaz', 'mannazwunjo', 'kaunazwunjo', 'algizraido', 'ehwazodal', 'algizdagaz', 'nauthizsoulo', 'inguzraido', 'souloraido', 'nauthizalgiz', 'dagazjera', 'algizkaunaz', 'mannazsoulo', 'mannazhagalaz', 'fehuodal', 'ansuznauthiz', 'algizodal', 'nauthizhagalaz', 'jeralaguz', 'teiwaznauthiz', 'mannazodal', 'hagalazmannaz', 'jeraeihwaz', 'eihwaznauthiz', 'isagebo', 'jerathurisaz', 'thurisazsoulo', 'algiznauthiz', 'berkanagebo', 'gebopertho', 'ehwazkaunaz', 'teiwazthurisaz', 'perthoisa', 'dagazlaguz', 'uruzodal', 'eihwazodal', 'raidosoulo', 'ehwazwunjo', 'ehwazraido', 'perthoodal', 'perthosoulo', 'ehwazteiwaz', 'hagalazpertho', 'jeranauthiz', 'nauthizlaguz', 'inguzmannaz', 'nauthizuruz', 'dagazthurisaz', 'algizthurisaz', 'nauthizehwaz', 'odalpertho', 'ehwazhagalaz', 'berkanateiwaz', 'perthoinguz', 'raidoalgiz', 'odalalgiz', 'ehwazeihwaz', 'laguzberkana', 'ansuzeihwaz', 'ansuzehwaz', 'mannazfehu', 'laguzwunjo', 'fehumannaz', 'inguzansuz', 'wunjolaguz', 'isaehwaz', 'hagalazeihwaz', 'algizinguz', 'dagazberkana', 'teiwazhagalaz', 'isakaunaz', 'ehwazuruz', 'uruzlaguz', 'perthothurisaz', 'thurisazisa', 'raidouruz', 'isadagaz', 'inguzalgiz', 'laguzehwaz', 'berkanainguz', 'wunjokaunaz', 'jerateiwaz', 'hagalazkaunaz', 'nauthizthurisaz', 'nauthizpertho', 'ehwazberkana', 'raidoisa', 'thurisazraido', 'berkanakaunaz', 'mannazteiwaz', 'raidoehwaz', 'ansuzjera', 'raidoodal', 'hagalazjera', 'odalhagalaz', 'inguzwunjo', 'eihwazberkana', 'uruzthurisaz', 'odalgebo', 'eihwazwunjo', 'laguzinguz', 'ansuzberkana', 'ehwazinguz', 'jeraansuz', 'mannazinguz', 'isaansuz', 'algizjera', 'kaunazeihwaz', 'ehwazdagaz', 'dagazteiwaz', 'berkanaalgiz', 'inguzberkana', 'laguzuruz', 'isajera', 'raidohagalaz', 'fehupertho', 'ansuzlaguz', 'raidoeihwaz', 'odallaguz', 'souloisa', 'soulomannaz', 'raidojera', 'fehukaunaz', 'fehuthurisaz', 'dagazfehu', 'dagaznauthiz', 'mannazeihwaz', 'dagazeihwaz', 'teiwazwunjo', 'isaraido', 'teiwazalgiz', 'dagazraido', 'teiwazmannaz', 'nauthizgebo', 'uruznauthiz', 'laguzjera', 'dagazisa', 'nauthizansuz', 'nauthizjera', 'gebojera', 'dagazpertho', 'fehuansuz', 'eihwazjera', 'thurisazberkana', 'inguzsoulo', 'teiwazgebo', 'hagalazisa', 'isaodal', 'laguzfehu', 'perthomannaz', 'jeraehwaz', 'thurisazgebo', 'perthoberkana', 'wunjoraido', 'soulowunjo', 'kaunazfehu', 'berkanasoulo', 'berkananauthiz', 'dagazmannaz', 'odalsoulo', 'uruzmannaz', 'wunjouruz', 'kaunazlaguz', 'inguzlaguz', 'eihwazgebo', 'soulogebo', 'raidofehu', 'gebodagaz', 'berkanafehu', 'ansuzisa', 'kaunazinguz', 'thurisazodal', 'ehwazjera', 'raidoberkana', 'laguznauthiz', 'hagalazdagaz', 'thurisazfehu', 'ehwazsoulo', 'laguzgebo', 'hagalazalgiz', 'nauthizkaunaz', 'nauthizdagaz', 'uruzinguz', 'raidomannaz', 'kaunazuruz', 'raidoansuz', 'berkanaehwaz', 'ansuzwunjo', 'wunjoteiwaz', 'ansuzsoulo', 'dagazsoulo', 'algizsoulo', 'ehwazfehu', 'nauthizinguz', 'mannazdagaz', 'mannazalgiz', 'ansuzuruz', 'laguzraido', 'hagalazansuz', 'hagalazsoulo', 'dagazansuz', 'algizfehu', 'eihwazteiwaz', 'kaunazehwaz', 'laguzteiwaz', 'gebouruz', 'hagalazberkana', 'odalthurisaz', 'berkanaansuz', 'ansuzhagalaz', 'isamannaz', 'laguzisa', 'eihwazpertho', 'uruzalgiz', 'isaberkana', 'souloeihwaz', 'laguzdagaz', 'nauthizmannaz', 'uruzjera', 'perthoehwaz', 'teiwazfehu', 'ansuzinguz', 'hagalaznauthiz', 'berkanapertho', 'soulokaunaz', 'soulouruz', 'berkanalaguz', 'teiwazpertho', 'thurisazansuz', 'isalaguz', 'ehwaznauthiz', 'laguzeihwaz', 'ansuzdagaz', 'wunjoehwaz', 'odalberkana', 'berkanaraido', 'kaunazhagalaz', 'uruzpertho', 'perthofehu', 'eihwazmannaz', 'kaunazodal', 'hagalazodal', 'inguzteiwaz', 'thurisazalgiz', 'wunjoeihwaz', 'mannazpertho', 'hagalazthurisaz', 'mannazthurisaz', 'geboodal', 'hagalazlaguz', 'kaunaznauthiz', 'ehwazalgiz', 'nauthizwunjo', 'isaeihwaz', 'fehugebo', 'eihwazlaguz', 'jeradagaz', 'thurisazkaunaz', 'odaljera', 'eihwazfehu', 'isapertho', 'algizgebo', 'mannazlaguz', 'raidowunjo', 'isasoulo', 'uruzgebo', 'berkanauruz', 'raidokaunaz', 'inguznauthiz', 'uruzdagaz', 'ansuzraido', 'eihwazuruz', 'fehuwunjo', 'geboteiwaz', 'ansuzalgiz', 'hagalazfehu', 'odalisa', 'ehwazlaguz', 'souloansuz', 'mannazraido', 'wunjogebo', 'kaunazteiwaz', 'perthoeihwaz', 'gebowunjo', 'eihwazinguz', 'jeragebo', 'inguzeihwaz', 'perthohagalaz', 'fehueihwaz', 'hagalazwunjo', 'isawunjo', 'raidodagaz', 'mannazehwaz', 'teiwazinguz', 'eihwazalgiz', 'algizeihwaz', 'wunjonauthiz', 'jerasoulo', 'laguzsoulo', 'berkanajera', 'wunjofehu', 'perthojera', 'geboberkana'}

def auto_create_func(set_):
    for i in set_:
        value_keys = i
        value_name = i
        value_mantic = "{} значение в мантике".format(i)
        value_protection = "{} значение в сфере защиты".format(i)
        obj_mk = ManticKeys.objects.create(**{'value_keys':value_keys,'value_name':value_name,'value_mantic':value_mantic,'value_protection':value_protection})


##
# заполнять мантические определения буду модудями
# модуль = Руна
# после заполнения модуля внесение информации в базу, в модель ManticKeys
# блок будет состоять из кортежа (value_keys, value_name, value_mantic, value_protection)
# 

# value_keys 'fehuuruz'
# value_name 'Феху - Уруз'

# value_mantic
# value_protection

# 'fehuuruz',
# 'fehuthurisaz',
# 'fehuansuz',
# 'fehuraido',
# 'fehukaunaz',
# 'fehugebo',
# 'fehuwunjo',
# 'fehuhagalaz',
# 'fehunauthiz',
# 'fehuisa',
# 'fehujera',
# 'fehueihwaz',
# 'fehupertho',
# 'fehualgiz',
# 'fehusoulo',
# 'fehuteiwaz',
# 'fehuberkana',
# 'fehuehwaz',
# 'fehumannaz',
# 'fehulaguz',
# 'fehuinguz',
# 'fehudagaz',
# 'fehuodal',

#this code has been transcoded using the "js2py" repository
__all__ = ['blowfish']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['KeySetup', 'fp_VideoCard', 'decrypt', '_longToStr', 'fp_mimetypen', 'fp_webgl', 'fp_display', '_strToLong', 'block_encrypt', 'fp_canvas', 'fp_os', 'createhash', 'fp_useragent', 'sha256', 'fp_flash', 'fp_timezone', 'fp_plugins', 'Base64Decode', 'base64ToAscii', 'fp_cookie', 'Base64Encode', 'encrypt', 'kzbrid', 'fp_fonts', 'block_decrypt', 'fp_browser', 'fp_language', 'fp_java'])
@Js
def PyJsHoisted_encrypt_(key, str, this, arguments, var=var):
    var = Scope({'key':key, 'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['xl_old', 'key', 'i', 'out', 'str', 'xr_old', 'len', 'x'])
    if ((var.get('key_old')==var.get(u"null")) or (var.get('key')!=var.get('key_old'))):
        var.get('KeySetup')(var.get('key'))
        var.put('key_old', var.get('key'))
    var.put('out', Js(''))
    while ((var.get('str').get('length')%Js(8.0))>Js(0.0)):
        var.put('str', Js(' '), '+')
    var.put('len', var.get('str').get('length'))
    var.put('xl_old', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(1000000.0))))
    var.put('xr_old', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(1000000.0))))
    var.put('out', var.get('_longToStr')(var.get('Array')(var.get('xl_old'), var.get('xr_old'))), '+')
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('len')):
        try:
            var.put('x', var.get('_strToLong')(var.get('str').callprop('substr', var.get('i'), Js(8.0))))
            var.put('x', var.get('block_encrypt')((var.get('x').get('0')^var.get('xl_old')), (var.get('x').get('1')^var.get('xr_old'))))
            var.put('xl_old', var.get('x').get('0'))
            var.put('xr_old', var.get('x').get('1'))
            var.put('out', var.get('_longToStr')(var.get('x')), '+')
        finally:
                var.put('i', Js(8.0), '+')
    return var.get('Base64Encode')(var.get('out'))
PyJsHoisted_encrypt_.func_name = 'encrypt'
var.put('encrypt', PyJsHoisted_encrypt_)
@Js
def PyJsHoisted_decrypt_(key, str, this, arguments, var=var):
    var = Scope({'key':key, 'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['xl_old', 'key', 'i', 'out', 'str', 'xr_old', 'tmp', 'len', 'x'])
    if ((var.get('key_old')==var.get(u"null")) or (var.get('key')!=var.get('key_old'))):
        var.get('KeySetup')(var.get('key'))
        var.put('key_old', var.get('key'))
    var.put('str', var.get('Base64Decode')(var.get('str')))
    var.put('out', Js(''))
    var.put('len', var.get('str').get('length'))
    var.put('x', var.get('_strToLong')(var.get('str').callprop('substr', Js(0.0), Js(8.0))))
    var.put('xl_old', var.get('x').get('0'))
    var.put('xr_old', var.get('x').get('1'))
    var.put('tmp', var.get('Array')())
    #for JS loop
    var.put('i', Js(8.0))
    while (var.get('i')<var.get('len')):
        try:
            var.put('x', var.get('_strToLong')(var.get('str').callprop('substr', var.get('i'), Js(8.0))))
            var.get('tmp').put('0', var.get('x').get('0'))
            var.get('tmp').put('1', var.get('x').get('1'))
            var.put('x', var.get('block_decrypt')(var.get('x').get('0'), var.get('x').get('1')))
            var.get('x').put('0', var.get('xl_old'), '^')
            var.get('x').put('1', var.get('xr_old'), '^')
            var.put('xl_old', var.get('tmp').get('0'))
            var.put('xr_old', var.get('tmp').get('1'))
            var.put('out', var.get('_longToStr')(var.get('x')), '+')
        finally:
                var.put('i', Js(8.0), '+')
    return var.get('out')
PyJsHoisted_decrypt_.func_name = 'decrypt'
var.put('decrypt', PyJsHoisted_decrypt_)
@Js
def PyJsHoisted_KeySetup_(key, this, arguments, var=var):
    var = Scope({'key':key, 'this':this, 'arguments':arguments}, var)
    var.registers(['j', 'keyArray', 'key_item', 'key', 'k', 'i', 'v'])
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(256.0)):
        try:
            var.get('sbox0').put(var.get('i'), var.get('sbox0_def').get(var.get('i')))
            var.get('sbox1').put(var.get('i'), var.get('sbox1_def').get(var.get('i')))
            var.get('sbox2').put(var.get('i'), var.get('sbox2_def').get(var.get('i')))
            var.get('sbox3').put(var.get('i'), var.get('sbox3_def').get(var.get('i')))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('keyArray', var.get('Array')(Js(0.0)))
    var.put('j', Js(0.0))
    var.put('k', Js(0.0))
    var.put('key_item', Js(0.0))
    #for JS loop
    var.put('j', Js(0.0))
    var.put('i', Js(0.0))
    while (var.get('j')<var.get('key').get('length')):
        try:
            var.put('key_item', Js(0.0))
            #for JS loop
            var.put('k', Js(0.0))
            while (var.get('k')<Js(4.0)):
                try:
                    var.put('key_item', ((var.get('key_item')<<Js(8.0))|var.get('key').callprop('charCodeAt', (var.get('j')%var.get('key').get('length')))))
                    (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                finally:
                        (var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1))
            var.get('keyArray').put(var.get('i'), var.get('key_item'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(18.0)):
        try:
            var.get('pbox').put(var.get('i'), (var.get('pbox_def').get(var.get('i'))^var.get('keyArray').get((var.get('i')%var.get('keyArray').get('length')))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('v', var.get('Array')())
    var.get('v').put('0', var.get('v').put('1', Js(0.0)))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(18.0)):
        try:
            var.put('v', var.get('block_encrypt')(var.get('v').get('0'), var.get('v').get('1')))
            var.get('pbox').put(var.get('i'), var.get('v').get('0'))
            var.get('pbox').put((var.get('i')+Js(1.0)), var.get('v').get('1'))
        finally:
                var.put('i', Js(2.0), '+')
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(256.0)):
        try:
            var.put('v', var.get('block_encrypt')(var.get('v').get('0'), var.get('v').get('1')))
            var.get('sbox0').put(var.get('i'), var.get('v').get('0'))
            var.get('sbox0').put((var.get('i')+Js(1.0)), var.get('v').get('1'))
        finally:
                var.put('i', Js(2.0), '+')
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(256.0)):
        try:
            var.put('v', var.get('block_encrypt')(var.get('v').get('0'), var.get('v').get('1')))
            var.get('sbox1').put(var.get('i'), var.get('v').get('0'))
            var.get('sbox1').put((var.get('i')+Js(1.0)), var.get('v').get('1'))
        finally:
                var.put('i', Js(2.0), '+')
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(256.0)):
        try:
            var.put('v', var.get('block_encrypt')(var.get('v').get('0'), var.get('v').get('1')))
            var.get('sbox2').put(var.get('i'), var.get('v').get('0'))
            var.get('sbox2').put((var.get('i')+Js(1.0)), var.get('v').get('1'))
        finally:
                var.put('i', Js(2.0), '+')
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(256.0)):
        try:
            var.put('v', var.get('block_encrypt')(var.get('v').get('0'), var.get('v').get('1')))
            var.get('sbox3').put(var.get('i'), var.get('v').get('0'))
            var.get('sbox3').put((var.get('i')+Js(1.0)), var.get('v').get('1'))
        finally:
                var.put('i', Js(2.0), '+')
PyJsHoisted_KeySetup_.func_name = 'KeySetup'
var.put('KeySetup', PyJsHoisted_KeySetup_)
@Js
def PyJsHoisted_block_encrypt_(vl, vr, this, arguments, var=var):
    var = Scope({'vl':vl, 'vr':vr, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'v_tmp', 'vl', 'vr'])
    var.put('v_tmp', Js(0.0))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(16.0)):
        try:
            var.put('vl', var.get('pbox').get(var.get('i')), '^')
            var.put('vr', (((var.get('sbox0').get((PyJsBshift(var.get('vl'),Js(24.0))&Js(255)))+var.get('sbox1').get((PyJsBshift(var.get('vl'),Js(16.0))&Js(255))))^var.get('sbox2').get((PyJsBshift(var.get('vl'),Js(8.0))&Js(255))))+var.get('sbox3').get((var.get('vl')&Js(255)))), '^')
            var.put('v_tmp', var.get('vl'))
            var.put('vl', var.get('vr'))
            var.put('vr', var.get('v_tmp'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('v_tmp', var.get('vl'))
    var.put('vl', var.get('vr'))
    var.put('vr', var.get('v_tmp'))
    var.put('vr', var.get('pbox').get('16'), '^')
    var.put('vl', var.get('pbox').get('17'), '^')
    return var.get('Array')(var.get('vl'), var.get('vr'))
PyJsHoisted_block_encrypt_.func_name = 'block_encrypt'
var.put('block_encrypt', PyJsHoisted_block_encrypt_)
@Js
def PyJsHoisted_block_decrypt_(vl, vr, this, arguments, var=var):
    var = Scope({'vl':vl, 'vr':vr, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'vl', 'vr'])
    #for JS loop
    var.put('i', Js(17.0))
    while (var.get('i')>Js(1.0)):
        try:
            var.put('vl', var.get('pbox').get(var.get('i')), '^')
            var.put('vr', (((var.get('sbox0').get((PyJsBshift(var.get('vl'),Js(24.0))&Js(255)))+var.get('sbox1').get((PyJsBshift(var.get('vl'),Js(16.0))&Js(255))))^var.get('sbox2').get((PyJsBshift(var.get('vl'),Js(8.0))&Js(255))))+var.get('sbox3').get((var.get('vl')&Js(255)))), '^')
            var.put('v_tmp', var.get('vl'))
            var.put('vl', var.get('vr'))
            var.put('vr', var.get('v_tmp'))
        finally:
                (var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))
    var.put('v_tmp', var.get('vl'))
    var.put('vl', var.get('vr'))
    var.put('vr', var.get('v_tmp'))
    var.put('vr', var.get('pbox').get('1'), '^')
    var.put('vl', var.get('pbox').get('0'), '^')
    return var.get('Array')(var.get('vl'), var.get('vr'))
PyJsHoisted_block_decrypt_.func_name = 'block_decrypt'
var.put('block_decrypt', PyJsHoisted_block_decrypt_)
@Js
def PyJsHoisted__strToLong_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['len', 'i', 'a', 'str'])
    var.put('a', var.get('Array').create())
    var.put('len', var.get('Math').callprop('ceil', (var.get('str').get('length')/Js(4.0))))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('len')):
        try:
            var.get('a').put(var.get('i'), (((var.get('str').callprop('charCodeAt', ((var.get('i')<<Js(2.0))+Js(3.0)))+(var.get('str').callprop('charCodeAt', ((var.get('i')<<Js(2.0))+Js(2.0)))<<Js(8.0)))+(var.get('str').callprop('charCodeAt', ((var.get('i')<<Js(2.0))+Js(1.0)))<<Js(16.0)))+(var.get('str').callprop('charCodeAt', (var.get('i')<<Js(2.0)))<<Js(24.0))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('a')
PyJsHoisted__strToLong_.func_name = '_strToLong'
var.put('_strToLong', PyJsHoisted__strToLong_)
@Js
def PyJsHoisted__longToStr_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['len', 'i', 'a'])
    var.put('len', var.get('a').get('length'))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('len')):
        try:
            var.get('a').put(var.get('i'), var.get('String').callprop('fromCharCode', (PyJsBshift(var.get('a').get(var.get('i')),Js(24.0))&Js(255)), (PyJsBshift(var.get('a').get(var.get('i')),Js(16.0))&Js(255)), (PyJsBshift(var.get('a').get(var.get('i')),Js(8.0))&Js(255)), (var.get('a').get(var.get('i'))&Js(255))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('a').callprop('join', Js(''))
PyJsHoisted__longToStr_.func_name = '_longToStr'
var.put('_longToStr', PyJsHoisted__longToStr_)
@Js
def PyJsHoisted_Base64Encode_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['octet', 'sextet', 'i', 'leftovers', 'str', 'result'])
    var.put('result', Js(''))
    var.put('i', Js(0.0))
    var.put('sextet', Js(0.0))
    var.put('leftovers', Js(0.0))
    var.put('octet', Js(0.0))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('str').get('length')):
        try:
            var.put('octet', var.get('str').callprop('charCodeAt', var.get('i')))
            while 1:
                SWITCHED = False
                CONDITION = ((var.get('i')%Js(3.0)))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                    SWITCHED = True
                    var.put('sextet', ((var.get('octet')&Js(252))>>Js(2.0)))
                    var.put('leftovers', (var.get('octet')&Js(3)))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    var.put('sextet', ((var.get('leftovers')<<Js(4.0))|((var.get('octet')&Js(240))>>Js(4.0))))
                    var.put('leftovers', (var.get('octet')&Js(15)))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    var.put('sextet', ((var.get('leftovers')<<Js(2.0))|((var.get('octet')&Js(192))>>Js(6.0))))
                    var.put('leftovers', (var.get('octet')&Js(63)))
                    break
                SWITCHED = True
                break
            var.put('result', (var.get('result')+var.get('base64ToAscii')(var.get('sextet'))))
            if ((var.get('i')%Js(3.0))==Js(2.0)):
                var.put('result', (var.get('result')+var.get('base64ToAscii')(var.get('leftovers'))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    while 1:
        SWITCHED = False
        CONDITION = ((var.get('str').get('length')%Js(3.0)))
        if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
            SWITCHED = True
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
            SWITCHED = True
            var.put('leftovers', (var.get('leftovers')<<Js(4.0)))
            var.put('result', (var.get('result')+var.get('base64ToAscii')(var.get('leftovers'))))
            var.put('result', (var.get('result')+Js('==')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
            SWITCHED = True
            var.put('leftovers', (var.get('leftovers')<<Js(2.0)))
            var.put('result', (var.get('result')+var.get('base64ToAscii')(var.get('leftovers'))))
            var.put('result', (var.get('result')+Js('=')))
            break
        SWITCHED = True
        break
    return var.get('result')
PyJsHoisted_Base64Encode_.func_name = 'Base64Encode'
var.put('Base64Encode', PyJsHoisted_Base64Encode_)
@Js
def PyJsHoisted_Base64Decode_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['shiftreg', 'result', 'i', 'str', 'count', 'x'])
    var.put('result', Js(''))
    var.put('i', Js(0.0))
    pass
    var.put('shiftreg', Js(0.0))
    var.put('count', (-Js(1.0)))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('str').get('length')):
        try:
            var.put('c', var.get('str').callprop('charAt', var.get('i')))
            if ((Js('A')<=var.get('c')) and (var.get('c')<=Js('Z'))):
                var.put('x', (var.get('str').callprop('charCodeAt', var.get('i'))-Js(65.0)))
            else:
                if ((Js('a')<=var.get('c')) and (var.get('c')<=Js('z'))):
                    var.put('x', ((var.get('str').callprop('charCodeAt', var.get('i'))-Js(97.0))+Js(26.0)))
                else:
                    if ((Js('0')<=var.get('c')) and (var.get('c')<=Js('9'))):
                        var.put('x', ((var.get('str').callprop('charCodeAt', var.get('i'))-Js(48.0))+Js(52.0)))
                    else:
                        if (var.get('c')==Js('+')):
                            var.put('x', Js(62.0))
                        else:
                            if (var.get('c')==Js('/')):
                                var.put('x', Js(63.0))
                            else:
                                continue
            (var.put('count',Js(var.get('count').to_number())+Js(1))-Js(1))
            while 1:
                SWITCHED = False
                CONDITION = ((var.get('count')%Js(4.0)))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                    SWITCHED = True
                    var.put('shiftreg', var.get('x'))
                    continue
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    var.put('v', ((var.get('shiftreg')<<Js(2.0))|(var.get('x')>>Js(4.0))))
                    var.put('shiftreg', (var.get('x')&Js(15)))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    var.put('v', ((var.get('shiftreg')<<Js(4.0))|(var.get('x')>>Js(2.0))))
                    var.put('shiftreg', (var.get('x')&Js(3)))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                    SWITCHED = True
                    var.put('v', ((var.get('shiftreg')<<Js(6.0))|(var.get('x')>>Js(0.0))))
                    var.put('shiftreg', (var.get('x')&Js(0)))
                    break
                SWITCHED = True
                break
            var.put('result', (var.get('result')+var.get('String').callprop('fromCharCode', var.get('v'))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('result').callprop('toString')
PyJsHoisted_Base64Decode_.func_name = 'Base64Decode'
var.put('Base64Decode', PyJsHoisted_Base64Decode_)
@Js
def PyJsHoisted_base64ToAscii_(c, this, arguments, var=var):
    var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['theChar', 'c'])
    var.put('theChar', Js(0.0))
    if ((Js(0.0)<=var.get('c')) and (var.get('c')<=Js(25.0))):
        var.put('theChar', var.get('String').callprop('fromCharCode', (var.get('c')+Js(65.0))))
    else:
        if ((Js(26.0)<=var.get('c')) and (var.get('c')<=Js(51.0))):
            var.put('theChar', var.get('String').callprop('fromCharCode', ((var.get('c')-Js(26.0))+Js(97.0))))
        else:
            if ((Js(52.0)<=var.get('c')) and (var.get('c')<=Js(61.0))):
                var.put('theChar', var.get('String').callprop('fromCharCode', ((var.get('c')-Js(52.0))+Js(48.0))))
            else:
                if (var.get('c')==Js(62.0)):
                    var.put('theChar', Js('+'))
                else:
                    if (var.get('c')==Js(63.0)):
                        var.put('theChar', Js('/'))
                    else:
                        var.put('theChar', var.get('String').callprop('fromCharCode', Js(255)))
    return var.get('theChar')
PyJsHoisted_base64ToAscii_.func_name = 'base64ToAscii'
var.put('base64ToAscii', PyJsHoisted_base64ToAscii_)
@Js
def PyJsHoisted_kzbrid_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['keys'])
    var.put('keys', Js([]))
    var.get('keys').callprop('push', var.get('fp_browser')())
    var.get('keys').callprop('push', var.get('fp_VideoCard')())
    var.get('keys').callprop('push', var.get('fp_canvas')())
    var.get('keys').callprop('push', var.get('fp_webgl')())
    var.get('keys').callprop('push', var.get('fp_cookie')())
    var.get('keys').callprop('push', var.get('fp_display')())
    var.get('keys').callprop('push', var.get('fp_flash')())
    var.get('keys').callprop('push', var.get('fp_java')())
    var.get('keys').callprop('push', var.get('fp_language')())
    var.get('keys').callprop('push', var.get('fp_mimetypen')())
    var.get('keys').callprop('push', var.get('fp_os')())
    var.get('keys').callprop('push', var.get('fp_plugins')())
    var.get('keys').callprop('push', var.get('fp_timezone')())
    var.get('keys').callprop('push', var.get('fp_useragent')())
    return var.get('createhash')(var.get('keys').callprop('join', Js('###')), Js(31.0))
PyJsHoisted_kzbrid_.func_name = 'kzbrid'
var.put('kzbrid', PyJsHoisted_kzbrid_)
@Js
def PyJsHoisted_fp_browser_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['strUserAgent', 'strBrowser', 'strOut', 'strOnError', 'numVersion'])
    Js('use strict')
    pass
    var.put('strOnError', Js('Error'))
    var.put('strUserAgent', var.get(u"null"))
    var.put('numVersion', var.get(u"null"))
    var.put('strBrowser', var.get(u"null"))
    var.put('strOut', var.get(u"null"))
    try:
        var.put('strUserAgent', var.get('navigator').get('userAgent').callprop('toLowerCase'))
        if JsRegExp('/msie (\\d+\\.\\d+);/').callprop('test', var.get('strUserAgent')):
            var.put('numVersion', var.get('Number')(var.get('RegExp').get('$1')))
            if (var.get('strUserAgent').callprop('indexOf', Js('trident/6'))>(-Js(1.0))):
                var.put('numVersion', Js(10.0))
            if (var.get('strUserAgent').callprop('indexOf', Js('trident/5'))>(-Js(1.0))):
                var.put('numVersion', Js(9.0))
            if (var.get('strUserAgent').callprop('indexOf', Js('trident/4'))>(-Js(1.0))):
                var.put('numVersion', Js(8.0))
            var.put('strBrowser', (Js('Internet Explorer ')+var.get('numVersion')))
        else:
            if (var.get('strUserAgent').callprop('indexOf', Js('trident/7'))>(-Js(1.0))):
                var.put('numVersion', Js(11.0))
                var.put('strBrowser', (Js('Internet Explorer ')+var.get('numVersion')))
            else:
                if JsRegExp('/firefox[\\/\\s](\\d+\\.\\d+)/').callprop('test', var.get('strUserAgent')):
                    var.put('numVersion', var.get('Number')(var.get('RegExp').get('$1')))
                    var.put('strBrowser', (Js('Firefox ')+var.get('numVersion')))
                else:
                    if JsRegExp('/opera[\\/\\s](\\d+\\.\\d+)/').callprop('test', var.get('strUserAgent')):
                        var.put('numVersion', var.get('Number')(var.get('RegExp').get('$1')))
                        var.put('strBrowser', (Js('Opera ')+var.get('numVersion')))
                    else:
                        if JsRegExp('/chrome[\\/\\s](\\d+\\.\\d+)/').callprop('test', var.get('strUserAgent')):
                            var.put('numVersion', var.get('Number')(var.get('RegExp').get('$1')))
                            var.put('strBrowser', (Js('Chrome ')+var.get('numVersion')))
                        else:
                            if JsRegExp('/version[\\/\\s](\\d+\\.\\d+)/').callprop('test', var.get('strUserAgent')):
                                var.put('numVersion', var.get('Number')(var.get('RegExp').get('$1')))
                                var.put('strBrowser', (Js('Safari ')+var.get('numVersion')))
                            else:
                                if JsRegExp('/rv[\\/\\s](\\d+\\.\\d+)/').callprop('test', var.get('strUserAgent')):
                                    var.put('numVersion', var.get('Number')(var.get('RegExp').get('$1')))
                                    var.put('strBrowser', (Js('Mozilla ')+var.get('numVersion')))
                                else:
                                    if JsRegExp('/mozilla[\\/\\s](\\d+\\.\\d+)/').callprop('test', var.get('strUserAgent')):
                                        var.put('numVersion', var.get('Number')(var.get('RegExp').get('$1')))
                                        var.put('strBrowser', (Js('Mozilla ')+var.get('numVersion')))
                                    else:
                                        if JsRegExp('/binget[\\/\\s](\\d+\\.\\d+)/').callprop('test', var.get('strUserAgent')):
                                            var.put('numVersion', var.get('Number')(var.get('RegExp').get('$1')))
                                            var.put('strBrowser', (Js('Library (BinGet) ')+var.get('numVersion')))
                                        else:
                                            if JsRegExp('/curl[\\/\\s](\\d+\\.\\d+)/').callprop('test', var.get('strUserAgent')):
                                                var.put('numVersion', var.get('Number')(var.get('RegExp').get('$1')))
                                                var.put('strBrowser', (Js('Library (cURL) ')+var.get('numVersion')))
                                            else:
                                                if JsRegExp('/java[\\/\\s](\\d+\\.\\d+)/').callprop('test', var.get('strUserAgent')):
                                                    var.put('numVersion', var.get('Number')(var.get('RegExp').get('$1')))
                                                    var.put('strBrowser', (Js('Library (Java) ')+var.get('numVersion')))
                                                else:
                                                    if JsRegExp('/libwww-perl[\\/\\s](\\d+\\.\\d+)/').callprop('test', var.get('strUserAgent')):
                                                        var.put('numVersion', var.get('Number')(var.get('RegExp').get('$1')))
                                                        var.put('strBrowser', (Js('Library (libwww-perl) ')+var.get('numVersion')))
                                                    else:
                                                        if JsRegExp('/microsoft url control -[\\s](\\d+\\.\\d+)/').callprop('test', var.get('strUserAgent')):
                                                            var.put('numVersion', var.get('Number')(var.get('RegExp').get('$1')))
                                                            var.put('strBrowser', (Js('Library (Microsoft URL Control) ')+var.get('numVersion')))
                                                        else:
                                                            if JsRegExp('/peach[\\/\\s](\\d+\\.\\d+)/').callprop('test', var.get('strUserAgent')):
                                                                var.put('numVersion', var.get('Number')(var.get('RegExp').get('$1')))
                                                                var.put('strBrowser', (Js('Library (Peach) ')+var.get('numVersion')))
                                                            else:
                                                                if JsRegExp('/php[\\/\\s](\\d+\\.\\d+)/').callprop('test', var.get('strUserAgent')):
                                                                    var.put('numVersion', var.get('Number')(var.get('RegExp').get('$1')))
                                                                    var.put('strBrowser', (Js('Library (PHP) ')+var.get('numVersion')))
                                                                else:
                                                                    if JsRegExp('/pxyscand[\\/\\s](\\d+\\.\\d+)/').callprop('test', var.get('strUserAgent')):
                                                                        var.put('numVersion', var.get('Number')(var.get('RegExp').get('$1')))
                                                                        var.put('strBrowser', (Js('Library (pxyscand) ')+var.get('numVersion')))
                                                                    else:
                                                                        if JsRegExp('/pycurl[\\/\\s](\\d+\\.\\d+)/').callprop('test', var.get('strUserAgent')):
                                                                            var.put('numVersion', var.get('Number')(var.get('RegExp').get('$1')))
                                                                            var.put('strBrowser', (Js('Library (PycURL) ')+var.get('numVersion')))
                                                                        else:
                                                                            if JsRegExp('/python-urllib[\\/\\s](\\d+\\.\\d+)/').callprop('test', var.get('strUserAgent')):
                                                                                var.put('numVersion', var.get('Number')(var.get('RegExp').get('$1')))
                                                                                var.put('strBrowser', (Js('Library (Python URLlib) ')+var.get('numVersion')))
                                                                            else:
                                                                                if JsRegExp('/appengine-google/').callprop('test', var.get('strUserAgent')):
                                                                                    var.put('numVersion', var.get('Number')(var.get('RegExp').get('$1')))
                                                                                    var.put('strBrowser', (Js('Cloud (Google AppEngine) ')+var.get('numVersion')))
                                                                                else:
                                                                                    var.put('strBrowser', Js('Unknown'))
        var.put('strOut', var.get('strBrowser'))
        return var.get('strOut')
    except PyJsException as PyJsTempException:
        PyJsHolder_657272_40615362 = var.own.get('err')
        var.force_own_put('err', PyExceptionToJs(PyJsTempException))
        try:
            return var.get('strOnError')
        finally:
            if PyJsHolder_657272_40615362 is not None:
                var.own['err'] = PyJsHolder_657272_40615362
            else:
                del var.own['err']
            del PyJsHolder_657272_40615362
PyJsHoisted_fp_browser_.func_name = 'fp_browser'
var.put('fp_browser', PyJsHoisted_fp_browser_)
@Js
def PyJsHoisted_fp_VideoCard_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['renderer', 'gl', 'grafikkarte', 'debugInfo', 'vendor'])
    var.put('gl', var.get('document').callprop('createElement', Js('canvas')).callprop('getContext', Js('webgl')))
    if var.get('gl'):
        var.put('debugInfo', var.get('gl').callprop('getExtension', Js('WEBGL_debug_renderer_info')))
        if var.get('debugInfo'):
            var.put('vendor', var.get('gl').callprop('getParameter', var.get('debugInfo').get('UNMASKED_VENDOR_WEBGL')))
            var.put('renderer', var.get('gl').callprop('getParameter', var.get('debugInfo').get('UNMASKED_RENDERER_WEBGL')))
            var.put('grafikkarte', (var.get('vendor')+var.get('renderer')))
        else:
            var.put('grafikkarte', Js('nografik'))
    else:
        var.put('grafikkarte', Js('nografik'))
    return var.get('grafikkarte')
PyJsHoisted_fp_VideoCard_.func_name = 'fp_VideoCard'
var.put('fp_VideoCard', PyJsHoisted_fp_VideoCard_)
@Js
def PyJsHoisted_fp_canvas_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['strng', 'hash', 'txt', 'ctx', 'canvas'])
    var.put('canvas', var.get('document').callprop('createElement', Js('canvas')))
    var.put('ctx', var.get('canvas').callprop('getContext', Js('2d')))
    var.put('txt', Js('i9asdm..$#po((^@KbXrww!~cz'))
    var.get('ctx').put('textBaseline', Js('top'))
    var.get('ctx').put('font', Js("16px 'Arial'"))
    var.get('ctx').put('textBaseline', Js('alphabetic'))
    var.get('ctx').callprop('rotate', Js(0.05))
    var.get('ctx').put('fillStyle', Js('#f60'))
    var.get('ctx').callprop('fillRect', Js(125.0), Js(1.0), Js(62.0), Js(20.0))
    var.get('ctx').put('fillStyle', Js('#069'))
    var.get('ctx').callprop('fillText', var.get('txt'), Js(2.0), Js(15.0))
    var.get('ctx').put('fillStyle', Js('rgba(102, 200, 0, 0.7)'))
    var.get('ctx').callprop('fillText', var.get('txt'), Js(4.0), Js(17.0))
    var.get('ctx').put('shadowBlur', Js(10.0))
    var.get('ctx').put('shadowColor', Js('blue'))
    var.get('ctx').callprop('fillRect', (-Js(20.0)), Js(10.0), Js(234.0), Js(5.0))
    var.put('strng', var.get('canvas').callprop('toDataURL'))
    var.put('hash', Js(0.0))
    if (var.get('strng').get('length')==Js(0.0)):
        return Js('nothing!')
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('strng').get('length')):
        try:
            var.put('char', var.get('strng').callprop('charCodeAt', var.get('i')))
            var.put('hash', (((var.get('hash')<<Js(5.0))-var.get('hash'))+var.get('char')))
            var.put('hash', (var.get('hash')&var.get('hash')))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('hash')
PyJsHoisted_fp_canvas_.func_name = 'fp_canvas'
var.put('fp_canvas', PyJsHoisted_fp_canvas_)
@Js
def PyJsHoisted_fp_webgl_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['h', 'j', 'g', 'n', 'm', 'k', 'i', 'height', 'width', 'l', 'ctx', 'canvas', 'f'])
    var.put('width', Js(256.0))
    var.put('height', Js(128.0))
    var.put('canvas', var.get('document').callprop('createElement', Js('canvas')))
    def PyJs_LONG_4_(var=var):
        return PyJsComma(PyJsComma(var.get('canvas').put('width', var.get('width')),var.get('canvas').put('height', var.get('height'))),var.put('ctx', ((((var.get('canvas').callprop('getContext', Js('webgl2')) or var.get('canvas').callprop('getContext', Js('experimental-webgl2'))) or var.get('canvas').callprop('getContext', Js('webgl'))) or var.get('canvas').callprop('getContext', Js('experimental-webgl'))) or var.get('canvas').callprop('getContext', Js('moz-webgl')))))
    PyJs_LONG_4_()
    try:
        var.put('f', Js('attribute vec2 attrVertex;varying vec2 varyinTexCoordinate;uniform vec2 uniformOffset;void main(){varyinTexCoordinate=attrVertex+uniformOffset;gl_Position=vec4(attrVertex,0,1);}'))
        var.put('g', Js('precision mediump float;varying vec2 varyinTexCoordinate;void main() {gl_FragColor=vec4(varyinTexCoordinate,0,1);}'))
        var.put('h', var.get('ctx').callprop('createBuffer'))
        var.get('ctx').callprop('bindBuffer', var.get('ctx').get('ARRAY_BUFFER'), var.get('h'))
        var.put('i', var.get('Float32Array').create(Js([(-Js(0.2)), (-Js(0.9)), Js(0.0), Js(0.4), (-Js(0.26)), Js(0.0), Js(0.0), Js(0.7321), Js(0.0)])))
        PyJsComma(PyJsComma(var.get('ctx').callprop('bufferData', var.get('ctx').get('ARRAY_BUFFER'), var.get('i'), var.get('ctx').get('STATIC_DRAW')),var.get('h').put('itemSize', Js(3.0))),var.get('h').put('numItems', Js(3.0)))
        var.put('j', var.get('ctx').callprop('createProgram'))
        var.put('k', var.get('ctx').callprop('createShader', var.get('ctx').get('VERTEX_SHADER')))
        var.get('ctx').callprop('shaderSource', var.get('k'), var.get('f'))
        var.get('ctx').callprop('compileShader', var.get('k'))
        var.put('l', var.get('ctx').callprop('createShader', var.get('ctx').get('FRAGMENT_SHADER')))
        var.get('ctx').callprop('shaderSource', var.get('l'), var.get('g'))
        var.get('ctx').callprop('compileShader', var.get('l'))
        var.get('ctx').callprop('attachShader', var.get('j'), var.get('k'))
        var.get('ctx').callprop('attachShader', var.get('j'), var.get('l'))
        var.get('ctx').callprop('linkProgram', var.get('j'))
        var.get('ctx').callprop('useProgram', var.get('j'))
        var.get('j').put('vertexPosAttrib', var.get('ctx').callprop('getAttribLocation', var.get('j'), Js('attrVertex')))
        var.get('j').put('offsetUniform', var.get('ctx').callprop('getUniformLocation', var.get('j'), Js('uniformOffset')))
        var.get('ctx').callprop('enableVertexAttribArray', var.get('j').get('vertexPosArray'))
        var.get('ctx').callprop('vertexAttribPointer', var.get('j').get('vertexPosAttrib'), var.get('h').get('itemSize'), var.get('ctx').get('FLOAT'), Js(1.0).neg(), Js(0.0), Js(0.0))
        var.get('ctx').callprop('uniform2f', var.get('j').get('offsetUniform'), Js(1.0), Js(1.0))
        var.get('ctx').callprop('drawArrays', var.get('ctx').get('TRIANGLE_STRIP'), Js(0.0), var.get('h').get('numItems'))
    except PyJsException as PyJsTempException:
        PyJsHolder_65_17613218 = var.own.get('e')
        var.force_own_put('e', PyExceptionToJs(PyJsTempException))
        try:
            pass
        finally:
            if PyJsHolder_65_17613218 is not None:
                var.own['e'] = PyJsHolder_65_17613218
            else:
                del var.own['e']
            del PyJsHolder_65_17613218
    var.put('m', Js(''))
    var.put('n', var.get('Uint8Array').create(((var.get('width')*var.get('height'))*Js(4.0))))
    var.get('ctx').callprop('readPixels', Js(0.0), Js(0.0), var.get('width'), var.get('height'), var.get('ctx').get('RGBA'), var.get('ctx').get('UNSIGNED_BYTE'), var.get('n'))
    var.put('m', var.get('JSON').callprop('stringify', var.get('n')).callprop('replace', JsRegExp('/,?"[0-9]+":/g'), Js('')))
    return var.get('sha256')(var.get('m'))
PyJsHoisted_fp_webgl_.func_name = 'fp_webgl'
var.put('fp_webgl', PyJsHoisted_fp_webgl_)
@Js
def PyJsHoisted_fp_cookie_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['bolCookieEnabled', 'bolOut', 'strOnError'])
    Js('use strict')
    pass
    var.put('strOnError', Js('Error'))
    var.put('bolCookieEnabled', var.get(u"null"))
    var.put('bolOut', var.get(u"null"))
    try:
        var.put('bolCookieEnabled', (Js(True) if var.get('navigator').get('cookieEnabled') else Js(False)))
        if (PyJsStrictEq(var.get('navigator').get('cookieEnabled').typeof(),Js('undefined')) and var.get('bolCookieEnabled').neg()):
            var.get('document').put('cookie', Js('testcookie'))
            var.put('bolCookieEnabled', (Js(True) if PyJsStrictNeq(var.get('document').get('cookie').callprop('indexOf', Js('testcookie')),(-Js(1.0))) else Js(False)))
        var.put('bolOut', var.get('bolCookieEnabled'))
        return var.get('bolOut')
    except PyJsException as PyJsTempException:
        PyJsHolder_657272_44730906 = var.own.get('err')
        var.force_own_put('err', PyExceptionToJs(PyJsTempException))
        try:
            return var.get('strOnError')
        finally:
            if PyJsHolder_657272_44730906 is not None:
                var.own['err'] = PyJsHolder_657272_44730906
            else:
                del var.own['err']
            del PyJsHolder_657272_44730906
PyJsHoisted_fp_cookie_.func_name = 'fp_cookie'
var.put('fp_cookie', PyJsHoisted_fp_cookie_)
@Js
def PyJsHoisted_fp_display_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['strScreen', 'strOut', 'strSep', 'strOnError', 'strDisplay', 'strPair'])
    Js('use strict')
    pass
    var.put('strSep', Js('|'))
    var.put('strPair', Js('='))
    var.put('strOnError', Js('Error'))
    var.put('strScreen', var.get(u"null"))
    var.put('strDisplay', var.get(u"null"))
    var.put('strOut', var.get(u"null"))
    try:
        var.put('strScreen', var.get('window').get('screen'))
        if var.get('strScreen'):
            var.put('strDisplay', ((((((((var.get('strScreen').get('colorDepth')+var.get('strSep'))+var.get('strScreen').get('width'))+var.get('strSep'))+var.get('strScreen').get('height'))+var.get('strSep'))+var.get('strScreen').get('availWidth'))+var.get('strSep'))+var.get('strScreen').get('availHeight')))
        var.put('strOut', var.get('strDisplay'))
        return var.get('strOut')
    except PyJsException as PyJsTempException:
        PyJsHolder_657272_96156866 = var.own.get('err')
        var.force_own_put('err', PyExceptionToJs(PyJsTempException))
        try:
            return var.get('strOnError')
        finally:
            if PyJsHolder_657272_96156866 is not None:
                var.own['err'] = PyJsHolder_657272_96156866
            else:
                del var.own['err']
            del PyJsHolder_657272_96156866
PyJsHoisted_fp_display_.func_name = 'fp_display'
var.put('fp_display', PyJsHoisted_fp_display_)
@Js
def PyJsHoisted_fp_flash_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['objPlayerVersion', 'strVersion', 'strOut', 'strOnError'])
    Js('use strict')
    pass
    var.put('strOnError', Js('N/A'))
    var.put('objPlayerVersion', var.get(u"null"))
    var.put('strVersion', var.get(u"null"))
    var.put('strOut', var.get(u"null"))
    try:
        var.put('objPlayerVersion', var.get('swfobject').callprop('getFlashPlayerVersion'))
        var.put('strVersion', ((((var.get('objPlayerVersion').get('major')+Js('.'))+var.get('objPlayerVersion').get('minor'))+Js('.'))+var.get('objPlayerVersion').get('release')))
        if PyJsStrictEq(var.get('strVersion'),Js('0.0.0')):
            var.put('strVersion', Js('N/A'))
        var.put('strOut', var.get('strVersion'))
        return var.get('strOut')
    except PyJsException as PyJsTempException:
        PyJsHolder_657272_57069964 = var.own.get('err')
        var.force_own_put('err', PyExceptionToJs(PyJsTempException))
        try:
            return var.get('strOnError')
        finally:
            if PyJsHolder_657272_57069964 is not None:
                var.own['err'] = PyJsHolder_657272_57069964
            else:
                del var.own['err']
            del PyJsHolder_657272_57069964
PyJsHoisted_fp_flash_.func_name = 'fp_flash'
var.put('fp_flash', PyJsHoisted_fp_flash_)
@Js
def PyJsHoisted_fp_fonts_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['style', 'body', 'result', 'div', 'fonts', 'i', 'divs', 'template', 'font', 'strOnError', 'count', 'e', 'fragment'])
    Js('use strict')
    pass
    var.put('strOnError', Js('Error'))
    var.put('style', var.get(u"null"))
    var.put('fonts', var.get(u"null"))
    var.put('font', var.get(u"null"))
    var.put('count', Js(0.0))
    var.put('template', var.get(u"null"))
    var.put('divs', var.get(u"null"))
    var.put('e', var.get(u"null"))
    var.put('div', var.get(u"null"))
    var.put('body', var.get(u"null"))
    var.put('i', Js(0.0))
    try:
        var.put('style', Js('position: absolute; visibility: hidden; display: block !important'))
        def PyJs_LONG_8_(var=var):
            return var.put('fonts', Js([Js('Abadi MT Condensed Light'), Js('Adobe Fangsong Std'), Js('Adobe Hebrew'), Js('Adobe Ming Std'), Js('Agency FB'), Js('Aharoni'), Js('Andalus'), Js('Angsana New'), Js('AngsanaUPC'), Js('Aparajita'), Js('Arab'), Js('Arabic Transparent'), Js('Arabic Typesetting'), Js('Arial Baltic'), Js('Arial Black'), Js('Arial CE'), Js('Arial CYR'), Js('Arial Greek'), Js('Arial TUR'), Js('Arial'), Js('Batang'), Js('BatangChe'), Js('Bauhaus 93'), Js('Bell MT'), Js('Bitstream Vera Serif'), Js('Bodoni MT'), Js('Bookman Old Style'), Js('Braggadocio'), Js('Broadway'), Js('Browallia New'), Js('BrowalliaUPC'), Js('Calibri Light'), Js('Calibri'), Js('Californian FB'), Js('Cambria Math'), Js('Cambria'), Js('Candara'), Js('Castellar'), Js('Casual'), Js('Centaur'), Js('Century Gothic'), Js('Chalkduster'), Js('Colonna MT'), Js('Comic Sans MS'), Js('Consolas'), Js('Constantia'), Js('Copperplate Gothic Light'), Js('Corbel'), Js('Cordia New'), Js('CordiaUPC'), Js('Courier New Baltic'), Js('Courier New CE'), Js('Courier New CYR'), Js('Courier New Greek'), Js('Courier New TUR'), Js('Courier New'), Js('DFKai-SB'), Js('DaunPenh'), Js('David'), Js('DejaVu LGC Sans Mono'), Js('Desdemona'), Js('DilleniaUPC'), Js('DokChampa'), Js('Dotum'), Js('DotumChe'), Js('Ebrima'), Js('Engravers MT'), Js('Eras Bold ITC'), Js('Estrangelo Edessa'), Js('EucrosiaUPC'), Js('Euphemia'), Js('Eurostile'), Js('FangSong'), Js('Forte'), Js('FrankRuehl'), Js('Franklin Gothic Heavy'), Js('Franklin Gothic Medium'), Js('FreesiaUPC'), Js('French Script MT'), Js('Gabriola'), Js('Gautami'), Js('Georgia'), Js('Gigi'), Js('Gisha'), Js('Goudy Old Style'), Js('Gulim'), Js('GulimChe'), Js('GungSeo'), Js('Gungsuh'), Js('GungsuhChe'), Js('Haettenschweiler'), Js('Harrington'), Js('Hei S'), Js('HeiT'), Js('Heisei Kaku Gothic'), Js('Hiragino Sans GB'), Js('Impact'), Js('Informal Roman'), Js('IrisUPC'), Js('Iskoola Pota'), Js('JasmineUPC'), Js('KacstOne'), Js('KaiTi'), Js('Kalinga'), Js('Kartika'), Js('Khmer UI'), Js('Kino MT'), Js('KodchiangUPC'), Js('Kokila'), Js('Kozuka Gothic Pr6N'), Js('Lao UI'), Js('Latha'), Js('Leelawadee'), Js('Levenim MT'), Js('LilyUPC'), Js('Lohit Gujarati'), Js('Loma'), Js('Lucida Bright'), Js('Lucida Console'), Js('Lucida Fax'), Js('Lucida Sans Unicode'), Js('MS Gothic'), Js('MS Mincho'), Js('MS PGothic'), Js('MS PMincho'), Js('MS Reference Sans Serif'), Js('MS UI Gothic'), Js('MV Boli'), Js('Magneto'), Js('Malgun Gothic'), Js('Mangal'), Js('Marlett'), Js('Matura MT Script Capitals'), Js('Meiryo UI'), Js('Meiryo'), Js('Menlo'), Js('Microsoft Himalaya'), Js('Microsoft JhengHei'), Js('Microsoft New Tai Lue'), Js('Microsoft PhagsPa'), Js('Microsoft Sans Serif'), Js('Microsoft Tai Le'), Js('Microsoft Uighur'), Js('Microsoft YaHei'), Js('Microsoft Yi Baiti'), Js('MingLiU'), Js('MingLiU-ExtB'), Js('MingLiU_HKSCS'), Js('MingLiU_HKSCS-ExtB'), Js('Miriam Fixed'), Js('Miriam'), Js('Mongolian Baiti'), Js('MoolBoran'), Js('NSimSun'), Js('Narkisim'), Js('News Gothic MT'), Js('Niagara Solid'), Js('Nyala'), Js('PMingLiU'), Js('PMingLiU-ExtB'), Js('Palace Script MT'), Js('Palatino Linotype'), Js('Papyrus'), Js('Perpetua'), Js('Plantagenet Cherokee'), Js('Playbill'), Js('Prelude Bold'), Js('Prelude Condensed Bold'), Js('Prelude Condensed Medium'), Js('Prelude Medium'), Js('PreludeCompressedWGL Black'), Js('PreludeCompressedWGL Bold'), Js('PreludeCompressedWGL Light'), Js('PreludeCompressedWGL Medium'), Js('PreludeCondensedWGL Black'), Js('PreludeCondensedWGL Bold'), Js('PreludeCondensedWGL Light'), Js('PreludeCondensedWGL Medium'), Js('PreludeWGL Black'), Js('PreludeWGL Bold'), Js('PreludeWGL Light'), Js('PreludeWGL Medium'), Js('Raavi'), Js('Rachana'), Js('Rockwell'), Js('Rod'), Js('Sakkal Majalla'), Js('Sawasdee'), Js('Script MT Bold'), Js('Segoe Print'), Js('Segoe Script'), Js('Segoe UI Light'), Js('Segoe UI Semibold'), Js('Segoe UI Symbol'), Js('Segoe UI'), Js('Shonar Bangla'), Js('Showcard Gothic'), Js('Shruti'), Js('SimHei'), Js('SimSun'), Js('SimSun-ExtB'), Js('Simplified Arabic Fixed'), Js('Simplified Arabic'), Js('Snap ITC'), Js('Sylfaen'), Js('Symbol'), Js('Tahoma'), Js('Times New Roman Baltic'), Js('Times New Roman CE'), Js('Times New Roman CYR'), Js('Times New Roman Greek'), Js('Times New Roman TUR'), Js('Times New Roman'), Js('TlwgMono'), Js('Traditional Arabic'), Js('Trebuchet MS'), Js('Tunga'), Js('Tw Cen MT Condensed Extra Bold'), Js('Ubuntu'), Js('Umpush'), Js('Univers'), Js('Utopia'), Js('Utsaah'), Js('Vani'), Js('Verdana'), Js('Vijaya'), Js('Vladimir Script'), Js('Vrinda'), Js('Webdings'), Js('Wide Latin'), Js('Wingdings')]))
        PyJs_LONG_8_()
        var.put('count', var.get('fonts').get('length'))
        var.put('template', (Js('<b style="display:inline !important; width:auto !important; font:normal 10px/1 \'X\',sans-serif !important">ww</b>')+Js('<b style="display:inline !important; width:auto !important; font:normal 10px/1 \'X\',monospace !important">ww</b>')))
        var.put('fragment', var.get('document').callprop('createDocumentFragment'))
        var.put('divs', Js([]))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('count')):
            try:
                var.put('font', var.get('fonts').get(var.get('i')))
                var.put('div', var.get('document').callprop('createElement', Js('div')))
                var.put('font', var.get('font').callprop('replace', JsRegExp('/[\'"<>]/g'), Js('')))
                var.get('div').put('innerHTML', var.get('template').callprop('replace', JsRegExp('/X/g'), var.get('font')))
                var.get('div').get('style').put('cssText', var.get('style'))
                var.get('fragment').callprop('appendChild', var.get('div'))
                var.get('divs').callprop('push', var.get('div'))
            finally:
                    var.put('i', (var.get('i')+Js(1.0)))
        var.put('body', var.get('document').get('body'))
        var.get('body').callprop('insertBefore', var.get('fragment'), var.get('body').get('firstChild'))
        var.put('result', Js([]))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('count')):
            try:
                var.put('e', var.get('divs').get(var.get('i')).callprop('getElementsByTagName', Js('b')))
                if PyJsStrictEq(var.get('e').get('0').get('offsetWidth'),var.get('e').get('1').get('offsetWidth')):
                    var.get('result').callprop('push', var.get('fonts').get(var.get('i')))
            finally:
                    var.put('i', (var.get('i')+Js(1.0)))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('count')):
            try:
                var.get('body').callprop('removeChild', var.get('divs').get(var.get('i')))
            finally:
                    var.put('i', (var.get('i')+Js(1.0)))
        return var.get('createhash')(var.get('result').callprop('join', Js('|')), Js(31.0))
    except PyJsException as PyJsTempException:
        PyJsHolder_657272_93550891 = var.own.get('err')
        var.force_own_put('err', PyExceptionToJs(PyJsTempException))
        try:
            return var.get('strOnError')
        finally:
            if PyJsHolder_657272_93550891 is not None:
                var.own['err'] = PyJsHolder_657272_93550891
            else:
                del var.own['err']
            del PyJsHolder_657272_93550891
PyJsHoisted_fp_fonts_.func_name = 'fp_fonts'
var.put('fp_fonts', PyJsHoisted_fp_fonts_)
@Js
def PyJsHoisted_fp_java_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['strJavaEnabled', 'strOut', 'strOnError'])
    Js('use strict')
    pass
    var.put('strOnError', Js('Error'))
    var.put('strJavaEnabled', var.get(u"null"))
    var.put('strOut', var.get(u"null"))
    try:
        if var.get('navigator').callprop('javaEnabled'):
            var.put('strJavaEnabled', Js('true'))
        else:
            var.put('strJavaEnabled', Js('false'))
        var.put('strOut', var.get('strJavaEnabled'))
        return var.get('strOut')
    except PyJsException as PyJsTempException:
        PyJsHolder_657272_41210627 = var.own.get('err')
        var.force_own_put('err', PyExceptionToJs(PyJsTempException))
        try:
            return var.get('strOnError')
        finally:
            if PyJsHolder_657272_41210627 is not None:
                var.own['err'] = PyJsHolder_657272_41210627
            else:
                del var.own['err']
            del PyJsHolder_657272_41210627
PyJsHoisted_fp_java_.func_name = 'fp_java'
var.put('fp_java', PyJsHoisted_fp_java_)
@Js
def PyJsHoisted_fp_language_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['strTypeSysLng', 'strTypeLng', 'strLang', 'strTypeBrLng', 'strTypeUsrLng', 'strOut', 'strSep', 'strOnError', 'strPair'])
    Js('use strict')
    pass
    var.put('strSep', Js('|'))
    var.put('strPair', Js('='))
    var.put('strOnError', Js('Error'))
    var.put('strLang', var.get(u"null"))
    var.put('strTypeLng', var.get(u"null"))
    var.put('strTypeBrLng', var.get(u"null"))
    var.put('strTypeSysLng', var.get(u"null"))
    var.put('strTypeUsrLng', var.get(u"null"))
    var.put('strOut', var.get(u"null"))
    try:
        var.put('strTypeLng', var.get('navigator').get('language').typeof())
        var.put('strTypeBrLng', var.get('navigator').get('browserLanguage').typeof())
        var.put('strTypeSysLng', var.get('navigator').get('systemLanguage').typeof())
        var.put('strTypeUsrLng', var.get('navigator').get('userLanguage').typeof())
        if PyJsStrictNeq(var.get('strTypeLng'),Js('undefined')):
            var.put('strLang', (((Js('lang')+var.get('strPair'))+var.get('navigator').get('language'))+var.get('strSep')))
        else:
            if PyJsStrictNeq(var.get('strTypeBrLng'),Js('undefined')):
                var.put('strLang', (((Js('lang')+var.get('strPair'))+var.get('navigator').get('browserLanguage'))+var.get('strSep')))
            else:
                var.put('strLang', ((Js('lang')+var.get('strPair'))+var.get('strSep')))
        if PyJsStrictNeq(var.get('strTypeSysLng'),Js('undefined')):
            var.put('strLang', (((Js('syslang')+var.get('strPair'))+var.get('navigator').get('systemLanguage'))+var.get('strSep')), '+')
        else:
            var.put('strLang', ((Js('syslang')+var.get('strPair'))+var.get('strSep')), '+')
        if PyJsStrictNeq(var.get('strTypeUsrLng'),Js('undefined')):
            var.put('strLang', ((Js('userlang')+var.get('strPair'))+var.get('navigator').get('userLanguage')), '+')
        else:
            var.put('strLang', (Js('userlang')+var.get('strPair')), '+')
        var.put('strOut', var.get('strLang'))
        return var.get('strOut')
    except PyJsException as PyJsTempException:
        PyJsHolder_657272_63893885 = var.own.get('err')
        var.force_own_put('err', PyExceptionToJs(PyJsTempException))
        try:
            return var.get('strOnError')
        finally:
            if PyJsHolder_657272_63893885 is not None:
                var.own['err'] = PyJsHolder_657272_63893885
            else:
                del var.own['err']
            del PyJsHolder_657272_63893885
PyJsHoisted_fp_language_.func_name = 'fp_language'
var.put('fp_language', PyJsHoisted_fp_language_)
@Js
def PyJsHoisted_fp_mimetypen_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['i'])
    var.put('strInputData', Js([]))
    if (var.get('navigator').get('plugins').get('length')==Js(0.0)):
        return Js('noPlugins')
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('navigator').get('mimeTypes').get('length')):
        try:
            var.get('strInputData').callprop('push', var.get('navigator').get('mimeTypes').get(var.get('i')).get('type'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('strTmp', var.get('strInputData').callprop('join', Js('|')))
    var.put('strOut', var.get('strTmp'))
    return var.get('strOut')
PyJsHoisted_fp_mimetypen_.func_name = 'fp_mimetypen'
var.put('fp_mimetypen', PyJsHoisted_fp_mimetypen_)
@Js
def PyJsHoisted_fp_os_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['strOSBits', 'strUserAgent', 'strOut', 'strPlatform', 'strSep', 'strOnError', 'strOS'])
    Js('use strict')
    pass
    var.put('strSep', Js('|'))
    var.put('strOnError', Js('Error'))
    var.put('strUserAgent', var.get(u"null"))
    var.put('strPlatform', var.get(u"null"))
    var.put('strOS', var.get(u"null"))
    var.put('strOSBits', var.get(u"null"))
    var.put('strOut', var.get(u"null"))
    try:
        var.put('strUserAgent', var.get('navigator').get('userAgent').callprop('toLowerCase'))
        var.put('strPlatform', var.get('navigator').get('platform').callprop('toLowerCase'))
        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('windows nt 6.3')),(-Js(1.0))):
            var.put('strOS', Js('Windows 8.1'))
        else:
            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('windows nt 6.2')),(-Js(1.0))):
                var.put('strOS', Js('Windows 8'))
            else:
                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('windows nt 6.1')),(-Js(1.0))):
                    var.put('strOS', Js('Windows 7'))
                else:
                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('windows nt 6.0')),(-Js(1.0))):
                        var.put('strOS', Js('Windows Vista/Windows Server 2008'))
                    else:
                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('windows nt 5.2')),(-Js(1.0))):
                            var.put('strOS', Js('Windows XP x64/Windows Server 2003'))
                        else:
                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('windows nt 5.1')),(-Js(1.0))):
                                var.put('strOS', Js('Windows XP'))
                            else:
                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('windows nt 5.01')),(-Js(1.0))):
                                    var.put('strOS', Js('Windows 2000, Service Pack 1 (SP1)'))
                                else:
                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('windows xp')),(-Js(1.0))):
                                        var.put('strOS', Js('Windows XP'))
                                    else:
                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('windows 2000')),(-Js(1.0))):
                                            var.put('strOS', Js('Windows 2000'))
                                        else:
                                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('windows nt 5.0')),(-Js(1.0))):
                                                var.put('strOS', Js('Windows 2000'))
                                            else:
                                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('windows nt 4.0')),(-Js(1.0))):
                                                    var.put('strOS', Js('Windows NT 4.0'))
                                                else:
                                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('windows nt')),(-Js(1.0))):
                                                        var.put('strOS', Js('Windows NT 4.0'))
                                                    else:
                                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('winnt4.0')),(-Js(1.0))):
                                                            var.put('strOS', Js('Windows NT 4.0'))
                                                        else:
                                                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('winnt')),(-Js(1.0))):
                                                                var.put('strOS', Js('Windows NT 4.0'))
                                                            else:
                                                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('windows me')),(-Js(1.0))):
                                                                    var.put('strOS', Js('Windows ME'))
                                                                else:
                                                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('win 9x 4.90')),(-Js(1.0))):
                                                                        var.put('strOS', Js('Windows ME'))
                                                                    else:
                                                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('windows 98')),(-Js(1.0))):
                                                                            var.put('strOS', Js('Windows 98'))
                                                                        else:
                                                                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('win98')),(-Js(1.0))):
                                                                                var.put('strOS', Js('Windows 98'))
                                                                            else:
                                                                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('windows 95')),(-Js(1.0))):
                                                                                    var.put('strOS', Js('Windows 95'))
                                                                                else:
                                                                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('windows_95')),(-Js(1.0))):
                                                                                        var.put('strOS', Js('Windows 95'))
                                                                                    else:
                                                                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('win95')),(-Js(1.0))):
                                                                                            var.put('strOS', Js('Windows 95'))
                                                                                        else:
                                                                                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('ce')),(-Js(1.0))):
                                                                                                var.put('strOS', Js('Windows CE'))
                                                                                            else:
                                                                                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('win16')),(-Js(1.0))):
                                                                                                    var.put('strOS', Js('Windows 3.11'))
                                                                                                else:
                                                                                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('iemobile')),(-Js(1.0))):
                                                                                                        var.put('strOS', Js('Windows Mobile'))
                                                                                                    else:
                                                                                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('wm5 pie')),(-Js(1.0))):
                                                                                                            var.put('strOS', Js('Windows Mobile'))
                                                                                                        else:
                                                                                                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('windows')),(-Js(1.0))):
                                                                                                                var.put('strOS', Js('Windows (Unknown Version)'))
                                                                                                            else:
                                                                                                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('openbsd')),(-Js(1.0))):
                                                                                                                    var.put('strOS', Js('Open BSD'))
                                                                                                                else:
                                                                                                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('sunos')),(-Js(1.0))):
                                                                                                                        var.put('strOS', Js('Sun OS'))
                                                                                                                    else:
                                                                                                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('ubuntu')),(-Js(1.0))):
                                                                                                                            var.put('strOS', Js('Ubuntu'))
                                                                                                                        else:
                                                                                                                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('ipad')),(-Js(1.0))):
                                                                                                                                var.put('strOS', Js('iOS (iPad)'))
                                                                                                                            else:
                                                                                                                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('ipod')),(-Js(1.0))):
                                                                                                                                    var.put('strOS', Js('iOS (iTouch)'))
                                                                                                                                else:
                                                                                                                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('iphone')),(-Js(1.0))):
                                                                                                                                        var.put('strOS', Js('iOS (iPhone)'))
                                                                                                                                    else:
                                                                                                                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('mac os x beta')),(-Js(1.0))):
                                                                                                                                            var.put('strOS', Js('Mac OSX Beta (Kodiak)'))
                                                                                                                                        else:
                                                                                                                                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('mac os x 10.0')),(-Js(1.0))):
                                                                                                                                                var.put('strOS', Js('Mac OSX Cheetah'))
                                                                                                                                            else:
                                                                                                                                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('mac os x 10.1')),(-Js(1.0))):
                                                                                                                                                    var.put('strOS', Js('Mac OSX Puma'))
                                                                                                                                                else:
                                                                                                                                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('mac os x 10.2')),(-Js(1.0))):
                                                                                                                                                        var.put('strOS', Js('Mac OSX Jaguar'))
                                                                                                                                                    else:
                                                                                                                                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('mac os x 10.3')),(-Js(1.0))):
                                                                                                                                                            var.put('strOS', Js('Mac OSX Panther'))
                                                                                                                                                        else:
                                                                                                                                                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('mac os x 10.4')),(-Js(1.0))):
                                                                                                                                                                var.put('strOS', Js('Mac OSX Tiger'))
                                                                                                                                                            else:
                                                                                                                                                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('mac os x 10.5')),(-Js(1.0))):
                                                                                                                                                                    var.put('strOS', Js('Mac OSX Leopard'))
                                                                                                                                                                else:
                                                                                                                                                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('mac os x 10.6')),(-Js(1.0))):
                                                                                                                                                                        var.put('strOS', Js('Mac OSX Snow Leopard'))
                                                                                                                                                                    else:
                                                                                                                                                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('mac os x 10.7')),(-Js(1.0))):
                                                                                                                                                                            var.put('strOS', Js('Mac OSX Lion'))
                                                                                                                                                                        else:
                                                                                                                                                                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('mac os x')),(-Js(1.0))):
                                                                                                                                                                                var.put('strOS', Js('Mac OSX (Version Unknown)'))
                                                                                                                                                                            else:
                                                                                                                                                                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('mac_68000')),(-Js(1.0))):
                                                                                                                                                                                    var.put('strOS', Js('Mac OS Classic (68000)'))
                                                                                                                                                                                else:
                                                                                                                                                                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('68K')),(-Js(1.0))):
                                                                                                                                                                                        var.put('strOS', Js('Mac OS Classic (68000)'))
                                                                                                                                                                                    else:
                                                                                                                                                                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('mac_powerpc')),(-Js(1.0))):
                                                                                                                                                                                            var.put('strOS', Js('Mac OS Classic (PowerPC)'))
                                                                                                                                                                                        else:
                                                                                                                                                                                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('ppc mac')),(-Js(1.0))):
                                                                                                                                                                                                var.put('strOS', Js('Mac OS Classic (PowerPC)'))
                                                                                                                                                                                            else:
                                                                                                                                                                                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('macintosh')),(-Js(1.0))):
                                                                                                                                                                                                    var.put('strOS', Js('Mac OS Classic'))
                                                                                                                                                                                                else:
                                                                                                                                                                                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('googletv')),(-Js(1.0))):
                                                                                                                                                                                                        var.put('strOS', Js('Android (GoogleTV)'))
                                                                                                                                                                                                    else:
                                                                                                                                                                                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('xoom')),(-Js(1.0))):
                                                                                                                                                                                                            var.put('strOS', Js('Android (Xoom)'))
                                                                                                                                                                                                        else:
                                                                                                                                                                                                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('htc_flyer')),(-Js(1.0))):
                                                                                                                                                                                                                var.put('strOS', Js('Android (HTC Flyer)'))
                                                                                                                                                                                                            else:
                                                                                                                                                                                                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('android')),(-Js(1.0))):
                                                                                                                                                                                                                    var.put('strOS', Js('Android'))
                                                                                                                                                                                                                else:
                                                                                                                                                                                                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('symbian')),(-Js(1.0))):
                                                                                                                                                                                                                        var.put('strOS', Js('Symbian'))
                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('series60')),(-Js(1.0))):
                                                                                                                                                                                                                            var.put('strOS', Js('Symbian (Series 60)'))
                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('series70')),(-Js(1.0))):
                                                                                                                                                                                                                                var.put('strOS', Js('Symbian (Series 70)'))
                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('series80')),(-Js(1.0))):
                                                                                                                                                                                                                                    var.put('strOS', Js('Symbian (Series 80)'))
                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('series90')),(-Js(1.0))):
                                                                                                                                                                                                                                        var.put('strOS', Js('Symbian (Series 90)'))
                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('x11')),(-Js(1.0))):
                                                                                                                                                                                                                                            var.put('strOS', Js('UNIX'))
                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('nix')),(-Js(1.0))):
                                                                                                                                                                                                                                                var.put('strOS', Js('UNIX'))
                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('linux')),(-Js(1.0))):
                                                                                                                                                                                                                                                    var.put('strOS', Js('Linux'))
                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('qnx')),(-Js(1.0))):
                                                                                                                                                                                                                                                        var.put('strOS', Js('QNX'))
                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('os/2')),(-Js(1.0))):
                                                                                                                                                                                                                                                            var.put('strOS', Js('IBM OS/2'))
                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('beos')),(-Js(1.0))):
                                                                                                                                                                                                                                                                var.put('strOS', Js('BeOS'))
                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('blackberry95')),(-Js(1.0))):
                                                                                                                                                                                                                                                                    var.put('strOS', Js('Blackberry (Storm 1/2)'))
                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('blackberry97')),(-Js(1.0))):
                                                                                                                                                                                                                                                                        var.put('strOS', Js('Blackberry (Bold)'))
                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('blackberry96')),(-Js(1.0))):
                                                                                                                                                                                                                                                                            var.put('strOS', Js('Blackberry (Tour)'))
                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('blackberry89')),(-Js(1.0))):
                                                                                                                                                                                                                                                                                var.put('strOS', Js('Blackberry (Curve 2)'))
                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('blackberry98')),(-Js(1.0))):
                                                                                                                                                                                                                                                                                    var.put('strOS', Js('Blackberry (Torch)'))
                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('playbook')),(-Js(1.0))):
                                                                                                                                                                                                                                                                                        var.put('strOS', Js('Blackberry (Playbook)'))
                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('wnd.rim')),(-Js(1.0))):
                                                                                                                                                                                                                                                                                            var.put('strOS', Js('Blackberry (IE/FF Emulator)'))
                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('blackberry')),(-Js(1.0))):
                                                                                                                                                                                                                                                                                                var.put('strOS', Js('Blackberry'))
                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('palm')),(-Js(1.0))):
                                                                                                                                                                                                                                                                                                    var.put('strOS', Js('Palm OS'))
                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('webos')),(-Js(1.0))):
                                                                                                                                                                                                                                                                                                        var.put('strOS', Js('WebOS'))
                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('hpwos')),(-Js(1.0))):
                                                                                                                                                                                                                                                                                                            var.put('strOS', Js('WebOS (HP)'))
                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('blazer')),(-Js(1.0))):
                                                                                                                                                                                                                                                                                                                var.put('strOS', Js('Palm OS (Blazer)'))
                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('xiino')),(-Js(1.0))):
                                                                                                                                                                                                                                                                                                                    var.put('strOS', Js('Palm OS (Xiino)'))
                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('kindle')),(-Js(1.0))):
                                                                                                                                                                                                                                                                                                                        var.put('strOS', Js('Kindle'))
                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('wii')),(-Js(1.0))):
                                                                                                                                                                                                                                                                                                                            var.put('strOS', Js('Nintendo (Wii)'))
                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('nintendo ds')),(-Js(1.0))):
                                                                                                                                                                                                                                                                                                                                var.put('strOS', Js('Nintendo (DS)'))
                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('playstation 3')),(-Js(1.0))):
                                                                                                                                                                                                                                                                                                                                    var.put('strOS', Js('Sony (Playstation Console)'))
                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('playstation portable')),(-Js(1.0))):
                                                                                                                                                                                                                                                                                                                                        var.put('strOS', Js('Sony (Playstation Portable)'))
                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('webtv')),(-Js(1.0))):
                                                                                                                                                                                                                                                                                                                                            var.put('strOS', Js('MSN TV (WebTV)'))
                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('inferno')),(-Js(1.0))):
                                                                                                                                                                                                                                                                                                                                                var.put('strOS', Js('Inferno'))
                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                var.put('strOS', Js('Unknown'))
        if PyJsStrictNeq(var.get('strPlatform').callprop('indexOf', Js('x64')),(-Js(1.0))):
            var.put('strOSBits', Js('64 bits'))
        else:
            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('x86_64')),(-Js(1.0))):
                var.put('strOSBits', Js('64 bits'))
            else:
                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('x86-64')),(-Js(1.0))):
                    var.put('strOSBits', Js('64 bits'))
                else:
                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('win64')),(-Js(1.0))):
                        var.put('strOSBits', Js('64 bits'))
                    else:
                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('x64;')),(-Js(1.0))):
                            var.put('strOSBits', Js('64 bits'))
                        else:
                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('amd64')),(-Js(1.0))):
                                var.put('strOSBits', Js('64 bits'))
                            else:
                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('wow64')),(-Js(1.0))):
                                    var.put('strOSBits', Js('64 bits'))
                                else:
                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('x64_64')),(-Js(1.0))):
                                        var.put('strOSBits', Js('64 bits'))
                                    else:
                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('ia65')),(-Js(1.0))):
                                            var.put('strOSBits', Js('64 bits'))
                                        else:
                                            if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('sparc64')),(-Js(1.0))):
                                                var.put('strOSBits', Js('64 bits'))
                                            else:
                                                if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('ppc64')),(-Js(1.0))):
                                                    var.put('strOSBits', Js('64 bits'))
                                                else:
                                                    if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('irix64')),(-Js(1.0))):
                                                        var.put('strOSBits', Js('64 bits'))
                                                    else:
                                                        if PyJsStrictNeq(var.get('strUserAgent').callprop('indexOf', Js('irix64')),(-Js(1.0))):
                                                            var.put('strOSBits', Js('64 bits'))
                                                        else:
                                                            var.put('strOSBits', Js('32 bits'))
        var.put('strOut', ((var.get('strOS')+var.get('strSep'))+var.get('strOSBits')))
        return var.get('strOut')
    except PyJsException as PyJsTempException:
        PyJsHolder_657272_89268985 = var.own.get('err')
        var.force_own_put('err', PyExceptionToJs(PyJsTempException))
        try:
            return var.get('strOnError')
        finally:
            if PyJsHolder_657272_89268985 is not None:
                var.own['err'] = PyJsHolder_657272_89268985
            else:
                del var.own['err']
            del PyJsHolder_657272_89268985
PyJsHoisted_fp_os_.func_name = 'fp_os'
var.put('fp_os', PyJsHoisted_fp_os_)
@Js
def PyJsHoisted_fp_plugins_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['i'])
    var.put('strInputData', Js([]))
    if (var.get('navigator').get('plugins').get('length')==Js(0.0)):
        return Js('noPlugins')
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('navigator').get('plugins').get('length')):
        try:
            var.get('strInputData').callprop('push', var.get('navigator').get('plugins').get(var.get('i')).get('name'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('strTmp', var.get('strInputData').callprop('join', Js('|')))
    var.put('strOut', var.get('strTmp'))
    return var.get('strOut')
PyJsHoisted_fp_plugins_.func_name = 'fp_plugins'
var.put('fp_plugins', PyJsHoisted_fp_plugins_)
@Js
def PyJsHoisted_fp_timezone_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['numGMTHours', 'dtDate', 'strOnError', 'numOffset', 'numOut'])
    Js('use strict')
    pass
    var.put('strOnError', Js('Error'))
    var.put('dtDate', var.get(u"null"))
    var.put('numOffset', var.get(u"null"))
    var.put('numGMTHours', var.get(u"null"))
    var.put('numOut', var.get(u"null"))
    try:
        var.put('dtDate', var.get('Date').create())
        var.put('numOffset', var.get('dtDate').callprop('getTimezoneOffset'))
        var.put('numGMTHours', ((var.get('numOffset')/Js(60.0))*(-Js(1.0))))
        var.put('numOut', var.get('numGMTHours'))
        return var.get('numOut')
    except PyJsException as PyJsTempException:
        PyJsHolder_657272_38833162 = var.own.get('err')
        var.force_own_put('err', PyExceptionToJs(PyJsTempException))
        try:
            return var.get('strOnError')
        finally:
            if PyJsHolder_657272_38833162 is not None:
                var.own['err'] = PyJsHolder_657272_38833162
            else:
                del var.own['err']
            del PyJsHolder_657272_38833162
PyJsHoisted_fp_timezone_.func_name = 'fp_timezone'
var.put('fp_timezone', PyJsHoisted_fp_timezone_)
@Js
def PyJsHoisted_fp_useragent_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['strUserAgent', 'strTmp', 'strSep', 'strOut'])
    Js('use strict')
    pass
    var.put('strSep', Js('|'))
    var.put('strTmp', var.get(u"null"))
    var.put('strUserAgent', var.get(u"null"))
    var.put('strOut', var.get(u"null"))
    var.put('strUserAgent', var.get('navigator').get('userAgent').callprop('toLowerCase'))
    var.put('strTmp', ((var.get('strUserAgent')+var.get('strSep'))+var.get('navigator').get('platform')))
    if var.get('navigator').get('cpuClass'):
        var.put('strTmp', (var.get('strSep')+var.get('navigator').get('cpuClass')), '+')
    if var.get('navigator').get('browserLanguage'):
        var.put('strTmp', (var.get('strSep')+var.get('navigator').get('browserLanguage')), '+')
    else:
        var.put('strTmp', (var.get('strSep')+var.get('navigator').get('language')), '+')
    var.put('strOut', var.get('strTmp'))
    return var.get('strOut')
PyJsHoisted_fp_useragent_.func_name = 'fp_useragent'
var.put('fp_useragent', PyJsHoisted_fp_useragent_)
@Js
def PyJsHoisted_createhash_(key, seed, this, arguments, var=var):
    var = Scope({'key':key, 'seed':seed, 'this':this, 'arguments':arguments}, var)
    var.registers(['key', 'remainder', 'h1', 'seed', 'k1', 'h1b', 'i', 'c2', 'c1', 'bytes'])
    pass
    var.put('remainder', (var.get('key').get('length')&Js(3.0)))
    var.put('bytes', (var.get('key').get('length')-var.get('remainder')))
    var.put('h1', var.get('seed'))
    var.put('c1', Js(3432918353))
    var.put('c2', Js(461845907))
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('bytes')):
        def PyJs_LONG_9_(var=var):
            return var.put('k1', ((((var.get('key').callprop('charCodeAt', var.get('i'))&Js(255))|((var.get('key').callprop('charCodeAt', var.put('i',Js(var.get('i').to_number())+Js(1)))&Js(255))<<Js(8.0)))|((var.get('key').callprop('charCodeAt', var.put('i',Js(var.get('i').to_number())+Js(1)))&Js(255))<<Js(16.0)))|((var.get('key').callprop('charCodeAt', var.put('i',Js(var.get('i').to_number())+Js(1)))&Js(255))<<Js(24.0))))
        PyJs_LONG_9_()
        var.put('i',Js(var.get('i').to_number())+Js(1))
        var.put('k1', ((((var.get('k1')&Js(65535))*var.get('c1'))+(((PyJsBshift(var.get('k1'),Js(16.0))*var.get('c1'))&Js(65535))<<Js(16.0)))&Js(4294967295)))
        var.put('k1', ((var.get('k1')<<Js(15.0))|PyJsBshift(var.get('k1'),Js(17.0))))
        var.put('k1', ((((var.get('k1')&Js(65535))*var.get('c2'))+(((PyJsBshift(var.get('k1'),Js(16.0))*var.get('c2'))&Js(65535))<<Js(16.0)))&Js(4294967295)))
        var.put('h1', var.get('k1'), '^')
        var.put('h1', ((var.get('h1')<<Js(13.0))|PyJsBshift(var.get('h1'),Js(19.0))))
        var.put('h1b', ((((var.get('h1')&Js(65535))*Js(5.0))+(((PyJsBshift(var.get('h1'),Js(16.0))*Js(5.0))&Js(65535))<<Js(16.0)))&Js(4294967295)))
        var.put('h1', (((var.get('h1b')&Js(65535))+Js(27492))+(((PyJsBshift(var.get('h1b'),Js(16.0))+Js(58964))&Js(65535))<<Js(16.0))))
    var.put('k1', Js(0.0))
    while 1:
        SWITCHED = False
        CONDITION = (var.get('remainder'))
        if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
            SWITCHED = True
            var.put('k1', ((var.get('key').callprop('charCodeAt', (var.get('i')+Js(2.0)))&Js(255))<<Js(16.0)), '^')
        if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
            SWITCHED = True
            var.put('k1', ((var.get('key').callprop('charCodeAt', (var.get('i')+Js(1.0)))&Js(255))<<Js(8.0)), '^')
        if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
            SWITCHED = True
            var.put('k1', (var.get('key').callprop('charCodeAt', var.get('i'))&Js(255)), '^')
            var.put('k1', ((((var.get('k1')&Js(65535))*var.get('c1'))+(((PyJsBshift(var.get('k1'),Js(16.0))*var.get('c1'))&Js(65535))<<Js(16.0)))&Js(4294967295)))
            var.put('k1', ((var.get('k1')<<Js(15.0))|PyJsBshift(var.get('k1'),Js(17.0))))
            var.put('k1', ((((var.get('k1')&Js(65535))*var.get('c2'))+(((PyJsBshift(var.get('k1'),Js(16.0))*var.get('c2'))&Js(65535))<<Js(16.0)))&Js(4294967295)))
            var.put('h1', var.get('k1'), '^')
        SWITCHED = True
        break
    var.put('h1', var.get('key').get('length'), '^')
    var.put('h1', PyJsBshift(var.get('h1'),Js(16.0)), '^')
    var.put('h1', ((((var.get('h1')&Js(65535))*Js(2246822507))+(((PyJsBshift(var.get('h1'),Js(16.0))*Js(2246822507))&Js(65535))<<Js(16.0)))&Js(4294967295)))
    var.put('h1', PyJsBshift(var.get('h1'),Js(13.0)), '^')
    var.put('h1', ((((var.get('h1')&Js(65535))*Js(3266489909))+(((PyJsBshift(var.get('h1'),Js(16.0))*Js(3266489909))&Js(65535))<<Js(16.0)))&Js(4294967295)))
    var.put('h1', PyJsBshift(var.get('h1'),Js(16.0)), '^')
    return PyJsBshift(var.get('h1'),Js(0.0))
PyJsHoisted_createhash_.func_name = 'createhash'
var.put('createhash', PyJsHoisted_createhash_)
var.put('pbox', var.get('Array')())
var.put('sbox0', var.get('Array')())
var.put('sbox1', var.get('Array')())
var.put('sbox2', var.get('Array')())
var.put('sbox3', var.get('Array')())
var.put('key_old', var.get(u"null"))
var.put('pbox_def', var.get('Array')(Js(608135816), Js(2242054355), Js(320440878), Js(57701188), Js(2752067618), Js(698298832), Js(137296536), Js(3964562569), Js(1160258022), Js(953160567), Js(3193202383), Js(887688300), Js(3232508343), Js(3380367581), Js(1065670069), Js(3041331479), Js(2450970073), Js(2306472731)))
def PyJs_LONG_0_(var=var):
    return var.get('Array')(Js(3509652390), Js(2564797868), Js(805139163), Js(3491422135), Js(3101798381), Js(1780907670), Js(3128725573), Js(4046225305), Js(614570311), Js(3012652279), Js(134345442), Js(2240740374), Js(1667834072), Js(1901547113), Js(2757295779), Js(4103290238), Js(227898511), Js(1921955416), Js(1904987480), Js(2182433518), Js(2069144605), Js(3260701109), Js(2620446009), Js(720527379), Js(3318853667), Js(677414384), Js(3393288472), Js(3101374703), Js(2390351024), Js(1614419982), Js(1822297739), Js(2954791486), Js(3608508353), Js(3174124327), Js(2024746970), Js(1432378464), Js(3864339955), Js(2857741204), Js(1464375394), Js(1676153920), Js(1439316330), Js(715854006), Js(3033291828), Js(289532110), Js(2706671279), Js(2087905683), Js(3018724369), Js(1668267050), Js(732546397), Js(1947742710), Js(3462151702), Js(2609353502), Js(2950085171), Js(1814351708), Js(2050118529), Js(680887927), Js(999245976), Js(1800124847), Js(3300911131), Js(1713906067), Js(1641548236), Js(4213287313), Js(1216130144), Js(1575780402), Js(4018429277), Js(3917837745), Js(3693486850), Js(3949271944), Js(596196993), Js(3549867205), Js(258830323), Js(2213823033), Js(772490370), Js(2760122372), Js(1774776394), Js(2652871518), Js(566650946), Js(4142492826), Js(1728879713), Js(2882767088), Js(1783734482), Js(3629395816), Js(2517608232), Js(2874225571), Js(1861159788), Js(326777828), Js(3124490320), Js(2130389656), Js(2716951837), Js(967770486), Js(1724537150), Js(2185432712), Js(2364442137), Js(1164943284), Js(2105845187), Js(998989502), Js(3765401048), Js(2244026483), Js(1075463327), Js(1455516326), Js(1322494562), Js(910128902), Js(469688178), Js(1117454909), Js(936433444), Js(3490320968), Js(3675253459), Js(1240580251), Js(122909385), Js(2157517691), Js(634681816), Js(4142456567), Js(3825094682), Js(3061402683), Js(2540495037), Js(79693498), Js(3249098678), Js(1084186820), Js(1583128258), Js(426386531), Js(1761308591), Js(1047286709), Js(322548459), Js(995290223), Js(1845252383), Js(2603652396), Js(3431023940), Js(2942221577), Js(3202600964), Js(3727903485), Js(1712269319), Js(422464435), Js(3234572375), Js(1170764815), Js(3523960633), Js(3117677531), Js(1434042557), Js(442511882), Js(3600875718), Js(1076654713), Js(1738483198), Js(4213154764), Js(2393238008), Js(3677496056), Js(1014306527), Js(4251020053), Js(793779912), Js(2902807211), Js(842905082), Js(4246964064), Js(1395751752), Js(1040244610), Js(2656851899), Js(3396308128), Js(445077038), Js(3742853595), Js(3577915638), Js(679411651), Js(2892444358), Js(2354009459), Js(1767581616), Js(3150600392), Js(3791627101), Js(3102740896), Js(284835224), Js(4246832056), Js(1258075500), Js(768725851), Js(2589189241), Js(3069724005), Js(3532540348), Js(1274779536), Js(3789419226), Js(2764799539), Js(1660621633), Js(3471099624), Js(4011903706), Js(913787905), Js(3497959166), Js(737222580), Js(2514213453), Js(2928710040), Js(3937242737), Js(1804850592), Js(3499020752), Js(2949064160), Js(2386320175), Js(2390070455), Js(2415321851), Js(4061277028), Js(2290661394), Js(2416832540), Js(1336762016), Js(1754252060), Js(3520065937), Js(3014181293), Js(791618072), Js(3188594551), Js(3933548030), Js(2332172193), Js(3852520463), Js(3043980520), Js(413987798), Js(3465142937), Js(3030929376), Js(4245938359), Js(2093235073), Js(3534596313), Js(375366246), Js(2157278981), Js(2479649556), Js(555357303), Js(3870105701), Js(2008414854), Js(3344188149), Js(4221384143), Js(3956125452), Js(2067696032), Js(3594591187), Js(2921233993), Js(2428461), Js(544322398), Js(577241275), Js(1471733935), Js(610547355), Js(4027169054), Js(1432588573), Js(1507829418), Js(2025931657), Js(3646575487), Js(545086370), Js(48609733), Js(2200306550), Js(1653985193), Js(298326376), Js(1316178497), Js(3007786442), Js(2064951626), Js(458293330), Js(2589141269), Js(3591329599), Js(3164325604), Js(727753846), Js(2179363840), Js(146436021), Js(1461446943), Js(4069977195), Js(705550613), Js(3059967265), Js(3887724982), Js(4281599278), Js(3313849956), Js(1404054877), Js(2845806497), Js(146425753), Js(1854211946))
var.put('sbox0_def', PyJs_LONG_0_())
def PyJs_LONG_1_(var=var):
    return var.get('Array')(Js(1266315497), Js(3048417604), Js(3681880366), Js(3289982499), Js(2909710000), Js(1235738493), Js(2632868024), Js(2414719590), Js(3970600049), Js(1771706367), Js(1449415276), Js(3266420449), Js(422970021), Js(1963543593), Js(2690192192), Js(3826793022), Js(1062508698), Js(1531092325), Js(1804592342), Js(2583117782), Js(2714934279), Js(4024971509), Js(1294809318), Js(4028980673), Js(1289560198), Js(2221992742), Js(1669523910), Js(35572830), Js(157838143), Js(1052438473), Js(1016535060), Js(1802137761), Js(1753167236), Js(1386275462), Js(3080475397), Js(2857371447), Js(1040679964), Js(2145300060), Js(2390574316), Js(1461121720), Js(2956646967), Js(4031777805), Js(4028374788), Js(33600511), Js(2920084762), Js(1018524850), Js(629373528), Js(3691585981), Js(3515945977), Js(2091462646), Js(2486323059), Js(586499841), Js(988145025), Js(935516892), Js(3367335476), Js(2599673255), Js(2839830854), Js(265290510), Js(3972581182), Js(2759138881), Js(3795373465), Js(1005194799), Js(847297441), Js(406762289), Js(1314163512), Js(1332590856), Js(1866599683), Js(4127851711), Js(750260880), Js(613907577), Js(1450815602), Js(3165620655), Js(3734664991), Js(3650291728), Js(3012275730), Js(3704569646), Js(1427272223), Js(778793252), Js(1343938022), Js(2676280711), Js(2052605720), Js(1946737175), Js(3164576444), Js(3914038668), Js(3967478842), Js(3682934266), Js(1661551462), Js(3294938066), Js(4011595847), Js(840292616), Js(3712170807), Js(616741398), Js(312560963), Js(711312465), Js(1351876610), Js(322626781), Js(1910503582), Js(271666773), Js(2175563734), Js(1594956187), Js(70604529), Js(3617834859), Js(1007753275), Js(1495573769), Js(4069517037), Js(2549218298), Js(2663038764), Js(504708206), Js(2263041392), Js(3941167025), Js(2249088522), Js(1514023603), Js(1998579484), Js(1312622330), Js(694541497), Js(2582060303), Js(2151582166), Js(1382467621), Js(776784248), Js(2618340202), Js(3323268794), Js(2497899128), Js(2784771155), Js(503983604), Js(4076293799), Js(907881277), Js(423175695), Js(432175456), Js(1378068232), Js(4145222326), Js(3954048622), Js(3938656102), Js(3820766613), Js(2793130115), Js(2977904593), Js(26017576), Js(3274890735), Js(3194772133), Js(1700274565), Js(1756076034), Js(4006520079), Js(3677328699), Js(720338349), Js(1533947780), Js(354530856), Js(688349552), Js(3973924725), Js(1637815568), Js(332179504), Js(3949051286), Js(53804574), Js(2852348879), Js(3044236432), Js(1282449977), Js(3583942155), Js(3416972820), Js(4006381244), Js(1617046695), Js(2628476075), Js(3002303598), Js(1686838959), Js(431878346), Js(2686675385), Js(1700445008), Js(1080580658), Js(1009431731), Js(832498133), Js(3223435511), Js(2605976345), Js(2271191193), Js(2516031870), Js(1648197032), Js(4164389018), Js(2548247927), Js(300782431), Js(375919233), Js(238389289), Js(3353747414), Js(2531188641), Js(2019080857), Js(1475708069), Js(455242339), Js(2609103871), Js(448939670), Js(3451063019), Js(1395535956), Js(2413381860), Js(1841049896), Js(1491858159), Js(885456874), Js(4264095073), Js(4001119347), Js(1565136089), Js(3898914787), Js(1108368660), Js(540939232), Js(1173283510), Js(2745871338), Js(3681308437), Js(4207628240), Js(3343053890), Js(4016749493), Js(1699691293), Js(1103962373), Js(3625875870), Js(2256883143), Js(3830138730), Js(1031889488), Js(3479347698), Js(1535977030), Js(4236805024), Js(3251091107), Js(2132092099), Js(1774941330), Js(1199868427), Js(1452454533), Js(157007616), Js(2904115357), Js(342012276), Js(595725824), Js(1480756522), Js(206960106), Js(497939518), Js(591360097), Js(863170706), Js(2375253569), Js(3596610801), Js(1814182875), Js(2094937945), Js(3421402208), Js(1082520231), Js(3463918190), Js(2785509508), Js(435703966), Js(3908032597), Js(1641649973), Js(2842273706), Js(3305899714), Js(1510255612), Js(2148256476), Js(2655287854), Js(3276092548), Js(4258621189), Js(236887753), Js(3681803219), Js(274041037), Js(1734335097), Js(3815195456), Js(3317970021), Js(1899903192), Js(1026095262), Js(4050517792), Js(356393447), Js(2410691914), Js(3873677099), Js(3682840055))
var.put('sbox1_def', PyJs_LONG_1_())
def PyJs_LONG_2_(var=var):
    return var.get('Array')(Js(3913112168), Js(2491498743), Js(4132185628), Js(2489919796), Js(1091903735), Js(1979897079), Js(3170134830), Js(3567386728), Js(3557303409), Js(857797738), Js(1136121015), Js(1342202287), Js(507115054), Js(2535736646), Js(337727348), Js(3213592640), Js(1301675037), Js(2528481711), Js(1895095763), Js(1721773893), Js(3216771564), Js(62756741), Js(2142006736), Js(835421444), Js(2531993523), Js(1442658625), Js(3659876326), Js(2882144922), Js(676362277), Js(1392781812), Js(170690266), Js(3921047035), Js(1759253602), Js(3611846912), Js(1745797284), Js(664899054), Js(1329594018), Js(3901205900), Js(3045908486), Js(2062866102), Js(2865634940), Js(3543621612), Js(3464012697), Js(1080764994), Js(553557557), Js(3656615353), Js(3996768171), Js(991055499), Js(499776247), Js(1265440854), Js(648242737), Js(3940784050), Js(980351604), Js(3713745714), Js(1749149687), Js(3396870395), Js(4211799374), Js(3640570775), Js(1161844396), Js(3125318951), Js(1431517754), Js(545492359), Js(4268468663), Js(3499529547), Js(1437099964), Js(2702547544), Js(3433638243), Js(2581715763), Js(2787789398), Js(1060185593), Js(1593081372), Js(2418618748), Js(4260947970), Js(69676912), Js(2159744348), Js(86519011), Js(2512459080), Js(3838209314), Js(1220612927), Js(3339683548), Js(133810670), Js(1090789135), Js(1078426020), Js(1569222167), Js(845107691), Js(3583754449), Js(4072456591), Js(1091646820), Js(628848692), Js(1613405280), Js(3757631651), Js(526609435), Js(236106946), Js(48312990), Js(2942717905), Js(3402727701), Js(1797494240), Js(859738849), Js(992217954), Js(4005476642), Js(2243076622), Js(3870952857), Js(3732016268), Js(765654824), Js(3490871365), Js(2511836413), Js(1685915746), Js(3888969200), Js(1414112111), Js(2273134842), Js(3281911079), Js(4080962846), Js(172450625), Js(2569994100), Js(980381355), Js(4109958455), Js(2819808352), Js(2716589560), Js(2568741196), Js(3681446669), Js(3329971472), Js(1835478071), Js(660984891), Js(3704678404), Js(4045999559), Js(3422617507), Js(3040415634), Js(1762651403), Js(1719377915), Js(3470491036), Js(2693910283), Js(3642056355), Js(3138596744), Js(1364962596), Js(2073328063), Js(1983633131), Js(926494387), Js(3423689081), Js(2150032023), Js(4096667949), Js(1749200295), Js(3328846651), Js(309677260), Js(2016342300), Js(1779581495), Js(3079819751), Js(111262694), Js(1274766160), Js(443224088), Js(298511866), Js(1025883608), Js(3806446537), Js(1145181785), Js(168956806), Js(3641502830), Js(3584813610), Js(1689216846), Js(3666258015), Js(3200248200), Js(1692713982), Js(2646376535), Js(4042768518), Js(1618508792), Js(1610833997), Js(3523052358), Js(4130873264), Js(2001055236), Js(3610705100), Js(2202168115), Js(4028541809), Js(2961195399), Js(1006657119), Js(2006996926), Js(3186142756), Js(1430667929), Js(3210227297), Js(1314452623), Js(4074634658), Js(4101304120), Js(2273951170), Js(1399257539), Js(3367210612), Js(3027628629), Js(1190975929), Js(2062231137), Js(2333990788), Js(2221543033), Js(2438960610), Js(1181637006), Js(548689776), Js(2362791313), Js(3372408396), Js(3104550113), Js(3145860560), Js(296247880), Js(1970579870), Js(3078560182), Js(3769228297), Js(1714227617), Js(3291629107), Js(3898220290), Js(166772364), Js(1251581989), Js(493813264), Js(448347421), Js(195405023), Js(2709975567), Js(677966185), Js(3703036547), Js(1463355134), Js(2715995803), Js(1338867538), Js(1343315457), Js(2802222074), Js(2684532164), Js(233230375), Js(2599980071), Js(2000651841), Js(3277868038), Js(1638401717), Js(4028070440), Js(3237316320), Js(6314154), Js(819756386), Js(300326615), Js(590932579), Js(1405279636), Js(3267499572), Js(3150704214), Js(2428286686), Js(3959192993), Js(3461946742), Js(1862657033), Js(1266418056), Js(963775037), Js(2089974820), Js(2263052895), Js(1917689273), Js(448879540), Js(3550394620), Js(3981727096), Js(150775221), Js(3627908307), Js(1303187396), Js(508620638), Js(2975983352), Js(2726630617), Js(1817252668), Js(1876281319), Js(1457606340), Js(908771278), Js(3720792119), Js(3617206836), Js(2455994898), Js(1729034894), Js(1080033504))
var.put('sbox2_def', PyJs_LONG_2_())
def PyJs_LONG_3_(var=var):
    return var.get('Array')(Js(976866871), Js(3556439503), Js(2881648439), Js(1522871579), Js(1555064734), Js(1336096578), Js(3548522304), Js(2579274686), Js(3574697629), Js(3205460757), Js(3593280638), Js(3338716283), Js(3079412587), Js(564236357), Js(2993598910), Js(1781952180), Js(1464380207), Js(3163844217), Js(3332601554), Js(1699332808), Js(1393555694), Js(1183702653), Js(3581086237), Js(1288719814), Js(691649499), Js(2847557200), Js(2895455976), Js(3193889540), Js(2717570544), Js(1781354906), Js(1676643554), Js(2592534050), Js(3230253752), Js(1126444790), Js(2770207658), Js(2633158820), Js(2210423226), Js(2615765581), Js(2414155088), Js(3127139286), Js(673620729), Js(2805611233), Js(1269405062), Js(4015350505), Js(3341807571), Js(4149409754), Js(1057255273), Js(2012875353), Js(2162469141), Js(2276492801), Js(2601117357), Js(993977747), Js(3918593370), Js(2654263191), Js(753973209), Js(36408145), Js(2530585658), Js(25011837), Js(3520020182), Js(2088578344), Js(530523599), Js(2918365339), Js(1524020338), Js(1518925132), Js(3760827505), Js(3759777254), Js(1202760957), Js(3985898139), Js(3906192525), Js(674977740), Js(4174734889), Js(2031300136), Js(2019492241), Js(3983892565), Js(4153806404), Js(3822280332), Js(352677332), Js(2297720250), Js(60907813), Js(90501309), Js(3286998549), Js(1016092578), Js(2535922412), Js(2839152426), Js(457141659), Js(509813237), Js(4120667899), Js(652014361), Js(1966332200), Js(2975202805), Js(55981186), Js(2327461051), Js(676427537), Js(3255491064), Js(2882294119), Js(3433927263), Js(1307055953), Js(942726286), Js(933058658), Js(2468411793), Js(3933900994), Js(4215176142), Js(1361170020), Js(2001714738), Js(2830558078), Js(3274259782), Js(1222529897), Js(1679025792), Js(2729314320), Js(3714953764), Js(1770335741), Js(151462246), Js(3013232138), Js(1682292957), Js(1483529935), Js(471910574), Js(1539241949), Js(458788160), Js(3436315007), Js(1807016891), Js(3718408830), Js(978976581), Js(1043663428), Js(3165965781), Js(1927990952), Js(4200891579), Js(2372276910), Js(3208408903), Js(3533431907), Js(1412390302), Js(2931980059), Js(4132332400), Js(1947078029), Js(3881505623), Js(4168226417), Js(2941484381), Js(1077988104), Js(1320477388), Js(886195818), Js(18198404), Js(3786409000), Js(2509781533), Js(112762804), Js(3463356488), Js(1866414978), Js(891333506), Js(18488651), Js(661792760), Js(1628790961), Js(3885187036), Js(3141171499), Js(876946877), Js(2693282273), Js(1372485963), Js(791857591), Js(2686433993), Js(3759982718), Js(3167212022), Js(3472953795), Js(2716379847), Js(445679433), Js(3561995674), Js(3504004811), Js(3574258232), Js(54117162), Js(3331405415), Js(2381918588), Js(3769707343), Js(4154350007), Js(1140177722), Js(4074052095), Js(668550556), Js(3214352940), Js(367459370), Js(261225585), Js(2610173221), Js(4209349473), Js(3468074219), Js(3265815641), Js(314222801), Js(3066103646), Js(3808782860), Js(282218597), Js(3406013506), Js(3773591054), Js(379116347), Js(1285071038), Js(846784868), Js(2669647154), Js(3771962079), Js(3550491691), Js(2305946142), Js(453669953), Js(1268987020), Js(3317592352), Js(3279303384), Js(3744833421), Js(2610507566), Js(3859509063), Js(266596637), Js(3847019092), Js(517658769), Js(3462560207), Js(3443424879), Js(370717030), Js(4247526661), Js(2224018117), Js(4143653529), Js(4112773975), Js(2788324899), Js(2477274417), Js(1456262402), Js(2901442914), Js(1517677493), Js(1846949527), Js(2295493580), Js(3734397586), Js(2176403920), Js(1280348187), Js(1908823572), Js(3871786941), Js(846861322), Js(1172426758), Js(3287448474), Js(3383383037), Js(1655181056), Js(3139813346), Js(901632758), Js(1897031941), Js(2986607138), Js(3066810236), Js(3447102507), Js(1393639104), Js(373351379), Js(950779232), Js(625454576), Js(3124240540), Js(4148612726), Js(2007998917), Js(544563296), Js(2244738638), Js(2330496472), Js(2058025392), Js(1291430526), Js(424198748), Js(50039436), Js(29584100), Js(3605783033), Js(2429876329), Js(2791104160), Js(1057563949), Js(3255363231), Js(3075367218), Js(3463963227), Js(1469046755), Js(985887462))
var.put('sbox3_def', PyJs_LONG_3_())
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
@Js
def PyJs_anonymous_5_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['S', 'SHA256', 'j', 'K', 'i', 'H', 'x'])
    @Js
    def PyJsHoisted_x_(num, root, this, arguments, var=var):
        var = Scope({'num':num, 'root':root, 'this':this, 'arguments':arguments}, var)
        var.registers(['num', 'root'])
        return (((var.get('Math').callprop('pow', var.get('num'), (Js(1.0)/var.get('root')))%Js(1.0))*Js(4294967296.0))|Js(0.0))
    PyJsHoisted_x_.func_name = 'x'
    var.put('x', PyJsHoisted_x_)
    @Js
    def PyJsHoisted_S_(X, n, this, arguments, var=var):
        var = Scope({'X':X, 'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['X', 'n'])
        return (PyJsBshift(var.get('X'),var.get('n'))|(var.get('X')<<(Js(32.0)-var.get('n'))))
    PyJsHoisted_S_.func_name = 'S'
    var.put('S', PyJsHoisted_S_)
    @Js
    def PyJsHoisted_SHA256_(b, this, arguments, var=var):
        var = Scope({'b':b, 'this':this, 'arguments':arguments}, var)
        var.registers(['m', 'W', 'a', 'y', 'l', 'z', 'b', 's', 'HASH'])
        var.put('HASH', var.get('H').callprop('slice', var.put('i', Js(0.0))))
        var.put('s', var.get('unescape')(var.get('encodeURI')(var.get('b'))))
        var.put('W', Js([]))
        var.put('l', var.get('s').get('length'))
        var.put('m', Js([]))
        #for JS loop
        
        while (var.get('i')<var.get('l')):
            var.get('m').put((var.get('i')>>Js(2.0)), ((var.get('s').callprop('charCodeAt', var.get('i'))&Js(255))<<(Js(8.0)*(Js(3.0)-((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))%Js(4.0))))), '|')
        
        var.put('l', Js(8.0), '*')
        var.get('m').put((var.get('l')>>Js(5.0)), (Js(128)<<(Js(24.0)-(var.get('l')%Js(32.0)))), '|')
        var.get('m').put(var.put('z', (((var.get('l')+Js(64.0))>>Js(5.0))|Js(15.0))), var.get('l'))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('z')):
            try:
                var.put('a', var.get('HASH').callprop('slice', var.put('j', Js(0.0)), Js(8.0)))
                #for JS loop
                
                while (var.get('j')<Js(64.0)):
                    try:
                        if (var.get('j')<Js(16.0)):
                            var.get('W').put(var.get('j'), var.get('m').get((var.get('j')+var.get('i'))))
                        else:
                            def PyJs_LONG_6_(var=var):
                                return (((((var.get('S')(var.put('y', var.get('W').get((var.get('j')-Js(2.0)))), Js(17.0))^var.get('S')(var.get('y'), Js(19.0)))^PyJsBshift(var.get('y'),Js(10.0)))+(var.get('W').get((var.get('j')-Js(7.0)))|Js(0.0)))+((var.get('S')(var.put('y', var.get('W').get((var.get('j')-Js(15.0)))), Js(7.0))^var.get('S')(var.get('y'), Js(18.0)))^PyJsBshift(var.get('y'),Js(3.0))))+(var.get('W').get((var.get('j')-Js(16.0)))|Js(0.0)))
                            var.get('W').put(var.get('j'), PyJs_LONG_6_())
                        def PyJs_LONG_7_(var=var):
                            return (var.put('y', ((((var.get('a').callprop('pop')+((var.get('S')(var.put('b', var.get('a').get('4')), Js(6.0))^var.get('S')(var.get('b'), Js(11.0)))^var.get('S')(var.get('b'), Js(25.0))))+(((var.get('b')&var.get('a').get('5'))^((~var.get('b'))&var.get('a').get('6')))+var.get('K').get(var.get('j'))))|Js(0.0))+(var.get('W').get((var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1)))|Js(0.0))))+((var.get('S')(var.put('l', var.get('a').get('0')), Js(2.0))^var.get('S')(var.get('l'), Js(13.0)))^var.get('S')(var.get('l'), Js(22.0))))
                        var.get('a').callprop('unshift', (PyJs_LONG_7_()+(((var.get('l')&var.get('a').get('1'))^(var.get('a').get('1')&var.get('a').get('2')))^(var.get('a').get('2')&var.get('l')))))
                    finally:
                            var.get('a').put('4', var.get('y'), '+')
                #for JS loop
                var.put('j', Js(8.0))
                while (var.put('j',Js(var.get('j').to_number())-Js(1))+Js(1)):
                    var.get('HASH').put(var.get('j'), (var.get('a').get(var.get('j'))+var.get('HASH').get(var.get('j'))))
                
            finally:
                    var.put('i', Js(16.0), '+')
        #for JS loop
        var.put('s', Js(''))
        while (var.get('j')<Js(63.0)):
            var.put('s', ((var.get('HASH').get((var.put('j',Js(var.get('j').to_number())+Js(1))>>Js(3.0)))>>(Js(4.0)*(Js(7.0)-(var.get('j')%Js(8.0)))))&Js(15.0)).callprop('toString', Js(16.0)), '+')
        
        return var.get('s')
    PyJsHoisted_SHA256_.func_name = 'SHA256'
    var.put('SHA256', PyJsHoisted_SHA256_)
    var.put('i', Js(1.0))
    var.put('K', Js([]))
    var.put('H', Js([]))
    while (var.put('i',Js(var.get('i').to_number())+Js(1))<Js(18.0)):
        #for JS loop
        var.put('j', (var.get('i')*var.get('i')))
        while (var.get('j')<Js(312.0)):
            try:
                var.get('K').put(var.get('j'), Js(1.0))
            finally:
                    var.put('j', var.get('i'), '+')
    pass
    #for JS loop
    PyJsComma(var.put('i', Js(1.0)),var.put('j', Js(0.0)))
    while (var.get('i')<Js(313.0)):
        if var.get('K').get(var.put('i',Js(var.get('i').to_number())+Js(1))).neg():
            var.get('H').put(var.get('j'), var.get('x')(var.get('i'), Js(2.0)))
            var.get('K').put((var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1)), var.get('x')(var.get('i'), Js(3.0)))
    
    pass
    pass
    return var.get('SHA256')
PyJs_anonymous_5_._set_name('anonymous')
var.put('sha256', PyJs_anonymous_5_())
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
# Add lib to the module scope
blowfish = var.to_python()

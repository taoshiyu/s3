CryptoJS = require('crypto-js')
const window = global
// x_s3_s4e= _s3[_0x2ae1('0x13')][0x5a](window[_0xd71476[_0x2ae1('0x156')](_ssc[0x14] + _ssc[0x13], _ssc[0x12]) + _ssc[0x16]](_0x26644a) + _0xd71476['BAPox'] + _s3_tid, _0x214f53, _0x51fc87, _0x47b591)
function get_x_s3_s4e(x_s3_tid, x_s3_sid,ip) {


    var _0x7db3eb = [x_s3_tid + ';' + x_s3_sid];

    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0'
    _0x7db3eb.push(ua)
    _0x7db3eb.push("zh-CN")
    _0x7db3eb.push('124.04347527516074')
    _0x7db3eb.push("Win32")
    _0x7db3eb.push([ip])
    _0x7db3eb.push("c2331586")
    _0x7db3eb.push([
        "1920",
        "1080",
        "1",
        "24"
    ])
    _0x7db3eb.push(-480)
    _0x7db3eb.push("https://www.shenzhenair.com/szair_B2C/")

    var _0x56055b = function (_0xd62ffc) {
        var _0x340501, _0x595b7e = (typeof _0xd62ffc === "undefined") ? -0x1 : _0xd62ffc;
        do {
            _0x340501 = Math['round']((Math['random']() * 0xff));
        } while (_0x340501 === _0x595b7e);
        var _0x3aefc8 = _0x340501['toString'](0x10);
        return (_0x3aefc8['lengtwh'] == 0x1) ? ('0' + _0x3aefc8) : _0x3aefc8;
    };

    function _0x3ffcf8(_0x5f0ceb) {
        var _0xfdf81d = '';
        for (var _0x105424 = 0x0; _0x105424 < _0x5f0ceb; _0x105424++) {
            _0xfdf81d += _0x56055b();
        }
        return _0xfdf81d;
    }

    _0x7db3eb.push(_0x3ffcf8(0x14))
    _0x7db3eb.push("c8823e45")
    _0x7db3eb.push('(https://www.shenzhenair.com/vodka/v1/js/sw.js:1:256343)')


    _0x245c1f = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
        "Win32",
        "zh-CN",
        "1920",
        "1080",
        "1",
        "24",
        -480,
        "https://www.shenzhenair.com/szair_B2C/",
        "c8823e45",
        "124.04347527516074",
        ["38.87.67.251"]
    ]['join']('') + 'c'
    _0x7db3eb.push(_0x3ffcf8(0x4) + CryptoJS.MD5(_0x245c1f).toString())
    _0x7db3eb.push([
        [
            2,
            2,
            2,
            2,
            2
        ],
        [
            2,
            2,
            3,
            2,
            3,
            3
        ],
        2,
        2,
        2,
        [
            3,
            2,
            3,
            2,
            2,
            3
        ],
        [
            2,
            2,
            2,
            1,
            1,
            1,
            3,
            0
        ],
        [
            2
        ],
        [
            2
        ],
        2,
        [
            2
        ],
        [
            2,
            2
        ],
        2,
        2
    ])
    _0x7db3eb.push([])
    _0x7db3eb.push(2)
    console.log(_0x7db3eb)
    console.log(JSON.stringify(_0x7db3eb))

    var _0x1ac89a = x_s3_tid.split(':')
    _0x461fc8 = _0x1ac89a[2]

    function _0x10e125(_0x1b5e95) {
        var _0x308ae7 = _0x1b5e95['toString']();
        var _0x27b0d0 = new Array();
        for (var _0x49a7c5 = 0x0; (_0x49a7c5 < _0x308ae7['length']); _0x49a7c5 += 0x2) {
            _0x27b0d0['push'](parseInt(_0x308ae7['substr'](_0x49a7c5, 0x2), 0x10));
        }
        return _0x27b0d0;
    }

    //======================================================================uuid1/2/3--------->countArray======================================================================

    function getMode(_0x1bda09) {
        return parseInt(_0x1bda09['split']('-')[0x0], 0x10) % 0x2;
    }

    mode = getMode(_0x461fc8)
    console.log('mode === ', mode)
    var prime = [0x18b1d, 0x18b93, 0x18bd5, 0x18c17, 0x18c97, 0x18d1f, 0x18d9d, 0x18dcd, 0x18e33, 0x18e8f, 0x18ee9, 0x18f55, 0x18fb9, 0x1903d, 0x1909f, 0x19111, 0x191ad, 0x19229, 0x192af, 0x1933f, 0x193df, 0x19457, 0x194bd, 0x1952b, 0x195d1, 0x19637, 0x19697, 0x196f3, 0x19775, 0x197e1, 0x19865, 0x198e5, 0x28f7, 0x2903, 0x2905, 0x2911, 0x2921, 0x2923, 0x293f, 0x2947, 0x295d, 0x2965, 0x2969, 0x296f, 0x2975, 0x2983, 0x2987, 0x298f, 0x299b, 0x29a1]

    function getTimeLow(_0x34d790) {
        var _0x3ca11c = _0x34d790['split']('-');
        var _0x536259 = parseInt(_0x3ca11c[0x0], 0x10)["toString"](0x2);
        for (var _0xc8e6b = _0x536259["length"]; _0xc8e6b < 0x20; _0xc8e6b++) {
            _0x536259 = '0' + _0x536259;
        }
        return _0x536259["split"]('')["map"](function (_0x2dc1ea) {
            return parseInt(_0x2dc1ea, 0x2);
        });
    }


    var _0x832dc7 = getTimeLow(_0x461fc8);
    var _0xb1428
    _0xb1428 = _0x1ac89a[3]
    _0xb1428 = parseInt(_0xb1428, 0x10)
    _0xb1428 = (_0xb1428 & 0xff) + Math['floor'](_0xb1428 / 0x10000) * 0x100

    console.log('_0xb1428 === ', _0xb1428)
    var _0x48b7ea = [0x35, 0x1f, 0x29, 0x2b]

    function _0x29cc1a(_0x17b62e) {
        var _0x4d59b6 = [];
        for (var _0x406ba5 = 0x0; _0x406ba5 < _0x17b62e['length']; _0x406ba5++) {
            if (!_0x17b62e[_0x406ba5]) {
                _0x4d59b6["push"](_0x406ba5);
            }
        }
        return new Uint8Array(_0x4d59b6);
    }

    function _0x405f89(_0x23b2b1) {
        var _0x13b662 = [];
        for (var _0x22cff5 = 0x0; _0x22cff5 < _0x23b2b1["length"]; _0x22cff5++) {
            if (_0x23b2b1[_0x22cff5]) {
                _0x13b662["push"](_0x22cff5);
            }
        }
        return new Uint8Array(_0x13b662);
    }

    function getMask(_0x48dbc7) {
        switch (_0x48dbc7) {
            case "dynamic":
                return 0x0;
            case "dynamic2":
                return 0x1;
            case "dynamic3":
                return 0x2;
            case "dynamic4":
                return 0x3;
            default:
        }
    }


    function _0x1a9b6c(_0x29411e) {
        return _0xb1428 >> 0x8 + _0x29411e * 0x6 & 0x3f;
    }

    function _0x407529(_0x360d9a) {
        return _0x1a9b6c(_0x360d9a) === _0x48b7ea[_0x360d9a] || [1, 1, "", 0, 0, 0, 31, 0][0x5];
    }

    function _0x405f89(_0x23b2b1) {
        var _0x13b662 = [];
        for (var _0x22cff5 = 0x0; _0x22cff5 < _0x23b2b1["length"]; _0x22cff5++) {
            if (_0x23b2b1[_0x22cff5]) {
                _0x13b662["push"](_0x22cff5);
            }
        }
        return new Uint8Array(_0x13b662);
    }

    function pushCountingEvent(_0x12f614, current_v) {
        var _0x3a7591,
            _0x4b09f6 = current_v;
        _0x3a7591 = _0x4b09f6["length"];
        if (_0x3a7591 < 0x10) {
            var _0xed5419 = _0x12f614 === "counting" ? 0x0 : 0x1;
            current_v = _0x29cc1a(_0x832dc7)
        } else {
            if (!_0x407529(getMask("dynamic"))) {
                current_v = current_v
            } else {
                if (_0x3a7591 % 0x2 === 0x1) {
                    current_v = current_v
                } else {
                    current_v = [current_v, prime]
                }
            }
        }
        return current_v
    }

    //======================================================================countArray---->dyna1ing======================================================================
    if (mode === 0) {
        current_v = _0x29cc1a(_0x832dc7)
        console.log('length === ', current_v['length'])
        current_v = pushCountingEvent('counting0', current_v)
    } else {
        current_v = _0x405f89(_0x832dc7)
        console.log('length === ', current_v['length'])
        current_v = pushCountingEvent('counting', current_v)
    }


    function _0x232bab(_0x14e83e, _0x2d9d27, _0x18ba23) {
        var _0x288c30 = Array["isArray"](_0x14e83e) && _0x14e83e["length"] > 0x0 ? _0x14e83e[0x0] : undefined;
        var _0x2cedf2 = Array["isArray"](_0x14e83e) && _0x14e83e['length'] > 0x1 ? _0x14e83e[0x1] : undefined;
        if (typeof _0x288c30 === 'undefined') {
            _0x2c5098["sData"]['tM'] += 0x1;
            return;
        }
        return new Uint8Array(_0x18ba23(_0x288c30, _0x2cedf2, _0x2d9d27));
    }

    //======================================================================dyna1ing------------>dyna2ing======================================================================
    var _0x506d7a = function (_0x4a6161) {
        return _0x4a6161;
    };
    var _0x1e761e = function (_0x505a3e) {
        return _0x505a3e["reverse"]();
    };
    var _0x4d6691 = function (_0x382da4) {
        var _0x445579 = 0x0;
        var _0x3c978b = Math["floor"](_0x382da4["length"] / 0x2);
        var _0x4c62c4 = _0x382da4[_0x3c978b];
        _0x382da4[_0x3c978b] = _0x382da4[_0x382da4['length'] - 0x1];
        _0x382da4[_0x382da4["length"] - 0x1] = _0x4c62c4;
        _0x4c62c4 = _0x382da4[_0x3c978b + 0x1];
        _0x382da4[_0x3c978b + 0x1] = _0x382da4[0x0];
        _0x382da4[0x0] = _0x4c62c4;
        return _0x382da4;
    };
    var _0x190045 = function (_0x400d06) {
        var _0x22c8c2 = 0x0;
        var _0x4438c1 = Math["floor"](_0x400d06['length'] / 0x2);
        var _0x4a8809 = _0x400d06[_0x4438c1];
        _0x400d06[_0x4438c1] = _0x400d06[0x0];
        _0x400d06[0x0] = _0x4a8809;
        _0x4a8809 = _0x400d06[_0x4438c1 + 0x1];
        _0x400d06[_0x4438c1 + 0x1] = _0x400d06[_0x400d06["length"] - 0x1];
        _0x400d06[_0x400d06["length"] - 0x1] = _0x4a8809;
        return _0x400d06;
    };
    var _0x12a1ad = function (_0x268684) {
        var _0x2bee68 = 0x0;
        var _0x3dd72b = _0x268684[_0x268684["length"] - 0x1];
        _0x268684[_0x268684["length"] - 0x1] = _0x268684[0x0];
        _0x268684[0x0] = _0x3dd72b;
        _0x3dd72b = _0x268684[_0x268684["length"] - 0x2];
        _0x268684[_0x268684["length"] - 0x2] = _0x268684[0x1];
        _0x268684[0x1] = _0x3dd72b;
        return _0x268684;
    };
    var _0x39a146 = function (_0x591129) {
        var _0x4ff838 = 0x0;
        var _0x39cc23 = _0x591129[_0x591129["length"] - 0x1];
        _0x591129[_0x591129["length"] - 0x1] = _0x591129[_0x591129['length'] - 0x2];
        _0x591129[_0x591129['length'] - 0x2] = _0x39cc23;
        _0x39cc23 = _0x591129[0x0];
        _0x591129[0x0] = _0x591129[0x1];
        _0x591129[0x1] = _0x39cc23;
        return _0x591129;
    };
    var _0x588802 = function (_0x3734fc, _0x4864cd, _0x3d1564) {
        var _0x15856b = [];
        for (var _0x4f14da = 0x0; _0x4f14da < _0x3734fc["length"]; _0x4f14da++) {
            _0x15856b["push"](_0x4864cd[_0x3734fc[_0x4f14da]] % 0x80);
        }
        return _0x15856b;
    };
    var _0x4ad074 = function (_0xc9ecd6, _0x57df50, _0xa3b963) {
        var _0x4581fd = [];
        for (var _0x1d1c35 = 0x0; _0x1d1c35 < _0xc9ecd6["length"]; _0x1d1c35++) {
            _0x4581fd['push'](_0x57df50[_0xc9ecd6[_0x1d1c35]] * _0xc9ecd6[_0x1d1c35] % 0x80);
        }
        return _0x4581fd;
    };
    var _0x2c3465 = function (_0x4f9411, _0x26851b, _0x29850a) {
        var _0x2befea = [];
        for (var _0x40d939 = 0x0; _0x40d939 < _0x4f9411["length"]; _0x40d939++) {
            _0x2befea['push'](_0x26851b[(_0x4f9411[_0x40d939] + (_0x29850a + 0x1) * 0x5) % _0x26851b['length']] % 0x80);
        }
        return _0x2befea;
    };
    var _0x5d0426 = function (_0x2f17e7, _0x36c739, _0x221f11) {
        var _0x1ef2c7 = [];
        for (var _0x9e569d = 0x0; _0x9e569d < _0x2f17e7['length']; _0x9e569d++) {
            _0x1ef2c7["push"](_0x36c739[(_0x2f17e7[_0x9e569d] + (_0x221f11 + _0x9e569d + 0x1) * 0x7) % _0x36c739["length"]] % 0x80);
        }
        return _0x1ef2c7;
    };
    var _0x3e22a4 = function (_0x54b33f, _0x4895a5, _0x3d3a8f) {
        var _0x1b2793 = [];
        for (var _0x1a6961 = 0x0; _0x1a6961 < _0x54b33f["length"]; _0x1a6961++) {
            _0x1b2793["push"](_0x4895a5[_0x54b33f[_0x1a6961]] * _0x54b33f[(_0x1a6961 + (_0x3d3a8f + 0x1) * 0x9) % _0x54b33f["length"]] % 0x80);
        }
        return _0x1b2793;
    };
    var _0x4092c2 = function (_0x124775, _0x86be26, _0x2da3e3) {
        var _0x5ac0b6 = [];
        for (var _0x430b7e = 0x0; _0x430b7e < _0x124775["length"]; _0x430b7e++) {
            _0x5ac0b6["push"]((_0x86be26[_0x124775[_0x430b7e]] * _0x124775[_0x430b7e] + (_0x2da3e3 + 0x1) * 0xd) % 0x80);
        }
        return _0x5ac0b6;
    };
    ordering_function_list = [_0x506d7a, _0x1e761e, _0x4d6691, _0x190045, _0x12a1ad, _0x39a146]
    wording_function_list = [_0x588802, _0x4ad074, _0x2c3465, _0x5d0426, _0x3e22a4, _0x4092c2]

    current_m = _0x1a9b6c(0)
    current_a = current_m % (6 - 0x2) + 0x2
    console.log('m === ', current_m, ' a === ', current_a)
    if (current_v["length"] % 0x2 === 0x0) { //ordering
        current_v = current_v
        console.log(current_v)
        current_v = ordering_function_list[current_a](current_v)
        current_n = 'order'
    } else { // wording
        current_v = [current_v, prime]
        console.log(current_v)
        current_v = _0x232bab(current_v, current_m, wording_function_list[current_a])
        current_n = 'word'
    }
    console.log(current_v)

    //======================================================================dyna2ing------------>dyna3ing======================================================================
    function _0x1ae6b2(_0x2f8ed9, _0x3f7963, _0x55eef7) {
        return _0x55eef7(_0x2f8ed9);
    };
    current_m = _0x1a9b6c(1)
    current_a = current_m % (6 - 0x2) + 0x2
    console.log('m === ', current_m, ' a === ', current_a)
    if (current_n === 'word') {
        current_v = current_v
        console.log(current_v)
        current_v = _0x1ae6b2(current_v, current_m, ordering_function_list[current_a])
    } else {
        current_v = [current_v, prime]
        console.log(current_v)
        current_v = _0x232bab(current_v, current_m, wording_function_list[current_a])
    }
    console.log(current_v)

    //======================================================================dyna3ing------------>Hexing======================================================================

    var _0xba466a = function (_0x4e61bc, _0x2635f8) {
        return _0x4e61bc;
    }
    var _0x2445b7 = function (_0x4ef86e, _0x594bf6) {
        var _0x576ad1 = Math["floor"](_0x4ef86e["length"] / 0x2);
        var _0x38a8c2 = Array["prototype"]["slice"]["call"](_0x4ef86e, 0x0, _0x576ad1);
        var _0x5056a9 = Array["prototype"]["slice"]["call"](_0x4ef86e, _0x576ad1);
        var _0x58f908 = new Int8Array(_0x4ef86e["length"]);
        _0x58f908["set"](_0x5056a9);
        _0x58f908["set"](_0x38a8c2, _0x5056a9["length"]);
        return _0x58f908;
    }
    var _0x1c7e76 = function (_0x4fbf16, _0x1eceb4) {
        var _0xbeac38 = 0x0;
        var _0x373be8 = Math["floor"](_0x4fbf16["length"] / 0x4);
        var _0x10ff00 = Array['prototype']["slice"]["call"](_0x4fbf16, 0x0, _0x373be8);
        var _0xc5bf56 = Array['prototype']['slice']["call"](_0x4fbf16, _0x373be8, 0x2 * _0x373be8);
        var _0x1212fe = Array["prototype"]["slice"]['call'](_0x4fbf16, 0x2 * _0x373be8, 0x3 * _0x373be8);
        var _0x1b3f4d = Array["prototype"]["slice"]["call"](_0x4fbf16, 0x3 * _0x373be8, _0x4fbf16["length"]);
        var _0x492cde = new Int8Array(_0x4fbf16["length"]);
        _0x492cde['set'](_0x1b3f4d);
        _0x492cde['set'](_0xc5bf56, _0x1b3f4d["length"]);
        _0x492cde["set"](_0x1212fe, _0x1b3f4d["length"] + _0x373be8);
        _0x492cde["set"](_0x10ff00, _0x1b3f4d["length"] + 0x2 * _0x373be8);
        return _0x492cde;
    }
    var _0x32b610 = function (_0x35f119, _0x1d357d) {
        var _0x1e3c63 = Math['floor'](_0x35f119["length"] / 0x4);
        var _0x1d7677 = Array["prototype"]['slice']["call"](_0x35f119, 0x0, _0x1e3c63);
        var _0x229988 = Array["prototype"]["slice"]["call"](_0x35f119, _0x1e3c63, 0x2 * _0x1e3c63);
        var _0x365e5f = Array['prototype']["slice"]["call"](_0x35f119, 0x2 * _0x1e3c63, 0x3 * _0x1e3c63);
        var _0x2c203b = Array["prototype"]["slice"]['call'](_0x35f119, 0x3 * _0x1e3c63, _0x35f119["length"]);
        var _0x725f7e = new Int8Array(_0x35f119["length"]);
        _0x725f7e['set'](_0x229988);
        _0x725f7e["set"](_0x1d7677, _0x1e3c63);
        _0x725f7e["set"](_0x365e5f, 0x2 * _0x1e3c63);
        _0x725f7e["set"](_0x2c203b, 0x3 * _0x1e3c63);
        return _0x725f7e;
    }
    var _0x1c29e9 = function (_0x36296b, _0x4d93e7) {
        var _0x2e7778 = Math["floor"](_0x36296b['length'] / 0x4);
        var _0x51c491 = Array['prototype']["slice"]["call"](_0x36296b, 0x0, _0x2e7778);
        var _0x5e2899 = Array["prototype"]["slice"]["call"](_0x36296b, _0x2e7778, 0x2 * _0x2e7778);
        var _0x3da88d = Array["prototype"]["slice"]["call"](_0x36296b, 0x2 * _0x2e7778, 0x3 * _0x2e7778);
        var _0x16a83f = Array["prototype"]['slice']['call'](_0x36296b, 0x3 * _0x2e7778, _0x36296b["length"]);
        var _0x2567af = new Int8Array(_0x36296b["length"]);
        _0x2567af["set"](_0x51c491);
        _0x2567af["set"](_0x16a83f, _0x2e7778);
        _0x2567af["set"](_0x3da88d, _0x16a83f['length'] + _0x2e7778);
        _0x2567af['set'](_0x5e2899, _0x16a83f["length"] + 0x2 * _0x2e7778);
        return _0x2567af;
    }
    hexing_function_list = [_0xba466a, _0x2445b7, _0x1c7e76, _0x32b610, _0x1c29e9]
    current_m = _0x1a9b6c(2)
    current_a = current_m % (5 - 0x1) + 0x1
    console.log('m === ', current_m, ' a === ', current_a)
    current_v = hexing_function_list[current_a](current_v)
    console.log(current_v)

    var _0x44bc4f = current_v['length'] - 0x10;
    var _0x200743 = _0x44bc4f ? Math['abs'](Math['floor'](_0xb1428 / 0x4)) % (_0x44bc4f + 0x1) : 0x0
    console.log(_0x200743)
    var _0x55d0ca = new Uint8Array(current_v['slice'](_0x200743, _0x200743 + 0x10))
    var _0x253bc1 = {};
    _0x253bc1["key"] = _0x55d0ca;
    _0x253bc1["mode"] = 'ecb';


    function _0x1f9a1e(_0x3d15ce, _0x12a973) {
        if (false) {
            throw new TypeError('Cannot call a class as a function');
        }
    }

    var _0x5e99c5 = new Uint32Array([0xa3b1bac6, 0x56aa3350, 0x677d9197, 0xb27022dc])
    var _0x377e13 = new Uint32Array([0x70e15, 0x1c232a31, 0x383f464d, 0x545b6269, 0x70777e85, 0x8c939aa1, 0xa8afb6bd, 0xc4cbd2d9, 0xe0e7eef5, 0xfc030a11, 0x181f262d, 0x343b4249, 0x50575e65, 0x6c737a81, 0x888f969d, 0xa4abb2b9, 0xc0c7ced5, 0xdce3eaf1, 0xf8ff060d, 0x141b2229, 0x30373e45, 0x4c535a61, 0x686f767d, 0x848b9299, 0xa0a7aeb5, 0xbcc3cad1, 0xd8dfe6ed, 0xf4fb0209, 0x10171e25, 0x2c333a41, 0x484f565d, 0x646b7279]);
    var _0x5886cf = new Uint8Array([0xd6, 0x90, 0xe9, 0xfe, 0xcc, 0xe1, 0x3d, 0xb7, 0x16, 0xb6, 0x14, 0xc2, 0x28, 0xfb, 0x2c, 0x5, 0x2b, 0x67, 0x9a, 0x76, 0x2a, 0xbe, 0x4, 0xc3, 0xaa, 0x44, 0x13, 0x26, 0x49, 0x86, 0x6, 0x99, 0x9c, 0x42, 0x50, 0xf4, 0x91, 0xef, 0x98, 0x7a, 0x33, 0x54, 0xb, 0x43, 0xed, 0xcf, 0xac, 0x62, 0xe4, 0xb3, 0x1c, 0xa9, 0xc9, 0x8, 0xe8, 0x95, 0x80, 0xdf, 0x94, 0xfa, 0x75, 0x8f, 0x3f, 0xa6, 0x47, 0x7, 0xa7, 0xfc, 0xf3, 0x73, 0x17, 0xba, 0x83, 0x59, 0x3c, 0x19, 0xe6, 0x85, 0x4f, 0xa8, 0x68, 0x6b, 0x81, 0xb2, 0x71, 0x64, 0xda, 0x8b, 0xf8, 0xeb, 0xf, 0x4b, 0x70, 0x56, 0x9d, 0x35, 0x1e, 0x24, 0xe, 0x5e, 0x63, 0x58, 0xd1, 0xa2, 0x25, 0x22, 0x7c, 0x3b, 0x1, 0x21, 0x78, 0x87, 0xd4, 0x0, 0x46, 0x57, 0x9f, 0xd3, 0x27, 0x52, 0x4c, 0x36, 0x2, 0xe7, 0xa0, 0xc4, 0xc8, 0x9e, 0xea, 0xbf, 0x8a, 0xd2, 0x40, 0xc7, 0x38, 0xb5, 0xa3, 0xf7, 0xf2, 0xce, 0xf9, 0x61, 0x15, 0xa1, 0xe0, 0xae, 0x5d, 0xa4, 0x9b, 0x34, 0x1a, 0x55, 0xad, 0x93, 0x32, 0x30, 0xf5, 0x8c, 0xb1, 0xe3, 0x1d, 0xf6, 0xe2, 0x2e, 0x82, 0x66, 0xca, 0x60, 0xc0, 0x29, 0x23, 0xab, 0xd, 0x53, 0x4e, 0x6f, 0xd5, 0xdb, 0x37, 0x45, 0xde, 0xfd, 0x8e, 0x2f, 0x3, 0xff, 0x6a, 0x72, 0x6d, 0x6c, 0x5b, 0x51, 0x8d, 0x1b, 0xaf, 0x92, 0xbb, 0xdd, 0xbc, 0x7f, 0x11, 0xd9, 0x5c, 0x41, 0x1f, 0x10, 0x5a, 0xd8, 0xa, 0xc1, 0x31, 0x88, 0xa5, 0xcd, 0x7b, 0xbd, 0x2d, 0x74, 0xd0, 0x12, 0xb8, 0xe5, 0xb4, 0xb0, 0x89, 0x69, 0x97, 0x4a, 0xc, 0x96, 0x77, 0x7e, 0x65, 0xb9, 0xf1, 0x9, 0xc5, 0x6e, 0xc6, 0x84, 0x18, 0xf0, 0x7d, 0xec, 0x3a, 0xdc, 0x4d, 0x20, 0x79, 0xee, 0x5f, 0x3e, 0xd7, 0xcb, 0x39, 0x48]);

    function rotateLeft(_0xdb63ea, _0x1dd1b6) {
        return (_0xdb63ea << _0x1dd1b6) | _0xdb63ea >>> 0x20 - _0x1dd1b6;
    }

    function linearTransform1(_0x1539ad) {
        return (_0x1539ad ^ rotateLeft(_0x1539ad, 0x2)) ^ rotateLeft(_0x1539ad, 0xa) ^ rotateLeft(_0x1539ad, 0x12) ^ rotateLeft(_0x1539ad, 0x18);
    }

    function linearTransform2(_0x460527) {
        return (_0x460527 ^ rotateLeft(_0x460527, 0xd) ^ rotateLeft(_0x460527, 0x17));
    }

    function tauTransform(_0x1e9d26) {
        return (((_0x5886cf[_0x1e9d26 >>> 0x18 & 0xff] << 0x18 | _0x5886cf[_0x1e9d26 >>> 0x10 & 0xff] << 0x10) | (_0x5886cf[_0x1e9d26 >>> 0x8 & 0xff] << 0x8)) | _0x5886cf[(_0x1e9d26 & 0xff)]);
    }

    function tTransform1(_0x49df1c) {
        var _0x172d7c = tauTransform(_0x49df1c);
        var _0x50b285 = linearTransform1(_0x172d7c);
        return _0x50b285;
    }

    function tTransform2(_0x3017ad) {
        var _0x2acbe7 = tauTransform(_0x3017ad);
        var _0x5a70d9 = linearTransform2(_0x2acbe7);
        return _0x5a70d9
    }

    function spawnEncryptRoundKeys() {
        var _0x1bd5d2 = new Uint32Array(0x4);
        _0x1bd5d2[0x0] = ((this['key'][0x0] << 0x18 | (this['key'][0x1] << 0x10)) | this['key'][0x2] << 0x8) | this['key'][0x3];
        _0x1bd5d2[0x1] = ((this['key'][0x4] << 0x18 | this['key'][0x5] << 0x10) | this['key'][0x6] << 0x8) | this['key'][0x7];
        _0x1bd5d2[0x2] = ((this['key'][0x8] << 0x18 | (this['key'][0x9] << 0x10)) | this['key'][0xa] << 0x8) | this['key'][0xb];
        _0x1bd5d2[0x3] = ((((this['key'][0xc] << 0x18) | (this['key'][0xd] << 0x10)) | this['key'][0xe] << 0x8) | this['key'][0xf]);
        var _0x2d500e = new Uint32Array(0x24);
        _0x2d500e[0x0] = _0x1bd5d2[0x0] ^ _0x5e99c5[0x0];
        _0x2d500e[0x1] = (_0x1bd5d2[0x1] ^ _0x5e99c5[0x1]);
        _0x2d500e[0x2] = (_0x1bd5d2[0x2] ^ _0x5e99c5[0x2]);
        _0x2d500e[0x3] = _0x1bd5d2[0x3] ^ _0x5e99c5[0x3];
        for (var _0x198c1c = 0x0; (_0x198c1c < 0x20); _0x198c1c++) {
            _0x2d500e[(_0x198c1c + 0x4)] = _0x2d500e[_0x198c1c] ^ tTransform2(_0x2d500e[_0x198c1c + 0x1] ^ _0x2d500e[_0x198c1c + 0x2] ^ _0x2d500e[_0x198c1c + 0x3] ^ _0x377e13[_0x198c1c]);
            this['encryptRoundKeys'][_0x198c1c] = _0x2d500e[(_0x198c1c + 0x4)];
        }
    }

    function _0x3479ed(_0x13e87c) {
        _0x1f9a1e(this, _0x3479ed);
    }

    function _0x1e37c2(_0x4a7fee) {
        var _0x144d79 = [
            "8",
            "16",
            "12",
            "9",
            "2",
            "14",
            "0",
            "10",
            "5",
            "1",
            "4",
            "13",
            "6",
            "3",
            "11",
            "15",
            "7"
        ]
            , _0x8b9da = 0x0;

        while (!![]) {
            switch (_0x144d79[_0x8b9da++]) {
                case '0':
                    if ((_0x4a7fee['iv'] !== undefined) && _0x4a7fee['iv'] !== null) {
                        _0x34afa7 = this[_0x1c61('0xf6')][_0x1c61('0xb0')](_0x4a7fee['iv']);
                        if (_0x109901[_0x1c61('0xf7')](_0x34afa7[_0x1c61('0x7')], 0x10)) {
                            throw new Error(_0x109901['GEMZK']);
                        }
                    }
                    continue;
                case '1':
                    if (['cbc', 'ecb']['indexOf']("ecb") >= 0x0) {
                        this["mode"] = "ecb";
                    }
                    continue;
                case '2':
                    this["key"] = _0x500c1e;
                    continue;
                case '3':
                    spawnEncryptRoundKeys();
                    continue;
                case '4':
                    this["cipherType"] = "base64";
                    continue;
                case '5':
                    this["mode"] = 'cbc';
                    continue;
                case '6':
                    this["encryptRoundKeys"] = new Uint32Array(0x20);
                    continue;
                case '7':
                    this["decryptRoundKeys"]["reverse"]();
                    continue;
                case '8':
                    _0x1f9a1e(this, _0x1e37c2);
                    continue;
                case '9':
                    if (false) {
                        throw new Error(_0x109901[_0x1c61('0x100')]);
                    }
                    continue;
                case '10':
                    this['iv'] = _0x34afa7;
                    continue;
                case '11':
                    Uint32Array["prototype"]['reverse'] = function () {
                        Array['prototype']["reverse"]["apply"](this, arguments);
                    }
                    ;
                    continue;
                case '12':
                    var _0x500c1e = _0x4a7fee['key'];
                    continue;
                case '13':
                    if (["base64", "text"]["indexOf"](_0x4a7fee["outType"]) >= 0x0) {
                        this[_0x1c61('0xfc')] = _0x4a7fee[_0x1c61('0x103')];
                    }
                    continue;
                case '14':
                    var _0x34afa7 = new Uint8Array(0x0);
                    continue;
                case '15':
                    this["decryptRoundKeys"] = new Uint32Array(this['encryptRoundKeys']);
                    continue;
                case '16':
                    this['Crypt'] = new _0x3479ed();
                    continue;
            }
            break;
        }
    }

    _0x1e37c2(_0x253bc1)
    console.log(this.key)
    console.log(this.decryptRoundKeys)
    console.log(this.encryptRoundKeys)

    function stringToArray(_0xe84d7d) {
        var _0x465dc1 = [];
        var _0x389e6e = _0xe84d7d["length"];
        for (var _0x187864 = 0x0; _0x187864 < _0x389e6e; _0x187864++) {
            var _0xb3e0ae = _0xe84d7d["charCodeAt"](_0x187864);
            if ((0x4e00 < _0xb3e0ae) && _0xb3e0ae < 0x9fa5) {
                var _0x40e0c5 = _0xb3e0ae["toString"](0x2);
                var _0xf1897c = _0x1c61('0xd2');
                var _0x31e1fe = '10';
                var _0x49a5bd = '10';
                var _0x2dac98 = _0x40e0c5[_0x1c61('0x7')];
                if (_0x2dac98 <= 0x6) {
                    _0x49a5bd = _0x5751f3[_0x1c61('0xd3')](_0x49a5bd + this[_0x1c61('0xcd')](0x6 - _0x2dac98), _0x40e0c5);
                    _0x31e1fe = _0x5751f3[_0x1c61('0xd3')](_0x31e1fe, this[_0x1c61('0xcd')](0x6));
                    _0xf1897c = _0xf1897c + this[_0x1c61('0xcd')](0x4);
                } else if (_0x5751f3['YOMlm'](_0x2dac98, 0x6) && _0x2dac98 <= 0xc) {
                    _0x49a5bd = _0x5751f3['ZNDqX'](_0x49a5bd, _0x40e0c5['slice'](-0x6));
                    _0x31e1fe = _0x5751f3['QnpWh'](_0x31e1fe + this[_0x1c61('0xcd')](_0x5751f3[_0x1c61('0xd4')](0xc, _0x2dac98)), _0x40e0c5[_0x1c61('0xd5')](0x0, _0x2dac98 - 0x6));
                    _0xf1897c = _0xf1897c + this[_0x1c61('0xcd')](0x4);
                } else {
                    _0x49a5bd = _0x49a5bd + _0x40e0c5[_0x1c61('0x0')](-0x6);
                    _0x31e1fe = _0x5751f3['PQKlq'](_0x31e1fe, _0x40e0c5[_0x1c61('0xd5')](_0x2dac98 - 0xc, 0x6));
                    _0xf1897c = _0x5751f3[_0x1c61('0xd6')](_0xf1897c + this[_0x1c61('0xcd')](0x10 - _0x2dac98), _0x40e0c5[_0x1c61('0xd5')](0x0, _0x5751f3[_0x1c61('0xd4')](_0x2dac98, 0xc)));
                }
                _0x465dc1['push'](_0x5751f3[_0x1c61('0xd7')](parseInt, _0xf1897c, 0x2), _0x5751f3[_0x1c61('0xd7')](parseInt, _0x31e1fe, 0x2), _0x5751f3[_0x1c61('0xd7')](parseInt, _0x49a5bd, 0x2));
            } else {
                _0x465dc1['push'](_0xb3e0ae);
            }
        }
        return _0x465dc1;
    }

    function padding(_0x5ae85f) {
        var _0x50c483 = ['0', '5', '2', '3', '4', '1']
            , _0xd310a1 = 0x0;
        while (!![]) {
            switch (_0x50c483[_0xd310a1++]) {
                case '0':
                    if (_0x5ae85f === null) {
                        return null;
                    }
                    continue;
                case '1':
                    return _0x2f9ade;
                case '2':
                    var _0x2f9ade = new Uint8Array(_0x5ae85f['length'] + _0x13e379);
                    continue;
                case '3':
                    _0x2f9ade['set'](_0x5ae85f, 0x0);
                    continue;
                case '4':
                    _0x2f9ade["fill"](_0x13e379, _0x5ae85f['length']);
                    continue;
                case '5':
                    var _0x13e379 = (16 - (_0x5ae85f['length'] % 16));
                    continue;
            }
            break;
        }
    }

    function uint8ToUint32Block(_0xabf1fc, _0x47b938) {
        var _0x1ab3d4 = [
            "5",
            "6",
            "0",
            "4",
            "2",
            "1",
            "3"
        ]
            , _0x35f03b = 0x0;
        while (!![]) {
            switch (_0x1ab3d4[_0x35f03b++]) {
                case '0':
                    _0x4d3846[0x0] = ((_0xabf1fc[_0x47b938] << 0x18) | _0xabf1fc[_0x47b938 + 0x1] << 0x10) | (_0xabf1fc[_0x47b938 + 0x2] << 0x8) | _0xabf1fc[(_0x47b938 + 0x3)];
                    continue;
                case '1':
                    _0x4d3846[0x3] = (_0xabf1fc[_0x47b938 + 0xc] << 0x18 | _0xabf1fc[_0x47b938 + 0xd] << 0x10 | _0xabf1fc[(_0x47b938 + 0xe)] << 0x8 | _0xabf1fc[_0x47b938 + 0xf]);
                    continue;
                case '2':
                    _0x4d3846[0x2] = ((_0xabf1fc[_0x47b938 + 0x8] << 0x18 | _0xabf1fc[(_0x47b938 + 0x9)] << 0x10) | _0xabf1fc[_0x47b938 + 0xa] << 0x8) | _0xabf1fc[(_0x47b938 + 0xb)];
                    continue;
                case '3':
                    return _0x4d3846;
                case '4':
                    _0x4d3846[0x1] = (((_0xabf1fc[(_0x47b938 + 0x4)] << 0x18) | _0xabf1fc[_0x47b938 + 0x5] << 0x10) | _0xabf1fc[(_0x47b938 + 0x6)] << 0x8 | _0xabf1fc[(_0x47b938 + 0x7)]);
                    continue;
                case '5':
                    if (typeof _0x47b938 == "undefined") {
                        _0x47b938 = 0x0;
                    }
                    continue;
                case '6':
                    var _0x4d3846 = new Uint32Array(0x4);
                    continue;
            }
            break;
        }
    }

    function doBlockCrypt(_0x5ac69f, _0x2ae5d5) {
        var _0x475ba0 = new Uint32Array(0x24);
        _0x475ba0["set"](_0x5ac69f, 0x0);
        for (var _0x1e39aa = 0x0; (_0x1e39aa < 0x20); _0x1e39aa++) {
            _0x475ba0[_0x1e39aa + 0x4] = (_0x475ba0[_0x1e39aa] ^ tTransform1(_0x475ba0[(_0x1e39aa + 0x1)] ^ _0x475ba0[(_0x1e39aa + 0x2)] ^ _0x475ba0[(_0x1e39aa + 0x3)] ^ _0x2ae5d5[_0x1e39aa]));
        }
        var _0x3157e6 = new Uint32Array(0x4);
        _0x3157e6[0x0] = _0x475ba0[0x23];
        _0x3157e6[0x1] = _0x475ba0[0x22];
        _0x3157e6[0x2] = _0x475ba0[0x21];
        _0x3157e6[0x3] = _0x475ba0[0x20];
        return _0x3157e6;
    }

    var _0x487d2e = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "+",
        "/"
    ]

    function arrayBufferToBase64(buffer) {
        let binary = '';
        // let bytes = new Uint8Array(buffer);
        let len = buffer.byteLength;
        for (let i = 0; i < len; i++) {
            binary += String.fromCharCode(buffer[i]);
        }
        return btoa(binary);
    }

    function encrypt(_0x1e95e4) {
        var _0x7faaa1 = stringToArray(_0x1e95e4);
        var _0x3321e4 = padding(_0x7faaa1);
        var _0x36c333 = (_0x3321e4["length"] / 16);
        var _0x23f85f = new Uint8Array(_0x3321e4["length"]);
        for (var _0x4b3011 = 0x0; _0x4b3011 < _0x36c333; _0x4b3011++) {
            var _0x53fc04 = _0x4b3011 * 16;
            var _0x28f8dc = uint8ToUint32Block(_0x3321e4, _0x53fc04);
            var _0x1692a3 = doBlockCrypt(_0x28f8dc, this["encryptRoundKeys"]);
            for (var _0x53f177 = 0x0; _0x53f177 < 16; _0x53f177++) {
                _0x23f85f[_0x53fc04 + _0x53f177] = _0x1692a3[parseInt((_0x53f177 / 0x4))] >> (((0x3 - _0x53f177) % 0x4) * 0x8) & 0xff;
            }
        }
        console.log('_0x23f85f === ' + _0x23f85f + '\n' + _0x23f85f.length)
        if (this["cipherType"] === 'base64') {
            return arrayBufferToBase64(_0x23f85f);
        } else {
            return this[_0x1c61('0xf6')]['utf8ArrayBufferToString'](_0x23f85f);
        }
    }

    console.log('x-s3-s4e ==== ' + encrypt(
        '["bd05e6983226abdfb703bbffdb3c02aa79dafebe:48:c38fe0c5-c5ef-11f0-a33d-3cd2e55daed6:0890002014;S1wkGu935hGpe3a4z4n7ojg31","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0","zh-CN","124.04347527516074","Win32",["38.87.67.251"],"c2331586",["1920","1080","1","24"],-480,"https://www.shenzhenair.com/szair_B2C/","25e94853a2882ee978d173ddde79f1ce40ad5321","c8823e45","(https://www.shenzhenair.com/vodka/v1/js/sw.js:6022:25)\\n","3521dd02e6064000b43da426ea93baa542fd9433",[[2,2,2,2,2],[2,2,3,2,3,3],2,2,2,[3,2,3,2,2,3],[2,2,2,1,1,1,3,0],[2],[2],2,[2],[2,2],2,2],[],2]'
    ))
    var x_s3_s4e = encrypt(JSON.stringify(_0x7db3eb))
    x_s3_s4e.replace(/(\s*|\t|\r|\n)/g, '')
    console.log('\n' + x_s3_s4e + '\n')
    x_s3_s4e = window.encodeURIComponent(x_s3_s4e) + '3sSs' + x_s3_tid
    return x_s3_s4e
}
x_s3_tid = 'bd05e6983226abdfb703bbffdb3c02aa79dafebe:48:c38fe0c5-c5ef-11f0-a33d-3cd2e55daed6:0890002014'
x_s3_sid = 'S1wkGu935hGpe3a4z4n7ojg31'
console.log(get_x_s3_s4e(x_s3_tid, x_s3_sid))





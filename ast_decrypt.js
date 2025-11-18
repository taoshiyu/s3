const parser = require("@babel/parser");
const traverse = require("@babel/traverse").default;
const types = require("@babel/types");
const generator = require("@babel/generator").default;
const fs = require('fs');
const {inType} = require("@babel/traverse/lib/path/ancestry");
const jsdom = require("jsdom");
const {emptyStatement} = require("@babel/types");
// const {get} = require("@babel/traverse/lib/path/family");
// var source = './feilin.js'
// var source = './sg.js'
// var dest_bk = './sg.bk.js'
// var dest = './sg.decrypt.js'
var source = './bootstrap.js'
var dest = './bootstrap.decrypte.js'
var resourceCode = fs.readFileSync(source, {'encoding': 'utf-8'})
var header_js = fs.readFileSync('./head.js', {'encoding': 'utf-8'})
var ast = parser.parse(resourceCode)
var tempAst = parser.parse('')
var vmAst = parser.parse('')
var start_t = new Date().getTime()


function createBrowserEnvironment() {
    const jsdom = require("jsdom");
    const {ExpressionStatement} = require("@babel/generator/lib/generators/expressions");
    const {JSDOM} = jsdom;
    const dom = new JSDOM('<!DOCTYPE html><html><body></body></html>', {
        url: 'https://example.com/',
        referrer: 'https://example.com/',
        contentType: 'text/html',
        userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        includeNodeLocations: true,
        storageQuota: 10000000,
        runScripts: 'dangerously',
        resources: 'usable'
    });

    const {window} = dom;


    // 复制所有 window 属性到 global
    for (const key in window) {
        if (!global.hasOwnProperty(key)) {
            global[key] = window[key];
        }
    }

    // 特殊处理一些全局对象

    const importantConstructors = [
        'Node', 'Document', 'Element', 'HTMLElement', 'HTMLDocument',
        'Window', 'Navigator', 'Screen', 'Location', 'History',
        'LocalStorage', 'SessionStorage', 'Storage', 'Range', "RegExp",
        'Image', 'Option', 'Text', 'Attr', 'Event', 'CustomEvent',
        'MouseEvent', 'KeyboardEvent', 'InputEvent', 'FocusEvent', 'Audio'
    ];

    importantConstructors.forEach(constructorName => {
        if (window[constructorName] && !global[constructorName]) {
            global[constructorName] = window[constructorName];
        }
    });

    global.window = window;
    global.document = window.document;
    global.navigator = window.navigator;
    global.screen = window.screen;
    global.location = window.location;
    global.history = window.history;
    global.localStorage = window.localStorage;
    global.sessionStorage = window.sessionStorage;
    global.Range = window.Range
    global.Document = window.document
    global.Element = window.Element
    global.Worker = window.Worker
    global.Screen = window.Screen
    global.Window = window;

    global.Navigator = window.navigator;
    global.Screen = window.screen;
    global.Location = window.location;
    global.History = window.history;
    global.LocalStorage = window.localStorage;
    global.SessionStorage = window.sessionStorage;
    global.Image = window.Image
    global.Option = window.Option
    global.Text = window.Text
    global.Attr = window.Attr
    global.Storage = window.Storage
    global.Error = window.Error
    global.String = window.String
    global.Event = window.Event

    window.matchMedia = function (mediaQuery) {
        return {
            matches: false,
            media: mediaQuery,
            addListener: function () {
            },
            removeListener: function () {
            },
            addEventListener: function () {
            },
            removeEventListener: function () {
            },
            dispatchEvent: function () {
                return false;
            }
        };
    };
    global.matchMedia = window.matchMedia

    return window;
}

createBrowserEnvironment();

function dumpNode(node) {

    tempAst.program.body = [node];
    let tempCode = generator(tempAst, {jsescOption: {minimal: true}}).code
    return tempCode

}

function loadNode(str) {
    console.log(str)
    try {
        let a = parser.parse(str)
        return a.program.body.at(0).expression
    } catch (e) {
        return types.stringLiteral(str)
    }

}

function dumpNodes(nodes) {
    tempAst.program.body = nodes;
    let tempCode = generator(tempAst, {jsescOption: {minimal: true}}).code
    return tempCode
}

var geval = eval
geval(header_js)

replace_ob_str = {
    CallExpression: function (path) {
        let node = path.node
        if (node.callee.name === '_0x1c61' || node.callee.name==="_0x2ae1" || node.callee.name==='_0x22cd') {
            try {
                console.log(dumpNode(node))
                path.replaceWith(types.stringLiteral(geval(dumpNode(node))))
            } catch (e) {
                console.log(e)
            }
        }
    }
}

key_length = 5


function replace_with_undefine(path) {
    path.replaceWith(types.unaryExpression('void', types.numericLiteral(0)))
}


function emband_replace_op(path, name, mapping) {
    let binding = path.getFunctionParent().scope.getBinding(name)
    if (!binding) {
        return
    }
    console.log([name, mapping])
    let emband_call = {
        CallExpression: {
            exit(path) {
                let callee = path.node.callee
                if (!callee.property) {
                    return
                }
                if (callee.object.name !== name) {
                    return
                }
                let k = path.node.callee.property.name

                let op_type = mapping.get(k)
                if (!op_type) {
                    return
                }
                let replace_by
                let arguments = path.node.arguments
                console.log(path.toString())
                if (op_type.type === 'BinaryExpression') {

                    replace_by = types.binaryExpression(op_type.operator, arguments[0], arguments[1])
                } else if (op_type.type === 'CallExpression') {
                    replace_by = types.callExpression(arguments[0], arguments.slice(1))
                } else if (op_type.type === 'UnaryExpression') {
                    replace_by = types.unaryExpression(op_type.operator, arguments[0])
                } else if (op_type.type === 'LogicalExpression') {
                    replace_by = types.logicalExpression(op_type.operator, arguments[0], arguments[1])
                } else {

                }
                path.replaceWith(replace_by)
                path.scope.crawl()
                console.log(path.toString())
            }
        },
        MemberExpression(path) {
            let k = path.node.property.name || path.node.property.value
            let op_type = mapping.get(k)
            if (!op_type) {
                return
            }
            if (op_type.type === 'StringLiteral') {
                path.replaceWith(types.stringLiteral(op_type.value))
            }
        }
    }
    let all_replaced = true
    for (b of binding.referencePaths) {
        let rp = b.parentPath
        let ra = b.parentPath.parentPath
        let k = rp.node.property && (rp.node.property.name || rp.node.property.value)
        if (rp.isMemberExpression() && k && k.length === key_length) {
            let op_type = mapping.get(k)
            if (!op_type) {
                continue
            }
            if (op_type.type === 'StringLiteral') {
                rp.replaceWith(types.stringLiteral(op_type.value))
            } else if (ra.node.type === 'CallExpression') {
                ra.traverse(emband_call)
                if (!(ra.node.callee && ra.node.callee.type === 'MemberExpression')) {
                    console.log(dumpNode(ra))
                    continue
                }
                let replace_by

                try {
                    let arguments = ra.node.arguments
                    if (op_type.type === 'BinaryExpression') {
                        replace_by = types.binaryExpression(op_type.operator, arguments[0], arguments[1])
                    } else if (op_type.type === 'CallExpression') {
                        replace_by = types.callExpression(arguments[0], arguments.slice(1))
                    } else if (op_type.type === 'UnaryExpression') {
                        replace_by = types.unaryExpression(op_type.operator, arguments[0])
                    } else if (op_type.type === 'LogicalExpression') {
                        replace_by = types.logicalExpression(op_type.operator, arguments[0], arguments[1])
                    } else {

                    }
                    ra.replaceWith(replace_by)
                    console.log(`${ra.toString()}=>${dumpNode(ra.node)}`)
                } catch (e) {
                    console.log(e)
                    console.log(`${ra.toString()}=x=>${dumpNode(replace_by)}`)
                    all_replaced = false
                }
            }
        }
        if (rp.isAssignmentExpression() || rp.isVariableDeclarator()) {
            let b_name = rp.isAssignmentExpression() ? rp.node.left.name : rp.node.id.name
            emband_replace_op(rp, b_name, mapping)
        }
    }
    path.scope.crawl()
    return all_replaced

}


function parse_ob_opcode(node) {
    if (node.type === "FunctionExpression") {
        let statement = node.body.body.at(-1)
        if (statement && statement.type === 'ReturnStatement') {
            let argument
            let value
            if (statement.argument.type === 'SequenceExpression') {
                argument = statement.argument.expressions.at(-1)
            } else if (statement.argument.type === 'CallExpression') {
                argument = statement.argument
            } else if (statement.argument.type === 'BinaryExpression') {
                argument = statement.argument
            } else if (statement.argument.type === 'UnaryExpression') {
                argument = statement.argument
            } else if (statement.argument.type === 'LogicalExpression') {
                argument = statement.argument
            } else if (statement.argument.type === 'StringLiteral') {
                argument = statement.argument
                value = argument.value
            } else {
                argument = statement.argument
            }
            let a_type = argument.type
            return {
                'type': a_type,
                'operator': argument.operator,
                'value': value
            }
        }
    }
    if (node.type === 'StringLiteral') {
        return {
            'type': node.type,
            'value': node.value,
            'operator': node.operator
        }
    }
    if (node.type === 'BinaryExpression') {

        return {
            'type': 'StringLiteral',
            'value': geval(dumpNode(node)),
            'operator': undefined
        }
    }
}


var replace_ob_opcode1 = {
    "FunctionDeclaration|FunctionExpression": {
        enter(func_path) {
            func_path.traverse(
                {
                    'VariableDeclarator': function (path) {
                        let binding = path.scope.getBinding(path.node.id.name)
                        if (binding) {
                            if (path.node.id.type === 'Identifier' && path.node.init && path.node.init.type === 'ObjectExpression') {
                                let binding_name = path.node.id.name
                                let properties = path.node.init.properties
                                let keys = properties.map(n => n.key)
                                if (keys.length > 0) {
                                    if (keys.every(k => k.value ? k.value.length === key_length : false)) {
                                        properties = path.node.init.properties
                                    } else {
                                        return
                                    }
                                }
                                for (r of binding.referencePaths) {
                                    if (r.parentPath.isMemberExpression() && r.parentPath.parentPath.isAssignmentExpression()) {
                                        let k = r.parentPath.node.property
                                        let v = r.parentPath.parentPath.node.right
                                        if (!k.name) {
                                            continue
                                        }
                                        if (k.name.length !== key_length) {
                                            continue
                                        }
                                        if (v.type !== 'FunctionExpression') {
                                            continue
                                        }
                                        properties.push(types.objectProperty(k, v))
                                        replace_with_undefine(r.parentPath.parentPath)
                                        // r.parentPath.parentPath.remove()
                                    }
                                }
                                let ob_opcode = new Map(
                                )
                                for (p of properties) {
                                    ob_opcode.set(p.key.value || p.key.name, parse_ob_opcode(p.value))
                                }
                                let all_replaced = emband_replace_op(path, binding_name, ob_opcode)
                                path.scope.crawl()
                                if (all_replaced && properties.length>0){
                                    // path.remove()
                                }

                            }

                        }
                    }
                }
            )
            func_path.scope.crawl()
        }
    },

}

replace_switch_cases = {
    'WhileStatement':{
        exit(path) {
            let node = path.node
            if (node.test.type==='UnaryExpression' && node.body.body && node.body.body.at(0).type==='SwitchStatement') {
                let switch_node = node.body.body.at(0)
                if (switch_node.discriminant.type==='MemberExpression') {
                    let loop_array_name = switch_node.discriminant.object.name
                    let loop_array = []
                    let binding = path.getFunctionParent().scope.getBinding(loop_array_name)
                    console.log([loop_array_name,dumpNode(binding.path.node)])
                    if (binding.path.node.type==='VariableDeclarator') {
                        loop_array = geval(dumpNode(binding.path.node.init))
                        console.log(loop_array)
                        binding.path.remove()
                    } else {
                        console.log(['不是VariableDeclarator',dumpNode(binding.path.node)])
                        return
                    }

                    let case_mapping = {}
                    for (const c of switch_node.cases) {
                        let c_test = c.test.value
                        let c_conseq = c.consequent
                        case_mapping[c_test] = c_conseq
                    }
                    let node_array = []
                    for (const c_t of loop_array) {
                        let conse = case_mapping[c_t]
                        let expr_1 = conse.at(0)
                        let expr_2 = conse.at(1)
                        if (expr_1.type==='ReturnStatement') {
                            node_array.push(expr_1)
                            break
                        }
                        if (expr_1.type==='ContinueStatement') {
                            continue
                        }
                        if (expr_1.type==='BreakStatement') {
                            break
                        }
                        if (expr_2 && expr_2.type ==='ContinueStatement') {
                            node_array.push(expr_1)
                            continue
                        }
                        if (expr_2 && expr_2.type==='BreakStatement') {
                            break
                        }


                    }
                    if (node_array.length>1) {
                        console.log(node_array)
                        path.replaceInline(node_array)
                    }
                }
            }
        }
    }
}
geval("var s3const = ['Chrome', \"Segoe\", \"Teletype-=\", \"data:image/png;base64,\", \"undefined\", \"cookie\", \"32.10.9\", 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/', \"url\", \"chrome\", \"navigator\", \"platform\", 'userAgent', \"plugins\", \"mimeTypes\", 'languages', \"maxTouchPoints\", 'mediaDevices', \"productSub\", \"webdriver\", \"connection\", \"permissions\", \"deviceMemory\", \"cookieEnabled\", \"doNotTrak\", \"document\", \"OfflineAudioContext\", 'webkitOfflineAudioContext', 'localStorage', \"sessionStorage\", \"indexedDB\", 'screen', 'debug', 'runtime', \"tid\"];")
geval("var _ssc = ['Chrome', \"Segoe\", 'Teletype=#', \"data:image/png;base64\", 'undefined', \"cookie\", \"32.10-94;\", 'context', \"url\", \"chrome\", \"source\", \"URL\", \"Map\", \"document\", \"s3-ex\", 'stack', 'Error\x20', 'expires', \"Com\", \"URI\", 'encode', \"Thu, 01 Jan 1970 00:00:01 GMT\", \"ponent\"];\n")
replace_s3_const  = {
    MemberExpression(path){
        if (path.node.object.name==='s3const' || path.node.object.name==='_ssc') {
            try{
                path.replaceWith(types.stringLiteral(geval(dumpNode(path.node))))
            } catch(e) {
                console.log(e)
            }
        }
    }
}
traverse(ast, replace_ob_str)
traverse(ast, replace_ob_opcode1)
traverse(ast,replace_ob_opcode1)
traverse(ast,replace_switch_cases)
traverse(ast,replace_s3_const)

var decrypt_code = generator(ast, {
    jsescOption: {// 自动转义
        // minimal: true,
    }
}).code
fs.writeFileSync(dest, decrypt_code, {encoding: 'utf-8'})
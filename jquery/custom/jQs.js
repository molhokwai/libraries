/* brake them, change them, until there are none anymore */
try {
    if(rules){
        /* check passed */
    }
    else{
        rules = {};
    }
}
catch(e){
    var rules = {};
}

rules['jQs'] = {
    /* JQUERY SIZING & STYLING */
    done : [],
    onDocumentReady : function(){
        $('.jQs').each(function(){
            if(!(this in rules.jQs.done)){
                var s = rules.jQs._do($(this)[0].className);
                if($(this).attr('style')){
                    s = $(this).attr('style') +' '+ s;
                }
                $(this).attr({'style' : s});
                
                rules.jQs.done.push(this);
            }
        });
    },

    /*  Execution, entry point
        See regExpY for params details
    */
    _do : function(className){
        var l=className.split(' ');
		var ld=[];
        for(var i=0; i<l.length;i++){
			ld[i] = false;
		}
        var result = [];
        for(var i=0; i<l.length;i++){
            var aP = rules.jQs.property.allParams();
            for (kh in aP){
                for(var j=0;j<aP[kh].params.length;j++){
                    aP[kh].params[j]['property'] = kh;
                    aP[kh].params[j]['value'] = l[i];
                    var r = rules.jQs.exec(aP[kh].params[j]);
                    if(r && r.length>0 && r[0]!= ""){
                        for(var n=0;n<r.length;n++){
                            result.push(r[n]);
							ld[i]=true;
                        }
                    }                
                }
            }
			if(!ld[i]){
            	var _rEe = new RegExp('[a-zA-Z\-]*:[a-zA-Z0-9\(\),#\.]*;').exec(l[i]);
        		if(_rEe!=null){
            		result.push(l[i]);
				}
			}
        }

        return result.join('');
    },

    /*  Execution.
        See regExpY & _do for params details
    */
    exec : function(params){
        var yielded = rules.jQs.regExpY(params);
        if (yielded && yielded.length>0 && yielded[0] && yielded[0]!=""){
            return rules.jQs.regExpYParse(yielded);
        }
    },

    /*  Regexp OBj Get
        [property choice regexp]
        [hyphen 0 | 1]
        [values choice regexp]
        [(double point | equal)(0 | 1) regexp]
        [number | color | name value regexp]
        [unit value regexp]
        [semicolon 0 | 1 regexp]
    */
    regExpGet : function(params){
            var s = "^(pcrS)"
                    +"[\\-]{0,1}"
                    +"(pvcrS)"
                    +"[:=]{0,1}"
                    +"(ncnvrS)"
                    +"(uvrS){0,2}"
                    +"[;]{0,1}";
            for(kp in params){
                if (typeof(params[kp])=='function'){
                    var r = params[kp]();
                    if(r && r!=""){
                        s = s.replace(kp,r);
                    }
                    else {
                        s = s.replace("("+kp+")", "([noval]{0})");
                    }
                }
            }
            return new RegExp(s);
    },

    /*  RegExp Yield

        @params (dictionary): {
            "v" : value for regExp exec
             // See rexExpB for other params details
        }
    */
    regExpY : function(params){
        var r_j_p_x_p = rules.jQs.property[params.property].params;
        var _regExp = rules.jQs.regExpGet(params);
        return _regExp.exec(params.value);
    },

    /*  RegExp Yield Parse

        @params (dictionary): {
            "yielded" : Yielded RegExp Object
             // See rexExpB for other params details
        }
    */
    regExpYParse : function(params) {
        var yielded = {
            'v' : params[0],
            'pcrS' : params[1],
            'pvcrS' : params[2],
            'ncnvrS' : params[3],
            'uvrS' : params[4]
        };

        /* property value ... */
        switch(yielded.pcrS){
            case 'w': case 'la': case 'large': 
                yielded.pcrS='width'; break;
            case 't': yielded.pcrS='text'; break;
            case 'pos' : case 'po' : yielded.pcrS='position';  break;
            case 'p': case 'pad': yielded.pcrS='padding'; break;
            case 'mi': yielded.pcrS='min'; break;
            case 'ma': yielded.pcrS='max'; break;
            case 'm': case 'marg': yielded.pcrS='margin'; break;
            case 'h': case 'tl': case 'tall': 
                yielded.pcrS='height'; break;
            case 'fl': yielded.pcrS='float'; break;
            case 'f': yielded.pcrS='font'; break;
            case 'disp' : case 'di' : yielded.pcrS='display';  break;
            case 'co' : yielded.pcrS='color';  break;            
            case 'bor' : case 'bord': yielded.pcrS='border';  break;
            case 'b': case 'back': yielded.pcrS='background'; break;
            case 'ou' : case 'out': yielded.pcrS='outline';  break;
            
            case 'default': break;
        }

        this.formatVal = function(val){
            /* property-value value... */
            switch(val){
                case 'l': val='left'; break;
                case 'r': val='right'; break;
                case 'c': val='center'; break;
                case 'all': val=''; break;
                case 'inl': val='inline'; break;
                case 'blo': val='block'; break;
                case 'j': val='justify'; break;
                case 'bo': val='both'; break;
                case 'b': val='bottom'; break;
                case 't': val='top'; break;
                case 's': val='size'; break;
                case 'st': val='style'; break;
                case 'i':  val='indent'; break;
                case 'd': val='decoration'; break;
                case 'abs': val='absolute'; break;
                case 'a': val='align'; break;
                case 'it': val='italic'; break;
                case 'co': val='color'; break;
                case 'h': val='height'; break;
                case 'w': val='width'; break;
                case 'ho': val='horizontal'; break;
                case 'v': val='vertical'; break;
                case 'we': val='weight'; break;
                case 'tr': val='transform'; break;
                case 'ca': val='capitalize'; break;
                case 'lo': val='lowercase'; break;
                case 'u': val='underline'; break;
                case 'bl': val='bold'; break;
                case 'o': val='overline'; break;
                case 'up': val='uppercase'; break;
                case 'strike-through': case 'str': case 'li': 
                    val='line-through'; break;
                case 'fa': val='face'; break;
                case 'fam': val='family'; break;
                case 'aut': val='auto'; break;
                case 'inh': val='inherit'; break;

                case 'default': break;
            }
            
            return val;
        }
        
        yielded.pvcrS = this.formatVal(yielded.pvcrS);
        yielded.ncnvrS = this.formatVal(yielded.ncnvrS);
        
        var _result = [];
        this.result = function(yielded){
            var result = yielded.pcrS
                        +(yielded.pvcrS && yielded.pvcrS!=''?'-'+yielded.pvcrS:'')
                        +':'
                        + (yielded.ncnvrS && yielded.ncnvrS!=''?yielded.ncnvrS:'')
                        + (yielded.uvrS && yielded.uvrS!=''?yielded.uvrS:'')
                        +';'
            return result;
        };
        
        if(yielded.pvcrS == 'horizontal'){
            var l = ['left','right'];
            for(var i=0;i<l.length;i++){
                yielded.pvcrS = l[i];       
                _result.push(this.result(yielded));
            }
        }
        else if(yielded.pvcrS == 'vertical'){
            var l = ['top','bottom'];
            for(var i=0;i<l.length;i++){
                yielded.pvcrS = l[i];       
                _result.push(this.result(yielded));
            }
        }
        else {
            _result.push(this.result(yielded));
        }                        
                    
        return _result;
    },

    /* Css Property Objects 
        @rules:
            -    Each one of the 'object' types is a css property equivalent
    */
    property : {
        allParams : function(){
            /*var properties = {'width': null, 'height': null, 'margin': null, 'padding': null, 'font': null, 'text': null, 
                    'float': null, 'clear': null, 'background': null, 'color': null, 'min': null, 'max': null};*/
            var properties = {};
            var r_j_p = rules.jQs.property;
            for(k in r_j_p){
                if(typeof(r_j_p[k])=='object'){
                    properties[k] = rules.jQs.property[k];
                }
            }
            return properties;
        },

        width : {
            /*  RegExp Yield Params
                See rexExpB for params details
            */
            params : [{ 
                "pcrS" : function(){ return "width|w|large|la"; },
                "pvcrS" : function(){ return ""; },
                "ncnvrS" : function(){ return "auto|aut|inherit|inh|[\-\+]{0,1}[0-9\,\.]{0,10}"; }, 
                "uvrS" : function(){ return "em|mm|px|pt|%"; }
            }]
        },
        height : {
            /*  RegExp Yield Params
                See property.width for params details
            */
            params : [{ 
                "pcrS" : function(){ return "height|h|tall|tl"; },
                "pvcrS" : function(){ return ""; },
                "ncnvrS" : function(){ return rules.jQs.property.width.params[0].ncnvrS(); }, 
                "uvrS" : function(){ return rules.jQs.property.width.params[0].uvrS(); }
            }]
        },
        margin : {
            /*  RegExp Yield Params
                See property.width for params details
            */
            params : [{ 
                "pcrS" : function(){ return "margin|marg|m"; },
                "pvcrS" : function(){ return "left|l|right|r|top|t|bottom|b|horizontal|ho|vertical|v|all"; },
                "ncnvrS" : function(){ return rules.jQs.property.width.params[0].ncnvrS(); }, 
                "uvrS" : function(){ return rules.jQs.property.width.params[0].uvrS(); }
            }]
        },
        padding : {
            /*  RegExp Yield Params
                See property.width for params details
            */
            params : [{ 
                "pcrS" : function(){ return "padding|pad|p"; },
                "pvcrS" : function(){ return rules.jQs.property.margin.params[0].pvcrS(); }, 
                "ncnvrS" : function(){ return rules.jQs.property.width.params[0].ncnvrS(); }, 
                "uvrS" : function(){ return rules.jQs.property.width.params[0].uvrS(); }
            }]
        },
        border : {
            /*  RegExp Yield Params
                See property.width for params details
            */
            params : [{ 
                "pcrS" : function(){ return "border|bord|bor"; },
                "pvcrS" : function(){ return rules.jQs.property.margin.params[0].pvcrS(); }, 
                "ncnvrS" : function(){ return "none|no|auto|aut|inherit|inh"; }, 
                "uvrS" : function(){ return ""; }
            }]
        },
        outline : {
            /*  RegExp Yield Params
                See property.width for params details
            */
            params : [{ 
                "pcrS" : function(){ return "outline|out|ou"; },
                "pvcrS" : function(){ return rules.jQs.property.margin.params[0].pvcrS(); }, 
                "ncnvrS" : function(){ return rules.jQs.property.border.params[0].ncnvrS(); }, 
                "uvrS" : function(){ return ""; }
            }]
        },
        font : {
            /*  RegExp Yield Params
                See property.width for params details
            */
            params : [{ 
                "pcrS" : function(){ return "font|f"; },
                "pvcrS" : function(){ return "style|st|weight|we|family|fam|face|fa"; },
                "ncnvrS" : function(){ return "[A-Za-z, ]{0,20}"; }, 
                "uvrS" : function(){ return ""; }
            },{ 
                "pcrS" : function(){ return "font|f"; },
                "pvcrS" : function(){ return "size|s"; },
                "ncnvrS" : function(){ return rules.jQs.property.width.params[0].ncnvrS(); }, 
                "uvrS" : function(){ return rules.jQs.property.width.params[0].uvrS(); }
            }]
        },
        text : {
            /*  RegExp Yield Params
                See property.width for params details
            */
            params : [{ 
                "pcrS" : function(){ return "text|t"; },
                "pvcrS" : function(){ return "decoration|d|align|a|tranform|tr|"; },
                "ncnvrS" : function(){ return "[A-Za-z]{0,10}"; }, //"overline|o|underline|u|uppercase|up|capitalize|ca|left|l|right|r|center|c|justify|j"; } 
                "uvrS" : function(){ return ""; }
            },{ 
                "pcrS" : function(){ return "text|t"; },
                "pvcrS" : function(){ return "indent|i"; },
                "ncnvrS" : function(){ return rules.jQs.property.width.params[0].ncnvrS(); }, 
                "uvrS" : function(){ return rules.jQs.property.width.params[0].uvrS(); }
            }]
        },
        float : {
            /*  RegExp Yield Params
                See property.width for params details
            */
            params : [{ 
                "pcrS" : function(){ return "float|fl"; },
                "pvcrS" : function(){ return ""; },
                "ncnvrS" : function(){ return "left|l|right|r|none|no"; },
                "uvrS" : function(){ return ""; }
            }]
        },
        clear : {
            /*  RegExp Yield Params
                See property.width for params details
            */
            params : [{ 
                "pcrS" : function(){ return "clear|c"; },
                "pvcrS" : function(){ return ""; },
                "ncnvrS" : function(){ return "left|l|right|r|both|bo|none|no"; },
                "uvrS" : function(){ return ""; }
            }]
        },
        background : {
            /*  RegExp Yield Params
                See property.width for params details
            */
            params : [{ 
                "pcrS" : function(){ return "background|b"; },
                "pvcrS" : function(){ return "color|co"; },
                /* eventually (needs correction): |RGB{1}\\([0-255\\,]{3}\\) */
                "ncnvrS" : function(){ return "#[A-Fa-f0-9]{6}|[A-Za-z0-9]{1,20}"; }, 
                "uvrS" : function(){ return ""; }
            }]
        },
        color : {
            /*  RegExp Yield Params
                See property.width for params details
            */
            params : [{ 
                "pcrS" : function(){ return "color|co"; },
                "pvcrS" : function(){ return ""; },
                "ncnvrS" : function(){ return rules.jQs.property.background.params[0].ncnvrS(); }, 
                "uvrS" : function(){ return ""; }
            }]
        },
        display : {
            /*  RegExp Yield Params
                See property.width for params details
            */
            params : [{ 
                "pcrS" : function(){ return "display|disp|di"; },
                "pvcrS" : function(){ return ""; },
                "ncnvrS" : function(){ return "inline|inl|block|blo|none|no"; }, 
                "uvrS" : function(){ return ""; }
            }]
        },
        position : {
            /*  RegExp Yield Params
                See property.width for params details
            */
            params : [{ 
                "pcrS" : function(){ return "po|pos|position"; },
                "pvcrS" : function(){ return ""; },
                "ncnvrS" : function(){ return "r|rel|relative|abs|absolute"; },
                "uvrS" : function(){ return ""; }
            }]
        },
        min : {
            /*  RegExp Yield Params
                See property.width for params details
            */
            params : [{ 
                "pcrS" : function(){ return "min|mi"; },
                "pvcrS" : function(){ return "width|w|height|h"; },
                "ncnvrS" : function(){ return rules.jQs.property.width.params[0].ncnvrS(); }, 
                "uvrS" : function(){ return rules.jQs.property.width.params[0].uvrS(); }
            }]
        },
        max : {
            /*  RegExp Yield Params
                See property.width for params details
            */
            params : [{ 
                "pcrS" : function(){ return "max|ma"; },
                "pvcrS" : function(){ return rules.jQs.property.min.params[0].pvcrS(); }, 
                "ncnvrS" : function(){ return rules.jQs.property.width.params[0].ncnvrS(); }, 
                "uvrS" : function(){ return rules.jQs.property.width.params[0].uvrS(); }
            }]
        }
    },

    /*  For Documentation and reference only
        Not used.
    */
    regExp_o : [
        [new RegExp("(width|w|large)([0-9].)(em|mm|px|pt|%)[^\s]"),'width'],
        [new RegExp("(height|h|long)([0-9].)(em|mm|px|pt|%)[^\s]"),'height'],
        [new RegExp("(margin-left|margin-l|marg-l|margl|ml|left,l)([0-9].)(em|mm|px|pt|%)[^\s]"),'margin-left'],
        [new RegExp("(margin-right|margin-r|marg-r|margr|mr|right,r)([0-9].)(em|mm|px|pt|%)[^\s]"),'margin-right'],
        [new RegExp("(margin-top|margin-top|marg-t|margt|mt|top,t)([0-9].)(em|mm|px|pt|%)[^\s]"),'margin-top'],
        [new RegExp("(margin-bottom|margin-b|marg-b|margb|b|bottom,b)([0-9].)(em|mm|px|pt|%)[^\s]"),'margin-bottom'],
        [new RegExp("(padding-left|padding-l|pad-l|padl|pleft|pl)([0-9].)(em|mm|px|pt|%)[^\s]"),'padding-left'],
        [new RegExp("(padding-right|padding-r|pad-r|padr|pright|pr)([0-9].)(em|mm|px|pt|%)[^\s]"),'padding-right'],
        [new RegExp("(padding-top|padding-t|padt|pad-t|ptop|pt)([0-9].)(em|mm|px|pt|%)[^\s]"),'padding-top'],
        [new RegExp("(padding-bottom|padding-b|pad-b|padb|pbottom|pb)([0-9].)(em|mm|px|pt|%)[^\s]"),'padding-bottom'],
        [new RegExp("(font-size|font-s|f-s|fonts|fs)([0-9].)(em|mm|px|pt|%)[^\s]"),'font-size'],
        [new RegExp("(text-indent|text-i|texti|ti)([0-9].)(em|mm|px|pt|%)[^\s]"),'text-indent'],
        [new RegExp("(float|f)\-{0,1}[left|right|none]([1-Za-z]{0,10})[^\s]"),'float'],
        [new RegExp("(clear|cl)\-{0,1}[left|right|both|none]([1-Za-z]{0,10})[^\s]"),'clear'],

        [new RegExp("(bold|b)[^\s]"),'bold'],
        [new RegExp("(italic|i)[^\s]"),'iitalic'],
        [new RegExp("(text-decoration|text-d|t-d,td)([A-Za-z]{1,20})[^\s]"),'text-decoration'],
        [new RegExp("(text-align|text-a|t-a|ta)([A-Za-z]{1,20})[^\s]"),'text-align'],
        [new RegExp("(font-color|font-c|f-c|fc|color|c)(^\#[A-Za-z]{6}|^[rgb|RGB]\([0-255\,]{3}\)[A-Za-z]{1,20})[^\s]"),'font-color'],
        [new RegExp("(background-color|background-c|b-c|bc)(^\#[A-Za-z]{6}|^[rgb|RGB]\([0-255\,]{3}\)[A-Za-z]{1,20})[^\s]"),'background-color']
    ]
};

/* on document ready... */
$(document).ready(function(){
    rules.jQs.onDocumentReady();    
});
